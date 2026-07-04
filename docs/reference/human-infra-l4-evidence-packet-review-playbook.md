# L4 Evidence Packet Review Playbook

This playbook explains how a future L4 evidence packet may be reviewed before any L4 evidence slot can close. It is a workflow companion to `human-infra-l4-evidence-intake-register.json`; it is not direct evidence, not a calibration result, and not permission to publish real weighted output.

Current repository state:

```text
packetCount = 0
closedSlotCount = 0
L4 aggregate calibrated admission = blocked
public weighted domain output = blocked
calibrated prediction = blocked
individual use = blocked
```

## Purpose

L4 moves the project from synthetic or local-only model rehearsal toward aggregate calibrated research modeling. That step has a higher trust boundary because evidence may involve governed access, disclosure review, real aggregate extraction, calibration diagnostics, and human judgment.

The playbook exists to prevent four failure modes:

- A natural-language claim being treated as direct evidence.
- A raw row, identifier, restricted file, or sensitive screenshot entering the repository.
- An AI-only signoff replacing human review.
- A reviewed packet being misread as permission to open L4, public weighted output, calibrated prediction, intervention ranking, medical advice, individual prediction, or individual death-date output.

## Scope

This playbook covers only L4 evidence packets for the five work orders in the intake register:

- `L4WO-01-nhats-governed-access-and-workspace`
- `L4WO-02-nhats-exact-field-value-confirmation`
- `L4WO-03-nhats-real-extraction-cohort-flow`
- `L4WO-04-nhanes-human-disclosure-review`
- `L4WO-05-validation-calibration-diagnostics`

It does not create a packet. It does not accept a packet. It does not close any slot.

## Packet Contract

Every future packet must follow `human-infra.l4-evidence-packet.v1` from the intake register. A packet can only be considered for bounded L4 evidence review when it includes:

- Matching `workOrderId`, `slotId`, `candidatePath`, `evidenceClass`, and `repositoryPolicy`.
- A redacted SHA-256 artifact hash.
- A non-sensitive artifact description.
- A producer role.
- A first human reviewer role.
- A second reviewer role when required by the slot.
- Explicit booleans showing no raw data, restricted data, identifiers, public AI upload, or AI-only signoff.
- `allowedUse = bounded L4 evidence review only`.
- `downstreamDecision = l4-still-blocked`.

The packet must not contain raw rows, identifiers, restricted file paths, real weighted rates, real standard errors, real confidence intervals, individual predictions, individual death dates, secrets, or screenshots with sensitive values.

Boundary shorthand:

```text
No raw rows.
No identifiers.
No restricted data copies.
No public AI upload.
No AI-only signoff.
```

## Lifecycle

```text
pending slot
  -> draft-redacted packet prepared outside raw-data surfaces
  -> producer preflight checks forbidden fields and repository policy
  -> first human reviewer checks source, hash, slot match and sensitivity class
  -> second reviewer checks independence, disclosure boundary and allowed use
  -> packet verdict recorded as rejected, cannot-evaluate, or reviewable-but-still-blocked
  -> slot remains pending until a future explicit register update closes it
```

The default result is still blocked. A packet can improve the evidence trail without changing model level.

## Review Roles

| Role | Responsibility | Cannot Do |
| --- | --- | --- |
| Producer | Prepare a redacted packet, hash the artifact, map it to one slot, and declare forbidden-field booleans. | Cannot approve its own packet. |
| First human reviewer | Verify slot match, evidence class, artifact hash, sensitivity class, repository policy, and forbidden fields. | Cannot be replaced by AI-only review. |
| Second reviewer | Recheck disclosure boundary, independence, allowed use, and downstream decision. | Cannot convert one reviewed packet into L4 admission. |
| Maintainer | Update the register only after all packet and slot conditions are satisfied. | Cannot close a slot while packetCount or evidenceRef semantics are inconsistent. |

AI tools may help format, diff, lint, or summarize a packet, but AI cannot be the only reviewer and cannot provide the human signoff.

## Verdicts

| Verdict | Meaning | Register Effect |
| --- | --- | --- |
| `rejected` | Packet contains forbidden material, wrong slot mapping, unsupported evidence class, AI-only signoff, or missing hash. | No slot closes. L4 remains blocked. |
| `cannot-evaluate` | Packet lacks enough non-sensitive context to judge source, hash, reviewer role, or boundary. | No slot closes. L4 remains blocked. |
| `reviewable-but-still-blocked` | Packet appears safe and relevant, but downstream gates still require other slots, reviewer actions, or calibration diagnostics. | Evidence may be queued for future register update. L4 remains blocked. |
| `slot-close-candidate` | All slot-specific evidence exists and both reviews pass. | A separate explicit register update is still required; this playbook alone does not close the slot. |

## Abort Gates

Any of the following must stop the packet from entering review:

- Raw rows, identifiers, restricted files, or sensitive screenshots are present.
- The artifact hash is missing, non-SHA-256, or cannot be matched to the redacted artifact.
- `publicAiUpload = true`.
- `aiOnlySignoff = true`.
- The packet tries to publish real weighted rates, real standard errors, real confidence intervals, or individual-level values.
- The packet sets `allowedUse` beyond bounded L4 evidence review.
- The packet sets `downstreamDecision` to anything other than `l4-still-blocked`.
- The packet claims calibration, clinical value, medical advice, intervention ranking, individual prediction, or individual death-date output.

## Slot Closure Rule

A slot can close only after a future reviewed register update proves all of these conditions:

1. The packet matches exactly one pending slot.
2. The packet class is allowed by the intake register.
3. The packet contains a redacted SHA-256 hash and no forbidden fields.
4. Required human review and second review are complete.
5. Repository policy remains compatible with the slot.
6. `downstreamDecision` remains `l4-still-blocked`.
7. The update does not open public weighted output, calibrated prediction, individual use, medical advice, intervention ranking, or death-date output.

Until that separate update exists, every slot remains pending and the packet counter remains zero.

## Safe Consumption

Future consumers may use reviewed packets only to decide whether a specific L4 evidence slot has enough redacted, human-reviewed evidence to enter the next review step. They must not use the packet to:

- Train a model.
- Calibrate a model.
- Publish real aggregate output.
- Rank interventions.
- Give medical advice.
- Predict an individual lifetime.
- Infer or disclose an individual death date.

## Verification

The repository audit must continue to prove:

```text
make l4-evidence-intake-register-audit
```

The audit must check that this playbook exists, that the intake register links to it, that packet counts remain zero, that every slot remains pending, and that all L4/public/calibrated/individual uses remain blocked.
