import { createHash } from "node:crypto";
import { execFile } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { promisify } from "node:util";
import { fileURLToPath } from "node:url";

const execFileAsync = promisify(execFile);
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(webRoot, "..");
const dataPath = path.join(webRoot, "src/data/effective-immortality-evidence.json");
const outputDir = path.join(webRoot, "src/data/effective-immortality-flywheel");
const verificationJsonPath = path.join(outputDir, "REFERENCE_VERIFICATION.json");
const verificationMdPath = path.join(outputDir, "REFERENCE_VERIFICATION.md");

const requestHeaders = {
  "user-agent": "human-infra-reference-verifier/0.1 (https://github.com/tradecatlabs/human_infra)",
  accept: "application/json,text/html;q=0.9,*/*;q=0.8",
};

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function normalizeText(value) {
  return String(value || "")
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, " ")
    .trim();
}

function firstAuthorFamily(authors) {
  const first = String(authors || "").split(";")[0]?.trim() || "";
  const parts = first.split(",").map((part) => part.trim()).filter(Boolean);
  return normalizeText(parts[0] || first.split(/\s+/).at(-1) || "");
}

function tokenSimilarity(a, b) {
  const left = new Set(normalizeText(a).split(/\s+/).filter(Boolean));
  const right = new Set(normalizeText(b).split(/\s+/).filter(Boolean));
  if (!left.size || !right.size) return 0;
  let intersection = 0;
  for (const token of left) if (right.has(token)) intersection += 1;
  return intersection / Math.max(left.size, right.size);
}

async function curlFetch(url, accept = "application/json,text/html;q=0.9,*/*;q=0.8") {
  const statusMarker = "\n__HTTP_STATUS__:";
  const urlMarker = "\n__EFFECTIVE_URL__:";
  try {
    const { stdout } = await execFileAsync("curl", [
      "-L",
      "--max-time",
      "20",
      "-sS",
      "-H",
      `Accept: ${accept}`,
      "-H",
      `User-Agent: ${requestHeaders["user-agent"]}`,
      "-w",
      `${statusMarker}%{http_code}${urlMarker}%{url_effective}`,
      url,
    ], { maxBuffer: 8 * 1024 * 1024 });
    const statusIndex = stdout.lastIndexOf(statusMarker);
    const urlIndex = stdout.lastIndexOf(urlMarker);
    if (statusIndex === -1 || urlIndex === -1 || urlIndex < statusIndex) {
      throw new Error("curl output missing status markers");
    }
    const body = stdout.slice(0, statusIndex);
    const status = Number(stdout.slice(statusIndex + statusMarker.length, urlIndex).trim());
    const effectiveUrl = stdout.slice(urlIndex + urlMarker.length).trim();
    return { ok: status >= 200 && status < 300, status, body, url: effectiveUrl };
  } catch (error) {
    throw new Error(error.stderr?.trim() || error.message);
  }
}

async function mapWithConcurrency(items, limit, worker) {
  const results = new Array(items.length);
  let nextIndex = 0;

  async function runWorker() {
    while (nextIndex < items.length) {
      const index = nextIndex;
      nextIndex += 1;
      results[index] = await worker(items[index], index);
    }
  }

  await Promise.all(Array.from({ length: Math.min(limit, items.length) }, runWorker));
  return results;
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function verifyCrossref(ref) {
  const doi = ref.doi.trim();
  const url = `https://api.crossref.org/works/${encodeURIComponent(doi)}`;
  try {
    let response = await curlFetch(url, "application/json,*/*;q=0.8");
    for (const delayMs of [1500, 3000, 5000]) {
      if (response.status !== 429) break;
      await sleep(delayMs);
      response = await curlFetch(url, "application/json,*/*;q=0.8");
    }
    if (!response.ok) {
      if (response.status === 429) {
        return {
          status: "WARN",
          method: "crossref",
          url,
          message: "Crossref rate limited this lookup with HTTP 429.",
        };
      }
      return {
        status: "FAIL",
        method: "crossref",
        url,
        message: `Crossref returned HTTP ${response.status}`,
      };
    }

    const payload = JSON.parse(response.body);
    const item = payload.message || {};
    const canonicalTitle = Array.isArray(item.title) ? item.title[0] : "";
    const canonicalYear = String(item.issued?.["date-parts"]?.[0]?.[0] || item.published?.["date-parts"]?.[0]?.[0] || "");
    const canonicalDoi = String(item.DOI || "").toLowerCase();
    const titleScore = tokenSimilarity(ref.title, canonicalTitle);
    const registryYear = String(ref.year || "");
    const yearMatches = registryYear === "n.d." || canonicalYear === registryYear;
    const doiMatches = canonicalDoi === doi.toLowerCase();
    const expectedFamily = firstAuthorFamily(ref.authors);
    const firstCanonicalFamily = normalizeText(item.author?.[0]?.family || "");
    const authorMatches = !expectedFamily || !firstCanonicalFamily || expectedFamily === firstCanonicalFamily;
    const failures = [];
    if (!doiMatches) failures.push(`DOI mismatch: ${canonicalDoi || "missing"}`);
    if (titleScore < 0.72) failures.push(`title similarity ${titleScore.toFixed(2)}`);
    if (!yearMatches) failures.push(`year mismatch: ${canonicalYear || "missing"}`);
    if (!authorMatches) failures.push(`first author mismatch: ${firstCanonicalFamily || "missing"}`);

    return {
      status: failures.length ? "FAIL" : "PASS",
      method: "crossref",
      url,
      message: failures.length ? failures.join("; ") : "Crossref metadata matches DOI, title, year, and first author.",
      canonical: {
        doi: item.DOI || "",
        title: canonicalTitle,
        year: canonicalYear,
        first_author_family: item.author?.[0]?.family || "",
        container: Array.isArray(item["container-title"]) ? item["container-title"][0] : "",
      },
    };
  } catch (error) {
    return {
      status: "WARN",
      method: "crossref",
      url,
      message: `Crossref lookup unavailable: ${error.message}`,
    };
  }
}

function arxivIdFromUrl(url) {
  const match = String(url || "").match(/arxiv\.org\/abs\/([^/?#]+)/i);
  return match?.[1] || "";
}

async function verifyArxiv(ref) {
  const id = arxivIdFromUrl(ref.url);
  if (!id) {
    return {
      status: "FAIL",
      method: "arxiv-api",
      url: ref.url,
      message: "arXiv entry has no parseable arXiv id.",
    };
  }

  const url = `https://export.arxiv.org/api/query?id_list=${encodeURIComponent(id)}`;
  try {
    const response = await curlFetch(url, "application/atom+xml,*/*;q=0.8");
    if (!response.ok) {
      return {
        status: "FAIL",
        method: "arxiv-api",
        url,
        message: `arXiv API returned HTTP ${response.status}`,
      };
    }
    const text = response.body;
    const title = text.match(/<title>([\s\S]*?)<\/title>/g)?.[1]?.replace(/<\/?title>/g, "").replace(/\s+/g, " ").trim() || "";
    const publishedYear = text.match(/<published>(\d{4})-/)?.[1] || "";
    const titleScore = tokenSimilarity(ref.title, title);
    const yearMatches = String(ref.year || "") === publishedYear;
    const failures = [];
    if (titleScore < 0.72) failures.push(`title similarity ${titleScore.toFixed(2)}`);
    if (!yearMatches) failures.push(`year mismatch: ${publishedYear || "missing"}`);
    return {
      status: failures.length ? "FAIL" : "PASS",
      method: "arxiv-api",
      url,
      message: failures.length ? failures.join("; ") : "arXiv API metadata matches title and year.",
      canonical: { id, title, year: publishedYear },
    };
  } catch (error) {
    return {
      status: "WARN",
      method: "arxiv-api",
      url,
      message: `arXiv lookup unavailable: ${error.message}`,
    };
  }
}

async function verifyUrl(ref) {
  if (!ref.url) {
    return {
      status: "WARN",
      method: "url",
      url: "",
      message: "No URL is registered.",
    };
  }

  if (ref.url.startsWith("/")) {
    const localPath = path.join(repoRoot, ref.url.replace(/^\//, ""));
    return {
      status: fs.existsSync(localPath) ? "PASS" : "FAIL",
      method: "local-file",
      url: ref.url,
      message: fs.existsSync(localPath) ? "Local artifact exists." : `Local artifact missing: ${localPath}`,
    };
  }

  try {
    const response = await curlFetch(ref.url, "text/html,*/*;q=0.8");
    if (response.status >= 200 && response.status < 400) {
      return {
        status: "PASS",
        method: "url",
        url: response.url || ref.url,
        message: `URL reachable with HTTP ${response.status}.`,
      };
    }
    const status = response.status === 401 || response.status === 403 ? "WARN" : "FAIL";
    return {
      status,
      method: "url",
      url: response.url || ref.url,
      message: `URL returned HTTP ${response.status}.`,
    };
  } catch (error) {
    return {
      status: "WARN",
      method: "url",
      url: ref.url,
      message: `URL lookup unavailable: ${error.message}`,
    };
  }
}

async function verifyReference(ref) {
  if (ref.entryType === "arxiv") {
    return verifyArxiv(ref);
  }
  if (ref.doi) {
    return verifyCrossref(ref);
  }
  return verifyUrl(ref);
}

function renderMarkdown(audit) {
  const rows = audit.details.per_entry
    .map((entry) => {
      return `| ${entry.key} | ${entry.entry_type} | ${entry.registry_status} | ${entry.live_status} | ${entry.method} | ${entry.message.replace(/\|/g, "\\|")} |`;
    })
    .join("\n");
  const failureRows = audit.details.per_entry
    .filter((entry) => entry.live_status !== "PASS")
    .map((entry) => `- \`${entry.key}\` (${entry.live_status}): ${entry.message}`)
    .join("\n") || "- None";

  return `# Reference Verification Report

Date: ${audit.generated_at}
Input: \`web/src/data/effective-immortality-evidence.json\`
Output JSON: \`web/src/data/effective-immortality-flywheel/REFERENCE_VERIFICATION.json\`

## Summary

Verdict: \`${audit.verdict}\`

Reason: \`${audit.reason_code}\`

${audit.summary}

| Status | Count |
| --- | ---: |
| PASS | ${audit.details.counts.PASS} |
| WARN | ${audit.details.counts.WARN} |
| FAIL | ${audit.details.counts.FAIL} |

## Non-PASS Entries

${failureRows}

## Per-Entry Verification

| Key | Type | Registry status | Live status | Method | Result |
| --- | --- | --- | --- | --- | --- |
${rows}

## Scope

This report performs primary-source reachability and metadata checks against DOI/Crossref, arXiv API, official URLs, and local project artifacts. It verifies reference existence and basic metadata consistency. It does not replace sentence-level citation-context review by an independent reviewer.
`;
}

const evidenceContent = fs.readFileSync(dataPath, "utf8");
const evidence = JSON.parse(evidenceContent);
const references = evidence.referenceRegistry || [];
if (!references.length) throw new Error("referenceRegistry is missing or empty");

const perEntry = await mapWithConcurrency(references, 2, async (ref) => {
  const result = await verifyReference(ref);
  return {
    key: ref.key,
    entry_type: ref.entryType,
    title: ref.title,
    year: ref.year,
    registry_status: ref.auditStatus,
    live_status: result.status,
    method: result.method,
    url: result.url,
    message: result.message,
    canonical: result.canonical || {},
  };
});

const counts = { PASS: 0, WARN: 0, FAIL: 0 };
for (const entry of perEntry) counts[entry.live_status] += 1;
const verdict = counts.FAIL ? "FAIL" : counts.WARN ? "WARN" : "PASS";
const audit = {
  audit_skill: "reference-registry-primary-source-verification",
  verdict,
  reason_code: counts.FAIL
    ? "reference_verification_failures"
    : counts.WARN
      ? "reference_verification_warnings"
      : "all_references_primary_source_verified",
  summary: counts.FAIL
    ? "At least one reference failed primary-source verification."
    : counts.WARN
      ? "All DOI/arXiv/local hard checks passed, but at least one URL or metadata lookup produced a warning."
      : "All Reference Registry entries passed primary-source verification.",
  generated_at: `${evidence.updated}T00:00:00.000Z`,
  audited_input_hashes: {
    "src/data/effective-immortality-evidence.json": sha256(evidenceContent),
  },
  details: {
    schema_version: evidence.schemaVersion,
    total_entries: references.length,
    counts,
    per_entry: perEntry,
  },
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(verificationJsonPath, `${JSON.stringify(audit, null, 2)}\n`);
fs.writeFileSync(verificationMdPath, renderMarkdown(audit));

console.log(`reference verification verdict ${audit.verdict}`);
console.log(`pass ${counts.PASS}`);
console.log(`warn ${counts.WARN}`);
console.log(`fail ${counts.FAIL}`);
console.log(`wrote ${path.relative(webRoot, verificationJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, verificationMdPath)}`);

if (audit.verdict === "FAIL") {
  process.exitCode = 1;
}
