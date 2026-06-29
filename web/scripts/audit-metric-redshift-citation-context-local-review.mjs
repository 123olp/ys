import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");

const dataPath = path.join(webRoot, "src/data/metric-redshift-recursive-waiting.json");
const packetPath = path.join(webRoot, "src/data/metric-redshift-recursive-waiting/CITATION_CONTEXT_REVIEW_PACKET.json");
const outputDir = path.join(webRoot, "src/data/metric-redshift-recursive-waiting");
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
  if (/人体|工程|返航|制造|可行性|生命支持|安全承诺/u.test(text)) {
    return "HIGH";
  }
  if (/黑洞|malament|hogarth|无限未来|事件视界|强引力/u.test(text)) {
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
    "检查摘要、图注和表格是否暗示了超出来源边界的结论。",
  ];
  if (tier === "HIGH") {
    focus.push("优先检查是否把概念、科普或边界文献升级为工程可行性、人体等待或安全承诺。");
  }
  if (/nasa/iu.test(context.sourceKeys.join(" "))) {
    focus.push("NASA 公共材料只能作为直觉和风险边界，不能作为任务设计或生命支持证据。");
  }
  if (/malament|hogarth/iu.test(`${context.context} ${context.sourceKeys.join(" ")}`)) {
    focus.push("Malament-Hogarth 来源只能用于极限时空和概念边界，不能支持普通黑洞等待室工程。");
  }
  return [...new Set(focus)];
}

function renderMarkdown(audit) {
  const rows = audit.details.contextReviews
    .map((row) => `| ${row.contextId} | ${row.riskTier} | ${row.localVerdict} | ${row.claimIds.join(", ")} | ${row.sourceKeys.join(", ")} |`)
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

  return `# Metric Redshift Citation Context Local Review

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
    sourceKeys: context.sourceKeys,
    safeUse: context.safeUse,
    forbiddenUse: context.forbiddenUse,
    freshReviewerFocus: reviewerFocus(context, tier),
  };
});

const missingContexts = (data.json.citationContextRegister || [])
  .map((context) => context.id)
  .filter((contextId) => !contextReviews.some((row) => row.contextId === contextId));

const findings = missingContexts.map((contextId) => ({
  severity: "fail",
  code: "missing-context-local-review",
  message: `${contextId} has no local review row.`,
}));

const verdict = findings.some((finding) => finding.severity === "fail")
  ? "FAIL"
  : "LOCAL_REVIEW_COMPLETE_REQUIRES_FRESH_REVIEW";

const audit = {
  audit: "metric-redshift-citation-context-local-review",
  verdict,
  reasonCode: verdict === "FAIL" ? "missing_context_rows" : "all_contexts_have_local_boundaries",
  summary:
    verdict === "FAIL"
      ? "At least one citation context is missing local boundary review."
      : "All registered MRW citation contexts have a local safe-use, forbidden-use, risk-tier, and fresh-reviewer focus record. Independent external citation review remains required.",
  generatedAt: new Date().toISOString(),
  auditedInputHashes: {
    "src/data/metric-redshift-recursive-waiting.json": sha256(data.content),
    "src/data/metric-redshift-recursive-waiting/CITATION_CONTEXT_REVIEW_PACKET.json": sha256(packet.content),
  },
  details: {
    contextCount: (data.json.citationContextRegister || []).length,
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
fs.writeFileSync(outputJsonPath, `${JSON.stringify(audit, null, 2)}\n`);
fs.writeFileSync(outputMdPath, renderMarkdown(audit));

console.log(`metric-redshift citation context local review verdict ${verdict}`);
console.log(`contexts ${audit.details.contextCount}`);
console.log(`reviewed ${audit.details.reviewedContextCount}`);
console.log(`findings ${findings.length}`);
console.log(`wrote ${path.relative(webRoot, outputJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, outputMdPath)}`);

if (verdict === "FAIL") {
  process.exitCode = 1;
}
