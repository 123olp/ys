#!/usr/bin/env python3
"""Regression tests for the repository privacy gate."""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


AUDITOR = Path(__file__).with_name("audit_repository_privacy.py").resolve()
CANONICAL_NAME = "tradecatlabs"
CANONICAL_EMAIL = "tradecatlabs@users.noreply.github.com"
PIN = "a" * 40


def run(command: list[str], root: Path, *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=root, check=check, capture_output=True, text=True)


class PrivacyAuditTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        run(["git", "init", "--quiet", "--initial-branch", "main"], self.root)
        run(["git", "config", "user.name", CANONICAL_NAME], self.root)
        run(["git", "config", "user.email", CANONICAL_EMAIL], self.root)
        workflow = self.root / ".github/workflows/check.yml"
        workflow.parent.mkdir(parents=True)
        workflow.write_text(
            """name: Check
on: [push, pull_request]
permissions:
  contents: read
env:
  PRIVACY_REPORT_MODE: ci
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@%s
        with:
          fetch-depth: 0
          persist-credentials: false
      - name: Run privacy preflight
        run: python tools/audit_repository_privacy.py --scope all
"""
            % PIN,
            encoding="utf-8",
        )
        (self.root / "README.md").write_text("clean\n", encoding="utf-8")
        self.commit("initial")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def commit(self, message: str) -> None:
        run(["git", "add", "--all"], self.root)
        run(["git", "commit", "--quiet", "--message", message], self.root)

    def audit(self, scope: str) -> subprocess.CompletedProcess[str]:
        return run(
            [
                "python3",
                str(AUDITOR),
                "--scope",
                scope,
                "--report-mode",
                "ci",
            ],
            self.root,
            check=False,
        )

    def test_clean_history_passes(self) -> None:
        result = self.audit("all")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_untrusted_git_input_fails_without_exception_or_path(self) -> None:
        with tempfile.TemporaryDirectory() as not_a_repository:
            result = run(
                [
                    "python3",
                    str(AUDITOR),
                    "--root",
                    not_a_repository,
                    "--scope",
                    "history",
                    "--report-mode",
                    "ci",
                ],
                Path(not_a_repository),
                check=False,
            )
        self.assertEqual(result.returncode, 2)
        self.assertEqual(
            result.stderr.strip(),
            "ERROR: privacy audit could not establish trusted input",
        )
        self.assertNotIn(not_a_repository, result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_ci_output_redacts_current_secret_and_path(self) -> None:
        token = "123456789:" + "A" * 35
        private_path = self.root / ".env"
        private_path.write_text(f"BOT_TOKEN={token}\n", encoding="utf-8")
        run(["git", "add", ".env", "--force"], self.root)
        result = self.audit("current")
        self.assertEqual(result.returncode, 1)
        self.assertIn("telegram-bot-token", result.stderr)
        self.assertIn("sensitive-filename", result.stderr)
        self.assertNotIn(token, result.stderr)
        self.assertNotIn(".env", result.stderr)
        self.assertRegex(result.stderr, r"location_id=[0-9a-f]{16}")

    def test_removed_secret_is_detected_in_history_without_echo(self) -> None:
        token = "cfat_" + "B" * 40
        filename = ".env.private"
        (self.root / filename).write_text(token + "\n", encoding="utf-8")
        self.commit("add private material")
        (self.root / filename).unlink()
        self.commit("remove private material")
        result = self.audit("history")
        self.assertEqual(result.returncode, 1)
        self.assertIn("cloudflare-api-token", result.stderr)
        self.assertIn("historical-sensitive-filename", result.stderr)
        self.assertNotIn(token, result.stderr)
        self.assertNotIn(filename, result.stderr)

    def test_noncanonical_commit_identity_is_redacted(self) -> None:
        run(["git", "config", "user.name", "Private Person"], self.root)
        run(["git", "config", "user.email", "private@example.test"], self.root)
        (self.root / "identity.txt").write_text("identity test\n", encoding="utf-8")
        self.commit("identity test")
        result = self.audit("history")
        self.assertEqual(result.returncode, 1)
        self.assertIn("commit-author-identity", result.stderr)
        self.assertNotIn("Private Person", result.stderr)
        self.assertNotIn("private@example.test", result.stderr)

    def test_workflow_policy_rejects_mutable_actions_and_secret_references(self) -> None:
        workflow = self.root / ".github/workflows/check.yml"
        workflow.write_text(
            workflow.read_text(encoding="utf-8").replace(
                f"actions/checkout@{PIN}", "actions/checkout@v4"
            )
            + "# ${{ secrets.PRIVATE_TOKEN }}\n",
            encoding="utf-8",
        )
        run(["git", "add", str(workflow.relative_to(self.root))], self.root)
        result = self.audit("current")
        self.assertEqual(result.returncode, 1)
        self.assertIn("workflow-action-not-pinned", result.stderr)
        self.assertIn("workflow-secret-reference", result.stderr)
        self.assertNotIn("PRIVATE_TOKEN", result.stderr)
        self.assertNotIn("check.yml", result.stderr)

    def test_workflow_policy_rejects_write_permission_and_late_preflight(self) -> None:
        workflow = self.root / ".github/workflows/check.yml"
        body = workflow.read_text(encoding="utf-8")
        body = body.replace("contents: read", "contents: write")
        body = body.replace(
            "    steps:\n",
            "    steps:\n      - run: pip install untrusted-package\n",
        )
        workflow.write_text(body, encoding="utf-8")
        run(["git", "add", str(workflow.relative_to(self.root))], self.root)
        result = self.audit("current")
        self.assertEqual(result.returncode, 1)
        self.assertIn("workflow-write-permission", result.stderr)
        self.assertIn("workflow-privacy-preflight-order", result.stderr)
        self.assertNotIn("untrusted-package", result.stderr)


if __name__ == "__main__":
    unittest.main()
