#!/usr/bin/env python3
"""Build timeline publication JSON and an ECharts standalone preview."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "docs" / "reference" / "history-timeline"


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
        parts.append(f'<a href="{html.escape(url, quote=True)}" target="_blank" rel="noopener">{html.escape(ref)}</a>')
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
    period_label = period.get("label_en", event.get("period_id", ""))
    event_id = event.get("event_id", "")
    publication_status = "selected" if event_id in works_ids else "candidate"
    links = source_links(source_registry, event.get("sources", []))
    body_parts = [
        html.escape(event.get("summary", "")),
        "",
        "<strong>Claim</strong>: " + html.escape(event.get("claim", "")),
        "",
        f"<strong>Period</strong>: {html.escape(period_label)}",
        f"<strong>Evidence</strong>: {html.escape(event.get('evidence_grade', ''))} / {html.escape(event.get('verification_status', ''))}",
        "",
        "Sources: " + links,
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
            "path_family": event.get("path_family", ""),
            "event_type": event.get("event_type", ""),
            "evidence_grade": event.get("evidence_grade", ""),
            "verification_status": event.get("verification_status", ""),
            "publication_status": publication_status,
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


def render_preview(timelinejs: dict) -> str:
    payload = json.dumps(
        timelinejs,
        ensure_ascii=False,
        separators=(",", ":"),
    ).replace("</", "<\\/")
    return PREVIEW_TEMPLATE.replace("__PAYLOAD__", payload)


PREVIEW_TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Human Infra 永生史</title>
  <style>
    :root {
      --bg: #f6f7f8;
      --panel: #ffffff;
      --line: #d8dde2;
      --ink: #182026;
      --muted: #5f6b76;
      --accent: #1f6f8f;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "PingFang SC", "Microsoft YaHei", sans-serif;
      line-height: 1.55;
    }
    header {
      padding: 28px 24px 20px;
      border-bottom: 1px solid var(--line);
      background: var(--panel);
    }
    .wrap {
      max-width: 1280px;
      margin: 0 auto;
    }
    h1 {
      margin: 0 0 8px;
      font-size: 28px;
      font-weight: 650;
      letter-spacing: 0;
    }
    .subtitle {
      margin: 0 0 14px;
      color: var(--muted);
      font-size: 14px;
    }
    .stats {
      display: flex;
      flex-wrap: wrap;
      gap: 8px 18px;
      font-size: 13px;
      color: var(--muted);
    }
    .stats strong { color: var(--ink); font-weight: 650; }
    .toolbar {
      position: sticky;
      top: 0;
      z-index: 10;
      padding: 12px 0;
      background: rgba(246, 247, 248, 0.96);
      backdrop-filter: blur(6px);
      border-bottom: 1px solid var(--line);
    }
    .controls {
      display: grid;
      grid-template-columns: minmax(220px, 1.6fr) repeat(5, minmax(130px, 0.8fr));
      gap: 10px;
    }
    input, select {
      width: 100%;
      height: 38px;
      padding: 0 10px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: var(--panel);
      color: var(--ink);
      font: inherit;
      font-size: 13px;
      outline: none;
    }
    input:focus, select:focus { border-color: var(--accent); }
    .result-line {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      padding: 12px 0 8px;
      color: var(--muted);
      font-size: 13px;
    }
    #chart {
      height: 74vh;
      min-height: 520px;
      margin-bottom: 30px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
    }
    .empty {
      padding: 36px 0;
      text-align: center;
      color: var(--muted);
    }
    footer {
      padding: 20px 0 36px;
      color: var(--muted);
      font-size: 12px;
    }
    @media (max-width: 900px) {
      .controls { grid-template-columns: 1fr 1fr; }
      header { padding: 22px 16px 16px; }
    }
    @media (max-width: 600px) {
      .controls { grid-template-columns: 1fr; }
      .wrap { padding: 0 12px; }
    }
  </style>
</head>
<body>
  <header>
    <div class="wrap">
      <h1>Human Infra 永生史</h1>
      <p class="subtitle" id="page-subtitle"></p>
      <div class="stats" id="stats"></div>
    </div>
  </header>
  <div class="toolbar">
    <div class="wrap">
      <div class="controls">
        <input id="q" type="search" placeholder="搜索标题、摘要、证据或来源">
        <select id="scope">
          <option value="all">全部资料</option>
          <option value="works">作品子集 400</option>
          <option value="reviewed">本地已复核</option>
        </select>
        <select id="period"><option value="">全部时期</option></select>
        <select id="path"><option value="">全部路径</option></select>
        <select id="type"><option value="">全部类型</option></select>
        <select id="evidence"><option value="">全部证据等级</option></select>
      </div>
    </div>
  </div>
  <main class="wrap">
    <div class="result-line">
      <span id="result-count"></span>
      <span>ECharts 图表模式 · 可缩放年份</span>
    </div>
    <div id="chart"></div>
    <div class="empty" id="empty" hidden>没有匹配的事件</div>
  </main>
  <footer class="wrap">数据来源为公开 Crossref/DOI 元数据；<span id="footer-note"></span></footer>
  <script id="timeline-data" type="application/json">__PAYLOAD__</script>
  <script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
  <script>
    (function () {
      const data = JSON.parse(document.getElementById('timeline-data').textContent);
      const events = data.events || [];
      const state = { q: '', scope: 'all', period: '', path: '', type: '', evidence: '' };
      const countEl = document.getElementById('result-count');
      const emptyEl = document.getElementById('empty');
      const chartEl = document.getElementById('chart');
      let chart = null;

      document.getElementById('page-subtitle').textContent = data.title && data.title.text ? data.title.text.text : '';

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

      function fillSelect(select, values, label) {
        select.innerHTML = '<option value="">' + label + '</option>' + values.map(function (v) {
          return '<option value="' + esc(v) + '">' + esc(v) + '</option>';
        }).join('');
      }

      fillSelect(document.getElementById('period'), unique(events.map(function (e) {
        return e.meta && e.meta.period_label;
      })), '全部时期');
      fillSelect(document.getElementById('path'), unique(events.map(function (e) {
        return e.meta && e.meta.path_family;
      })), '全部路径');
      fillSelect(document.getElementById('type'), unique(events.map(function (e) {
        return e.meta && e.meta.event_type;
      })), '全部类型');
      fillSelect(document.getElementById('evidence'), unique(events.map(function (e) {
        return e.meta && e.meta.evidence_grade;
      })), '全部证据等级');

      const periodCount = unique(events.map(function (e) { return e.meta && e.meta.period_label; })).length;
      const pathCount = unique(events.map(function (e) { return e.meta && e.meta.path_family; })).length;
      const worksCount = events.filter(function (e) {
        return e.meta && e.meta.publication_status === 'selected';
      }).length;
      const reviewedCount = events.filter(function (e) {
        return e.meta && e.meta.verification_status === 'locally_reviewed';
      }).length;
      const exactDateCount = events.filter(function (e) {
        return e.start_date && e.start_date.month != null;
      }).length;
      document.getElementById('stats').innerHTML =
        '<span><strong>' + events.length + '</strong> 条原始资料</span>' +
        '<span><strong>' + worksCount + '</strong> 条作品子集</span>' +
        '<span><strong>' + reviewedCount + '</strong> 条本地已复核</span>' +
        '<span><strong>' + periodCount + '</strong> 个时期</span>' +
        '<span><strong>' + pathCount + '</strong> 条路径族</span>' +
        '<span><strong>' + exactDateCount + '</strong> 条含年月日</span>' +
        '<span>作品化状态 <strong>随 scope 筛选</strong></span>';

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
        countEl.textContent = filtered.length + ' 条匹配';
        const scopeLabels = {
          all: '当前显示全部资料，只用于巡检和检索。',
          works: '当前显示作品子集 400，只表示进入作品化评审范围。',
          reviewed: '当前显示本地已复核资料，可支撑时间轴发布，但仍需 fresh review 才能进入叙事正文。'
        };
        document.getElementById('footer-note').textContent = scopeLabels[state.scope] || '';
        emptyEl.hidden = filtered.length !== 0;
        if (typeof window.echarts === 'undefined') {
          chartEl.innerHTML = '<div class="empty">ECharts 未加载，请检查网络后刷新。</div>';
          return;
        }
        if (!chart) chart = window.echarts.init(chartEl);
        const pathLabels = unique(filtered.map(function (e) {
          return e.meta && e.meta.path_family;
        }));
        const pathIndex = {};
        pathLabels.forEach(function (p, i) { pathIndex[p] = i; });
        const typeColors = {
          myth: '#7b5e7b',
          religious: '#7b5e7b',
          thought: '#1f6f8f',
          practice: '#2f7d4f',
          technology: '#b05f3a',
          institution: '#5b6bb0',
          literature: '#5f6b76',
          failure: '#a23b3b',
          demographic: '#3a8f8f',
          policy: '#8a6d3b'
        };
        const points = filtered.map(function (e) {
          const meta = e.meta || {};
          const year = e.start_date && e.start_date.year != null ? e.start_date.year : 0;
          return {
            value: [year, pathIndex[meta.path_family] || 0],
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
                '路径：' + esc(meta.path_family || '') + '<br>' +
                '类型：' + esc(meta.event_type || '') + '<br>' +
                '证据：' + esc(meta.evidence_grade || '') + ' / ' + esc(meta.verification_status || '') + '<br>' +
                '编号：' + esc(meta.event_id || '') + '<br>' +
                '来源：' + (meta.source_links || '无');
            }
          },
          grid: { left: 130, right: 40, top: 40, bottom: 80 },
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
            data: points,
            itemStyle: {
              color: function (params) {
                const meta = params.data && params.data.meta || {};
                return typeColors[meta.event_type] || '#5f6b76';
              },
              opacity: 0.72
            }
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
