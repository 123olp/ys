import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");

const dataPath = path.join(webRoot, "src/data/metric-redshift-recursive-waiting.json");
const outputDir = path.join(webRoot, "src/data/metric-redshift-recursive-waiting");
const outputJsonPath = path.join(outputDir, "CITATION_CONTEXT_REVIEW_PACKET.json");
const outputMdPath = path.join(outputDir, "CITATION_CONTEXT_REVIEW_PACKET.md");

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function readJson(filePath) {
  const content = fs.readFileSync(filePath, "utf8");
  return { content, json: JSON.parse(content) };
}

function sourceRowsForContext(sourceByKey, context) {
  return (context.sourceKeys || []).map((key) => {
    const source = sourceByKey.get(key);
    return {
      key,
      title: source?.title || "",
      authors: source?.authors || "",
      year: source?.year || "",
      url: source?.url || "",
      evidenceLayer: source?.evidenceLayer || "",
      supports: source?.supports || "",
      doesNotSupport: source?.doesNotSupport || "",
    };
  });
}

function claimRowsForContext(claimById, context) {
  return (context.claimIds || []).map((claimId) => {
    const claim = claimById.get(claimId);
    return {
      id: claimId,
      claim: claim?.claim || "",
      claimType: claim?.claimType || "",
      section: claim?.section || "",
    };
  });
}

function renderMarkdown(packet) {
  const indexRows = packet.details.contextPackets
    .map((row) => `| ${row.id} | ${row.claimIds.join(", ")} | ${row.sourceKeys.join(", ")} | ${row.localReviewStatus} | ${row.safeUse.replace(/\|/g, "\\|")} | ${row.forbiddenUse.replace(/\|/g, "\\|")} |`)
    .join("\n");

  const contextSections = packet.details.contextPackets
    .map((row) => {
      const claims = row.claims.map((claim) => `- \`${claim.id}\` ${claim.claim}`).join("\n");
      const sources = row.sources
        .map((source) => `- \`${source.key}\` (${source.year}). ${source.title}. ${source.url}\n  - Supports: ${source.supports}\n  - Does not support: ${source.doesNotSupport}`)
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

  return `# Metric Redshift Citation Context Review Packet

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

const data = readJson(dataPath);
const sourceByKey = new Map((data.json.sourceCards || []).map((source) => [source.key, source]));
const claimById = new Map((data.json.claimRegister || []).map((claim) => [claim.id, claim]));

const contextPackets = (data.json.citationContextRegister || []).map((context) => {
  const sources = sourceRowsForContext(sourceByKey, context);
  const claims = claimRowsForContext(claimById, context);
  return {
    id: context.id,
    context: context.context,
    claimIds: context.claimIds || [],
    sourceKeys: context.sourceKeys || [],
    safeUse: context.safeUse,
    forbiddenUse: context.forbiddenUse,
    localReviewStatus: context.reviewStatus,
    claims,
    sources,
    reviewerPrompt: [
      `For ${context.id}, verify source existence, metadata, and context support.`,
      `Safe use: ${context.safeUse}`,
      `Forbidden use: ${context.forbiddenUse}`,
      "Return PASS / WARN / FAIL with evidence URLs and sentence-level rationale.",
    ].join(" "),
  };
});

const packet = {
  audit: "metric-redshift-citation-context-review-packet",
  verdict: "READY_FOR_EXTERNAL_REVIEW",
  reasonCode: "packet_generated_no_external_judgment",
  summary:
    "MRW citation contexts have been packaged for independent fresh reviewer verification. Local safe-use and forbidden-use boundaries are included, but no external reviewer verdict is claimed.",
  generatedAt: new Date().toISOString(),
  auditedInputHashes: {
    "src/data/metric-redshift-recursive-waiting.json": sha256(data.content),
  },
  details: {
    contextCount: contextPackets.length,
    claimCount: (data.json.claimRegister || []).length,
    sourceCount: (data.json.sourceCards || []).length,
    contextPackets,
    reviewerInstructions: [
      "Use publisher, arXiv, DOI, or official source lookups rather than this packet as evidence.",
      "Check whether each source supports the registered safe use.",
      "Check whether the manuscript or caption could imply any forbidden use.",
      "Do not upgrade NASA public pages into engineering feasibility evidence.",
      "Do not upgrade Malament-Hogarth or time-travel philosophy sources into human waiting engineering evidence.",
    ],
  },
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(outputJsonPath, `${JSON.stringify(packet, null, 2)}\n`);
fs.writeFileSync(outputMdPath, renderMarkdown(packet));

console.log(`metric-redshift citation context packet verdict ${packet.verdict}`);
console.log(`contexts ${packet.details.contextCount}`);
console.log(`sources ${packet.details.sourceCount}`);
console.log(`wrote ${path.relative(webRoot, outputJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, outputMdPath)}`);
