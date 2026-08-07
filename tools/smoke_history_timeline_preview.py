#!/usr/bin/env python3
"""Browser-level smoke gate for the history timeline preview."""

from __future__ import annotations

import functools
import http.server
import os
import sys
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "docs" / "reference" / "history-timeline"

RESOURCE_BUDGETS = {
    "echarts.common.min.js": 700_000,
    "timelinejs.light.json": 1_100_000,
    "timelinejs.detail.json": 750_000,
}
TOTAL_RESOURCE_BUDGET = 2_600_000


def fail(message: str) -> None:
    print(f"status=FAIL reason={message}")
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def tooltip_texts(page) -> list[str]:
    return page.evaluate(
        """() => Array.from(document.querySelectorAll('#chart div'))
          .filter(function (el) { return el.innerText && el.innerText.indexOf('编号：') >= 0; })
          .map(function (el) { return el.innerText; })"""
    )


def resource_transfers(page) -> dict[str, int]:
    entries = page.evaluate("performance.getEntriesByType('resource')")
    return {
        str(entry["name"].rsplit("/", 1)[-1]): int(entry["transferSize"] or 0)
        for entry in entries
    }


def main() -> None:
    os.chdir(PACKAGE)
    server = None
    try:
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(PACKAGE))
        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        url = f"http://127.0.0.1:{server.server_port}/preview.html"

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            requested = []
            page.on("request", lambda request: requested.append(request.url))
            page.goto(url, wait_until="networkidle")
            page.wait_for_selector("#chart canvas")
            page.wait_for_selector("#event-nav-index:not(:empty)")
            page.wait_for_timeout(600)

            require(page.evaluate("typeof echarts === 'object'"), "echarts_not_loaded")
            legend = page.locator("#evidence-legend").inner_text()
            require("证据等级图例" in legend, "missing_evidence_legend")

            initial = " ".join(tooltip_texts(page))
            require("HIT-TEC-001" in initial, "missing_initial_tooltip")

            page.wait_for_function(
                "document.getElementById('event-detail-text').innerText.indexOf('Claim:') >= 0",
                timeout=10000,
            )
            full_text = page.locator("#event-detail-text").inner_text()
            require("Claim:" in full_text, "auto_full_event_not_loaded")
            require("<br>" not in full_text, "detail_text_is_not_plain")
            require(
                not any(line.strip().startswith(("时期:", "路径:", "类型:", "证据:", "来源:")) for line in full_text.splitlines()),
                "detail_text_contains_duplicate_metadata",
            )
            require(any("timelinejs.detail.json" in item for item in requested), "detail_data_not_loaded")
            require(not any("timelinejs.json" in item and "detail" not in item for item in requested), "full_data_should_not_load_for_preview")
            transfers = resource_transfers(page)
            for resource, budget in RESOURCE_BUDGETS.items():
                require(resource in transfers, f"missing_resource {resource}")
                require(transfers[resource] <= budget, f"resource_over_budget {resource}={transfers[resource]}")
            total_transfer = sum(transfers.values())
            require(total_transfer <= TOTAL_RESOURCE_BUDGET, f"total_over_budget {total_transfer}")

            page.click("#next-event")
            page.wait_for_timeout(300)
            next_text = " ".join(tooltip_texts(page))
            require("HIT-THT-038" in next_text, "missing_next_tooltip")
            require("event=HIT-THT-038" in page.url, "missing_next_url_event")

            page.fill("#event-jump", "HIT-THT-032")
            page.click("#jump-event")
            page.wait_for_timeout(400)
            jump_text = " ".join(tooltip_texts(page))
            require("HIT-THT-032" in jump_text, "jump_did_not_update_tooltip")
            require("event=HIT-THT-032" in page.url, "jump_did_not_update_url")

            full_table = page.locator("#full-event-table-code").inner_text()
            require("HIT-MTH-001" in full_table, "missing_full_event_table")

            page.select_option("#mode", "density")
            page.wait_for_timeout(400)
            require(page.locator("#chart canvas").count() > 0, "density_chart_missing")

            page.select_option("#scope", "works")
            page.wait_for_timeout(500)
            scope_table = page.locator("#scope-summary-table").inner_text()
            require("全部资料" in scope_table and "399" in scope_table, "scope_aggregate_not_updated")

            browser.close()
    finally:
        if server is not None:
            server.shutdown()
            server.server_close()
    print("status=OK history_timeline_browser=pass")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pragma: no cover
        print(f"status=FAIL reason=unexpected_error detail={type(exc).__name__}: {exc}")
        raise SystemExit(1) from exc
