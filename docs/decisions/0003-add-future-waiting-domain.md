# 0003 Add Future Waiting Domain

## Status

Accepted.

## Context

Human Infra already separates longevity evidence, disembodied central nervous system work, and memory editing. The “black hole waiting room” idea does not fit any of those domains:

- it is not a health intervention with clinical evidence;
- it is not primarily about replacing the body with an external CNS support architecture;
- it is not about editing memory or identity content.

Its real object is “using physics or biological state changes to reduce the subjective cost of waiting for the future.”

## Decision

Create `domains/future-waiting/` for future-waiting paths.

The first path is:

- `domains/future-waiting/paths/black-hole-waiting-room.md`

## Alternatives Considered

- Add it to `longevity-evidence/`: rejected because it would pollute evidence-based health intervention work with speculative spacetime waiting.
- Add it to `disembodied-cns/`: rejected because life support may be a dependency but is not the core mechanism.
- Add it as a single `docs/reference/` page: rejected because the user asked for an immortality path, and future-waiting is likely to grow as a path taxonomy.

## Consequences

- Future-waiting paths get their own safety and evidence boundary.
- Longevity Evidence stays focused on biomedical and public evidence.
- Speculative physics paths must clearly distinguish physical theory, thought experiment, and engineering feasibility.

## Safety And Evidence Boundary

This domain must not provide executable space mission design, black-hole approach procedures, human experimentation protocols, or claims that time dilation is a practical immortality technology.
