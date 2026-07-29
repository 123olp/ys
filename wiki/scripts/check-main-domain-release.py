#!/usr/bin/env python3
"""校验主域名门户的静态发布与路由契约。"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup


def normalize_url(value: str) -> str:
    return value.rstrip("/") + "/"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--portal-url", required=True)
    parser.add_argument("--wiki-url", required=True)
    parser.add_argument("--technology-tree-url", required=True)
    args = parser.parse_args()

    directory = args.directory.resolve()
    portal_url = normalize_url(args.portal_url)
    wiki_url = normalize_url(args.wiki_url)
    technology_tree_url = normalize_url(args.technology_tree_url)
    index_path = directory / "index.html"

    require(index_path.is_file(), "主域名门户缺少 index.html")
    for filename in (
        "404.html",
        "runtime-config.js",
        "robots.txt",
        "sitemap.xml",
        "llms.txt",
        "entity.jsonld",
    ):
        require((directory / filename).is_file(), f"主域名门户缺少 {filename}")
    for forbidden in ("_worker.js", "_routes.json", "functions"):
        require(
            not (directory / forbidden).exists(),
            f"主域名门户禁止包含请求时计算入口: {forbidden}",
        )

    soup = BeautifulSoup(index_path.read_text(encoding="utf-8"), "lxml")
    source_html = index_path.read_text(encoding="utf-8")
    canonical = soup.select_one("link[rel='canonical']")
    search_form = soup.select_one("#search-form")
    tree_link = next(
        (
            link
            for link in soup.select("a.other-project-link[href]")
            if link.get("href") == technology_tree_url
        ),
        None,
    )
    require(canonical is not None, "主域名门户缺少 canonical")
    require(canonical.get("href") == portal_url, "主域名 canonical 不一致")
    require(search_form is not None, "主域名门户缺少搜索表单")
    require(
        search_form.get("action") == f"{wiki_url}search/",
        "主域名门户搜索未指向正式 Wiki",
    )
    require(tree_link is not None, "主域名门户缺少科技树入口")
    translations_hash_match = re.search(
        r"translationsHash\s*=\s*['\"]([a-f0-9]+)['\"]",
        source_html,
    )
    require(
        translations_hash_match is not None,
        "主域名门户缺少 Wikimedia 本地化资源版本",
    )
    translations_hash = translations_hash_match.group(1)
    for locale in ("zh-hans", "zh-hant"):
        translation_path = (
            directory
            / "portal"
            / "wikipedia.org"
            / "assets"
            / "l10n"
            / f"{locale}-{translations_hash}.json"
        )
        require(
            translation_path.is_file(),
            f"主域名门户缺少 Wikimedia 本地化资源: {translation_path.name}",
        )
        translation = json.loads(translation_path.read_text(encoding="utf-8"))
        require(
            translation.get("code") == locale,
            f"Wikimedia 本地化资源语言代码不一致: {translation_path.name}",
        )

    runtime_config = (directory / "runtime-config.js").read_text(encoding="utf-8")
    require(wiki_url in runtime_config, "主域名运行时配置未指向正式 Wiki")
    require(
        f"Sitemap: {portal_url}sitemap.xml"
        in (directory / "robots.txt").read_text(encoding="utf-8"),
        "主域名 robots.txt 未声明正式 sitemap",
    )
    structured_data = json.loads(
        (directory / "entity.jsonld").read_text(encoding="utf-8")
    )
    require(structured_data.get("url") == portal_url, "主域名实体 URL 不一致")
    require(
        wiki_url in structured_data.get("sameAs", []),
        "主域名实体图缺少 Wiki",
    )
    require(
        technology_tree_url in structured_data.get("sameAs", []),
        "主域名实体图缺少科技树",
    )
    print("主域名静态门户契约通过。")


if __name__ == "__main__":
    main()
