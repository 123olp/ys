# Governance

Human Infra uses a lightweight maintainer-led governance model until the project has multiple active maintainers.

## Decision Sources

Decisions should follow this priority order:

1. Safety, legality, privacy, and human dignity.
2. Source traceability and evidence quality.
3. Project domain boundaries in `docs/reference/domain-map.md`.
4. Documentation architecture and repository standards.
5. Local implementation convenience.

## Decision Records

Durable architecture or domain decisions belong in `docs/decisions/`.

Use a decision record when a change:

- creates, removes, or redefines a top-level domain;
- changes safety or ethical boundaries;
- changes repository structure;
- introduces a new tooling or data pipeline ownership model;
- changes how evidence is interpreted or presented.

## Maintainer Responsibilities

- Keep root files current.
- Keep `AGENTS.md` files synchronized with architecture changes.
- Keep source notes separate from stable documentation.
- Keep generated data clearly separated from authored knowledge.
- Reject contributions that erase uncertainty or violate safety boundaries.

## Review Standard

A change is ready when:

- its file location matches the domain map;
- source claims are traceable;
- safety boundaries are explicit;
- root and directory `AGENTS.md` files remain accurate;
- `python3 tools/check_repository.py` passes.
