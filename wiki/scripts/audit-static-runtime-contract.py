#!/usr/bin/env python3
"""审计 MediaWiki 只读快照是否只暴露真实可用的交互能力。"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlparse

from lxml import html as lxml_html


FORBIDDEN_OPERATIONAL_IDS = {
    "ca-addsection",
    "ca-edit",
    "ca-history",
    "ca-more-history",
    "ca-more-viewsource",
    "ca-talk",
    "ca-unwatch",
    "ca-ve-edit",
    "ca-viewsource",
    "ca-watch",
    "n-recentchanges",
    "n-specialpages",
    "p-personal",
    "p-variants",
    "pt-login-2",
    "t-info",
    "t-permalink",
    "t-recentchangeslinked",
    "t-whatlinkshere",
    "vector-sticky-header",
    "vector-user-links-dropdown-checkbox",
    "vector-variants-dropdown-checkbox",
}
DYNAMIC_CLASS_TOKENS = {
    "mw-collapsed",
    "mw-collapsible",
    "mw-collapsible-toggle",
    "mw-made-collapsible",
    "sortable",
}
ALLOWED_EMPTY_FRAGMENT_CLASS = "vector-toc-link"


def parse_document(path: Path):
    try:
        return lxml_html.fromstring(path.read_bytes())
    except Exception as error:
        raise RuntimeError(f"无法解析静态页面 {path}: {error}") from error


def class_tokens(node) -> set[str]:
    return set((node.get("class") or "").split())


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def audit_document(path: Path, root: Path) -> list[str]:
    document = parse_document(path)
    issues: list[str] = []
    label = relative(path, root)

    identified_nodes = document.xpath("//*[@id]")
    id_counts = Counter(node.get("id") for node in identified_nodes)
    for node_id, count in sorted(id_counts.items()):
        if count > 1:
            issues.append(f"{label}: DOM id 重复 #{node_id} count={count}")

    for node in identified_nodes:
        node_id = node.get("id")
        if node_id in FORBIDDEN_OPERATIONAL_IDS:
            issues.append(f"{label}: 保留了不可用操作控件 #{node_id}")

    for anchor in document.xpath('//a[@href="#"]'):
        if ALLOWED_EMPTY_FRAGMENT_CLASS in class_tokens(anchor):
            continue
        text = " ".join(anchor.text_content().split()) or "(无文本)"
        issues.append(f"{label}: 存在无目标链接 href=# 文本={text!r}")

    for form in document.xpath("//form[@action]"):
        action = form.get("action") or ""
        if action != "/search/":
            issues.append(f"{label}: 保留了无静态后端的表单 action={action!r}")

    for node in document.xpath("//*[@class]"):
        unsupported = class_tokens(node) & DYNAMIC_CLASS_TOKENS
        if unsupported:
            issues.append(
                f"{label}: 保留了无运行时动态类 {sorted(unsupported)}"
            )

    for node in document.xpath("//script[@src] | //link[@href]"):
        resource = node.get("src") or node.get("href") or ""
        if "load.php" in resource:
            issues.append(f"{label}: 重新引入了 ResourceLoader 资源 {resource}")

    return issues


def audit_required_contracts(root: Path) -> list[str]:
    issues: list[str] = []
    stylesheet = root / "assets" / "mediawiki.css"
    if not stylesheet.is_file():
        issues.append("发布物缺少 assets/mediawiki.css")

    samples = {
        "首页": root / "index.html",
        "普通词条": root / "wiki" / "长寿逃逸速度" / "index.html",
    }
    for label, path in samples.items():
        if not path.is_file():
            issues.append(f"{label}: 缺少样本页面 {relative(path, root)}")
            continue
        document = parse_document(path)
        controls = document.xpath(
            '//*[@id="vector-appearance"]//input[@type="radio"]'
        )
        if controls:
            issues.append(f"{label}: 静态快照伪装了 Vector 外观控件")
        adapter = document.xpath(
            '//script[@src="/assets/vector-client-preferences.js"]'
        )
        if adapter:
            issues.append(f"{label}: 静态快照包含自写 Vector 适配器")
        if document.xpath(
            '//*[contains(concat(" ", normalize-space(@class), " "), '
            '" vector-appearance-landmark ")]'
        ):
            issues.append(f"{label}: 静态快照保留了不可运行的外观入口")
        root_element = document.getroottree().getroot()
        if "client-nojs" not in class_tokens(root_element):
            issues.append(f"{label}: html 未保持 client-nojs 静态能力声明")
        if (
            "vector-feature-appearance-pinned-clientpref-0"
            not in class_tokens(root_element)
        ):
            issues.append(f"{label}: 未声明 Vector 原生 unpinned 降级状态")
        if (
            "vector-feature-appearance-pinned-clientpref-1"
            in class_tokens(root_element)
        ):
            issues.append(f"{label}: 无脚本快照错误保留 pinned 外观状态")

    home = samples["首页"]
    if home.is_file():
        document = parse_document(home)
        if document.xpath('//*[@id="vector-toc-pinned-container"]'):
            issues.append("首页: 错误包含普通词条目录")
        language_links = document.xpath(
            '//*[@id="p-lang-btn"]//a[starts-with(@href, "http")]'
        )
        if len(language_links) < 300:
            issues.append(f"首页: 外部语言链接不足，实际为 {len(language_links)}")

    article = samples["普通词条"]
    if article.is_file():
        document = parse_document(article)
        toc_links = document.xpath(
            '//*[@id="vector-toc-pinned-container"]'
            '//a[contains(concat(" ", normalize-space(@class), " "), '
            '" vector-toc-link ")]'
        )
        if not toc_links:
            issues.append("普通词条: 缺少原生 Vector 目录项")

    return issues


def audit_internal_routes(root: Path, html_files: list[Path]) -> list[str]:
    missing: dict[str, set[str]] = {}
    for path in html_files:
        document = parse_document(path)
        for anchor in document.xpath("//a[@href]"):
            parsed = urlparse(anchor.get("href") or "")
            if parsed.scheme or parsed.netloc:
                continue
            if not parsed.path.startswith("/wiki/"):
                continue
            target = root / unquote(parsed.path).lstrip("/")
            if parsed.path.endswith("/"):
                target /= "index.html"
            if target.is_file():
                continue
            missing.setdefault(parsed.path, set()).add(relative(path, root))

    return [
        f"内部路由缺少静态目标 {route!r}，来源页面数={len(sources)}"
        for route, sources in sorted(missing.items())
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Wiki Pages 静态发布物根目录",
    )
    args = parser.parse_args()
    root = args.output.resolve()
    if not root.is_dir():
        print(f"静态发布物目录不存在: {root}", file=sys.stderr)
        return 2

    html_files = sorted(root.rglob("*.html"))
    if not html_files:
        print(f"静态发布物不包含 HTML: {root}", file=sys.stderr)
        return 2

    issues: list[str] = []
    for path in html_files:
        issues.extend(audit_document(path, root))
    issues.extend(audit_internal_routes(root, html_files))
    issues.extend(audit_required_contracts(root))

    if issues:
        print(
            f"Wiki 静态运行时契约失败: issues={len(issues)} "
            f"pages={len(html_files)}",
            file=sys.stderr,
        )
        for issue in issues[:80]:
            print(f"- {issue}", file=sys.stderr)
        if len(issues) > 80:
            print(f"- 其余 {len(issues) - 80} 个问题已省略", file=sys.stderr)
        return 1

    print(
        f"Wiki 静态运行时契约通过: pages={len(html_files)} "
        "dead_links=0 internal_routes=0 form_actions=0 "
        "dynamic_markers=0 operational_controls=0 duplicate_ids=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
