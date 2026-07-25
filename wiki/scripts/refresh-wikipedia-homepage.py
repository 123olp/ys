#!/usr/bin/env python3
"""固定中文维基百科首页的原始源码、样式和渲染结果。"""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


WIKI_DIR = Path(__file__).resolve().parents[1]
SNAPSHOT_DIR = WIKI_DIR / "homepage-upstream" / "snapshot"
API = "https://zh.wikipedia.org/w/api.php"
USER_AGENT = "HumanInfraHomepageVendor/1.0 (tradecatlabs; local research wiki)"
PAGES = {
    "Wikipedia:首页": "Wikipedia_Home.wiki",
    "Wikipedia:首页/banner": "Wikipedia_Home_banner.wiki",
    "Wikipedia:首页/styles.css": "Wikipedia_Home_styles.css",
}


def fetch_json(params: dict[str, str]) -> dict:
    url = f"{API}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def sha256(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="写入新的固定快照；省略时只显示远端修订信息",
    )
    args = parser.parse_args()

    query = fetch_json(
        {
            "action": "query",
            "prop": "revisions",
            "rvprop": "ids|timestamp|content",
            "rvslots": "main",
            "titles": "|".join(PAGES),
            "format": "json",
            "formatversion": "2",
        }
    )

    files: dict[str, str] = {}
    pages: dict[str, dict[str, str | int]] = {}
    for page in query["query"]["pages"]:
        revision = page["revisions"][0]
        content = revision["slots"]["main"]["content"]
        filename = PAGES[page["title"]]
        files[filename] = content
        pages[page["title"]] = {
            "filename": filename,
            "revid": revision["revid"],
            "timestamp": revision["timestamp"],
            "sha256": sha256(content),
            "source_url": f"https://zh.wikipedia.org/w/index.php?title={urllib.parse.quote(page['title'])}&oldid={revision['revid']}",
        }

    parsed = fetch_json(
        {
            "action": "parse",
            "oldid": str(pages["Wikipedia:首页"]["revid"]),
            "prop": "text",
            "format": "json",
            "formatversion": "2",
        }
    )
    rendered = parsed["parse"]["text"]
    rendered_filename = "Wikipedia_Home_rendered.html"
    files[rendered_filename] = rendered

    metadata = {
        "schema_version": 1,
        "source": "Chinese Wikipedia",
        "license": "CC BY-SA 4.0",
        "api": API,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "pages": pages,
        "rendered": {
            "filename": rendered_filename,
            "pageid": parsed["parse"]["pageid"],
            "title": parsed["parse"]["title"],
            "sha256": sha256(rendered),
        },
    }

    for title, record in sorted(pages.items()):
        print(f"{title}: revid={record['revid']} timestamp={record['timestamp']}")

    if not args.write:
        return

    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    for filename, content in files.items():
        (SNAPSHOT_DIR / filename).write_text(content, encoding="utf-8")
    (SNAPSHOT_DIR / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"已写入官方首页快照: {SNAPSHOT_DIR}")


if __name__ == "__main__":
    main()
