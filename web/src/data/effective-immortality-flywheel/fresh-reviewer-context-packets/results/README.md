# Fresh Reviewer Per-Context Results

This directory is the only supported input location for external reviewer result files.

Expected file pattern: `CTX*.json`

Result schema: `../RESULT_SCHEMA.json`

Result schema hash: `sha256:2efec5cdc63f32e4cd9bdbd1d423ef71d2e95b83302cc48020fb5069e7fece9d`

Canonical output: `web/src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`

## Workflow

1. Read `../INDEX.md` and review each context packet in priority order.
2. Copy each packet's result stub into this directory as `CTX<id>.json`.
3. Fill the fields from a real fresh-reviewer source lookup. Use `../RESULT_SCHEMA.json` as the return contract. Do not use local author guesses.
4. Run `npm run assemble:fresh-reviewer-results`.
5. Keep the reviewed `CTX*.json` files in this directory; the canonical ledger stores their SHA-256 hashes.
6. Run `npm run audit:fresh-reviewer-results`.

The assembler writes the canonical results file only when every required context file exists and passes structural validation. The audit gate rejects a canonical ledger whose source `CTX*.json` files are missing or hash-mismatched.

## Current Status

| Metric | Count |
| --- | ---: |
| Required contexts | 12 |
| Per-context result files | 0 |
| Missing contexts | 12 |
| Structural findings | 0 |

## Missing Contexts

| Context | Status |
| --- | --- |
| CTX2 | missing |
| CTX3 | missing |
| CTX5 | missing |
| CTX7 | missing |
| CTX10 | missing |
| CTX11 | missing |
| CTX12 | missing |
| CTX9 | missing |
| CTX1 | missing |
| CTX4 | missing |
| CTX6 | missing |
| CTX8 | missing |

## Findings

| Severity | Context | Code | File | Message |
| --- | --- | --- | --- | --- |
| - | - | - | - | No structural findings |
