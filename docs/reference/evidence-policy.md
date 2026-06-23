# Evidence Policy

Human Infra documents must distinguish evidence, interpretation, speculation, and product intent.

## Evidence Classes

- `source`: raw external or internal material, such as public database records, papers, notes, or standards.
- `extracted fact`: a fact copied or normalized from a source.
- `interpretation`: a human-authored explanation of what a fact means.
- `claim`: a statement that can be supported, weakened, or rejected by evidence.
- `speculation`: a plausible but unproven hypothesis.
- `decision`: a repository or domain choice recorded because the project needs a stable boundary.

## Required Boundaries

- Do not turn speculation into claims.
- Do not turn claims into recommendations without a defined evidence threshold.
- Do not collapse human evidence, animal evidence, mechanism evidence, and marketing language into one category.
- Do not use AI summaries as primary facts.
- Do not remove uncertainty to make a narrative smoother.

## Health And Neural Topics

Health, neural, memory, and identity-related content requires stricter wording:

- State the population or subject type.
- State whether evidence is human, animal, in vitro, computational, or conceptual.
- State known limitations.
- Keep safety warnings near the claim, not hidden in another document.

## Repository Practice

- Use `docs/source-notes/` for raw source intake.
- Distill stable rules into `docs/reference/`.
- Use domain documents for domain-specific evidence models.
- Use decision records when evidence changes a structural boundary.
