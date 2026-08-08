#!/usr/bin/env python3
"""Fail closed when current files, Git history, or CI policy expose private data."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
import sys
import threading
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator


CANONICAL_NAME = "tradecatlabs"
CANONICAL_EMAIL = "tradecatlabs@users.noreply.github.com"
MAX_REPORTED_FINDINGS = 20

TEXT_RULES = (
    (
        "linux-user-path",
        re.compile(
            r"/home/[A-Za-z0-9._-]+/(?:\.projects|Downloads|Desktop|Documents|workspace|src|code)(?:/|`|$)"
        ),
    ),
    ("windows-user-path", re.compile(r"(?:[A-Za-z]:\\|/mnt/[a-z]/)Users[/\\][A-Za-z0-9._-]+[/\\]")),
    ("wsl-unc-path", re.compile(r"\\\\wsl(?:\.localhost|\$)\\", re.IGNORECASE)),
    ("machine-hostname", re.compile(r"\bLAPTOP-(?=[A-Z0-9]{7,15}\b)(?=[A-Z0-9]*\d)[A-Z0-9]+\b")),
    ("cloudflare-api-token", re.compile(r"\bcfat_[A-Za-z0-9_-]{30,}\b")),
    ("telegram-bot-token", re.compile(r"\b\d{8,12}:[A-Za-z0-9_-]{30,}\b")),
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
    ("openai-api-key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("aws-access-key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("private-key-material", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
)

SENSITIVE_SUFFIXES = {".key", ".p12", ".pfx"}
SENSITIVE_NAMES = {"aau_token", "id_rsa", "id_ed25519", "id_ecdsa"}
ENV_EXAMPLES = {".env.example", ".env.sample", ".env.template"}
WORKFLOW_SUFFIXES = {".yml", ".yaml"}
PINNED_ACTION = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+@[0-9a-f]{40}$")
AUTHOR_HEADER = re.compile(r"^author (.*) <([^<>]+)> \d+ [+-]\d{4}$")
COMMITTER_HEADER = re.compile(r"^committer (.*) <([^<>]+)> \d+ [+-]\d{4}$")


class AuditFailure(RuntimeError):
    """Raised when Git cannot provide trustworthy audit input."""


@dataclass(frozen=True)
class Finding:
    rule: str
    path: str = ""
    line: int = 0
    revision: str = ""

    def safe_location(self) -> str:
        payload = "\0".join((self.rule, self.path, str(self.line), self.revision))
        return hashlib.sha256(payload.encode("utf-8", errors="surrogateescape")).hexdigest()[:16]

    def local_location(self) -> str:
        location = self.path or "commit-metadata"
        if self.line:
            location = f"{location}:{self.line}"
        if self.revision:
            location = f"{self.revision[:12]}:{location}"
        return re.sub(
            r"[\x00-\x1f\x7f-\x9f]",
            lambda match: f"\\x{ord(match.group()):02x}",
            location,
        )


class Findings:
    def __init__(self) -> None:
        self.total = 0
        self.items: list[Finding] = []

    def add(self, finding: Finding) -> None:
        self.total += 1
        if len(self.items) < MAX_REPORTED_FINDINGS:
            self.items.append(finding)


def run_git(root: Path, args: list[str], *, input_data: bytes | None = None) -> bytes:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=root,
            input=input_data,
            check=True,
            capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise AuditFailure("git-input-unavailable") from exc
    return result.stdout


def tracked_files(root: Path) -> list[str]:
    output = run_git(root, ["ls-files", "-z"])
    return [item.decode("utf-8", errors="surrogateescape") for item in output.split(b"\0") if item]


def sensitive_filename(relative: str) -> bool:
    name = Path(relative).name.lower()
    if name in SENSITIVE_NAMES or Path(name).suffix in SENSITIVE_SUFFIXES:
        return True
    return name == ".env" or (name.startswith(".env.") and name not in ENV_EXAMPLES)


def scan_text(body: str, path: str, findings: Findings, *, revision: str = "") -> None:
    for rule_name, pattern in TEXT_RULES:
        line_number = 1
        previous_offset = 0
        for match in pattern.finditer(body):
            line_number += body.count("\n", previous_offset, match.start())
            previous_offset = match.start()
            findings.add(Finding(rule_name, path, line_number, revision))


def workflow_files(relative_files: list[str]) -> list[str]:
    return [
        relative
        for relative in relative_files
        if relative.startswith(".github/workflows/") and Path(relative).suffix.lower() in WORKFLOW_SUFFIXES
    ]


def scan_workflow_policy(body: str, path: str, findings: Findings) -> None:
    checks = (
        ("workflow-pull-request-target", re.compile(r"\bpull_request_target\s*:")),
        ("workflow-secret-reference", re.compile(r"\$\{\{\s*secrets\.")),
        ("workflow-debug-output", re.compile(r"(?mi)^\s*(?:run:\s*)?(?:set\s+-x|printenv(?:\s|$)|env\s*$)")),
        ("workflow-debug-flag", re.compile(r"ACTIONS_(?:STEP|RUNNER)_DEBUG")),
        ("workflow-write-permission", re.compile(r"(?m)^\s*(?:permissions:\s*write-all|[A-Za-z-]+:\s*write)\s*$")),
    )
    for rule, pattern in checks:
        if pattern.search(body):
            findings.add(Finding(rule, path))

    required = (
        ("workflow-minimal-permissions", re.compile(r"(?m)^permissions:\s*\n\s+contents:\s*read\s*$")),
        ("workflow-full-history", re.compile(r"(?m)^\s+fetch-depth:\s*0\s*$")),
        ("workflow-no-persisted-credentials", re.compile(r"(?m)^\s+persist-credentials:\s*false\s*$")),
        ("workflow-ci-redaction-mode", re.compile(r"(?m)^\s+PRIVACY_REPORT_MODE:\s*ci\s*$")),
    )
    for rule, pattern in required:
        if not pattern.search(body):
            findings.add(Finding(rule, path))

    privacy_command = "tools/audit_repository_privacy.py --scope all"
    privacy_offset = body.find(privacy_command)
    if privacy_offset < 0:
        findings.add(Finding("workflow-privacy-preflight-missing", path))
    else:
        privacy_line_start = body.rfind("\n", 0, privacy_offset) + 1
        before_privacy = body[:privacy_line_start]
        if re.search(r"(?m)^(?:\s+-\s*run:|\s{8,}run:)\s*", before_privacy):
            findings.add(Finding("workflow-privacy-preflight-order", path))
        for action_match in re.finditer(r"(?m)^\s*-?\s*uses:\s*([^\s#]+)", before_privacy):
            action = action_match.group(1)
            if not (action.startswith("actions/checkout@") or action.startswith("actions/setup-python@")):
                findings.add(Finding("workflow-privacy-preflight-order", path))
                break

    for line_number, line in enumerate(body.splitlines(), start=1):
        stripped = line.strip().removeprefix("- ").lstrip()
        if not stripped.startswith("uses:"):
            continue
        action = stripped.removeprefix("uses:").strip().split(" #", 1)[0]
        if action.startswith("./"):
            continue
        if not PINNED_ACTION.fullmatch(action):
            findings.add(Finding("workflow-action-not-pinned", path, line_number))


def audit_current(root: Path, findings: Findings) -> None:
    relative_files = tracked_files(root)
    for relative in relative_files:
        path = root / relative
        if not path.is_file():
            continue
        if sensitive_filename(relative):
            findings.add(Finding("sensitive-filename", relative))
        data = path.read_bytes()
        if b"\0" not in data:
            scan_text(data.decode("utf-8", errors="replace"), relative, findings)

    for relative in workflow_files(relative_files):
        body = (root / relative).read_text(encoding="utf-8", errors="replace")
        scan_workflow_policy(body, relative, findings)


def batch_objects(root: Path, object_ids: list[str]) -> Iterator[tuple[str, str, bytes]]:
    if not object_ids:
        return
    try:
        process = subprocess.Popen(
            ["git", "cat-file", "--batch"],
            cwd=root,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
    except OSError as exc:
        raise AuditFailure("git-batch-unavailable") from exc
    if process.stdin is None or process.stdout is None:
        process.kill()
        raise AuditFailure("git-batch-pipe-unavailable")

    def write_objects() -> None:
        try:
            for object_id in object_ids:
                process.stdin.write(object_id.encode("ascii") + b"\n")
            process.stdin.close()
        except (BrokenPipeError, OSError, ValueError):
            return

    writer = threading.Thread(target=write_objects, name="git-cat-file-writer", daemon=True)
    writer.start()
    try:
        for _ in object_ids:
            header = process.stdout.readline().decode("ascii", errors="strict").split()
            if len(header) != 3:
                raise AuditFailure("git-batch-header-invalid")
            object_id, object_type, raw_size = header
            size = int(raw_size)
            body = process.stdout.read(size)
            separator = process.stdout.read(1)
            if len(body) != size or separator != b"\n":
                raise AuditFailure("git-batch-body-invalid")
            yield object_id, object_type, body
    finally:
        writer.join(timeout=5)
        return_code = process.wait(timeout=5)
        if return_code != 0:
            raise AuditFailure("git-batch-failed")


def audit_commit(root: Path, revision: str, body: bytes, findings: Findings) -> None:
    text = body.decode("utf-8", errors="replace")
    headers, _, message = text.partition("\n\n")
    author = None
    committer = None
    for line in headers.splitlines():
        if match := AUTHOR_HEADER.match(line):
            author = match.groups()
        elif match := COMMITTER_HEADER.match(line):
            committer = match.groups()
    if author != (CANONICAL_NAME, CANONICAL_EMAIL):
        findings.add(Finding("commit-author-identity", revision=revision))
    if committer != (CANONICAL_NAME, CANONICAL_EMAIL):
        findings.add(Finding("commit-committer-identity", revision=revision))
    scan_text(message, "commit-message", findings, revision=revision)


def audit_history(root: Path, revision: str, findings: Findings) -> None:
    resolved = run_git(root, ["rev-parse", "--verify", f"{revision}^{{commit}}"])
    resolved_revision = resolved.decode("ascii").strip()
    commit_ids = run_git(root, ["rev-list", resolved_revision]).decode("ascii").splitlines()
    for object_id, object_type, body in batch_objects(root, commit_ids):
        if object_type != "commit":
            raise AuditFailure("git-history-object-not-commit")
        audit_commit(root, object_id, body, findings)

    historical_paths = run_git(
        root,
        ["log", "-z", "--format=", "--name-only", resolved_revision],
    ).split(b"\0")
    for raw_path in historical_paths:
        if not raw_path:
            continue
        relative = raw_path.decode("utf-8", errors="surrogateescape").lstrip("\n")
        if relative and sensitive_filename(relative):
            findings.add(Finding("historical-sensitive-filename", relative))

    object_lines = run_git(root, ["rev-list", "--objects", resolved_revision]).splitlines()
    object_paths: dict[str, str] = {}
    for raw_line in object_lines:
        object_id, separator, raw_path = raw_line.partition(b" ")
        if not separator:
            continue
        relative = raw_path.decode("utf-8", errors="surrogateescape")
        object_key = object_id.decode("ascii")
        object_paths.setdefault(object_key, relative)

    for object_id, object_type, body in batch_objects(root, list(object_paths)):
        if object_type != "blob" or b"\0" in body:
            continue
        relative = object_paths[object_id]
        scan_text(body.decode("utf-8", errors="replace"), relative, findings, revision=object_id)


def report(findings: Findings, mode: str) -> int:
    if findings.total == 0:
        print("repository privacy audit: PASS")
        return 0
    for finding in findings.items:
        if mode == "ci":
            location = f"location_id={finding.safe_location()}"
        else:
            location = finding.local_location()
        print(f"ERROR: {finding.rule}: {location}", file=sys.stderr)
    omitted = findings.total - len(findings.items)
    if omitted:
        print(f"ERROR: additional findings omitted: {omitted}", file=sys.stderr)
    print(f"repository privacy audit: FAIL ({findings.total} finding(s))", file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Git 仓库根目录")
    parser.add_argument("--scope", choices=("current", "history", "all"), default="current")
    parser.add_argument("--revision", default="HEAD", help="历史扫描起点")
    parser.add_argument(
        "--report-mode",
        choices=("local", "ci"),
        default=os.environ.get("PRIVACY_REPORT_MODE", "local"),
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()
    findings = Findings()

    try:
        if args.scope in {"current", "all"}:
            audit_current(root, findings)
        if args.scope in {"history", "all"}:
            audit_history(root, args.revision, findings)
    except Exception as exc:
        if args.report_mode == "ci":
            print("ERROR: privacy audit could not establish trusted input", file=sys.stderr)
        else:
            print(f"ERROR: privacy audit could not run: {exc}", file=sys.stderr)
        return 2

    return report(findings, args.report_mode)


if __name__ == "__main__":
    raise SystemExit(main())
