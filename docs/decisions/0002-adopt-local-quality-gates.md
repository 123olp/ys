# 0002 Adopt Local Quality Gates

## Status

Accepted.

## Context

Human Infra is a knowledge-first repository. Its main failure modes are structural drift, broken links, stale navigation, generated-data confusion, and lightweight script breakage.

The project does not yet need a full CI stack, package manager, database, or web framework.

## Decision

Use a small local quality gate:

- `tools/check_repository.py` for required files, required directories, temporary filenames, cache directories, and local Markdown links.
- `Makefile` for repeatable `make check`, `make structure`, `make py-compile`, and `make clean`.
- Python compilation checks for the maintenance script and Longevity Evidence data scripts.

## Alternatives Considered

- Full documentation site generator: rejected for now because there is no publishing target yet.
- Markdown lint dependency: deferred until style problems become measurable.
- CI workflow: deferred until this becomes a GitHub repository with remote checks.

## Consequences

- Contributors have a single local command.
- The repository avoids framework and dependency ownership.
- Link and structure drift becomes visible early.
- The gate is intentionally limited and can be expanded later.

## Safety And Evidence Boundary

Quality gates check repository structure; they do not verify scientific correctness, medical claims, or ethical adequacy. Human review remains required for evidence and safety.
