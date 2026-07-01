# 0106. Establish Transcendental Domain Index

Date: 2026-07-01

## Status

Accepted.

## Context

Human Infra has already created the main A-K effective-immortality domains: cellular reprogramming, regenerative medicine, cancer control, immune maintenance, brain preservation, memory editing, cognitive augmentation, future waiting, disembodied CNS, biostasis, and resource/social infrastructure.

The current problem is not missing directories. The risk is conceptual duplication: adding new directories for every phrase in the transcendental chain would create synonym domains and weaken navigation.

The user asked to establish the directories, documents, and indexes for this first-principles search space. The correct structure is therefore an index layer that proves the directories already exist, explains their first-principles relation, and defines when a future candidate deserves a new `domains/` directory.

## Decision

Create `docs/reference/transcendental-domain-index.md` as the compressed first-principles index for effective immortality research domains.

The document maps:

- ultimate target;
- possibility conditions;
- existing domain directories;
- domain boundary rules;
- current gap records;
- minimum reading path.

It links to `research-domain-atlas.md` instead of replacing it. The atlas remains the full map and domain-generation contract; the new index is the short navigation layer for the first-principles chain.

## Consequences

- The A-K trunk now has one stable entry point.
- New domain proposals must first pass through the existing atlas and the new transcendental index.
- The repository avoids duplicate directories for concepts already covered by existing domains.
- Future work should enrich existing domain README files and Source Cards before creating new directories.

## Non-goals

- Do not create duplicate domains for already covered objects such as Yamanaka factors, biostasis, future waiting, memory editing, or cognitive augmentation.
- Do not turn the index into a fact source for biomedical, physical, or engineering claims.
- Do not treat the index as a substitute for evidence review, safety boundaries, or domain README maintenance.
