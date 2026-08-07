(function () {
  "use strict";

  const PATH_LABELS = {
    maintenance: "生物维护",
    reconstruction: "生物重建",
    suspension: "生物暂停",
    digital_migration: "数字迁移",
    cognitive_extension: "认知外延",
    social_composite: "社会复合",
    philosophical: "哲学判据",
    cross_path: "跨路径"
  };

  const EVENT_TYPE_LABELS = {
    myth: "神话与宗教",
    religious: "宗教",
    thought: "思想与概念",
    practice: "实践与方法",
    technology: "技术与工程",
    institution: "制度与机构",
    literature: "文学与作品",
    failure: "失败与教训",
    demographic: "人口与统计",
    policy: "政策与治理"
  };

  const TIME_WINDOWS = {
    all: null,
    ancient: [-4000, -1],
    classical: [0, 500],
    medieval: [501, 1500],
    modern: [1501, 1900],
    twentieth: [1901, 2000],
    twentyfirst: [2001, 2100]
  };

  const params = new URLSearchParams(window.location.search);
  const state = {
    q: params.get("q") || "",
    scope: params.get("scope") || "all",
    period: params.get("period") || "",
    path: params.get("path") || "",
    type: params.get("type") || "",
    evidence: params.get("evidence") || "",
    mode: params.get("mode") || "path",
    window: params.get("window") || "all"
  };

  let events = [];
  let filtered = [];
  let currentIndex = -1;
  let chart = null;

  const chartEl = document.getElementById("chart");
  const chartStatusEl = document.getElementById("chart-status");
  const countEl = document.getElementById("result-count");
  const detailEl = document.getElementById("event-detail");
  const detailEmptyEl = document.getElementById("event-detail-empty");
  const detailMetaEl = document.getElementById("event-detail-meta");
  const detailTextEl = document.getElementById("event-detail-text");
  const navIndexEl = document.getElementById("event-nav-index");

  function esc(value) {
    return String(value == null ? "" : value).replace(/[&<>"']/g, function (ch) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch];
    });
  }

  function dateLabel(event) {
    const start = event.start_date || {};
    let label = start.year != null ? String(start.year) : "";
    if (start.month != null) label += "-" + String(start.month).padStart(2, "0");
    if (start.day != null) label += "-" + String(start.day).padStart(2, "0");
    return label;
  }

  function unique(values) {
    return Array.from(new Set(values.filter(Boolean))).sort(function (a, b) {
      return String(a).localeCompare(String(b), "zh-Hans-CN");
    });
  }

  function fillSelect(select, values, label, display) {
    select.innerHTML = "<option value=\"\">" + label + "</option>" + values.map(function (v) {
      return "<option value=\"" + esc(v) + "\">" + esc(display ? display(v) : v) + "</option>";
    }).join("");
  }

  function fillPairSelect(select, pairs, label) {
    select.innerHTML = "<option value=\"\">" + label + "</option>" + pairs.map(function (pair) {
      return "<option value=\"" + esc(pair.value) + "\">" + esc(pair.label) + "</option>";
    }).join("");
  }

  function plainText(event) {
    const meta = event.meta || {};
    return [
      event.text && event.text.headline,
      event.text && event.text.text ? event.text.text.replace(/<[^>]*>/g, " ") : "",
      meta.event_id,
      meta.period_label,
      meta.path_family,
      meta.event_type,
      meta.evidence_grade
    ].join(" ").toLowerCase();
  }

  function matches(event) {
    const meta = event.meta || {};
    const year = event.start_date && event.start_date.year != null ? event.start_date.year : 0;
    const windowRange = TIME_WINDOWS[state.window] || null;
    if (windowRange && (year < windowRange[0] || year > windowRange[1])) return false;
    if (state.scope === "works" && meta.publication_status !== "selected") return false;
    if (state.scope === "reviewed" && meta.verification_status !== "locally_reviewed") return false;
    if (state.period && meta.period_label !== state.period) return false;
    if (state.path && meta.path_family !== state.path) return false;
    if (state.type && meta.event_type !== state.type) return false;
    if (state.evidence && meta.evidence_grade !== state.evidence) return false;
    if (state.q && plainText(event).indexOf(state.q) < 0) return false;
    return true;
  }

  function filteredEvents() {
    const result = events.filter(matches).slice();
    result.sort(function (a, b) {
      const ay = a.start_date && a.start_date.year != null ? a.start_date.year : 0;
      const by = b.start_date && b.start_date.year != null ? b.start_date.year : 0;
      return ay - by;
    });
    return result;
  }

  function scopeLabel() {
    if (state.scope === "works") return "作品子集";
    if (state.scope === "reviewed") return "本地已复核";
    return "全部资料";
  }

  function updateCountAndStatus() {
    countEl.textContent = filtered.length + " 条匹配 · " + scopeLabel();
    const windowLabel = document.getElementById("window").selectedOptions.length
      ? document.getElementById("window").selectedOptions[0].textContent
      : "全部时间";
    chartStatusEl.textContent = "当前范围：" + scopeLabel() + "；时间窗口：" + windowLabel +
      "；图表为增强视图，核心数据见表格和原始 JSON。";
  }

  function densityOption() {
    const binSize = 100;
    const years = filtered.map(function (event) {
      return event.start_date && event.start_date.year != null ? event.start_date.year : 0;
    });
    if (!years.length) {
      return {
        animation: false,
        xAxis: { type: "category", data: [] },
        yAxis: { type: "value", name: "事件数" },
        series: [{ type: "bar", data: [] }]
      };
    }
    const minYear = Math.floor(Math.min.apply(null, years) / binSize) * binSize;
    const maxYear = Math.ceil(Math.max.apply(null, years) / binSize) * binSize;
    const bins = [];
    const counts = {};
    for (let start = minYear; start < maxYear; start += binSize) {
      const key = start;
      bins.push(key);
      counts[key] = 0;
    }
    years.forEach(function (year) {
      const key = Math.floor(year / binSize) * binSize;
      if (counts[key] != null) counts[key] += 1;
    });
    return {
      animation: false,
      tooltip: {
        trigger: "axis",
        formatter: function (params) {
          const item = params[0] || {};
          const key = item.value != null ? bins[item.dataIndex] : null;
          if (key == null) return "";
          return key + "~" + (key + binSize) + " 年：" + item.value + " 条事件";
        }
      },
      grid: { left: 70, right: 40, top: 40, bottom: 90 },
      xAxis: {
        type: "category",
        name: "年代",
        nameLocation: "middle",
        nameGap: 45,
        data: bins.map(function (key) { return key + "~" + (key + binSize); })
      },
      yAxis: { type: "value", name: "事件数" },
      dataZoom: [
        { type: "inside", xAxisIndex: 0, start: 0, end: 100 },
        { type: "slider", xAxisIndex: 0, bottom: 16, start: 0, end: 100 }
      ],
      series: [{
        type: "bar",
        data: bins.map(function (key) {
          return {
            value: counts[key],
            label: key + "~" + (key + binSize)
          };
        })
      }]
    };
  }

  function scatterOption() {
    const pathLabels = unique(filtered.map(function (event) {
      return event.meta && event.meta.path_family_label;
    }));
    const pathIndex = {};
    pathLabels.forEach(function (label, index) { pathIndex[label] = index; });
    const points = filtered.map(function (event, index) {
      const meta = event.meta || {};
      const year = event.start_date && event.start_date.year != null ? event.start_date.year : 0;
      return {
        value: [year, pathIndex[meta.path_family_label] || 0],
        title: event.text && event.text.headline ? event.text.headline : "",
        dateLabel: dateLabel(event),
        meta: meta,
        _idx: index
      };
    });
    return {
      animation: false,
      tooltip: {
        trigger: "item",
        formatter: function (params) {
          const item = params.data || {};
          const meta = item.meta || {};
          return "<strong>" + esc(item.title || "") + "</strong><br>" +
            "日期：" + esc(item.dateLabel || (params.value ? params.value[0] : "?")) + "<br>" +
            "时期：" + esc(meta.period_label || "") + "<br>" +
            "路径：" + esc(meta.path_family_label || meta.path_family || "") + "<br>" +
            "类型：" + esc(meta.event_type_label || meta.event_type || "") + "<br>" +
            "证据：" + esc(meta.evidence_grade || "") + " / " + esc(meta.verification_status || "") + "<br>" +
            "编号：" + esc(meta.event_id || "") + "<br>" +
            "来源：" + (meta.source_links || "无");
        }
      },
      grid: { left: 140, right: 40, top: 40, bottom: 90 },
      xAxis: {
        type: "value",
        name: "年份",
        nameLocation: "middle",
        nameGap: 45,
        min: "dataMin",
        max: "dataMax"
      },
      yAxis: { type: "category", data: pathLabels },
      dataZoom: [
        { type: "inside", xAxisIndex: 0, start: 0, end: 100 },
        { type: "slider", xAxisIndex: 0, bottom: 16, start: 0, end: 100 }
      ],
      series: [{
        type: "scatter",
        symbolSize: 7,
        data: points
      }]
    };
  }

  function showDetail(index) {
    if (!filtered.length || index < 0 || index >= filtered.length) {
      currentIndex = -1;
      detailEmptyEl.hidden = false;
      detailMetaEl.replaceChildren();
      detailTextEl.replaceChildren();
      navIndexEl.textContent = "";
      return;
    }
    currentIndex = index;
    const event = filtered[index];
    const meta = event.meta || {};
    detailEmptyEl.hidden = true;
    detailMetaEl.innerHTML =
      "<dt>标题</dt><dd>" + esc(event.text && event.text.headline) + "</dd>" +
      "<dt>编号</dt><dd>" + esc(meta.event_id || "") + "</dd>" +
      "<dt>日期</dt><dd>" + esc(dateLabel(event)) + "</dd>" +
      "<dt>时期</dt><dd>" + esc(meta.period_label || "") + "</dd>" +
      "<dt>路径</dt><dd>" + esc(meta.path_family_label || meta.path_family || "") + "</dd>" +
      "<dt>类型</dt><dd>" + esc(meta.event_type_label || meta.event_type || "") + "</dd>" +
      "<dt>证据</dt><dd>" + esc(meta.evidence_grade || "") + " / " + esc(meta.verification_status || "") + "</dd>" +
      "<dt>作品化</dt><dd>" + (meta.publication_status === "selected" ? "作品子集" : "候选资料") + "</dd>" +
      "<dt>来源</dt><dd>" + (meta.source_links || "无") + "</dd>";
    detailTextEl.innerHTML = event.text && event.text.text ? event.text.text : "";
    navIndexEl.textContent = (index + 1) + " / " + filtered.length;
  }

  function moveEvent(delta) {
    if (!filtered.length) return;
    if (currentIndex < 0) {
      currentIndex = delta > 0 ? 0 : filtered.length - 1;
    } else {
      currentIndex = (currentIndex + delta + filtered.length) % filtered.length;
    }
    showDetail(currentIndex);
  }

  function render() {
    filtered = filteredEvents();
    updateCountAndStatus();
    if (!filtered.length) {
      if (chart) chart.setOption({ series: [] }, true);
      showDetail(-1);
      return;
    }
    if (typeof window.echarts === "undefined") {
      chartEl.replaceChildren(document.createTextNode("ECharts 未加载，请检查网络后刷新；核心数据仍可直接读取下方表格和原始 JSON。"));
      showDetail(-1);
      return;
    }
    if (!chart) {
      chart = window.echarts.init(chartEl, null, {
        width: Math.max(900, Math.min(window.innerWidth - 40, 1400)),
        height: 560
      });
      chart.on("click", function (params) {
        if (params.data && typeof params.data._idx === "number") {
          showDetail(params.data._idx);
        }
      });
    }
    chart.setOption(state.mode === "density" ? densityOption() : scatterOption(), true);
    chart.resize();
    if (currentIndex < 0 || !filtered[currentIndex]) {
      showDetail(filtered.length ? 0 : -1);
    } else {
      showDetail(currentIndex);
    }
  }

  function bindControls() {
    function bind(id, key, eventName) {
      document.getElementById(id).addEventListener(eventName, function (event) {
        state[key] = event.target.value;
        render();
      });
    }
    document.getElementById("q").addEventListener("input", function (event) {
      state.q = event.target.value;
      render();
    });
    bind("scope", "scope", "change");
    bind("period", "period", "change");
    bind("path", "path", "change");
    bind("type", "type", "change");
    bind("evidence", "evidence", "change");
    bind("mode", "mode", "change");
    bind("window", "window", "change");
    document.getElementById("prev-event").addEventListener("click", function () {
      moveEvent(-1);
    });
    document.getElementById("next-event").addEventListener("click", function () {
      moveEvent(1);
    });
    document.addEventListener("keydown", function (event) {
      const tag = event.target && event.target.tagName;
      if (tag === "INPUT" || tag === "SELECT" || tag === "TEXTAREA") return;
      if (event.key === "ArrowLeft") moveEvent(-1);
      if (event.key === "ArrowRight") moveEvent(1);
    });
    window.addEventListener("resize", function () {
      if (chart) chart.resize();
    });
  }

  function initSelects() {
    fillSelect(
      document.getElementById("period"),
      unique(events.map(function (event) { return event.meta && event.meta.period_label; })),
      "全部时期"
    );
    const pathPairs = unique(events.map(function (event) { return event.meta && event.meta.path_family; }))
      .map(function (value) {
        return {
          value: value,
          label: PATH_LABELS[value] || value
        };
      });
    fillPairSelect(document.getElementById("path"), pathPairs, "全部路径");
    const typePairs = unique(events.map(function (event) { return event.meta && event.meta.event_type; }))
      .map(function (value) {
        return {
          value: value,
          label: EVENT_TYPE_LABELS[value] || value
        };
      });
    fillPairSelect(document.getElementById("type"), typePairs, "全部类型");
    fillSelect(
      document.getElementById("evidence"),
      unique(events.map(function (event) { return event.meta && event.meta.evidence_grade; })),
      "全部证据等级"
    );

    document.getElementById("q").value = state.q;
    document.getElementById("scope").value = state.scope;
    document.getElementById("period").value = state.period;
    document.getElementById("path").value = state.path;
    document.getElementById("type").value = state.type;
    document.getElementById("evidence").value = state.evidence;
    document.getElementById("mode").value = state.mode;
    document.getElementById("window").value = state.window;
  }

  async function load() {
    chartStatusEl.textContent = "正在加载 timelinejs.json ...";
    try {
      const response = await fetch("timelinejs.json");
      if (!response.ok) throw new Error("HTTP " + response.status);
      const data = await response.json();
      events = data.events || [];
      initSelects();
      bindControls();
      render();
    } catch (error) {
      chartStatusEl.textContent = "无法加载 timelinejs.json：" + error.message +
        "；可直接打开 timeline.json 或 timeline-events.psql.txt 阅读原始资料。";
    }
  }

  load();
})();
