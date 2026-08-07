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
                "headline": "永生年表",
                "text": "从神话、宗教与炼金术，到老年科学、健康寿命和生物技术产业的严肃历史年表。",
            }
        },
        "scale": "human",
        "events": events,
    }


def build_timelinejs_light(timelinejs: dict) -> dict:
    events = []
    for event in timelinejs["events"]:
        meta = dict(event.get("meta", {}))
        for key in ("period_id", "chapter", "date_start", "status", "source_links"):
            meta.pop(key, None)
        light_event = {
            "start_date": event.get("start_date", {}),
            "text": {
                "headline": event.get("text", {}).get("headline", ""),
            },
            "meta": meta,
        }
        if "end_date" in event:
            light_event["end_date"] = event["end_date"]
        events.append(light_event)
    return {
        "title": timelinejs.get("title", {}),
        "scale": timelinejs.get("scale", "human"),
        "events": events,
    }


def build_timelinejs_detail(timelinejs: dict) -> dict:
    return {
        "events": [
            {
                "event_id": event.get("meta", {}).get("event_id", ""),
                "text": event.get("text", {}).get("text", ""),
            }
            for event in timelinejs["events"]
        ]
    }


def build_path_summary_table(timelinejs: dict) -> str:
    path_stats: dict[str, list[int]] = defaultdict(lambda: [0, 0, 0])
    totals = [0, 0, 0]
    for event in timelinejs["events"]:
        meta = event.get("meta", {})
        path = meta.get("path_family", "")
        path_stats[path][0] += 1
        totals[0] += 1
        if meta.get("publication_status") == "selected":
            path_stats[path][1] += 1
            totals[1] += 1
        if meta.get("verification_status") == "locally_reviewed":
            path_stats[path][2] += 1
            totals[2] += 1
    rows = [
        [PATH_LABELS_ZH.get(path, path), counts[0], counts[1], counts[2]]
        for path, counts in path_stats.items()
    ]
    rows.sort(key=lambda row: -row[1])
    rows.append(["合计", totals[0], totals[1], totals[2]])
    return tabulate(
        rows,
        headers=["路径族", "全部资料", "作品子集", "本地已复核"],
        tablefmt="psql",
        missingval="",
    )


def build_type_summary_table(timelinejs: dict) -> str:
    type_stats: dict[str, list[int]] = defaultdict(lambda: [0, 0, 0])
    totals = [0, 0, 0]
    for event in timelinejs["events"]:
        meta = event.get("meta", {})
        event_type = meta.get("event_type", "")
        type_stats[event_type][0] += 1
        totals[0] += 1
        if meta.get("publication_status") == "selected":
            type_stats[event_type][1] += 1
            totals[1] += 1
        if meta.get("verification_status") == "locally_reviewed":
            type_stats[event_type][2] += 1
            totals[2] += 1
    rows = [
        [
            EVENT_TYPE_LABELS_ZH.get(event_type, event_type),
            counts[0],
            counts[1],
            counts[2],
        ]
        for event_type, counts in type_stats.items()
    ]
    rows.sort(key=lambda row: -row[1])
    rows.append(["合计", totals[0], totals[1], totals[2]])
    return tabulate(
        rows,
        headers=["事件类型", "全部资料", "作品子集", "本地已复核"],
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


def build_reviewed_table(events: list[dict]) -> str:
    reviewed = [
        event
        for event in events
        if event.get("meta", {}).get("verification_status") == "locally_reviewed"
    ]
    if not reviewed:
        return ""
    rows = []
    for event in reviewed:
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


def build_publication_table(
    event_count: int,
    source_count: int,
    period_count: int,
    works_count: int,
    reviewed_count: int,
    generated_at: str,
) -> str:
    return f"""<table>
      <tbody>
        <tr>
          <th scope="row">数据范围</th>
          <td>{event_count} 条事件 / {source_count} 个来源 / {period_count} 个时期</td>
        </tr>
        <tr>
          <th scope="row">作品化</th>
          <td>{works_count} 条作品子集；{reviewed_count} 条本地已复核</td>
        </tr>
        <tr>
          <th scope="row">生成时间</th>
          <td><time datetime="{generated_at}">{generated_at}</time></td>
        </tr>
        <tr>
          <th scope="row">原始数据</th>
          <td><a href="timeline.json">timeline.json</a> · <a href="sources.json">sources.json</a> · <a href="periods.json">periods.json</a> · <a href="timelinejs.json">timelinejs.json</a> · <a href="timeline-events.psql.txt">timeline-events.psql.txt</a></td>
        </tr>
        <tr>
          <th scope="row">出版契约</th>
          <td><a href="publication-manifest.v1.json">publication-manifest.v1.json</a> · <a href="PUBLICATION.md">PUBLICATION.md</a></td>
        </tr>
      </tbody>
    </table>"""


def build_aggregate_blocks(
    path_table: str,
    type_table: str,
    scope_table: str,
    status_table: str,
    publication_table: str,
    reviewed_table: str,
    event_count: int,
) -> str:
    blocks = [
        (
            "路径族与范围聚合",
            f'<pre id="path-summary-table"><code>{path_table}</code></pre>',
        ),
        (
            "事件类型与范围聚合",
            f'<pre id="type-summary-table"><code>{type_table}</code></pre>',
        ),
        (
            "范围与复核状态",
            (
                f'<pre id="scope-summary-table"><code>{scope_table}</code></pre>\n'
                f'<pre id="status-summary-table"><code>{status_table}</code></pre>'
            ),
        ),
        ("资料与出版", publication_table),
        (
            "本地已复核事件",
            f'<pre id="reviewed-summary-table"><code>{reviewed_table}</code></pre>',
        ),
        (
            f"完整事件明细（{event_count} 条）",
            '<pre id="full-event-table"><code id="full-event-table-code"></code></pre>',
        ),
    ]
    return "\n\n".join(
        f"<h2>{html.escape(title)}</h2>\n{body}" for title, body in blocks
    )


def render_preview(timelinejs: dict) -> str:
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
    type_table = html.escape(build_type_summary_table(timelinejs))
    scope_table, status_table = build_scope_status_tables(timelinejs)
    scope_table = html.escape(scope_table)
    status_table = html.escape(status_table)
    reviewed_table = html.escape(build_reviewed_table(timelinejs["events"]))
    publication_table = build_publication_table(
        len(timelinejs["events"]),
        source_count,
        period_count,
        works_count,
        reviewed_count,
        generated_at,
    )
    aggregate_blocks = build_aggregate_blocks(
        path_table,
        type_table,
        scope_table,
        status_table,
        publication_table,
        reviewed_table,
        len(timelinejs["events"]),
    )
    return PREVIEW_TEMPLATE.replace("__AGGREGATE_BLOCKS__", aggregate_blocks)


PREVIEW_TEMPLATE = r"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>永生年表</title>
  <style>pre { overflow-x: auto; }</style>
</head>
<body>
  <h1>永生年表</h1>

  <h2>事件阅读器</h2>
  <p>
    <button id="prev-event" type="button" aria-label="前一条事件">前一条</button>
    <span id="event-nav-index" aria-live="polite"></span>
    <button id="next-event" type="button" aria-label="后一条事件">后一条</button>
    <label for="event-jump">跳转</label>
    <input id="event-jump" type="text" placeholder="编号或序号">
    <button id="jump-event" type="button">跳转</button>
  </p>
  <p id="event-detail-empty" hidden>点击图表中的事件，或用前一条/后一条浏览当前筛选结果。</p>
  <pre id="event-detail-table"><code id="event-detail-table-code"></code></pre>
  <pre id="event-detail-text"></pre>

  <h2>时间轴图表</h2>
  <p id="result-count"></p>
  <div id="chart" role="img" aria-label="永生年表事件时间轴图表"></div>
  <p id="evidence-legend">证据等级图例：T · I · M · S · L</p>
  <p id="chart-status">图表为增强视图；核心资料与查询入口在下方。</p>

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
      <p>
        <label for="mode">视图</label>
        <select id="mode" name="mode">
          <option value="path">按路径族</option>
          <option value="density">年代密度</option>
        </select>
      </p>
      <p>
        <label for="window">时间窗口</label>
        <select id="window" name="window">
          <option value="all">全部时间</option>
          <option value="ancient">公元前（-4000~-1）</option>
          <option value="classical">古典（0~500）</option>
          <option value="medieval">中世纪（501~1500）</option>
          <option value="modern">近代（1501~1900）</option>
          <option value="twentieth">20世纪（1901~2000）</option>
          <option value="twentyfirst">21世纪（2001~2100）</option>
        </select>
      </p>
      <p><button type="submit">查询</button></p>
    </fieldset>
  </form>
  <noscript><p>筛选和图表需要 JavaScript。核心数据仍可直接读取 <a href="timeline.json">timeline.json</a>、<a href="sources.json">sources.json</a> 与 <a href="timeline-events.psql.txt">timeline-events.psql.txt</a>。</p></noscript>

  __AGGREGATE_BLOCKS__

  <script src="echarts.common.min.js"></script>
  <script src="preview-core.js"></script>
  <script src="preview.js"></script>
</body>
</html>
"""


def main() -> None:
    timelinejs = build_timelinejs()
    (PACKAGE / "timelinejs.json").write_text(
        json.dumps(timelinejs, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (PACKAGE / "timelinejs.light.json").write_text(
        json.dumps(
            build_timelinejs_light(timelinejs),
            ensure_ascii=False,
            separators=(",", ":"),
        ) + "\n",
        encoding="utf-8",
    )
    (PACKAGE / "timelinejs.detail.json").write_text(
        json.dumps(
            build_timelinejs_detail(timelinejs),
            ensure_ascii=False,
            separators=(",", ":"),
        ) + "\n",
        encoding="utf-8",
    )
    (PACKAGE / "preview.html").write_text(render_preview(timelinejs), encoding="utf-8")
    (PACKAGE / "timeline-events.psql.txt").write_text(
        build_event_table(timelinejs["events"]) + "\n",
        encoding="utf-8",
    )
    print(
        f"status=OK preview_events={len(timelinejs['events'])} "
        "files=timelinejs.json,timelinejs.light.json,timelinejs.detail.json,preview.html,timeline-events.psql.txt"
    )


if __name__ == "__main__":
    main()
