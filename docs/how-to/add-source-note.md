# How To Add A Source Note

Source notes preserve raw or lightly processed inputs without pretending they are stable knowledge.

## Steps

1. Rename the file to a semantic filename.
2. Place it under `docs/source-notes/`.
3. If creating a new note, start from `docs/templates/source-note.md`.
4. Record source origin, access date, owner, URL or local path when known.
5. Add a short entry to `docs/source-notes/README.md`.
6. Identify the distillation target:
   - `docs/reference/`
   - `docs/explanations/`
   - `domains/<domain>/`
7. Run:

```bash
make check
```

## Rules

- Do not use temporary editor filenames.
- Do not turn source notes into product claims directly.
- Preserve uncertainty.
- Keep source notes separate from stable reference documents.
