import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");
const dataPath = path.join(webRoot, "src/data/effective-immortality-evidence.json");
const referenceVerificationPath = path.join(
  webRoot,
  "src/data/effective-immortality-flywheel/REFERENCE_VERIFICATION.json",
);
const outputDir = path.join(webRoot, "src/data/effective-immortality-flywheel");
const auditJsonPath = path.join(outputDir, "CLAIM_CONTEXT_AUDIT.json");
const auditMdPath = path.join(outputDir, "CLAIM_CONTEXT_AUDIT.md");

const allowedAlignmentVerdicts = new Set([
  "FRAMEWORK_ONLY",
  "OPERATIONAL_INTERFACE",
  "METHOD_SUPPORTED",
  "BOUNDED_EMPIRICAL",
  "NORMATIVE_MEASUREMENT",
  "GOVERNANCE_REQUIRED",
  "HARD_BOUNDARY",
]);

const allowedCitationStatuses = new Set(["KEEP", "KEEP WITH BOUNDARY"]);

const requiredClaimMapFields = [
  "claimId",
  "paperSections",
  "evidenceEdges",
  "citationContexts",
  "alignmentVerdict",
  "currentSupport",
  "falsifiers",
  "upgradeGate",
];

const requiredContextFields = [
  "id",
  "sourceGroup",
  "canonicalRecord",
  "usedFor",
  "supports",
  "doesNotSupport",
  "citationStatus",
];

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function unique(values) {
  return [...new Set(values)].sort((a, b) => a.localeCompare(b));
}

function pushGap(gaps, severity, code, message, subject) {
  gaps.push({ severity, code, message, subject });
}

function renderMarkdown(audit) {
  const gapRows = audit.details.gaps.length
    ? audit.details.gaps
        .map((gap) => `| ${gap.severity} | ${gap.code} | ${gap.subject} | ${gap.message.replace(/\|/g, "\\|")} |`)
        .join("\n")
    : "| - | - | - | None |";

  const claimRows = audit.details.claim_alignment
    .map((row) => (
      `| ${row.claim_id} | ${row.alignment_verdict} | ${row.context_count} | ${row.reference_count} | ${row.boundary_status} | ${row.status} |`
    ))
    .join("\n");

  const contextRows = audit.details.context_coverage
    .map((row) => (
      `| ${row.context_id} | ${row.citation_status} | ${row.reference_count} | ${row.has_boundary ? "yes" : "no"} | ${row.status} |`
    ))
    .join("\n");

  return `# Claim Context Alignment Audit

Date: ${audit.generated_at}
Input: \`web/src/data/effective-immortality-evidence.json\`
Output JSON: \`web/src/data/effective-immortality-flywheel/CLAIM_CONTEXT_AUDIT.json\`

## Summary

Verdict: \`${audit.verdict}\`

Reason: \`${audit.reason_code}\`

${audit.summary}

| Metric | Count |
| --- | ---: |
| Claims | ${audit.details.claim_count} |
| Claim evidence rows | ${audit.details.claim_evidence_map_count} |
| Citation contexts | ${audit.details.citation_context_count} |
| Reference registry entries | ${audit.details.reference_registry_count} |
| Reference verification FAIL rows | ${audit.details.reference_verification_fail_count} |
| Gaps | ${audit.details.gaps.length} |

## Claim Alignment

| Claim | Alignment verdict | Contexts | References through contexts | Boundary status | Status |
| --- | --- | ---: | ---: | --- | --- |
${claimRows}

## Context Coverage

| Context | Citation status | References | Boundary text | Status |
| --- | --- | ---: | --- | --- |
${contextRows}

## Gaps

| Severity | Code | Subject | Message |
| --- | --- | --- | --- |
${gapRows}

## Scope

This audit checks local claim-context-reference structure: every core claim must have a claim evidence map row, every cited context must exist, every context must state both support and non-support boundaries, and every context used by a claim must be backed by at least one Reference Registry entry. It also consumes REFERENCE_VERIFICATION.json when present and fails if any reference has live_status=FAIL. It does not replace fresh reviewer sentence-level citation-context judgment.
`;
}

const evidenceContent = fs.readFileSync(dataPath, "utf8");
const evidence = JSON.parse(evidenceContent);
const referenceVerification = fs.existsSync(referenceVerificationPath)
  ? JSON.parse(fs.readFileSync(referenceVerificationPath, "utf8"))
  : null;

const claims = evidence.claimRegister || [];
const claimMap = evidence.claimEvidenceMap || [];
const contexts = evidence.citationContextRegister || [];
const references = evidence.referenceRegistry || [];
const edges = evidence.evidenceEdges || [];

const gaps = [];
const claimIds = new Set(claims.map((claim) => claim.id));
const mappedClaimIds = new Set(claimMap.map((claim) => claim.claimId));
const contextIds = new Set(contexts.map((context) => context.id));
const edgeIds = new Set(edges.map((edge) => edge.edge));
const referencesByContext = new Map();

for (const context of contexts) {
  referencesByContext.set(context.id, []);
}
for (const ref of references) {
  for (const contextId of ref.citationContexts || []) {
    if (!referencesByContext.has(contextId)) referencesByContext.set(contextId, []);
    referencesByContext.get(contextId).push(ref.key);
  }
}

for (const claim of claims) {
  if (!mappedClaimIds.has(claim.id)) {
    pushGap(gaps, "FAIL", "missing_claim_evidence_map", `Claim ${claim.id} has no claimEvidenceMap row.`, claim.id);
  }
}

for (const row of claimMap) {
  if (!claimIds.has(row.claimId)) {
    pushGap(gaps, "FAIL", "unknown_claim", `Claim evidence row points to unknown claim ${row.claimId}.`, row.claimId || "UNKNOWN");
  }
  for (const field of requiredClaimMapFields) {
    if (!row[field] || (Array.isArray(row[field]) && row[field].length === 0)) {
      pushGap(gaps, "FAIL", "claim_map_missing_field", `Missing required field ${field}.`, row.claimId || "UNKNOWN");
    }
  }
  if (!allowedAlignmentVerdicts.has(row.alignmentVerdict)) {
    pushGap(gaps, "FAIL", "unknown_alignment_verdict", `Unknown alignment verdict ${row.alignmentVerdict}.`, row.claimId || "UNKNOWN");
  }
  for (const edge of row.evidenceEdges || []) {
    if (!edgeIds.has(edge)) {
      pushGap(gaps, "FAIL", "unknown_evidence_edge", `Unknown evidence edge ${edge}.`, row.claimId || "UNKNOWN");
    }
  }
  for (const contextId of row.citationContexts || []) {
    if (!contextIds.has(contextId)) {
      pushGap(gaps, "FAIL", "unknown_citation_context", `Unknown citation context ${contextId}.`, row.claimId || "UNKNOWN");
    } else if ((referencesByContext.get(contextId) || []).length === 0) {
      pushGap(gaps, "FAIL", "context_without_reference", `Citation context ${contextId} has no Reference Registry entry.`, row.claimId || "UNKNOWN");
    }
  }
  if ((row.falsifiers || []).length === 0) {
    pushGap(gaps, "FAIL", "missing_falsifier", "Claim evidence row has no falsifier.", row.claimId || "UNKNOWN");
  }
  if (row.claimId === "CL7" && row.alignmentVerdict !== "HARD_BOUNDARY") {
    pushGap(gaps, "FAIL", "hard_boundary_not_marked", "CL7 must remain HARD_BOUNDARY.", row.claimId);
  }
}

for (const context of contexts) {
  for (const field of requiredContextFields) {
    if (!context[field]) {
      pushGap(gaps, "FAIL", "context_missing_field", `Missing required field ${field}.`, context.id || "UNKNOWN");
    }
  }
  if (!allowedCitationStatuses.has(context.citationStatus)) {
    pushGap(gaps, "FAIL", "unknown_citation_status", `Unknown citation status ${context.citationStatus}.`, context.id || "UNKNOWN");
  }
  if (!context.doesNotSupport || String(context.doesNotSupport).length < 12) {
    pushGap(gaps, "FAIL", "missing_non_support_boundary", "Citation context lacks a meaningful doesNotSupport boundary.", context.id || "UNKNOWN");
  }
  if ((referencesByContext.get(context.id) || []).length === 0) {
    pushGap(gaps, "FAIL", "context_without_reference", "Citation context has no Reference Registry backing entry.", context.id || "UNKNOWN");
  }
}

for (const ref of references) {
  for (const contextId of ref.citationContexts || []) {
    if (!contextIds.has(contextId)) {
      pushGap(gaps, "FAIL", "reference_unknown_context", `Reference points to unknown context ${contextId}.`, ref.key);
    }
  }
}

const referenceVerificationFailures = referenceVerification
  ? (referenceVerification.details?.per_entry || []).filter((entry) => entry.live_status === "FAIL")
  : [];
for (const entry of referenceVerificationFailures) {
  pushGap(gaps, "FAIL", "reference_verification_fail", `Reference verification failed: ${entry.message}`, entry.key);
}

const claimAlignment = claimMap.map((row) => {
  const uniqueRefs = unique((row.citationContexts || []).flatMap((contextId) => referencesByContext.get(contextId) || []));
  const boundaryStatus = row.claimId === "CL7" || row.alignmentVerdict.includes("BOUNDARY") || row.alignmentVerdict === "BOUNDED_EMPIRICAL"
    ? "explicit"
    : "scoped";
  const rowGapCount = gaps.filter((gap) => gap.subject === row.claimId).length;
  return {
    claim_id: row.claimId,
    alignment_verdict: row.alignmentVerdict,
    context_count: (row.citationContexts || []).length,
    reference_count: uniqueRefs.length,
    boundary_status: boundaryStatus,
    status: rowGapCount ? "FAIL" : "PASS",
  };
});

const contextCoverage = contexts.map((context) => {
  const refs = referencesByContext.get(context.id) || [];
  const hasBoundary = Boolean(context.doesNotSupport && String(context.doesNotSupport).length >= 12);
  const rowGapCount = gaps.filter((gap) => gap.subject === context.id).length;
  return {
    context_id: context.id,
    citation_status: context.citationStatus,
    reference_count: refs.length,
    has_boundary: hasBoundary,
    status: rowGapCount ? "FAIL" : "PASS",
  };
});

const audit = {
  audit_skill: "claim-context-alignment-audit",
  verdict: gaps.length ? "FAIL" : "PASS",
  reason_code: gaps.length ? "claim_context_alignment_gaps" : "all_claim_contexts_aligned",
  summary: gaps.length
    ? "At least one claim, citation context, reference backing, or hard-boundary invariant is incomplete."
    : "All core claims have bounded claim evidence rows; all citation contexts state support and non-support boundaries; all contexts are backed by Reference Registry entries; no reference verification FAIL rows are present.",
  generated_at: `${evidence.updated}T00:00:00.000Z`,
  audited_input_hashes: {
    "src/data/effective-immortality-evidence.json": sha256(evidenceContent),
    ...(referenceVerification
      ? {
          "src/data/effective-immortality-flywheel/REFERENCE_VERIFICATION.json": sha256(
            fs.readFileSync(referenceVerificationPath, "utf8"),
          ),
        }
      : {}),
  },
  details: {
    schema_version: evidence.schemaVersion,
    claim_count: claims.length,
    claim_evidence_map_count: claimMap.length,
    citation_context_count: contexts.length,
    reference_registry_count: references.length,
    reference_verification_fail_count: referenceVerificationFailures.length,
    claim_alignment: claimAlignment,
    context_coverage: contextCoverage,
    gaps,
  },
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(auditJsonPath, `${JSON.stringify(audit, null, 2)}\n`);
fs.writeFileSync(auditMdPath, renderMarkdown(audit));

console.log(`claim-context verdict ${audit.verdict}`);
console.log(`claims ${claims.length}`);
console.log(`contexts ${contexts.length}`);
console.log(`references ${references.length}`);
console.log(`gaps ${gaps.length}`);
console.log(`wrote ${path.relative(webRoot, auditJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, auditMdPath)}`);

if (audit.verdict === "FAIL") {
  process.exitCode = 1;
}
