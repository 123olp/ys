import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");
const dataPath = path.join(webRoot, "src/data/effective-immortality-evidence.json");
const packetPath = path.join(webRoot, "src/data/effective-immortality-flywheel/CITATION_CONTEXT_REVIEW_PACKET.json");
const referenceVerificationPath = path.join(webRoot, "src/data/effective-immortality-flywheel/REFERENCE_VERIFICATION.json");
const claimContextAuditPath = path.join(webRoot, "src/data/effective-immortality-flywheel/CLAIM_CONTEXT_AUDIT.json");
const outputDir = path.join(webRoot, "src/data/effective-immortality-flywheel");
const outputJsonPath = path.join(outputDir, "CITATION_CONTEXT_RISK_TRIAGE.json");
const outputMdPath = path.join(outputDir, "CITATION_CONTEXT_RISK_TRIAGE.md");

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

function statusByReference(referenceVerification) {
  const entries = referenceVerification.details?.per_entry || [];
  return new Map(entries.map((entry) => [entry.key, entry]));
}

function claimById(evidence) {
  return new Map((evidence.claimRegister || []).map((claim) => [claim.id, claim]));
}

function claimMapById(evidence) {
  return new Map((evidence.claimEvidenceMap || []).map((row) => [row.claimId, row]));
}

function isHighBoundaryText(text) {
  return /不证明|不能泛化|不能把|不能替代|不等于|不提供数值|不输出个体|不得/gu.test(text || "");
}

function riskForContext(contextPacket, referenceStatusMap) {
  const riskFactors = [];
  const warnedReferences = contextPacket.references
    .filter((ref) => referenceStatusMap.get(ref.key)?.live_status === "WARN")
    .map((ref) => ref.key);
  const failedReferences = contextPacket.references
    .filter((ref) => referenceStatusMap.get(ref.key)?.live_status === "FAIL")
    .map((ref) => ref.key);

  if (contextPacket.citation_status?.includes("BOUNDARY")) {
    riskFactors.push("boundary-sensitive citation context");
  }
  if (isHighBoundaryText(contextPacket.does_not_support)) {
    riskFactors.push("explicit does-not-support boundary");
  }
  if (warnedReferences.length) {
    riskFactors.push(`reference verification WARN: ${warnedReferences.join(", ")}`);
  }
  if (failedReferences.length) {
    riskFactors.push(`reference verification FAIL: ${failedReferences.join(", ")}`);
  }
  if (/延寿|寿命|健康寿命|死亡风险|永生|个体预测/gu.test(contextPacket.used_for || "")) {
    riskFactors.push("life-extension or mortality-adjacent use");
  }
  if (/AI|生成式|智能|模型|预测|诊断/giu.test(contextPacket.used_for || "")) {
    riskFactors.push("AI or prediction transfer risk");
  }

  let score = 0;
  score += contextPacket.citation_status?.includes("BOUNDARY") ? 2 : 0;
  score += isHighBoundaryText(contextPacket.does_not_support) ? 2 : 0;
  score += warnedReferences.length ? 2 : 0;
  score += failedReferences.length ? 5 : 0;
  score += /延寿|寿命|健康寿命|死亡风险|永生|个体预测/gu.test(contextPacket.used_for || "") ? 2 : 0;
  score += /AI|生成式|智能|模型|预测|诊断/giu.test(contextPacket.used_for || "") ? 1 : 0;

  const riskTier = failedReferences.length
    ? "BLOCKER"
    : score >= 6
      ? "HIGH"
      : score >= 3
        ? "MEDIUM"
        : "LOW";

  const requiredAction = riskTier === "BLOCKER"
    ? "Fix failed references before any submission path."
    : riskTier === "HIGH"
      ? "Fresh reviewer must inspect exact source-to-claim support and boundary wording."
      : riskTier === "MEDIUM"
        ? "Fresh reviewer should confirm the context is scoped and not overgeneralized."
        : "Fresh reviewer can sample after higher-risk contexts are resolved.";

  return {
    risk_tier: riskTier,
    risk_score: score,
    risk_factors: riskFactors.length ? riskFactors : ["low structural risk in local packet"],
    warned_references: warnedReferences,
    failed_references: failedReferences,
    required_action: requiredAction,
  };
}

function claimRiskTier(contextRows) {
  const ranks = { LOW: 1, MEDIUM: 2, HIGH: 3, BLOCKER: 4 };
  return contextRows.reduce((max, row) => (ranks[row.risk_tier] > ranks[max] ? row.risk_tier : max), "LOW");
}

function reviewerFocus(contextRow) {
  const focus = [
    "Check whether the source supports only the local usedFor statement, not the broader Human Infra theory.",
    "Check whether the does-not-support boundary is preserved in prose and figure captions.",
  ];
  if (contextRow.warned_references.length) {
    focus.push("Manually verify publisher or book page metadata because automated URL access returned WARN.");
  }
  if (contextRow.risk_factors.some((item) => item.includes("life-extension"))) {
    focus.push("Reject any upgrade from method, association, or framework language to concrete lifespan-extension evidence.");
  }
  if (contextRow.risk_factors.some((item) => item.includes("AI"))) {
    focus.push("Reject any upgrade from task-limited AI evidence to general intelligence, healthspan, or immortality benefit.");
  }
  return sortedUnique(focus);
}

function renderMarkdown(audit) {
  const contextRows = audit.details.context_triage
    .map((row) => `| ${row.context_id} | ${row.risk_tier} | ${row.risk_score} | ${row.claims.join(", ")} | ${row.references.length} | ${row.required_action.replace(/\|/gu, "\\|")} |`)
    .join("\n");

  const claimRows = audit.details.claim_triage
    .map((row) => `| ${row.claim_id} | ${row.risk_tier} | ${row.claim_type} | ${row.contexts.join(", ")} | ${row.required_action.replace(/\|/gu, "\\|")} |`)
    .join("\n");

  const detailedContexts = audit.details.context_triage
    .map((row) => `### ${row.context_id}: ${row.source_group}

- Risk tier: ${row.risk_tier}
- Risk score: ${row.risk_score}
- Claims: ${row.claims.join(", ")}
- References: ${row.references.join(", ")}
- Risk factors: ${row.risk_factors.join("; ")}
- Safe use: ${row.safe_use}
- Forbidden use: ${row.forbidden_use}
- Required action: ${row.required_action}
- Reviewer focus:
${row.reviewer_focus.map((item) => `  - ${item}`).join("\n")}
`)
    .join("\n");

  return `# Citation Context Risk Triage

Date: ${audit.generated_at}
Input: \`web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_REVIEW_PACKET.json\`
Output JSON: \`web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_RISK_TRIAGE.json\`

## Summary

Verdict: \`${audit.verdict}\`

Reason: \`${audit.reason_code}\`

${audit.summary}

This is a local structural risk triage. It does not replace fresh reviewer sentence-level citation-context judgment.

| Tier | Count |
| --- | ---: |
| BLOCKER | ${audit.details.counts.BLOCKER} |
| HIGH | ${audit.details.counts.HIGH} |
| MEDIUM | ${audit.details.counts.MEDIUM} |
| LOW | ${audit.details.counts.LOW} |

## Context Triage

| Context | Tier | Score | Claims | References | Required action |
| --- | --- | ---: | --- | ---: | --- |
${contextRows}

## Claim Triage

| Claim | Tier | Type | Contexts | Required action |
| --- | --- | --- | --- | --- |
${claimRows}

## Detailed Reviewer Queue

${detailedContexts}

## Scope

This triage ranks citation contexts by local overclaim risk, boundary sensitivity, reference verification WARN/FAIL state, and claim type. It does not read full source text and must not be cited as evidence that a reference supports a claim.
`;
}

const evidence = readJson(dataPath);
const packet = readJson(packetPath);
const referenceVerification = readJson(referenceVerificationPath);
const claimContextAudit = readJson(claimContextAuditPath);

const referenceStatusMap = statusByReference(referenceVerification.json);
const claimLookup = claimById(evidence.json);
const claimMapLookup = claimMapById(evidence.json);

const contextTriage = packet.json.details.context_packets.map((contextPacket) => {
  const risk = riskForContext(contextPacket, referenceStatusMap);
  return {
    context_id: contextPacket.context_id,
    source_group: contextPacket.source_group,
    claims: contextPacket.claims,
    references: contextPacket.references.map((ref) => ref.key),
    local_citation_status: contextPacket.citation_status,
    safe_use: contextPacket.supports,
    forbidden_use: contextPacket.does_not_support,
    reviewer_focus: reviewerFocus({ ...contextPacket, ...risk }),
    ...risk,
  };
});

const contextById = new Map(contextTriage.map((row) => [row.context_id, row]));
const claimTriage = (evidence.json.claimEvidenceMap || []).map((row) => {
  const claim = claimLookup.get(row.claimId) || {};
  const contexts = (row.citationContexts || []).map((contextId) => contextById.get(contextId)).filter(Boolean);
  const riskTier = claimRiskTier(contexts);
  const highContexts = contexts.filter((context) => ["HIGH", "BLOCKER"].includes(context.risk_tier)).map((context) => context.context_id);
  return {
    claim_id: row.claimId,
    claim_type: claim.claimType || "",
    alignment_verdict: row.alignmentVerdict,
    contexts: contexts.map((context) => context.context_id),
    risk_tier: riskTier,
    high_priority_contexts: highContexts,
    required_action: highContexts.length
      ? `Fresh reviewer should inspect high-priority contexts first: ${highContexts.join(", ")}.`
      : "No high-priority local risk context; keep standard fresh-review coverage.",
  };
});

const counts = { BLOCKER: 0, HIGH: 0, MEDIUM: 0, LOW: 0 };
for (const row of contextTriage) {
  counts[row.risk_tier] += 1;
}

const audit = {
  audit_skill: "citation-context-risk-triage",
  verdict: counts.BLOCKER > 0 ? "BLOCKED_BY_REFERENCE_FAILURE" : "REQUIRES_FRESH_REVIEW",
  reason_code: counts.BLOCKER > 0 ? "reference_failures_present" : "local_triage_ready_external_review_required",
  summary:
    "Citation contexts have been ranked for local overclaim and boundary risk so a fresh reviewer can prioritize exact source-to-claim verification.",
  generated_at: `${evidence.json.updated}T00:00:00.000Z`,
  audited_input_hashes: {
    "src/data/effective-immortality-evidence.json": sha256(evidence.content),
    "src/data/effective-immortality-flywheel/CITATION_CONTEXT_REVIEW_PACKET.json": sha256(packet.content),
    "src/data/effective-immortality-flywheel/REFERENCE_VERIFICATION.json": sha256(referenceVerification.content),
    "src/data/effective-immortality-flywheel/CLAIM_CONTEXT_AUDIT.json": sha256(claimContextAudit.content),
  },
  details: {
    schema_version: evidence.json.schemaVersion,
    claim_context_audit_verdict: claimContextAudit.json.verdict,
    reference_verification_verdict: referenceVerification.json.verdict,
    counts,
    context_triage: contextTriage,
    claim_triage: claimTriage,
  },
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(outputJsonPath, `${JSON.stringify(audit, null, 2)}\n`);
fs.writeFileSync(outputMdPath, renderMarkdown(audit));

console.log(`citation-context risk triage ${audit.verdict}`);
console.log(`blocker ${counts.BLOCKER}`);
console.log(`high ${counts.HIGH}`);
console.log(`medium ${counts.MEDIUM}`);
console.log(`low ${counts.LOW}`);
console.log(`wrote ${path.relative(webRoot, outputJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, outputMdPath)}`);

if (counts.BLOCKER > 0) {
  process.exitCode = 1;
}
