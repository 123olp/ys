#!/usr/bin/env python3
"""从固定中文维基百科首页快照生成 Human Infra 首页。"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


WIKI_DIR = Path(__file__).resolve().parents[1]
SNAPSHOT_DIR = WIKI_DIR / "homepage-upstream" / "snapshot"
CONTENT_DIR = WIKI_DIR / "content"
HOME_OUTPUT = CONTENT_DIR / "Human_Infra_Main_Page.wiki"
BANNER_OUTPUT = CONTENT_DIR / "Template_Home_Header.wiki"
STYLE_OUTPUT = CONTENT_DIR / "Template_Home_styles_css.wiki"
GENERATED_NOTICE = (
    "<!-- 由 scripts/build-wikipedia-homepage.py 从固定中文维基百科首页快照生成；"
    "禁止手工修改布局。 -->\n"
)
CSS_NOTICE = (
    "/* 由 scripts/build-wikipedia-homepage.py 从固定中文维基百科首页样式生成；"
    "禁止手工修改布局。 */\n"
)
PARSER_HEADING_COMPAT = """

/*
 * MediaWiki 1.46 将原始 h1 包装为 .mw-heading1；Wikimedia 生产渲染保留直接 h1。
 * 这里仅消除包装层的字号放大，使官方 h1 规则得到相同的计算结果。
 */
#mp-2012-banner-title .mw-heading1 {
    border-bottom: none;
    font-size: 100%;
    margin: 0;
}

#mp-2012-banner-title .mw-heading1 h1 {
    display: flow-root;
}

/* 官方移动端不显示桌面页首标志槽。 */
@media all and (max-width: 719px) {
    #mp-2012-banner-logo {
        display: none;
    }
}
"""
LOCAL_CONTENT_CLASS_COMPAT = """

/*
 * 上游首页在多个栏目复用 #column-feature-more。本地内容槽位改用 class，
 * 避免静态页面出现重复 DOM id，同时保持上游几何与配色。
 */
.column-feature-more .column-feature-more-header a {
    font-weight: bold;
    color: #474747;
}

html.skin-theme-clientpref-night .column-feature-more .column-feature-more-header a {
    color: #b8b8b8;
}
@media (prefers-color-scheme: dark) {
    html.skin-theme-clientpref-os .column-feature-more .column-feature-more-header a {
        color: #b8b8b8;
    }
}

.column-feature-more {
    margin-top: 1.2em;
    clear: left;
}

.column-feature-more ul {
    list-style: none;
    margin-left: 0;
}

.column-feature-more li {
    font-size: .9em;
    color: #474747;
}
"""


def fail(message: str) -> None:
    raise SystemExit(message)


def sha256(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def replace_once(source: str, old: str, new: str, label: str) -> str:
    count = source.count(old)
    if count != 1:
        fail(f"{label} 预期命中 1 次，实际命中 {count} 次")
    return source.replace(old, new, 1)


def replace_template_call(source: str, name: str, replacement: str) -> str:
    start_token = "{{" + name + "|"
    start = source.find(start_token)
    if start < 0:
        fail(f"找不到上游模板调用: {name}")
    if source.find(start_token, start + len(start_token)) >= 0:
        fail(f"上游模板调用不唯一: {name}")

    depth = 0
    cursor = start
    while cursor < len(source):
        if source[cursor] == "{":
            depth += 1
        elif source[cursor] == "}":
            depth -= 1
            if depth == 0:
                return source[:start] + replacement + source[cursor + 1 :]
        cursor += 1
    fail(f"上游模板调用未闭合: {name}")
    return source


def replace_inner(
    source: str, start_marker: str, end_marker: str, replacement: str, label: str
) -> str:
    start = source.find(start_marker)
    if start < 0 or source.find(start_marker, start + 1) >= 0:
        fail(f"{label} 起始锚点缺失或不唯一")
    content_start = start + len(start_marker)
    end = source.find(end_marker, content_start)
    if end < 0 or source.find(end_marker, end + 1) >= 0:
        fail(f"{label} 结束锚点缺失或不唯一")
    return source[:content_start] + replacement + source[end:]


def verify_snapshot() -> dict:
    metadata_path = SNAPSHOT_DIR / "metadata.json"
    if not metadata_path.is_file():
        fail("缺少首页快照 metadata.json，请先运行 refresh-wikipedia-homepage.py --write")
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    records = list(metadata["pages"].values()) + [
        metadata["rendered"],
        metadata["language_links"],
    ]
    for record in records:
        path = SNAPSHOT_DIR / record["filename"]
        if not path.is_file():
            fail(f"首页快照文件缺失: {path}")
        digest = sha256(path.read_text(encoding="utf-8"))
        if digest != record["sha256"]:
            fail(f"首页快照哈希漂移: {path}")
    return metadata


def build_home() -> str:
    source = (SNAPSHOT_DIR / "Wikipedia_Home.wiki").read_text(encoding="utf-8")
    source = replace_once(source, "{{noedit0}} ", "", "本地 noedit 兼容")
    source = replace_once(
        source,
        '<templatestyles src="Wikipedia:首页/styles.css" />',
        '<templatestyles src="首页/styles.css" />',
        "TemplateStyles 路由",
    )
    source = replace_once(
        source, "{{Wikipedia:首页/banner}}", "{{首页/页首}}", "页首槽位"
    )

    replacements = {
        "Feature": '<div id="column-feature" class="mp-2012-text">{{首页/特色研究}}</div>',
        "Dyk": '<div id="column-dyk" class="mp-2012-text">{{首页/知识与路线}}</div>',
        "Good": '<div id="column-good" class="mp-2012-text">{{首页/证据动态}}</div>',
        "Featurepic": '<div class="mp-2012-text">{{首页/研究图谱}}</div>',
        "Itn": '<div id="column-itn" class="mp-2012-text">{{首页/争议与未知}}</div>',
        "Otd": '<div id="column-otd" class="mp-2012-text">{{首页/相关入口}}</div>',
    }
    for name, replacement in replacements.items():
        source = replace_template_call(source, name, replacement)

    headings = {
        "<h2>{{#ifeq:{{FeaturedContentType|{{{timecorrection|}}}}}|1|特色列表|典范条目}}</h2>": "<h2>典范研究</h2>",
        "<h2>优良条目</h2>": "<h2>证据动态</h2>",
        "<h2>每日图片</h2>": "<h2>研究图谱</h2>",
        "<h2>新闻动态</h2>": "<h2>争议与未知</h2>",
        "<h2>历史上的今天</h2>": "<h2>历史与前沿</h2>",
        "<h2>動態热门</h2>": "<h2>当前重点</h2>",
        "<h2>參與维基百科</h2>": "<h2>参与 Human Infra</h2>",
        "<h2>维基百科提醒您</h2>": "<h2>Human Infra 提醒您</h2>",
    }
    for old, new in headings.items():
        source = replace_once(source, old, new, f"栏目标题 {old}")

    source = replace_once(
        source, "{{Uptrends}}", "{{首页/当前重点}}", "当前重点槽位"
    )
    source = replace_once(
        source,
        "[[Wikipedia:动态热门|更多動態熱門]]",
        "[[技术路线全景索引|更多技术路线]]",
        "当前重点页脚",
    )
    source = replace_inner(
        source,
        '<div id="column-participate" class="mp-2012-text">',
        "\n</div>\n</div>\n<!-- ===========右欄第二个框关闭=========== -->",
        "\n{{首页/参与建设}}",
        "参与建设槽位",
    )
    source = replace_inner(
        source,
        '<div id="column-tips" class="plainlinks mp-2012-text">',
        "\n</div>\n</div>\n<!-- ===========右欄第三个框关闭=========== -->",
        "\n{{首页/研究提醒}}",
        "研究提醒槽位",
    )
    source = replace_inner(
        source,
        '<div id="mp-2012-links" class="nomobile">',
        "\n</div>\n<!--  =======维基媒体基金会其他計劃========   -->",
        "\n{{首页/站点链接}}",
        "站点链接槽位",
    )
    source = replace_inner(
        source,
        '<div id="mp-2012-sisters" class="nomobile">',
        "\n</div>\n<!-- 內容关闭 -->",
        "\n{{首页/关联项目}}",
        "关联项目槽位",
    )
    upstream = (SNAPSHOT_DIR / "Wikipedia_Home.wiki").read_text(encoding="utf-8")
    upstream_ids = set(re.findall(r'id="(mp-2012[^"]*)"', upstream))
    generated_ids = set(re.findall(r'id="(mp-2012[^"]*)"', source))
    missing_ids = sorted(upstream_ids - generated_ids)
    if missing_ids:
        fail(f"生成首页丢失上游 mp-2012 DOM 契约: {missing_ids}")
    for content_id in (
        "column-feature",
        "column-dyk",
        "column-good",
        "column-itn",
        "column-otd",
        "column-uptrends",
        "column-participate",
        "column-tips",
    ):
        if source.count(f'id="{content_id}"') != 1:
            fail(f"生成首页缺少或重复官方内容容器: {content_id}")
    language_links = json.loads(
        (SNAPSHOT_DIR / "Wikipedia_Home_language_links.json").read_text(
            encoding="utf-8"
        )
    )
    expected_count = verify_snapshot()["language_links"]["count"]
    if len(language_links) != expected_count:
        fail(
            "首页语言链接数量与固定快照不一致: "
            f"expected={expected_count}, actual={len(language_links)}"
        )
    language_wikitext = "\n".join(
        f"[[{item['lang']}:{item['title']}]]" for item in language_links
    )
    return GENERATED_NOTICE + source + "\n" + language_wikitext + "\n"


def build_banner() -> str:
    source = (SNAPSHOT_DIR / "Wikipedia_Home_banner.wiki").read_text(
        encoding="utf-8"
    )
    substitutions = {
        '<templatestyles src="Wikipedia:首页/styles.css" />': '<templatestyles src="首页/styles.css" />',
        '<div id="mp-2012-banner-logo"><!-- &#x200B; --></div>': '<div id="mp-2012-banner-logo">[[File:Human-Infra-mark.svg|108px|link=Human Infra:关于|Human Infra Wiki]]</div>',
        "[[Wikipedia:关于|维基百科]]": "[[Human Infra:关于|人类基础设施]]",
        "海納百川，有容乃大<br />[[Wikipedia:欢迎|人人可編輯]]的[[自由內容|自由]]百科全書": "Human Infra 知识库<br />研究主体持续性何以可能",
        "篇[[Wikipedia:什么是条目|條目]]": "篇内容条目",
        "[[Wikipedia:分類索引|分类]]": "[[研究域全景索引|研究域]]",
        "[[Portal:首頁|主题]]": "[[技术路线全景索引|技术路线]]",
        "[[Wikipedia:互助客栈/求助|求助]]": "[[证据地图与支持边界|证据]]",
        "[[Wikipedia:新手入門/主頁|入门]]": "[[Portal:永生与主体持续性|专题]]",
        "[[Wikipedia:沙盒|沙盒]]": "[[Help:词条录入标准|入门]]",
        "[[Wikipedia:联络我们/捐赠者|捐款]]": "[[Human Infra:内容方针|方针]]",
    }
    for old, new in substitutions.items():
        source = replace_once(source, old, new, f"页首内容 {old}")
    return GENERATED_NOTICE + source


def build_styles() -> str:
    source = (SNAPSHOT_DIR / "Wikipedia_Home_styles.css").read_text(
        encoding="utf-8"
    )
    # 本地站点标识由页首内容槽位提供，因此不使用上游 Wikipedia 标志背景。
    source = replace_once(
        source,
        '    background-image: url("//upload.wikimedia.org/wikipedia/commons/8/80/Wikipedia-logo-v2.svg");\n',
        "",
        "Wikipedia logo 远程 URL 兼容转换",
    )
    # TemplateStyles 默认允许 Wikimedia Commons 的 HTTPS 图片，但不接受协议相对 URL。
    source = replace_once(
        source,
        '    background-image: url("//upload.wikimedia.org/wikipedia/commons/0/0a/Zhwp_blue_banner.png");\n',
        '    background-image: url("https://upload.wikimedia.org/wikipedia/commons/0/0a/Zhwp_blue_banner.png");\n',
        "banner 远程 URL 兼容转换",
    )
    return (
        CSS_NOTICE
        + source
        + PARSER_HEADING_COMPAT
        + LOCAL_CONTENT_CLASS_COMPAT
    )


def write_or_check(path: Path, expected: str, check: bool) -> None:
    if check:
        if not path.is_file() or path.read_text(encoding="utf-8") != expected:
            fail(f"生成产物漂移，请重新构建: {path}")
        return
    path.write_text(expected, encoding="utf-8")
    print(f"已生成: {path.relative_to(WIKI_DIR)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="只校验生成产物")
    args = parser.parse_args()

    verify_snapshot()
    write_or_check(HOME_OUTPUT, build_home(), args.check)
    write_or_check(BANNER_OUTPUT, build_banner(), args.check)
    write_or_check(STYLE_OUTPUT, build_styles(), args.check)
    if args.check:
        print("Wikipedia 首页快照与生成契约: PASS")


if __name__ == "__main__":
    try:
        main()
    except (KeyError, json.JSONDecodeError) as error:
        print(f"首页快照元数据无效: {error}", file=sys.stderr)
        raise SystemExit(1) from error
