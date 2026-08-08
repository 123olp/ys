# Security Policy

This repository is primarily documentation and lightweight public-data tooling, but it still contains safety-sensitive material.

## Scope

Security and safety reports are relevant when they involve:

- scripts that mishandle network input, files, paths, or generated data;
- data provenance mistakes that could mislead health or safety interpretation;
- documentation that enables unsafe medical, neural, memory, or human experimentation behavior;
- privacy leaks, credentials, private notes, or unintended personal data;
- instructions that could be used for coercive monitoring or manipulation.

## Out of Scope

- General disagreement with a domain model or theory.
- Requests for medical advice.
- Requests for invasive neural, memory editing, or human experimentation steps.

## Reporting

Do not publish sensitive exploit details, private data, or unsafe procedural steps in a public issue.

Use GitHub private vulnerability reporting. Do not include secrets, personal data, local paths, or exploit details in a public issue, pull request, discussion, or commit message.

## Handling Rules

- Preserve evidence.
- Minimize exposure.
- Remove secrets or private data immediately after confirming scope.
- Document the root cause and prevention rule in the appropriate `docs/` or `domains/*/AGENTS.md` file when it has long-term value.
- Run `make privacy-audit` before committing public changes. CI uses redacted location identifiers and never echoes matched values.
- Run `make public-product-boundary` before merging changes that touch Wiki, timeline, technology-tree, deployment, or publication assets.
