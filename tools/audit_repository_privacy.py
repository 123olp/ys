#!/usr/bin/env python3
"""Fail closed when tracked files expose local identity or credentials."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


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
    (
        "private-key-material",
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    ),
)

SENSITIVE_SUFFIXES = {".key", ".p12", ".pfx"}
SENSITIVE_NAMES = {"aau_token", "id_rsa", "id_ed25519", "id_ecdsa"}
ENV_EXAMPLES = {".env.example", ".env.sample", ".env.template"}


def tracked_files(root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=root,
        check=True,
        capture_output=True,
    )
    return [item.decode("utf-8", errors="surrogateescape") for item in result.stdout.split(b"\0") if item]


def sensitive_filename(relative: str) -> bool:
    name = Path(relative).name.lower()
    if name in SENSITIVE_NAMES or Path(name).suffix in SENSITIVE_SUFFIXES:
        return True
    return name == ".env" or (name.startswith(".env.") and name not in ENV_EXAMPLES)


def audit(root: Path) -> list[tuple[str, str, int]]:
    findings: list[tuple[str, str, int]] = []
    for relative in tracked_files(root):
        path = root / relative
        if not path.is_file():
            continue
        if sensitive_filename(relative):
            findings.append(("sensitive-filename", relative, 0))
        data = path.read_bytes()
        if b"\0" in data:
            continue
        body = data.decode("utf-8", errors="replace")
        for line_number, line in enumerate(body.splitlines(), start=1):
            for rule_name, pattern in TEXT_RULES:
                if pattern.search(line):
                    findings.append((rule_name, relative, line_number))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Git 仓库根目录")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    try:
        findings = audit(root)
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: privacy audit could not run: {exc}", file=sys.stderr)
        return 2

    if findings:
        for rule_name, relative, line_number in findings:
            location = f"{relative}:{line_number}" if line_number else relative
            print(f"ERROR: {rule_name}: {location}", file=sys.stderr)
        print(f"repository privacy audit: FAIL ({len(findings)} finding(s))", file=sys.stderr)
        return 1

    print("repository privacy audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
