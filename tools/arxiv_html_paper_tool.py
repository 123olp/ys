#!/usr/bin/env python3
"""复用 arXiv HTML papers 前端框架的本地工具。"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_SOURCE = Path(".research/arxiv-html/2606.26689v1/wget")
DEFAULT_TEMPLATE_DIR = Path(__file__).resolve().with_name("arxiv-html-paper") / "templates"
DEFAULT_FALLBACK_ASSET_DIR = Path(__file__).resolve().with_name("arxiv-html-paper") / "assets"
DEFAULT_PUBLIC_DIR = Path("web/public")
DEFAULT_LAYOUT_TARGET = Path("web/src/layouts/PaperReaderLayout.astro")
DEFAULT_PAGE_TARGET = Path("web/src/pages/paper.astro")

DEFAULT_PAPER_URL = "https://arxiv.org/html/2606.26689v1"

REQUIRED_ASSET_PATHS = [
    "static/browse/0.3.4/css/ar5iv.0.8.5.css",
    "static/browse/0.3.4/css/arxiv-html-papers-20260131.css",
    "static/browse/0.3.4/css/arxiv-html-papers-theme-20250131.css",
    "static/browse/0.3.4/js/arxiv-html-papers-20260131.js",
    "static/browse/0.3.4/images/arxiv-logo-one-color-white.svg",
    "static/browse/0.3.4/images/icons/apple-touch-icon.png",
    "static/browse/0.3.4/images/icons/favicon-16x16.png",
    "static/browse/0.3.4/images/icons/favicon-32x32.png",
    "static/browse/0.3.4/images/icons/safari-pinned-tab.svg",
    "static/browse/0.3.4/images/icons/site.webmanifest",
    "use.typekit.net/utz6mli.css",
    "use.typekit.net/font-files/ibm-plex-mono-n4.woff2",
    "use.typekit.net/font-files/ibm-plex-mono-n8.woff2",
    "use.typekit.net/font-files/rival-sans-i1.woff2",
    "use.typekit.net/font-files/rival-sans-i3.woff2",
    "use.typekit.net/font-files/rival-sans-i4.woff2",
    "use.typekit.net/font-files/rival-sans-i7.woff2",
    "use.typekit.net/font-files/rival-sans-n1.woff2",
    "use.typekit.net/font-files/rival-sans-n3.woff2",
    "use.typekit.net/font-files/rival-sans-n4.woff2",
    "use.typekit.net/font-files/rival-sans-n7.woff2",
]

OPTIONAL_ASSET_PATHS = [
    "use.typekit.net/robots.txt",
]

REQUIRED_ASSET_GLOBS: list[str] = []

COPY_SPECS = [
    ("arxiv.org/static/browse/0.3.4", "static/browse/0.3.4"),
    ("use.typekit.net", "use.typekit.net"),
]

TYPEKIT_FONT_SPECS = [
    ("rival-sans", "normal", 100, "d9b715", "00000000000000007735aa06", "rival-sans-n1.woff2"),
    ("rival-sans", "italic", 700, "b20507", "00000000000000007735aa19", "rival-sans-i7.woff2"),
    ("rival-sans", "normal", 700, "c7b379", "00000000000000007735aa1c", "rival-sans-n7.woff2"),
    ("rival-sans", "normal", 300, "a78e89", "00000000000000007735aa1f", "rival-sans-n3.woff2"),
    ("rival-sans", "italic", 400, "0d56a2", "00000000000000007735aa31", "rival-sans-i4.woff2"),
    ("rival-sans", "normal", 400, "556d5f", "00000000000000007735aa34", "rival-sans-n4.woff2"),
    ("rival-sans", "italic", 300, "0fd226", "00000000000000007735aa36", "rival-sans-i3.woff2"),
    ("rival-sans", "italic", 100, "2843f2", "00000000000000007735aa38", "rival-sans-i1.woff2"),
    ("ibm-plex-mono", "normal", 400, "bda79b", "00000000000000007735944d", "ibm-plex-mono-n4.woff2"),
    ("ibm-plex-mono", "normal", 800, "d37375", "00000000000000007735946a", "ibm-plex-mono-n8.woff2"),
]

TYPEKIT_CSS_HEADER = """/*
 * The Typekit service used to deliver this font or fonts for use on websites
 * is provided by Adobe and is subject to these Terms of Use
 * http://www.adobe.com/products/eulas/tou_typekit. For font license
 * information, see the list below.
 *
 * ibm-plex-mono:
 *   - http://typekit.com/eulas/00000000000000007735944d
 *   - http://typekit.com/eulas/00000000000000007735946a
 * rival-sans:
 *   - http://typekit.com/eulas/00000000000000007735aa06
 *   - http://typekit.com/eulas/00000000000000007735aa19
 *   - http://typekit.com/eulas/00000000000000007735aa1c
 *   - http://typekit.com/eulas/00000000000000007735aa1f
 *   - http://typekit.com/eulas/00000000000000007735aa31
 *   - http://typekit.com/eulas/00000000000000007735aa34
 *   - http://typekit.com/eulas/00000000000000007735aa36
 *   - http://typekit.com/eulas/00000000000000007735aa38
 *
 * © 2009-2026 Adobe Systems Incorporated. All Rights Reserved.
 */
/*{"last_published":"2024-10-15 19:56:54 UTC"}*/
"""


@dataclass
class AssetReport:
    public_dir: Path
    missing_required_paths: list[str]
    missing_required_globs: list[str]
    present_required_paths: list[str]
    optional_missing_paths: list[str]
    typekit_font_file_count: int

    @property
    def ok(self) -> bool:
        return not self.missing_required_paths and not self.missing_required_globs

    def to_dict(self) -> dict[str, object]:
        return {
            "ok": self.ok,
            "public_dir": str(self.public_dir),
            "required_paths_present": len(self.present_required_paths),
            "required_paths_total": len(REQUIRED_ASSET_PATHS),
            "missing_required_paths": self.missing_required_paths,
            "missing_required_globs": self.missing_required_globs,
            "optional_missing_paths": self.optional_missing_paths,
            "typekit_font_file_count": self.typekit_font_file_count,
        }


def fail(message: str) -> int:
    print(f"error: {message}", file=sys.stderr)
    return 1


def normalize_path(path: Path) -> Path:
    return path.expanduser().resolve()


def resolve_source_child(source_root: Path, source_rel: str, dest_rel: str) -> Path | None:
    candidates = [
        source_root / source_rel,
        source_root / dest_rel,
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists() and dst.is_file():
        raise RuntimeError(f"target path is a file: {dst}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst, dirs_exist_ok=True)


def render_typekit_css() -> str:
    blocks = [TYPEKIT_CSS_HEADER]
    for family, style, weight, _font_hash, _font_id, filename in TYPEKIT_FONT_SPECS:
        blocks.append(
            "\n".join(
                [
                    "",
                    "@font-face {",
                    f'font-family:"{family}";',
                    f'src:url("font-files/{filename}") format("woff2");',
                    f"font-display:auto;font-style:{style};font-weight:{weight};font-stretch:normal;",
                    "}",
                ]
            )
        )
    blocks.append("")
    blocks.append('.tk-rival-sans { font-family: "rival-sans",sans-serif; }')
    blocks.append('.tk-ibm-plex-mono { font-family: "ibm-plex-mono",sans-serif; }')
    blocks.append("")
    return "\n".join(blocks)


def normalize_typekit_assets(public_dir: Path) -> None:
    typekit_dir = public_dir / "use.typekit.net"
    font_dir = typekit_dir / "font-files"
    font_dir.mkdir(parents=True, exist_ok=True)

    for _family, _style, _weight, font_hash, font_id, filename in TYPEKIT_FONT_SPECS:
        source_dir = typekit_dir / "af" / font_hash / font_id / "30"
        source_candidates = sorted(source_dir.glob("l?*"))
        if not source_candidates:
            raise RuntimeError(f"typekit woff2 source missing: {source_dir}")
        shutil.copy2(source_candidates[0], font_dir / filename)

    (typekit_dir / "utz6mli.css").write_text(render_typekit_css(), encoding="utf-8")
    shutil.rmtree(typekit_dir / "af", ignore_errors=True)
    shutil.rmtree(public_dir / "p.typekit.net", ignore_errors=True)


def install_assets(source_root: Path, public_dir: Path) -> list[str]:
    source_root = normalize_path(source_root)
    public_dir = normalize_path(public_dir)
    copied: list[str] = []

    if not source_root.exists():
        raise RuntimeError(f"source mirror does not exist: {source_root}")

    for source_rel, dest_rel in COPY_SPECS:
        src = resolve_source_child(source_root, source_rel, dest_rel)
        if src is None:
            raise RuntimeError(f"source mirror missing {source_rel} or {dest_rel}")
        dst = public_dir / dest_rel
        copy_tree(src, dst)
        copied.append(dest_rel)

    normalize_typekit_assets(public_dir)
    copied.append("normalized Typekit font files")

    if DEFAULT_FALLBACK_ASSET_DIR.exists():
        copy_tree(DEFAULT_FALLBACK_ASSET_DIR, public_dir)
        copied.append("arxiv-html-paper fallback assets")

    return copied


def build_asset_report(public_dir: Path) -> AssetReport:
    public_dir = normalize_path(public_dir)
    missing_required_paths: list[str] = []
    present_required_paths: list[str] = []
    optional_missing_paths: list[str] = []
    missing_required_globs: list[str] = []

    for rel in REQUIRED_ASSET_PATHS:
        if (public_dir / rel).is_file():
            present_required_paths.append(rel)
        else:
            missing_required_paths.append(rel)

    for rel in OPTIONAL_ASSET_PATHS:
        if not (public_dir / rel).is_file():
            optional_missing_paths.append(rel)

    for pattern in REQUIRED_ASSET_GLOBS:
        if not any(public_dir.glob(pattern)):
            missing_required_globs.append(pattern)

    font_count = sum(1 for path in (public_dir / "use.typekit.net" / "font-files").glob("*.woff2"))

    return AssetReport(
        public_dir=public_dir,
        missing_required_paths=missing_required_paths,
        missing_required_globs=missing_required_globs,
        present_required_paths=present_required_paths,
        optional_missing_paths=optional_missing_paths,
        typekit_font_file_count=font_count,
    )


def print_asset_report(report: AssetReport, as_json: bool = False) -> None:
    if as_json:
        print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
        return

    status = "ok" if report.ok else "failed"
    print(f"arXiv HTML paper assets: {status}")
    print(f"public dir: {report.public_dir}")
    print(f"required paths: {len(report.present_required_paths)}/{len(REQUIRED_ASSET_PATHS)}")
    print(f"typekit font files: {report.typekit_font_file_count}")

    if report.missing_required_paths:
        print("missing required paths:")
        for rel in report.missing_required_paths:
            print(f"  - {rel}")

    if report.missing_required_globs:
        print("missing required glob matches:")
        for pattern in report.missing_required_globs:
            print(f"  - {pattern}")

    if report.optional_missing_paths:
        print("optional paths missing:")
        for rel in report.optional_missing_paths:
            print(f"  - {rel}")


def read_template(template_dir: Path, name: str) -> str:
    path = normalize_path(template_dir) / name
    if not path.is_file():
        raise RuntimeError(f"template not found: {path}")
    return path.read_text(encoding="utf-8")


def render_template(text: str, values: dict[str, str]) -> str:
    rendered = text
    for key, value in values.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    return rendered


def write_file(path: Path, content: str, force: bool) -> None:
    path = normalize_path(path)
    if path.exists() and not force:
        raise RuntimeError(f"target exists, use --force to overwrite: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def layout_import_path(layout_target: Path, page_target: Path) -> str:
    rel = os.path.relpath(normalize_path(layout_target), normalize_path(page_target).parent)
    rel = rel.replace(os.sep, "/")
    if not rel.startswith("."):
        rel = "./" + rel
    return rel


def write_layout(template_dir: Path, target: Path, force: bool) -> Path:
    content = read_template(template_dir, "PaperReaderLayout.astro")
    write_file(target, content, force=force)
    return normalize_path(target)


def write_page(
    template_dir: Path,
    target: Path,
    layout_target: Path,
    force: bool,
    values: dict[str, str],
) -> Path:
    content = read_template(template_dir, "paper.astro")
    values = dict(values)
    values["LAYOUT_IMPORT"] = layout_import_path(layout_target, target)
    write_file(target, render_template(content, values), force=force)
    return normalize_path(target)


def default_page_values(args: argparse.Namespace) -> dict[str, str]:
    return {
        "TITLE": args.title,
        "DESCRIPTION": args.description,
        "AUTHOR": args.author,
        "DATE_LABEL": args.date_label,
        "ABSTRACT": args.abstract,
        "KEYWORDS": args.keywords,
        "ARXIV_ID": args.arxiv_id,
        "CATEGORY": args.category,
    }


def cmd_print_mirror_command(args: argparse.Namespace) -> int:
    output_dir = args.output_dir
    url = args.url
    print(
        "wget --page-requisites --convert-links --adjust-extension --span-hosts "
        "--domains=arxiv.org,static.arxiv.org,use.typekit.net "
        "--no-parent --wait=0.2 --timeout=30 --tries=2 "
        f"--directory-prefix={output_dir} {url}"
    )
    print(
        "monolith --isolate --ignore-errors --timeout 120 "
        f"--output {output_dir}/monolith/snapshot.singlefile.html {url}"
    )
    return 0


def cmd_install_assets(args: argparse.Namespace) -> int:
    try:
        copied = install_assets(args.source, args.public_dir)
    except RuntimeError as exc:
        return fail(str(exc))
    for rel in copied:
        print(f"copied: {rel}")
    report = build_asset_report(args.public_dir)
    print_asset_report(report, as_json=args.json)
    return 0 if report.ok else 1


def cmd_verify_assets(args: argparse.Namespace) -> int:
    report = build_asset_report(args.public_dir)
    print_asset_report(report, as_json=args.json)
    return 0 if report.ok else 1


def cmd_write_layout(args: argparse.Namespace) -> int:
    try:
        target = write_layout(args.template_dir, args.target, force=args.force)
    except RuntimeError as exc:
        return fail(str(exc))
    print(f"wrote layout: {target}")
    return 0


def cmd_write_page(args: argparse.Namespace) -> int:
    try:
        target = write_page(
            args.template_dir,
            args.target,
            args.layout_target,
            force=args.force,
            values=default_page_values(args),
        )
    except RuntimeError as exc:
        return fail(str(exc))
    print(f"wrote page: {target}")
    return 0


def cmd_scaffold(args: argparse.Namespace) -> int:
    web_root = normalize_path(args.web_root)
    public_dir = args.public_dir or web_root / "public"
    layout_target = args.layout_target or web_root / "src/layouts/PaperReaderLayout.astro"
    page_target = args.page_target or web_root / f"src/pages/{args.slug}.astro"

    if not args.skip_assets:
        try:
            copied = install_assets(args.source, public_dir)
        except RuntimeError as exc:
            return fail(str(exc))
        for rel in copied:
            print(f"copied: {rel}")

    try:
        print(f"wrote layout: {write_layout(args.template_dir, layout_target, force=args.force)}")
        print(
            "wrote page: "
            + str(
                write_page(
                    args.template_dir,
                    page_target,
                    layout_target,
                    force=args.force,
                    values=default_page_values(args),
                )
            )
        )
    except RuntimeError as exc:
        return fail(str(exc))

    report = build_asset_report(public_dir)
    print_asset_report(report, as_json=args.json)
    return 0 if report.ok else 1


def add_common_page_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--title", default="arXiv-style HTML Paper")
    parser.add_argument("--description", default="Reusable arXiv HTML papers reader")
    parser.add_argument("--author", default="Local Research Notes")
    parser.add_argument("--date-label", default="Working paper")
    parser.add_argument("--abstract", default="Replace this abstract with the paper summary.")
    parser.add_argument("--keywords", default="research; model; visualization")
    parser.add_argument("--arxiv-id", default="local.paper.0001")
    parser.add_argument("--category", default="cs.HC")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Install and scaffold the arXiv HTML papers reader resources for Astro projects."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    mirror = subparsers.add_parser("print-mirror-command", help="print wget/monolith commands for mirroring a paper")
    mirror.add_argument("--url", default=DEFAULT_PAPER_URL)
    mirror.add_argument("--output-dir", default=".research/arxiv-html/2606.26689v1")
    mirror.set_defaults(func=cmd_print_mirror_command)

    install = subparsers.add_parser("install-assets", help="copy arXiv reader CSS/JS/icons/fonts into public/")
    install.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    install.add_argument("--public-dir", type=Path, default=DEFAULT_PUBLIC_DIR)
    install.add_argument("--json", action="store_true")
    install.set_defaults(func=cmd_install_assets)

    verify = subparsers.add_parser("verify-assets", help="verify local arXiv reader resources")
    verify.add_argument("--public-dir", type=Path, default=DEFAULT_PUBLIC_DIR)
    verify.add_argument("--json", action="store_true")
    verify.set_defaults(func=cmd_verify_assets)

    layout = subparsers.add_parser("write-layout", help="write PaperReaderLayout.astro from the reusable template")
    layout.add_argument("--template-dir", type=Path, default=DEFAULT_TEMPLATE_DIR)
    layout.add_argument("--target", type=Path, default=DEFAULT_LAYOUT_TARGET)
    layout.add_argument("--force", action="store_true")
    layout.set_defaults(func=cmd_write_layout)

    page = subparsers.add_parser("write-page", help="write a starter arXiv-style paper route")
    page.add_argument("--template-dir", type=Path, default=DEFAULT_TEMPLATE_DIR)
    page.add_argument("--target", type=Path, default=DEFAULT_PAGE_TARGET)
    page.add_argument("--layout-target", type=Path, default=DEFAULT_LAYOUT_TARGET)
    page.add_argument("--force", action="store_true")
    add_common_page_args(page)
    page.set_defaults(func=cmd_write_page)

    scaffold = subparsers.add_parser("scaffold", help="install assets and write layout/page in one step")
    scaffold.add_argument("--web-root", type=Path, default=Path("web"))
    scaffold.add_argument("--public-dir", type=Path)
    scaffold.add_argument("--layout-target", type=Path)
    scaffold.add_argument("--page-target", type=Path)
    scaffold.add_argument("--template-dir", type=Path, default=DEFAULT_TEMPLATE_DIR)
    scaffold.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    scaffold.add_argument("--slug", default="paper")
    scaffold.add_argument("--skip-assets", action="store_true")
    scaffold.add_argument("--force", action="store_true")
    scaffold.add_argument("--json", action="store_true")
    add_common_page_args(scaffold)
    scaffold.set_defaults(func=cmd_scaffold)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
