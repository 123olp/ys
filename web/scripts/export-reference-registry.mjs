import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");
const dataPath = path.join(webRoot, "src/data/effective-immortality-evidence.json");
const outputDir = path.join(webRoot, "src/data/effective-immortality-flywheel");
const bibPath = path.join(outputDir, "references.bib");
const auditJsonPath = path.join(outputDir, "CITATION_AUDIT.json");
const auditMdPath = path.join(outputDir, "CITATION_AUDIT.md");

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function bibType(entryType) {
  const mapping = {
    article: "article",
    inproceedings: "inproceedings",
    book: "book",
    report: "techreport",
    arxiv: "misc",
    standard: "misc",
    "official-web": "misc",
    "guideline-web": "misc",
    registry: "misc",
    encyclopedia: "misc",
    "project-note": "misc",
  };
  return mapping[entryType] || "misc";
}

function normalizeAuthors(authors) {
  if (!authors) return "";
  return authors
    .split(";")
    .map((author) => author.trim())
    .filter(Boolean)
    .join(" and ");
}

function escapeBibtex(value) {
  return String(value)
    .replace(/\\/g, "\\textbackslash{}")
    .replace(/[{}]/g, "")
    .trim();
}

function pushField(lines, field, value) {
  if (!value) return;
  lines.push(`  ${field} = {${escapeBibtex(value)}},`);
}

function renderBibEntry(ref) {
  const type = bibType(ref.entryType);
  const lines = [`@${type}{${ref.key},`];
  pushField(lines, "author", normalizeAuthors(ref.authors));
  pushField(lines, "title", ref.title);

  if (type === "article") {
    pushField(lines, "journal", ref.venue);
  } else if (type === "inproceedings") {
    pushField(lines, "booktitle", ref.venue);
  } else if (type === "book") {
    pushField(lines, "publisher", ref.venue);
  } else if (type === "techreport") {
    pushField(lines, "institution", ref.venue);
  } else {
    pushField(lines, "howpublished", ref.venue);
  }

  pushField(lines, "year", ref.year);
  pushField(lines, "volume", ref.volume);
  pushField(lines, "number", ref.issue);
  pushField(lines, "pages", ref.pages);
  pushField(lines, "doi", ref.doi);
  pushField(lines, "url", ref.url);

  if (ref.entryType === "arxiv") {
    const match = ref.url.match(/arxiv\.org\/abs\/([^/?#]+)/i);
    pushField(lines, "eprint", match?.[1] || "");
    pushField(lines, "archivePrefix", "arXiv");
  }

  pushField(lines, "note", `auditStatus=${ref.auditStatus}; usedFor=${ref.usedFor}`);
  if (lines.length > 1) {
    lines[lines.length - 1] = lines[lines.length - 1].replace(/,$/, "");
  }
  lines.push("}");
  return lines.join("\n");
}

function renderAuditJson(evidence, bibContent) {
  const generatedAt = `${evidence.updated}T00:00:00.000Z`;
  const refs = evidence.referenceRegistry;
  const perEntry = refs.map((ref) => ({
    key: ref.key,
    verdict: "KEEP",
    axis_failures: [],
    note: `${ref.auditStatus}: ${ref.usedFor}`,
    metadata: {
      entry_type: ref.entryType,
      title: ref.title,
      year: ref.year,
      venue: ref.venue,
      doi: ref.doi,
      url: ref.url,
      audit_status: ref.auditStatus,
    },
    uses: ref.citationContexts.map((contextId) => ({
      file: "web/src/data/effective-immortality-evidence.json",
      verdict: "SUPPORTS",
      note: `Bounded citation context ${contextId}`,
    })),
  }));

  return {
    audit_skill: "citation-audit",
    verdict: "WARN",
    reason_code: "metadata_registry_without_fresh_reviewer",
    summary:
      "Reference Registry exported to BibTeX and machine-readable audit ledger; metadata is locally verified, but no fresh reviewer thread has audited every prose citation context.",
    audited_input_hashes: {
      "src/data/effective-immortality-evidence.json": sha256(
        fs.readFileSync(dataPath, "utf8"),
      ),
      "src/data/effective-immortality-flywheel/references.bib": sha256(bibContent),
    },
    trace_path: "docs/source-notes/2026-06-28-effective-immortality-flywheel-citation-audit.md",
    thread_id: "not-invoked-local-registry-export",
    reviewer_model: "not_invoked",
    reviewer_reasoning: "not_invoked",
    generated_at: generatedAt,
    details: {
      total_entries: refs.length,
      counts: { KEEP: refs.length, FIX: 0, REPLACE: 0, REMOVE: 0 },
      per_entry: perEntry,
      assurance_limitations: [
        "This JSON is generated from the local Reference Registry, not from a fresh cross-model citation-audit reviewer thread.",
        "Run npm run verify:references for live DOI/Crossref, arXiv API, official URL, and local artifact verification; see REFERENCE_VERIFICATION.json and REFERENCE_VERIFICATION.md.",
        "The Web paper does not yet use LaTeX \\cite commands, so sentence-level cite contexts are represented by citationContextRegister IDs.",
        "Official-web entries use URL reachability and source identity instead of fabricated DOI fields.",
      ],
    },
  };
}

function renderAuditMarkdown(audit) {
  const rows = audit.details.per_entry
    .map((entry) => {
      const meta = entry.metadata;
      return `| ${entry.key} | ${meta.entry_type} | ${meta.year} | ${meta.doi || meta.url} | ${meta.audit_status} | KEEP |`;
    })
    .join("\n");

  return `# Citation Audit Report

Date: ${audit.generated_at}
Input: \`web/src/data/effective-immortality-evidence.json\`
Bib file: \`web/src/data/effective-immortality-flywheel/references.bib\`
JSON ledger: \`web/src/data/effective-immortality-flywheel/CITATION_AUDIT.json\`

## Summary

Verdict: \`${audit.verdict}\`

Reason: \`${audit.reason_code}\`

${audit.summary}

| Verdict | Count |
| --- | ---: |
| KEEP | ${audit.details.counts.KEEP} |
| FIX | ${audit.details.counts.FIX} |
| REPLACE | ${audit.details.counts.REPLACE} |
| REMOVE | ${audit.details.counts.REMOVE} |

## Scope

This audit is generated from the structured Reference Registry. It verifies that the Web paper has a machine-readable bibliography surface and records per-entry metadata status. It does not claim a full fresh reviewer audit over every prose citation context.

## Per-Entry Ledger

| Key | Type | Year | DOI / URL | Metadata status | Verdict |
| --- | --- | --- | --- | --- | --- |
${rows}

## Assurance Limitations

${audit.details.assurance_limitations.map((item) => `- ${item}`).join("\n")}
`;
}

const evidence = JSON.parse(fs.readFileSync(dataPath, "utf8"));
if (!Array.isArray(evidence.referenceRegistry) || evidence.referenceRegistry.length === 0) {
  throw new Error("referenceRegistry is missing or empty");
}

const bibContent = `${evidence.referenceRegistry.map(renderBibEntry).join("\n\n")}\n`;
const auditJson = renderAuditJson(evidence, bibContent);
const auditMd = renderAuditMarkdown(auditJson);

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(bibPath, bibContent);
fs.writeFileSync(auditJsonPath, `${JSON.stringify(auditJson, null, 2)}\n`);
fs.writeFileSync(auditMdPath, auditMd);

console.log(`wrote ${path.relative(webRoot, bibPath)}`);
console.log(`wrote ${path.relative(webRoot, auditJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, auditMdPath)}`);
