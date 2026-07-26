import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");

const dataPath = path.join(webRoot, "src/data/controllable-metric-waiting-room-hypothesis.json");
const pagePath = path.join(webRoot, "src/pages/papers/controllable-metric-waiting-room-hypothesis.astro");
const outputDir = path.join(webRoot, "src/data/controllable-metric-waiting-room-hypothesis");
const toolSeedPath = path.join(outputDir, "TOOL_GENERATED_PAGE_SEED.astro");
const derivationPackagePath = path.join(outputDir, "DERIVATION_PACKAGE.md");
const referenceVerificationPath = path.join(outputDir, "REFERENCE_VERIFICATION.json");
const citationContextPacketPath = path.join(outputDir, "CITATION_CONTEXT_REVIEW_PACKET.json");
const citationContextLocalReviewPath = path.join(outputDir, "CITATION_CONTEXT_LOCAL_REVIEW.json");
const preSubmissionReviewPath = path.join(outputDir, "PRE_SUBMISSION_REVIEW.json");
const auditJsonPath = path.join(outputDir, "COVERAGE_AUDIT.json");
const auditMdPath = path.join(outputDir, "COVERAGE_AUDIT.md");

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function readArtifactJson(filePath) {
  if (!fs.existsSync(filePath)) {
    return { exists: false, json: null, error: null };
  }
  try {
    return { exists: true, json: readJson(filePath), error: null };
  } catch (error) {
    return { exists: true, json: null, error };
  }
}

function pushFinding(findings, severity, code, message) {
  findings.push({ severity, code, message });
}

function countPattern(text, pattern) {
  return [...text.matchAll(pattern)].length;
}

function splitIds(value) {
  return String(value)
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function markdownTable(rows) {
  if (rows.length === 0) {
    return "No findings.";
  }
  return [
    "| Severity | Code | Message |",
    "| --- | --- | --- |",
    ...rows.map((row) => `| ${row.severity} | ${row.code} | ${row.message.replaceAll("|", "\\|")} |`),
  ].join("\n");
}

const data = readJson(dataPath);
const page = fs.readFileSync(pagePath, "utf8");
const seed = fs.existsSync(toolSeedPath) ? fs.readFileSync(toolSeedPath, "utf8") : "";
const derivationPackage = fs.existsSync(derivationPackagePath) ? fs.readFileSync(derivationPackagePath, "utf8") : "";
const searchableSource = `${page}\n${JSON.stringify(data)}`;
const findings = [];

const requiredPageStrings = data.auditContract?.requiredPageStrings ?? [];
const minimumCounts = data.auditContract?.minimumCounts ?? {};
const collections = {
  conceptRows: data.conceptRows,
  hypothesisRows: data.hypothesisRows,
  researchQuestionRows: data.researchQuestionRows,
  stateRows: data.stateRows,
  loopRows: data.loopRows,
  variableRows: data.variableRows,
  formalAssumptionRows: data.formalAssumptionRows,
  equationRows: data.equationRows,
  propositionRows: data.propositionRows,
  claimEvidenceRows: data.claimEvidenceRows,
  citationContextRows: data.citationContextRows,
  preSubmissionReviewRows: data.preSubmissionReviewRows,
  scenarioRows: data.scenarioRows,
  qualitativeGateScaleRows: data.qualitativeGateScaleRows,
  scenarioEvaluationRows: data.scenarioEvaluationRows,
  scenarioMatrixRows: data.scenarioMatrixRows,
  gateColumnRows: data.gateColumnRows,
  falsifierRows: data.falsifierRows,
  protocolRows: data.protocolRows,
  evidenceNeedRows: data.evidenceNeedRows,
  evaluationRoadmapRows: data.evaluationRoadmapRows,
  sourceRows: data.sourceRows,
};

for (const required of requiredPageStrings) {
  if (!searchableSource.includes(required)) {
    pushFinding(findings, "fail", "required-page-string-missing", `Page missing required string: ${required}`);
  }
}

const artifactSpecs = [
  {
    label: "Reference Verification",
    path: referenceVerificationPath,
    expectedVerdicts: ["PASS"],
  },
  {
    label: "Citation Context Review Packet",
    path: citationContextPacketPath,
    expectedVerdicts: ["READY_FOR_EXTERNAL_REVIEW"],
  },
  {
    label: "Citation Context Local Review",
    path: citationContextLocalReviewPath,
    expectedVerdicts: ["LOCAL_REVIEW_COMPLETE_REQUIRES_FRESH_REVIEW"],
  },
  {
    label: "Pre-Submission Review",
    path: preSubmissionReviewPath,
    expectedVerdicts: ["NEEDS_EXTERNAL_REVIEW_BEFORE_FORMAL_SUBMISSION"],
  },
];

const artifactSummaries = artifactSpecs.map((spec) => {
  const artifact = readArtifactJson(spec.path);
  const relativePath = path.relative(webRoot, spec.path);
  if (!artifact.exists) {
    pushFinding(findings, "fail", "required-audit-artifact-missing", `${spec.label} missing at ${relativePath}.`);
    return { label: spec.label, path: relativePath, status: "MISSING", verdict: "MISSING" };
  }
  if (artifact.error || !artifact.json) {
    pushFinding(findings, "fail", "required-audit-artifact-invalid-json", `${spec.label} is not valid JSON at ${relativePath}.`);
    return { label: spec.label, path: relativePath, status: "INVALID_JSON", verdict: "INVALID_JSON" };
  }
  const verdict = artifact.json.verdict || artifact.json.auditStatus || "UNKNOWN";
  if (!spec.expectedVerdicts.includes(verdict)) {
    pushFinding(findings, "fail", "audit-artifact-verdict-invalid", `${spec.label} verdict ${verdict} does not match expected ${spec.expectedVerdicts.join(", ")}.`);
    return { label: spec.label, path: relativePath, status: "FAIL", verdict };
  }
  return { label: spec.label, path: relativePath, status: "PASS", verdict };
});

for (const [name, rows] of Object.entries(collections)) {
  if (!Array.isArray(rows)) {
    pushFinding(findings, "fail", "collection-not-array", `${name} must be an array.`);
    continue;
  }
  const minimum = minimumCounts[name] ?? 1;
  if (rows.length < minimum) {
    pushFinding(findings, "fail", "collection-count-low", `${name} count ${rows.length} is below minimum ${minimum}.`);
  }
  if (!page.includes(`${name}.map`)) {
    pushFinding(findings, "fail", "collection-not-rendered", `Page does not render ${name} with a map expression.`);
  }
  const ids = rows.map((row) => row[0]);
  if (new Set(ids).size !== ids.length) {
    pushFinding(findings, "fail", "collection-duplicate-id", `${name} contains duplicate first-column IDs.`);
  }
}

const claimById = new Map((data.claimEvidenceRows || []).map((row) => [row[0], row]));
const sourceById = new Map((data.sourceRows || []).map((row) => [row[0], row]));
const scenarioById = new Map((data.scenarioRows || []).map((row) => [row[0], row]));
const gateScaleIds = new Set((data.qualitativeGateScaleRows || []).map((row) => row[0]));
const gateColumnIds = new Set((data.gateColumnRows || []).map((row) => row[0]));

for (const row of data.citationContextRows || []) {
  const contextId = row[0];
  const claimIds = splitIds(row[1]);
  const sourceIds = splitIds(row[2]);
  if (row[6] !== "ready-for-external-review") {
    pushFinding(findings, "fail", "citation-context-status-invalid", `${contextId} status must be ready-for-external-review.`);
  }
  for (const claimId of claimIds) {
    if (!claimById.has(claimId)) {
      pushFinding(findings, "fail", "citation-context-unknown-claim", `${contextId} points to unknown claim ${claimId}.`);
    }
  }
  for (const sourceId of sourceIds) {
    if (!sourceById.has(sourceId)) {
      pushFinding(findings, "fail", "citation-context-unknown-source", `${contextId} points to unknown source ${sourceId}.`);
    }
  }
  if (claimIds.length === 1 && sourceIds.length === 1) {
    const claim = claimById.get(claimIds[0]);
    if (claim && claim[2] !== sourceIds[0]) {
      pushFinding(findings, "fail", "citation-context-claim-source-mismatch", `${contextId} maps ${claimIds[0]} to ${sourceIds[0]}, but claim source is ${claim[2]}.`);
    }
  }
}

const citationPacket = readArtifactJson(citationContextPacketPath).json;
const citationLocalReview = readArtifactJson(citationContextLocalReviewPath).json;
const preSubmissionReview = readArtifactJson(preSubmissionReviewPath).json;

if (citationPacket?.details?.contextCount !== (data.citationContextRows || []).length) {
  pushFinding(findings, "fail", "citation-packet-context-count-mismatch", `Citation packet context count ${citationPacket?.details?.contextCount ?? "missing"} does not match registered contexts ${(data.citationContextRows || []).length}.`);
}

if (citationLocalReview?.details?.reviewedContextCount !== (data.citationContextRows || []).length) {
  pushFinding(findings, "fail", "citation-local-review-count-mismatch", `Citation local review count ${citationLocalReview?.details?.reviewedContextCount ?? "missing"} does not match registered contexts ${(data.citationContextRows || []).length}.`);
}

if (preSubmissionReview?.details?.preSubmissionRowCount !== (data.preSubmissionReviewRows || []).length) {
  pushFinding(findings, "fail", "pre-submission-row-count-mismatch", `Pre-submission row count ${preSubmissionReview?.details?.preSubmissionRowCount ?? "missing"} does not match registered rows ${(data.preSubmissionReviewRows || []).length}.`);
}

for (const row of data.scenarioEvaluationRows || []) {
  if (!scenarioById.has(row[0])) {
    pushFinding(findings, "fail", "scenario-evaluation-unknown-scenario", `Scenario evaluation row ${row[0]} does not point to a registered scenario.`);
  }
}

for (const row of data.scenarioMatrixRows || []) {
  const scenarioId = row[0];
  if (!scenarioById.has(scenarioId)) {
    pushFinding(findings, "fail", "scenario-matrix-unknown-scenario", `Scenario matrix row ${scenarioId} does not point to a registered scenario.`);
  }
  if (row.length !== 11) {
    pushFinding(findings, "fail", "scenario-matrix-width-invalid", `Scenario matrix row ${scenarioId} must have 11 columns, found ${row.length}.`);
  }
  for (const value of row.slice(2, 10)) {
    if (!gateScaleIds.has(value)) {
      pushFinding(findings, "fail", "scenario-matrix-unknown-gate-scale", `Scenario matrix row ${scenarioId} uses unknown gate scale ${value}.`);
    }
  }
}

for (const row of data.gateColumnRows || []) {
  if (!["K", "P_exit", "P_adopt", "P_cont", "R_life", "R_engineering", "R_tail", "C_wait"].includes(row[0])) {
    pushFinding(findings, "fail", "unknown-gate-column", `Gate column ${row[0]} is not part of the current NCG contract.`);
  }
}

for (const column of ["K", "P_exit", "P_adopt", "P_cont", "R_life", "R_engineering", "R_tail", "C_wait"]) {
  if (!gateColumnIds.has(column)) {
    pushFinding(findings, "fail", "gate-column-missing", `Gate column ${column} is missing.`);
  }
}

if (!page.includes("controllable-metric-waiting-room-hypothesis.json")) {
  pushFinding(findings, "fail", "structured-data-import-missing", "Page must import the structured JSON data source.");
}

if (!seed.includes("This tool-generated seed is retained")) {
  pushFinding(findings, "fail", "tool-seed-marker-missing", "Tool-generated seed is missing or does not contain the expected marker.");
}

for (const required of ["# Derivation Package", "## Target", "## Status", "## Invariant Object", "## Assumptions", "## Notation", "## Main Derivation", "## Boundaries and Non-Claims"]) {
  if (!derivationPackage.includes(required)) {
    pushFinding(findings, "fail", "derivation-package-section-missing", `DERIVATION_PACKAGE.md missing required section: ${required}`);
  }
}

for (const domClass of ["PaperReaderLayout", "ltx_page_navbar", "ltx_TOC", "ltx_document", "ltx_abstract", "ltx_bibliography"]) {
  if (!page.includes(domClass)) {
    pushFinding(findings, "fail", "arxiv-dom-contract-missing", `Page is missing ${domClass}.`);
  }
}

for (let index = 1; index <= 14; index += 1) {
  if (!page.includes(`id="S${index}"`)) {
    pushFinding(findings, "fail", "section-missing", `Page missing section S${index}.`);
  }
  if (!page.includes(`href="#S${index}"`)) {
    pushFinding(findings, "fail", "toc-anchor-missing", `TOC missing anchor S${index}.`);
  }
}

if (!page.includes('id="F1"')) {
  pushFinding(findings, "fail", "figure-f1-missing", "Page must render Figure 1.");
}

if (!page.includes('id="F2"') || !page.includes('id="controllable-metric-waiting-room-loop-svg"')) {
  pushFinding(findings, "fail", "figure-f2-svg-missing", "Page must render Figure 2 with controllable-metric-waiting-room-loop-svg.");
}

if (!page.includes('id="F3"') || !page.includes('id="controllable-metric-waiting-room-scenario-matrix-svg"')) {
  pushFinding(findings, "fail", "figure-f3-svg-missing", "Page must render Figure 3 with controllable-metric-waiting-room-scenario-matrix-svg.");
}

const sectionCount = countPattern(page, /<section id="S\d+"/gu);
const tocCount = countPattern(page, /ltx_tocentry_section/gu);
const duplicateClassAttributes = countPattern(page, /class="[^"]*"\s+class="/gu);

if (sectionCount < 14) {
  pushFinding(findings, "fail", "section-count-low", `Expected at least 14 sections, found ${sectionCount}.`);
}
if (tocCount < 14) {
  pushFinding(findings, "fail", "toc-count-low", `Expected at least 14 TOC section entries, found ${tocCount}.`);
}
if (duplicateClassAttributes > 0) {
  pushFinding(findings, "fail", "duplicate-class-attribute", `Found ${duplicateClassAttributes} duplicate class attribute patterns.`);
}

const failCount = findings.filter((finding) => finding.severity === "fail").length;
const audit = {
  generatedAt: new Date().toISOString(),
  verdict: failCount === 0 ? "PASS" : "FAIL",
  summary: {
    sectionCount,
    tocCount,
    duplicateClassAttributes,
    collectionCounts: Object.fromEntries(Object.entries(collections).map(([name, rows]) => [name, Array.isArray(rows) ? rows.length : 0])),
    artifacts: artifactSummaries,
  },
  findings,
  contract: {
    toolSeedPath: path.relative(webRoot, toolSeedPath),
    derivationPackagePath: path.relative(webRoot, derivationPackagePath),
    referenceVerificationPath: path.relative(webRoot, referenceVerificationPath),
    citationContextPacketPath: path.relative(webRoot, citationContextPacketPath),
    citationContextLocalReviewPath: path.relative(webRoot, citationContextLocalReviewPath),
    preSubmissionReviewPath: path.relative(webRoot, preSubmissionReviewPath),
    pagePath: path.relative(webRoot, pagePath),
    dataPath: path.relative(webRoot, dataPath),
  },
};

const markdown = [
  "# Controllable Metric Waiting Room Paper Coverage Audit",
  "",
  `**Generated**: ${audit.generatedAt}`,
  `**Verdict**: ${audit.verdict}`,
  "",
  "## Summary",
  "",
  `- Sections: ${sectionCount}`,
  `- TOC section entries: ${tocCount}`,
  `- Duplicate class attribute patterns: ${duplicateClassAttributes}`,
  `- Tool seed: ${audit.contract.toolSeedPath}`,
  `- Derivation package: ${audit.contract.derivationPackagePath}`,
  `- Reference verification: ${audit.contract.referenceVerificationPath}`,
  `- Citation context packet: ${audit.contract.citationContextPacketPath}`,
  `- Citation context local review: ${audit.contract.citationContextLocalReviewPath}`,
  `- Pre-submission review: ${audit.contract.preSubmissionReviewPath}`,
  "",
  "## Findings",
  "",
  markdownTable(findings),
  "",
].join("\n");

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(auditJsonPath, `${JSON.stringify(audit, null, 2)}\n`);
fs.writeFileSync(auditMdPath, markdown);

if (audit.verdict !== "PASS") {
  console.error(markdown);
  process.exit(1);
}

console.log(`Controllable metric waiting room paper audit PASS: ${auditJsonPath}`);
