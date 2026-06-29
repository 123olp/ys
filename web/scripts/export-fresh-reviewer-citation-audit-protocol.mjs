import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");
const dataPath = path.join(webRoot, "src/data/effective-immortality-evidence.json");
const outputDir = path.join(webRoot, "src/data/effective-immortality-flywheel");

const packetPath = path.join(outputDir, "CITATION_CONTEXT_REVIEW_PACKET.json");
const riskPath = path.join(outputDir, "CITATION_CONTEXT_RISK_TRIAGE.json");
const localReviewPath = path.join(outputDir, "CITATION_CONTEXT_LOCAL_REVIEW.json");
const highRiskPath = path.join(outputDir, "HIGH_RISK_CITATION_CONTEXT_REVIEW.json");
const referenceVerificationPath = path.join(outputDir, "REFERENCE_VERIFICATION.json");
const citationAuditPath = path.join(outputDir, "CITATION_AUDIT.json");

const outputJsonPath = path.join(outputDir, "FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json");
const outputMdPath = path.join(outputDir, "FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.md");

const riskOrder = {
  BLOCKER: 0,
  HIGH: 1,
  MEDIUM: 2,
  LOW: 3,
  UNKNOWN: 4,
};

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

function unique(values) {
  return [...new Set(values.filter(Boolean))];
}

function contextNumber(contextId) {
  const match = /^CTX(\d+)$/u.exec(contextId);
  return match ? Number(match[1]) : Number.MAX_SAFE_INTEGER;
}

function sortQueue(a, b) {
  const tierDelta = (riskOrder[a.risk_tier] ?? riskOrder.UNKNOWN) - (riskOrder[b.risk_tier] ?? riskOrder.UNKNOWN);
  if (tierDelta) return tierDelta;
  const scoreDelta = (b.risk_score ?? 0) - (a.risk_score ?? 0);
  if (scoreDelta) return scoreDelta;
  return contextNumber(a.context_id) - contextNumber(b.context_id);
}

function buildReviewerQuestions(contextPacket, riskRow, localRow) {
  const base = [
    "该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？",
    "该来源是否支持 safe use 中登记的最小用途？",
    "当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？",
    "如果只支持部分用途，需要把哪一句改成更弱表述？",
  ];
  if (riskRow?.risk_tier === "HIGH" || riskRow?.risk_tier === "BLOCKER") {
    base.push("高风险检查：是否把指标、机制、治理、任务内效果或预测语言外推为永生、寿命收益或飞轮成立的实证证据？");
  }
  if ((localRow?.warned_references || []).length) {
    base.push(`人工检查自动访问 WARN 的来源：${localRow.warned_references.join(", ")}。`);
  }
  if ((localRow?.failed_references || []).length) {
    base.push(`先处理失败来源，不得在失败来源修复前通过该语境：${localRow.failed_references.join(", ")}。`);
  }
  return unique([...(localRow?.fresh_reviewer_focus || []), ...(localRow?.reviewer_focus || []), ...base]);
}

function buildReviewPrompt(queueRow) {
  const refs = queueRow.references
    .map((ref) => `- ${ref.key}: ${ref.title || ref.used_for || "registered reference"} (${ref.audit_status}; ${ref.live_status || "UNKNOWN"})`)
    .join("\n");

  return `你是独立引用语境审稿人。不要使用项目作者的本地结论作为证据，必须重新打开来源并检查正文语境。

Context: ${queueRow.context_id}
Source group: ${queueRow.source_group}
Risk: ${queueRow.risk_tier} / score ${queueRow.risk_score}
Claims: ${queueRow.claims.join(", ")}
Used for: ${queueRow.used_for}
Safe use: ${queueRow.safe_use}
Forbidden use: ${queueRow.forbidden_use}

References:
${refs}

请逐项输出：
1. reference_existence: PASS / FAIL / UNCERTAIN，并给出核验 URL。
2. safe_use_support: SUPPORTS / WEAK / WRONG，并说明来源文本如何支持或不支持。
3. forbidden_use_violation: NONE / POSSIBLE / PRESENT。
4. required_action: KEEP / SOFTEN / REWRITE / REMOVE / REPLACE_SOURCE。
5. one_sentence_reason: 一句话说明 verdict。`;
}

function renderMarkdown(protocol) {
  const queueRows = protocol.details.review_queue
    .map((row) => `| ${row.priority} | ${row.context_id} | ${row.risk_tier} | ${row.risk_score} | ${row.source_group.replace(/\|/gu, "\\|")} | ${row.claims.join(", ")} | ${row.required_action_before_submission} |`)
    .join("\n");

  const detailSections = protocol.details.review_queue
    .map((row) => {
      const refs = row.references
        .map((ref) => `| \`${ref.key}\` | ${ref.audit_status} | ${ref.live_status || "UNKNOWN"} | ${ref.used_for.replace(/\|/gu, "\\|")} |`)
        .join("\n");
      const questions = row.reviewer_questions.map((question) => `  - ${question}`).join("\n");
      return `### ${row.priority}. ${row.context_id}: ${row.source_group}

- Risk tier: ${row.risk_tier}
- Risk score: ${row.risk_score}
- Claims: ${row.claims.join(", ")}
- Used for: ${row.used_for}
- Safe use: ${row.safe_use}
- Forbidden use: ${row.forbidden_use}
- Local review verdict: ${row.local_verdict}
- Required action before submission: ${row.required_action_before_submission}

Reviewer questions:
${questions}

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
${refs}

Suggested fresh-reviewer prompt:

\`\`\`text
${row.reviewer_prompt}
\`\`\`
`;
    })
    .join("\n");

  return `# Fresh Reviewer Citation Audit Protocol

Date: ${protocol.generated_at}
Output JSON: \`web/src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json\`

## Summary

Verdict: \`${protocol.verdict}\`

Reason: \`${protocol.reason_code}\`

${protocol.summary}

This protocol does not clear the citation-audit warning. It turns the remaining independent sentence-level citation-context review into an executable queue.

| Metric | Count |
| --- | ---: |
| Contexts in queue | ${protocol.details.context_count} |
| High or blocker contexts | ${protocol.details.high_or_blocker_count} |
| Medium contexts | ${protocol.details.medium_count} |
| Low contexts | ${protocol.details.low_count} |

## Reviewer Independence Contract

- Use a fresh reviewer thread or a reviewer with no prior exposure to this paper's local conclusions.
- Re-open source pages or PDFs; do not rely on memory or the local review artifacts as proof.
- Check existence, metadata, and exact claim-to-source fit.
- Treat wrong-context support as more serious than metadata drift.
- Keep source-boundary language: a method source cannot become evidence for effective immortality.

## Pass Gate

- Every row in the queue must receive a reviewer verdict.
- No row may remain \`WRONG\`, \`PRESENT\`, \`REMOVE\`, or \`REPLACE_SOURCE\` before formal submission.
- Every \`WEAK\` or \`POSSIBLE\` row must trigger a prose downgrade, boundary strengthening, or citation replacement.
- High-risk contexts must be resolved before medium and low contexts are treated as clean.
- The final audit trace must record reviewer identity class, source URLs, verdicts, and required text changes.

## Review Queue

| Priority | Context | Risk tier | Score | Source group | Claims | Required action |
| ---: | --- | --- | ---: | --- | --- | --- |
${queueRows}

## Context Protocol

${detailSections}
`;
}

const evidence = readJson(dataPath);
const packet = readJson(packetPath);
const risk = readJson(riskPath);
const localReview = readJson(localReviewPath);
const highRisk = readJson(highRiskPath);
const referenceVerification = readJson(referenceVerificationPath);
const citationAudit = readJson(citationAuditPath);

const riskByContext = asMap(risk.json.details?.context_triage, "context_id");
const localByContext = asMap(localReview.json.details?.context_reviews, "context_id");
const referenceStatusByKey = asMap(referenceVerification.json.details?.per_entry, "key");
const highRiskReviewedIds = new Set((highRisk.json.details?.reviewed_contexts || []).map((row) => row.context_id));

const reviewQueue = (packet.json.details?.context_packets || [])
  .map((contextPacket) => {
    const riskRow = riskByContext.get(contextPacket.context_id) || {};
    const localRow = localByContext.get(contextPacket.context_id) || {};
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
    const row = {
      context_id: contextPacket.context_id,
      source_group: contextPacket.source_group,
      risk_tier: riskRow.risk_tier || "UNKNOWN",
      risk_score: riskRow.risk_score ?? null,
      claims: contextPacket.claims || [],
      references,
      used_for: contextPacket.used_for,
      safe_use: contextPacket.supports,
      forbidden_use: contextPacket.does_not_support,
      local_verdict: localRow.local_verdict || localRow.local_citation_status || "UNKNOWN",
      dedicated_high_risk_review: highRiskReviewedIds.has(contextPacket.context_id),
      reviewer_questions: buildReviewerQuestions(contextPacket, riskRow, localRow),
      required_action_before_submission: riskRow.risk_tier === "HIGH" || riskRow.risk_tier === "BLOCKER"
        ? "Resolve before any submission-facing claim can be treated as clean."
        : "Review after high-risk contexts; keep registered boundary language.",
    };
    return { ...row, reviewer_prompt: buildReviewPrompt(row) };
  })
  .sort(sortQueue)
  .map((row, index) => ({ priority: index + 1, ...row }));

const counts = reviewQueue.reduce(
  (acc, row) => {
    if (row.risk_tier === "HIGH" || row.risk_tier === "BLOCKER") acc.high_or_blocker_count += 1;
    if (row.risk_tier === "MEDIUM") acc.medium_count += 1;
    if (row.risk_tier === "LOW") acc.low_count += 1;
    return acc;
  },
  { high_or_blocker_count: 0, medium_count: 0, low_count: 0 },
);

const protocol = {
  audit_skill: "fresh-reviewer-citation-audit-protocol",
  verdict: "READY_FOR_FRESH_REVIEWER",
  reason_code: "external_sentence_level_review_protocol_exported",
  summary: "The citation-context queue, reviewer independence contract, pass gate, and per-context prompts are ready for an external fresh reviewer. This artifact does not replace the reviewer run.",
  generated_at: `${evidence.json.updated}T00:00:00.000Z`,
  audited_input_hashes: {
    "src/data/effective-immortality-evidence.json": sha256(evidence.content),
    "src/data/effective-immortality-flywheel/CITATION_CONTEXT_REVIEW_PACKET.json": sha256(packet.content),
    "src/data/effective-immortality-flywheel/CITATION_CONTEXT_RISK_TRIAGE.json": sha256(risk.content),
    "src/data/effective-immortality-flywheel/CITATION_CONTEXT_LOCAL_REVIEW.json": sha256(localReview.content),
    "src/data/effective-immortality-flywheel/HIGH_RISK_CITATION_CONTEXT_REVIEW.json": sha256(highRisk.content),
    "src/data/effective-immortality-flywheel/REFERENCE_VERIFICATION.json": sha256(referenceVerification.content),
    "src/data/effective-immortality-flywheel/CITATION_AUDIT.json": sha256(citationAudit.content),
  },
  details: {
    schema_version: evidence.json.schemaVersion,
    citation_audit_verdict: citationAudit.json.verdict,
    citation_audit_reason_code: citationAudit.json.reason_code,
    citation_context_risk_triage_verdict: risk.json.verdict,
    citation_context_local_review_verdict: localReview.json.verdict,
    context_count: reviewQueue.length,
    ...counts,
    reviewer_independence_contract: [
      "Fresh thread or independent reviewer required.",
      "Web or primary-source lookup required for every reviewed context.",
      "Local review artifacts are allowed only as a queue and boundary map, not as evidence of support.",
      "Every context verdict must include source URL or retrieval note.",
    ],
    verdict_schema: {
      reference_existence: ["PASS", "FAIL", "UNCERTAIN"],
      safe_use_support: ["SUPPORTS", "WEAK", "WRONG"],
      forbidden_use_violation: ["NONE", "POSSIBLE", "PRESENT"],
      required_action: ["KEEP", "SOFTEN", "REWRITE", "REMOVE", "REPLACE_SOURCE"],
    },
    blocking_conditions: [
      "Any FAIL or UNCERTAIN reference existence verdict without manual resolution.",
      "Any WRONG safe-use support verdict.",
      "Any PRESENT forbidden-use violation.",
      "Any required_action of REMOVE or REPLACE_SOURCE unresolved in manuscript text.",
    ],
    review_queue: reviewQueue,
  },
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(outputJsonPath, `${JSON.stringify(protocol, null, 2)}\n`);
fs.writeFileSync(outputMdPath, renderMarkdown(protocol));

console.log(`fresh reviewer citation audit protocol ${protocol.verdict}`);
console.log(`contexts ${protocol.details.context_count}`);
console.log(`high_or_blocker ${protocol.details.high_or_blocker_count}`);
console.log(`medium ${protocol.details.medium_count}`);
console.log(`low ${protocol.details.low_count}`);
console.log(`wrote ${path.relative(webRoot, outputJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, outputMdPath)}`);
