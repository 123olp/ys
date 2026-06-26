# Source Management

Source management keeps raw material separate from stable knowledge.

## Source Types

- `source note`: raw or lightly processed written material in `docs/source-notes/`.
- `external public data`: downloaded or API-collected data under `domains/*/data/raw/`.
- `processed data`: normalized script output under `domains/*/data/processed/`.
- `stable documentation`: authored documents under `docs/` or `domains/`.

## Intake Rules

- Rename temporary files before placing them in `docs/source-notes/`.
- Record source origin when known.
- Do not mix raw notes with stable reference documents.
- Do not commit large generated data unless explicitly curated as a small sample.
- Do not overwrite versioned external snapshots unless the source policy says they are disposable.

## Distillation Rules

Source notes become useful only after distillation:

1. Identify the domain affected.
2. Extract stable claims or terms.
3. Preserve uncertainty.
4. Move durable material into `docs/reference/`, `docs/explanations/`, or a domain directory.
5. Leave the original note available for traceability.

When a source is expected to support a model, Web page, literature map, or public claim, create a research card before updating stable documents. The card records the source identity, Human Infra mapping, model position, evidence role, transfer boundary, and repository action.

Use [Source Card System](source-card-system.md) and [Research Card Template](../templates/research-card.md).

## Generated Data Rules

- Raw data goes under `domains/*/data/raw/`.
- Processed data goes under `domains/*/data/processed/`.
- Both paths are ignored by default.
- Generated data must not be treated as authored knowledge until reviewed.
