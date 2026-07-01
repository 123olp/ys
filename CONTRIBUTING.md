# Contributing

Human Infra is a knowledge-first repository. Contributions should improve the clarity, traceability, safety, or maintainability of the project.

## Contribution Types

- Fix documentation errors, broken links, stale paths, or ambiguous wording.
- Improve domain models, terminology, evidence boundaries, and ethical constraints.
- Add or update public data source documentation.
- Improve lightweight scripts that collect, normalize, or validate public evidence.
- Add source notes only when they can be traced and later distilled into stable documents.

## Repository Shape

- Use `docs/` for cross-domain documentation.
- Use `domains/` for domain-specific materials.
- Use `docs/source-notes/` for raw or lightly processed inputs.
- Use `tools/` for repository maintenance checks.
- Keep generated data in `domains/*/data/raw/` or `domains/*/data/processed/`.

## Documentation Rules

- Prefer concise, stable names over temporary working names.
- Put explanatory essays in `docs/explanations/`.
- Put factual maps, rules, glossaries, and standards in `docs/reference/`.
- Put task-oriented procedures in `docs/how-to/`.
- Put learning paths in `docs/tutorials/`.
- Put durable architecture decisions in `docs/decisions/`.
- Use `docs/templates/` when creating a repeated document type.
- Every public claim about health, safety, data, or neural systems must preserve uncertainty and source traceability.

## Safety Rules

- Do not add medical advice, personal treatment recommendations, or dosage instructions.
- Do not add executable procedures for invasive neural work, memory manipulation, or human experimentation.
- Do not turn Human Infra into a monitoring or control framework for extracting more work from people.
- When unsure, link to source material and mark the conclusion as unsettled.

## Local Checks

Run the repository structure check before handing off:

```bash
make check
```

For the current data scripts:

```bash
python3 -m py_compile domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_mvp_data.py domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_core_data.py
```
