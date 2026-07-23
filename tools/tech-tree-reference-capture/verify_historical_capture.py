#!/usr/bin/env python3
"""审计 Historical Tech Tree 图数据、镜像闭合和逐文件哈希。"""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlparse


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    return parser.parse_args()


def select_array(data: dict[str, object], names: tuple[str, ...]) -> list[dict[str, object]]:
    for name in names:
        value = data.get(name)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]
    return []


def local_image_path(raw: str) -> Path:
    parsed = urlparse(raw)
    return Path(unquote(parsed.path).lstrip("/"))


def mirror_path_for_url(raw: str) -> Path:
    parsed = urlparse(raw)
    known_routes = {
        "/": "index.html",
        "/about": "about/index.html",
        "/changelog": "changelog/index.html",
        "/image-credits": "image-credits/index.html",
        "/mini-tree": "mini-tree/index.html",
    }
    if parsed.path in known_routes:
        return Path(known_routes[parsed.path])
    relative = Path(unquote(parsed.path).lstrip("/"))
    if parsed.path.endswith("/"):
        relative /= "index.html"
    return relative


def main() -> int:
    args = parse_args()
    run_dir = args.run_dir.resolve()
    mirror = run_dir / "mirror"
    evidence = run_dir / "evidence"
    browser = run_dir / "browser"
    failures: list[str] = []

    api_path = mirror / "api/inventions"
    if not api_path.is_file():
        failures.append("缺少 mirror/api/inventions")
        data: dict[str, object] = {}
    else:
        try:
            parsed = json.loads(api_path.read_text(encoding="utf-8-sig"))
            data = parsed if isinstance(parsed, dict) else {}
        except (OSError, json.JSONDecodeError) as error:
            failures.append(f"API JSON 无法解析：{error}")
            data = {}

    nodes = select_array(data, ("nodes", "inventions", "technologies"))
    links = select_array(data, ("links", "connections", "edges"))
    node_ids = {str(node.get("id")) for node in nodes if node.get("id")}
    broken_links = [
        link
        for link in links
        if str(link.get("source")) not in node_ids or str(link.get("target")) not in node_ids
    ]
    if len(nodes) < 2400:
        failures.append(f"节点不足：期望至少 2400，实际 {len(nodes)}")
    if len(links) < 3700:
        failures.append(f"连接不足：期望至少 3700，实际 {len(links)}")
    if broken_links:
        failures.append(f"存在 {len(broken_links)} 条端点缺失的连接")

    declared_images = {
        local_image_path(str(node["localImage"]))
        for node in nodes
        if node.get("localImage")
    }
    missing_images = sorted(
        image.as_posix() for image in declared_images if not (mirror / image).is_file()
    )
    if missing_images:
        failures.append(f"缺少 {len(missing_images)} 张 API 声明的本地图片")

    discovery_path = browser / "discover-report.json"
    if not discovery_path.is_file():
        failures.append("缺少 browser/discover-report.json")
        discovered_resources: list[dict[str, object]] = []
    else:
        discovery = json.loads(discovery_path.read_text(encoding="utf-8"))
        discovered_resources = discovery.get("resources", [])
        if discovery.get("verdict") != "PASS":
            failures.append("在线 Chrome 发现门禁未通过")

    verify_path = browser / "offline/verify-report.json"
    if not verify_path.is_file():
        failures.append("缺少 browser/offline/verify-report.json")
    else:
        offline = json.loads(verify_path.read_text(encoding="utf-8"))
        if offline.get("verdict") != "PASS":
            failures.append("离线 Chrome 交互门禁未通过")
        if offline.get("remoteRuntimeRequests"):
            failures.append("离线运行仍请求远程资源")

    missing_discovered: list[str] = []
    for resource in discovered_resources:
        url = str(resource.get("url", ""))
        parsed = urlparse(url)
        if parsed.netloc != "www.historicaltechtree.com":
            continue
        relative = mirror_path_for_url(url)
        if not (mirror / relative).is_file():
            missing_discovered.append(url)
    if missing_discovered:
        failures.append(f"缺少 {len(missing_discovered)} 个 Chrome 发现的同源资源")

    file_rows: list[dict[str, object]] = []
    for root_name in ("raw", "mirror", "browser", "source-code"):
        root = run_dir / root_name
        if not root.is_dir():
            failures.append(f"缺少抓取目录：{root_name}")
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(run_dir).as_posix()
            file_rows.append(
                {
                    "path": relative,
                    "bytes": path.stat().st_size,
                    "sha256": sha256(path),
                    "content_type": mimetypes.guess_type(relative)[0]
                    or "application/octet-stream",
                    "retrieval_result": "present-and-hashed",
                }
            )

    evidence.mkdir(parents=True, exist_ok=True)
    manifest = {
        "schema_version": "1.0.0",
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "source": "https://www.historicaltechtree.com/",
        "usage_boundary": "local research reference only; no redistribution grant",
        "graph": {
            "nodes": len(nodes),
            "links": len(links),
            "top_level_keys": sorted(data),
            "broken_link_endpoints": len(broken_links),
        },
        "assets": {
            "declared_local_images": len(declared_images),
            "missing_local_images": len(missing_images),
            "browser_discovered_resources": len(discovered_resources),
            "missing_browser_resources": len(missing_discovered),
        },
        "files": file_rows,
        "counts": {
            "files": len(file_rows),
            "bytes": sum(int(row["bytes"]) for row in file_rows),
        },
    }
    (evidence / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (evidence / "SHA256SUMS").write_text(
        "".join(f'{row["sha256"]}  {row["path"]}\n' for row in file_rows),
        encoding="utf-8",
    )
    report = {
        "verdict": "PASS" if not failures else "BLOCK",
        "failures": failures,
        "graph": manifest["graph"],
        "assets": manifest["assets"],
        "counts": manifest["counts"],
        "missing_local_images_sample": missing_images[:20],
        "missing_browser_resources_sample": missing_discovered[:20],
    }
    (evidence / "verification-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
