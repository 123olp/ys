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
from urllib.parse import parse_qsl, quote, unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "runtime" / "pages" / "wiki"
GEO_CONFIG = ROOT / "config" / "geo-publication.json"
VECTOR_APPEARANCE_CONTROLS = (
    ROOT / "vector-upstream" / "appearance-controls.html"
)
VECTOR_CLIENT_PREFERENCES_SCRIPT = (
    ROOT / "scripts" / "vector-client-preferences-static.js"
)
MAIN_PAGE = "Human Infra:首页"
SHELL_PAGE = "有效永生与主体持续性"
ASSET_URL_PATTERN = re.compile(r"url\((?P<value>[^)]+)\)")
SKIPPED_NAMESPACES = {-2, -1}
REQUEST_TIMEOUT = 30
THREAD_LOCAL = threading.local()
STATIC_NOJS_CSS = """
.client-nojs .mw-portlet-lang .vector-dropdown-content{display:none}
.client-nojs .mw-portlet-lang .vector-dropdown-checkbox:checked~.vector-dropdown-content{display:block}
.client-nojs #p-lang-btn .vector-dropdown-content{left:auto;right:0;box-sizing:border-box;max-width:calc(100vw - 48px)}
.client-nojs.vector-feature-appearance-pinned-clientpref-0 .vector-user-links .vector-appearance-landmark{display:block}
@media screen and (min-width:1120px){.client-nojs.vector-feature-appearance-pinned-clientpref-1 .vector-column-end .vector-appearance-landmark{display:block}.client-nojs #vector-appearance .vector-pinnable-header-unpinned .vector-pinnable-header-pin-button,.client-nojs #vector-appearance .vector-pinnable-header-pinned .vector-pinnable-header-unpin-button{display:inline-block}}
"""


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


def extract_description(title: str, body: str) -> str:
    """提取页面首个有效正文段，作为搜索摘要而不生成新事实。"""

    soup = BeautifulSoup(body, "lxml")
    for selector in (
        "style",
        "script",
        "table",
        ".mw-empty-elt",
        ".hatnote",
        ".navbox",
        ".metadata",
    ):
        for node in soup.select(selector):
            node.decompose()
    for paragraph in soup.select("p"):
        text = " ".join(paragraph.get_text(" ", strip=True).split())
        if len(text) >= 24:
            return text[:217].rstrip() + ("..." if len(text) > 217 else "")
    return f"{title}是 Human Infra Wiki 中经过来源与边界治理的研究词条。"


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
    page_response = session.get(
        api_url.removesuffix("/api.php") + "/index.php",
        params={"title": parsed["title"]},
        timeout=REQUEST_TIMEOUT,
    )
    page_response.raise_for_status()
    page_soup = BeautifulSoup(page_response.text, "lxml")
    toc = page_soup.select_one("#vector-toc-pinned-container")
    body = parsed["text"]
    return {
        "sourceTitle": title,
        "title": parsed["title"],
        "displayTitle": parsed.get("displaytitle") or html.escape(parsed["title"]),
        "body": body,
        "description": extract_description(parsed["title"], body),
        "bodyClass": " ".join(page_soup.body.get("class", [])),
        "toc": str(toc) if toc else "",
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


def copy_document_assets(
    session: requests.Session,
    base_url: str,
    soup: BeautifulSoup,
    output_dir: Path,
) -> None:
    """复制页面 HTML 直接引用的同源资源，保持 MediaWiki 原始 URL。"""

    base = urlparse(base_url)
    values: set[str] = set()
    for node in soup.select("img[src]"):
        values.add(node["src"])
    for node in soup.select("source[srcset]"):
        values.update(
            item.strip().split()[0]
            for item in node["srcset"].split(",")
            if item.strip()
        )

    for value in values:
        asset_url = urljoin(base_url, value)
        parsed = urlparse(asset_url)
        if parsed.netloc != base.netloc or not parsed.path.startswith("/resources/"):
            continue
        target = output_dir / parsed.path.lstrip("/")
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            continue
        response = session.get(asset_url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        target.write_bytes(response.content)


def install_static_vector_appearance(
    soup: BeautifulSoup,
    output_dir: Path,
) -> None:
    """冻结 Vector 客户端生成的原生外观控件并安装静态偏好适配器。"""

    appearance = soup.select_one("#vector-appearance")
    if appearance is None:
        raise RuntimeError("Vector 页面外壳缺少 #vector-appearance")
    controls_document = BeautifulSoup(
        VECTOR_APPEARANCE_CONTROLS.read_text(encoding="utf-8"),
        "lxml",
    )
    controls = controls_document.select_one("#vector-appearance-controls")
    if controls is None:
        raise RuntimeError("Vector 外观控件快照缺少根节点")
    if len(controls.select("input[type='radio']")) != 8:
        raise RuntimeError("Vector 外观控件快照必须包含 8 个单选项")
    for child in list(controls.children):
        appearance.append(child.extract())

    assets_dir = output_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(
        VECTOR_CLIENT_PREFERENCES_SCRIPT,
        assets_dir / "vector-client-preferences.js",
    )
    script = soup.new_tag(
        "script",
        src="/assets/vector-client-preferences.js",
        defer=True,
    )
    soup.body.append(script)


def build_shell(
    session: requests.Session,
    base_url: str,
    output_dir: Path,
    source_page: str,
    shell_name: str,
) -> None:
    response = session.get(
        f"{base_url}/index.php",
        params={"title": source_page},
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

    copy_document_assets(session, base_url, soup, output_dir)
    install_static_vector_appearance(soup, output_dir)

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
    client_preferences_url = (
        f"{base_url}/load.php?lang=zh&modules="
        "skins.vector.clientPreferences&only=styles&skin=vector-2022"
    )
    client_preferences_stylesheet, _ = fetch_text(
        session,
        client_preferences_url,
    )
    stylesheets.append(localize_css(
        session,
        client_preferences_url,
        client_preferences_stylesheet,
        output_dir,
    ))
    style_link = soup.new_tag("link", rel="stylesheet", href="/assets/mediawiki.css")
    soup.head.append(style_link)
    if not soup.select_one("link[rel~='icon']"):
        icon_link = soup.new_tag(
            "link",
            rel="icon",
            href="/resources/assets/human-infra-mark.svg",
            type="image/svg+xml",
        )
        soup.head.append(icon_link)

    if soup.title:
        soup.title.string = "__HI_DOCUMENT_TITLE__"
    if soup.body:
        soup.body["class"] = "__HI_BODY_CLASS__"
    heading = soup.select_one("#firstHeading")
    if heading:
        heading.clear()
        heading.append("__HI_DISPLAY_TITLE__")
    toc = soup.select_one("#vector-toc-pinned-container")
    if toc:
        toc.replace_with("__HI_TOC__")
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

    for selector in (
        "meta[name='description']",
        "meta[name='robots']",
        "meta[property='og:title']",
        "meta[property='og:description']",
        "meta[property='og:type']",
        "meta[property='og:url']",
        "meta[property='og:site_name']",
        "meta[name='twitter:card']",
        "meta[name='twitter:title']",
        "meta[name='twitter:description']",
        "script[type='application/ld+json']",
    ):
        for node in soup.select(selector):
            node.decompose()

    metadata = (
        ("name", "description", "__HI_DESCRIPTION__"),
        ("name", "robots", "index,follow,max-image-preview:large"),
        ("property", "og:title", "__HI_DOCUMENT_TITLE__"),
        ("property", "og:description", "__HI_DESCRIPTION__"),
        ("property", "og:type", "__HI_OG_TYPE__"),
        ("property", "og:url", "__HI_CANONICAL__"),
        ("property", "og:site_name", "Human Infra Wiki"),
        ("name", "twitter:card", "summary"),
        ("name", "twitter:title", "__HI_DOCUMENT_TITLE__"),
        ("name", "twitter:description", "__HI_DESCRIPTION__"),
    )
    for attribute, key, value in metadata:
        soup.head.append(soup.new_tag(
            "meta",
            attrs={attribute: key, "content": value},
        ))
    structured_data = soup.new_tag("script", type="application/ld+json")
    structured_data.string = "__HI_STRUCTURED_DATA__"
    soup.head.append(structured_data)

    output_dir.joinpath("assets").mkdir(parents=True, exist_ok=True)
    output_dir.joinpath("assets", "mediawiki.css").write_text(
        "\n".join([*stylesheets, STATIC_NOJS_CSS]),
        encoding="utf-8",
    )
    output_dir.joinpath("snapshot", "shell.html").parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    shell = str(soup)
    encoded_source = quote(source_page.replace(" ", "_"), safe="")
    shell = shell.replace(encoded_source, "__HI_PAGE_TITLE_ENCODED__")
    shell = shell.replace(source_page.replace(" ", "_"), "__HI_PAGE_CLASS__")
    shell = shell.replace(source_page, "__HI_PAGE_TITLE__")
    shell = re.sub(r"(?<=oldid=)\d+", "__HI_REVISION_ID__", shell)
    for token in (
        "__HI_DOCUMENT_TITLE__",
        "__HI_DISPLAY_TITLE__",
        "__HI_BODY_CLASS__",
        "__HI_PAGE_TITLE__",
        "__HI_PAGE_TITLE_ENCODED__",
        "__HI_PAGE_CLASS__",
        "__HI_REVISION_ID__",
        "__HI_TOC__",
        "__HI_CONTENT__",
        "__HI_CATEGORIES__",
        "__HI_REVISION__",
        "__HI_CANONICAL__",
        "__HI_DESCRIPTION__",
        "__HI_OG_TYPE__",
        "__HI_STRUCTURED_DATA__",
    ):
        shell = shell.replace(html.escape(token), token)
    output_dir.joinpath("snapshot", shell_name).write_text(
        shell,
        encoding="utf-8",
    )


def title_url_path(title: str) -> str:
    """把 MediaWiki 标题映射为可读且可静态托管的 URL 路径。"""

    parts = title.replace(" ", "_").split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise ValueError(f"词条标题不能安全映射到静态路径: {title}")
    return "/".join(quote(part, safe=":@!$&'()*+,;=-._~") for part in parts)


def title_output_path(output_dir: Path, title: str) -> Path:
    parts = title.replace(" ", "_").split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise ValueError(f"词条标题不能安全映射到静态路径: {title}")
    return output_dir.joinpath("wiki", *parts, "index.html")


def canonical_url(base_url: str, title: str) -> str:
    return f"{base_url.rstrip('/')}/wiki/{title_url_path(title)}/"


def render_shell(
    shell: str,
    page: dict[str, Any],
    canonical: str,
    public_origin: str,
    main_page: str,
) -> str:
    revision = (
        f"只读公开快照，源修订 ID：{page['revision']}。"
        if page.get("revision")
        else "只读公开快照。"
    )
    page_title = html.escape(page["title"])
    page_class = html.escape(page["title"].replace(" ", "_"))
    body_class = html.escape(page.get("bodyClass", ""))
    encoded_title = quote(page["title"].replace(" ", "_"), safe="")
    revision_id = str(page.get("revision") or "")
    description_text = (
        page.get("description")
        or f"{page['title']}是 Human Infra Wiki 中的研究词条。"
    )
    description = html.escape(description_text, quote=True)
    is_main_page = page["title"] == main_page
    document_title = f"{page['title']} - Human Infra Wiki"
    structured_data = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage" if is_main_page else "Article",
            "headline": page["title"],
            "name": page["title"],
            "description": description_text,
            "url": canonical,
            "inLanguage": "zh",
            "isPartOf": {
                "@type": "WebSite",
                "@id": f"{public_origin.rstrip('/')}/#website",
                "name": "Human Infra Wiki",
                "url": f"{public_origin.rstrip('/')}/",
            },
            "publisher": {
                "@type": "Organization",
                "name": "tradecatlabs",
                "url": "https://github.com/tradecatlabs",
            },
        },
        ensure_ascii=False,
        separators=(",", ":"),
    ).replace("<", "\\u003c")
    replacements = {
        "__HI_DOCUMENT_TITLE__": html.escape(document_title),
        "__HI_DISPLAY_TITLE__": page["displayTitle"],
        "__HI_BODY_CLASS__": body_class,
        "__HI_PAGE_TITLE__": page_title,
        "__HI_PAGE_TITLE_ENCODED__": encoded_title,
        "__HI_PAGE_CLASS__": page_class,
        "__HI_REVISION_ID__": revision_id,
        "__HI_TOC__": page.get("toc", ""),
        "__HI_CONTENT__": page["body"],
        "__HI_CATEGORIES__": page.get("categories", ""),
        "__HI_REVISION__": revision,
        "__HI_CANONICAL__": canonical,
        "__HI_DESCRIPTION__": description,
        "__HI_OG_TYPE__": "website" if is_main_page else "article",
        "__HI_STRUCTURED_DATA__": structured_data,
    }
    rendered = shell
    for token, value in replacements.items():
        rendered = rendered.replace(token, value)
    return rendered


def static_href_from_mediawiki(href: str) -> str | None:
    """把公开快照中的 MediaWiki 本地链接转换为静态路由。"""

    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc:
        return None
    path = parsed.path
    query = dict(parse_qsl(parsed.query, keep_blank_values=True))
    title = ""
    if path.startswith("/index.php/"):
        title = unquote(path.removeprefix("/index.php/")).replace("_", " ")
    elif path == "/index.php" and query.get("title"):
        title = query["title"].replace("_", " ")
    elif path.startswith("/wiki/"):
        title = unquote(path.removeprefix("/wiki/")).replace("_", " ")
    else:
        return None

    normalized = normalize_title(title).casefold()
    if normalized == normalize_title("首页").casefold():
        return "/"
    if normalized == normalize_title("Special:Search").casefold():
        search = query.get("search", "")
        return f"/search/?q={quote(search)}" if search else "/search/"
    if normalized == normalize_title("Special:Random").casefold():
        return "/random/"
    if normalized.startswith("special:") or query.get("action"):
        return "#"
    return f"/wiki/{title_url_path(title)}/"


def rewrite_static_document(
    document: str,
    route_overrides: dict[str, str] | None = None,
) -> str:
    soup = BeautifulSoup(document, "lxml")

    # 公开快照没有 MediaWiki 后端或 Vector ResourceLoader。移除无法在
    # 纯静态环境成立的操作容器，避免保留看似可用但实际无效的控件。
    for form in list(soup.select("form[action]")):
        action = form.get("action", "")
        if action.startswith("/index.php/"):
            form.decompose()
    for selector in (
        "#p-variants",
        "#t-permalink",
        "#vector-sticky-header",
    ):
        for node in soup.select(selector):
            node.decompose()
    for toggle_selector in (
        "#vector-user-links-dropdown-checkbox",
        "#vector-variants-dropdown-checkbox",
    ):
        dropdown_toggle = soup.select_one(toggle_selector)
        if not dropdown_toggle:
            continue
        dropdown = dropdown_toggle.find_parent(
            class_="vector-dropdown"
        )
        if dropdown:
            dropdown.decompose()

    for node in soup.select(".mw-editsection, .mw-collapsible-toggle"):
        node.decompose()
    for node in soup.select(
        ".sortable, .mw-collapsible, .mw-collapsed, .mw-made-collapsible"
    ):
        classes = [
            value
            for value in node.get("class", [])
            if value not in {
                "sortable",
                "mw-collapsible",
                "mw-collapsed",
                "mw-made-collapsible",
            }
        ]
        if classes:
            node["class"] = classes
        elif node.has_attr("class"):
            del node["class"]

    for link in soup.select("a[href], link[href]"):
        rewritten = static_href_from_mediawiki(link.get("href", ""))
        if rewritten is not None:
            link["href"] = rewritten
        if route_overrides and link.get("href") in route_overrides:
            link["href"] = route_overrides[link["href"]]
    for link in list(soup.select('a[href="#"]')):
        if "vector-toc-link" in link.get("class", []):
            continue
        list_item = link.find_parent("li", class_="mw-list-item")
        if list_item:
            list_item.decompose()
        else:
            link.unwrap()
    for portlet in soup.select("#p-cactions"):
        if not portlet.select_one("a[href]"):
            portlet.decompose()

    for form in soup.select("form[action='/index.php']"):
        form["action"] = "/search/"
        form["method"] = "get"
        for hidden in form.select("input[name='title']"):
            hidden.decompose()
        search_input = form.select_one("input[name='search']")
        if search_input:
            search_input["name"] = "q"
    return str(soup)


def write_static_search(output_dir: Path, shell: str, public_origin: str) -> None:
    page = {
        "title": "搜索",
        "displayTitle": "搜索",
        "body": (
            '<div class="mw-parser-output">'
            '<form action="/search/" class="mw-search-form" method="get">'
            '<label for="hi-static-search">搜索 Human Infra Wiki</label>'
            '<div class="cdx-search-input">'
            '<input class="cdx-text-input__input" id="hi-static-search" '
            'name="q" type="search">'
            '<button class="cdx-button cdx-button--action-progressive" '
            'type="submit">搜索</button></div></form>'
            '<p id="hi-search-summary">输入词条名称开始搜索。</p>'
            '<ul class="mw-search-results" id="hi-search-results"></ul>'
            '</div>'
        ),
        "bodyClass": (
            "skin--responsive skin-vector mediawiki ltr sitedir-ltr "
            "ns--1 ns-special page-Special_Search skin-vector-2022 action-view"
        ),
        "categories": "",
        "revision": None,
        "description": "Human Infra Wiki 静态标题搜索。",
        "toc": "",
    }
    target = output_dir / "search" / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    document = render_shell(
        shell,
        page,
        f"{public_origin.rstrip('/')}/search/",
        public_origin,
        MAIN_PAGE,
    )
    soup = BeautifulSoup(
        rewrite_static_document(
            document,
            {
                f"/wiki/{title_url_path('搜索')}/": "/search/",
            },
        ),
        "lxml",
    )
    script = soup.new_tag("script", src="/assets/wiki-search.js", defer=True)
    soup.body.append(script)
    target.write_text(str(soup), encoding="utf-8")
    output_dir.joinpath("assets", "wiki-search.js").write_text(
        """\
(async function () {
  "use strict";
  const params = new URLSearchParams(window.location.search);
  const query = (params.get("q") || "").trim();
  const input = document.getElementById("hi-static-search");
  const summary = document.getElementById("hi-search-summary");
  const results = document.getElementById("hi-search-results");
  input.value = query;
  if (!query) return;
  const normalize = (value) => value.replaceAll("_", " ").toLocaleLowerCase("zh-CN");
  const response = await fetch("/snapshot/index.json");
  if (!response.ok) {
    summary.textContent = "搜索索引暂时不可用。";
    return;
  }
  const index = await response.json();
  const needle = normalize(query);
  const matches = index.pages.filter((page) => {
    return normalize(page.title).includes(needle)
      || (page.aliases || []).some((alias) => normalize(alias).includes(needle));
  }).slice(0, 100);
  summary.textContent = matches.length
    ? `找到 ${matches.length} 个标题结果。`
    : "没有找到匹配的词条。";
  for (const page of matches) {
    const item = document.createElement("li");
    const link = document.createElement("a");
    link.href = page.urlPath;
    link.textContent = page.title;
    item.append(link);
    results.append(item);
  }
}());
""",
        encoding="utf-8",
    )


def write_static_random(output_dir: Path) -> None:
    target = output_dir / "random" / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        """<!doctype html>
<html lang="zh"><head><meta charset="utf-8">
<meta name="robots" content="noindex,follow">
<title>随机词条 - Human Infra Wiki</title></head>
<body><p>正在选择随机词条……</p>
<script>
fetch("/snapshot/index.json").then((response) => response.json()).then((index) => {
  const page = index.pages[Math.floor(Math.random() * index.pages.length)];
  window.location.replace(page.urlPath);
});
</script></body></html>
""",
        encoding="utf-8",
    )


def write_static_compatibility(output_dir: Path, shell: str, public_origin: str) -> None:
    not_found = {
        "title": "页面不存在",
        "displayTitle": "页面不存在",
        "body": (
            '<div class="mw-parser-output">'
            '<p>该页面不在当前公开快照中。</p>'
            '<p><a href="/">返回首页</a></p></div>'
        ),
        "bodyClass": (
            "skin--responsive skin-vector mediawiki ltr sitedir-ltr "
            "ns-0 ns-subject page-页面不存在 rootpage-页面不存在 "
            "skin-vector-2022 action-view"
        ),
        "categories": "",
        "revision": None,
        "description": "请求的页面不在当前 Human Infra Wiki 公开快照中。",
        "toc": "",
    }
    document = render_shell(
        shell,
        not_found,
        f"{public_origin.rstrip('/')}/404.html",
        public_origin,
        MAIN_PAGE,
    )
    soup = BeautifulSoup(
        rewrite_static_document(
            document,
            {
                f"/wiki/{title_url_path('页面不存在')}/": "/404.html",
            },
        ),
        "lxml",
    )
    robots = soup.select_one("meta[name='robots']")
    if robots:
        robots["content"] = "noindex,follow"
    output_dir.joinpath("404.html").write_text(str(soup), encoding="utf-8")

    compat_dir = output_dir / "compat"
    compat_dir.mkdir(parents=True, exist_ok=True)
    compat_dir.joinpath("index.html").write_text(
        """<!doctype html>
<html lang="zh"><head><meta charset="utf-8">
<meta name="robots" content="noindex,follow">
<title>正在转向静态词条 - Human Infra Wiki</title></head>
<body><p>正在转向静态词条……</p>
<script>
const params = new URLSearchParams(window.location.search);
const title = (params.get("title") || "").replaceAll("_", " ").trim();
if (title === "Special:Search") {
  const target = new URL("/search/", window.location.origin);
  target.searchParams.set("q", params.get("search") || "");
  window.location.replace(target);
} else if (title === "Special:Random") {
  window.location.replace("/random/");
} else if (title) {
  const path = title.replaceAll(" ", "_").split("/")
    .map(encodeURIComponent).join("/");
  window.location.replace(`/wiki/${path}/`);
} else {
  window.location.replace("/");
}
</script></body></html>
""",
        encoding="utf-8",
    )


def write_static_pages(
    output_dir: Path,
    index: list[dict[str, Any]],
    pages_by_file: dict[str, dict[str, Any]],
) -> None:
    config = json.loads(GEO_CONFIG.read_text(encoding="utf-8"))
    public_origin = config["products"]["wiki"]["url"].rstrip("/")
    article_shell = output_dir.joinpath(
        "snapshot", "article-shell.html"
    ).read_text(encoding="utf-8")
    main_shell = output_dir.joinpath(
        "snapshot", "main-shell.html"
    ).read_text(encoding="utf-8")

    for entry in index:
        page = pages_by_file[entry["file"]]
        entry["urlPath"] = f"/wiki/{title_url_path(page['title'])}/"
        shell = main_shell if page["title"] == MAIN_PAGE else article_shell
        document = rewrite_static_document(render_shell(
            shell,
            page,
            canonical_url(public_origin, page["title"]),
            public_origin,
            MAIN_PAGE,
        ))
        target = title_output_path(output_dir, page["title"])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(document, encoding="utf-8")
        if page["title"] == MAIN_PAGE:
            output_dir.joinpath("index.html").write_text(
                document,
                encoding="utf-8",
            )

    write_static_search(output_dir, article_shell, public_origin)
    write_static_random(output_dir)
    write_static_compatibility(output_dir, article_shell, public_origin)
    output_dir.joinpath("_redirects").write_text(
        "/index.php /compat/ 302\n"
        "/index.php/* /wiki/:splat/ 301\n",
        encoding="utf-8",
    )


def write_geo_publication(
    output_dir: Path,
    index: list[dict[str, Any]],
    pages_by_file: dict[str, dict[str, Any]],
) -> None:
    config = json.loads(GEO_CONFIG.read_text(encoding="utf-8"))
    project = config["project"]
    product = config["products"]["wiki"]
    publisher = config["publisher"]
    base_url = product["url"]

    urls = [
        canonical_url(base_url, entry["title"])
        for entry in index
    ]
    output_dir.joinpath("robots.txt").write_text(
        "User-agent: *\nAllow: /\nDisallow: /snapshot/\n\n"
        f"Sitemap: {base_url}sitemap.xml\n",
        encoding="utf-8",
    )
    output_dir.joinpath("sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(
            f"  <url><loc>{html.escape(url)}</loc></url>\n"
            for url in urls
        )
        + "</urlset>\n",
        encoding="utf-8",
    )

    preferred_titles = (
        MAIN_PAGE,
        "有效永生与主体持续性",
        "长寿逃逸速度",
        "主体持续性",
        "证据地图",
        "研究域全景",
    )
    entries_by_title = {entry["title"]: entry for entry in index}
    links = []
    for title in preferred_titles:
        entry = entries_by_title.get(title)
        if entry:
            page = pages_by_file[entry["file"]]
            links.append(
                f"- [{title}]({canonical_url(base_url, title)}): "
                f"{page['description']}"
            )
    output_dir.joinpath("llms.txt").write_text(
        f"# {product['name']}\n\n"
        f"> {product['description']}\n\n"
        "## Core pages\n\n"
        + "\n".join(links)
        + "\n\n## Machine discovery\n\n"
        f"- [Complete sitemap]({base_url}sitemap.xml)\n"
        f"- [Page metadata index]({base_url}geo/pages.ndjson)\n"
        f"- [Entity graph]({base_url}geo/entity.jsonld)\n\n"
        "## Evidence boundary\n\n"
        "Pages separate claims, sources, applicability boundaries and unknowns. "
        "A listed research domain or technology is not proof of efficacy, "
        "feasibility or individual benefit. Do not use this Wiki as individual "
        "medical, legal or lifespan advice.\n",
        encoding="utf-8",
    )

    geo_dir = output_dir / "geo"
    geo_dir.mkdir()
    entity = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"{base_url}#website",
        "name": product["name"],
        "alternateName": project["alternateName"],
        "url": base_url,
        "description": product["description"],
        "inLanguage": "zh",
        "publisher": {
            "@type": "Organization",
            "name": publisher["name"],
            "url": publisher["url"],
        },
        "isPartOf": {
            "@type": "Project",
            "name": project["name"],
            "url": config["products"]["portal"]["url"],
        },
        "sameAs": [
            project["repository"],
            config["products"]["technologyTree"]["url"],
        ],
    }
    geo_dir.joinpath("entity.jsonld").write_text(
        json.dumps(entity, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    with geo_dir.joinpath("pages.ndjson").open("w", encoding="utf-8") as handle:
        for entry in index:
            page = pages_by_file[entry["file"]]
            handle.write(json.dumps(
                {
                    "title": entry["title"],
                    "url": canonical_url(base_url, entry["title"]),
                    "description": page["description"],
                    "revision": page["revision"],
                    "aliases": entry["aliases"],
                },
                ensure_ascii=False,
                separators=(",", ":"),
            ) + "\n")


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

    build_shell(
        session,
        base_url,
        output_dir,
        SHELL_PAGE,
        "article-shell.html",
    )
    build_shell(
        session,
        base_url,
        output_dir,
        MAIN_PAGE,
        "main-shell.html",
    )
    index_by_title: dict[str, dict[str, Any]] = {}
    pages_by_file: dict[str, dict[str, Any]] = {}
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
            pages_by_file[filename] = {
                key: value
                for key, value in page.items()
                if key != "sourceTitle"
            }
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
    write_static_pages(output_dir, index, pages_by_file)
    if len(pages_by_file) != len(index):
        raise RuntimeError(
            "快照实体与索引数量不一致: "
            f"pages={len(pages_by_file)} index={len(index)}"
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
                "pages": [
                    {
                        key: value
                        for key, value in entry.items()
                        if key != "file"
                    }
                    for entry in index
                ],
            },
            ensure_ascii=False,
            separators=(",", ":"),
        ),
        encoding="utf-8",
    )
    write_geo_publication(output_dir, index, pages_by_file)
    copy_media(output_dir)
    output_dir.joinpath("snapshot", "article-shell.html").unlink()
    output_dir.joinpath("snapshot", "main-shell.html").unlink()
    output_dir.joinpath("_headers").write_text(
        "/assets/*\n"
        "  Cache-Control: public, max-age=31536000, immutable\n"
        "/wiki/*\n"
        "  Cache-Control: public, max-age=3600\n"
        "/snapshot/index.json\n"
        "  Cache-Control: public, max-age=300\n"
        "/geo/*\n"
        "  Cache-Control: public, max-age=300\n"
        "/sitemap.xml\n"
        "  Cache-Control: public, max-age=300\n"
        "/llms.txt\n"
        "  Cache-Control: public, max-age=300\n",
        encoding="utf-8",
    )
    forbidden = [
        output_dir / "_worker.js",
        output_dir / "_routes.json",
        output_dir / "functions",
    ]
    present = [str(path) for path in forbidden if path.exists()]
    if present:
        raise RuntimeError(
            "纯静态发布物禁止包含 Worker/Functions: " + ", ".join(present)
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
