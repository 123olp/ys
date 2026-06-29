import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");

const dataPath = path.join(webRoot, "src/data/controllable-metric-waiting-room-hypothesis.json");
const packetPath = path.join(webRoot, "src/data/controllable-metric-waiting-room-hypothesis/CITATION_CONTEXT_REVIEW_PACKET.json");
const outputDir = path.join(webRoot, "src/data/controllable-metric-waiting-room-hypothesis");
const outputJsonPath = path.join(outputDir, "CITATION_CONTEXT_LOCAL_REVIEW.json");
const outputMdPath = path.join(outputDir, "CITATION_CONTEXT_LOCAL_REVIEW.md");

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function readJson(filePath) {
  const content = fs.readFileSync(filePath, "utf8");
  return { content, json: JSON.parse(content) };
}

function riskTier(context) {
  const text = `${context.context} ${context.safeUse} ${context.forbiddenUse}`.toLowerCase();
  if (/人工黑洞|强引力工程|人体|安全承诺|工程|个体|永生|可部署|制造|重力控制/u.test(text)) {
    return "HIGH";
  }
  if (/黑洞|malament|hogarth|固有时|度规|nasa|无限未来|事件视界|强引力/u.test(text)) {
    return "MEDIUM";
  }
  return "LOW";
}

function localVerdict(tier) {
  if (tier === "HIGH") {
    return "KEEP_WITH_STRICT_BOUNDARY_REQUIRES_FRESH_REVIEW";
  }
  if (tier === "MEDIUM") {
    return "KEEP_WITH_BOUNDARY_REQUIRES_FRESH_REVIEW";
  }
  return "KEEP_AS_BACKGROUND_REQUIRES_FRESH_REVIEW";
}

function reviewerFocus(context, tier) {
  const focus = [
    "确认来源只支持 safe use，不支持 forbidden use。",
    "检查摘要、图注、公式、表格和模型段是否暗示了超出来源边界的结论。",
  ];
  const sourceText = context.sources
    .map((source) => `${source.author} ${source.title} ${source.url}`)
    .join(" ")
    .toLowerCase();

  if (tier === "HIGH") {
    focus.push("优先检查是否把概念、科普或边界文献升级为人工黑洞、强引力工程、人体等待、安全承诺或个体方案。");
  }
  if (/nasa/iu.test(sourceText)) {
    focus.push("NASA 公共材料只能作为传播层解释和风险直觉，不能作为任务设计、生命支持或工程制造证据。");
  }
  if (/malament|hogarth/iu.test(sourceText)) {
    focus.push("Malament-Hogarth 来源只能用于极限时空和概念谱系，不能支持现实可部署等待室。");
  }
  if (/arxiv\.org\/abs\/1203\.4000/iu.test(sourceText)) {
    focus.push("Zaslavskii 2012 应主要用于限制和反证普通黑洞未来观察叙事，而不是支持可行性叙事。");
  }
  if (/effective-immortality-flywheel/iu.test(sourceText)) {
    focus.push("Human Infra 内部页面只能支持项目模型接口，不能替代外部物理、医学或工程证据。");
  }
  return [...new Set(focus)];
}

function renderMarkdown(audit) {
  const rows = audit.details.contextReviews
    .map((row) => `| ${row.contextId} | ${row.riskTier} | ${row.localVerdict} | ${row.claimIds.join(", ")} | ${row.sourceIds.join(", ")} |`)
    .join("\n");

  const sections = audit.details.contextReviews
    .map((row) => `### ${row.contextId}

- Risk tier: ${row.riskTier}
- Local verdict: ${row.localVerdict}
- Safe use: ${row.safeUse}
- Forbidden use: ${row.forbiddenUse}
- Fresh reviewer focus:
${row.freshReviewerFocus.map((item) => `  - ${item}`).join("\n")}
`)
    .join("\n");

  return `# Controllable Metric Waiting Room Citation Context Local Review

**Generated**: ${audit.generatedAt}
**Verdict**: ${audit.verdict}

${audit.summary}

This is a local boundary review. It is not an independent external citation verdict.

## Context Table

| Context | Risk tier | Local verdict | Claims | Sources |
| --- | --- | --- | --- | --- |
${rows}

## Context Details

${sections}
`;
}

const data = readJson(dataPath);
const packet = readJson(packetPath);
const contextPackets = packet.json.details?.contextPackets || [];

const contextReviews = contextPackets.map((context) => {
  const tier = riskTier(context);
  return {
    contextId: context.id,
    riskTier: tier,
    localVerdict: localVerdict(tier),
    claimIds: context.claimIds,
    sourceIds: context.sourceIds,
    safeUse: context.safeUse,
    forbiddenUse: context.forbiddenUse,
    freshReviewerFocus: reviewerFocus(context, tier),
  };
});

const registeredContextIds = new Set((data.json.citationContextRows || []).map((row) => row[0]));
const reviewedContextIds = new Set(contextReviews.map((row) => row.contextId));
const findings = [];

for (const contextId of registeredContextIds) {
  if (!reviewedContextIds.has(contextId)) {
    findings.push({
      severity: "fail",
      code: "missing-context-local-review",
      message: `${contextId} has no local review row.`,
    });
  }
}

for (const context of contextReviews) {
  if (!registeredContextIds.has(context.contextId)) {
    findings.push({
      severity: "fail",
      code: "unknown-context-local-review",
      message: `${context.contextId} is not registered in citationContextRows.`,
    });
  }
  if (context.riskTier === "HIGH" && !context.localVerdict.includes("STRICT_BOUNDARY")) {
    findings.push({
      severity: "fail",
      code: "high-risk-context-without-strict-boundary",
      message: `${context.contextId} is HIGH risk but lacks a strict-boundary verdict.`,
    });
  }
}

const verdict = findings.some((finding) => finding.severity === "fail")
  ? "FAIL"
  : "LOCAL_REVIEW_COMPLETE_REQUIRES_FRESH_REVIEW";

const audit = {
  audit: "controllable-metric-waiting-room-citation-context-local-review",
  verdict,
  reasonCode: verdict === "FAIL" ? "missing_or_invalid_context_rows" : "all_contexts_have_local_boundaries",
  summary:
    verdict === "FAIL"
      ? "At least one controllable metric waiting room citation context is missing or has invalid local boundary review."
      : "All registered controllable metric waiting room citation contexts have a local safe-use, forbidden-use, risk-tier, and fresh-reviewer focus record. Independent external citation review remains required.",
  generatedAt: new Date().toISOString(),
  auditedInputHashes: {
    "src/data/controllable-metric-waiting-room-hypothesis.json": sha256(data.content),
    "src/data/controllable-metric-waiting-room-hypothesis/CITATION_CONTEXT_REVIEW_PACKET.json": sha256(packet.content),
  },
  details: {
    contextCount: registeredContextIds.size,
    reviewedContextCount: contextReviews.length,
    riskTierCounts: contextReviews.reduce((acc, row) => {
      acc[row.riskTier] = (acc[row.riskTier] || 0) + 1;
      return acc;
    }, {}),
    contextReviews,
  },
  findings,
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(outputJsonPath, `${JSON.stringify(audit, null, 2)}\n`, "utf8");
fs.writeFileSync(outputMdPath, renderMarkdown(audit), "utf8");

console.log(`controllable metric waiting room citation context local review verdict ${verdict}`);
console.log(`contexts ${audit.details.contextCount}`);
console.log(`reviewed ${audit.details.reviewedContextCount}`);
console.log(`findings ${findings.length}`);
console.log(`wrote ${path.relative(webRoot, outputJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, outputMdPath)}`);

if (verdict === "FAIL") {
  process.exitCode = 1;
}
