#!/usr/bin/env python3
"""Append validated timeline batches to the Human Infra history timeline.

The batch file is a JSON object with a list of items. Each item must carry
enough Crossref-verified metadata to produce one event and one source card.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "docs" / "reference" / "history-timeline"
SOURCES_NOTE = ROOT / "docs" / "source-notes" / "2026-08-06-human-immortality-research-major-events-timeline.md"

EVENT_PREFIX = {
    "demographic": "DEM",
    "failure": "FAI",
    "institution": "INS",
    "literature": "LIT",
    "myth": "MTH",
    "religious": "MTH",
    "policy": "POL",
    "practice": "PRA",
    "technology": "TEC",
    "thought": "THT",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def next_id(existing: list[str], prefix: str) -> str:
    max_num = 0
    for item in existing:
        match = re.fullmatch(rf"HIT-{prefix}-(\d{{3,}})", item)
        if match:
            max_num = max(max_num, int(match.group(1)))
    return f"HIT-{prefix}-{max_num + 1:03d}"


def next_source_id(existing: list[str]) -> str:
    max_num = 0
    for item in existing:
        match = re.fullmatch(r"SRC-(\d{3,})", item)
        if match:
            max_num = max(max_num, int(match.group(1)))
    return f"SRC-{max_num + 1:03d}"


def bump_version(version: str) -> str:
    major, minor, patch = (int(part) for part in version.split("."))
    return f"{major}.{minor + 1}.{patch}"


def update_readme(event_count: int, source_count: int, round_lines: list[str]) -> None:
    readme = PACKAGE / "README.md"
    text = readme.read_text(encoding="utf-8")
    text = re.sub(
        r"正式来源卡：\d+ 个来源",
        f"正式来源卡：{source_count} 个来源",
        text,
    )
    text = re.sub(
        r"正式年表数据：\d+ 条事件",
        f"正式年表数据：{event_count} 条事件",
        text,
    )
    text = re.sub(
        r"来源卡：\d+ 个来源已注册",
        f"来源卡：{source_count} 个来源已注册",
        text,
    )
    text = re.sub(
        r"事件：\d+ 条事件已转为结构化 JSON",
        f"事件：{event_count} 条事件已转为结构化 JSON",
        text,
    )
    lines = text.splitlines()
    indexes = [i for i, line in enumerate(lines) if re.search(r"第\d+轮补录来源：", line)]
    if indexes:
        index = max(indexes)
        lines[index + 1 : index + 1] = round_lines
        text = "\n".join(lines)
    readme.write_text(text, encoding="utf-8")


def update_source_note(round_lines: list[str], ref_lines: list[str]) -> None:
    text = SOURCES_NOTE.read_text(encoding="utf-8")
    lines = text.rstrip().splitlines()
    ref_start = None
    for index, line in enumerate(lines):
        if re.match(r"^\[\d+\]:", line):
            ref_start = index
            break
    if ref_start is None:
        lines.extend([""] + round_lines)
    else:
        lines[ref_start:ref_start] = [""] + round_lines + [""]
    if ref_lines:
        lines.extend([""] + ref_lines)
    SOURCES_NOTE.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def max_ref_number() -> int:
    text = SOURCES_NOTE.read_text(encoding="utf-8")
    numbers = [int(match.group(1)) for match in re.finditer(r"^\[(\d+)\]:", text, re.MULTILINE)]
    return max(numbers) if numbers else 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", required=True, type=Path)
    args = parser.parse_args()

    batch = json.loads(args.batch.read_text(encoding="utf-8"))
    items = batch["items"]
    require(len(items) == 5, "batch items must contain exactly 5 entries")

    timeline = load(PACKAGE / "timeline.json")
    sources = load(PACKAGE / "sources.json")
    event_ids = [event["event_id"] for event in timeline["events"]]
    source_ids = [source["source_id"] for source in sources["sources"]]

    timestamp = now_iso()
    new_events: list[dict] = []
    new_sources: list[dict] = []
    round_lines: list[str] = []
    ref_lines: list[str] = []
    ref_num = max_ref_number()
    round_refs: dict[int, list[int]] = {}

    for item in items:
        source_id = next_source_id(source_ids)
        source_ids.append(source_id)
        ref_num += 1
        round_refs.setdefault(item["round"], []).append(ref_num)
        source = {
            "source_id": source_id,
            "source_type": item.get("source_type", "primary"),
            "label": item["label"],
            "url": item["url"],
            "doi": item.get("doi"),
            "access_date": "2026-08-07",
            "note": item.get("source_note", "Crossref/DOI 元数据核验。"),
        }
        new_sources.append(source)

        prefix = EVENT_PREFIX[item["event_type"]]
        event_id = next_id(event_ids, prefix)
        event_ids.append(event_id)
        event = {
            "event_id": event_id,
            "title": item["title"],
            "date_start": item.get("date_start", "2026"),
            "date_type": item.get("date_type", "approx"),
            "period_id": item.get("period_id", "period-21st-century"),
            "civilization": item.get("civilization", "International"),
            "region": item.get("region", "Global"),
            "path_family": item["path_family"],
            "event_type": item["event_type"],
            "claim": item["claim"],
            "summary": item["summary"],
            "sources": [source_id],
            "evidence_grade": item.get("evidence_grade", "S"),
            "verification_status": "unreviewed",
            "status": "draft",
            "significance": item.get("significance", "medium"),
            "uncertainty": item.get(
                "uncertainty",
                "本记录基于期刊元数据和论文标题，尚未完成全文语境复核。",
            ),
            "cross_links": [],
            "chapter": item["chapter"],
            "notes": f"第 {item['round']} 轮补录：{item['topic']}；待本地复核。",
            "created_at": timestamp,
            "updated_at": timestamp,
        }
        new_events.append(event)

        ref_lines.append(
            f'[{ref_num}]: {item["url"]} "{item["label"]}"'
        )

    timeline["events"].extend(new_events)
    timeline["version"] = bump_version(timeline["version"])
    sources["sources"].extend(new_sources)
    sources["version"] = bump_version(sources["version"])

    dump(PACKAGE / "timeline.json", timeline)
    dump(PACKAGE / "sources.json", sources)

    for round_no in sorted({item["round"] for item in items}):
        round_items = [item for item in items if item["round"] == round_no]
        inserted_by_round: list[str] = []
        for event in new_events:
            for item in round_items:
                if item["title"] == event["title"] and event["event_id"] not in inserted_by_round:
                    inserted_by_round.append(event["event_id"])
        ids = inserted_by_round
        refs = "、".join(f"[{num}]" for num in round_refs[round_no])
        round_line = (
            f"## 年表工程第{round_no}轮补录（{round_items[0]['topic']}，2026-08-07）\n\n"
            f"第{round_no}轮补录来源为{round_items[0]['topic']}方向精选论文节点，\n"
            "共新增 5 条事件、5 张来源卡。\n新增事件 ID 如下：\n\n"
            + "\n".join(f"- {event_id}" for event_id in ids)
            + f"\n\n本轮核验方法：五篇论文使用 Crossref/DOI 元数据核验\n{refs}。"
        )
        round_lines.append(round_line)

    readme_round_lines = []
    for round_no in sorted({item["round"] for item in items}):
        round_items = [item for item in items if item["round"] == round_no]
        titles = "、".join(f"《{item['label']}》论文发表" for item in round_items)
        readme_round_lines.append(f"第{round_no}轮补录来源：{round_items[0]['topic']}；新增 {titles}。")

    update_readme(len(timeline["events"]), len(sources["sources"]), readme_round_lines)
    update_source_note(round_lines, ref_lines)

    print(
        f"status=OK version={timeline['version']} "
        f"events={len(timeline['events'])} sources={len(sources['sources'])} "
        f"added_events={len(new_events)} added_sources={len(new_sources)}"
    )


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"error: {message}")


if __name__ == "__main__":
    main()
