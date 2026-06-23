# How To Contribute Documentation

Use this guide when adding or changing Human Infra documentation.

## Steps

1. Decide the document type:
   - tutorial: learning path;
   - how-to: task procedure;
   - reference: stable lookup;
   - explanation: conceptual understanding;
   - source note: raw or lightly processed input.
2. Place the file in the matching directory.
3. Use a semantic filename.
4. Add the file to the local `README.md` or `AGENTS.md` if it changes navigation or architecture.
5. Preserve source traceability for factual claims.
6. Mark uncertainty instead of forcing a conclusion.
7. Run:

```bash
python3 tools/check_repository.py
```

## Placement Rules

- Cross-domain principles go under `docs/`.
- Domain-specific material goes under `domains/<domain>/`.
- Raw notes go under `docs/source-notes/`.
- Data source outputs stay under `domains/*/data/raw/` or `domains/*/data/processed/`.
