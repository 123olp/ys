import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import Ajv2020 from "ajv/dist/2020.js";
import addFormats from "ajv-formats";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");
const outputDir = path.join(webRoot, "src/data/effective-immortality-flywheel");
const packetDir = path.join(outputDir, "fresh-reviewer-context-packets");
const resultsDir = path.join(packetDir, "results");

const protocolPath = path.join(outputDir, "FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json");
const canonicalResultsPath = path.join(outputDir, "FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json");
const resultSchemaPath = path.join(packetDir, "RESULT_SCHEMA.json");
const resultsReadmePath = path.join(resultsDir, "README.md");

const verdictSchema = {
  reference_existence: ["PASS", "FAIL", "UNCERTAIN"],
  safe_use_support: ["SUPPORTS", "WEAK", "WRONG"],
  forbidden_use_violation: ["NONE", "POSSIBLE", "PRESENT"],
  required_action: ["KEEP", "SOFTEN", "REWRITE", "REMOVE", "REPLACE_SOURCE"],
  resolution_status: ["RESOLVED", "ACCEPTED_WITH_BOUNDARY", "PENDING_FIX", "UNRESOLVED"],
};

const reviewerFields = [
  "reviewer_identity_class",
  "reviewed_at",
  "source_urls",
  "reviewer_reason",
  "manuscript_change_required",
  "manuscript_change_summary",
  "reviewer_trace_path",
];

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function readJson(filePath) {
  const content = fs.readFileSync(filePath, "utf8");
  return { content, json: JSON.parse(content) };
}

function loadResultSchemaValidator(protocolHash) {
  if (!fs.existsSync(resultSchemaPath)) {
    return {
      schemaHash: null,
      validate: null,
      findings: [
        {
          severity: "BLOCKER",
          context_id: "GLOBAL",
          file: path.relative(webRoot, resultSchemaPath),
          code: "result_schema_missing",
          message: "Fresh reviewer result schema is missing. Run npm run export:fresh-reviewer-handoff before assembling results.",
        },
      ],
    };
  }

  const schema = readJson(resultSchemaPath);
  const schemaHash = sha256(schema.content);
  const expectedProtocolHash = schema.json?.properties?.source_protocol_hash?.const;
  const findings = [];

  if (expectedProtocolHash !== protocolHash) {
    findings.push({
      severity: "BLOCKER",
      context_id: "GLOBAL",
      file: path.relative(webRoot, resultSchemaPath),
      code: "result_schema_protocol_hash_mismatch",
      message: "Fresh reviewer result schema was generated against a different protocol hash.",
    });
  }

  try {
    const ajv = new Ajv2020({ allErrors: true, strict: true, allowUnionTypes: true });
    addFormats(ajv);
    return {
      schemaHash,
      validate: ajv.compile(schema.json),
      findings,
    };
  } catch (error) {
    return {
      schemaHash,
      validate: null,
      findings: [
        ...findings,
        {
          severity: "BLOCKER",
          context_id: "GLOBAL",
          file: path.relative(webRoot, resultSchemaPath),
          code: "result_schema_compile_failed",
          message: error.message,
        },
      ],
    };
  }
}

function contextNumber(contextId) {
  const match = /^CTX(\d+)$/u.exec(contextId);
  return match ? Number(match[1]) : Number.MAX_SAFE_INTEGER;
}

function escapeCell(value) {
  return String(value ?? "").replace(/\|/gu, "\\|").replace(/\n/gu, "<br>");
}

function readResultRows() {
  if (!fs.existsSync(resultsDir)) return [];
  return fs
    .readdirSync(resultsDir)
    .filter((fileName) => /^CTX\d+\.json$/u.test(fileName))
    .sort((a, b) => contextNumber(path.basename(a, ".json")) - contextNumber(path.basename(b, ".json")))
    .map((fileName) => {
      const absolutePath = path.join(resultsDir, fileName);
      const source = readJson(absolutePath);
      const raw = source.json;
      const result = raw.result || raw.result_stub || raw;
      return {
        fileName,
        absolutePath,
        relativePath: path.relative(webRoot, absolutePath),
        hash: sha256(source.content),
        result,
      };
    });
}

function validateResultAgainstSchema(file, schemaValidator) {
  if (!schemaValidator.validate) {
    return [];
  }

  const valid = schemaValidator.validate(file.result);
  if (valid) return [];

  return (schemaValidator.validate.errors || []).map((error) => ({
    severity: "BLOCKER",
    context_id: file.result?.context_id || path.basename(file.fileName, ".json"),
    file: file.relativePath,
    code: "result_schema_violation",
    message: `${error.instancePath || "/"} ${error.message || "does not satisfy RESULT_SCHEMA.json"}`,
  }));
}

function validateResultFile(file, protocolHash, requiredContextIds, schemaValidator) {
  const findings = [];
  const row = file.result || {};
  const contextId = row.context_id || path.basename(file.fileName, ".json");

  findings.push(...validateResultAgainstSchema(file, schemaValidator));

  if (!requiredContextIds.has(contextId)) {
    findings.push({
      severity: "BLOCKER",
      context_id: contextId,
      file: file.relativePath,
      code: "unknown_context_result",
      message: "Result file does not map to any context in the current fresh reviewer protocol.",
    });
  }

  if (row.context_id !== contextId) {
    findings.push({
      severity: "BLOCKER",
      context_id: contextId,
      file: file.relativePath,
      code: "context_id_mismatch",
      message: "The result file name and result.context_id do not match.",
    });
  }

  if (row.source_protocol_hash && row.source_protocol_hash !== protocolHash) {
    findings.push({
      severity: "BLOCKER",
      context_id: contextId,
      file: file.relativePath,
      code: "source_protocol_hash_mismatch",
      message: "The per-context result was produced against a different protocol hash.",
    });
  }

  for (const [field, allowedValues] of Object.entries(verdictSchema)) {
    if (!allowedValues.includes(row[field])) {
      findings.push({
        severity: "BLOCKER",
        context_id: contextId,
        file: file.relativePath,
        code: `invalid_${field}`,
        message: `${field} must be one of ${allowedValues.join(", ")}.`,
      });
    }
  }

  for (const field of reviewerFields) {
    const value = row[field];
    const missingArray = Array.isArray(value) && value.length === 0;
    if (value === null || value === undefined || value === "" || missingArray) {
      findings.push({
        severity: "BLOCKER",
        context_id: contextId,
        file: file.relativePath,
        code: `missing_${field}`,
        message: `${field} is required for a completed external reviewer result.`,
      });
    }
  }

  if (row.resolution_status === "PENDING_FIX" || row.resolution_status === "UNRESOLVED") {
    findings.push({
      severity: "BLOCKER",
      context_id: contextId,
      file: file.relativePath,
      code: "unresolved_result_status",
      message: "Completed assembly requires RESOLVED or ACCEPTED_WITH_BOUNDARY status.",
    });
  }

  return findings;
}

function canonicalRow(protocolRow, resultRow, protocolHash) {
  return {
    context_id: protocolRow.context_id,
    priority: protocolRow.priority,
    risk_tier: protocolRow.risk_tier,
    source_group: protocolRow.source_group,
    claims: protocolRow.claims,
    references: protocolRow.references.map((ref) => ref.key),
    source_protocol_hash: protocolHash,
    reviewer_identity_class: resultRow.reviewer_identity_class,
    reviewed_at: resultRow.reviewed_at,
    source_urls: resultRow.source_urls,
    reference_existence: resultRow.reference_existence,
    safe_use_support: resultRow.safe_use_support,
    forbidden_use_violation: resultRow.forbidden_use_violation,
    required_action: resultRow.required_action,
    resolution_status: resultRow.resolution_status,
    reviewer_reason: resultRow.reviewer_reason,
    manuscript_change_required: resultRow.manuscript_change_required,
    manuscript_change_summary: resultRow.manuscript_change_summary,
    reviewer_trace_path: resultRow.reviewer_trace_path,
  };
}

function renderResultsReadme(status) {
  const missingRows = status.missing_contexts.length
    ? status.missing_contexts.map((contextId) => `| ${contextId} | missing |`).join("\n")
    : "| - | No missing context files |";

  const findingRows = status.findings.length
    ? status.findings
        .map((finding) => `| ${finding.severity} | ${finding.context_id} | ${escapeCell(finding.code)} | ${escapeCell(finding.file || "")} | ${escapeCell(finding.message)} |`)
        .join("\n")
    : "| - | - | - | - | No structural findings |";

  return `# Fresh Reviewer Per-Context Results

This directory is the only supported input location for external reviewer result files.

Expected file pattern: \`CTX*.json\`

Result schema: \`../RESULT_SCHEMA.json\`

Result schema hash: \`${status.result_schema_hash || "missing"}\`

Canonical output: \`web/src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json\`

Protocol hash: \`${status.source_protocol_hash}\`

## Workflow

1. Read \`../INDEX.md\` and review each context packet in priority order.
2. Copy each packet's result stub into this directory as \`CTX<id>.json\`.
3. Fill the fields from a real fresh-reviewer source lookup. Use \`../RESULT_SCHEMA.json\` as the return contract. Do not use local author guesses.
4. Run \`npm run assemble:fresh-reviewer-results\`.
5. Keep the reviewed \`CTX*.json\` files in this directory; the canonical ledger stores their SHA-256 hashes.
6. Run \`npm run audit:fresh-reviewer-results\`.

The assembler writes the canonical results file only when every required context file exists and passes structural validation. The audit gate rejects a canonical ledger whose source \`CTX*.json\` files are missing or hash-mismatched.

## Current Status

| Metric | Count |
| --- | ---: |
| Required contexts | ${status.required_context_count} |
| Per-context result files | ${status.result_file_count} |
| Missing contexts | ${status.missing_contexts.length} |
| Structural findings | ${status.findings.length} |

## Missing Contexts

| Context | Status |
| --- | --- |
${missingRows}

## Findings

| Severity | Context | Code | File | Message |
| --- | --- | --- | --- | --- |
${findingRows}
`;
}

const protocol = readJson(protocolPath);
const protocolHash = sha256(protocol.content);
const requiredRows = protocol.json.details.review_queue || [];
const requiredContextIds = new Set(requiredRows.map((row) => row.context_id));
const schemaValidator = loadResultSchemaValidator(protocolHash);
fs.mkdirSync(resultsDir, { recursive: true });

const resultFiles = readResultRows();
const seenContexts = new Set();
const duplicateFindings = [];
const rowsByContext = new Map();

for (const file of resultFiles) {
  const contextId = file.result?.context_id || path.basename(file.fileName, ".json");
  if (seenContexts.has(contextId)) {
    duplicateFindings.push({
      severity: "BLOCKER",
      context_id: contextId,
      file: file.relativePath,
      code: "duplicate_context_result",
      message: "Only one result file per context is allowed.",
    });
  }
  seenContexts.add(contextId);
  rowsByContext.set(contextId, file.result);
}

const missingContexts = requiredRows
  .filter((row) => !rowsByContext.has(row.context_id))
  .map((row) => row.context_id);

const structuralFindings = [
  ...duplicateFindings,
  ...(resultFiles.length > 0 ? schemaValidator.findings : []),
  ...resultFiles.flatMap((file) => validateResultFile(file, protocolHash, requiredContextIds, schemaValidator)),
];

const status = {
  source_protocol_hash: protocolHash,
  result_schema_hash: schemaValidator.schemaHash,
  required_context_count: requiredRows.length,
  result_file_count: resultFiles.length,
  missing_contexts: missingContexts,
  findings: structuralFindings,
};

fs.writeFileSync(resultsReadmePath, renderResultsReadme(status));

if (resultFiles.length === 0) {
  console.log("fresh reviewer per-context results directory initialized");
  console.log("no CTX*.json result files found; canonical results not written");
  console.log(`wrote ${path.relative(webRoot, resultsReadmePath)}`);
  if (fs.existsSync(canonicalResultsPath)) {
    console.error("canonical results file exists but no per-context result files are present; refusing to accept unverifiable reviewer provenance");
    process.exitCode = 1;
    process.exit();
  }
  process.exit(0);
}

if (structuralFindings.some((finding) => finding.severity === "BLOCKER")) {
  console.error("fresh reviewer per-context results contain structural blockers; canonical results not written");
  console.log(`wrote ${path.relative(webRoot, resultsReadmePath)}`);
  process.exitCode = 1;
  process.exit();
}

if (missingContexts.length > 0) {
  console.log("fresh reviewer per-context results are incomplete");
  console.log(`missing contexts ${missingContexts.join(", ")}`);
  console.log(`wrote ${path.relative(webRoot, resultsReadmePath)}`);
  if (fs.existsSync(canonicalResultsPath)) {
    console.error("canonical results file already exists but per-context result set is incomplete; refusing to overwrite or silently rely on stale results");
    process.exitCode = 1;
  }
  process.exit();
}

const canonicalResults = {
  result_kind: "fresh-reviewer-citation-audit-results",
  assembled_at: new Date().toISOString(),
  source_protocol_hash: protocolHash,
  assembly_source_dir: "web/src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/results",
  assembly_input_hashes: Object.fromEntries(
    resultFiles
      .slice()
      .sort((a, b) => contextNumber(path.basename(a.fileName, ".json")) - contextNumber(path.basename(b.fileName, ".json")))
      .map((file) => [file.relativePath, file.hash]),
  ),
  results: requiredRows
    .slice()
    .sort((a, b) => a.priority - b.priority)
    .map((row) => canonicalRow(row, rowsByContext.get(row.context_id), protocolHash)),
};

fs.writeFileSync(canonicalResultsPath, `${JSON.stringify(canonicalResults, null, 2)}\n`);

console.log("fresh reviewer canonical results assembled");
console.log(`contexts ${canonicalResults.results.length}`);
console.log(`wrote ${path.relative(webRoot, canonicalResultsPath)}`);
console.log(`wrote ${path.relative(webRoot, resultsReadmePath)}`);
