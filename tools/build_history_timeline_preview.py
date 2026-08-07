#!/usr/bin/env python3
"""Build timeline publication JSON and a zero-styling semantic preview."""

from __future__ import annotations

import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from tabulate import tabulate


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "docs" / "reference" / "history-timeline"

PATH_LABELS_ZH = {
    "maintenance": "生物维护",
    "reconstruction": "生物重建",
    "suspension": "生物暂停",
    "digital_migration": "数字迁移",
    "cognitive_extension": "认知外延",
    "social_composite": "社会复合",
    "philosophical": "哲学判据",
    "cross_path": "跨路径",
}

EVENT_TYPE_LABELS_ZH = {
    "myth": "神话与宗教",
    "religious": "宗教",
    "thought": "思想与概念",
    "practice": "实践与方法",
    "technology": "技术与工程",
    "institution": "制度与机构",
    "literature": "文学与作品",
    "failure": "失败与教训",
    "demographic": "人口与统计",
    "policy": "政策与治理",
}


def load_json(relative_path: str):
    path = ROOT / relative_path
    return json.loads(path.read_text(encoding="utf-8"))


def parse_year(value: str) -> int | None:
    match = re.match(r"^(-?\d{1,6})", value.strip())
    if not match:
        return None
    return int(match.group(1))


def source_links(source_registry: dict[str, dict], refs: list[str]) -> str:
    parts = []
    for ref in refs:
        source = source_registry.get(ref, {})
        label = source.get("label", ref)
        url = source.get("url", "#")
        parts.append(
            f'<a href="{html.escape(url, quote=True)}" target="_blank" rel="noopener">'
            f"{html.escape(ref)}</a>"
        )
    return " · ".join(parts)


def event_to_timelinejs(
    event: dict,
    source_registry: dict[str, dict],
    period_registry: dict[str, dict],
    works_ids: set[str],
) -> dict:
    start_year = parse_year(event.get("date_start", "")) or 0
    end_year = parse_year(event.get("date_end", "")) if event.get("date_end") else None
    start_date = {"year": start_year}
    if event.get("date_type") == "exact" and event.get("date_start"):
        month_match = re.search(r"-(\d{1,2})-(\d{1,2})$", str(event["date_start"]))
        if month_match:
            start_date["month"] = int(month_match.group(1))
            start_date["day"] = int(month_match.group(2))

    period = period_registry.get(event.get("period_id", ""), {})
    period_label = period.get("label_zh") or period.get("label_en") or event.get("period_id", "")
    event_id = event.get("event_id", "")
    path_family = event.get("path_family", "")
    event_type = event.get("event_type", "")
    path_family_label = PATH_LABELS_ZH.get(path_family, path_family)
    event_type_label = EVENT_TYPE_LABELS_ZH.get(event_type, event_type)
    publication_status = "selected" if event_id in works_ids else "candidate"
    source_refs = event.get("sources", [])
    links = source_links(source_registry, source_refs)
    body_parts = [
        html.escape(event.get("summary", "")),
        "",
        "Claim: " + html.escape(event.get("claim", "")),
        "",
        f"时期: {html.escape(period_label)}",
        f"路径: {html.escape(path_family_label)}",
        f"类型: {html.escape(event_type_label)}",
        f"证据: {html.escape(event.get('evidence_grade', ''))} / "
        f"{html.escape(event.get('verification_status', ''))}",
        "",
        "来源: " + links,
    ]
    item = {
        "start_date": start_date,
        "text": {
            "headline": event.get("title", ""),
            "text": "<br>".join(body_parts),
        },
        "group": event.get("chapter", "未分组"),
        "meta": {
            "event_id": event_id,
            "period_id": event.get("period_id", ""),
            "period_label": period_label,
            "chapter": event.get("chapter", ""),
            "path_family": path_family,
            "path_family_label": path_family_label,
            "event_type": event_type,
            "event_type_label": event_type_label,
            "evidence_grade": event.get("evidence_grade", ""),
            "verification_status": event.get("verification_status", ""),
            "publication_status": publication_status,
            "source_refs": source_refs,
            "source_links": links,
            "status": event.get("status", ""),
            "date_start": event.get("date_start", ""),
        },
    }
    if end_year is not None and event.get("date_type") == "range":
        item["end_date"] = {"year": end_year}
    return item


def build_timelinejs() -> dict:
    timeline = load_json("docs/reference/history-timeline/timeline.json")
    source_registry = {
        source["source_id"]: source
        for source in load_json("docs/reference/history-timeline/sources.json")["sources"]
    }
    period_registry = {
        period["period_id"]: period
        for period in load_json("docs/reference/history-timeline/periods.json")["periods"]
    }
    works_ids = set(
        load_json("docs/reference/history-timeline/works-subset.v1.json")["event_ids"]
    )
    events = [
        event_to_timelinejs(event, source_registry, period_registry, works_ids)
        for event in timeline["events"]
    ]
    events.sort(key=lambda item: item["start_date"]["year"])
    return {
        "title": {
            "text": {
                "headline": "Human Infra 永生史",
                "text": "从神话、宗教与炼金术，到老年科学、健康寿命和生物技术产业的严肃历史年表。",
            }
        },
        "scale": "human",
        "events": events,
    }


def build_path_summary_table(timelinejs: dict) -> str:
    path_stats: dict[str, list[int]] = defaultdict(lambda: [0, 0, 0])
    for event in timelinejs["events"]:
        meta = event.get("meta", {})
        path = meta.get("path_family", "")
        path_stats[path][0] += 1
        if meta.get("publication_status") == "selected":
            path_stats[path][1] += 1
        if meta.get("verification_status") == "locally_reviewed":
            path_stats[path][2] += 1
    rows = [
        [PATH_LABELS_ZH.get(path, path), counts[0], counts[1], counts[2]]
        for path, counts in path_stats.items()
    ]
    rows.sort(key=lambda row: -row[1])
    return tabulate(
        rows,
        headers=["路径族", "全部资料", "作品子集", "本地已复核"],
        tablefmt="psql",
        missingval="",
    )


def build_scope_status_tables(timelinejs: dict) -> tuple[str, str]:
    events = timelinejs["events"]
    verification_counts = Counter(
        event.get("meta", {}).get("verification_status", "") for event in events
    )
    works_count = sum(
        1
        for event in events
        if event.get("meta", {}).get("publication_status") == "selected"
    )
    reviewed_count = verification_counts.get("locally_reviewed", 0)
    scope_table = tabulate(
        [
            ["全部资料", len(events)],
            ["作品子集", works_count],
            ["本地已复核", reviewed_count],
        ],
        headers=["范围", "事件数"],
        tablefmt="psql",
        missingval="",
    )
    status_table = tabulate(
        sorted(verification_counts.items()),
        headers=["复核状态", "事件数"],
        tablefmt="psql",
        missingval="",
    )
    return scope_table, status_table


def build_event_table(events: list[dict]) -> str:
    rows = []
    for event in events:
        meta = event.get("meta", {})
        start_date = event.get("start_date", {})
        rows.append(
            [
                meta.get("event_id", ""),
                start_date.get("year", ""),
                meta.get("period_label", ""),
                meta.get("path_family_label", ""),
                meta.get("event_type_label", ""),
                meta.get("evidence_grade", ""),
                meta.get("verification_status", ""),
                event.get("text", {}).get("headline", ""),
                ", ".join(meta.get("source_refs", [])),
            ]
        )
    return tabulate(
        rows,
        headers=[
            "event_id",
            "year",
            "period",
            "path",
            "type",
            "evidence",
            "status",
            "title",
            "sources",
        ],
        tablefmt="psql",
        missingval="",
    )


def render_preview(timelinejs: dict) -> str:
    payload = json.dumps(
        timelinejs,
        ensure_ascii=False,
        separators=(",", ":"),
    ).replace("</", "<\\/")
    source_count = len(load_json("docs/reference/history-timeline/sources.json")["sources"])
    period_count = len(load_json("docs/reference/history-timeline/periods.json")["periods"])
    works_count = sum(
        1
        for event in timelinejs["events"]
        if event.get("meta", {}).get("publication_status") == "selected"
    )
    reviewed_count = sum(
        1
        for event in timelinejs["events"]
        if event.get("meta", {}).get("verification_status") == "locally_reviewed"
    )
    generated_at = load_json(
        "docs/reference/history-timeline/publication-manifest.v1.json"
    ).get("created_at", "2026-08-07T00:00:00Z")
    path_table = html.escape(build_path_summary_table(timelinejs))
    scope_table, status_table = build_scope_status_tables(timelinejs)
    scope_table = html.escape(scope_table)
    status_table = html.escape(status_table)
    event_table = html.escape(build_event_table(timelinejs["events"]))
    return (
        PREVIEW_TEMPLATE
        .replace("__PAYLOAD__", payload)
        .replace("__PATH_LABELS_JSON__", json.dumps(PATH_LABELS_ZH, ensure_ascii=False))
        .replace("__EVENT_TYPE_LABELS_JSON__", json.dumps(EVENT_TYPE_LABELS_ZH, ensure_ascii=False))
        .replace("__EVENT_COUNT__", str(len(timelinejs["events"])))
        .replace("__SOURCE_COUNT__", str(source_count))
        .replace("__PERIOD_COUNT__", str(period_count))
        .replace("__WORKS_COUNT__", str(works_count))
        .replace("__REVIEWED_COUNT__", str(reviewed_count))
        .replace("__GENERATED_AT__", generated_at)
        .replace("__PATH_TABLE__", path_table)
        .replace("__SCOPE_TABLE__", scope_table)
        .replace("__STATUS_TABLE__", status_table)
        .replace("__EVENT_TABLE__", event_table)
    )


PREVIEW_TEMPLATE = r"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Human Infra 永生史</title>
</head>
<body>
  <h1>Human Infra 永生史</h1>
  <p>从神话、宗教与炼金术，到老年科学、健康寿命和生物技术产业的严肃历史年表。时间轴为增强视图，psql 表格和原始 JSON 是资料事实来源。</p>

  <dl>
    <dt>数据范围</dt>
    <dd>__EVENT_COUNT__ 条事件 / __SOURCE_COUNT__ 个来源 / __PERIOD_COUNT__ 个时期</dd>
    <dt>作品化</dt>
    <dd>__WORKS_COUNT__ 条作品子集；__REVIEWED_COUNT__ 条本地已复核</dd>
    <dt>生成时间</dt>
    <dd><time datetime="__GENERATED_AT__">__GENERATED_AT__</time></dd>
    <dt>原始数据</dt>
    <dd><a href="timeline.json">timeline.json</a> · <a href="sources.json">sources.json</a> · <a href="periods.json">periods.json</a> · <a href="timelinejs.json">timelinejs.json</a></dd>
    <dt>出版契约</dt>
    <dd><a href="publication-manifest.v1.json">publication-manifest.v1.json</a> · <a href="PUBLICATION.md">PUBLICATION.md</a></dd>
  </dl>

  <h2>查询条件</h2>
  <form method="get" action="preview.html" id="filter-form">
    <fieldset>
      <legend>筛选</legend>
      <p><label for="q">搜索</label> <input id="q" name="q" type="search" placeholder="标题、摘要、证据或来源"></p>
      <p>
        <label for="scope">范围</label>
        <select id="scope" name="scope">
          <option value="all">全部资料</option>
          <option value="works">作品子集</option>
          <option value="reviewed">本地已复核</option>
        </select>
      </p>
      <p><label for="period">时期</label> <select id="period" name="period"><option value="">全部时期</option></select></p>
      <p><label for="path">路径</label> <select id="path" name="path"><option value="">全部路径</option></select></p>
      <p><label for="type">类型</label> <select id="type" name="type"><option value="">全部类型</option></select></p>
      <p><label for="evidence">证据等级</label> <select id="evidence" name="evidence"><option value="">全部证据等级</option></select></p>
      <p><button type="submit">查询</button></p>
    </fieldset>
  </form>
  <noscript><p>筛选和图表需要 JavaScript。核心数据仍可直接读取 <a href="timeline.json">timeline.json</a> 与 <a href="sources.json">sources.json</a>。</p></noscript>

  <h2>路径族概览</h2>
  <pre><code>__PATH_TABLE__</code></pre>

  <h2>范围与复核状态</h2>
  <pre><code>__SCOPE_TABLE__</code></pre>
  <pre><code>__STATUS_TABLE__</code></pre>

  <h2>时间轴图表</h2>
  <div id="chart"></div>
  <p id="chart-status">图表为增强视图；核心数据见下方事件明细与原始 JSON。</p>

  <h2>事件明细</h2>
  <details open>
    <summary>事件明细（__EVENT_COUNT__ 行）</summary>
    <pre><code>__EVENT_TABLE__</code></pre>
  </details>

  <script id="timeline-data" type="application/json">__PAYLOAD__</script>
  <script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
  <script>
    (function () {
      const data = JSON.parse(document.getElementById('timeline-data').textContent);
      const events = data.events || [];
      const PATH_LABELS = __PATH_LABELS_JSON__;
      const EVENT_TYPE_LABELS = __EVENT_TYPE_LABELS_JSON__;
      const params = new URLSearchParams(window.location.search);
      const state = {
        q: params.get('q') || '',
        scope: params.get('scope') || 'all',
        period: params.get('period') || '',
        path: params.get('path') || '',
        type: params.get('type') || '',
        evidence: params.get('evidence') || ''
      };
      const countEl = document.getElementById('result-count');
      const emptyEl = document.getElementById('empty');
      const chartEl = document.getElementById('chart');
      const chartStatusEl = document.getElementById('chart-status');
      let chart = null;

      function esc(value) {
        return String(value == null ? '' : value).replace(/[&<>"']/g, function (ch) {
          return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[ch];
        });
      }

      function dateLabel(e) {
        const start = e.start_date || {};
        let label = start.year != null ? String(start.year) : '';
        if (start.month != null) label += '-' + String(start.month).padStart(2, '0');
        if (start.day != null) label += '-' + String(start.day).padStart(2, '0');
        return label;
      }

      function unique(values) {
        return Array.from(new Set(values.filter(Boolean))).sort();
      }

      function fillSelect(select, values, label, display) {
        select.innerHTML = '<option value="">' + label + '</option>' + values.map(function (v) {
          return '<option value="' + esc(v) + '">' + esc(display ? display(v) : v) + '</option>';
        }).join('');
      }

      fillSelect(document.getElementById('period'), unique(events.map(function (e) {
        return e.meta && e.meta.period_label;
      })), '全部时期');
      fillSelect(document.getElementById('path'), unique(events.map(function (e) {
        return e.meta && e.meta.path_family;
      })), '全部路径', function (v) { return PATH_LABELS[v] || v; });
      fillSelect(document.getElementById('type'), unique(events.map(function (e) {
        return e.meta && e.meta.event_type;
      })), '全部类型', function (v) { return EVENT_TYPE_LABELS[v] || v; });
      fillSelect(document.getElementById('evidence'), unique(events.map(function (e) {
        return e.meta && e.meta.evidence_grade;
      })), '全部证据等级');

      document.getElementById('q').value = state.q;
      document.getElementById('scope').value = state.scope;
      document.getElementById('period').value = state.period;
      document.getElementById('path').value = state.path;
      document.getElementById('type').value = state.type;
      document.getElementById('evidence').value = state.evidence;

      function plainText(e) {
        const meta = e.meta || {};
        return [
          e.text && e.text.headline,
          e.text && e.text.text ? e.text.text.replace(/<[^>]*>/g, ' ') : '',
          meta.event_id,
          meta.period_label,
          meta.path_family,
          meta.event_type,
          meta.evidence_grade
        ].join(' ').toLowerCase();
      }

      function matches(e) {
        const meta = e.meta || {};
        if (state.scope === 'works' && meta.publication_status !== 'selected') return false;
        if (state.scope === 'reviewed' && meta.verification_status !== 'locally_reviewed') return false;
        if (state.period && meta.period_label !== state.period) return false;
        if (state.path && meta.path_family !== state.path) return false;
        if (state.type && meta.event_type !== state.type) return false;
        if (state.evidence && meta.evidence_grade !== state.evidence) return false;
        if (state.q && plainText(e).indexOf(state.q) < 0) return false;
        return true;
      }

      function filteredEvents() {
        const filtered = events.filter(matches).slice();
        filtered.sort(function (a, b) {
          const ay = a.start_date && a.start_date.year != null ? a.start_date.year : 0;
          const by = b.start_date && b.start_date.year != null ? b.start_date.year : 0;
          return ay - by;
        });
        return filtered;
      }

      function render() {
        const filtered = filteredEvents();
        const scopeLabels = {
          all: '当前显示全部资料，只用于巡检和检索。',
          works: '当前显示作品子集，只表示进入作品化评审范围。',
          reviewed: '当前显示本地已复核资料，可支撑时间轴发布，但仍需 fresh review 才能进入叙事正文。'
        };
        chartStatusEl.textContent = scopeLabels[state.scope] + ' 图表为增强视图；核心数据见下方事件明细与原始 JSON。';
        if (typeof window.echarts === 'undefined') {
          chartEl.replaceChildren(document.createTextNode('ECharts 未加载，请检查网络后刷新；核心数据仍可直接读取下方表格。'));
          return;
        }
        if (!chart) {
          chart = window.echarts.init(chartEl, null, {
            width: Math.max(900, Math.min(window.innerWidth - 40, 1400)),
            height: 560
          });
        }
        const pathLabels = unique(filtered.map(function (e) {
          return e.meta && e.meta.path_family_label;
        }));
        const pathIndex = {};
        pathLabels.forEach(function (p, i) { pathIndex[p] = i; });
        const points = filtered.map(function (e) {
          const meta = e.meta || {};
          const year = e.start_date && e.start_date.year != null ? e.start_date.year : 0;
          return {
            value: [year, pathIndex[meta.path_family_label] || 0],
            title: e.text && e.text.headline ? e.text.headline : '',
            dateLabel: dateLabel(e),
            meta: meta
          };
        });
        chart.setOption({
          animation: false,
          tooltip: {
            trigger: 'item',
            formatter: function (params) {
              const item = params.data || {};
              const meta = item.meta || {};
              return '<strong>' + esc(item.title || '') + '</strong><br>' +
                '日期：' + esc(item.dateLabel || (params.value ? params.value[0] : '?')) + '<br>' +
                '时期：' + esc(meta.period_label || '') + '<br>' +
                '路径：' + esc(meta.path_family_label || meta.path_family || '') + '<br>' +
                '类型：' + esc(meta.event_type_label || meta.event_type || '') + '<br>' +
                '证据：' + esc(meta.evidence_grade || '') + ' / ' + esc(meta.verification_status || '') + '<br>' +
                '编号：' + esc(meta.event_id || '') + '<br>' +
                '来源：' + (meta.source_links || '无');
            }
          },
          grid: { left: 140, right: 40, top: 40, bottom: 80 },
          xAxis: {
            type: 'value',
            name: '年份',
            nameLocation: 'middle',
            nameGap: 40,
            min: 'dataMin',
            max: 'dataMax'
          },
          yAxis: {
            type: 'category',
            data: pathLabels
          },
          dataZoom: [
            { type: 'inside', xAxisIndex: 0, start: 0, end: 100 },
            { type: 'slider', xAxisIndex: 0, bottom: 16, start: 0, end: 100 }
          ],
          series: [{
            type: 'scatter',
            symbolSize: 7,
            data: points
          }]
        });
        chart.resize();
      }

      document.getElementById('q').addEventListener('input', function (e) {
        state.q = e.target.value;
        render();
      });
      document.getElementById('scope').addEventListener('change', function (e) {
        state.scope = e.target.value;
        render();
      });
      document.getElementById('period').addEventListener('change', function (e) {
        state.period = e.target.value;
        render();
      });
      document.getElementById('path').addEventListener('change', function (e) {
        state.path = e.target.value;
        render();
      });
      document.getElementById('type').addEventListener('change', function (e) {
        state.type = e.target.value;
        render();
      });
      document.getElementById('evidence').addEventListener('change', function (e) {
        state.evidence = e.target.value;
        render();
      });
      window.addEventListener('resize', function () {
        if (chart) chart.resize();
      });

      render();
    })();
  </script>
</body>
</html>
"""


def main() -> None:
    timelinejs = build_timelinejs()
    (PACKAGE / "timelinejs.json").write_text(
        json.dumps(timelinejs, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (PACKAGE / "preview.html").write_text(render_preview(timelinejs), encoding="utf-8")
    print(
        f"status=OK preview_events={len(timelinejs['events'])} "
        "files=timelinejs.json,preview.html"
    )


if __name__ == "__main__":
    main()
