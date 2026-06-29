import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");
const outputDir = path.join(webRoot, "src/data/effective-immortality-flywheel");

const protocolPath = path.join(outputDir, "FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json");
const resultsPath = path.join(outputDir, "FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json");
const resultInputsDir = path.join(outputDir, "fresh-reviewer-context-packets/results");
const templateJsonPath = path.join(outputDir, "FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.json");
const templateMdPath = path.join(outputDir, "FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.md");
const outputJsonPath = path.join(outputDir, "FRESH_REVIEWER_CITATION_AUDIT_RESULTS_AUDIT.json");
const outputMdPath = path.join(outputDir, "FRESH_REVIEWER_CITATION_AUDIT_RESULTS_AUDIT.md");

const verdictSchema = {
  reference_existence: ["PASS", "FAIL", "UNCERTAIN"],
  safe_use_support: ["SUPPORTS", "WEAK", "WRONG"],
  forbidden_use_violation: ["NONE", "POSSIBLE", "PRESENT"],
  required_action: ["KEEP", "SOFTEN", "REWRITE", "REMOVE", "REPLACE_SOURCE"],
  resolution_status: ["RESOLVED", "ACCEPTED_WITH_BOUNDARY", "PENDING_FIX", "UNRESOLVED", "NOT_REVIEWED"],
};

const expectedResultKind = "fresh-reviewer-citation-audit-results";
const expectedAssemblySourceDir = "web/src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/results";

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function readJson(filePath) {
  const content = fs.readFileSync(filePath, "utf8");
  return { content, json: JSON.parse(content) };
}

function buildTemplate(protocol, protocolHash) {
  return {
    template_kind: "fresh-reviewer-citation-audit-results-template",
    generated_at: protocol.generated_at,
    source_protocol_hash: protocolHash,
    instructions: [
      "Use this template as a field reference for per-context reviewer result files.",
      "Use fresh-reviewer-context-packets/INDEX.md to review one citation context at a time.",
      "Write one completed reviewer result per file under fresh-reviewer-context-packets/results/CTX*.json.",
      "Run npm run assemble:fresh-reviewer-results to generate FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json.",
      "Do not fill reviewer results with local author guesses. Each row must be based on reopened sources or PDFs.",
      "Every source_urls entry should point to the reviewer-opened source, DOI page, official page, PDF, or retrieval note.",
      "Use resolution_status=RESOLVED only after required prose or citation changes have been made.",
    ],
    verdict_schema: verdictSchema,
    results: protocol.details.review_queue.map((row) => ({
      context_id: row.context_id,
      priority: row.priority,
      risk_tier: row.risk_tier,
      source_group: row.source_group,
      claims: row.claims,
      references: row.references.map((ref) => ref.key),
      reviewer_identity_class: null,
      reviewed_at: null,
      source_urls: [],
      reference_existence: null,
      safe_use_support: null,
      forbidden_use_violation: null,
      required_action: null,
      resolution_status: "NOT_REVIEWED",
      reviewer_reason: null,
      manuscript_change_required: null,
      manuscript_change_summary: null,
      reviewer_trace_path: null,
    })),
  };
}

function validateResults(protocol, protocolHash, results) {
  const findings = [];
  const rowsByContext = new Map((results.results || []).map((row) => [row.context_id, row]));

  if (results.result_kind !== expectedResultKind) {
    findings.push({
      severity: "BLOCKER",
      context_id: "GLOBAL",
      code: "canonical_result_kind_missing",
      message: `Formal results must be assembled by the per-context assembler with result_kind=${expectedResultKind}.`,
    });
  }

  if (!results.assembled_at) {
    findings.push({
      severity: "BLOCKER",
      context_id: "GLOBAL",
      code: "assembled_at_missing",
      message: "Formal results must record the assembly timestamp.",
    });
  }

  if (results.assembly_source_dir !== expectedAssemblySourceDir) {
    findings.push({
      severity: "BLOCKER",
      context_id: "GLOBAL",
      code: "assembly_source_dir_mismatch",
      message: `Formal results must be assembled from ${expectedAssemblySourceDir}.`,
    });
  }

  if (!results.assembly_input_hashes || typeof results.assembly_input_hashes !== "object" || Array.isArray(results.assembly_input_hashes)) {
    findings.push({
      severity: "BLOCKER",
      context_id: "GLOBAL",
      code: "assembly_input_hashes_missing",
      message: "Formal results must include SHA-256 hashes for every per-context reviewer result input file.",
    });
  }

  if (results.source_protocol_hash !== protocolHash) {
    findings.push({
      severity: "BLOCKER",
      context_id: "GLOBAL",
      code: "source_protocol_hash_mismatch",
      message: "Results were not produced against the current fresh reviewer protocol hash.",
    });
  }

  for (const queueRow of protocol.details.review_queue) {
    const result = rowsByContext.get(queueRow.context_id);
    if (!result) {
      findings.push({
        severity: "BLOCKER",
        context_id: queueRow.context_id,
        code: "missing_context_result",
        message: "Required context has no reviewer result row.",
      });
      continue;
    }

    const expectedInputRelativePath = `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/results/${queueRow.context_id}.json`;
    const recordedInputHash = results.assembly_input_hashes?.[expectedInputRelativePath];
    const expectedInputPath = path.join(resultInputsDir, `${queueRow.context_id}.json`);

    if (!recordedInputHash) {
      findings.push({
        severity: "BLOCKER",
        context_id: queueRow.context_id,
        code: "missing_assembly_input_hash",
        message: `Formal results must record the input hash for ${expectedInputRelativePath}.`,
      });
    } else if (!fs.existsSync(expectedInputPath)) {
      findings.push({
        severity: "BLOCKER",
        context_id: queueRow.context_id,
        code: "missing_assembly_input_file",
        message: `The source reviewer result file ${expectedInputRelativePath} is missing.`,
      });
    } else {
      const actualInputHash = sha256(fs.readFileSync(expectedInputPath, "utf8"));
      if (actualInputHash !== recordedInputHash) {
        findings.push({
          severity: "BLOCKER",
          context_id: queueRow.context_id,
          code: "assembly_input_hash_mismatch",
          message: `The source reviewer result file ${expectedInputRelativePath} no longer matches the canonical ledger hash.`,
        });
      }
    }

    if (result.source_protocol_hash && result.source_protocol_hash !== protocolHash) {
      findings.push({
        severity: "BLOCKER",
        context_id: queueRow.context_id,
        code: "row_source_protocol_hash_mismatch",
        message: "Reviewer row source protocol hash does not match the current protocol hash.",
      });
    }

    for (const [field, allowedValues] of Object.entries(verdictSchema)) {
      if (!allowedValues.includes(result[field])) {
        findings.push({
          severity: "BLOCKER",
          context_id: queueRow.context_id,
          code: `invalid_${field}`,
          message: `${field} must be one of ${allowedValues.join(", ")}.`,
        });
      }
    }

    if (!Array.isArray(result.source_urls) || result.source_urls.length === 0) {
      findings.push({
        severity: "BLOCKER",
        context_id: queueRow.context_id,
        code: "missing_source_urls",
        message: "Fresh reviewer result must include at least one source URL or retrieval note.",
      });
    }

    if (!result.reviewer_identity_class || !result.reviewed_at || !result.reviewer_reason) {
      findings.push({
        severity: "BLOCKER",
        context_id: queueRow.context_id,
        code: "missing_reviewer_trace_fields",
        message: "Reviewer identity class, reviewed_at, and reviewer_reason are required.",
      });
    }

    if (result.reference_existence !== "PASS") {
      findings.push({
        severity: "BLOCKER",
        context_id: queueRow.context_id,
        code: "reference_existence_not_pass",
        message: "Reference existence must be PASS before formal submission.",
      });
    }

    if (result.safe_use_support === "WRONG") {
      findings.push({
        severity: "BLOCKER",
        context_id: queueRow.context_id,
        code: "safe_use_wrong",
        message: "Source does not support the registered safe use.",
      });
    }

    if (result.forbidden_use_violation === "PRESENT") {
      findings.push({
        severity: "BLOCKER",
        context_id: queueRow.context_id,
        code: "forbidden_use_present",
        message: "The manuscript currently uses the source for a forbidden claim.",
      });
    }

    if (
      ["WEAK", "POSSIBLE"].includes(result.safe_use_support) ||
      result.forbidden_use_violation === "POSSIBLE" ||
      ["SOFTEN", "REWRITE", "REMOVE", "REPLACE_SOURCE"].includes(result.required_action)
    ) {
      if (!["RESOLVED", "ACCEPTED_WITH_BOUNDARY"].includes(result.resolution_status)) {
        findings.push({
          severity: "BLOCKER",
          context_id: queueRow.context_id,
          code: "required_action_unresolved",
          message: "Weak support, possible forbidden use, or rewrite action remains unresolved.",
        });
      }
    }
  }

  const unexpectedContexts = (results.results || [])
    .map((row) => row.context_id)
    .filter((contextId) => !protocol.details.review_queue.some((queueRow) => queueRow.context_id === contextId));

  for (const contextId of unexpectedContexts) {
    findings.push({
      severity: "WARN",
      context_id: contextId,
      code: "unexpected_context_result",
      message: "Result row does not correspond to the current protocol queue.",
    });
  }

  return findings;
}

function renderTemplateMarkdown(template) {
  const rows = template.results
    .map((row) => `| ${row.priority} | ${row.context_id} | ${row.risk_tier} | ${row.source_group.replace(/\|/gu, "\\|")} | ${row.references.join(", ")} |`)
    .join("\n");

  return `# Fresh Reviewer Citation Audit Results Template

Source protocol hash: \`${template.source_protocol_hash}\`

Use this JSON template as a field reference only. Do not copy it directly to \`FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json\`.

Use \`web/src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/INDEX.md\` to review one citation context at a time.

Completed reviewer result files belong in \`web/src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/results/CTX*.json\`. Run \`npm run assemble:fresh-reviewer-results\` to create the canonical results ledger with per-file hashes.

## Required Verdict Fields

| Field | Allowed values |
| --- | --- |
| reference_existence | ${verdictSchema.reference_existence.join(", ")} |
| safe_use_support | ${verdictSchema.safe_use_support.join(", ")} |
| forbidden_use_violation | ${verdictSchema.forbidden_use_violation.join(", ")} |
| required_action | ${verdictSchema.required_action.join(", ")} |
| resolution_status | ${verdictSchema.resolution_status.join(", ")} |

## Queue

| Priority | Context | Risk | Source group | References |
| ---: | --- | --- | --- | --- |
${rows}
`;
}

function renderAuditMarkdown(audit) {
  const findingRows = audit.details.findings.length
    ? audit.details.findings
        .map((finding) => `| ${finding.severity} | ${finding.context_id} | ${finding.code} | ${finding.message.replace(/\|/gu, "\\|")} |`)
        .join("\n")
    : "| - | - | - | No findings |";

  return `# Fresh Reviewer Citation Audit Results Audit

Date: ${audit.generated_at}

Verdict: \`${audit.verdict}\`

Reason: \`${audit.reason_code}\`

${audit.summary}

| Metric | Count |
| --- | ---: |
| Required contexts | ${audit.details.required_context_count} |
| Completed contexts | ${audit.details.completed_context_count} |
| Blocking findings | ${audit.details.blocking_finding_count} |
| Warning findings | ${audit.details.warning_finding_count} |

## Findings

| Severity | Context | Code | Message |
| --- | --- | --- | --- |
${findingRows}

## Scope

This audit validates the shape and blocking status of \`FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json\` when that file exists. If the results file is absent, the audit intentionally remains pending and does not claim that the fresh reviewer has run.
`;
}

const protocol = readJson(protocolPath);
const protocolHash = sha256(protocol.content);
const template = buildTemplate(protocol.json, protocolHash);

fs.writeFileSync(templateJsonPath, `${JSON.stringify(template, null, 2)}\n`);
fs.writeFileSync(templateMdPath, renderTemplateMarkdown(template));

let resultsContent = null;
let resultsJson = null;
let findings = [];
let completedContextCount = 0;
let verdict = "PENDING_EXTERNAL_REVIEW_RESULTS";
let reasonCode = "fresh_reviewer_results_file_missing";
let summary = "Fresh reviewer results have not been recorded yet. A template has been generated for the external reviewer result ledger.";

if (fs.existsSync(resultsPath)) {
  const results = readJson(resultsPath);
  resultsContent = results.content;
  resultsJson = results.json;
  findings = validateResults(protocol.json, protocolHash, resultsJson);
  completedContextCount = (resultsJson.results || []).filter((row) => row.resolution_status !== "NOT_REVIEWED").length;
  const blockingCount = findings.filter((finding) => finding.severity === "BLOCKER").length;
  const warningCount = findings.filter((finding) => finding.severity === "WARN").length;

  if (blockingCount > 0) {
    verdict = "FAIL";
    reasonCode = "fresh_reviewer_results_blocked";
    summary = "Fresh reviewer results exist, but at least one blocking citation-context issue remains unresolved.";
  } else if (completedContextCount !== protocol.json.details.context_count) {
    verdict = "PENDING_EXTERNAL_REVIEW_RESULTS";
    reasonCode = "fresh_reviewer_results_incomplete";
    summary = "Fresh reviewer results file exists, but not every required context has a completed result.";
  } else if (warningCount > 0) {
    verdict = "WARN";
    reasonCode = "fresh_reviewer_results_warn";
    summary = "Fresh reviewer results are complete with non-blocking warnings.";
  } else {
    verdict = "PASS";
    reasonCode = "fresh_reviewer_results_pass";
    summary = "Fresh reviewer results cover every required context and no blocking citation-context issues remain.";
  }
}

const audit = {
  audit_skill: "fresh-reviewer-citation-results-audit",
  verdict,
  reason_code: reasonCode,
  summary,
  generated_at: protocol.json.generated_at,
  audited_input_hashes: {
    "src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json": protocolHash,
    ...(resultsContent ? { "src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json": sha256(resultsContent) } : {}),
  },
  details: {
    source_protocol_hash: protocolHash,
    results_file_present: Boolean(resultsContent),
    required_context_count: protocol.json.details.context_count,
    completed_context_count: completedContextCount,
    blocking_finding_count: findings.filter((finding) => finding.severity === "BLOCKER").length,
    warning_finding_count: findings.filter((finding) => finding.severity === "WARN").length,
    template_json: "web/src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.json",
    template_markdown: "web/src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.md",
    context_packet_index: "web/src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/INDEX.md",
    findings,
  },
};

fs.writeFileSync(outputJsonPath, `${JSON.stringify(audit, null, 2)}\n`);
fs.writeFileSync(outputMdPath, renderAuditMarkdown(audit));

console.log(`fresh reviewer citation results audit ${audit.verdict}`);
console.log(`required contexts ${audit.details.required_context_count}`);
console.log(`completed contexts ${audit.details.completed_context_count}`);
console.log(`blocking findings ${audit.details.blocking_finding_count}`);
console.log(`wrote ${path.relative(webRoot, templateJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, templateMdPath)}`);
console.log(`wrote ${path.relative(webRoot, outputJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, outputMdPath)}`);

if (audit.verdict === "FAIL") {
  process.exitCode = 1;
}
