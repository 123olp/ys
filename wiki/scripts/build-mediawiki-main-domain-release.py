#!/usr/bin/env python3
"""从 MediaWiki 静态首页生成主域名发布物，不创建前端框架。"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup


LOCAL_ASSET_PREFIXES = ("/assets/", "/images/", "/resources/")


def normalize_url(value: str) -> str:
    return value.rstrip("/") + "/"


def rewrite_internal_url(
    value: str,
    *,
    wiki_url: str,
    keep_root: bool = False,
) -> str:
    if not value or value.startswith(("#", "javascript:", "mailto:")):
        return value
    parsed = urlparse(value)
    if parsed.scheme or parsed.netloc:
        return value
    if value == "/" and keep_root:
        return "/"
    if value.startswith(LOCAL_ASSET_PREFIXES):
        return value
    if value.startswith("/"):
        return f"{wiki_url}{value.lstrip('/')}"
    return value


def transform_page(
    source_path: Path,
    target_path: Path,
    *,
    portal_url: str,
    wiki_url: str,
    technology_tree_url: str,
    is_index: bool,
) -> None:
    soup = BeautifulSoup(source_path.read_text(encoding="utf-8"), "lxml")

    for node in soup.select("[href]"):
        if node.get("title") == "历史技术谱系":
            node["href"] = technology_tree_url
        else:
            node["href"] = rewrite_internal_url(
                node["href"],
                wiki_url=wiki_url,
                keep_root=is_index,
            )
    for form in soup.select("form[action]"):
        form["action"] = rewrite_internal_url(
            form["action"],
            wiki_url=wiki_url,
        )

    if is_index:
        canonical = soup.select_one("link[rel='canonical']")
        if canonical is None:
            raise RuntimeError("MediaWiki 首页缺少 canonical")
        canonical["href"] = portal_url
        for selector in ("meta[property='og:url']",):
            node = soup.select_one(selector)
            if node is not None:
                node["content"] = portal_url
        for script in soup.select("script[type='application/ld+json']"):
            try:
                payload = json.loads(script.string or "")
            except json.JSONDecodeError:
                continue
            if isinstance(payload, dict):
                payload["url"] = portal_url
                script.string = json.dumps(
                    payload,
                    ensure_ascii=False,
                    separators=(",", ":"),
                ).replace("<", "\\u003c")

    target_path.write_text(str(soup), encoding="utf-8")


def build(
    source_wiki_dir: Path,
    output_dir: Path,
    *,
    portal_url: str,
    wiki_url: str,
    technology_tree_url: str,
) -> None:
    source_wiki_dir = source_wiki_dir.resolve()
    portal_url = normalize_url(portal_url)
    wiki_url = normalize_url(wiki_url)
    technology_tree_url = normalize_url(technology_tree_url)

    for filename in ("index.html", "404.html"):
        if not (source_wiki_dir / filename).is_file():
            raise RuntimeError(f"MediaWiki 静态源缺少 {filename}")

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    for directory in ("assets", "images", "resources"):
        source = source_wiki_dir / directory
        if not source.is_dir():
            raise RuntimeError(f"MediaWiki 静态源缺少资源目录: {directory}")
        shutil.copytree(source, output_dir / directory)

    transform_page(
        source_wiki_dir / "index.html",
        output_dir / "index.html",
        portal_url=portal_url,
        wiki_url=wiki_url,
        technology_tree_url=technology_tree_url,
        is_index=True,
    )
    transform_page(
        source_wiki_dir / "404.html",
        output_dir / "404.html",
        portal_url=portal_url,
        wiki_url=wiki_url,
        technology_tree_url=technology_tree_url,
        is_index=False,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-wiki", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--portal-url", required=True)
    parser.add_argument("--wiki-url", required=True)
    parser.add_argument("--technology-tree-url", required=True)
    args = parser.parse_args()
    build(
        args.source_wiki,
        args.output.resolve(),
        portal_url=args.portal_url,
        wiki_url=args.wiki_url,
        technology_tree_url=args.technology_tree_url,
    )


if __name__ == "__main__":
    main()
