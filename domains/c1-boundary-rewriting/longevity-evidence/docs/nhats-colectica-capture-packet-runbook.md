# NHATS Colectica Capture Packet Runbook

This runbook turns the existing NHATS Colectica machine contracts into a human-executable first capture workflow. It exists to move `MODEL-G4-field-and-value-confirmation` from "contracted but not executable" toward governed field and value confirmation.

It does not authorize NHATS download, raw metadata storage, row-level extraction, route-classifier promotion, aggregate cohort flow, calibration, public export, medical advice, or individual prediction.

## Authoritative Inputs

Use these files as the only local source of truth before producing any packet:

| Artifact | Role |
| --- | --- |
| `../data/manual/life_path_nhats_colectica_access_route_probe_register.json` | Identifies the official access route and the controlled capture boundary. |
| `../data/manual/life_path_nhats_colectica_authenticated_capture_template.json` | Defines the redacted capture evidence slots that a variable page packet must satisfy. |
| `../data/manual/life_path_nhats_colectica_capture_task_register.json` | Lists the 9 route-field groups and 39 pending capture tasks. |
| `../data/manual/life_path_nhats_colectica_capture_packet_validator_test_cases.json` | Defines the synthetic validator behavior and packet schema. |
| `../data/manual/life_path_nhats_colectica_capture_packet_review_execution_register.json` | Records future packet review state; currently 0 packets, 0 second reviews, and 0 closed slots. |
| `../data/manual/life_path_nhats_route_value_crosswalk_assembly_protocol.json` | Defines when reviewed packets may later become route-value and missing-code crosswalk rows. |
| `../data/manual/life_path_nhats_route_classifier_readiness.json` | Keeps route classifier, extraction, aggregation, public output, calibration, and individual prediction blocked. |
| `../../../../docs/reference/human-infra-l4-evidence-packet-review-playbook.md` | Cross-project L4 evidence review posture. |

## Non-Negotiable Boundaries

- Do not store NHATS credentials, account identifiers, session cookies, tokens, raw Colectica exports, raw metadata dumps, raw value-label tables, row-level data, respondent identifiers, death dates, screenshots with restricted content, or controlled-use files in this repository.
- Do not upload restricted or raw NHATS material to public AI systems.
- Do not convert a validator `reviewable-but-still-blocked` result into slot closure.
- Do not edit the review execution register unless there is a governed, redacted packet plus human review evidence and second-reviewer signoff.
- Do not open route-classifier, extraction, aggregation, weighted counts, public export, calibration, or individual-prediction gates from this runbook.

## First Packet Target

The first packet should use the lowest-risk join-key task:

| Field | Value |
| --- | --- |
| `requiredRouteFieldId` | `identity_join_key` |
| `taskId` | `identity_join_key-spid` |
| `variableName` | `spid` |
| `round` | `both` |
| Expected verdict | `reviewable-but-still-blocked` if all required redacted review fields are present and no forbidden material appears. |

This task is preferred because it tests canonical key confirmation without opening outcome, death-date, missingness, weight, or disclosure logic.

## Capture Workflow

1. Work in a controlled environment outside the repository.
2. Open the official NHATS Colectica route identified by the access-route probe and authenticated capture template.
3. Locate the registered task variable page for `spid`.
4. Confirm only these review facts:
   - value labels were reviewed;
   - question text was reviewed;
   - universe and skip logic were reviewed;
   - concordance to the registered task was reviewed;
   - public-use tier was reviewed;
   - sensitive or restricted material was excluded;
   - variable-specific missing codes were reviewed.
5. Create a local source artifact outside the repository and compute its SHA-256 digest.
6. Produce a redacted packet JSON in a temporary local path. The packet must not contain raw value labels or raw metadata.
7. Run the single-packet validator.
8. If the verdict is `rejected` or `cannot-evaluate`, fix the external packet and revalidate; do not modify repository review registers.
9. If the verdict is `reviewable-but-still-blocked`, route the packet to human review and independent second review. The slot still remains open until a later governed register update.

## Draft Generator

Before hand-filling a packet, generate the fail-closed local draft:

```bash
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/build_nhats_colectica_capture_packet_draft.py
```

The generator writes ignored files under `build/reports/nhats-colectica-capture-packet-draft/`. The generated packet is intentionally not reviewable because it contains placeholders and all review flags remain false. It is only a shape scaffold for the first controlled human capture; it does not execute login, attach evidence, close a slot, open route classifier, allow extraction, publish output, calibrate a model, or support individual prediction.

## Review Handoff Builder

After a packet has been created or edited outside the repository, build the local handoff report:

```bash
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/build_nhats_colectica_capture_packet_review_handoff.py \
  --packet build/reports/nhats-colectica-capture-packet-draft/identity_join_key-spid-draft.json
```

The default draft must produce `blocked-not-reviewable`. A real redacted packet may only produce `review-handoff-ready-but-slot-still-open` after the existing packet validator returns `reviewable-but-still-blocked`. Even then, the handoff remains an ignored local report: it does not update `life_path_nhats_colectica_capture_packet_review_execution_register.json`, close a capture slot, open a route classifier, allow extraction, publish output, calibrate a model, or support individual prediction.

## Redacted Packet Skeleton

Use this as a shape template, not as evidence:

```json
{
  "packetSchema": "human-infra.life-path-nhats-colectica-capture-packet.v1",
  "packetId": "nhats-colectica-capture-packet-YYYYMMDD-001",
  "sourceId": "nhats",
  "taskRegisterId": "nhats-r13-r14-colectica-capture-task-register-2026-07-03",
  "templateId": "nhats-r13-r14-colectica-authenticated-capture-template-2026-07-03",
  "routeClassifierReadinessId": "nhats-r13-r14-route-classifier-readiness-2026-07-03",
  "requiredRouteFieldId": "identity_join_key",
  "taskId": "identity_join_key-spid",
  "variableName": "spid",
  "round": "both",
  "detailsPageUrlRedacted": "redacted controlled Colectica details page URL or public canonical route",
  "sourceCaptureSha256": "<64 lowercase hex sha256>",
  "artifactHashAlgorithm": "sha256",
  "captureMethod": "controlled-colectica-authenticated-page-redacted",
  "captureDate": "YYYY-MM-DD",
  "artifactDescriptionRedacted": "Redacted capture packet; credential material, row-level material, identifiers, restricted exports and individual dates are not attached.",
  "valueLabelsReviewed": true,
  "questionTextReviewed": true,
  "universeSkipLogicReviewed": true,
  "concordanceReviewed": true,
  "publicUseTierReviewed": true,
  "sensitiveRestrictedExclusionReviewed": true,
  "variableSpecificMissingCodesReviewed": true,
  "reviewerRole": "human-domain-reviewer",
  "secondReviewerRole": "independent-human-reviewer",
  "aiOnlySignoff": false,
  "publicAiUpload": false,
  "rawMetadataAttached": false,
  "rawValueLabelsAttached": false,
  "promotionAllowed": false,
  "routeClassifierAllowed": false,
  "realExtractionAllowed": false,
  "aggregateCohortFlowAllowed": false,
  "weightedRouteCountsAllowed": false,
  "publicExportAllowed": false,
  "calibrationAllowed": false,
  "individualPredictionAllowed": false
}
```

## Validator Command

Run the validator against a temporary redacted packet:

```bash
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_colectica_capture_packet_validator.py \
  --packet /path/to/redacted-packet.json \
  --out /path/to/validation-output.json
```

The command output should still state `model_g4=blocked`. A successful single-packet evaluation is evidence of packet-shape validity only.

## Verdict Handling

| Verdict | Meaning | Next action |
| --- | --- | --- |
| `rejected` | The packet contains a forbidden key, mismatched contract id, forbidden variable, non-human review role, unsafe flag, or other hard violation. | Discard or rebuild the external packet. Do not update repository registers. |
| `cannot-evaluate` | Required review fields or packet fields are missing. | Complete missing redacted review fields outside the repo and revalidate. |
| `reviewable-but-still-blocked` | The redacted packet shape is acceptable for human review. | Send to human reviewer and independent second reviewer. Slot closure remains blocked. |

## Capture Task Groups

| Group | Count | Variables |
| --- | ---: | --- |
| `identity_join_key` | 2 | `spid`, `spidr12` |
| `round13_baseline_eligibility` | 5 | `r13status`, `r13statuscat`, `r13dcontnew`, `fl13newsample`, `fl13facility` |
| `round14_interview_status` | 7 | `r14status`, `r14statuscat`, `r14dcontnew`, `r14breakoffst`, `r14breakoffqt`, `fl14pt2miss`, `r14dlmlint` |
| `proxy_status` | 6 | `is13resptype`, `op13proxy`, `op13whyproxy`, `is14resptype`, `op14proxy`, `op14whyproxy` |
| `facility_residential_status` | 4 | `r13dresid`, `fl13facility`, `r14dresid`, `fl14facility` |
| `death_decedent_indicator` | 4 | `fl13spdied`, `fl14spdied`, `r13dlmlint`, `r14dlmlint` |
| `nonresponse_missing_code` | 6 | `r13breakoffst`, `r13breakoffqt`, `fl13pt2miss`, `r14breakoffst`, `r14breakoffqt`, `fl14pt2miss` |
| `design_weight_linkage` | 4 | `w13varstrat`, `w13varunit`, `w14varstrat`, `w14varunit` |
| `disclosure_cell_count` | 1 | `computed_output_cell_n` |

## What This Does Not Unblock

Even after the first packet validates as `reviewable-but-still-blocked`, these remain blocked:

- capture slot closure;
- value-label confirmation register update;
- route-value crosswalk rows;
- variable-specific missing-code map;
- route classifier;
- real NHATS extraction;
- aggregate cohort flow;
- weighted route counts;
- public output;
- L4 validation/calibration;
- individual prediction or personal death-date output.

## Promotion Path After Human Review

Only after redacted packet review and independent second-reviewer signoff should maintainers consider a later update to:

1. `life_path_nhats_colectica_capture_packet_review_execution_register.json`;
2. `life_path_nhats_colectica_value_label_review_execution_register.json`;
3. `life_path_nhats_route_value_crosswalk_assembly_protocol.json`;
4. `life_path_nhats_route_value_crosswalk_entry_validator_test_cases.json`.

That later update must still keep route classifier, extraction, public export, calibration, and individual prediction blocked until all upstream gates explicitly pass.
