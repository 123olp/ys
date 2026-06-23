# Document Lifecycle

Human Infra documents should move from raw input to stable knowledge through explicit stages.

## Stages

1. `source`: raw or lightly processed material.
2. `draft`: authored but not yet stable.
3. `stable`: accepted as project guidance or reference.
4. `superseded`: replaced by a newer document or decision.
5. `archived`: retained only for traceability.

## Promotion Rules

A document can become stable when:

- its location matches the information architecture;
- its claim boundaries are clear;
- safety-sensitive claims preserve uncertainty;
- related README or AGENTS files are updated;
- local repository checks pass.

## Review Triggers

Review a document when:

- a domain boundary changes;
- a safety rule changes;
- a data source changes API, license, or availability;
- a source note contradicts a stable statement;
- a reader cannot tell whether a document is raw input or stable guidance.

## Deletion Rules

Prefer deletion or archiving over keeping stale active documents.

Do not delete:

- source notes needed for traceability;
- decision records;
- data provenance records;
- safety boundary history.
