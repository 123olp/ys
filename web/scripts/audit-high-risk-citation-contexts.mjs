import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");
const dataPath = path.join(webRoot, "src/data/effective-immortality-evidence.json");
const riskPath = path.join(webRoot, "src/data/effective-immortality-flywheel/CITATION_CONTEXT_RISK_TRIAGE.json");
const referenceVerificationPath = path.join(webRoot, "src/data/effective-immortality-flywheel/REFERENCE_VERIFICATION.json");
const outputDir = path.join(webRoot, "src/data/effective-immortality-flywheel");
const outputJsonPath = path.join(outputDir, "HIGH_RISK_CITATION_CONTEXT_REVIEW.json");
const outputMdPath = path.join(outputDir, "HIGH_RISK_CITATION_CONTEXT_REVIEW.md");

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function readJson(filePath) {
  const content = fs.readFileSync(filePath, "utf8");
  return { content, json: JSON.parse(content) };
}

function sortedUnique(values) {
  return [...new Set(values.filter(Boolean))].sort((a, b) => a.localeCompare(b));
}

function referencesForContext(referenceRegistry, contextId) {
  return referenceRegistry
    .filter((ref) => (ref.citationContexts || []).includes(contextId))
    .sort((a, b) => a.key.localeCompare(b.key));
}

function claimsForContext(claimEvidenceMap, contextId) {
  return claimEvidenceMap
    .filter((row) => (row.citationContexts || []).includes(contextId))
    .map((row) => row.claimId)
    .sort((a, b) => a.localeCompare(b));
}

function renderMarkdown(audit) {
  const rows = audit.details.reviewed_contexts.length
    ? audit.details.reviewed_contexts
        .map((context) => `| ${context.context_id} | ${context.local_verdict} | ${context.claims.join(", ")} | ${context.references.length} | ${context.action} |`)
        .join("\n")
    : "| - | - | - | - | - |";

  const missingRows = audit.details.missing_review_contexts.length
    ? audit.details.missing_review_contexts.map((context) => `- ${context}`).join("\n")
    : "- None";

  const contextSections = audit.details.reviewed_contexts
    .map((context) => {
      const sourceRows = context.source_findings
        .map((source) => `| \`${source.reference_key}\` | ${source.verification} | ${source.context_support} | ${source.boundary} | ${source.action} |`)
        .join("\n");

      const sourceDetails = context.source_findings
        .map((source) => `#### \`${source.reference_key}\`: ${source.title}

- Source role: ${source.source_role}
- Inspected source(s): ${source.inspected_sources.map((item) => `<${item}>`).join("; ")}
- Support judgment: ${source.context_support}
- Evidence note: ${source.evidence_note}
- Boundary note: ${source.boundary}
- Action: ${source.action}
`)
        .join("\n");

      return `### ${context.context_id}: ${context.source_group}

- Risk tier: ${context.risk_tier}
- Local verdict: ${context.local_verdict}
- Claims: ${context.claims.join(", ")}
- Used for: ${context.used_for}
- Supports: ${context.supports}
- Does not support: ${context.does_not_support}
- Action: ${context.action}

| Reference | Verification | Context support | Boundary | Action |
| --- | --- | --- | --- | --- |
${sourceRows}

${sourceDetails}`;
    })
    .join("\n");

  return `# High-Risk Citation Context Review

Date: ${audit.generated_at}
Input: \`web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_RISK_TRIAGE.json\`
Output JSON: \`web/src/data/effective-immortality-flywheel/HIGH_RISK_CITATION_CONTEXT_REVIEW.json\`

## Summary

Verdict: \`${audit.verdict}\`

Reason: \`${audit.reason_code}\`

${audit.summary}

This is a local source-bounded review of HIGH/BLOCKER citation contexts. It improves the local evidence chain but does not replace a fresh independent reviewer thread.

| Metric | Count |
| --- | ---: |
| High or blocker contexts | ${audit.details.high_or_blocker_context_count} |
| Reviewed contexts | ${audit.details.reviewed_context_count} |
| Missing review contexts | ${audit.details.missing_review_context_count} |

## Reviewed Contexts

| Context | Local verdict | Claims | References | Action |
| --- | --- | --- | ---: | --- |
${rows}

## Missing Review Contexts

${missingRows}

## Context Details

${contextSections}

## Scope

This artifact checks the local highest-risk citation context against accessible source metadata and official/source pages. It records source-support boundaries and recommended prose actions. It does not claim that the whole paper has passed sentence-level citation-context review.
`;
}

const preparedReviews = {
  CTX2: {
    local_verdict: "KEEP_WITH_BOUNDARY",
    action: "Keep the context only as T -> E measurement language; keep fresh reviewer review required before formal submission.",
    source_findings: [
      {
        reference_key: "grossman1972healthcapital",
        title: "On the Concept of Health Capital and the Demand for Health",
        source_role: "Health capital lineage and economic-theory entry point.",
        inspected_sources: [
          "https://api.crossref.org/works/10.1086/259880",
          "https://ideas.repec.org/a/ucp/jpolec/v80y1972i2p223-55.html",
          "https://EconPapers.repec.org/RePEc:ucp:jpolec:v:80:y:1972:i:2:p:223-55",
        ],
        verification: "METADATA_VERIFIED_FULL_TEXT_RESTRICTED",
        context_support: "WEAK_FOR_CONTEXT_WITH_METADATA_ONLY",
        evidence_note:
          "Crossref and RePEc verify the article metadata, DOI, Journal of Political Economy venue, year, and page range. The accessible metadata supports using the source as the health-capital lineage entry, but the local audit did not extract full-text passages because the available PDF is scanned/restricted.",
        boundary:
          "Do not let Grossman alone carry the claim that effective time includes agency, subject continuity, or future option value.",
        action: "Keep as lineage source; fresh reviewer should inspect full text if a stronger health-capital claim is made.",
      },
      {
        reference_key: "whohale7752",
        title: "Healthy life expectancy (HALE) metadata",
        source_role: "Official public-health metric for health-adjusted expected years.",
        inspected_sources: [
          "https://www.who.int/data/gho/indicator-metadata-registry/imr-details/7752",
        ],
        verification: "OFFICIAL_PAGE_VERIFIED",
        context_support: "SUPPORTS_HEALTH_ADJUSTED_TIME",
        evidence_note:
          "WHO defines HALE as the average years expected in full health and states that it captures fatal and non-fatal outcomes by adjusting life expectancy across health states.",
        boundary:
          "HALE is population-health measurement language; it does not define subject continuity, individual medical advice, agency, or future option value.",
        action: "Use for health-adjusted time only.",
      },
      {
        reference_key: "niceEconomicEvaluation",
        title: "Economic evaluation",
        source_role: "Policy evaluation language for QALYs and lifetime health effects.",
        inspected_sources: [
          "https://www.nice.org.uk/process/pmg36/chapter/economic-evaluation-2",
        ],
        verification: "OFFICIAL_PAGE_VERIFIED",
        context_support: "SUPPORTS_QALY_QUALITY_AND_LENGTH_LANGUAGE",
        evidence_note:
          "NICE states that health effects should be expressed in QALYs and explains that QALYs combine life expectancy with health-related quality of life within the model time horizon.",
        boundary:
          "QALY is a health-economic index with assumptions and valuation choices; it cannot fully represent dignity, identity continuity, agency, subjective time, or option space.",
        action: "Use for quality-adjusted time only; keep extra Human Infra fields for agency and option value.",
      },
    ],
  },
};

const evidence = readJson(dataPath);
const risk = readJson(riskPath);
const referenceVerification = readJson(referenceVerificationPath);

const contextsById = new Map((evidence.json.citationContextRegister || []).map((context) => [context.id, context]));
const referenceRegistry = evidence.json.referenceRegistry || [];
const claimEvidenceMap = evidence.json.claimEvidenceMap || [];
const referenceStatus = new Map((referenceVerification.json.details?.per_entry || []).map((entry) => [entry.key, entry]));

const highContexts = (risk.json.details?.context_triage || [])
  .filter((context) => ["HIGH", "BLOCKER"].includes(context.risk_tier))
  .sort((a, b) => a.context_id.localeCompare(b.context_id));

const reviewedContexts = [];
const missingReviewContexts = [];

for (const riskContext of highContexts) {
  const prepared = preparedReviews[riskContext.context_id];
  if (!prepared) {
    missingReviewContexts.push(riskContext.context_id);
    continue;
  }

  const context = contextsById.get(riskContext.context_id) || {};
  const references = referencesForContext(referenceRegistry, riskContext.context_id).map((ref) => ({
    key: ref.key,
    title: ref.title,
    audit_status: ref.auditStatus,
    live_status: referenceStatus.get(ref.key)?.live_status || "UNKNOWN",
    method: referenceStatus.get(ref.key)?.method || "UNKNOWN",
  }));
  const sourceFindingKeys = new Set(prepared.source_findings.map((source) => source.reference_key));
  const missingSourceFindings = references.filter((ref) => !sourceFindingKeys.has(ref.key)).map((ref) => ref.key);
  if (missingSourceFindings.length) {
    missingReviewContexts.push(`${riskContext.context_id}: missing source findings for ${missingSourceFindings.join(", ")}`);
  }

  reviewedContexts.push({
    context_id: riskContext.context_id,
    source_group: context.sourceGroup || riskContext.source_group,
    risk_tier: riskContext.risk_tier,
    claims: claimsForContext(claimEvidenceMap, riskContext.context_id),
    references,
    used_for: context.usedFor,
    supports: context.supports,
    does_not_support: context.doesNotSupport,
    local_verdict: prepared.local_verdict,
    action: prepared.action,
    source_findings: prepared.source_findings,
  });
}

const reviewCoverageComplete = missingReviewContexts.length === 0;
const audit = {
  audit_skill: "high-risk-citation-context-review",
  verdict: reviewCoverageComplete ? "PASS_WITH_LIMITATIONS" : "INCOMPLETE",
  reason_code: reviewCoverageComplete
    ? "high_risk_contexts_reviewed_with_source_boundaries"
    : "high_risk_contexts_missing_local_review",
  summary: reviewCoverageComplete
    ? "All locally HIGH/BLOCKER citation contexts have a source-bounded local review and explicit boundary action. Fresh independent citation-context review remains required before formal submission."
    : "At least one locally HIGH/BLOCKER citation context lacks a source-bounded local review.",
  generated_at: `${evidence.json.updated}T00:00:00.000Z`,
  audited_input_hashes: {
    "src/data/effective-immortality-evidence.json": sha256(evidence.content),
    "src/data/effective-immortality-flywheel/CITATION_CONTEXT_RISK_TRIAGE.json": sha256(risk.content),
    "src/data/effective-immortality-flywheel/REFERENCE_VERIFICATION.json": sha256(referenceVerification.content),
  },
  details: {
    schema_version: evidence.json.schemaVersion,
    high_or_blocker_context_count: highContexts.length,
    reviewed_context_count: reviewedContexts.length,
    missing_review_context_count: missingReviewContexts.length,
    missing_review_contexts: missingReviewContexts,
    reviewed_contexts: reviewedContexts,
    fresh_reviewer_required: true,
  },
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(outputJsonPath, `${JSON.stringify(audit, null, 2)}\n`);
fs.writeFileSync(outputMdPath, renderMarkdown(audit));

console.log(`high-risk citation-context review ${audit.verdict}`);
console.log(`high/blocker contexts ${highContexts.length}`);
console.log(`reviewed ${reviewedContexts.length}`);
console.log(`missing ${missingReviewContexts.length}`);
console.log(`wrote ${path.relative(webRoot, outputJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, outputMdPath)}`);

if (!reviewCoverageComplete) {
  process.exitCode = 1;
}
