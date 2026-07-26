import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(webRoot, "..");

const dataPath = path.join(webRoot, "src/data/controllable-metric-waiting-room-hypothesis.json");
const pagePath = path.join(webRoot, "src/pages/papers/controllable-metric-waiting-room-hypothesis.astro");
const outputDir = path.join(webRoot, "src/data/controllable-metric-waiting-room-hypothesis");
const outputJsonPath = path.join(outputDir, "PRE_SUBMISSION_REVIEW.json");
const outputMdPath = path.join(outputDir, "PRE_SUBMISSION_REVIEW.md");

const auditArtifacts = [
  {
    label: "Reference Verification",
    file: "web/src/data/controllable-metric-waiting-room-hypothesis/REFERENCE_VERIFICATION.json",
    expectedVerdicts: ["PASS"],
  },
  {
    label: "Citation Context Review Packet",
    file: "web/src/data/controllable-metric-waiting-room-hypothesis/CITATION_CONTEXT_REVIEW_PACKET.json",
    expectedVerdicts: ["READY_FOR_EXTERNAL_REVIEW"],
  },
  {
    label: "Citation Context Local Review",
    file: "web/src/data/controllable-metric-waiting-room-hypothesis/CITATION_CONTEXT_LOCAL_REVIEW.json",
    expectedVerdicts: ["LOCAL_REVIEW_COMPLETE_REQUIRES_FRESH_REVIEW"],
  },
];

const requiredBoundaryStrings = [
  "不声称人工黑洞或重力控制已经可实现",
  "不提供强引力工程方案",
  "不输出个体寿命预测",
  "不是预测器",
  "不是外部审稿结论",
  "不适合作为正式物理论文",
  "不适合作为正式物理论文、强引力工程可行性论文、医学建议或个体决策材料提交",
];

const bannedTerms = [
  "innovative",
  "pioneering",
  "revolutionary paradigm",
  "transformative framework",
  "superior",
  "surpass",
  "excel",
  "remarkable",
  "unprecedented",
  "breakthrough performance",
  "general-purpose",
  "is capable of",
  "notably",
  "yielding",
  "at its essence",
  "encompass",
  "differentiate",
  "reveal",
  "underscore",
  "pave the way for",
  "highlight the potential of",
  "profound challenges",
  "stems from",
  "rigid",
  "impede",
];

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function readFile(filePath) {
  return fs.readFileSync(filePath, "utf8");
}

function repoPath(relativePath) {
  return path.join(repoRoot, relativePath);
}

function lineNumber(content, index) {
  return content.slice(0, index).split(/\r?\n/u).length;
}

function addFinding(findings, severity, dimension, code, file, line, quote, suggestedFix) {
  findings.push({ severity, dimension, code, file, line, quote, suggestedFix });
}

function scanNeedles(content, file, needles, findings) {
  for (const needle of needles) {
    if (!content.includes(needle)) {
      addFinding(
        findings,
        "MAJOR",
        "boundary",
        "required_boundary_missing",
        file,
        1,
        needle,
        "Restore this boundary statement or update the pre-submission contract with an explicit replacement.",
      );
    }
  }
}

function scanBannedTerms(content, file, findings) {
  for (const term of bannedTerms) {
    const regex = new RegExp(`\\b${term.replace(/[.*+?^${}()|[\]\\]/gu, "\\$&")}\\b`, "giu");
    for (const match of content.matchAll(regex)) {
      addFinding(
        findings,
        "MINOR",
        "writing",
        "banned_ai_tone_term",
        file,
        lineNumber(content, match.index || 0),
        match[0],
        "Replace with a precise technical phrase or remove the claim-softening term.",
      );
    }
  }
}

function scanEmDash(content, file, findings) {
  for (const match of content.matchAll(/—/gu)) {
    addFinding(
      findings,
      "MINOR",
      "writing",
      "em_dash_present",
      file,
      lineNumber(content, match.index || 0),
      "—",
      "Use comma, colon, semicolon, parentheses, or an explicit connective.",
    );
  }
}

function renderMarkdown(audit) {
  const countRows = Object.entries(audit.summary.counts)
    .map(([key, value]) => `| ${key} | ${value} |`)
    .join("\n");

  const artifactRows = audit.details.artifacts
    .map((artifact) => `| ${artifact.label} | ${artifact.status} | ${artifact.verdict} | ${artifact.file} |`)
    .join("\n");

  const findingRows = audit.details.findings.length
    ? audit.details.findings
      .map((finding, index) => `| ${index + 1} | ${finding.severity} | ${finding.dimension} | ${finding.file}:${finding.line} | ${finding.code} | ${finding.quote.replace(/\|/gu, "\\|")} | ${finding.suggestedFix.replace(/\|/gu, "\\|")} |`)
      .join("\n")
    : "| - | - | - | - | - | None | None |";

  return `# Controllable Metric Waiting Room Pre-Submission Review

**Generated**: ${audit.generatedAt}
**Verdict**: ${audit.verdict}

${audit.summary.text}

This is a local pre-submission review. It does not replace independent external reviewer judgment.

## Severity Counts

| Severity | Count |
| --- | ---: |
${countRows}

## Artifact Gate

| Artifact | Status | Verdict | File |
| --- | --- | --- | --- |
${artifactRows}

## Findings

| # | Severity | Dimension | Location | Code | Quote | Suggested fix |
| ---: | --- | --- | --- | --- | --- | --- |
${findingRows}

## Submission Recommendation

${audit.submissionRecommendation}
`;
}

const dataContent = readFile(dataPath);
const pageContent = readFile(pagePath);
const data = JSON.parse(dataContent);
const findings = [];
const artifacts = [];
const auditedInputHashes = {
  "web/src/data/controllable-metric-waiting-room-hypothesis.json": sha256(dataContent),
  "web/src/pages/papers/controllable-metric-waiting-room-hypothesis.astro": sha256(pageContent),
};

for (const artifact of auditArtifacts) {
  const artifactPath = repoPath(artifact.file);
  if (!fs.existsSync(artifactPath)) {
    artifacts.push({ ...artifact, status: "MISSING", verdict: "MISSING" });
    addFinding(
      findings,
      "CRITICAL",
      "integrity",
      "required_audit_artifact_missing",
      artifact.file,
      1,
      artifact.label,
      "Run npm run audit:controllable-metric-waiting-room to regenerate required audit artifacts.",
    );
    continue;
  }

  const content = readFile(artifactPath);
  auditedInputHashes[artifact.file] = sha256(content);
  const json = JSON.parse(content);
  const verdict = json.verdict || json.auditStatus || "UNKNOWN";
  const status = artifact.expectedVerdicts.includes(verdict) ? "PASS" : "FAIL";
  artifacts.push({ ...artifact, status, verdict });
  if (status === "FAIL") {
    addFinding(
      findings,
      "CRITICAL",
      "integrity",
      "audit_artifact_verdict_invalid",
      artifact.file,
      1,
      `${artifact.label}: ${verdict}`,
      `Expected one of ${artifact.expectedVerdicts.join(", ")}.`,
    );
  }
}

scanNeedles(`${dataContent}\n${pageContent}`, "controllable metric waiting room paper source", requiredBoundaryStrings, findings);
scanBannedTerms(`${dataContent}\n${pageContent}`, "controllable metric waiting room paper source", findings);
scanEmDash(pageContent, "web/src/pages/papers/controllable-metric-waiting-room-hypothesis.astro", findings);

const preSubmissionRows = data.preSubmissionReviewRows || [];
if (preSubmissionRows.length < 5) {
  addFinding(
    findings,
    "MAJOR",
    "macro-logic",
    "pre_submission_rows_low",
    "web/src/data/controllable-metric-waiting-room-hypothesis.json",
    1,
    `preSubmissionReviewRows=${preSubmissionRows.length}`,
    "Keep at least five pre-submission rows covering object boundary, sources, citation context, model/figures, and recommendation.",
  );
}

if (!preSubmissionRows.some((row) => row[2] === "NOT_READY_FOR_FORMAL_SUBMISSION")) {
  addFinding(
    findings,
    "CRITICAL",
    "macro-logic",
    "submission_recommendation_missing",
    "web/src/data/controllable-metric-waiting-room-hypothesis.json",
    1,
    "NOT_READY_FOR_FORMAL_SUBMISSION",
    "Keep the formal-submission boundary until external reviewer results and stronger physical/engineering evidence exist.",
  );
}

const counts = findings.reduce((acc, finding) => {
  acc[finding.severity] = (acc[finding.severity] || 0) + 1;
  return acc;
}, { CRITICAL: 0, MAJOR: 0, MINOR: 0 });

const verdict = counts.CRITICAL > 0
  ? "BLOCKED"
  : counts.MAJOR > 0
    ? "NEEDS_MAJOR_REVISION"
    : "NEEDS_EXTERNAL_REVIEW_BEFORE_FORMAL_SUBMISSION";

const audit = {
  audit: "controllable-metric-waiting-room-pre-submission-review",
  verdict,
  reasonCode: verdict === "BLOCKED"
    ? "critical_pre_submission_findings"
    : verdict === "NEEDS_MAJOR_REVISION"
      ? "major_pre_submission_findings"
      : "local_gate_clean_external_review_required",
  generatedAt: new Date().toISOString(),
  summary: {
    text: verdict === "NEEDS_EXTERNAL_REVIEW_BEFORE_FORMAL_SUBMISSION"
      ? "Local pre-submission review found no blocking mechanical issues. The paper remains a working paper and still requires independent external citation-context review before formal submission."
      : "Local pre-submission review found issues that must be resolved before the paper can be treated as submission-ready.",
    counts,
  },
  auditedInputHashes,
  details: {
    artifacts,
    preSubmissionRowCount: preSubmissionRows.length,
    findings,
  },
  submissionRecommendation:
    "Use as a Human Infra arXiv-style working paper. Do not submit as a formal physics, strong-gravity engineering-feasibility, medical, or individual decision paper until external reviewer results and stronger model evidence are added.",
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(outputJsonPath, `${JSON.stringify(audit, null, 2)}\n`, "utf8");
fs.writeFileSync(outputMdPath, renderMarkdown(audit), "utf8");

console.log(`controllable metric waiting room pre-submission review verdict ${verdict}`);
console.log(`critical ${counts.CRITICAL}`);
console.log(`major ${counts.MAJOR}`);
console.log(`minor ${counts.MINOR}`);
console.log(`wrote ${path.relative(webRoot, outputJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, outputMdPath)}`);

if (verdict === "BLOCKED") {
  process.exitCode = 1;
}
