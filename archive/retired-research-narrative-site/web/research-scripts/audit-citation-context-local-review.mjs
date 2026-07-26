import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");
const dataPath = path.join(webRoot, "src/data/effective-immortality-evidence.json");
const packetPath = path.join(webRoot, "src/data/effective-immortality-flywheel/CITATION_CONTEXT_REVIEW_PACKET.json");
const riskPath = path.join(webRoot, "src/data/effective-immortality-flywheel/CITATION_CONTEXT_RISK_TRIAGE.json");
const highRiskPath = path.join(webRoot, "src/data/effective-immortality-flywheel/HIGH_RISK_CITATION_CONTEXT_REVIEW.json");
const referenceVerificationPath = path.join(webRoot, "src/data/effective-immortality-flywheel/REFERENCE_VERIFICATION.json");
const claimContextAuditPath = path.join(webRoot, "src/data/effective-immortality-flywheel/CLAIM_CONTEXT_AUDIT.json");
const outputDir = path.join(webRoot, "src/data/effective-immortality-flywheel");
const outputJsonPath = path.join(outputDir, "CITATION_CONTEXT_LOCAL_REVIEW.json");
const outputMdPath = path.join(outputDir, "CITATION_CONTEXT_LOCAL_REVIEW.md");

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function readJson(filePath) {
  const content = fs.readFileSync(filePath, "utf8");
  return { content, json: JSON.parse(content) };
}

function asMap(rows, key) {
  return new Map((rows || []).map((row) => [row[key], row]));
}

function sortedUnique(values) {
  return [...new Set(values.filter(Boolean))].sort((a, b) => a.localeCompare(b));
}

function localVerdict(contextPacket, riskRow, failedReferences) {
  if (failedReferences.length) {
    return "BLOCKED_BY_REFERENCE_FAILURE";
  }
  if (riskRow?.risk_tier === "HIGH" || riskRow?.risk_tier === "BLOCKER") {
    return "KEEP_WITH_STRICT_BOUNDARY";
  }
  if (riskRow?.risk_tier === "MEDIUM" || contextPacket.citation_status?.includes("BOUNDARY")) {
    return "KEEP_WITH_BOUNDARY";
  }
  return "KEEP_AS_METHOD_OR_FRAME_LANGUAGE";
}

function boundaryAction(verdict, riskRow) {
  if (verdict === "BLOCKED_BY_REFERENCE_FAILURE") {
    return "Fix failed references before the context can remain in the manuscript.";
  }
  if (verdict === "KEEP_WITH_STRICT_BOUNDARY") {
    return "Keep only the registered safe-use sentence. Fresh reviewer must inspect exact source-to-claim support before formal submission.";
  }
  if (verdict === "KEEP_WITH_BOUNDARY") {
    return "Keep the does-not-support boundary visible in prose, tables, and figure captions.";
  }
  return riskRow?.required_action || "Keep as background, method, or framework language only.";
}

function reviewerFocus(contextPacket, riskRow, failedReferences, warnedReferences) {
  const focus = [
    "确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。",
    "确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。",
  ];
  if (failedReferences.length) {
    focus.push(`先修复失败引用：${failedReferences.join(", ")}。`);
  }
  if (warnedReferences.length) {
    focus.push(`人工复核自动访问 WARN 的来源：${warnedReferences.join(", ")}。`);
  }
  if (riskRow?.risk_tier === "HIGH") {
    focus.push("优先检查是否把测量语言、规范语言或任务内效果外推成主体持续性、寿命或未来选择权结论。");
  }
  if (/寿命|死亡风险|永生|健康寿命/gu.test(contextPacket.used_for || "")) {
    focus.push("拒绝从方法、关联或指标语言直接跳到具体延寿效果。");
  }
  if (/AI|模型|预测|诊断/giu.test(contextPacket.used_for || "")) {
    focus.push("拒绝从任务内 AI 效果直接跳到通用能力增强、健康寿命收益或永生收益。");
  }
  return sortedUnique(focus);
}

function renderMarkdown(audit) {
  const contextRows = audit.details.context_reviews
    .map((row) => `| ${row.context_id} | ${row.risk_tier} | ${row.local_verdict} | ${row.claims.join(", ")} | ${row.references.length} | ${row.boundary_action.replace(/\|/gu, "\\|")} |`)
    .join("\n");

  const detailSections = audit.details.context_reviews
    .map((row) => {
      const referenceRows = row.references
        .map((ref) => `| \`${ref.key}\` | ${ref.audit_status} | ${ref.live_status} | ${ref.used_for.replace(/\|/gu, "\\|")} |`)
        .join("\n");
      return `### ${row.context_id}: ${row.source_group}

- Risk tier: ${row.risk_tier}
- Local verdict: ${row.local_verdict}
- Claims: ${row.claims.join(", ")}
- Used for: ${row.used_for}
- Safe use: ${row.safe_use}
- Forbidden use: ${row.forbidden_use}
- Boundary action: ${row.boundary_action}
- Fresh reviewer focus:
${row.fresh_reviewer_focus.map((item) => `  - ${item}`).join("\n")}

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
${referenceRows}
`;
    })
    .join("\n");

  return `# Citation Context Local Review

Date: ${audit.generated_at}
Input: \`web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_REVIEW_PACKET.json\`
Output JSON: \`web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_LOCAL_REVIEW.json\`

## Summary

Verdict: \`${audit.verdict}\`

Reason: \`${audit.reason_code}\`

${audit.summary}

This is a local source-boundary review for every registered citation context. It improves traceability and fresh-reviewer readiness, but it is not an independent sentence-level citation audit.

| Metric | Count |
| --- | ---: |
| Contexts | ${audit.details.context_count} |
| Reviewed contexts | ${audit.details.reviewed_context_count} |
| Blocked contexts | ${audit.details.blocked_context_count} |
| High-risk contexts with dedicated review | ${audit.details.high_risk_dedicated_review_count} |

## Context Review Table

| Context | Risk tier | Local verdict | Claims | References | Boundary action |
| --- | --- | --- | --- | ---: | --- |
${contextRows}

## Context Details

${detailSections}

## Scope

This artifact checks whether the manuscript has a registered safe-use boundary, forbidden-use boundary, reference list, reference verification state, and fresh-reviewer focus for each citation context. It does not prove the cited sources support every sentence in the manuscript. Formal submission still requires an independent fresh reviewer thread.
`;
}

const evidence = readJson(dataPath);
const packet = readJson(packetPath);
const risk = readJson(riskPath);
const highRisk = fs.existsSync(highRiskPath) ? readJson(highRiskPath) : null;
const referenceVerification = readJson(referenceVerificationPath);
const claimContextAudit = readJson(claimContextAuditPath);

const riskByContext = asMap(risk.json.details?.context_triage, "context_id");
const referenceStatusByKey = asMap(referenceVerification.json.details?.per_entry, "key");
const highRiskReviewedIds = new Set(
  (highRisk?.json.details?.reviewed_contexts || []).map((row) => row.context_id),
);

const contextReviews = (packet.json.details?.context_packets || []).map((contextPacket) => {
  const riskRow = riskByContext.get(contextPacket.context_id);
  const references = (contextPacket.references || []).map((ref) => {
    const status = referenceStatusByKey.get(ref.key) || {};
    return {
      key: ref.key,
      title: ref.title,
      audit_status: ref.audit_status,
      live_status: status.live_status || "UNKNOWN",
      verification_method: status.method || "UNKNOWN",
      used_for: ref.used_for,
    };
  });
  const failedReferences = references.filter((ref) => ref.live_status === "FAIL").map((ref) => ref.key);
  const warnedReferences = references.filter((ref) => ref.live_status === "WARN").map((ref) => ref.key);
  const verdict = localVerdict(contextPacket, riskRow, failedReferences);

  return {
    context_id: contextPacket.context_id,
    source_group: contextPacket.source_group,
    risk_tier: riskRow?.risk_tier || "UNKNOWN",
    risk_score: riskRow?.risk_score ?? null,
    claims: contextPacket.claims || [],
    references,
    used_for: contextPacket.used_for,
    safe_use: contextPacket.supports,
    forbidden_use: contextPacket.does_not_support,
    local_verdict: verdict,
    boundary_action: boundaryAction(verdict, riskRow),
    fresh_reviewer_focus: reviewerFocus(contextPacket, riskRow, failedReferences, warnedReferences),
    dedicated_high_risk_review: highRiskReviewedIds.has(contextPacket.context_id),
  };
});

const blockedContexts = contextReviews.filter((row) => row.local_verdict === "BLOCKED_BY_REFERENCE_FAILURE");
const allContextsReviewed = contextReviews.length === (packet.json.details?.context_count || contextReviews.length);
const audit = {
  audit_skill: "citation-context-local-review",
  verdict: blockedContexts.length
    ? "BLOCKED_BY_REFERENCE_FAILURE"
    : allContextsReviewed
      ? "LOCAL_REVIEW_COMPLETE_REQUIRES_FRESH_REVIEW"
      : "INCOMPLETE",
  reason_code: blockedContexts.length
    ? "reference_failures_present"
    : allContextsReviewed
      ? "all_contexts_have_local_source_boundaries"
      : "context_review_count_mismatch",
  summary: blockedContexts.length
    ? "At least one citation context has failed references and cannot pass the local review gate."
    : "All registered citation contexts have local safe-use, forbidden-use, reference-state, and fresh-reviewer focus records. Fresh independent sentence-level citation review remains required before formal submission.",
  generated_at: `${evidence.json.updated}T00:00:00.000Z`,
  audited_input_hashes: {
    "src/data/effective-immortality-evidence.json": sha256(evidence.content),
    "src/data/effective-immortality-flywheel/CITATION_CONTEXT_REVIEW_PACKET.json": sha256(packet.content),
    "src/data/effective-immortality-flywheel/CITATION_CONTEXT_RISK_TRIAGE.json": sha256(risk.content),
    "src/data/effective-immortality-flywheel/REFERENCE_VERIFICATION.json": sha256(referenceVerification.content),
    "src/data/effective-immortality-flywheel/CLAIM_CONTEXT_AUDIT.json": sha256(claimContextAudit.content),
    ...(highRisk ? { "src/data/effective-immortality-flywheel/HIGH_RISK_CITATION_CONTEXT_REVIEW.json": sha256(highRisk.content) } : {}),
  },
  details: {
    schema_version: evidence.json.schemaVersion,
    claim_context_audit_verdict: claimContextAudit.json.verdict,
    reference_verification_verdict: referenceVerification.json.verdict,
    citation_context_risk_triage_verdict: risk.json.verdict,
    high_risk_review_verdict: highRisk?.json.verdict || "MISSING",
    context_count: packet.json.details?.context_count || contextReviews.length,
    reviewed_context_count: contextReviews.length,
    blocked_context_count: blockedContexts.length,
    high_risk_dedicated_review_count: contextReviews.filter((row) => row.dedicated_high_risk_review).length,
    context_reviews: contextReviews,
    fresh_reviewer_required: true,
  },
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(outputJsonPath, `${JSON.stringify(audit, null, 2)}\n`);
fs.writeFileSync(outputMdPath, renderMarkdown(audit));

console.log(`citation-context local review ${audit.verdict}`);
console.log(`contexts ${audit.details.context_count}`);
console.log(`reviewed ${audit.details.reviewed_context_count}`);
console.log(`blocked ${audit.details.blocked_context_count}`);
console.log(`wrote ${path.relative(webRoot, outputJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, outputMdPath)}`);

if (blockedContexts.length || !allContextsReviewed) {
  process.exitCode = 1;
}
