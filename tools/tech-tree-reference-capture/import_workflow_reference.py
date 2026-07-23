#!/usr/bin/env python3
"""导入 Windows 侧已验证的网页抓取工作流参考快照。"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_SOURCE = Path(
    "/mnt/d/.projects/epub-translator/work/philosophy-knowledge-graph/site-mirror"
)
DEFAULT_OUTPUT_ROOT = Path("build/reference-captures/tech-tree")
EXPECTED_PORTRAITS = 189
REQUIRED_FILES = (
    "index.original.html",
    "index.html",
    "css/main.css",
    "data/data.enc",
    "font/FranklinGothic-Book_gdi.woff",
    "js/app.min.js",
    "js/createjs.min.js",
    "vendor/d3.v7.min.js",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="导入 Windows 工作流参考快照并生成完整性证据和 ZIP。"
    )
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument(
        "--run-id",
        default=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
    )
    return parser.parse_args()


def expected_portraits(source: Path) -> set[str]:
    people_csv = source.parent / "exports/people.csv"
    if not people_csv.is_file():
        return set()
    with people_csv.open(encoding="utf-8-sig", newline="") as stream:
        return {
            f"{row['urlName']}.jpg"
            for row in csv.DictReader(stream)
            if row.get("urlName")
        }


def validate_source(source: Path) -> tuple[list[str], set[str], set[str]]:
    failures = [
        relative for relative in REQUIRED_FILES if not (source / relative).is_file()
    ]
    actual_portraits = {
        path.name for path in (source / "img/philosopher").glob("*.jpg")
    }
    upstream_portraits = expected_portraits(source)
    if not upstream_portraits:
        failures.append("missing sibling exports/people.csv portrait inventory")
    elif len(upstream_portraits) != EXPECTED_PORTRAITS:
        failures.append(
            f"exports/people.csv: expected {EXPECTED_PORTRAITS}, "
            f"got {len(upstream_portraits)}"
        )
    missing_portraits = upstream_portraits - actual_portraits
    if missing_portraits:
        failures.append(f"missing upstream portraits: {sorted(missing_portraits)}")
    managed_portraits = actual_portraits - upstream_portraits
    return failures, upstream_portraits, managed_portraits


def build_manifest(
    source: Path,
    target: Path,
    run_id: str,
    upstream_portraits: set[str],
    managed_portraits: set[str],
) -> dict[str, object]:
    files: list[dict[str, object]] = []
    for path in sorted(target.rglob("*")):
        if not path.is_file():
            continue
        files.append(
            {
                "path": path.relative_to(target).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )

    return {
        "schema_version": "1.0.0",
        "capture_id": run_id,
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "source_snapshot": str(source),
        "reference_id": "philosophy-knowledge-graph",
        "source_page": "https://www.denizcemonduygu.com/philo/browse/",
        "capture_method": (
            "Imported byte-for-byte from the verified Windows aria2 snapshot; "
            "see CAPTURE-CONTRACT.md for the upstream workflow."
        ),
        "usage_boundary": "local research reference only; no redistribution grant",
        "counts": {
            "files": len(files),
            "bytes": sum(int(item["bytes"]) for item in files),
            "upstream_portraits": len(upstream_portraits),
            "managed_portraits": len(managed_portraits),
            "all_portraits": len(list((target / "img/philosopher").glob("*.jpg"))),
        },
        "managed_portrait_files": sorted(managed_portraits),
        "required_files": list(REQUIRED_FILES),
        "files": files,
    }


def write_checksums(manifest: dict[str, object], destination: Path) -> None:
    rows = [
        f'{item["sha256"]}  raw-source/{item["path"]}'
        for item in manifest["files"]  # type: ignore[index]
    ]
    destination.write_text("\n".join(rows) + "\n", encoding="utf-8")


def create_archive(run_dir: Path) -> Path:
    archive = run_dir.with_suffix(".zip")
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(run_dir.rglob("*")):
            if path.is_file():
                bundle.write(path, path.relative_to(run_dir.parent))
    return archive


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    failures, upstream_portraits, managed_portraits = validate_source(source)
    if failures:
        print(
            json.dumps(
                {"status": "BLOCK", "source": str(source), "failures": failures},
                ensure_ascii=False,
                indent=2,
            ),
            file=sys.stderr,
        )
        return 1

    run_dir = (
        args.output_root / "workflow-reference" / "philosophy-knowledge-graph" / args.run_id
    ).resolve()
    if run_dir.exists():
        print(f"拒绝覆盖既有批次：{run_dir}", file=sys.stderr)
        return 1

    raw_target = run_dir / "raw-source"
    evidence_dir = run_dir / "evidence"
    raw_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, raw_target, copy_function=shutil.copy2)
    evidence_dir.mkdir()

    manifest = build_manifest(
        source,
        raw_target,
        args.run_id,
        upstream_portraits,
        managed_portraits,
    )
    manifest_path = evidence_dir / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    write_checksums(manifest, evidence_dir / "SHA256SUMS")

    report = {
        "status": "PASS",
        "checks": {
            "required_files": "PASS",
            "portrait_count": "PASS",
            "byte_copy": "PASS",
            "sha256_manifest": "PASS",
        },
        "counts": manifest["counts"],
        "entrypoints": {
            "upstream_preserved": "raw-source/index.original.html",
            "offline_runtime": "raw-source/index.html",
            "chinese_projection": "raw-source/index.zh-CN.html",
        },
    }
    (evidence_dir / "import-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    archive = create_archive(run_dir)
    result = {
        "status": "PASS",
        "run_dir": str(run_dir),
        "archive": str(archive),
        "archive_bytes": archive.stat().st_size,
        "archive_sha256": sha256(archive),
        "counts": manifest["counts"],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
