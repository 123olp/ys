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

const protocolPath = path.join(outputDir, "FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json");
const indexJsonPath = path.join(packetDir, "INDEX.json");
const indexMdPath = path.join(packetDir, "INDEX.md");
const handoffJsonPath = path.join(packetDir, "HANDOFF.json");
const handoffMdPath = path.join(packetDir, "HANDOFF.md");
const resultSchemaJsonPath = path.join(packetDir, "RESULT_SCHEMA.json");
const resultSchemaMdPath = path.join(packetDir, "RESULT_SCHEMA.md");
const outputJsonPath = path.join(packetDir, "HANDOFF_AUDIT.json");
const outputMdPath = path.join(packetDir, "HANDOFF_AUDIT.md");

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function relativePath(filePath) {
  return path.relative(webRoot, filePath);
}

function readText(filePath) {
  return fs.readFileSync(filePath, "utf8");
}

function readJson(filePath) {
  const content = readText(filePath);
  return { content, json: JSON.parse(content) };
}

function escapeCell(value) {
  return String(value ?? "").replace(/\|/gu, "\\|").replace(/\n/gu, "<br>");
}

function sameSet(left, right) {
  if (left.length !== right.length) return false;
  const rightSet = new Set(right);
  return left.every((value) => rightSet.has(value));
}

function finding(severity, code, message, file = "") {
  return { severity, code, message, file };
}

function readRequiredInputs() {
  const findings = [];
  const inputs = {};
  const required = [
    ["protocol", protocolPath],
    ["indexJson", indexJsonPath],
    ["indexMd", indexMdPath],
    ["handoffJson", handoffJsonPath],
    ["handoffMd", handoffMdPath],
    ["schemaJson", resultSchemaJsonPath],
    ["schemaMd", resultSchemaMdPath],
  ];

  for (const [key, filePath] of required) {
    if (!fs.existsSync(filePath)) {
      findings.push(finding("BLOCKER", "missing_required_handoff_input", `Missing ${relativePath(filePath)}.`, relativePath(filePath)));
      continue;
    }

    try {
      if (filePath.endsWith(".json")) {
        inputs[key] = readJson(filePath);
      } else {
        inputs[key] = { content: readText(filePath) };
      }
    } catch (error) {
      findings.push(finding("BLOCKER", "unreadable_required_handoff_input", error.message, relativePath(filePath)));
    }
  }

  return { inputs, findings };
}

function validateSchema(schemaJson, protocolHash, indexContexts) {
  const findings = [];

  try {
    const ajv = new Ajv2020({ allErrors: true, strict: true, allowUnionTypes: true });
    addFormats(ajv);
    ajv.compile(schemaJson);
  } catch (error) {
    findings.push(finding("BLOCKER", "result_schema_compile_failed", error.message, relativePath(resultSchemaJsonPath)));
  }

  const schemaProtocolHash = schemaJson?.properties?.source_protocol_hash?.const;
  if (schemaProtocolHash !== protocolHash) {
    findings.push(
      finding(
        "BLOCKER",
        "result_schema_protocol_hash_mismatch",
        "RESULT_SCHEMA.json source_protocol_hash const does not match the current protocol hash.",
        relativePath(resultSchemaJsonPath),
      ),
    );
  }

  const schemaContexts = schemaJson?.properties?.context_id?.enum || [];
  if (!sameSet(schemaContexts, indexContexts)) {
    findings.push(
      finding(
        "BLOCKER",
        "result_schema_context_enum_mismatch",
        "RESULT_SCHEMA.json context_id enum does not exactly match the packet index contexts.",
        relativePath(resultSchemaJsonPath),
      ),
    );
  }

  const requiredFields = schemaJson?.required || [];
  for (const field of [
    "context_id",
    "source_protocol_hash",
    "reviewer_identity_class",
    "reviewed_at",
    "source_urls",
    "reference_existence",
    "safe_use_support",
    "forbidden_use_violation",
    "required_action",
    "resolution_status",
    "reviewer_reason",
    "reviewer_trace_path",
  ]) {
    if (!requiredFields.includes(field)) {
      findings.push(finding("BLOCKER", "result_schema_missing_required_field", `RESULT_SCHEMA.json does not require ${field}.`, relativePath(resultSchemaJsonPath)));
    }
  }

  return findings;
}

function validateHandoff(handoff, handoffMd, schema, protocolHash, index, fileHashes) {
  const findings = [];
  const indexPackets = index.packets || [];
  const indexContexts = indexPackets.map((packet) => packet.context_id);

  if (handoff.handoff_kind !== "fresh-reviewer-citation-context-handoff") {
    findings.push(finding("BLOCKER", "handoff_kind_invalid", "HANDOFF.json has an unexpected handoff_kind.", relativePath(handoffJsonPath)));
  }

  if (handoff.source_protocol_hash !== protocolHash) {
    findings.push(finding("BLOCKER", "handoff_protocol_hash_mismatch", "HANDOFF.json source_protocol_hash does not match the current protocol hash.", relativePath(handoffJsonPath)));
  }

  if (handoff.packet_count !== indexPackets.length || handoff.packets?.length !== indexPackets.length) {
    findings.push(finding("BLOCKER", "handoff_packet_count_mismatch", "HANDOFF.json packet_count does not match INDEX.json.", relativePath(handoffJsonPath)));
  }

  const handoffContexts = (handoff.packets || []).map((packet) => packet.context_id);
  if (!sameSet(handoffContexts, indexContexts)) {
    findings.push(finding("BLOCKER", "handoff_packet_context_mismatch", "HANDOFF.json packets do not exactly match INDEX.json contexts.", relativePath(handoffJsonPath)));
  }

  const requiredResultContexts = (handoff.required_result_files || [])
    .map((filePath) => path.basename(filePath, ".json"))
    .filter((contextId) => /^CTX\d+$/u.test(contextId));
  if (!sameSet(requiredResultContexts, indexContexts)) {
    findings.push(finding("BLOCKER", "handoff_required_result_files_mismatch", "HANDOFF.json required_result_files do not exactly match INDEX.json contexts.", relativePath(handoffJsonPath)));
  }

  const schemaHash = fileHashes.get(relativePath(resultSchemaJsonPath));
  const schemaMdHash = fileHashes.get(relativePath(resultSchemaMdPath));
  if (handoff.result_schema?.path !== relativePath(resultSchemaJsonPath) || handoff.result_schema?.sha256 !== schemaHash) {
    findings.push(finding("BLOCKER", "handoff_result_schema_hash_mismatch", "HANDOFF.json result_schema hash does not match RESULT_SCHEMA.json.", relativePath(handoffJsonPath)));
  }
  if (handoff.result_schema?.markdown_path !== relativePath(resultSchemaMdPath) || handoff.result_schema?.markdown_sha256 !== schemaMdHash) {
    findings.push(finding("BLOCKER", "handoff_result_schema_markdown_hash_mismatch", "HANDOFF.json result_schema markdown hash does not match RESULT_SCHEMA.md.", relativePath(handoffJsonPath)));
  }

  const expectedSourcePaths = [
    relativePath(protocolPath),
    relativePath(indexJsonPath),
    relativePath(indexMdPath),
    ...indexContexts.flatMap((contextId) => [
      relativePath(path.join(packetDir, `${contextId}.json`)),
      relativePath(path.join(packetDir, `${contextId}.md`)),
    ]),
  ];
  const sourceFileMap = new Map((handoff.source_files || []).map((row) => [row.path, row.sha256]));

  for (const expectedPath of expectedSourcePaths) {
    if (!sourceFileMap.has(expectedPath)) {
      findings.push(finding("BLOCKER", "handoff_source_file_missing", `HANDOFF.json source_files is missing ${expectedPath}.`, relativePath(handoffJsonPath)));
      continue;
    }
    if (sourceFileMap.get(expectedPath) !== fileHashes.get(expectedPath)) {
      findings.push(finding("BLOCKER", "handoff_source_file_hash_mismatch", `HANDOFF.json hash does not match ${expectedPath}.`, relativePath(handoffJsonPath)));
    }
  }

  for (const contextId of indexContexts) {
    if (!handoffMd.includes(`# Fresh Reviewer Context Packet: ${contextId}`)) {
      findings.push(finding("BLOCKER", "handoff_markdown_missing_context", `HANDOFF.md does not include packet section ${contextId}.`, relativePath(handoffMdPath)));
    }
  }

  if (!handoffMd.includes("Schema file:") || !handoffMd.includes(relativePath(resultSchemaJsonPath))) {
    findings.push(finding("BLOCKER", "handoff_markdown_missing_schema_reference", "HANDOFF.md does not include the result schema reference.", relativePath(handoffMdPath)));
  }

  if (!schema?.properties?.reviewed_at?.format) {
    findings.push(finding("BLOCKER", "result_schema_missing_date_time_format", "RESULT_SCHEMA.json does not enforce reviewed_at date-time format.", relativePath(resultSchemaJsonPath)));
  }

  return findings;
}

function renderAuditMarkdown(audit) {
  const rows = audit.details.findings.length
    ? audit.details.findings
        .map((item) => `| ${item.severity} | ${escapeCell(item.code)} | ${escapeCell(item.file || "")} | ${escapeCell(item.message)} |`)
        .join("\n")
    : "| - | - | - | No findings |";

  return `# Fresh Reviewer Handoff Audit

Date: ${audit.generated_at}

Verdict: \`${audit.verdict}\`

Reason: \`${audit.reason_code}\`

${audit.summary}

| Metric | Count |
| --- | ---: |
| Packets | ${audit.details.packet_count} |
| Source trace files | ${audit.details.source_file_count} |
| Findings | ${audit.details.findings.length} |

## Findings

| Severity | Code | File | Message |
| --- | --- | --- | --- |
${rows}

## Scope

This audit validates that the external fresh-reviewer handoff is complete, hash-traceable, schema-backed, and aligned with the current protocol. It does not replace a fresh external reviewer verdict.
`;
}

const { inputs, findings: inputFindings } = readRequiredInputs();
const findings = [...inputFindings];
const fileHashes = new Map();

for (const [filePath, input] of [
  [protocolPath, inputs.protocol],
  [indexJsonPath, inputs.indexJson],
  [indexMdPath, inputs.indexMd],
  [handoffJsonPath, inputs.handoffJson],
  [handoffMdPath, inputs.handoffMd],
  [resultSchemaJsonPath, inputs.schemaJson],
  [resultSchemaMdPath, inputs.schemaMd],
]) {
  if (input?.content) fileHashes.set(relativePath(filePath), sha256(input.content));
}

if (inputs.indexJson?.json?.packets) {
  for (const packet of inputs.indexJson.json.packets) {
    for (const extension of ["json", "md"]) {
      const filePath = path.join(packetDir, `${packet.context_id}.${extension}`);
      if (!fs.existsSync(filePath)) {
        findings.push(finding("BLOCKER", "packet_file_missing", `Missing ${relativePath(filePath)}.`, relativePath(filePath)));
        continue;
      }
      fileHashes.set(relativePath(filePath), sha256(readText(filePath)));
    }
  }
}

if (inputs.protocol?.content && inputs.indexJson?.json && inputs.handoffJson?.json && inputs.handoffMd?.content && inputs.schemaJson?.json) {
  const protocolHash = sha256(inputs.protocol.content);
  const indexContexts = (inputs.indexJson.json.packets || []).map((packet) => packet.context_id);
  findings.push(...validateSchema(inputs.schemaJson.json, protocolHash, indexContexts));
  findings.push(...validateHandoff(inputs.handoffJson.json, inputs.handoffMd.content, inputs.schemaJson.json, protocolHash, inputs.indexJson.json, fileHashes));
}

const blockingCount = findings.filter((item) => item.severity === "BLOCKER").length;
const audit = {
  audit_skill: "fresh-reviewer-handoff-audit",
  verdict: blockingCount > 0 ? "FAIL" : "PASS",
  reason_code: blockingCount > 0 ? "fresh_reviewer_handoff_blocked" : "fresh_reviewer_handoff_pass",
  summary: blockingCount > 0
    ? "Fresh reviewer handoff has blocking completeness, schema, or hash-trace findings."
    : "Fresh reviewer handoff is complete, schema-backed, and hash-traceable.",
  generated_at: inputs.protocol?.json?.generated_at || new Date().toISOString(),
  audited_input_hashes: Object.fromEntries(fileHashes),
  details: {
    packet_count: inputs.indexJson?.json?.packet_count || 0,
    source_file_count: inputs.handoffJson?.json?.source_files?.length || 0,
    blocking_finding_count: blockingCount,
    findings,
  },
};

fs.writeFileSync(outputJsonPath, `${JSON.stringify(audit, null, 2)}\n`);
fs.writeFileSync(outputMdPath, renderAuditMarkdown(audit));

console.log(`fresh reviewer handoff audit ${audit.verdict}`);
console.log(`packets ${audit.details.packet_count}`);
console.log(`blocking findings ${audit.details.blocking_finding_count}`);
console.log(`wrote ${relativePath(outputJsonPath)}`);
console.log(`wrote ${relativePath(outputMdPath)}`);

if (audit.verdict === "FAIL") {
  process.exitCode = 1;
}
