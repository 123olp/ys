# Repository Guidelines

## Project Structure & Module Organization
- `docs/` — source-of-truth documents (e.g., `docs/实践指南.md`, `docs/implementation_roadmap.md`).
- `archives/original_docs/` — raw/source materials; do not edit retroactively.
- `data/{evidence,refs}/` — datasets and references that back claims.
- `prototypes/` — experimental code or analyses (scaffolded directories exist).
- `audit/`, `governance/`, `kpi/`, `reviews/`, `lesson/` — formal reviews, policies, metrics, peer reviews, and post‑mortems (e.g., `lesson/文档体系重构_20251017_1105.md`).
- `figs/`, `style/` — images and style assets.
- `.github/` — issue/PR templates; `Makefile` — doc build tasks.

## Build, Test, and Development Commands
- `make` or `make all` — build the default report from `docs/系统化审阅报告_2025-10-17.md` to `out/report.{html,pdf}` (requires `pandoc`).
- `make clean` — remove build artifacts in `out/`.
- Verify `pandoc` availability: `pandoc -v`.
- Open the result locally: `out/report.html`.

## Coding Style & Naming Conventions
- Markdown: ATX headings (`#`), one H1 per file, Title Case for H1/H2.
- Lists and code blocks: use fenced blocks with language hints.
- File names: keep existing names; for new dated docs prefer `topic_YYYY-MM-DD.md` or `主题_YYYYMMDD.md`.
- YAML/JSON: 2‑space indentation. Makefile recipes must use tabs.

## Testing Guidelines
- A change is “green” when `make` succeeds and outputs both HTML/PDF.
- For substantial docs, manually check headings, tables, links, and images render.
- If adding datasets, include a short README in the same folder describing schema and source.

## Commit & Pull Request Guidelines
- Commit messages: imperative mood, concise subject (≤72 chars), body with why/what/impact.
- Group related changes; avoid mixed doc/data/logical changes in one commit.
- Use `.github/pull_request_template.md`; link issues (e.g., `Fixes #123`).
- Include before/after screenshots for visual changes; update `CHANGELOG.md` for user‑visible updates.

## Security & Agent Notes
- Do not commit secrets or private data. Redact PII in `archives/`.
- Agents and contributors: keep patches minimal, avoid renames that break links, prefer adding over rewriting. When uncertain, open an Issue before large moves.
