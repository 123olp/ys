#!/usr/bin/env python3
"""在相同 Chromium 环境中比较官方中文维基首页与本地首页。"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import Any

try:
    from playwright.async_api import Browser, Page, async_playwright
except ModuleNotFoundError as error:
    raise SystemExit(
        "缺少 Playwright；请安装 Python playwright 并执行 playwright install chromium。"
    ) from error


VIEWPORTS = {
    "desktop": {"width": 1440, "height": 1000},
    "mobile": {"width": 390, "height": 844},
}
SELECTORS = {
    "root": "#mp-2012",
    "banner": "#mp-2012-banner",
    "logo": "#mp-2012-banner-logo",
    "title": "#mp-2012-banner-title",
    "heading": "#mp-2012-banner-title h1",
    "intro": "#mp-2012-banner-intro",
    "left": "#mp-2012-column-left",
    "right": "#mp-2012-column-right",
}
STYLE_FIELDS = ("fontSize", "lineHeight", "margin", "padding")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--official-url",
        default="https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5",
    )
    parser.add_argument("--local-url", default="http://127.0.0.1:18782/")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("runtime/homepage-compare"),
    )
    parser.add_argument("--tolerance", type=float, default=1.0)
    return parser.parse_args()


async def collect_page(
    browser: Browser,
    label: str,
    url: str,
    viewport: dict[str, int],
    output: Path,
) -> dict[str, Any]:
    context = await browser.new_context(
        viewport=viewport,
        device_scale_factor=1,
        color_scheme="light",
    )
    page = await context.new_page()
    errors: list[str] = []
    page.on(
        "console",
        lambda message: errors.append(f"console:{message.type}:{message.text}")
        if message.type == "error"
        else None,
    )
    page.on("pageerror", lambda error: errors.append(f"pageerror:{error}"))
    page.on(
        "requestfailed",
        lambda request: errors.append(
            f"requestfailed:{request.url}:{request.failure or 'unknown'}"
        ),
    )

    await page.goto(url, wait_until="domcontentloaded", timeout=60_000)
    await page.wait_for_selector(SELECTORS["root"], timeout=30_000)
    await page.wait_for_timeout(500)
    metrics = await extract_metrics(page)
    await page.screenshot(path=output / f"{label}.png", full_page=True)
    (output / f"{label}-errors.txt").write_text(
        "\n".join(errors),
        encoding="utf-8",
    )
    metrics["errors"] = errors
    await context.close()
    return metrics


async def extract_metrics(page: Page) -> dict[str, Any]:
    return await page.evaluate(
        """(selectors) => {
            const elements = {};
            for (const [name, selector] of Object.entries(selectors)) {
                const element = document.querySelector(selector);
                if (!element) {
                    elements[name] = null;
                    continue;
                }
                const rect = element.getBoundingClientRect();
                const style = getComputedStyle(element);
                elements[name] = {
                    x: rect.x,
                    y: rect.y,
                    width: rect.width,
                    height: rect.height,
                    display: style.display,
                    fontSize: style.fontSize,
                    lineHeight: style.lineHeight,
                    margin: style.margin,
                    padding: style.padding
                };
            }
            return {
                htmlClass: document.documentElement.className,
                document: {
                    width: document.documentElement.scrollWidth,
                    height: document.documentElement.scrollHeight
                },
                viewport: { width: innerWidth, height: innerHeight },
                elements
            };
        }""",
        SELECTORS,
    )


def normalize(metrics: dict[str, Any]) -> dict[str, Any]:
    elements = metrics["elements"]
    root = elements["root"]
    banner = elements["banner"]
    normalized: dict[str, Any] = {
        "horizontalOverflow": metrics["document"]["width"] - metrics["viewport"]["width"],
        "standardFont": "vector-feature-custom-font-size-clientpref-1"
        in metrics["htmlClass"],
        "elements": {},
    }
    for name, values in elements.items():
        if values is None:
            normalized["elements"][name] = None
            continue
        item = dict(values)
        item["x"] -= root["x"]
        item["y"] -= root["y"]
        if name in {"left", "right"}:
            item["y"] -= banner["height"]
        normalized["elements"][name] = item
    return normalized


def compare(
    official: dict[str, Any],
    local: dict[str, Any],
    mode: str,
    tolerance: float,
) -> list[str]:
    failures: list[str] = []
    if not local["standardFont"]:
        failures.append(f"{mode}: 本地 Vector 未使用标准字号")
    if local["horizontalOverflow"] > tolerance:
        failures.append(
            f"{mode}: 本地横向溢出 {local['horizontalOverflow']:.2f}px"
        )

    geometry_contract = {
        "root": ("x", "y", "width"),
        "banner": ("x", "y", "width", "height"),
        "title": ("x", "y", "width", "height"),
        "heading": ("x", "height"),
        "intro": ("x", "y", "width", "height"),
        "left": ("x", "y", "width"),
        "right": ("x", "width") if mode == "mobile" else ("x", "y", "width"),
    }
    names = tuple(geometry_contract)
    for name in names:
        expected = official["elements"][name]
        actual = local["elements"][name]
        if expected is None or actual is None:
            failures.append(f"{mode}: 缺少契约节点 {name}")
            continue
        for field in geometry_contract[name]:
            difference = abs(expected[field] - actual[field])
            field_tolerance = 2.0 if mode == "mobile" and name == "left" else tolerance
            if difference > field_tolerance:
                failures.append(
                    f"{mode}:{name}.{field} 偏差 {difference:.2f}px "
                    f"(official={expected[field]:.2f}, local={actual[field]:.2f})"
                )
        for field in STYLE_FIELDS:
            if expected[field] != actual[field]:
                failures.append(
                    f"{mode}:{name}.{field} 不一致 "
                    f"(official={expected[field]}, local={actual[field]})"
                )

    if mode == "mobile":
        logo = local["elements"]["logo"]
        if logo is None or logo["display"] != "none":
            failures.append("mobile: 本地品牌标志槽未按官方移动端几何折叠")
    return failures


async def run(args: argparse.Namespace) -> int:
    args.output.mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {"runs": {}, "failures": []}
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        for mode, viewport in VIEWPORTS.items():
            official = await collect_page(
                browser,
                f"official-{mode}",
                args.official_url,
                viewport,
                args.output,
            )
            local = await collect_page(
                browser,
                f"local-{mode}",
                args.local_url,
                viewport,
                args.output,
            )
            official_normalized = normalize(official)
            local_normalized = normalize(local)
            failures = compare(
                official_normalized,
                local_normalized,
                mode,
                args.tolerance,
            )
            if local["errors"]:
                failures.extend(f"{mode}: {error}" for error in local["errors"])
            report["runs"][mode] = {
                "official": official,
                "local": local,
                "officialNormalized": official_normalized,
                "localNormalized": local_normalized,
            }
            report["failures"].extend(failures)
        await browser.close()

    report["status"] = "PASS" if not report["failures"] else "FAIL"
    (args.output / "report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wikipedia 首页浏览器对比: {report['status']}")
    print(f"证据目录: {args.output.resolve()}")
    for failure in report["failures"]:
        print(f"- {failure}")
    return 0 if report["status"] == "PASS" else 1


def main() -> None:
    args = parse_args()
    try:
        result = asyncio.run(run(args))
    except Exception as error:
        print(f"浏览器对比执行失败: {error}", file=sys.stderr)
        raise SystemExit(2) from error
    raise SystemExit(result)


if __name__ == "__main__":
    main()
