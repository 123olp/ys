import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");

const dataPath = path.join(webRoot, "src/data/proper-time-differential-waiting-hypothesis.json");
const outputDir = path.join(webRoot, "src/data/proper-time-differential-waiting-hypothesis");
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
  return value
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function findReference(referenceByKey, referenceLabel) {
  const exact = referenceByKey.get(referenceLabel);
  if (exact) {
    return exact;
  }

  const normalizedLabel = referenceLabel.toLowerCase();
  for (const [key, reference] of referenceByKey.entries()) {
    const normalizedKey = key.toLowerCase();
    const normalizedTitle = reference.title.toLowerCase();
    if (normalizedLabel.includes(normalizedKey) || normalizedTitle.includes(normalizedLabel)) {
      return reference;
    }
  }

  return null;
}

function sourceRowsForContext(sourceById, referenceByKey, sourceIds) {
  return sourceIds.map((id) => {
    const source = sourceById.get(id);
    const reference = findReference(referenceByKey, source?.referenceKey ?? "");
    return {
      id,
      layer: source?.layer ?? "",
      referenceKey: source?.referenceKey ?? "",
      referenceTitle: reference?.title ?? "",
      referenceUrl: reference?.url ?? "",
      supports: source?.supports ?? "",
      doesNotSupport: source?.doesNotSupport ?? "",
    };
  });
}

function claimRowsForContext(claimById, claimIds) {
  return claimIds.map((id) => {
    const claim = claimById.get(id);
    return {
      id,
      claim: claim?.claim ?? "",
      sourceIds: claim?.sourceIds ?? [],
      evidenceRole: claim?.evidenceRole ?? "",
      boundary: claim?.boundary ?? "",
    };
  });
}

function renderMarkdown(packet) {
  const indexRows = packet.details.contextPackets
    .map((row) => `| ${row.id} | ${row.claimIds.join(", ")} | ${row.sourceIds.join(", ")} | ${row.reviewStatus} | ${row.safeUse.replace(/\|/g, "\\|")} | ${row.forbiddenUse.replace(/\|/g, "\\|")} |`)
    .join("\n");

  const contextSections = packet.details.contextPackets
    .map((row) => {
      const claims = row.claims.map((claim) => `- \`${claim.id}\` ${claim.claim}\n  - Evidence role: ${claim.evidenceRole}\n  - Boundary: ${claim.boundary}`).join("\n");
      const sources = row.sources
        .map((source) => `- \`${source.id}\` ${source.referenceKey}. ${source.referenceTitle}. ${source.referenceUrl}\n  - Supports: ${source.supports}\n  - Does not support: ${source.doesNotSupport}`)
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

  return `# Proper-Time Differential Citation Context Review Packet

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
const sourceById = new Map(
  (json.sourceCardRows ?? []).map((row) => [
    row[0],
    {
      id: row[0],
      layer: row[1],
      referenceKey: row[2],
      supports: row[3],
      doesNotSupport: row[4],
    },
  ]),
);
const claimById = new Map(
  (json.claimEvidenceRows ?? []).map((row) => [
    row[0],
    {
      id: row[0],
      claim: row[1],
      sourceIds: splitIds(row[2]),
      evidenceRole: row[3],
      boundary: row[4],
    },
  ]),
);
const referenceByKey = new Map(
  (json.referenceRows ?? []).map((row) => [
    row[0],
    {
      key: row[0],
      title: row[1],
      url: row[2],
      role: row[3],
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
    sources: sourceRowsForContext(sourceById, referenceByKey, sourceIds),
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
  audit: "proper-time-differential-citation-context-review-packet",
  verdict: "READY_FOR_EXTERNAL_REVIEW",
  reasonCode: "packet_generated_no_external_judgment",
  summary:
    "Proper-time differential citation contexts have been packaged for independent fresh reviewer verification. Local safe-use and forbidden-use boundaries are included, but no external reviewer verdict is claimed.",
  generatedAt: new Date().toISOString(),
  auditedInputHashes: {
    "src/data/proper-time-differential-waiting-hypothesis.json": sha256(content),
  },
  details: {
    contextCount: contextPackets.length,
    claimCount: (json.claimEvidenceRows ?? []).length,
    sourceCount: (json.sourceCardRows ?? []).length,
    referenceCount: (json.referenceRows ?? []).length,
    contextPackets,
    reviewerInstructions: [
      "Use publisher, arXiv, DOI, official science pages, or local Human Infra artifacts rather than this packet as proof.",
      "Check whether each source supports the registered safe use.",
      "Check whether the manuscript could imply any forbidden use.",
      "Do not upgrade public black-hole explanations into engineering feasibility evidence.",
      "Do not upgrade Malament-Hogarth or Human Infra internal theory into deployable waiting-room evidence.",
      "Do not treat NCG as an empirical estimator or individual decision tool.",
    ],
  },
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(outputJsonPath, `${JSON.stringify(packet, null, 2)}\n`, "utf8");
fs.writeFileSync(outputMdPath, renderMarkdown(packet), "utf8");

console.log(`proper-time differential citation context packet verdict ${packet.verdict}`);
console.log(`contexts ${packet.details.contextCount}`);
console.log(`sources ${packet.details.sourceCount}`);
console.log(`references ${packet.details.referenceCount}`);
console.log(`wrote ${path.relative(webRoot, outputJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, outputMdPath)}`);
