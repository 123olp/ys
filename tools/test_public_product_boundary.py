#!/usr/bin/env python3
"""Contract tests for the public product-source boundary."""

from __future__ import annotations

import unittest

from audit_public_product_boundary import (
    FORBIDDEN_EXACT,
    FORBIDDEN_PREFIXES,
    FORBIDDEN_TOOL,
)


class PublicProductBoundaryTests(unittest.TestCase):
    def test_product_roots_are_forbidden(self) -> None:
        self.assertTrue("wiki/content/Page.wiki".startswith(FORBIDDEN_PREFIXES))
        self.assertTrue("docs/reference/history-timeline/timeline.json".startswith(FORBIDDEN_PREFIXES))
        self.assertTrue("tools/tech-tree-reference-capture/capture.sh".startswith(FORBIDDEN_PREFIXES))

    def test_timeline_tools_are_forbidden(self) -> None:
        self.assertIsNotNone(FORBIDDEN_TOOL.match("tools/validate_history_timeline.py"))
        self.assertIsNotNone(FORBIDDEN_TOOL.match("tools/history_timeline_rounds_401_500.json"))

    def test_public_research_docs_remain_allowed(self) -> None:
        path = "docs/reference/evidence-policy.md"
        self.assertNotIn(path, FORBIDDEN_EXACT)
        self.assertFalse(path.startswith(FORBIDDEN_PREFIXES))
        self.assertIsNone(FORBIDDEN_TOOL.match(path))


if __name__ == "__main__":
    unittest.main()
