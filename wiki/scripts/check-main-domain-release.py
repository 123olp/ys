#!/usr/bin/env python3
"""校验主域名完全复用 MediaWiki 静态首页与 Vector 资源。"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from bs4.element import NavigableString


RESOURCE_DIRECTORIES = ("assets", "images", "resources")
LOCAL_ASSET_PREFIXES = ("/assets/", "/images/", "/resources/")
FORBIDDEN_RUNTIME_ENTRIES = (
    "_worker.js",
    "_routes.json",
    "functions",
    "adapter.js",
    "languages.json",
    "runtime-config.js",
)
ALLOWED_GENERATED_FILES = {
    "_headers",
    "404.html",
    "entity.jsonld",
    "healthz",
    "index.html",
    "llms.txt",
    "robots.txt",
    "sitemap.xml",
}
REQUIRED_DOM_SELECTORS = (
    "body.mediawiki.skin-vector.skin-vector-2022",
    "header.vector-header.mw-header",
    ".mw-page-container",
    "main.mw-body#content",
    ".mw-parser-output",
    "footer#footer",
)


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


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def dom_signature(soup: BeautifulSoup) -> list[tuple[str, str, tuple[str, ...]]]:
    return [
        (
            node.name,
            node.get("id", ""),
            tuple(sorted(node.get("class", []))),
        )
        for node in soup.find_all(True)
    ]


def style_signature(soup: BeautifulSoup) -> list[str]:
    return [
        hashlib.sha256(style.encode("utf-8")).hexdigest()
        for style in (node.string or "" for node in soup.find_all("style"))
    ]


def script_sources(soup: BeautifulSoup) -> list[str]:
    return [node.get("src", "") for node in soup.find_all("script") if node.get("src")]


def content_signature(soup: BeautifulSoup) -> list[str]:
    return [
        str(node)
        for node in soup.find_all(string=True)
        if isinstance(node, NavigableString)
        and not (
            node.parent is not None
            and node.parent.name == "script"
            and node.parent.get("type") == "application/ld+json"
        )
    ]


def non_route_attribute_signature(
    soup: BeautifulSoup,
) -> list[tuple[str, tuple[tuple[str, object], ...]]]:
    signature = []
    for node in soup.find_all(True):
        attributes = dict(node.attrs)
        if node.has_attr("href") and not (
            node.name == "link" and "stylesheet" in node.get("rel", [])
        ):
            attributes.pop("href", None)
        if node.name == "form":
            attributes.pop("action", None)
        if node.name == "meta" and node.get("property") == "og:url":
            attributes.pop("content", None)
        signature.append(
            (
                node.name,
                tuple(
                    sorted(
                        (name, tuple(value) if isinstance(value, list) else value)
                        for name, value in attributes.items()
                    )
                ),
            )
        )
    return signature


def files_under(directory: Path) -> dict[str, str]:
    return {
        path.relative_to(directory).as_posix(): sha256(path)
        for path in sorted(directory.rglob("*"))
        if path.is_file()
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--source-wiki", type=Path, required=True)
    parser.add_argument("--portal-url", required=True)
    parser.add_argument("--wiki-url", required=True)
    parser.add_argument("--technology-tree-url", required=True)
    args = parser.parse_args()

    directory = args.directory.resolve()
    source_wiki = args.source_wiki.resolve()
    portal_url = normalize_url(args.portal_url)
    wiki_url = normalize_url(args.wiki_url)
    technology_tree_url = normalize_url(args.technology_tree_url)

    index_path = directory / "index.html"
    source_index_path = source_wiki / "index.html"
    require(index_path.is_file(), "主域名缺少 MediaWiki index.html")
    require(source_index_path.is_file(), "校验缺少 MediaWiki 静态源首页")
    for filename in (
        "404.html",
        "healthz",
        "robots.txt",
        "sitemap.xml",
        "llms.txt",
        "entity.jsonld",
    ):
        require((directory / filename).is_file(), f"主域名缺少 {filename}")
    for forbidden in FORBIDDEN_RUNTIME_ENTRIES:
        require(
            not (directory / forbidden).exists(),
            f"主域名禁止包含自写前端或请求时计算入口: {forbidden}",
        )

    expected_files = set(ALLOWED_GENERATED_FILES)
    for resource_directory in RESOURCE_DIRECTORIES:
        expected_files.update(
            f"{resource_directory}/{path}"
            for path in files_under(source_wiki / resource_directory)
        )
    actual_files = set(files_under(directory))
    require(
        actual_files == expected_files,
        "主域名发布物包含非 MediaWiki 资源或缺少受控发布文件: "
        f"extra={sorted(actual_files - expected_files)} "
        f"missing={sorted(expected_files - actual_files)}",
    )

    page_pairs = []
    for filename in ("index.html", "404.html"):
        source_soup = BeautifulSoup(
            (source_wiki / filename).read_text(encoding="utf-8"),
            "lxml",
        )
        output_soup = BeautifulSoup(
            (directory / filename).read_text(encoding="utf-8"),
            "lxml",
        )
        for selector in REQUIRED_DOM_SELECTORS:
            require(
                output_soup.select_one(selector) is not None,
                f"{filename} 缺少 MediaWiki/Vector DOM 契约: {selector}",
            )
        require(
            dom_signature(output_soup) == dom_signature(source_soup),
            f"{filename} 修改了 MediaWiki DOM 标签、ID 或 class",
        )
        require(
            content_signature(output_soup) == content_signature(source_soup),
            f"{filename} 修改了 MediaWiki 可见内容或内联资源",
        )
        require(
            non_route_attribute_signature(output_soup)
            == non_route_attribute_signature(source_soup),
            f"{filename} 修改了 MediaWiki 非路由属性",
        )
        source_links = source_soup.select("[href]")
        output_links = output_soup.select("[href]")
        require(
            len(source_links) == len(output_links),
            f"{filename} 修改了 MediaWiki 链接节点数量",
        )
        for source_link, output_link in zip(source_links, output_links, strict=True):
            expected_href = (
                technology_tree_url
                if source_link.get("title") == "历史技术谱系"
                else rewrite_internal_url(
                    source_link.get("href", ""),
                    wiki_url=wiki_url,
                    keep_root=filename == "index.html",
                )
            )
            if (
                filename == "index.html"
                and source_link.name == "link"
                and "canonical" in source_link.get("rel", [])
            ):
                expected_href = portal_url
            require(
                output_link.get("href") == expected_href,
                f"{filename} 包含未经契约允许的链接改写: "
                f"{source_link.get('href')} -> {output_link.get('href')}",
            )
        source_forms = source_soup.select("form[action]")
        output_forms = output_soup.select("form[action]")
        require(
            len(source_forms) == len(output_forms),
            f"{filename} 修改了 MediaWiki 表单数量",
        )
        for source_form, output_form in zip(source_forms, output_forms, strict=True):
            require(
                output_form.get("action")
                == rewrite_internal_url(
                    source_form.get("action", ""),
                    wiki_url=wiki_url,
                ),
                f"{filename} 包含未经契约允许的表单路由改写",
            )
        source_og_url = source_soup.select_one("meta[property='og:url']")
        output_og_url = output_soup.select_one("meta[property='og:url']")
        require(
            (source_og_url is None) == (output_og_url is None),
            f"{filename} 修改了 MediaWiki Open Graph 元数据结构",
        )
        if source_og_url is not None and output_og_url is not None:
            expected_og_url = (
                portal_url
                if filename == "index.html"
                else source_og_url.get("content")
            )
            require(
                output_og_url.get("content") == expected_og_url,
                f"{filename} 包含未经契约允许的 Open Graph URL 改写",
            )
        source_json_ld = source_soup.select("script[type='application/ld+json']")
        output_json_ld = output_soup.select("script[type='application/ld+json']")
        require(
            len(source_json_ld) == len(output_json_ld),
            f"{filename} 修改了 MediaWiki JSON-LD 数量",
        )
        for source_script, output_script in zip(
            source_json_ld,
            output_json_ld,
            strict=True,
        ):
            try:
                expected_payload = json.loads(source_script.string or "")
                output_payload = json.loads(output_script.string or "")
            except json.JSONDecodeError as error:
                raise RuntimeError(
                    f"{filename} 包含不可解析的 MediaWiki JSON-LD"
                ) from error
            if filename == "index.html" and isinstance(expected_payload, dict):
                expected_payload["url"] = portal_url
            require(
                output_payload == expected_payload,
                f"{filename} 包含未经契约允许的 JSON-LD 改写",
            )
        require(
            style_signature(output_soup) == style_signature(source_soup),
            f"{filename} 新增或修改了 MediaWiki TemplateStyles",
        )
        require(
            script_sources(output_soup) == script_sources(source_soup),
            f"{filename} 新增或修改了 MediaWiki 脚本依赖",
        )
        require(
            [
                node.get("href")
                for node in output_soup.select("link[rel~='stylesheet']")
            ]
            == [
                node.get("href")
                for node in source_soup.select("link[rel~='stylesheet']")
            ],
            f"{filename} 新增或替换了 MediaWiki 样式表",
        )
        page_pairs.append((filename, output_soup))

    output_soup = page_pairs[0][1]
    generator = output_soup.select_one("meta[name='generator']")
    require(
        generator is not None
        and generator.get("content", "").startswith("MediaWiki "),
        "主域名首页不是 MediaWiki 生成物",
    )
    for resource_directory in RESOURCE_DIRECTORIES:
        source_files = files_under(source_wiki / resource_directory)
        output_files = files_under(directory / resource_directory)
        require(
            output_files == source_files,
            f"主域名 {resource_directory}/ 未原样复用 MediaWiki 资源",
        )

    canonical = output_soup.select_one("link[rel='canonical']")
    search_form = output_soup.select_one("form#searchform")
    require(canonical is not None, "主域名缺少 canonical")
    require(canonical.get("href") == portal_url, "主域名 canonical 不一致")
    require(search_form is not None, "主域名缺少 MediaWiki 原生搜索表单")
    require(
        search_form.get("action") == f"{wiki_url}search/",
        "主域名搜索未路由到正式 Wiki",
    )
    require(
        any(
            link.get("href") == technology_tree_url
            for link in output_soup.select("a[href]")
        ),
        "MediaWiki 首页内容缺少科技树入口",
    )
    require(
        any(
            link.get("href", "").startswith(f"{wiki_url}wiki/")
            for link in output_soup.select("a[href]")
        ),
        "MediaWiki 首页词条链接未路由到正式 Wiki",
    )
    for link in output_soup.select("a[href]"):
        href = link.get("href", "")
        require(
            not href.startswith("/wiki/"),
            f"主域名残留不可达的本地 Wiki 路由: {href}",
        )
        parsed = urlparse(href)
        allowed_local = (
            href in {"", "/"}
            or href.startswith(("#", "javascript:", "mailto:"))
            or href.startswith(("/assets/", "/images/", "/resources/"))
        )
        require(
            allowed_local or bool(parsed.scheme) or bool(parsed.netloc),
            f"主域名残留未改写的相对导航链接: {href}",
        )

    require(
        f"Sitemap: {portal_url}sitemap.xml"
        in (directory / "robots.txt").read_text(encoding="utf-8"),
        "主域名 robots.txt 未声明正式 sitemap",
    )
    headers = (directory / "_headers").read_text(encoding="utf-8")
    require(
        headers.count(
            "Cache-Control: public, max-age=0, must-revalidate, no-transform"
        )
        == 2,
        "主域名 HTML 未禁止 Cloudflare 等边缘层修改 MediaWiki 页面",
    )
    structured_data = json.loads(
        (directory / "entity.jsonld").read_text(encoding="utf-8")
    )
    require(structured_data.get("url") == portal_url, "主域名实体 URL 不一致")
    require(wiki_url in structured_data.get("sameAs", []), "实体图缺少 Wiki")
    require(
        technology_tree_url in structured_data.get("sameAs", []),
        "实体图缺少科技树",
    )
    print("主域名 MediaWiki 原生框架与静态路由契约通过。")


if __name__ == "__main__":
    main()
