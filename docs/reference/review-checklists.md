# Review Checklists

Use these checklists when reviewing changes to this repository.

## Documentation Review

- File is in the correct Diataxis location.
- Filename is semantic and stable.
- The document has one primary job.
- Navigation files are updated.
- Local Markdown links pass `make check`.
- The document does not duplicate a nearby document without adding a clear role.

## Evidence Review

- Claims are separated from evidence and speculation.
- Source traceability is preserved.
- Health, neural, memory, or identity claims state uncertainty.
- Mechanism evidence is not presented as clinical proof.
- AI summaries are not used as primary facts.

## Safety Review

- No medical diagnosis or personal treatment instruction is added.
- No invasive neural, memory manipulation, or human experimentation procedure is added.
- No executable black-hole approach, extreme orbital, or human space survival procedure is added.
- No organizational monitoring or coercive control pattern is normalized.
- Consent, exit, dignity, and audit boundaries are preserved for high-risk topics.

## Domain Boundary Review

- The change belongs in the selected domain.
- Cross-domain rules stay under `docs/`.
- Domain-specific material stays under `domains/<domain>/`.
- New domains update `docs/reference/domain-map.md`.
- `AGENTS.md` files reflect architecture changes.
- Speculative physics paths are kept separate from biomedical evidence and neural intervention domains.

## Data Pipeline Review

- Script output stays under `domains/*/data/raw/` or `domains/*/data/processed/`.
- Generated data is not treated as authored knowledge.
- Network scripts have timeouts and bounded retries.
- Source IDs, retrieval time, URL, and raw hash are preserved where practical.
- Data refresh does not silently overwrite curated conclusions.
