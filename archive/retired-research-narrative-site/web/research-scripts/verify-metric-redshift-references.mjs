import { createHash } from "node:crypto";
import { execFile } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { promisify } from "node:util";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");
const execFileAsync = promisify(execFile);

const dataPath = path.join(webRoot, "src/data/metric-redshift-recursive-waiting.json");
const outputDir = path.join(webRoot, "src/data/metric-redshift-recursive-waiting");
const outputJsonPath = path.join(outputDir, "REFERENCE_VERIFICATION.json");
const outputMdPath = path.join(outputDir, "REFERENCE_VERIFICATION.md");

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function readJson(filePath) {
  const content = fs.readFileSync(filePath, "utf8");
  return { content, json: JSON.parse(content) };
}

function routeToPagePath(route) {
  const trimmed = route.replace(/^\/+|\/+$/g, "");
  if (!trimmed) {
    return path.join(webRoot, "src/pages/index.astro");
  }
  return path.join(webRoot, "src/pages", `${trimmed}.astro`);
}

function parseCurlStatus(stdout) {
  const statuses = [...stdout.matchAll(/^HTTP\/\S+\s+(\d+)/gmu)]
    .map((match) => Number.parseInt(match[1], 10))
    .filter((status) => status !== 200 || !stdout.includes("200 Connection established"));
  if (statuses.length > 0) {
    return statuses.at(-1);
  }
  const fallbackStatuses = [...stdout.matchAll(/^HTTP\/\S+\s+(\d+)/gmu)].map((match) => Number.parseInt(match[1], 10));
  return fallbackStatuses.length > 0 ? fallbackStatuses.at(-1) : null;
}

async function curlHead(url) {
  try {
    const { stdout, stderr } = await execFileAsync("curl", [
      "-sS",
      "-I",
      "-L",
      "--max-time",
      "12",
      "--connect-timeout",
      "5",
      "-A",
      "human-infra-reference-verifier/0.1",
      url,
    ], { maxBuffer: 1024 * 1024 });
    return {
      ok: true,
      status: parseCurlStatus(stdout),
      stderr,
    };
  } catch (error) {
    return {
      ok: false,
      status: parseCurlStatus(error.stdout || ""),
      stderr: error.stderr || error.message,
    };
  }
}

async function verifyExternalUrl(source) {
  const head = await curlHead(source.url);
  if (head.status && head.status >= 200 && head.status < 400) {
    return {
      key: source.key,
      title: source.title,
      url: source.url,
      method: "CURL_HEAD",
      liveStatus: "PASS",
      statusCode: head.status,
      finalUrl: source.url,
      note: "Source URL responded successfully to curl HEAD.",
    };
  }
  const warningStatuses = new Set([401, 403, 405, 406, 408, 429, 500, 502, 503, 504]);
  return {
    key: source.key,
    title: source.title,
    url: source.url,
    method: "CURL_HEAD",
    liveStatus: head.status && !warningStatuses.has(head.status) && head.status >= 400 ? "FAIL" : "WARN",
    statusCode: head.status,
    finalUrl: source.url,
    note: head.status
      ? `curl HEAD returned ${head.status}; human review may be needed for access-controlled or transient responses.`
      : `curl HEAD did not return a target HTTP status: ${head.stderr}`,
  };
}

function verifyLocalRoute(source) {
  const pagePath = routeToPagePath(source.url);
  const exists = fs.existsSync(pagePath);
  return {
    key: source.key,
    title: source.title,
    url: source.url,
    method: "LOCAL_ROUTE",
    liveStatus: exists ? "PASS" : "FAIL",
    statusCode: exists ? 200 : 404,
    finalUrl: source.url,
    note: exists
      ? `Local route source exists at ${path.relative(webRoot, pagePath)}.`
      : `Local route source is missing at ${path.relative(webRoot, pagePath)}.`,
  };
}

function renderMarkdown(audit) {
  const rows = audit.details.perEntry
    .map((row) => `| \`${row.key}\` | ${row.liveStatus} | ${row.method} | ${row.statusCode ?? "n/a"} | ${row.url} | ${row.note.replace(/\|/g, "\\|")} |`)
    .join("\n");

  return `# Metric Redshift Reference Verification

**Generated**: ${audit.generatedAt}
**Verdict**: ${audit.verdict}

${audit.summary}

This artifact checks source-entry existence and URL accessibility. It does not prove that a source supports a manuscript claim.

## Summary

| Status | Count |
| --- | ---: |
| PASS | ${audit.details.counts.PASS || 0} |
| WARN | ${audit.details.counts.WARN || 0} |
| FAIL | ${audit.details.counts.FAIL || 0} |

## Entries

| Source | Status | Method | HTTP | URL | Note |
| --- | --- | --- | ---: | --- | --- |
${rows}
`;
}

const data = readJson(dataPath);
const sourceCards = data.json.sourceCards || [];
const perEntry = await Promise.all(sourceCards.map(async (source) => {
  if (!source.url) {
    return {
      key: source.key,
      title: source.title,
      url: "",
      method: "NONE",
      liveStatus: "FAIL",
      statusCode: null,
      finalUrl: "",
      note: "Source card has no URL.",
    };
  }
  if (source.url.startsWith("/")) {
    return verifyLocalRoute(source);
  }
  return verifyExternalUrl(source);
}));

const counts = perEntry.reduce((acc, entry) => {
  acc[entry.liveStatus] = (acc[entry.liveStatus] || 0) + 1;
  return acc;
}, {});
const verdict = counts.FAIL ? "FAIL" : counts.WARN ? "WARN" : "PASS";
const audit = {
  audit: "metric-redshift-reference-verification",
  verdict,
  reasonCode: counts.FAIL ? "source_url_failures" : counts.WARN ? "source_url_warnings" : "all_source_urls_accessible",
  summary:
    counts.FAIL
      ? "At least one metric-redshift source URL failed local primary-source verification."
      : counts.WARN
        ? "Metric-redshift source URLs were checked; at least one source returned a warning that requires human review."
        : "All metric-redshift source URLs were accessible or locally present at verification time.",
  generatedAt: new Date().toISOString(),
  auditedInputHashes: {
    "src/data/metric-redshift-recursive-waiting.json": sha256(data.content),
  },
  details: {
    sourceCount: sourceCards.length,
    counts,
    perEntry,
  },
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(outputJsonPath, `${JSON.stringify(audit, null, 2)}\n`);
fs.writeFileSync(outputMdPath, renderMarkdown(audit));

console.log(`metric-redshift reference verification verdict ${verdict}`);
console.log(`sources ${sourceCards.length}`);
console.log(`pass ${counts.PASS || 0}`);
console.log(`warn ${counts.WARN || 0}`);
console.log(`fail ${counts.FAIL || 0}`);
console.log(`wrote ${path.relative(webRoot, outputJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, outputMdPath)}`);

if (verdict === "FAIL") {
  process.exitCode = 1;
}
