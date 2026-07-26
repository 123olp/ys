import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");

const dataPath = path.join(webRoot, "src/data/controllable-metric-waiting-room-hypothesis.json");
const outputDir = path.join(webRoot, "src/data/controllable-metric-waiting-room-hypothesis");
const outputJsonPath = path.join(outputDir, "CITATION_CONTEXT_REVIEW_PACKET.json");
const outputMdPath = path.join(outputDir, "CITATION_CONTEXT_REVIEW_PACKET.md");

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function readJson(filePath) {
  const content = fs.readFileSync(filePath, "utf8");
  return { content, json: JSON.parse(content) };
}

function splitIds(value) {
  return String(value)
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function sourceRowsForContext(sourceById, sourceIds) {
  return sourceIds.map((id) => {
    const source = sourceById.get(id);
    return {
      id,
      author: source?.author ?? "",
      title: source?.title ?? "",
      url: source?.url ?? "",
      role: source?.role ?? "",
    };
  });
}

function claimRowsForContext(claimById, claimIds) {
  return claimIds.map((id) => {
    const claim = claimById.get(id);
    return {
      id,
      claim: claim?.claim ?? "",
      sourceId: claim?.sourceId ?? "",
      evidenceStatus: claim?.evidenceStatus ?? "",
      safeInference: claim?.safeInference ?? "",
      forbiddenInference: claim?.forbiddenInference ?? "",
    };
  });
}

function renderMarkdown(packet) {
  const indexRows = packet.details.contextPackets
    .map((row) => `| ${row.id} | ${row.claimIds.join(", ")} | ${row.sourceIds.join(", ")} | ${row.reviewStatus} | ${row.safeUse.replace(/\|/g, "\\|")} | ${row.forbiddenUse.replace(/\|/g, "\\|")} |`)
    .join("\n");

  const contextSections = packet.details.contextPackets
    .map((row) => {
      const claims = row.claims
        .map((claim) => `- \`${claim.id}\` ${claim.claim}\n  - Evidence status: ${claim.evidenceStatus}\n  - Safe inference: ${claim.safeInference}\n  - Forbidden inference: ${claim.forbiddenInference}`)
        .join("\n");
      const sources = row.sources
        .map((source) => `- \`${source.id}\` ${source.author}. ${source.title}. ${source.url}\n  - Role: ${source.role}`)
        .join("\n");
      return `### ${row.id}: ${row.context}

**Safe use**: ${row.safeUse}

**Forbidden use**: ${row.forbiddenUse}

**Claims**

${claims}

**Sources**

${sources}

**Reviewer prompt**

${row.reviewerPrompt}
`;
    })
    .join("\n");

  return `# Controllable Metric Waiting Room Citation Context Review Packet

**Generated**: ${packet.generatedAt}
**Verdict**: ${packet.verdict}

${packet.summary}

This packet is an external-review input. It is not a reviewer verdict.

## Context Index

| Context | Claims | Sources | Local status | Safe use | Forbidden use |
| --- | --- | --- | --- | --- | --- |
${indexRows}

## Reviewer Instructions

${packet.details.reviewerInstructions.map((item) => `- ${item}`).join("\n")}

## Context Packets

${contextSections}
`;
}

const { content, json } = readJson(dataPath);
const claimById = new Map(
  (json.claimEvidenceRows ?? []).map((row) => [
    row[0],
    {
      id: row[0],
      claim: row[1],
      sourceId: row[2],
      evidenceStatus: row[3],
      safeInference: row[4],
      forbiddenInference: row[5],
    },
  ]),
);
const sourceById = new Map(
  (json.sourceRows ?? []).map((row) => [
    row[0],
    {
      id: row[0],
      author: row[1],
      title: row[2],
      url: row[3],
      role: row[4],
    },
  ]),
);

const contextPackets = (json.citationContextRows ?? []).map((row) => {
  const claimIds = splitIds(row[1]);
  const sourceIds = splitIds(row[2]);
  return {
    id: row[0],
    claimIds,
    sourceIds,
    context: row[3],
    safeUse: row[4],
    forbiddenUse: row[5],
    reviewStatus: row[6],
    claims: claimRowsForContext(claimById, claimIds),
    sources: sourceRowsForContext(sourceById, sourceIds),
    reviewerPrompt: [
      `For ${row[0]}, verify source existence, metadata, and context support.`,
      `Context: ${row[3]}`,
      `Safe use: ${row[4]}`,
      `Forbidden use: ${row[5]}`,
      "Return PASS / WARN / FAIL with evidence URLs and sentence-level rationale.",
    ].join(" "),
  };
});

const packet = {
  audit: "controllable-metric-waiting-room-citation-context-review-packet",
  verdict: "READY_FOR_EXTERNAL_REVIEW",
  reasonCode: "packet_generated_no_external_judgment",
  summary:
    "Controllable metric waiting room citation contexts have been packaged for independent fresh reviewer verification. Local safe-use and forbidden-use boundaries are included, but no external reviewer verdict is claimed.",
  generatedAt: new Date().toISOString(),
  auditedInputHashes: {
    "src/data/controllable-metric-waiting-room-hypothesis.json": sha256(content),
  },
  details: {
    contextCount: contextPackets.length,
    claimCount: (json.claimEvidenceRows ?? []).length,
    sourceCount: (json.sourceRows ?? []).length,
    contextPackets,
    reviewerInstructions: [
      "Use arXiv, official science pages, or local Human Infra pages as primary evidence rather than this packet.",
      "Check whether each source supports the registered safe use.",
      "Check whether the manuscript could imply any forbidden use.",
      "Do not upgrade public black-hole explanations into engineering feasibility evidence.",
      "Do not upgrade Malament-Hogarth or black-hole boundary papers into deployable waiting-room evidence.",
      "Do not treat toy NCG, K, or P_access as empirical estimators or individual decision tools.",
      "Do not treat Human Infra internal pages as external physics, medicine, or engineering evidence.",
    ],
  },
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(outputJsonPath, `${JSON.stringify(packet, null, 2)}\n`, "utf8");
fs.writeFileSync(outputMdPath, renderMarkdown(packet), "utf8");

console.log(`controllable metric waiting room citation context packet verdict ${packet.verdict}`);
console.log(`contexts ${packet.details.contextCount}`);
console.log(`sources ${packet.details.sourceCount}`);
console.log(`wrote ${path.relative(webRoot, outputJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, outputMdPath)}`);
