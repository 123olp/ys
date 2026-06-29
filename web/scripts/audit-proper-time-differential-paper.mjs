import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");

const pagePath = path.join(webRoot, "src/pages/papers/proper-time-differential-waiting-hypothesis.astro");
const dataPath = path.join(webRoot, "src/data/proper-time-differential-waiting-hypothesis.json");
const outputDir = path.join(webRoot, "src/data/proper-time-differential-waiting-hypothesis");
const toolSeedPath = path.join(outputDir, "TOOL_GENERATED_PAGE_SEED.astro");
const citationPacketJsonPath = path.join(outputDir, "CITATION_CONTEXT_REVIEW_PACKET.json");
const citationPacketMdPath = path.join(outputDir, "CITATION_CONTEXT_REVIEW_PACKET.md");
const citationLocalReviewJsonPath = path.join(outputDir, "CITATION_CONTEXT_LOCAL_REVIEW.json");
const citationLocalReviewMdPath = path.join(outputDir, "CITATION_CONTEXT_LOCAL_REVIEW.md");
const referenceVerificationJsonPath = path.join(outputDir, "REFERENCE_VERIFICATION.json");
const referenceVerificationMdPath = path.join(outputDir, "REFERENCE_VERIFICATION.md");
const preSubmissionReviewJsonPath = path.join(outputDir, "PRE_SUBMISSION_REVIEW.json");
const preSubmissionReviewMdPath = path.join(outputDir, "PRE_SUBMISSION_REVIEW.md");
const auditJsonPath = path.join(outputDir, "COVERAGE_AUDIT.json");
const auditMdPath = path.join(outputDir, "COVERAGE_AUDIT.md");

function pushFinding(findings, severity, code, message) {
  findings.push({ severity, code, message });
}

function countPattern(text, pattern) {
  return [...text.matchAll(pattern)].length;
}

function listMissing(text, required) {
  return required.filter((item) => !text.includes(item));
}

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function assertArrayRows(findings, name, value, minimumCount) {
  if (!Array.isArray(value)) {
    pushFinding(findings, "fail", "data-collection-not-array", `${name} must be an array.`);
    return 0;
  }

  if (value.length < minimumCount) {
    pushFinding(findings, "fail", "data-collection-count-low", `${name} expected at least ${minimumCount} rows, found ${value.length}.`);
  }

  for (const [index, row] of value.entries()) {
    if (!Array.isArray(row) || row.some((cell) => typeof cell !== "string" || cell.trim() === "")) {
      pushFinding(findings, "fail", "data-row-invalid", `${name}[${index}] must be a non-empty string tuple.`);
    }
  }

  return value.length;
}

function checkUniqueIds(findings, name, rows) {
  const seen = new Set();
  for (const row of rows) {
    const id = row[0];
    if (seen.has(id)) {
      pushFinding(findings, "fail", "duplicate-data-id", `${name} has duplicate id: ${id}`);
    }
    seen.add(id);
  }
  return seen;
}

function parseSourceIds(sourceText) {
  return sourceText
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

const page = fs.readFileSync(pagePath, "utf8");
const data = readJson(dataPath);
const seed = fs.existsSync(toolSeedPath) ? fs.readFileSync(toolSeedPath, "utf8") : "";
const findings = [];

const requiredPageStrings = data.auditContract?.requiredPageStrings ?? [];
const minimumCounts = data.auditContract?.minimumCounts ?? {};
const dataCollections = {
  conceptRows: data.conceptRows,
  hypothesisRows: data.hypothesisRows,
  contributionRows: data.contributionRows,
  stateRows: data.stateRows,
  modelRows: data.modelRows,
  ladderRows: data.ladderRows,
  falsifierRows: data.falsifierRows,
  protocolRows: data.protocolRows,
  sourceCardRows: data.sourceCardRows,
  claimEvidenceRows: data.claimEvidenceRows,
  scenarioRows: data.scenarioRows,
  scenarioEvaluationRows: data.scenarioEvaluationRows,
  qualitativeNcgScaleRows: data.qualitativeNcgScaleRows,
  scenarioVariableRows: data.scenarioVariableRows,
  toyNcgProtocolRows: data.toyNcgProtocolRows,
  ncgFormulaBlockRows: data.ncgFormulaBlockRows,
  figurePlanRows: data.figurePlanRows,
  citationBoundaryRows: data.citationBoundaryRows,
  citationContextRows: data.citationContextRows,
  preSubmissionReviewRows: data.preSubmissionReviewRows,
  referenceRows: data.referenceRows,
};

const requiredSections = Array.from({ length: 15 }, (_, index) => `id="S${index + 1}"`);
const requiredTocAnchors = Array.from({ length: 15 }, (_, index) => `href="#S${index + 1}"`);
const requiredReferenceUrls = (data.referenceRows ?? []).map((row) => row[2]);

const missingStrings = listMissing(page, requiredPageStrings);
for (const missing of missingStrings) {
  pushFinding(findings, "fail", "required-string-missing", `Page missing required string: ${missing}`);
}

const collectionCounts = {};
for (const [name, rows] of Object.entries(dataCollections)) {
  collectionCounts[name] = assertArrayRows(findings, name, rows, minimumCounts[name] ?? 1);
  if (!page.includes(`${name}.map`)) {
    pushFinding(findings, "fail", "data-collection-not-rendered", `Page does not render ${name} with a map expression.`);
  }
}

if (!page.includes("proper-time-differential-waiting-hypothesis.json")) {
  pushFinding(findings, "fail", "data-source-import-missing", "Page must import the structured JSON data source.");
}

for (const missing of listMissing(page, requiredSections)) {
  pushFinding(findings, "fail", "section-missing", `Page missing section marker: ${missing}`);
}

for (const missing of listMissing(page, requiredTocAnchors)) {
  pushFinding(findings, "fail", "toc-anchor-missing", `TOC missing anchor: ${missing}`);
}

for (const url of requiredReferenceUrls) {
  if (typeof url !== "string" || url.trim() === "") {
    pushFinding(findings, "fail", "reference-url-invalid", `Reference URL must be a non-empty string: ${url}`);
  }
}

if (!seed.includes("This tool-generated seed is retained")) {
  pushFinding(findings, "fail", "tool-seed-missing", "Tool-generated page seed is missing or does not contain the expected marker.");
}

const sectionCount = countPattern(page, /<section id="S\d+"/gu);
if (sectionCount < 15) {
  pushFinding(findings, "fail", "section-count-low", `Expected at least 15 sections, found ${sectionCount}.`);
}

const tocCount = countPattern(page, /ltx_tocentry_section/gu);
if (tocCount < 15) {
  pushFinding(findings, "fail", "toc-count-low", `Expected at least 15 TOC section entries, found ${tocCount}.`);
}

if (!page.includes('id="F4"')) {
  pushFinding(findings, "fail", "scenario-comparison-figure-missing", "Page must render Figure 4 as the NCG scenario comparison figure.");
}

if (!page.includes('id="scenario-ncg-matrix-svg"')) {
  pushFinding(findings, "fail", "scenario-comparison-svg-missing", "Figure 4 must include the data-driven scenario-ncg-matrix-svg element.");
}

const sourceCardCount = collectionCounts.sourceCardRows ?? 0;
const claimEvidenceCount = collectionCounts.claimEvidenceRows ?? 0;
const scenarioCount = collectionCounts.scenarioRows ?? 0;
const scenarioEvaluationCount = collectionCounts.scenarioEvaluationRows ?? 0;
const qualitativeNcgScaleCount = collectionCounts.qualitativeNcgScaleRows ?? 0;
const scenarioVariableCount = collectionCounts.scenarioVariableRows ?? 0;
const toyNcgProtocolCount = collectionCounts.toyNcgProtocolRows ?? 0;
const ncgFormulaBlockCount = collectionCounts.ncgFormulaBlockRows ?? 0;
const figurePlanCount = collectionCounts.figurePlanRows ?? 0;
const citationContextCount = collectionCounts.citationContextRows ?? 0;
const preSubmissionReviewCount = collectionCounts.preSubmissionReviewRows ?? 0;
const sourceCardIds = checkUniqueIds(findings, "sourceCardRows", data.sourceCardRows ?? []);
const claimEvidenceIds = checkUniqueIds(findings, "claimEvidenceRows", data.claimEvidenceRows ?? []);
const scenarioIds = new Set((data.scenarioRows ?? []).map((row) => row[0].split(" ")[0]));
checkUniqueIds(findings, "scenarioRows", (data.scenarioRows ?? []).map((row) => [row[0].split(" ")[0], ...row.slice(1)]));
checkUniqueIds(findings, "scenarioEvaluationRows", data.scenarioEvaluationRows ?? []);
checkUniqueIds(findings, "qualitativeNcgScaleRows", data.qualitativeNcgScaleRows ?? []);
checkUniqueIds(findings, "scenarioVariableRows", data.scenarioVariableRows ?? []);
checkUniqueIds(findings, "toyNcgProtocolRows", data.toyNcgProtocolRows ?? []);
checkUniqueIds(findings, "ncgFormulaBlockRows", data.ncgFormulaBlockRows ?? []);
checkUniqueIds(findings, "figurePlanRows", data.figurePlanRows ?? []);
checkUniqueIds(findings, "citationContextRows", data.citationContextRows ?? []);
checkUniqueIds(findings, "preSubmissionReviewRows", data.preSubmissionReviewRows ?? []);

for (const row of data.claimEvidenceRows ?? []) {
  for (const sourceId of parseSourceIds(row[2] ?? "")) {
    if (!sourceCardIds.has(sourceId)) {
      pushFinding(findings, "fail", "claim-source-card-missing", `${row[0]} references missing source card ${sourceId}.`);
    }
  }
}

const allowedContextStatuses = new Set(["ready-for-external-review", "needs-source-verification", "blocked"]);
for (const row of data.citationContextRows ?? []) {
  const rowId = row[0];
  for (const claimId of parseSourceIds(row[1] ?? "")) {
    if (!claimEvidenceIds.has(claimId)) {
      pushFinding(findings, "fail", "citation-context-unknown-claim", `${rowId} references missing claim ${claimId}.`);
    }
  }

  for (const sourceId of parseSourceIds(row[2] ?? "")) {
    if (!sourceCardIds.has(sourceId)) {
      pushFinding(findings, "fail", "citation-context-unknown-source", `${rowId} references missing source card ${sourceId}.`);
    }
  }

  if (!allowedContextStatuses.has(row[6])) {
    pushFinding(findings, "fail", "citation-context-status-invalid", `${rowId} uses invalid review status ${row[6]}.`);
  }
}

if (!fs.existsSync(citationPacketJsonPath) || !fs.existsSync(citationPacketMdPath)) {
  pushFinding(findings, "fail", "citation-context-packet-missing", "Citation context review packet must be exported before paper audit.");
} else {
  const citationPacket = readJson(citationPacketJsonPath);
  if (citationPacket.verdict !== "READY_FOR_EXTERNAL_REVIEW") {
    pushFinding(findings, "fail", "citation-context-packet-verdict-invalid", `Unexpected citation context packet verdict: ${citationPacket.verdict}`);
  }
  if (citationPacket.details?.contextCount !== citationContextCount) {
    pushFinding(findings, "fail", "citation-context-packet-count-mismatch", `Packet context count ${citationPacket.details?.contextCount} does not match data count ${citationContextCount}.`);
  }

  for (const context of citationPacket.details?.contextPackets ?? []) {
    for (const source of context.sources ?? []) {
      if (!source.referenceUrl) {
        pushFinding(findings, "fail", "citation-context-packet-source-url-missing", `${context.id} source ${source.id} is missing a reference URL in the exported packet.`);
      }
    }
  }
}

if (!fs.existsSync(citationLocalReviewJsonPath) || !fs.existsSync(citationLocalReviewMdPath)) {
  pushFinding(findings, "fail", "citation-context-local-review-missing", "Citation context local review must be generated before paper audit.");
} else {
  const localReview = readJson(citationLocalReviewJsonPath);
  if (localReview.verdict !== "LOCAL_REVIEW_COMPLETE_REQUIRES_FRESH_REVIEW") {
    pushFinding(findings, "fail", "citation-context-local-review-verdict-invalid", `Unexpected citation context local review verdict: ${localReview.verdict}`);
  }
  if (localReview.details?.reviewedContextCount !== citationContextCount) {
    pushFinding(findings, "fail", "citation-context-local-review-count-mismatch", `Local review context count ${localReview.details?.reviewedContextCount} does not match data count ${citationContextCount}.`);
  }
}

if (!fs.existsSync(referenceVerificationJsonPath) || !fs.existsSync(referenceVerificationMdPath)) {
  pushFinding(findings, "fail", "reference-verification-missing", "Reference verification must be generated before paper audit.");
} else {
  const referenceVerification = readJson(referenceVerificationJsonPath);
  if (referenceVerification.verdict === "FAIL") {
    pushFinding(findings, "fail", "reference-verification-failed", "Reference verification has FAIL verdict.");
  } else if (referenceVerification.verdict === "WARN") {
    pushFinding(findings, "warn", "reference-verification-warning", "Reference verification has WARN verdict; human review remains required.");
  } else if (referenceVerification.verdict !== "PASS") {
    pushFinding(findings, "fail", "reference-verification-verdict-invalid", `Unexpected reference verification verdict: ${referenceVerification.verdict}`);
  }
  if (referenceVerification.details?.referenceCount !== (data.referenceRows ?? []).length) {
    pushFinding(findings, "fail", "reference-verification-count-mismatch", `Reference verification count ${referenceVerification.details?.referenceCount} does not match data count ${(data.referenceRows ?? []).length}.`);
  }
}

if (!fs.existsSync(preSubmissionReviewJsonPath) || !fs.existsSync(preSubmissionReviewMdPath)) {
  pushFinding(findings, "fail", "pre-submission-review-missing", "Pre-submission review must be generated before paper audit.");
} else {
  const preSubmissionReview = readJson(preSubmissionReviewJsonPath);
  if (preSubmissionReview.verdict !== "NEEDS_EXTERNAL_REVIEW_BEFORE_FORMAL_SUBMISSION") {
    pushFinding(findings, "fail", "pre-submission-review-verdict-invalid", `Unexpected pre-submission review verdict: ${preSubmissionReview.verdict}`);
  }
  if (preSubmissionReview.details?.preSubmissionRowCount !== preSubmissionReviewCount) {
    pushFinding(findings, "fail", "pre-submission-review-count-mismatch", `Pre-submission review row count ${preSubmissionReview.details?.preSubmissionRowCount} does not match data count ${preSubmissionReviewCount}.`);
  }
}

for (const row of data.scenarioEvaluationRows ?? []) {
  const scenarioId = row[1];
  if (!scenarioIds.has(scenarioId)) {
    pushFinding(findings, "fail", "scenario-evaluation-unknown-scenario", `${row[0]} references missing scenario ${scenarioId}.`);
  }
}

const scaleIds = new Set((data.qualitativeNcgScaleRows ?? []).map((row) => row[0]));
const scenarioEvaluationByScenario = new Map((data.scenarioEvaluationRows ?? []).map((row) => [row[1], row[3]]));
for (const row of data.scenarioVariableRows ?? []) {
  const rowId = row[0];
  const scenarioId = row[1];
  const variableRatings = row.slice(3, 12);
  const ncgClass = row[12];

  if (!scenarioIds.has(scenarioId)) {
    pushFinding(findings, "fail", "scenario-variable-unknown-scenario", `${rowId} references missing scenario ${scenarioId}.`);
  }

  for (const rating of variableRatings) {
    if (!scaleIds.has(rating)) {
      pushFinding(findings, "fail", "scenario-variable-unknown-scale", `${rowId} uses unknown qualitative scale ${rating}.`);
    }
  }

  const expectedClass = scenarioEvaluationByScenario.get(scenarioId);
  if (expectedClass && expectedClass !== ncgClass) {
    pushFinding(findings, "fail", "scenario-variable-class-mismatch", `${rowId} NCG class ${ncgClass} does not match scenario evaluation class ${expectedClass}.`);
  }
}

const modelSymbols = new Set((data.modelRows ?? []).map((row) => row[0]));
for (const row of data.ncgFormulaBlockRows ?? []) {
  for (const symbol of parseSourceIds(row[2] ?? "")) {
    if (!modelSymbols.has(symbol)) {
      pushFinding(findings, "fail", "formula-block-unknown-variable", `${row[0]} references missing model variable ${symbol}.`);
    }
  }
}

const duplicateClassCount = countPattern(page, /<[^>]+class="[^"]+"\s+class="/gu);
if (duplicateClassCount > 0) {
  pushFinding(findings, "fail", "duplicate-class-attribute", `Found ${duplicateClassCount} duplicate class attribute patterns.`);
}

if (page.includes("人工黑洞可制造") && !page.includes("不得宣称人工黑洞可制造")) {
  pushFinding(findings, "fail", "unsafe-artificial-black-hole-claim", "Artificial black-hole manufacturability appears without the required negative boundary.");
}

const failCount = findings.filter((finding) => finding.severity === "fail").length;
const warnCount = findings.filter((finding) => finding.severity === "warn").length;
const verdict = failCount > 0 ? "FAIL" : warnCount > 0 ? "WARN" : "PASS";

const audit = {
  schemaVersion: "proper-time-differential-coverage-audit.v0.1",
  generatedAt: new Date().toISOString(),
  verdict,
  summary: {
    failCount,
    warnCount,
    sectionCount,
    tocCount,
    sourceCardCount,
    claimEvidenceCount,
    scenarioCount,
    scenarioEvaluationCount,
    qualitativeNcgScaleCount,
    scenarioVariableCount,
    toyNcgProtocolCount,
    ncgFormulaBlockCount,
    figurePlanCount,
    citationContextCount,
    preSubmissionReviewCount,
    duplicateClassCount,
    dataCollections: collectionCounts,
  },
  inputs: {
    pagePath: path.relative(webRoot, pagePath),
    dataPath: path.relative(webRoot, dataPath),
    toolSeedPath: path.relative(webRoot, toolSeedPath),
    citationPacketJsonPath: path.relative(webRoot, citationPacketJsonPath),
    citationPacketMdPath: path.relative(webRoot, citationPacketMdPath),
    citationLocalReviewJsonPath: path.relative(webRoot, citationLocalReviewJsonPath),
    citationLocalReviewMdPath: path.relative(webRoot, citationLocalReviewMdPath),
    referenceVerificationJsonPath: path.relative(webRoot, referenceVerificationJsonPath),
    referenceVerificationMdPath: path.relative(webRoot, referenceVerificationMdPath),
    preSubmissionReviewJsonPath: path.relative(webRoot, preSubmissionReviewJsonPath),
    preSubmissionReviewMdPath: path.relative(webRoot, preSubmissionReviewMdPath),
  },
  findings,
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(auditJsonPath, `${JSON.stringify(audit, null, 2)}\n`, "utf8");

const md = [
  "# Proper-Time Differential Waiting Hypothesis Coverage Audit",
  "",
  `- Verdict: ${verdict}`,
  `- Generated: ${audit.generatedAt}`,
  `- Sections: ${sectionCount}`,
  `- TOC entries: ${tocCount}`,
  `- Source cards: ${sourceCardCount}`,
  `- Claim-evidence rows: ${claimEvidenceCount}`,
  `- Scenario cards: ${scenarioCount}`,
  `- Scenario evaluations: ${scenarioEvaluationCount}`,
  `- Qualitative NCG scale rows: ${qualitativeNcgScaleCount}`,
  `- Scenario variable rows: ${scenarioVariableCount}`,
  `- Toy NCG protocol rows: ${toyNcgProtocolCount}`,
  `- NCG formula blocks: ${ncgFormulaBlockCount}`,
  `- Figure plan rows: ${figurePlanCount}`,
  `- Citation context rows: ${citationContextCount}`,
  `- Pre-submission review rows: ${preSubmissionReviewCount}`,
  `- Duplicate class patterns: ${duplicateClassCount}`,
  `- Data source: ${path.relative(webRoot, dataPath)}`,
  "",
  "## Findings",
  "",
  findings.length === 0
    ? "- None"
    : findings.map((finding) => `- ${finding.severity.toUpperCase()} ${finding.code}: ${finding.message}`).join("\n"),
  "",
].join("\n");

fs.writeFileSync(auditMdPath, md, "utf8");

console.log(`Proper-time differential coverage audit: ${verdict}`);
console.log(`wrote ${path.relative(webRoot, auditJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, auditMdPath)}`);

if (verdict === "FAIL") {
  process.exit(1);
}
