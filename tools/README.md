# Tools

`tools/` contains repository maintenance scripts. These scripts support the knowledge base itself; they are not product code.

## Current Tools

- `arxiv_html_paper_tool.py`: installs, verifies, and scaffolds the reusable arXiv HTML papers reader framework for Astro projects.
- `check_repository.py`: verifies required files, required directories, temporary filename cleanup, Python cache cleanup, and local Markdown links.

Reusable tool package:

- `arxiv-html-paper/`: templates and usage notes for the arXiv HTML papers reuse kit.

## Commands

From the repository root:

```bash
python3 tools/check_repository.py
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public
make check
make clean
```
