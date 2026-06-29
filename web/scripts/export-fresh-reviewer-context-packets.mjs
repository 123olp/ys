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
const templatePath = path.join(outputDir, "FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.json");
const indexJsonPath = path.join(packetDir, "INDEX.json");
const indexMdPath = path.join(packetDir, "INDEX.md");

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function readJson(filePath) {
  const content = fs.readFileSync(filePath, "utf8");
  return { content, json: JSON.parse(content) };
}

function escapeCell(value) {
  return String(value ?? "").replace(/\|/gu, "\\|").replace(/\n/gu, "<br>");
}

function resultStubFor(row, protocolHash) {
  return {
    context_id: row.context_id,
    priority: row.priority,
    risk_tier: row.risk_tier,
    source_group: row.source_group,
    claims: row.claims,
    references: row.references.map((ref) => ref.key),
    source_protocol_hash: protocolHash,
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
  };
}

function renderPacketMarkdown(packet) {
  const referenceRows = packet.context.references
    .map((ref) => `| \`${ref.key}\` | ${escapeCell(ref.title || "")} | ${escapeCell(ref.audit_status)} | ${escapeCell(ref.live_status)} | ${escapeCell(ref.used_for)} |`)
    .join("\n");
  const questionRows = packet.context.reviewer_questions.map((question) => `- ${question}`).join("\n");

  return `# Fresh Reviewer Context Packet: ${packet.context.context_id}

Protocol hash: \`${packet.source_protocol_hash}\`
Packet hash: \`${packet.packet_hash}\`

## Review Boundary

This packet is for an external fresh reviewer. Do not treat local review verdicts as proof. Re-open the listed sources or PDFs, then judge whether the sources support the registered safe use and whether the manuscript violates the forbidden-use boundary.

## Context

| Field | Value |
| --- | --- |
| Priority | ${packet.context.priority} |
| Context | ${packet.context.context_id} |
| Risk tier | ${packet.context.risk_tier} |
| Risk score | ${packet.context.risk_score} |
| Source group | ${escapeCell(packet.context.source_group)} |
| Claims | ${escapeCell(packet.context.claims.join(", "))} |
| Used for | ${escapeCell(packet.context.used_for)} |
| Safe use | ${escapeCell(packet.context.safe_use)} |
| Forbidden use | ${escapeCell(packet.context.forbidden_use)} |
| Local verdict | ${escapeCell(packet.context.local_verdict)} |
| Required action before submission | ${escapeCell(packet.context.required_action_before_submission)} |

## Reviewer Questions

${questionRows}

## References

| Reference | Title | Audit status | Live status | Registered use |
| --- | --- | --- | --- | --- |
${referenceRows}

## Prompt

\`\`\`text
${packet.context.reviewer_prompt}
\`\`\`

## Result Stub

Copy this object into \`results/${packet.context.context_id}.json\` after review, replacing null values with the external reviewer verdict. Keep that per-context file in the results directory; \`npm run assemble:fresh-reviewer-results\` is the only supported way to create \`FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json\`.

\`\`\`json
${JSON.stringify(packet.result_stub, null, 2)}
\`\`\`
`;
}

function renderIndexMarkdown(index) {
  const rows = index.packets
    .map((packet) => `| ${packet.priority} | ${packet.context_id} | ${packet.risk_tier} | ${packet.risk_score} | ${escapeCell(packet.source_group)} | [MD](${packet.markdown_path}) / [JSON](${packet.json_path}) |`)
    .join("\n");

  return `# Fresh Reviewer Context Packet Index

Date: ${index.generated_at}
Protocol hash: \`${index.source_protocol_hash}\`

This directory splits the fresh reviewer citation-context queue into one packet per context. It is a consumption artifact for an external reviewer; it does not clear the fresh-reviewer gate by itself.

## Workflow

1. Review packets in priority order.
2. For each packet, re-open the source URLs, DOI pages, official pages, PDFs, or retrieval notes.
3. Fill the packet's result stub with reviewer verdicts.
4. Save each completed stub as \`results/CTX*.json\`.
5. Run \`npm run assemble:fresh-reviewer-results\` to create the canonical results ledger with input hashes.
6. Run \`npm run audit:fresh-reviewer-results\`; only a complete PASS can clear the external citation-context gate.

## Packets

| Priority | Context | Risk | Score | Source group | Files |
| ---: | --- | --- | ---: | --- | --- |
${rows}
`;
}

const protocol = readJson(protocolPath);
const protocolHash = sha256(protocol.content);
const templateHash = fs.existsSync(templatePath)
  ? sha256(fs.readFileSync(templatePath, "utf8"))
  : "not-generated-yet";

fs.mkdirSync(packetDir, { recursive: true });

const packets = protocol.json.details.review_queue.map((row) => {
  const resultStub = resultStubFor(row, protocolHash);
  const packet = {
    packet_kind: "fresh-reviewer-context-packet",
    generated_at: protocol.json.generated_at,
    source_protocol_hash: protocolHash,
    source_template_hash: templateHash,
    context: row,
    result_stub: resultStub,
  };
  const packetHash = sha256(JSON.stringify(packet, null, 2));
  const packetWithHash = { ...packet, packet_hash: packetHash };
  const baseName = row.context_id;
  const jsonPath = path.join(packetDir, `${baseName}.json`);
  const mdPath = path.join(packetDir, `${baseName}.md`);
  fs.writeFileSync(jsonPath, `${JSON.stringify(packetWithHash, null, 2)}\n`);
  fs.writeFileSync(mdPath, renderPacketMarkdown(packetWithHash));
  return {
    priority: row.priority,
    context_id: row.context_id,
    risk_tier: row.risk_tier,
    risk_score: row.risk_score,
    source_group: row.source_group,
    json_path: `./${baseName}.json`,
    markdown_path: `./${baseName}.md`,
    packet_hash: packetHash,
  };
});

const index = {
  index_kind: "fresh-reviewer-context-packet-index",
  generated_at: protocol.json.generated_at,
  source_protocol_hash: protocolHash,
  source_template_hash: templateHash,
  packet_count: packets.length,
  packets,
};

fs.writeFileSync(indexJsonPath, `${JSON.stringify(index, null, 2)}\n`);
fs.writeFileSync(indexMdPath, renderIndexMarkdown(index));

console.log("fresh reviewer context packets exported");
console.log(`contexts ${packets.length}`);
console.log(`wrote ${path.relative(webRoot, indexJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, indexMdPath)}`);
