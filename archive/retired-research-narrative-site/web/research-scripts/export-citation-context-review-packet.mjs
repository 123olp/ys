import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");
const dataPath = path.join(webRoot, "src/data/effective-immortality-evidence.json");
const outputDir = path.join(webRoot, "src/data/effective-immortality-flywheel");
const outputJsonPath = path.join(outputDir, "CITATION_CONTEXT_REVIEW_PACKET.json");
const outputMdPath = path.join(outputDir, "CITATION_CONTEXT_REVIEW_PACKET.md");

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function sortedUnique(values) {
  return [...new Set(values)].sort((a, b) => a.localeCompare(b));
}

function referencesForContext(references, contextId) {
  return references
    .filter((ref) => (ref.citationContexts || []).includes(contextId))
    .map((ref) => ({
      key: ref.key,
      entry_type: ref.entryType,
      authors: ref.authors,
      year: ref.year,
      title: ref.title,
      venue: ref.venue,
      doi: ref.doi || "",
      url: ref.url || "",
      used_for: ref.usedFor,
      audit_status: ref.auditStatus,
    }))
    .sort((a, b) => a.key.localeCompare(b.key));
}

function claimsForContext(claimMap, contextId) {
  return claimMap
    .filter((row) => (row.citationContexts || []).includes(contextId))
    .map((row) => row.claimId)
    .sort((a, b) => a.localeCompare(b));
}

function renderReferenceList(refs) {
  return refs
    .map((ref) => {
      const locator = ref.doi ? `DOI: ${ref.doi}` : `URL: ${ref.url}`;
      return `  - \`${ref.key}\` (${ref.year}). ${ref.title}. ${locator}. Local status: ${ref.audit_status}.`;
    })
    .join("\n");
}

function renderMarkdown(packet) {
  const claimSections = packet.details.claim_packets
    .map((claim) => {
      const contextBlocks = claim.contexts
        .map((context) => `#### ${context.context_id}: ${context.source_group}

- Used for: ${context.used_for}
- Supports: ${context.supports}
- Does not support: ${context.does_not_support}
- Local citation status: ${context.citation_status}
- References:
${renderReferenceList(context.references)}
`)
        .join("\n");

      return `### ${claim.claim_id}: ${claim.claim_text}

- Claim type: ${claim.claim_type}
- Current status: ${claim.current_status}
- Alignment verdict: ${claim.alignment_verdict}
- Current support: ${claim.current_support}
- Evidence edges: ${claim.evidence_edges.join("; ")}
- Falsifiers: ${claim.falsifiers.join("; ")}
- Upgrade gate: ${claim.upgrade_gate}

${contextBlocks}`;
    })
    .join("\n");

  const contextRows = packet.details.context_packets
    .map((context) => `| ${context.context_id} | ${context.claims.join(", ")} | ${context.reference_count} | ${context.citation_status} | ${context.does_not_support.replace(/\|/g, "\\|")} |`)
    .join("\n");

  return `# Citation Context Review Packet

Date: ${packet.generated_at}
Input: \`web/src/data/effective-immortality-evidence.json\`
Output JSON: \`web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_REVIEW_PACKET.json\`

## Status

Verdict: \`${packet.verdict}\`

Reason: \`${packet.reason_code}\`

${packet.summary}

This packet is designed for a fresh reviewer thread. It is not a reviewer verdict.

## Fresh Reviewer Instructions

${packet.details.reviewer_instructions.map((item) => `- ${item}`).join("\n")}

## Review Questions

${packet.details.review_questions.map((item, index) => `${index + 1}. ${item}`).join("\n")}

## Packet Metrics

| Metric | Count |
| --- | ---: |
| Claims | ${packet.details.claim_count} |
| Citation contexts | ${packet.details.context_count} |
| Reference entries | ${packet.details.reference_count} |
| Claim-context links | ${packet.details.claim_context_link_count} |
| Context-reference links | ${packet.details.context_reference_link_count} |

## Context Index

| Context | Claims using it | References | Local status | Non-support boundary |
| --- | --- | ---: | --- | --- |
${contextRows}

## Claim Review Packets

${claimSections}

## Required Reviewer Output

For every claim-context-reference group, return:

\`\`\`text
CLAIM_ID:
CONTEXT_ID:
REFERENCE_KEYS:
EXISTENCE: YES / NO / UNCERTAIN
METADATA: CORRECT / FIX_NEEDED / UNCERTAIN
CONTEXT_SUPPORT: SUPPORTS / WEAK / WRONG / AMBIGUOUS
BOUNDARY_OK: YES / NO
RATIONALE:
ACTION: KEEP / FIX_METADATA / SOFTEN_CLAIM / REPLACE_CITATION / REMOVE_CITATION
\`\`\`

The reviewer must use web/DBLP/arXiv/DOI/publisher lookups and must not rely on this packet as proof that a source supports a claim.
`;
}

const evidenceContent = fs.readFileSync(dataPath, "utf8");
const evidence = JSON.parse(evidenceContent);

const claims = evidence.claimRegister || [];
const claimMap = evidence.claimEvidenceMap || [];
const contexts = evidence.citationContextRegister || [];
const references = evidence.referenceRegistry || [];

const claimById = new Map(claims.map((claim) => [claim.id, claim]));
const contextById = new Map(contexts.map((context) => [context.id, context]));

const claimPackets = claimMap.map((row) => {
  const claim = claimById.get(row.claimId) || {};
  return {
    claim_id: row.claimId,
    claim_text: claim.claim || "",
    claim_type: claim.claimType || "",
    current_status: claim.currentStatus || "",
    upgrade_condition: claim.requiredUpgrade || "",
    paper_sections: row.paperSections || [],
    evidence_edges: row.evidenceEdges || [],
    alignment_verdict: row.alignmentVerdict,
    current_support: row.currentSupport,
    falsifiers: row.falsifiers || [],
    upgrade_gate: row.upgradeGate,
    contexts: (row.citationContexts || []).map((contextId) => {
      const context = contextById.get(contextId) || {};
      const contextReferences = referencesForContext(references, contextId);
      return {
        context_id: contextId,
        source_group: context.sourceGroup || "",
        canonical_record: context.canonicalRecord || "",
        used_for: context.usedFor || "",
        supports: context.supports || "",
        does_not_support: context.doesNotSupport || "",
        citation_status: context.citationStatus || "",
        references: contextReferences,
      };
    }),
  };
});

const contextPackets = contexts.map((context) => {
  const refs = referencesForContext(references, context.id);
  return {
    context_id: context.id,
    source_group: context.sourceGroup,
    used_for: context.usedFor,
    supports: context.supports,
    does_not_support: context.doesNotSupport,
    citation_status: context.citationStatus,
    claims: claimsForContext(claimMap, context.id),
    reference_count: refs.length,
    references: refs,
  };
});

const contextReferenceLinkCount = contextPackets.reduce((total, context) => total + context.reference_count, 0);
const claimContextLinkCount = claimPackets.reduce((total, claim) => total + claim.contexts.length, 0);

const packet = {
  audit_skill: "citation-context-review-packet",
  verdict: "READY_FOR_EXTERNAL_REVIEW",
  reason_code: "packet_generated_no_external_judgment",
  summary:
    "A structured packet for fresh reviewer sentence-level citation-context review has been generated from the Claim Register, Claim Evidence Map, Citation Context Register, and Reference Registry.",
  generated_at: `${evidence.updated}T00:00:00.000Z`,
  audited_input_hashes: {
    "src/data/effective-immortality-evidence.json": sha256(evidenceContent),
  },
  details: {
    schema_version: evidence.schemaVersion,
    claim_count: claims.length,
    context_count: contexts.length,
    reference_count: references.length,
    claim_context_link_count: claimContextLinkCount,
    context_reference_link_count: contextReferenceLinkCount,
    reviewer_instructions: [
      "Use a fresh context with no prior conversation state.",
      "Verify source existence and metadata through DOI, arXiv, PubMed, publisher, official standard, or official registry pages.",
      "Judge whether the cited source supports the exact claim and context, not merely a related topic.",
      "Preserve the does-not-support boundary when the reference only provides method language, governance language, association evidence, or task-limited evidence.",
      "Flag any source used to support effective immortality, lifespan extension, or individual prediction when it only supports a weaker claim.",
    ],
    review_questions: [
      "Does each reference exist and match the registered title, authors, year, venue, DOI or URL?",
      "Does each reference support the exact usedFor claim for its citation context?",
      "Does any prose overstate a method source, governance framework, observational association, mechanism review, or task-limited AI study?",
      "Are all doesNotSupport boundaries honored by the current working paper and Web page?",
      "Should any claim be softened, any citation replaced, or any reference removed?",
    ],
    claim_packets: claimPackets,
    context_packets: contextPackets,
  },
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(outputJsonPath, `${JSON.stringify(packet, null, 2)}\n`);
fs.writeFileSync(outputMdPath, renderMarkdown(packet));

console.log(`citation-context review packet ${packet.verdict}`);
console.log(`claims ${claims.length}`);
console.log(`contexts ${contexts.length}`);
console.log(`references ${references.length}`);
console.log(`claim-context links ${claimContextLinkCount}`);
console.log(`context-reference links ${contextReferenceLinkCount}`);
console.log(`wrote ${path.relative(webRoot, outputJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, outputMdPath)}`);
