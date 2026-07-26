#!/usr/bin/env python3
"""把本地 MediaWiki 渲染结果导出为 Cloudflare Pages 只读快照。"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import html
import json
import re
import shutil
import sys
import threading
import time
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "runtime" / "pages" / "wiki"
MAIN_PAGE = "Human Infra:首页"
SHELL_PAGE = "有效永生与主体持续性"
ASSET_URL_PATTERN = re.compile(r"url\((?P<value>[^)]+)\)")
SKIPPED_NAMESPACES = {-2, -1}
REQUEST_TIMEOUT = 30
THREAD_LOCAL = threading.local()


def request_json(
    session: requests.Session,
    api_url: str,
    params: dict[str, Any],
) -> dict[str, Any]:
    for attempt in range(4):
        response = session.get(api_url, params=params, timeout=REQUEST_TIMEOUT)
        if response.ok:
            return response.json()
        if attempt == 3:
            response.raise_for_status()
        time.sleep(2**attempt)
    raise RuntimeError("无法读取 MediaWiki API")


def list_exportable_pages(
    session: requests.Session,
    api_url: str,
) -> list[str]:
    siteinfo = request_json(
        session,
        api_url,
        {
            "action": "query",
            "meta": "siteinfo",
            "siprop": "namespaces",
            "format": "json",
            "formatversion": "2",
        },
    )
    namespace_ids = sorted(
        namespace["id"]
        for namespace in siteinfo["query"]["namespaces"].values()
        if namespace["id"] not in SKIPPED_NAMESPACES
        and namespace["id"] >= 0
        and namespace["id"] % 2 == 0
    )

    titles: list[str] = []
    for namespace_id in namespace_ids:
        continuation: dict[str, Any] = {}
        while True:
            payload = request_json(
                session,
                api_url,
                {
                    "action": "query",
                    "list": "allpages",
                    "apnamespace": namespace_id,
                    "aplimit": "max",
                    "format": "json",
                    "formatversion": "2",
                    **continuation,
                },
            )
            titles.extend(page["title"] for page in payload["query"]["allpages"])
            if "continue" not in payload:
                break
            continuation = payload["continue"]
    return sorted(set(titles), key=str.casefold)


def normalize_title(title: str) -> str:
    return unquote(title).replace("_", " ").strip()


def page_filename(title: str) -> str:
    digest = hashlib.sha256(title.encode("utf-8")).hexdigest()
    return f"{digest}.json"


def fetch_page(
    api_url: str,
    title: str,
) -> dict[str, Any]:
    session = getattr(THREAD_LOCAL, "session", None)
    if session is None:
        session = requests.Session()
        session.headers["User-Agent"] = "HumanInfraWikiPagesExporter/1.0"
        THREAD_LOCAL.session = session
    payload = request_json(
        session,
        api_url,
        {
            "action": "parse",
            "page": title,
            "prop": "text|displaytitle|categorieshtml|revid",
            "redirects": "1",
            "format": "json",
            "formatversion": "2",
        },
    )
    parsed = payload["parse"]
    return {
        "sourceTitle": title,
        "title": parsed["title"],
        "displayTitle": parsed.get("displaytitle") or html.escape(parsed["title"]),
        "body": parsed["text"],
        "categories": parsed.get("categorieshtml", ""),
        "revision": parsed.get("revid"),
    }


def fetch_text(
    session: requests.Session,
    url: str,
) -> tuple[str, str]:
    response = session.get(url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.text, response.headers.get("content-type", "")


def extension_for(content_type: str, url: str) -> str:
    media_type = content_type.split(";", 1)[0].strip().lower()
    mapping = {
        "image/svg+xml": ".svg",
        "image/png": ".png",
        "image/jpeg": ".jpg",
        "image/gif": ".gif",
        "image/webp": ".webp",
        "font/woff": ".woff",
        "font/woff2": ".woff2",
    }
    if media_type in mapping:
        return mapping[media_type]
    suffix = Path(urlparse(url).path).suffix
    return suffix if suffix and len(suffix) <= 8 else ".bin"


def localize_css(
    session: requests.Session,
    base_url: str,
    css_text: str,
    output_dir: Path,
) -> str:
    asset_dir = output_dir / "assets" / "mediawiki"
    asset_dir.mkdir(parents=True, exist_ok=True)

    def replace(match: re.Match[str]) -> str:
        raw = match.group("value").strip()
        quote = raw[0] if raw[:1] in {"'", '"'} else ""
        value = raw[1:-1] if quote and raw[-1:] == quote else raw
        if value.startswith(("data:", "#", "http://", "https://", "//")):
            return match.group(0)

        resource_url = urljoin(base_url, value)
        response = session.get(resource_url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        digest = hashlib.sha256(resource_url.encode("utf-8")).hexdigest()[:20]
        suffix = extension_for(
            response.headers.get("content-type", ""),
            resource_url,
        )
        target = asset_dir / f"{digest}{suffix}"
        if not target.exists():
            target.write_bytes(response.content)
        return f"url('/assets/mediawiki/{target.name}')"

    return ASSET_URL_PATTERN.sub(replace, css_text)


def build_shell(
    session: requests.Session,
    base_url: str,
    output_dir: Path,
) -> None:
    response = session.get(
        f"{base_url}/index.php",
        params={"title": SHELL_PAGE},
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")

    for script in soup.find_all("script"):
        script.decompose()
    for selector in (
        "#p-personal",
        "#ca-edit",
        "#ca-ve-edit",
        "#ca-history",
        "#ca-watch",
        "#ca-unwatch",
    ):
        for node in soup.select(selector):
            node.decompose()
    for link in soup.select(
        "link[rel='alternate'], link[rel='EditURI'], "
        "link[type='application/atom+xml'], link[rel='search']"
    ):
        link.decompose()

    stylesheets: list[str] = []
    for link in soup.select("link[rel~='stylesheet'][href]"):
        stylesheet_url = urljoin(base_url, link["href"])
        stylesheet, _ = fetch_text(session, stylesheet_url)
        stylesheets.append(localize_css(
            session,
            stylesheet_url,
            stylesheet,
            output_dir,
        ))
        link.decompose()
    style_link = soup.new_tag("link", rel="stylesheet", href="/assets/mediawiki.css")
    soup.head.append(style_link)

    if soup.title:
        soup.title.string = "__HI_DOCUMENT_TITLE__"
    heading = soup.select_one("#firstHeading")
    if heading:
        heading.clear()
        heading.append("__HI_DISPLAY_TITLE__")
    content = soup.select_one("#mw-content-text")
    if content is None:
        raise RuntimeError("MediaWiki 页面缺少 #mw-content-text")
    content.clear()
    content.append("__HI_CONTENT__")
    categories = soup.select_one("#catlinks")
    if categories:
        categories.replace_with("__HI_CATEGORIES__")
    last_modified = soup.select_one("#footer-info-lastmod")
    if last_modified:
        last_modified.clear()
        last_modified.append("__HI_REVISION__")

    canonical = soup.select_one("link[rel='canonical']")
    if canonical:
        canonical["href"] = "__HI_CANONICAL__"
    else:
        canonical = soup.new_tag(
            "link",
            rel="canonical",
            href="__HI_CANONICAL__",
        )
        soup.head.append(canonical)

    output_dir.joinpath("assets").mkdir(parents=True, exist_ok=True)
    output_dir.joinpath("assets", "mediawiki.css").write_text(
        "\n".join(stylesheets),
        encoding="utf-8",
    )
    output_dir.joinpath("snapshot", "shell.html").parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    shell = str(soup)
    for token in (
        "__HI_DOCUMENT_TITLE__",
        "__HI_DISPLAY_TITLE__",
        "__HI_CONTENT__",
        "__HI_CATEGORIES__",
        "__HI_REVISION__",
        "__HI_CANONICAL__",
    ):
        shell = shell.replace(html.escape(token), token)
    output_dir.joinpath("snapshot", "shell.html").write_text(
        shell,
        encoding="utf-8",
    )


def copy_media(output_dir: Path) -> None:
    images = ROOT / "runtime" / "images"
    if images.exists():
        shutil.copytree(
            images,
            output_dir / "images",
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns("archive"),
        )
    resource_dir = output_dir / "resources" / "assets"
    license_dir = resource_dir / "licenses"
    license_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(
        ROOT / "portal" / "assets" / "human-infra-mark.svg",
        resource_dir / "human-infra-mark.svg",
    )


def write_worker(output_dir: Path) -> None:
    source = ROOT / "pages" / "wiki-worker.js"
    if not source.is_file():
        raise RuntimeError(f"缺少 Pages Worker: {source}")
    shutil.copy2(source, output_dir / "_worker.js")


def export_snapshot(base_url: str, output_dir: Path, workers: int) -> None:
    api_url = f"{base_url}/api.php"
    session = requests.Session()
    session.headers["User-Agent"] = "HumanInfraWikiPagesExporter/1.0"

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    titles = list_exportable_pages(session, api_url)
    if MAIN_PAGE not in titles:
        raise RuntimeError(f"缺少项目首页: {MAIN_PAGE}")

    build_shell(session, base_url, output_dir)
    pages_dir = output_dir / "snapshot" / "pages"
    pages_dir.mkdir(parents=True)
    index_by_title: dict[str, dict[str, Any]] = {}
    failures: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(fetch_page, api_url, title): title
            for title in titles
        }
        for position, future in enumerate(
            concurrent.futures.as_completed(futures),
            start=1,
        ):
            title = futures[future]
            try:
                page = future.result()
            except Exception as exc:  # noqa: BLE001 - 末尾统一报告失败
                failures.append(f"{title}: {exc}")
                continue
            filename = page_filename(page["title"])
            pages_dir.joinpath(filename).write_text(
                json.dumps(
                    {
                        key: value
                        for key, value in page.items()
                        if key != "sourceTitle"
                    },
                    ensure_ascii=False,
                    separators=(",", ":"),
                ),
                encoding="utf-8",
            )
            normalized = normalize_title(page["title"]).casefold()
            entry = index_by_title.setdefault(
                normalized,
                {
                    "title": page["title"],
                    "normalized": normalized,
                    "file": filename,
                    "aliases": [],
                },
            )
            source_title = page["sourceTitle"]
            if normalize_title(source_title).casefold() != normalized:
                entry["aliases"].append(source_title)
            if position % 250 == 0:
                print(f"已导出 {position}/{len(titles)}", file=sys.stderr)

    if failures:
        raise RuntimeError("页面导出失败:\n" + "\n".join(failures[:20]))

    index = sorted(
        index_by_title.values(),
        key=lambda page: page["title"].casefold(),
    )
    for entry in index:
        entry["aliases"] = sorted(set(entry["aliases"]), key=str.casefold)
    page_files = list(pages_dir.glob("*.json"))
    if len(page_files) != len(index):
        raise RuntimeError(
            "快照实体与索引数量不一致: "
            f"files={len(page_files)} index={len(index)}"
        )
    alias_count = sum(len(entry["aliases"]) for entry in index)
    output_dir.joinpath("snapshot", "index.json").write_text(
        json.dumps(
            {
                "generatedAt": time.strftime(
                    "%Y-%m-%dT%H:%M:%SZ",
                    time.gmtime(),
                ),
                "mainPage": MAIN_PAGE,
                "pageCount": len(index),
                "sourcePageCount": len(titles),
                "aliasCount": alias_count,
                "pages": index,
            },
            ensure_ascii=False,
            separators=(",", ":"),
        ),
        encoding="utf-8",
    )
    copy_media(output_dir)
    write_worker(output_dir)
    output_dir.joinpath("_headers").write_text(
        "/assets/*\n"
        "  Cache-Control: public, max-age=31536000, immutable\n"
        "/snapshot/pages/*\n"
        "  Cache-Control: public, max-age=3600\n"
        "/snapshot/index.json\n"
        "  Cache-Control: public, max-age=300\n",
        encoding="utf-8",
    )
    print(
        "Wiki 快照完成: "
        f"pages={len(index)} aliases={alias_count} output={output_dir}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base-url",
        default="http://127.0.0.1:18782",
        help="本地 MediaWiki 基址",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Pages 发布目录",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=8,
        help="本地 MediaWiki 有界并发请求数",
    )
    args = parser.parse_args()
    if not 1 <= args.workers <= 16:
        parser.error("--workers 必须在 1 到 16 之间")
    export_snapshot(
        args.base_url.rstrip("/"),
        args.output.resolve(),
        args.workers,
    )


if __name__ == "__main__":
    main()
