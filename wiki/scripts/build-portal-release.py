#!/usr/bin/env python3
"""从 Wikimedia 门户快照生成仅增强机器元数据的 Pages 发布物。"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "geo-publication.json"


def upsert_meta(
    soup: BeautifulSoup,
    *,
    name: str | None = None,
    prop: str | None = None,
    content: str,
) -> None:
    selector = f"meta[name='{name}']" if name else f"meta[property='{prop}']"
    node = soup.select_one(selector)
    if node is None:
        node = soup.new_tag("meta")
        soup.head.append(node)
    if name:
        node["name"] = name
    if prop:
        node["property"] = prop
    node["content"] = content


def build_portal(output_dir: Path) -> None:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    project = config["project"]
    portal = config["products"]["portal"]
    wiki = config["products"]["wiki"]
    tree = config["products"]["technologyTree"]
    publisher = config["publisher"]

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)
    shutil.copytree(ROOT / "portal" / "assets", output_dir / "assets")
    for filename in (
        "adapter.js",
        "languages.json",
        "LICENSE.wikimedia-portals",
        "UPSTREAM.md",
    ):
        shutil.copy2(ROOT / "portal" / filename, output_dir / filename)

    soup = BeautifulSoup(
        (ROOT / "portal" / "index.html").read_text(encoding="utf-8"),
        "lxml",
    )
    soup.html["lang"] = "mul"
    soup.title.string = portal["name"]
    search_form = soup.select_one("#search-form")
    search_input = soup.select_one("#searchInput")
    if search_form is None or search_input is None:
        raise RuntimeError("门户缺少上游搜索表单契约")
    search_form["action"] = f"{wiki['url']}search/"
    search_form["method"] = "get"
    search_input["name"] = "q"
    upsert_meta(soup, name="description", content=portal["description"])
    upsert_meta(soup, name="robots", content="index,follow,max-image-preview:large")
    upsert_meta(soup, prop="og:title", content=portal["name"])
    upsert_meta(soup, prop="og:description", content=portal["description"])
    upsert_meta(soup, prop="og:type", content="website")
    upsert_meta(soup, prop="og:url", content=portal["url"])
    upsert_meta(soup, prop="og:site_name", content=project["name"])
    upsert_meta(
        soup,
        prop="og:image",
        content=f"{portal['url']}assets/human-infra-mark.svg",
    )
    upsert_meta(soup, name="twitter:card", content="summary")
    upsert_meta(soup, name="twitter:title", content=portal["name"])
    upsert_meta(soup, name="twitter:description", content=portal["description"])

    canonical = soup.select_one("link[rel='canonical']")
    if canonical is None:
        canonical = soup.new_tag("link", rel="canonical")
        soup.head.append(canonical)
    canonical["href"] = portal["url"]

    for old in soup.select("script[type='application/ld+json']"):
        old.decompose()
    structured_data = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"{portal['url']}#website",
        "name": portal["name"],
        "alternateName": project["alternateName"],
        "url": portal["url"],
        "description": portal["description"],
        "inLanguage": ["zh", "en"],
        "publisher": {
            "@type": "Organization",
            "name": publisher["name"],
            "url": publisher["url"],
        },
        "sameAs": [
            project["repository"],
            project["community"],
            wiki["url"],
            tree["url"],
        ],
    }
    script = soup.new_tag("script", type="application/ld+json")
    script.string = json.dumps(
        structured_data,
        ensure_ascii=False,
        separators=(",", ":"),
    ).replace("<", "\\u003c")
    soup.head.append(script)

    html = str(soup)
    output_dir.joinpath("index.html").write_text(html, encoding="utf-8")
    not_found = BeautifulSoup(html, "lxml")
    not_found.select_one("meta[name='robots']")["content"] = "noindex,follow"
    output_dir.joinpath("404.html").write_text(str(not_found), encoding="utf-8")
    output_dir.joinpath("robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        f"Sitemap: {portal['url']}sitemap.xml\n",
        encoding="utf-8",
    )
    output_dir.joinpath("sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"  <url><loc>{portal['url']}</loc></url>\n"
        "</urlset>\n",
        encoding="utf-8",
    )
    output_dir.joinpath("llms.txt").write_text(
        f"# {project['name']}\n\n"
        f"> {project['description']}\n\n"
        "## Primary products\n\n"
        f"- [Language portal]({portal['url']}): {portal['description']}\n"
        f"- [Research Wiki]({wiki['url']}): {wiki['description']}\n"
        f"- [Technology tree]({tree['url']}): {tree['description']}\n"
        f"- [Source repository]({project['repository']}): "
        "research domains, evidence registers and governance contracts\n\n"
        "## Use boundary\n\n"
        "Human Infra is a research knowledge infrastructure. Domain registration "
        "does not prove intervention efficacy, and its content is not individual "
        "medical, legal or lifespan advice.\n",
        encoding="utf-8",
    )
    output_dir.joinpath("entity.jsonld").write_text(
        json.dumps(structured_data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build_portal(args.output.resolve())


if __name__ == "__main__":
    main()
