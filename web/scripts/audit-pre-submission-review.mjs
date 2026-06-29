import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(webRoot, "..");

const evidencePath = path.join(webRoot, "src/data/effective-immortality-evidence.json");
const outputDir = path.join(webRoot, "src/data/effective-immortality-flywheel");
const outputJsonPath = path.join(outputDir, "PRE_SUBMISSION_REVIEW.json");
const outputMdPath = path.join(outputDir, "PRE_SUBMISSION_REVIEW.md");

const expected = {
  paperVersion: "v0.25",
  schemaVersion: "2.0",
  evidenceMatrixVersion: "v1.3",
  citationAuditVersion: "v1.1",
  preSubmissionReviewVersion: "v0.1",
  searchExecutionRegisterVersion: "v0.1",
  candidateSourceVerificationVersion: "v0.1",
  candidateSourceExtractionVersion: "v0.1",
};

const activeFiles = [
  "docs/explanations/effective-immortality-acceleration-flywheel.md",
  "web/src/pages/papers/effective-immortality-flywheel.astro",
  "docs/source-notes/2026-06-28-effective-immortality-flywheel-evidence-matrix.md",
  "docs/source-notes/2026-06-28-effective-immortality-flywheel-derivation-package.md",
  "docs/source-notes/2026-06-28-effective-immortality-flywheel-automated-research-run.md",
  "docs/source-notes/2026-06-28-effective-immortality-flywheel-citation-audit.md",
  "docs/source-notes/2026-06-29-effective-immortality-flywheel-search-execution-register.md",
  "docs/source-notes/2026-06-29-effective-immortality-flywheel-candidate-source-verification.md",
  "web/src/data/effective-immortality-evidence.json",
];

const auditArtifacts = [
  {
    label: "Citation Context Review Packet",
    file: "web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_REVIEW_PACKET.json",
    expectedVerdicts: ["READY_FOR_EXTERNAL_REVIEW"],
  },
  {
    label: "Citation Context Risk Triage",
    file: "web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_RISK_TRIAGE.json",
    expectedVerdicts: ["REQUIRES_FRESH_REVIEW"],
  },
  {
    label: "High-Risk Citation Context Review",
    file: "web/src/data/effective-immortality-flywheel/HIGH_RISK_CITATION_CONTEXT_REVIEW.json",
    expectedVerdicts: ["PASS_WITH_LIMITATIONS"],
  },
  {
    label: "Citation Context Local Review",
    file: "web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_LOCAL_REVIEW.json",
    expectedVerdicts: ["LOCAL_REVIEW_COMPLETE_REQUIRES_FRESH_REVIEW"],
  },
  {
    label: "Fresh Reviewer Citation Audit Protocol",
    file: "web/src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json",
    expectedVerdicts: ["READY_FOR_FRESH_REVIEWER"],
  },
  {
    label: "Fresh Reviewer Handoff Audit",
    file: "web/src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/HANDOFF_AUDIT.json",
    expectedVerdicts: ["PASS"],
  },
  {
    label: "Fresh Reviewer Citation Results Audit",
    file: "web/src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_RESULTS_AUDIT.json",
    expectedVerdicts: ["PENDING_EXTERNAL_REVIEW_RESULTS", "PASS"],
  },
  {
    label: "Citation Audit",
    file: "web/src/data/effective-immortality-flywheel/CITATION_AUDIT.json",
    expectedVerdicts: ["WARN"],
    knownWarnReason: "metadata_registry_without_fresh_reviewer",
  },
  {
    label: "Reference Verification",
    file: "web/src/data/effective-immortality-flywheel/REFERENCE_VERIFICATION.json",
    expectedVerdicts: ["PASS", "WARN"],
  },
  {
    label: "Claim Context Audit",
    file: "web/src/data/effective-immortality-flywheel/CLAIM_CONTEXT_AUDIT.json",
    expectedVerdicts: ["PASS"],
  },
  {
    label: "Coverage Audit",
    file: "web/src/data/effective-immortality-flywheel/COVERAGE_AUDIT.json",
    expectedVerdicts: ["PASS"],
  },
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
  "yet",
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

function readRepoFile(relativePath) {
  return fs.readFileSync(path.join(repoRoot, relativePath), "utf8");
}

function lineNumber(content, index) {
  return content.slice(0, index).split(/\r?\n/u).length;
}

function excerptAt(content, index, length = 140) {
  const start = Math.max(0, index - 50);
  const end = Math.min(content.length, index + length);
  return content.slice(start, end).replace(/\s+/gu, " ").trim();
}

function addFinding(findings, severity, dimension, code, file, line, quote, suggestedFix) {
  findings.push({ severity, dimension, code, file, line, quote, suggested_fix: suggestedFix });
}

function findAll(content, regex) {
  const matches = [];
  for (const match of content.matchAll(regex)) {
    matches.push({ index: match.index || 0, text: match[0] });
  }
  return matches;
}

function escapeRegex(text) {
  return text.replace(/[.*+?^${}()|[\]\\]/gu, "\\$&");
}

function loadJson(relativePath) {
  const content = readRepoFile(relativePath);
  return { content, json: JSON.parse(content) };
}

function verdictOf(json) {
  return json.verdict || json.auditStatus || json.status || "UNKNOWN";
}

function renderMarkdown(audit) {
  const countRows = Object.entries(audit.summary.counts)
    .map(([key, value]) => `| ${key} | ${value} |`)
    .join("\n");

  const findingRows = audit.details.findings.length
    ? audit.details.findings
        .map((finding, index) => (
          `| ${index + 1} | ${finding.severity} | ${finding.dimension} | ${finding.file}:${finding.line} | ${finding.code} | ${finding.quote.replace(/\|/gu, "\\|")} | ${finding.suggested_fix.replace(/\|/gu, "\\|")} |`
        ))
        .join("\n")
    : "| - | - | - | - | - | None | None |";

  const scanRows = audit.details.scan_results
    .map((row) => `| ${row.scan} | ${row.count} | ${row.status} |`)
    .join("\n");

  return `# Pre-Submission Review

Date: ${audit.generated_at}
Input: effective immortality working paper, Web paper page, Evidence Matrix, derivation package, citation audit notes, structured evidence data, and generated audit ledgers.
Output JSON: \`web/src/data/effective-immortality-flywheel/PRE_SUBMISSION_REVIEW.json\`

## Summary

Verdict: \`${audit.verdict}\`

Reason: \`${audit.reason_code}\`

${audit.summary.text}

| Severity | Count |
| --- | ---: |
${countRows}

## Findings

| # | Severity | Dimension | Location | Code | Quote | Suggested fix |
| ---: | --- | --- | --- | --- | --- | --- |
${findingRows}

## Mechanical Scan

| Scan | Count | Status |
| --- | ---: | --- |
${scanRows}

## Submission Recommendation

${audit.submission_recommendation}

## Scope

This is a local pre-submission audit. It checks version drift, required non-claim boundaries, generated audit artifacts, banned AI-tone terms, em dash usage, and current known blockers. It does not replace a fresh external reviewer thread for sentence-level citation-context judgment.
`;
}

const evidenceContent = readRepoFile("web/src/data/effective-immortality-evidence.json");
const evidence = JSON.parse(evidenceContent);
const findings = [];
const scanResults = [];
let highRiskReviewState = "missing";
let localContextReviewState = "missing";
let freshReviewerProtocolState = "missing";
let freshReviewerHandoffState = "missing";
let freshReviewerResultsState = "missing";
const auditedInputHashes = {
  "web/src/data/effective-immortality-evidence.json": sha256(evidenceContent),
};

for (const relativePath of activeFiles) {
  const content = readRepoFile(relativePath);
  auditedInputHashes[relativePath] = sha256(content);
}

if (evidence.schemaVersion !== expected.schemaVersion) {
  addFinding(
    findings,
    "CRITICAL",
    "macro-logic",
    "schema_version_drift",
    "web/src/data/effective-immortality-evidence.json",
    1,
    `schemaVersion=${evidence.schemaVersion}`,
    `Update schemaVersion to ${expected.schemaVersion} or update the pre-submission contract.`,
  );
}

const requiredNeedles = [
  {
    file: "docs/explanations/effective-immortality-acceleration-flywheel.md",
    needles: [
      `Status: working paper ${expected.paperVersion}`,
      `Evidence Matrix ${expected.evidenceMatrixVersion}`,
      `Pre-Submission Review ${expected.preSubmissionReviewVersion}`,
      `Search Execution Register ${expected.searchExecutionRegisterVersion}`,
      `Candidate Source Verification ${expected.candidateSourceVerificationVersion}`,
      `Candidate Source Extraction ${expected.candidateSourceExtractionVersion}`,
      "不证明永生已经可行",
      "不输出个体死亡日期",
      "不替代医学",
    ],
  },
  {
    file: "web/src/pages/papers/effective-immortality-flywheel.astro",
    needles: [
      `Working paper ${expected.paperVersion}`,
      `Evidence Matrix ${expected.evidenceMatrixVersion}`,
      `Pre-Submission Review ${expected.preSubmissionReviewVersion}`,
      `Search Execution Register ${expected.searchExecutionRegisterVersion}`,
      `Candidate Source Verification ${expected.candidateSourceVerificationVersion}`,
      `Candidate Source Extraction ${expected.candidateSourceExtractionVersion}`,
      "不证明永生已经可行",
      "不输出个体死亡日期",
      "不替代医学",
    ],
  },
  {
    file: "docs/source-notes/2026-06-28-effective-immortality-flywheel-derivation-package.md",
    needles: [`Evidence Matrix ${expected.evidenceMatrixVersion}`],
  },
  {
    file: "docs/source-notes/2026-06-28-effective-immortality-flywheel-automated-research-run.md",
    needles: [
      `Working paper 升级到 \`${expected.paperVersion}\``,
      `schema \`${expected.schemaVersion}\``,
      `Citation Audit 升级到 \`${expected.citationAuditVersion}\``,
      `Pre-Submission Review ${expected.preSubmissionReviewVersion}`,
    ],
  },
  {
    file: "docs/source-notes/2026-06-29-effective-immortality-flywheel-search-execution-register.md",
    needles: [
      `Search Execution Register ${expected.searchExecutionRegisterVersion}`,
      "candidate_queue_only",
      "候选来源只代表“值得筛选”，不代表已经支持本文主张",
    ],
  },
  {
    file: "docs/source-notes/2026-06-29-effective-immortality-flywheel-candidate-source-verification.md",
    needles: [
      `Candidate Source Verification ${expected.candidateSourceVerificationVersion}`,
      "VERIFY_PASS_METADATA_ONLY",
      "没有任何一条因此自动成为正式论文证据",
    ],
  },
  {
    file: "docs/source-notes/2026-06-29-effective-immortality-flywheel-candidate-source-extraction.md",
    needles: [
      `Candidate Source Extraction ${expected.candidateSourceExtractionVersion}`,
      "HOLD_METADATA_ONLY",
      "非随机试验 meta-analysis，部分生存结果未达统计显著",
    ],
  },
];

for (const { file, needles } of requiredNeedles) {
  const content = readRepoFile(file);
  for (const needle of needles) {
    if (!content.includes(needle)) {
      addFinding(findings, "MAJOR", "macro-logic", "missing_required_marker", file, 1, needle, "Restore this marker or update the pre-submission contract deliberately.");
    }
  }
}

const stalePatterns = [
  { regex: /Evidence Matrix v0\.[0-9]+/gu, label: "stale_evidence_matrix_v0" },
  { regex: /Evidence Matrix v1\.[0-2]/gu, label: "stale_evidence_matrix_v1" },
  { regex: /Citation Audit 升级到 `v0\.[0-9]+`/gu, label: "stale_citation_audit_version" },
  { regex: /schema `1\.[0-8]`/gu, label: "stale_schema_version" },
  { regex: /schema 1\.[0-8]/gu, label: "stale_schema_version" },
  { regex: /v0\.2[01]/gu, label: "stale_paper_version" },
];

for (const relativePath of activeFiles) {
  const content = readRepoFile(relativePath);
  for (const stale of stalePatterns) {
    for (const match of findAll(content, stale.regex)) {
      addFinding(
        findings,
        "MAJOR",
        "macro-logic",
        stale.label,
        relativePath,
        lineNumber(content, match.index),
        excerptAt(content, match.index),
        `Replace stale marker with ${expected.paperVersion}, schema ${expected.schemaVersion}, Evidence Matrix ${expected.evidenceMatrixVersion}, or Citation Audit ${expected.citationAuditVersion} as appropriate.`,
      );
    }
  }
}

const textFilesForStyle = [
  "docs/explanations/effective-immortality-acceleration-flywheel.md",
  "web/src/pages/papers/effective-immortality-flywheel.astro",
];

let emDashCount = 0;
let bannedCount = 0;
for (const relativePath of textFilesForStyle) {
  const content = readRepoFile(relativePath);
  for (const match of findAll(content, /[—–]/gu)) {
    emDashCount += 1;
    addFinding(findings, "MINOR", "writing-details", "em_dash_usage", relativePath, lineNumber(content, match.index), excerptAt(content, match.index), "Replace em dash or en dash with comma, colon, semicolon, parentheses, or a shorter sentence.");
  }
  for (const term of bannedTerms) {
    const regex = new RegExp(`\\b${escapeRegex(term)}\\b`, "giu");
    for (const match of findAll(content, regex)) {
      bannedCount += 1;
      addFinding(findings, bannedCount >= 3 ? "MAJOR" : "MINOR", "writing-details", "banned_ai_tone_term", relativePath, lineNumber(content, match.index), excerptAt(content, match.index), "Replace AI-tone vocabulary with precise technical language or delete it.");
    }
  }
}
scanResults.push({ scan: "em dash / en dash", count: emDashCount, status: emDashCount ? "WARN" : "PASS" });
scanResults.push({ scan: "banned AI-tone terms", count: bannedCount, status: bannedCount ? "WARN" : "PASS" });

for (const artifact of auditArtifacts) {
  const absolutePath = path.join(repoRoot, artifact.file);
  if (!fs.existsSync(absolutePath)) {
    addFinding(findings, "CRITICAL", "integrity-gate", "missing_audit_artifact", artifact.file, 1, artifact.label, "Run npm run audit:paper-integrity.");
    continue;
  }

  const { content, json } = loadJson(artifact.file);
  auditedInputHashes[artifact.file] = sha256(content);
  const verdict = verdictOf(json);
  if (!artifact.expectedVerdicts.includes(verdict)) {
    addFinding(findings, "CRITICAL", "integrity-gate", "unexpected_audit_verdict", artifact.file, 1, `${artifact.label}: ${verdict}`, `Expected one of ${artifact.expectedVerdicts.join(", ")}.`);
  }

  if (artifact.label === "High-Risk Citation Context Review") {
    highRiskReviewState = verdict;
  }

  if (artifact.label === "Citation Context Local Review") {
    localContextReviewState = verdict;
  }

  if (artifact.label === "Fresh Reviewer Citation Audit Protocol") {
    freshReviewerProtocolState = verdict;
  }

  if (artifact.label === "Fresh Reviewer Handoff Audit") {
    freshReviewerHandoffState = verdict;
  }

  if (artifact.label === "Fresh Reviewer Citation Results Audit") {
    freshReviewerResultsState = verdict;
  }

  if (artifact.label === "Citation Audit" && verdict === "WARN") {
    if (freshReviewerResultsState !== "PASS") {
      addFinding(
        findings,
        "MAJOR",
        "integrity-gate",
        "fresh_reviewer_citation_audit_pending",
        artifact.file,
        1,
        `${json.reason_code || "citation audit warns"}; high_risk_local_review=${highRiskReviewState}; all_context_local_review=${localContextReviewState}; fresh_reviewer_protocol=${freshReviewerProtocolState}; fresh_reviewer_handoff=${freshReviewerHandoffState}; fresh_reviewer_results=${freshReviewerResultsState}`,
        "Before formal submission, run the fresh reviewer protocol and record passing sentence-level citation-context results. The local context reviews, protocol, and result template narrow the queue but are not a substitute for reviewer verdicts.",
      );
    }
  }

  if (artifact.label === "Reference Verification" && verdict === "WARN") {
    const failCount = json.details?.counts?.FAIL ?? json.details?.fail_count ?? 0;
    const warnCount = json.details?.counts?.WARN ?? json.details?.warn_count ?? 0;
    if (failCount > 0) {
      addFinding(findings, "CRITICAL", "integrity-gate", "reference_verification_fail", artifact.file, 1, `${failCount} FAIL`, "Fix failed references before proceeding.");
    } else {
      addFinding(findings, "MINOR", "integrity-gate", "reference_verification_external_warn", artifact.file, 1, `${warnCount} WARN`, "Keep publisher 403 warnings documented; manually verify before formal submission if the venue requires it.");
    }
  }
}

const counts = {
  CRITICAL: findings.filter((finding) => finding.severity === "CRITICAL").length,
  MAJOR: findings.filter((finding) => finding.severity === "MAJOR").length,
  MINOR: findings.filter((finding) => finding.severity === "MINOR").length,
};

const verdict = counts.CRITICAL > 0 ? "FAIL" : counts.MAJOR > 0 || counts.MINOR > 0 ? "WARN" : "PASS";
const reasonCode = counts.CRITICAL > 0
  ? "pre_submission_critical_findings"
  : counts.MAJOR > 0
    ? "pre_submission_major_queue"
    : counts.MINOR > 0
      ? "pre_submission_minor_queue"
      : "local_pre_submission_clean";

const audit = {
  audit_skill: "pre-submission-review",
  version: expected.preSubmissionReviewVersion,
  verdict,
  reason_code: reasonCode,
  generated_at: `${evidence.updated}T00:00:00.000Z`,
  reviewer_scope: "local structural, style, version-drift, and artifact audit; no external fresh reviewer",
  summary: {
    text: verdict === "PASS"
      ? "No local pre-submission findings were detected."
      : "Local pre-submission audit found items that must remain visible before formal submission.",
    counts,
  },
  audited_input_hashes: auditedInputHashes,
  details: {
    expected,
    scan_results: scanResults,
    findings,
  },
  submission_recommendation: counts.CRITICAL > 0
    ? "Do not submit. Fix CRITICAL local integrity findings first."
    : counts.MAJOR > 0
      ? "Needs final external citation-context review before formal submission; local structure can continue."
      : counts.MINOR > 0
        ? "Locally usable after minor cleanup; no structural blocker detected."
        : "Ready for local circulation; formal submission still depends on venue-specific formatting and external review.",
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(outputJsonPath, `${JSON.stringify(audit, null, 2)}\n`);
fs.writeFileSync(outputMdPath, renderMarkdown(audit));

console.log(`pre-submission verdict ${audit.verdict}`);
console.log(`critical ${counts.CRITICAL}`);
console.log(`major ${counts.MAJOR}`);
console.log(`minor ${counts.MINOR}`);
console.log(`wrote ${path.relative(webRoot, outputJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, outputMdPath)}`);

if (counts.CRITICAL > 0) {
  process.exitCode = 1;
}
