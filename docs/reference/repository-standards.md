# Repository Standards

Human Infra is a knowledge-first repository with a lightweight data tooling domain. Its standard structure combines:

- docs-as-code workflow;
- Diataxis information architecture;
- GitHub community health files;
- research repository citation and licensing placeholders;
- local validation for structure drift.

## Standard Root Files

Required for this repository:

- `README.md`: project overview and navigation.
- `AGENTS.md`: agent-facing architecture and maintenance rules.
- `LICENSE.md`: current rights boundary and future license decision note.
- `CONTRIBUTING.md`: contribution workflow.
- `CODE_OF_CONDUCT.md`: collaboration behavior boundary.
- `SECURITY.md`: safety and vulnerability reporting.
- `SUPPORT.md`: support boundary and help entry points.
- `GOVERNANCE.md`: decision ownership and review rules.
- `CHANGELOG.md`: notable structure changes.
- `CITATION.cff`: citation metadata placeholder for research reuse.
- `.gitignore`: generated artifacts, local caches, and private files.
- `.editorconfig`: baseline editor formatting rules.
- `.gitattributes`: text normalization and binary artifact hints.
- `Makefile`: local check and cleanup commands.

## Standard Directories

```text
.
├── .github/
├── docs/
│   ├── decisions/
│   ├── explanations/
│   ├── how-to/
│   ├── reference/
│   ├── source-notes/
│   ├── templates/
│   └── tutorials/
├── domains/
├── Makefile
├── .editorconfig
├── .gitattributes
└── tools/
```

## GitHub Community Health Files

The repository keeps issue templates, PR template, and root collaboration files so future public collaboration has a predictable entry point.

Files that need real maintainer contacts before public launch:

- `SECURITY.md`
- `CODE_OF_CONDUCT.md`
- `SUPPORT.md`

## Data Boundary

Generated or downloaded data belongs under:

```text
domains/*/data/raw/
domains/*/data/processed/
```

These directories are ignored by default. Curated sample data must be explicitly documented before committing.

## Sources Used

- Diataxis: https://diataxis.fr/
- GitHub Community Profiles: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions
- GitHub About READMEs: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- GitHub Issue and PR Templates: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests
- The Good Docs Project: https://www.thegooddocsproject.dev/
