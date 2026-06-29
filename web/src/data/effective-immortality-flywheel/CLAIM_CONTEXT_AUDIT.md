# Claim Context Alignment Audit

Date: 2026-06-29T00:00:00.000Z
Input: `web/src/data/effective-immortality-evidence.json`
Output JSON: `web/src/data/effective-immortality-flywheel/CLAIM_CONTEXT_AUDIT.json`

## Summary

Verdict: `PASS`

Reason: `all_claim_contexts_aligned`

All core claims have bounded claim evidence rows; all citation contexts state support and non-support boundaries; all contexts are backed by Reference Registry entries; no reference verification FAIL rows are present.

| Metric | Count |
| --- | ---: |
| Claims | 7 |
| Claim evidence rows | 7 |
| Citation contexts | 12 |
| Reference registry entries | 53 |
| Reference verification FAIL rows | 0 |
| Gaps | 0 |

## Claim Alignment

| Claim | Alignment verdict | Contexts | References through contexts | Boundary status | Status |
| --- | --- | ---: | ---: | --- | --- |
| CL1 | FRAMEWORK_ONLY | 6 | 19 | scoped | PASS |
| CL2 | OPERATIONAL_INTERFACE | 8 | 26 | scoped | PASS |
| CL3 | METHOD_SUPPORTED | 2 | 13 | scoped | PASS |
| CL4 | BOUNDED_EMPIRICAL | 2 | 9 | explicit | PASS |
| CL5 | NORMATIVE_MEASUREMENT | 2 | 5 | scoped | PASS |
| CL6 | GOVERNANCE_REQUIRED | 4 | 24 | scoped | PASS |
| CL7 | HARD_BOUNDARY | 5 | 25 | explicit | PASS |

## Context Coverage

| Context | Citation status | References | Boundary text | Status |
| --- | --- | ---: | --- | --- |
| CTX1 | KEEP | 2 | yes | PASS |
| CTX2 | KEEP WITH BOUNDARY | 3 | yes | PASS |
| CTX3 | KEEP WITH BOUNDARY | 3 | yes | PASS |
| CTX4 | KEEP WITH BOUNDARY | 4 | yes | PASS |
| CTX5 | KEEP WITH BOUNDARY | 3 | yes | PASS |
| CTX6 | KEEP WITH BOUNDARY | 3 | yes | PASS |
| CTX7 | KEEP WITH BOUNDARY | 4 | yes | PASS |
| CTX8 | KEEP | 6 | yes | PASS |
| CTX9 | KEEP | 11 | yes | PASS |
| CTX10 | KEEP WITH BOUNDARY | 4 | yes | PASS |
| CTX11 | KEEP WITH BOUNDARY | 4 | yes | PASS |
| CTX12 | KEEP WITH BOUNDARY | 2 | yes | PASS |

## Gaps

| Severity | Code | Subject | Message |
| --- | --- | --- | --- |
| - | - | - | None |

## Scope

This audit checks local claim-context-reference structure: every core claim must have a claim evidence map row, every cited context must exist, every context must state both support and non-support boundaries, and every context used by a claim must be backed by at least one Reference Registry entry. It also consumes REFERENCE_VERIFICATION.json when present and fails if any reference has live_status=FAIL. It does not replace fresh reviewer sentence-level citation-context judgment.
