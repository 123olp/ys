# 0001 Adopt Docs-As-Code Knowledge Base Structure

## Status

Accepted.

## Context

Human Infra is not a web app, service backend, or conventional Python package. It is a knowledge-first repository with one lightweight public-data collection domain.

The repository needs:

- clear root files for collaboration and safety;
- a documentation information architecture;
- domain boundaries that keep Longevity Evidence, Disembodied CNS, and Memory Editing separate;
- generated data separated from authored knowledge;
- a local validation script so structure drift is visible.

## Decision

Adopt a docs-as-code knowledge repository shape:

- root community and governance files;
- `docs/` organized by tutorials, how-to, reference, explanations, decisions, and source notes;
- `domains/` for bounded subject areas;
- `tools/` for repository maintenance checks;
- `.github/` for collaboration templates;
- generated data ignored under `**/data/raw/` and `**/data/processed/`.

## Consequences

- The repository is easier to navigate as a knowledge base.
- New domains require explicit boundary decisions.
- Documentation changes can be validated locally.
- This does not turn the project into an application repository.
