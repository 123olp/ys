#!/usr/bin/env python3
"""Refresh the local portal from Wikimedia's official production artifact."""

from __future__ import annotations

import re
import urllib.request
from pathlib import Path
from urllib.parse import urljoin, urlparse


ROOT = Path(__file__).resolve().parents[1]
PORTAL_DIR = ROOT / "portal"
UPSTREAM_URL = "https://www.wikipedia.org/"
TECH_TREE_URL = "https://tree.tradecatlabs.com/"
LANGUAGES = [
    ("zh", "中文", "界面语言"),
    ("en", "English", "Interface language"),
    ("ja", "日本語", "表示言語"),
    ("de", "Deutsch", "Oberflächensprache"),
    ("ru", "Русский", "Язык интерфейса"),
    ("fr", "Français", "Langue de l’interface"),
    ("es", "Español", "Idioma de interfaz"),
    ("ar", "العربية", "لغة الواجهة"),
    ("pt", "Português", "Idioma da interface"),
    ("hi", "हिन्दी", "इंटरफ़ेस भाषा"),
]
WIKI_ENTRIES = [
    ("Human Infra:首页", "Wiki 首页", "知识导航与特色研究"),
    ("Portal:永生与主体持续性", "永生与主体持续性", "终极目标与研究路线"),
    ("Portal:衰老机制与长寿科学", "长寿科学", "衰老机制与干预证据"),
    ("Portal:身体替代与人体增强", "人体增强", "身体、认知与工具增强"),
    ("Portal:脑、记忆与主体连续性", "记忆与认知", "记忆编辑与主体连续性"),
    ("Portal:AI与自动化科学", "AI 与自动化科学", "技术窗口与科研加速"),
    ("Portal:未来等待", "未来等待", "生物停滞与时间差分"),
    ("研究域全景索引", "研究域", "C1-C6 研究域索引"),
    ("Category:技术节点", "技术节点", "历史基础与未来节点"),
    ("Category:证据来源", "证据来源", "论文、数据与来源卡片"),
    ("Category:专题门户", "专题门户", "专题入口与交叉索引"),
    ("Human Infra:关于", "关于", "范围、治理与参与方式"),
]


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "HumanInfraWikiPortal/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def replace_once(text: str, pattern: str, replacement: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"upstream portal contract changed: {pattern}")
    return updated


def language_ring() -> str:
    blocks = []
    for index, (code, name, description) in enumerate(LANGUAGES, start=1):
        direction = "rtl" if code == "ar" else "ltr"
        blocks.append(
            f'<div class="central-featured-lang lang{index}" lang="{code}" dir="{direction}">\n'
            f'<a href="#" class="link-box" data-hi-language="{code}" '
            f'title="{name} — Human Infra">\n'
            f"<strong>{name}</strong>\n"
            f"<small>{description}</small>\n"
            "</a>\n"
            "</div>"
        )
    return "\n".join(blocks)


def portal_footer() -> str:
    entries = []
    for title, label, description in WIKI_ENTRIES:
        entries.append(
            '<div class="other-project">\n'
            f'<a class="other-project-link" href="#" data-hi-title="{title}">\n'
            '<div class="other-project-icon">\n'
            '<img src="assets/human-infra-mark.svg" width="42" height="42" alt="">\n'
            "</div>\n"
            '<div class="other-project-text">\n'
            f'<span class="other-project-title">{label}</span>\n'
            f'<span class="other-project-tagline">{description}</span>\n'
            "</div>\n"
            "</a>\n"
            "</div>"
        )
        if title == "Human Infra:首页":
            entries.append(
                '<div class="other-project">\n'
                f'<a class="other-project-link" href="{TECH_TREE_URL}">\n'
                '<div class="other-project-icon">\n'
                '<img src="assets/human-infra-mark.svg" width="42" height="42" alt="">\n'
                "</div>\n"
                '<div class="other-project-text">\n'
                '<span class="other-project-title">科技树</span>\n'
                '<span class="other-project-tagline">目标、依赖与证据路线</span>\n'
                "</div>\n"
                "</a>\n"
                "</div>"
            )
    return (
        '<footer class="footer" data-el-section="other projects">\n'
        '<div class="footer-sidebar">\n'
        '<div class="footer-sidebar-content">\n'
        '<div class="footer-sidebar-icon">\n'
        '<img src="assets/human-infra-mark.svg" width="42" height="42" alt="">\n'
        "</div>\n"
        '<div class="footer-sidebar-text">Human Infra 是面向主体持续性的研究型知识基础设施。</div>\n'
        '<div class="footer-sidebar-text">'
        '<a href="UPSTREAM.md">门户界面直接复用 Wikimedia 官方 portals 工程。</a>'
        "</div>\n"
        "</div>\n"
        "</div>\n"
        '<div class="footer-sidebar app-badges">\n'
        '<div class="footer-sidebar-content">\n'
        '<div class="footer-sidebar-text">\n'
        '<div class="footer-sidebar-icon">\n'
        '<img src="assets/human-infra-mark.svg" width="42" height="42" alt="">\n'
        "</div>\n"
        '<strong><a href="#" data-hi-title="Human Infra:首页">进入 Human Infra Wiki</a></strong>\n'
        "<p>浏览研究域、技术路线、论文、证据来源与专题门户。</p>\n"
        "</div>\n"
        "</div>\n"
        "</div>\n"
        '<nav aria-label="Human Infra 入口" class="other-projects">\n'
        + "\n".join(entries)
        + "\n</nav>\n"
        "<hr>\n"
        '<p class="site-license">\n'
        '<small>门户框架源自 <a href="https://gerrit.wikimedia.org/r/wikimedia/portals">'
        "Wikimedia portals</a>（MIT）；知识内容按各页面标注的许可与来源使用。</small>\n"
        "</p>\n"
        "</footer>"
    )


def localize_assets(html: str) -> tuple[str, dict[str, str]]:
    references = set(
        re.findall(
            r'(?:https://www\.wikipedia\.org/|/)?'
            r'(?:portal/wikipedia\.org/assets/(?:img|js)/|static/(?:apple-touch|favicon)/)'
            r'[^"\'() ]+',
            html,
        )
    )
    local_assets: dict[str, str] = {}
    for reference in sorted(references):
        remote_url = urljoin(UPSTREAM_URL, reference)
        path = urlparse(remote_url).path
        filename = Path(path).name
        local_path = f"assets/{filename}"
        html = html.replace(reference, local_path)
        local_assets[remote_url] = local_path
    return html, local_assets


def adapt(html: str) -> tuple[str, dict[str, str]]:
    html = html.replace("<title>Wikipedia</title>", "<title>Human Infra</title>")
    html = html.replace(
        "Wikipedia is a free online encyclopedia, created and edited by volunteers "
        "around the world and hosted by the Wikimedia Foundation.",
        "Human Infra is a research wiki for subject continuity and human infrastructure.",
    )
    html = re.sub(
        r'<meta property="og:image"[^>]+>',
        '<meta property="og:image" content="assets/human-infra-mark.svg">',
        html,
        count=1,
    )
    html = replace_once(
        html,
        r'<img class="central-featured-logo"[^>]+>',
        '<img class="central-featured-logo" src="assets/human-infra-mark.svg" '
        'width="200" height="183" alt="">',
    )
    html = replace_once(
        html,
        r'<span class="central-textlogo__image sprite svg-Wikipedia_wordmark">.*?</span>',
        '<img class="central-textlogo__image" src="assets/human-infra-wordmark.svg" '
        'width="176" height="32" alt="Human Infra">',
    )
    html = replace_once(
        html,
        r'<strong class="jsl10n localized-slogan"[^>]*>.*?</strong>',
        '<strong class="localized-slogan">主体持续性知识基础设施</strong>',
    )
    html = replace_once(
        html,
        r'<nav data-jsl10n="top-ten-nav-label".*?</nav>',
        '<nav aria-label="界面语言" class="central-featured" data-el-section="primary links">\n'
        + language_ring()
        + "\n</nav>",
    )
    html = replace_once(
        html,
        r'action="(?:https:)?//www\.wikipedia\.org/search-redirect\.php"',
        'action="#"',
    )
    html = html.replace(
        'data-jsl10n="portal.search-input-label">Search Wikipedia',
        ">搜索 Human Infra Wiki",
    )
    html = html.replace(
        'data-jsl10n="portal.language-button-text">Read Wikipedia in your language ',
        ">使用你的语言访问 Human Infra Wiki ",
    )
    html = replace_once(
        html,
        r'<footer class="footer".*?</footer>',
        portal_footer(),
    )
    html = html.replace(
        "</body>",
        '<script src="runtime-config.js"></script>\n'
        '<script src="adapter.js"></script>\n'
        "</body>",
    )
    return localize_assets(html)


def main() -> None:
    raw_html = fetch(UPSTREAM_URL).decode("utf-8")
    adapted, assets = adapt(raw_html)
    (PORTAL_DIR / "index.html").write_text(adapted, encoding="utf-8")
    for remote, relative_path in assets.items():
        target = PORTAL_DIR / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(fetch(remote))
    print(f"refreshed official Wikimedia portal snapshot: {PORTAL_DIR / 'index.html'}")


if __name__ == "__main__":
    main()
