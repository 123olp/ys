# Changelog

## 1.0.1 - 2026-06-29

- Documented the reader DOM contract as an interaction interface, not only a CSS/semantic class list.
- Added TOC slot, `.ltx_page_navbar > nav.ltx_TOC`, `.ltx_abstract`, `.ltx_bibliography`, duplicate-class, and browser-click assertions to the contract, consumer guide, governance checklist, and maintenance runbook.
- Clarified that `verify-assets` proves CSS/JS/font availability only and does not prove arXiv reader controls are usable.

## 1.0.0 - 2026-06-28

- Formalized the arXiv HTML Paper Reuse Kit as a reusable package.
- Added the consumer contract, machine-readable JSON contract, consumer guide, governance document, maintenance runbook, and package version file.
- Clarified that the kit owns the arXiv-style reader framework while consumer projects own article content.
- Defined compatibility boundaries for CLI commands, required assets, template placeholders, DOM classes, reading-state attributes, and localStorage keys.
