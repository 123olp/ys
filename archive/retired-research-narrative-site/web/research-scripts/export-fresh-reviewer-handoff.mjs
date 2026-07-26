import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

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

const resolutionStatusSchema = ["RESOLVED", "ACCEPTED_WITH_BOUNDARY", "PENDING_FIX", "UNRESOLVED"];

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function readText(filePath) {
  return fs.readFileSync(filePath, "utf8");
}

function readJson(filePath) {
  const content = readText(filePath);
  return { content, json: JSON.parse(content) };
}

function relativePath(filePath) {
  return path.relative(webRoot, filePath);
}

function requireFile(filePath, producerCommand) {
  if (fs.existsSync(filePath)) return;
  throw new Error(`Missing ${relativePath(filePath)}. Run ${producerCommand} first.`);
}

function contextNumber(contextId) {
  const match = /^CTX(\d+)$/u.exec(contextId);
  return match ? Number(match[1]) : Number.MAX_SAFE_INTEGER;
}

function escapeCell(value) {
  return String(value ?? "").replace(/\|/gu, "\\|").replace(/\n/gu, "<br>");
}

function renderBulletList(items) {
  return items.map((item) => `- ${item}`).join("\n");
}

function renderPacketTable(packets) {
  return packets
    .map(
      (packet) =>
        `| ${packet.priority} | ${packet.context_id} | ${packet.risk_tier} | ${packet.risk_score} | ${escapeCell(packet.source_group)} | \`results/${packet.context_id}.json\` |`,
    )
    .join("\n");
}

function renderResultSchema(verdictSchema) {
  return [
    `| reference_existence | ${(verdictSchema.reference_existence || []).join(", ")} |`,
    `| safe_use_support | ${(verdictSchema.safe_use_support || []).join(", ")} |`,
    `| forbidden_use_violation | ${(verdictSchema.forbidden_use_violation || []).join(", ")} |`,
    `| required_action | ${(verdictSchema.required_action || []).join(", ")} |`,
    `| resolution_status | ${resolutionStatusSchema.join(", ")} |`,
  ].join("\n");
}

function renderResultSchemaProperties(properties) {
  return [
    `| reference_existence | ${(properties.reference_existence?.enum || []).join(", ")} |`,
    `| safe_use_support | ${(properties.safe_use_support?.enum || []).join(", ")} |`,
    `| forbidden_use_violation | ${(properties.forbidden_use_violation?.enum || []).join(", ")} |`,
    `| required_action | ${(properties.required_action?.enum || []).join(", ")} |`,
    `| resolution_status | ${(properties.resolution_status?.enum || []).join(", ")} |`,
  ].join("\n");
}

function buildResultSchema(protocolHash, packets, verdictSchema) {
  return {
    $schema: "https://json-schema.org/draft/2020-12/schema",
    $id: "https://human-infra.local/schemas/fresh-reviewer-context-result.schema.json",
    title: "Fresh reviewer citation-context result",
    type: "object",
    additionalProperties: false,
    required: [
      "context_id",
      "priority",
      "risk_tier",
      "source_group",
      "claims",
      "references",
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
      "manuscript_change_required",
      "manuscript_change_summary",
      "reviewer_trace_path",
    ],
    properties: {
      context_id: {
        type: "string",
        enum: packets.map((packet) => packet.context_id),
      },
      priority: {
        type: "integer",
        minimum: 1,
        maximum: packets.length,
      },
      risk_tier: {
        type: "string",
        enum: ["HIGH", "MEDIUM", "LOW"],
      },
      source_group: {
        type: "string",
        minLength: 1,
      },
      claims: {
        type: "array",
        minItems: 1,
        items: {
          type: "string",
          pattern: "^CL\\d+$",
        },
      },
      references: {
        type: "array",
        minItems: 1,
        items: {
          type: "string",
          minLength: 1,
        },
      },
      source_protocol_hash: {
        type: "string",
        const: protocolHash,
      },
      reviewer_identity_class: {
        type: "string",
        minLength: 1,
        description: "Reviewer class or role, for example independent-human-reviewer or fresh-ai-reviewer-with-web.",
      },
      reviewed_at: {
        type: "string",
        format: "date-time",
      },
      source_urls: {
        type: "array",
        minItems: 1,
        items: {
          type: "string",
          minLength: 1,
        },
        description: "Reviewer-opened source URLs, DOI pages, official pages, PDF links, or explicit retrieval notes.",
      },
      reference_existence: {
        type: "string",
        enum: verdictSchema.reference_existence,
      },
      safe_use_support: {
        type: "string",
        enum: verdictSchema.safe_use_support,
      },
      forbidden_use_violation: {
        type: "string",
        enum: verdictSchema.forbidden_use_violation,
      },
      required_action: {
        type: "string",
        enum: verdictSchema.required_action,
      },
      resolution_status: {
        type: "string",
        enum: resolutionStatusSchema,
      },
      reviewer_reason: {
        type: "string",
        minLength: 1,
      },
      manuscript_change_required: {
        type: ["boolean", "string"],
      },
      manuscript_change_summary: {
        type: "string",
        minLength: 1,
      },
      reviewer_trace_path: {
        type: "string",
        minLength: 1,
        description: "Path or note pointing to the reviewer trace, transcript, source notes, or review worksheet.",
      },
    },
  };
}

function renderResultSchemaMarkdown(schema, protocolHash) {
  return `# Fresh Reviewer Result Schema

Protocol hash: \`${protocolHash}\`

This schema defines the shape of each completed external reviewer result file under \`fresh-reviewer-context-packets/results/CTX*.json\`. It is a return contract for reviewers and a field-level guide for humans. The assembler remains the authoritative gate for accepting completed results.

## Required Files

Each reviewed context must produce exactly one result file:

\`\`\`text
fresh-reviewer-context-packets/results/CTX*.json
\`\`\`

Do not write \`FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json\` by hand. Run \`npm run assemble:fresh-reviewer-results\` after all per-context files are present.

## Required Verdict Fields

| Field | Allowed values |
| --- | --- |
${renderResultSchemaProperties(schema.properties)}

## Required Trace Fields

| Field | Requirement |
| --- | --- |
| reviewer_identity_class | Non-empty reviewer class or role |
| reviewed_at | ISO date-time |
| source_urls | At least one reopened source URL or retrieval note |
| reviewer_reason | Non-empty reason for the verdict |
| manuscript_change_required | Boolean or explicit text |
| manuscript_change_summary | Non-empty summary |
| reviewer_trace_path | Path or note for the review trace |

## JSON Schema

\`\`\`json
${JSON.stringify(schema, null, 2)}
\`\`\`
`;
}

function renderFileTraceRows(files) {
  return files
    .map((file) => `| \`${file.path}\` | \`${file.sha256}\` |`)
    .join("\n");
}

function renderHandoffMarkdown(handoff, packetMarkdownSections) {
  return `# Fresh Reviewer Citation Context Handoff

Generated at: ${handoff.generated_at}

Protocol hash: \`${handoff.source_protocol_hash}\`

This handoff is the standalone external-review package for the effective immortality flywheel paper. It is a queue, contract, and evidence map for an independent citation-context reviewer. It is not reviewer evidence by itself.

## Independence Contract

${renderBulletList(handoff.reviewer_independence_contract)}

Additional boundary: do not trust local review artifacts as evidence. Local ledgers identify what to check; only reopened sources, PDFs, DOI pages, official pages, or explicit retrieval notes can support reviewer verdicts.

## Required Workflow

${handoff.workflow.map((step, index) => `${index + 1}. ${step}`).join("\n")}

## Required Output Files

The reviewer must return one JSON file per citation context:

| Priority | Context | Risk | Score | Source group | Required result file |
| ---: | --- | --- | ---: | --- | --- |
${renderPacketTable(handoff.packets)}

After all result files exist, run:

\`\`\`bash
cd web
npm run assemble:fresh-reviewer-results
npm run audit:fresh-reviewer-results
\`\`\`

The canonical \`FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json\` is accepted only when it is assembled from these per-context files and records matching SHA-256 hashes.

Schema file: \`${handoff.result_schema.path}\`

Schema hash: \`${handoff.result_schema.sha256}\`

## Verdict Schema

| Field | Allowed values |
| --- | --- |
${renderResultSchema(handoff.verdict_schema)}

## Return Checklist

${renderBulletList(handoff.return_checklist)}

## Blocking Conditions

${renderBulletList(handoff.blocking_conditions)}

## Source Trace

| File | SHA-256 |
| --- | --- |
${renderFileTraceRows(handoff.source_files)}

## Packet Contents

${packetMarkdownSections.join("\n\n---\n\n")}
`;
}

requireFile(protocolPath, "npm run export:fresh-reviewer-protocol");
requireFile(indexJsonPath, "npm run export:fresh-reviewer-context-packets");
requireFile(indexMdPath, "npm run export:fresh-reviewer-context-packets");

const protocol = readJson(protocolPath);
const index = readJson(indexJsonPath);
const indexMarkdown = readText(indexMdPath);
const protocolHash = sha256(protocol.content);
const indexJsonHash = sha256(index.content);
const indexMdHash = sha256(indexMarkdown);

const packets = index.json.packets
  .slice()
  .sort((a, b) => a.priority - b.priority || contextNumber(a.context_id) - contextNumber(b.context_id));

const packetFiles = packets.flatMap((packet) => {
  const jsonPath = path.join(packetDir, `${packet.context_id}.json`);
  const mdPath = path.join(packetDir, `${packet.context_id}.md`);
  requireFile(jsonPath, "npm run export:fresh-reviewer-context-packets");
  requireFile(mdPath, "npm run export:fresh-reviewer-context-packets");
  return [
    { context_id: packet.context_id, kind: "json", absolutePath: jsonPath, path: relativePath(jsonPath), content: readText(jsonPath) },
    { context_id: packet.context_id, kind: "markdown", absolutePath: mdPath, path: relativePath(mdPath), content: readText(mdPath) },
  ];
});

const packetMarkdownSections = packets.map((packet) => readText(path.join(packetDir, `${packet.context_id}.md`)));
const resultSchema = buildResultSchema(protocolHash, packets, {
  ...protocol.json.details.verdict_schema,
  resolution_status: resolutionStatusSchema,
});
const resultSchemaContent = `${JSON.stringify(resultSchema, null, 2)}\n`;
const resultSchemaMarkdown = renderResultSchemaMarkdown(resultSchema, protocolHash);

fs.writeFileSync(resultSchemaJsonPath, resultSchemaContent);
fs.writeFileSync(resultSchemaMdPath, resultSchemaMarkdown);

const sourceFiles = [
  { path: relativePath(protocolPath), sha256: protocolHash },
  { path: relativePath(indexJsonPath), sha256: indexJsonHash },
  { path: relativePath(indexMdPath), sha256: indexMdHash },
  ...packetFiles.map((file) => ({ path: file.path, sha256: sha256(file.content) })),
];

const handoff = {
  handoff_kind: "fresh-reviewer-citation-context-handoff",
  generated_at: protocol.json.generated_at,
  source_protocol_hash: protocolHash,
  source_index_hash: indexJsonHash,
  packet_count: packets.length,
  result_schema: {
    path: relativePath(resultSchemaJsonPath),
    sha256: sha256(resultSchemaContent),
    markdown_path: relativePath(resultSchemaMdPath),
    markdown_sha256: sha256(resultSchemaMarkdown),
  },
  required_result_files: packets.map((packet) => `web/src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/results/${packet.context_id}.json`),
  reviewer_independence_contract: protocol.json.details.reviewer_independence_contract,
  verdict_schema: {
    ...protocol.json.details.verdict_schema,
    resolution_status: resolutionStatusSchema,
  },
  blocking_conditions: protocol.json.details.blocking_conditions,
  workflow: [
    "Open HANDOFF.md in a fresh reviewer context.",
    "Review contexts in priority order and reopen every listed source, DOI page, official page, PDF, or retrieval note.",
    "Judge reference existence, safe-use support, forbidden-use boundary, required action, and resolution status.",
    "Write one completed result file per context under fresh-reviewer-context-packets/results/CTX*.json.",
    "Run the assembler and audit commands; do not hand-edit the canonical results ledger.",
  ],
  return_checklist: [
    "Every CTX*.json contains reviewer_identity_class, reviewed_at, source_urls, reviewer_reason, manuscript_change_required, manuscript_change_summary, and reviewer_trace_path.",
    "Every source_urls array points to reviewer-opened sources or explicit retrieval notes.",
    "No result uses local author claims as evidence.",
    "Any SOFTEN, REWRITE, REMOVE, REPLACE_SOURCE, WEAK, WRONG, POSSIBLE, or PRESENT verdict is either resolved in manuscript text or remains blocking.",
    "Canonical results are produced only by npm run assemble:fresh-reviewer-results.",
  ],
  packets: packets.map((packet) => ({
    priority: packet.priority,
    context_id: packet.context_id,
    risk_tier: packet.risk_tier,
    risk_score: packet.risk_score,
    source_group: packet.source_group,
    source_packet_hash: packet.packet_hash,
    required_result_file: `results/${packet.context_id}.json`,
  })),
  source_files: sourceFiles,
};

fs.writeFileSync(handoffJsonPath, `${JSON.stringify(handoff, null, 2)}\n`);
fs.writeFileSync(handoffMdPath, renderHandoffMarkdown(handoff, packetMarkdownSections));

console.log("fresh reviewer handoff exported");
console.log(`contexts ${handoff.packet_count}`);
console.log(`wrote ${relativePath(resultSchemaJsonPath)}`);
console.log(`wrote ${relativePath(resultSchemaMdPath)}`);
console.log(`wrote ${relativePath(handoffJsonPath)}`);
console.log(`wrote ${relativePath(handoffMdPath)}`);
