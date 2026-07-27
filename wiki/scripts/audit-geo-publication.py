#!/usr/bin/env python3
"""校验门户和 Wiki 发布物的 GEO 机器可读契约。"""

from __future__ import annotations

import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path

from bs4 import BeautifulSoup


REQUIRED_META = (
    ("name", "description"),
    ("name", "robots"),
    ("property", "og:title"),
    ("property", "og:description"),
    ("property", "og:url"),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def audit_html(path: Path, *, placeholders: bool = False) -> None:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
    require(soup.title is not None, f"{path}: 缺少 title")
    require(soup.select_one("link[rel='canonical']") is not None, f"{path}: 缺少 canonical")
    for attribute, value in REQUIRED_META:
        node = soup.select_one(f"meta[{attribute}='{value}']")
        require(node is not None, f"{path}: 缺少 {attribute}={value}")
        require(bool(node.get("content")), f"{path}: {value} 内容为空")
    scripts = soup.select("script[type='application/ld+json']")
    require(len(scripts) == 1, f"{path}: JSON-LD 数量必须为 1")
    if placeholders:
        require(
            "__HI_STRUCTURED_DATA__" in scripts[0].get_text(),
            f"{path}: 缺少结构化数据占位符",
        )
    else:
        json.loads(scripts[0].get_text())


def audit_portal(directory: Path) -> None:
    audit_html(directory / "index.html")
    for filename in (
        "robots.txt",
        "sitemap.xml",
        "llms.txt",
        "entity.jsonld",
        "UPSTREAM.md",
    ):
        require((directory / filename).is_file(), f"门户缺少 {filename}")
    soup = BeautifulSoup(
        (directory / "index.html").read_text(encoding="utf-8"),
        "lxml",
    )
    search_form = soup.select_one("#search-form")
    search_input = soup.select_one("#searchInput")
    require(search_form is not None, "门户缺少搜索表单")
    require(search_input is not None, "门户缺少搜索输入框")
    require(
        search_form.get("action")
        == "https://human-infra-wiki.pages.dev/search/",
        "门户搜索回退 action 未指向本地 Wiki",
    )
    require(search_form.get("method") == "get", "门户搜索必须使用 GET")
    require(search_input.get("name") == "q", "门户搜索参数必须为 q")
    ET.parse(directory / "sitemap.xml")
    json.loads((directory / "entity.jsonld").read_text(encoding="utf-8"))
    require(
        "Sitemap: https://human-infra.pages.dev/sitemap.xml"
        in (directory / "robots.txt").read_text(encoding="utf-8"),
        "门户 robots.txt 缺少正式 sitemap",
    )


def audit_wiki(directory: Path) -> None:
    audit_html(directory / "index.html")
    audit_html(directory / "wiki" / "长寿逃逸速度" / "index.html")
    for filename in (
        "robots.txt",
        "sitemap.xml",
        "llms.txt",
        "geo/entity.jsonld",
        "geo/pages.ndjson",
    ):
        require((directory / filename).is_file(), f"Wiki 缺少 {filename}")
    sitemap = ET.parse(directory / "sitemap.xml")
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_urls = sitemap.findall("s:url", namespace)
    index = json.loads(
        (directory / "snapshot" / "index.json").read_text(encoding="utf-8")
    )
    ndjson_lines = [
        line
        for line in (directory / "geo" / "pages.ndjson")
        .read_text(encoding="utf-8")
        .splitlines()
        if line
    ]
    require(len(sitemap_urls) == index["pageCount"], "Wiki sitemap 与页面数不一致")
    require(len(ndjson_lines) == index["pageCount"], "Wiki NDJSON 与页面数不一致")
    require(
        len(list((directory / "wiki").rglob("index.html")))
        == index["pageCount"],
        "Wiki 静态 HTML 与页面数不一致",
    )
    require(
        not any(
            (directory / name).exists()
            for name in ("_worker.js", "_routes.json", "functions")
        ),
        "Wiki 发布物包含请求时计算入口",
    )
    for line in ndjson_lines:
        record = json.loads(line)
        require(record.get("title") and record.get("url"), "Wiki NDJSON 条目不完整")
        require(record.get("description"), "Wiki NDJSON 条目缺少摘要")
    json.loads((directory / "geo" / "entity.jsonld").read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--portal-dir", type=Path, required=True)
    parser.add_argument("--wiki-dir", type=Path, required=True)
    args = parser.parse_args()
    audit_portal(args.portal_dir.resolve())
    audit_wiki(args.wiki_dir.resolve())
    print("GEO 发布契约通过：门户与 Wiki 机器入口、页面元数据和索引一致。")


if __name__ == "__main__":
    main()
