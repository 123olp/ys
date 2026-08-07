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
    scope_table, status_table = build_scope_status_tables(timelinejs)
    scope_table = html.escape(scope_table)
    status_table = html.escape(status_table)
    reviewed_table = html.escape(build_reviewed_table(timelinejs["events"]))
    return (
        PREVIEW_TEMPLATE
        .replace("__EVENT_COUNT__", str(len(timelinejs["events"])))
        .replace("__SOURCE_COUNT__", str(source_count))
        .replace("__PERIOD_COUNT__", str(period_count))
        .replace("__WORKS_COUNT__", str(works_count))
        .replace("__REVIEWED_COUNT__", str(reviewed_count))
        .replace("__GENERATED_AT__", generated_at)
        .replace("__PATH_TABLE__", path_table)
        .replace("__SCOPE_TABLE__", scope_table)
        .replace("__STATUS_TABLE__", status_table)
        .replace("__REVIEWED_TABLE__", reviewed_table)
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
    <dd><a href="timeline.json">timeline.json</a> · <a href="sources.json">sources.json</a> · <a href="periods.json">periods.json</a> · <a href="timelinejs.json">timelinejs.json</a> · <a href="timeline-events.psql.txt">timeline-events.psql.txt</a></dd>
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

  <h2>路径族概览</h2>
  <pre><code>__PATH_TABLE__</code></pre>

  <h2>范围与复核状态</h2>
  <pre><code>__SCOPE_TABLE__</code></pre>
  <pre><code>__STATUS_TABLE__</code></pre>

  <h2>事件阅读器</h2>
  <p>
    <button id="prev-event" type="button" aria-label="前一条事件">前一条</button>
    <span id="event-nav-index"></span>
    <button id="next-event" type="button" aria-label="后一条事件">后一条</button>
  </p>
  <p id="event-detail-empty" hidden>点击图表中的事件，或用前一条/后一条浏览当前筛选结果。</p>
  <dl id="event-detail-meta"></dl>
  <pre id="event-detail-text"></pre>

  <h2>时间轴图表</h2>
  <p id="result-count"></p>
  <div id="chart"></div>
  <p id="chart-status">图表为增强视图；核心数据见下方事件明细与原始 JSON。</p>

  <h2>本地已复核事件</h2>
  <pre><code>__REVIEWED_TABLE__</code></pre>
  <p><a href="timeline-events.psql.txt">下载/查看完整事件明细（__EVENT_COUNT__ 行）</a></p>

  <script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
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
    (PACKAGE / "preview.html").write_text(render_preview(timelinejs), encoding="utf-8")
    (PACKAGE / "timeline-events.psql.txt").write_text(
        build_event_table(timelinejs["events"]) + "\n",
        encoding="utf-8",
    )
    print(
        f"status=OK preview_events={len(timelinejs['events'])} "
        "files=timelinejs.json,preview.html,timeline-events.psql.txt"
    )


if __name__ == "__main__":
    main()
