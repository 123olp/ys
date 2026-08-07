(function () {
  "use strict";

  const Core = window.HumanInfraTimelineCore;
  const {
    TIME_WINDOWS,
    esc,
    dateLabel,
    displayWidth,
    padEnd,
    psqlTable,
    renderPsqlTable,
    eventRow,
    unique,
    matchesEvent
  } = Core;

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

  const EVIDENCE_COLORS = {
    T: "#2f7d4f",
    I: "#4c6fbf",
    M: "#b0763b",
    S: "#8a6d3b",
    L: "#7b4f9e"
  };

  const PREFERRED_EVENT_ID = "HIT-TEC-001";

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
  let currentEventId = params.get("event") || "";
  let highlightedDataIndex = -1;
  let chart = null;
  let fullEventsPromise = null;
  let fullTableRenderToken = 0;
  let densityCache = null;

  const chartEl = document.getElementById("chart");
  const chartStatusEl = document.getElementById("chart-status");
  const countEl = document.getElementById("result-count");
  const detailEmptyEl = document.getElementById("event-detail-empty");
  const detailTableCodeEl = document.getElementById("event-detail-table-code");
  const detailTextEl = document.getElementById("event-detail-text");
  const navIndexEl = document.getElementById("event-nav-index");
  const fullEventTableCodeEl = document.getElementById("full-event-table-code");
  const loadFullEventBtn = document.getElementById("load-full-event");

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

  const matches = function (event) {
    return matchesEvent(event, state);
  };

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

  function urlParams() {
    const next = new URLSearchParams();
    if (state.q) next.set("q", state.q);
    if (state.scope && state.scope !== "all") next.set("scope", state.scope);
    if (state.period) next.set("period", state.period);
    if (state.path) next.set("path", state.path);
    if (state.type) next.set("type", state.type);
    if (state.evidence) next.set("evidence", state.evidence);
    if (state.mode && state.mode !== "path") next.set("mode", state.mode);
    if (state.window && state.window !== "all") next.set("window", state.window);
    if (currentEventId) next.set("event", currentEventId);
    return next;
  }

  function syncUrl(mode) {
    const query = urlParams().toString();
    const url = "preview.html" + (query ? "?" + query : "");
    if (mode === "replace") {
      history.replaceState(null, "", url);
    } else {
      history.pushState(null, "", url);
    }
  }

  function ensureFullEvents() {
    if (!fullEventsPromise) {
      fullEventsPromise = fetch("timelinejs.json").then(function (response) {
        if (!response.ok) throw new Error("HTTP " + response.status);
        return response.json();
      }).then(function (data) {
        const byId = new Map();
        (data.events || []).forEach(function (event) {
          byId.set(event.meta && event.meta.event_id, event);
        });
        return byId;
      });
    }
    return fullEventsPromise;
  }

  function loadFullDetail(index) {
    const event = filtered[index];
    if (!event) return;
    if (event.text && event.text.text) {
      detailTextEl.innerHTML = event.text.text;
      loadFullEventBtn.hidden = true;
      return;
    }
    detailTextEl.textContent = "正在加载完整事件…";
    ensureFullEvents().then(function (byId) {
      if (currentIndex !== index) return;
      const full = byId.get(filtered[index].meta.event_id);
      detailTextEl.innerHTML = full && full.text && full.text.text ? full.text.text : "";
      loadFullEventBtn.hidden = true;
    }).catch(function (error) {
      if (currentIndex !== index) return;
      detailTextEl.textContent = "完整事件加载失败：" + error.message;
      loadFullEventBtn.hidden = false;
    });
  }

  function ensureCurrentPointVisible() {
    if (!chart || state.mode !== "path" || currentIndex < 0 || filtered.length < 2) return;
    const zoom = chart.getOption().dataZoom && chart.getOption().dataZoom[0];
    if (!zoom || (zoom.start <= 0 && zoom.end >= 100)) return;
    const year = filtered[currentIndex].start_date && filtered[currentIndex].start_date.year;
    if (year == null) return;
    const minYear = filtered[0].start_date && filtered[0].start_date.year != null
      ? filtered[0].start_date.year
      : 0;
    const maxYear = filtered[filtered.length - 1].start_date && filtered[filtered.length - 1].start_date.year != null
      ? filtered[filtered.length - 1].start_date.year
      : 0;
    const span = maxYear - minYear || 1;
    const center = (year - minYear) / span * 100;
    let windowSize = zoom.end - zoom.start;
    if (!windowSize || windowSize <= 0) windowSize = 20;
    let start = center - windowSize / 2;
    let end = center + windowSize / 2;
    if (start < 0) {
      end -= start;
      start = 0;
    }
    if (end > 100) {
      start -= end - 100;
      end = 100;
    }
    if (start < 0) start = 0;
    chart.dispatchAction({ type: "dataZoom", dataZoomIndex: 0, start: start, end: end });
  }

  function clearChartHighlight() {
    if (!chart || state.mode !== "path" || highlightedDataIndex < 0) return;
    chart.dispatchAction({ type: "downplay", seriesIndex: 0, dataIndex: highlightedDataIndex });
    chart.dispatchAction({ type: "hideTip" });
    highlightedDataIndex = -1;
  }

  function syncChartHighlight() {
    if (!chart) return;
    if (state.mode === "density") {
      chart.setOption(densityOption(), false);
      return;
    }
    if (currentIndex < 0) {
      clearChartHighlight();
      return;
    }
    if (highlightedDataIndex >= 0 && highlightedDataIndex !== currentIndex) {
      chart.dispatchAction({ type: "downplay", seriesIndex: 0, dataIndex: highlightedDataIndex });
    }
    ensureCurrentPointVisible();
    chart.dispatchAction({ type: "highlight", seriesIndex: 0, dataIndex: currentIndex });
    chart.dispatchAction({
      type: "showTip",
      seriesIndex: 0,
      dataIndex: currentIndex,
      name: currentEventId
    });
    highlightedDataIndex = currentIndex;
  }

  function getDensityCache() {
    if (densityCache && densityCache.filtered === filtered) return densityCache;
    const binSize = 100;
    const years = filtered.map(function (event) {
      return event.start_date && event.start_date.year != null ? event.start_date.year : 0;
    });
    if (!years.length) return null;
    const minYear = Math.floor(Math.min.apply(null, years) / binSize) * binSize;
    const maxYear = Math.ceil(Math.max.apply(null, years) / binSize) * binSize;
    const bins = [];
    const counts = {};
    const binIndices = {};
    for (let start = minYear; start < maxYear; start += binSize) {
      const key = start;
      bins.push(key);
      counts[key] = 0;
      binIndices[key] = [];
    }
    years.forEach(function (year, index) {
      const key = Math.floor(year / binSize) * binSize;
      if (counts[key] != null) {
        counts[key] += 1;
        binIndices[key].push(index);
      }
    });
    densityCache = { filtered, binSize, minYear, maxYear, bins, counts, binIndices };
    return densityCache;
  }

  function densityOption() {
    const cache = getDensityCache();
    if (!cache) {
      return {
        animation: false,
        xAxis: { type: "category", data: [] },
        yAxis: { type: "value", name: "事件数" },
        series: [{ type: "bar", data: [] }]
      };
    }
    const { binSize, bins, counts, binIndices } = cache;
    let currentBinIndex = -1;
    if (currentIndex >= 0 && filtered[currentIndex].start_date) {
      const currentYear = filtered[currentIndex].start_date.year;
      if (currentYear != null) {
        currentBinIndex = bins.indexOf(Math.floor(currentYear / binSize) * binSize);
      }
    }
    return {
      animation: false,
      tooltip: {
        trigger: "axis",
        confine: true,
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
            label: key + "~" + (key + binSize),
            _indices: binIndices[key]
          };
        }),
        markLine: currentBinIndex >= 0 ? {
          symbol: "none",
          label: {
            formatter: "当前事件",
            position: "insideEndTop"
          },
          lineStyle: { color: "#c0392b" },
          data: [{ xAxis: currentBinIndex }]
        } : undefined
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
        _idx: index,
        symbolSize: index === currentIndex ? 14 : 7
      };
    });
    return {
      animation: false,
      tooltip: {
        trigger: "item",
        confine: true,
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
            "来源：" + esc((meta.source_refs || []).join(", ") || "无");
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
      series: [
        {
          type: "scatter",
          progressive: 1000,
          z: 2,
          itemStyle: {
            color: function (params) {
              const grade = params.data && params.data.meta && params.data.meta.evidence_grade;
              return EVIDENCE_COLORS[grade] || "#5470c6";
            }
          },
          data: points
        },
        currentIndex >= 0 ? {
          type: "scatter",
          symbolSize: 24,
          silent: true,
          z: 3,
          tooltip: { show: false },
          itemStyle: {
            color: "transparent",
            borderColor: "#c0392b",
            borderWidth: 2
          },
          data: [points[currentIndex]]
        } : undefined
      ].filter(Boolean)
    };
  }

  function showDetail(index) {
    if (!filtered.length || index < 0 || index >= filtered.length) {
      currentIndex = -1;
      currentEventId = "";
      detailEmptyEl.hidden = false;
      detailTableCodeEl.textContent = "";
      detailTextEl.replaceChildren();
      navIndexEl.textContent = "";
      loadFullEventBtn.hidden = true;
      chartEl.setAttribute("aria-label", "永生年表事件时间轴图表");
      clearChartHighlight();
      return;
    }
    currentIndex = index;
    const event = filtered[index];
    const meta = event.meta || {};
    currentEventId = meta.event_id || "";
    detailEmptyEl.hidden = true;
    detailTableCodeEl.textContent = psqlTable(
      ["标题", "编号", "日期", "时期", "路径", "类型", "证据", "作品化", "来源"],
      [eventRow(event)]
    );
    navIndexEl.textContent = (index + 1) + " / " + filtered.length;
    chartEl.setAttribute(
      "aria-label",
      "永生年表事件时间轴图表，当前事件：" + (event.text && event.text.headline || meta.event_id || "")
    );
    if (event.text && event.text.text) {
      detailTextEl.innerHTML = event.text.text;
      loadFullEventBtn.hidden = true;
    } else {
      detailTextEl.textContent = "";
      loadFullEventBtn.hidden = false;
    }
    syncChartHighlight();
  }

  function moveEvent(delta) {
    if (!filtered.length) return;
    if (currentIndex < 0) {
      currentIndex = delta > 0 ? 0 : filtered.length - 1;
    } else {
      currentIndex = (currentIndex + delta + filtered.length) % filtered.length;
    }
    showDetail(currentIndex);
    syncUrl("replace");
  }

  function setCodeText(id, text) {
    const element = document.getElementById(id);
    if (element && element.firstElementChild) {
      element.firstElementChild.textContent = text;
    }
  }

  function updateAggregates() {
    const pathStats = {};
    const typeStats = {};
    const statusCounts = {};
    let worksCount = 0;
    let reviewedCount = 0;
    filtered.forEach(function (event) {
      const meta = event.meta || {};
      const path = meta.path_family || "unknown";
      const type = meta.event_type || "unknown";
      const status = meta.verification_status || "unknown";
      if (!pathStats[path]) pathStats[path] = [0, 0, 0];
      if (!typeStats[type]) typeStats[type] = [0, 0, 0];
      pathStats[path][0] += 1;
      typeStats[type][0] += 1;
      statusCounts[status] = (statusCounts[status] || 0) + 1;
      if (meta.publication_status === "selected") {
        pathStats[path][1] += 1;
        typeStats[type][1] += 1;
        worksCount += 1;
      }
      if (meta.verification_status === "locally_reviewed") {
        pathStats[path][2] += 1;
        typeStats[type][2] += 1;
        reviewedCount += 1;
      }
    });

    const pathRows = Object.keys(pathStats).map(function (path) {
      return [PATH_LABELS[path] || path].concat(pathStats[path]);
    });
    pathRows.sort(function (a, b) { return b[1] - a[1]; });
    pathRows.push(["合计", filtered.length, worksCount, reviewedCount]);
    setCodeText(
      "path-summary-table",
      renderPsqlTable(["路径族", "全部资料", "作品子集", "本地已复核"], pathRows)
    );

    const typeRows = Object.keys(typeStats).map(function (type) {
      return [EVENT_TYPE_LABELS[type] || type].concat(typeStats[type]);
    });
    typeRows.sort(function (a, b) { return b[1] - a[1]; });
    typeRows.push(["合计", filtered.length, worksCount, reviewedCount]);
    setCodeText(
      "type-summary-table",
      renderPsqlTable(["事件类型", "全部资料", "作品子集", "本地已复核"], typeRows)
    );

    setCodeText(
      "scope-summary-table",
      renderPsqlTable(
        ["范围", "事件数"],
        [
          ["全部资料", filtered.length],
          ["作品子集", worksCount],
          ["本地已复核", reviewedCount]
        ]
      )
    );
    const statusRows = Object.keys(statusCounts).sort(function (a, b) {
      return statusCounts[b] - statusCounts[a];
    }).map(function (status) {
      return [status, statusCounts[status]];
    });
    setCodeText(
      "status-summary-table",
      renderPsqlTable(["复核状态", "事件数"], statusRows)
    );

    const reviewedRows = filtered.filter(function (event) {
      return event.meta && event.meta.verification_status === "locally_reviewed";
    }).map(eventRow);
    setCodeText("reviewed-summary-table", renderPsqlTable(
      ["标题", "编号", "日期", "时期", "路径", "类型", "证据", "作品化", "来源"],
      reviewedRows
    ));

    if (fullEventTableCodeEl) {
      const token = ++fullTableRenderToken;
      fullEventTableCodeEl.textContent = "正在生成完整事件明细…";
      const scheduleIdle = window.requestIdleCallback || function (callback) {
        setTimeout(callback, 0);
      };
      scheduleIdle(function () {
        if (token !== fullTableRenderToken) return;
        fullEventTableCodeEl.textContent = renderPsqlTable(
          ["标题", "编号", "日期", "时期", "路径", "类型", "证据", "作品化", "来源"],
          filtered.map(eventRow)
        );
      });
    }
  }

  function jumpToEvent() {
    const value = String(document.getElementById("event-jump").value || "").trim();
    if (!value) return;
    let index = -1;
    if (/^\d+$/.test(value)) {
      index = Number(value) - 1;
    } else if (value.toUpperCase().indexOf("HIT-") === 0) {
      const needle = value.toUpperCase();
      index = filtered.findIndex(function (event) {
        return (event.meta && event.meta.event_id || "").toUpperCase() === needle;
      });
      if (index < 0) {
        index = filtered.findIndex(function (event) {
          return (event.meta && event.meta.event_id || "").toUpperCase().indexOf(needle) === 0;
        });
      }
    } else {
      const needle = value.toLowerCase();
      index = filtered.findIndex(function (event) {
        return (event.text && event.text.headline || "").toLowerCase().indexOf(needle) >= 0;
      });
    }
    if (index >= 0 && index < filtered.length) {
      showDetail(index);
      syncUrl("replace");
    } else {
      navIndexEl.textContent = "未找到：" + value;
    }
  }

  function resolveCurrentIndex() {
    if (!filtered.length) {
      currentIndex = -1;
      return;
    }
    if (currentEventId) {
      const index = filtered.findIndex(function (event) {
        return event.meta && event.meta.event_id === currentEventId;
      });
      if (index >= 0) {
        currentIndex = index;
        return;
      }
    }
    const preferredIndex = filtered.findIndex(function (event) {
      return event.meta && event.meta.event_id === PREFERRED_EVENT_ID;
    });
    currentIndex = preferredIndex >= 0 ? preferredIndex : 0;
  }

  function render() {
    filtered = filteredEvents();
    resolveCurrentIndex();
    updateCountAndStatus();
    updateAggregates();
    if (!filtered.length) {
      if (chart) chart.setOption({ series: [] }, true);
      showDetail(-1);
      return;
    }
    if (typeof window.echarts === "undefined") {
      chartEl.replaceChildren(document.createTextNode("ECharts 未加载，请确认 echarts.min.js 已随预览目录发布；核心数据仍可直接读取下方表格和原始 JSON。"));
      showDetail(-1);
      return;
    }
    if (!chart) {
      chart = window.echarts.init(chartEl, null, {
        width: Math.max(320, chartEl.clientWidth || window.innerWidth - 40),
        height: 560
      });
      chart.on("click", function (params) {
        const data = params.data || {};
        if (typeof data._idx === "number") {
          showDetail(data._idx);
          syncUrl("replace");
        } else if (data._indices && data._indices.length) {
          showDetail(data._indices[0]);
          syncUrl("replace");
        }
      });
    }
    chart.setOption(state.mode === "density" ? densityOption() : scatterOption(), true);
    chart.resize();
    highlightedDataIndex = -1;
    showDetail(currentIndex);
  }

  function bindControls() {
    function bind(id, key, eventName) {
      document.getElementById(id).addEventListener(eventName, function (event) {
        state[key] = event.target.value;
        render();
        syncUrl("push");
      });
    }
    let qTimer = null;
    document.getElementById("q").addEventListener("input", function (event) {
      state.q = event.target.value;
      clearTimeout(qTimer);
      qTimer = setTimeout(function () {
        render();
        syncUrl("replace");
      }, 300);
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
    document.getElementById("jump-event").addEventListener("click", jumpToEvent);
    document.getElementById("event-jump").addEventListener("keydown", function (event) {
      if (event.key === "Enter") jumpToEvent();
    });
    loadFullEventBtn.addEventListener("click", function () {
      loadFullDetail(currentIndex);
    });
    document.addEventListener("keydown", function (event) {
      const tag = event.target && event.target.tagName;
      if (tag === "INPUT" || tag === "SELECT" || tag === "TEXTAREA") return;
      if (event.key === "ArrowLeft") moveEvent(-1);
      if (event.key === "ArrowRight") moveEvent(1);
    });
    window.addEventListener("popstate", function () {
      clearTimeout(qTimer);
      const nextParams = new URLSearchParams(window.location.search);
      state.q = nextParams.get("q") || "";
      state.scope = nextParams.get("scope") || "all";
      state.period = nextParams.get("period") || "";
      state.path = nextParams.get("path") || "";
      state.type = nextParams.get("type") || "";
      state.evidence = nextParams.get("evidence") || "";
      state.mode = nextParams.get("mode") || "path";
      state.window = nextParams.get("window") || "all";
      currentEventId = nextParams.get("event") || "";
      applyControlValues();
      render();
    });
    window.addEventListener("resize", function () {
      if (chart) chart.resize();
    });
  }

  function applyControlValues() {
    document.getElementById("q").value = state.q;
    document.getElementById("scope").value = state.scope;
    document.getElementById("period").value = state.period;
    document.getElementById("path").value = state.path;
    document.getElementById("type").value = state.type;
    document.getElementById("evidence").value = state.evidence;
    document.getElementById("mode").value = state.mode;
    document.getElementById("window").value = state.window;
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

    applyControlValues();
  }

  function buildSearchText(event) {
    const meta = event.meta || {};
    return [
      event.text && event.text.headline,
      meta.event_id,
      meta.period_label,
      meta.path_family,
      meta.path_family_label,
      meta.event_type,
      meta.event_type_label,
      meta.evidence_grade,
      meta.verification_status,
      meta.publication_status,
      (meta.source_refs || []).join(" ")
    ].join(" ").toLowerCase();
  }

  async function load() {
    chartStatusEl.textContent = "正在加载 timelinejs.light.json ...";
    try {
      const response = await fetch("timelinejs.light.json");
      if (!response.ok) throw new Error("HTTP " + response.status);
      const data = await response.json();
      events = data.events || [];
      events.forEach(function (event) {
        event._searchText = buildSearchText(event);
      });
      initSelects();
      bindControls();
      render();
      syncUrl("replace");
    } catch (error) {
      chartStatusEl.textContent = "无法加载 timelinejs.light.json：" + error.message +
        "；可直接打开 timeline.json 或 timeline-events.psql.txt 阅读原始资料。";
    }
  }

  load();
})();
