# Fresh Reviewer Result Schema

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`

This schema defines the shape of each completed external reviewer result file under `fresh-reviewer-context-packets/results/CTX*.json`. It is a return contract for reviewers and a field-level guide for humans. The assembler remains the authoritative gate for accepting completed results.

## Required Files

Each reviewed context must produce exactly one result file:

```text
fresh-reviewer-context-packets/results/CTX*.json
```

Do not write `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json` by hand. Run `npm run assemble:fresh-reviewer-results` after all per-context files are present.

## Required Verdict Fields

| Field | Allowed values |
| --- | --- |
| reference_existence | PASS, FAIL, UNCERTAIN |
| safe_use_support | SUPPORTS, WEAK, WRONG |
| forbidden_use_violation | NONE, POSSIBLE, PRESENT |
| required_action | KEEP, SOFTEN, REWRITE, REMOVE, REPLACE_SOURCE |
| resolution_status | RESOLVED, ACCEPTED_WITH_BOUNDARY, PENDING_FIX, UNRESOLVED |

## Required Trace Fields

| Field | Requirement |
| --- | --- |
| reviewer_identity_class | Non-empty reviewer class or role |
| reviewed_at | ISO date-time |
| source_urls | At least one reopened source URL or retrieval note |
| reviewer_reason | Non-empty reason for the verdict |
| manuscript_change_required | Boolean or explicit text |
| manuscript_change_summary | Non-empty summary |
| reviewer_trace_path | Path or note for the review trace |

## JSON Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://human-infra.local/schemas/fresh-reviewer-context-result.schema.json",
  "title": "Fresh reviewer citation-context result",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "context_id",
    "priority",
    "risk_tier",
    "source_group",
    "claims",
    "references",
    "source_protocol_hash",
    "reviewer_identity_class",
    "reviewed_at",
    "source_urls",
    "reference_existence",
    "safe_use_support",
    "forbidden_use_violation",
    "required_action",
    "resolution_status",
    "reviewer_reason",
    "manuscript_change_required",
    "manuscript_change_summary",
    "reviewer_trace_path"
  ],
  "properties": {
    "context_id": {
      "type": "string",
      "enum": [
        "CTX2",
        "CTX3",
        "CTX5",
        "CTX7",
        "CTX10",
        "CTX11",
        "CTX12",
        "CTX9",
        "CTX1",
        "CTX4",
        "CTX6",
        "CTX8"
      ]
    },
    "priority": {
      "type": "integer",
      "minimum": 1,
      "maximum": 12
    },
    "risk_tier": {
      "type": "string",
      "enum": [
        "HIGH",
        "MEDIUM",
        "LOW"
      ]
    },
    "source_group": {
      "type": "string",
      "minLength": 1
    },
    "claims": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "string",
        "pattern": "^CL\\d+$"
      }
    },
    "references": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "string",
        "minLength": 1
      }
    },
    "source_protocol_hash": {
      "type": "string",
      "const": "sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de"
    },
    "reviewer_identity_class": {
      "type": "string",
      "minLength": 1,
      "description": "Reviewer class or role, for example independent-human-reviewer or fresh-ai-reviewer-with-web."
    },
    "reviewed_at": {
      "type": "string",
      "format": "date-time"
    },
    "source_urls": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "string",
        "minLength": 1
      },
      "description": "Reviewer-opened source URLs, DOI pages, official pages, PDF links, or explicit retrieval notes."
    },
    "reference_existence": {
      "type": "string",
      "enum": [
        "PASS",
        "FAIL",
        "UNCERTAIN"
      ]
    },
    "safe_use_support": {
      "type": "string",
      "enum": [
        "SUPPORTS",
        "WEAK",
        "WRONG"
      ]
    },
    "forbidden_use_violation": {
      "type": "string",
      "enum": [
        "NONE",
        "POSSIBLE",
        "PRESENT"
      ]
    },
    "required_action": {
      "type": "string",
      "enum": [
        "KEEP",
        "SOFTEN",
        "REWRITE",
        "REMOVE",
        "REPLACE_SOURCE"
      ]
    },
    "resolution_status": {
      "type": "string",
      "enum": [
        "RESOLVED",
        "ACCEPTED_WITH_BOUNDARY",
        "PENDING_FIX",
        "UNRESOLVED"
      ]
    },
    "reviewer_reason": {
      "type": "string",
      "minLength": 1
    },
    "manuscript_change_required": {
      "type": [
        "boolean",
        "string"
      ]
    },
    "manuscript_change_summary": {
      "type": "string",
      "minLength": 1
    },
    "reviewer_trace_path": {
      "type": "string",
      "minLength": 1,
      "description": "Path or note pointing to the reviewer trace, transcript, source notes, or review worksheet."
    }
  }
}
```
