import {existsSync, readFileSync, writeFileSync} from "node:fs";
import {resolve} from "node:path";
import process from "node:process";

const root = resolve(import.meta.dirname, "..");
const dist = resolve(root, "dist");
const baseArgumentIndex = process.argv.indexOf("--base");
const originArgumentIndex = process.argv.indexOf("--origin");
const rawBase = baseArgumentIndex >= 0 ? process.argv[baseArgumentIndex + 1] : "/human_infra";
const base = rawBase === "/" ? "" : rawBase.replace(/\/$/, "");
const publicOrigin = (
  originArgumentIndex >= 0
    ? process.argv[originArgumentIndex + 1]
    : process.env.PUBLIC_SITE_ORIGIN || process.env.CF_PAGES_URL || "https://human-infra.pages.dev"
).replace(/\/$/, "");
const expectedDomainCount = 994;
const expectedBoundedClaimCount = 30;
const expectedSourceAnchorCount = 21;
const expectedC1ClaimCount = 10;

const checks = [];

function record(id, passed, details) {
  checks.push({id, status: passed ? "pass" : "fail", details});
}

function read(relativePath) {
  const path = resolve(dist, relativePath);
  record(`exists:${relativePath}`, existsSync(path), path);
  return existsSync(path) ? readFileSync(path, "utf8") : "";
}

function routeFile(route) {
  if (route === "/") return "index.html";
  return `${route.replace(/^\//, "").replace(/\/$/, "")}/index.html`;
}

function publishedTargetFile(href) {
  if (/^(?:mailto:|tel:|#|javascript:)/.test(href)) return null;

  let pathname;
  if (href.startsWith(`${publicOrigin}${base}`)) {
    pathname = new URL(href).pathname.slice(base.length) || "/";
  } else if (href === base || href.startsWith(`${base}/`)) {
    pathname = href.slice(base.length) || "/";
  } else {
    return null;
  }

  const cleanPath = decodeURIComponent(pathname.split(/[?#]/, 1)[0]);
  if (cleanPath === "/") return "index.html";
  const relative = cleanPath.replace(/^\//, "").replace(/\/$/, "");
  return /\/[^/]+\.[^/]+$/.test(`/${relative}`) ? relative : `${relative}/index.html`;
}

const robots = read("robots.txt");
const llms = read("llms.txt");
const llmsFull = read("llms-full.txt");
const knowledgeText = read("knowledge-index.json");
const metricsText = read("geo-metrics.json");
const promptBankText = read("geo-prompt-bank.json");
const evidenceGraphText = read("evidence-graph.json");
const sitemapIndex = read("sitemap-index.xml");

record(
  "robots:sitemap",
  robots.includes(`${publicOrigin}${base}/sitemap-index.xml`),
  "robots.txt points to the canonical sitemap index"
);
record(
  "llms:full-context",
  llms.includes(`(${publicOrigin}${base}/llms-full.txt)`),
  "llms.txt links the exact full-context file URL without a trailing slash"
);
record(
  "llms:knowledge-index",
  llms.includes(`(${publicOrigin}${base}/knowledge-index.json)`),
  "llms.txt links the exact knowledge-index file URL without a trailing slash"
);
record(
  "llms:evidence-graph",
  llms.includes(`(${publicOrigin}${base}/evidence-graph.json)`),
  "llms.txt links the bounded evidence graph without a trailing slash"
);
record("llms:boundary", /does not|不|Do not infer/.test(llms), "llms.txt exposes claim boundaries");
record("llms-full:domains", llmsFull.includes("C1:") && llmsFull.includes("C6:"), "full context covers C1-C6");

let knowledge;
try {
  knowledge = JSON.parse(knowledgeText);
  record("knowledge:valid-json", true, "knowledge-index.json parsed");
} catch (error) {
  record("knowledge:valid-json", false, String(error));
  knowledge = {domains: [], entry_points: [], tiers: []};
}

let metrics;
try {
  metrics = JSON.parse(metricsText);
  record("metrics:valid-json", true, "geo-metrics.json parsed");
} catch (error) {
  record("metrics:valid-json", false, String(error));
  metrics = {metrics: []};
}

let promptBank;
try {
  promptBank = JSON.parse(promptBankText);
  record("prompt-bank:valid-json", true, "geo-prompt-bank.json parsed");
} catch (error) {
  record("prompt-bank:valid-json", false, String(error));
  promptBank = {prompts: []};
}

let evidenceGraph;
try {
  evidenceGraph = JSON.parse(evidenceGraphText);
  record("evidence-graph:valid-json", true, "evidence-graph.json parsed");
} catch (error) {
  record("evidence-graph:valid-json", false, String(error));
  evidenceGraph = {fact_cards: [], sources: [], graph: {nodes: [], edges: []}};
}

record(
  "prompt-bank:coverage",
  promptBank.prompts?.length >= 12 && new Set(promptBank.prompts.map((prompt) => prompt.category)).size >= 6,
  `${promptBank.prompts?.length ?? 0} prompts across ${new Set(promptBank.prompts?.map((prompt) => prompt.category) ?? []).size} categories`
);

record(
  "knowledge:domain-count",
  knowledge.domains?.length === expectedDomainCount,
  `expected ${expectedDomainCount}, found ${knowledge.domains?.length ?? 0}`
);
record(
  "knowledge:tier-coverage",
  knowledge.tiers?.length === 6 && knowledge.tiers.every((tier) => tier.count > 0),
  "all C1-C6 tiers have registered domains"
);
record(
  "metrics:observability-boundary",
  metrics.metrics?.some((metric) => metric.observability === "external_sampling_required" && metric.target === null),
  "external AI visibility is not represented as an observed result"
);

const factCards = evidenceGraph.fact_cards ?? [];
const evidenceSources = evidenceGraph.sources ?? [];
const evidenceNodes = evidenceGraph.graph?.nodes ?? [];
const evidenceEdges = evidenceGraph.graph?.edges ?? [];
const sourceIds = new Set(evidenceSources.map((source) => source.id));
const nodeIds = new Set(evidenceNodes.map((node) => node.id));
const edgeIds = new Set(evidenceEdges.map((edge) => edge.id));
const domainIds = new Set(factCards.map((card) => card.domain_id));
const edgesByPredicate = Object.groupBy(evidenceEdges, (edge) => edge.predicate);
const expectedSupportEdgeCount = factCards.reduce((count, card) => count + (card.source_ids?.length ?? 0), 0);
const expectedFalsifierEdgeCount = factCards.reduce((count, card) => count + (card.falsifiers?.length ?? 0), 0);
const expectedEndpointEdgeCount = factCards.reduce(
  (count, card) => count + (card.endpoint_candidates?.length ?? 0),
  0
);

record(
  "evidence-graph:claim-count",
  factCards.length === expectedBoundedClaimCount,
  `expected ${expectedBoundedClaimCount}, found ${factCards.length}`
);
record(
  "evidence-graph:source-count",
  evidenceSources.length === expectedSourceAnchorCount,
  `expected ${expectedSourceAnchorCount}, found ${evidenceSources.length}`
);
record(
  "evidence-graph:c1-coverage",
  factCards.filter((card) => card.tier === "C1").length === expectedC1ClaimCount,
  `expected ${expectedC1ClaimCount} C1 claims`
);
record(
  "evidence-graph:claim-source-coverage",
  factCards.every(
    (card) => card.source_ids?.length > 0 && card.source_ids.every((sourceId) => sourceIds.has(sourceId))
  ),
  "every bounded claim resolves to at least one registered source anchor"
);
record(
  "evidence-graph:claim-falsifier-coverage",
  factCards.every((card) => card.falsifiers?.length > 0),
  "every bounded claim exposes a falsifier or downgrade condition"
);
record(
  "evidence-graph:claim-boundary-coverage",
  factCards.every(
    (card) =>
      card.evidence_boundary &&
      card.transfer_boundary &&
      card.prohibited_uses?.length > 0 &&
      card.model_use_blocked?.includes("calibrated-prediction")
  ),
  "every bounded claim exposes transfer, prohibited-use, and model-admission boundaries"
);
record(
  "evidence-graph:source-boundary-coverage",
  evidenceSources.every(
    (source) => source.url && source.evidence_role && source.transfer_boundary && source.review_status
  ),
  "every source anchor has a URL, evidence role, transfer boundary, and review state"
);
record(
  "evidence-graph:referential-integrity",
  evidenceEdges.length > 0 &&
    evidenceEdges.every((edge) => nodeIds.has(edge.subject) && nodeIds.has(edge.object)),
  `${evidenceEdges.length} graph edges resolve to existing nodes`
);
record(
  "evidence-graph:unique-identifiers",
  nodeIds.size === evidenceNodes.length && edgeIds.size === evidenceEdges.length,
  `${nodeIds.size}/${evidenceNodes.length} unique node IDs; ${edgeIds.size}/${evidenceEdges.length} unique edge IDs`
);
record(
  "evidence-graph:source-connectivity",
  evidenceSources.every((source) =>
    evidenceEdges.some(
      (edge) => edge.predicate === "catalogs_source_anchor" && edge.object === source.id
    )
  ),
  "every source anchor is connected to the project inventory"
);
record(
  "evidence-graph:domain-edge-completeness",
  (edgesByPredicate.contains_domain?.length ?? 0) === domainIds.size &&
    (edgesByPredicate.has_bounded_claim?.length ?? 0) === factCards.length,
  `${edgesByPredicate.contains_domain?.length ?? 0}/${domainIds.size} domain edges; ` +
    `${edgesByPredicate.has_bounded_claim?.length ?? 0}/${factCards.length} claim edges`
);
record(
  "evidence-graph:source-edge-completeness",
  (edgesByPredicate.catalogs_source_anchor?.length ?? 0) === evidenceSources.length &&
    (edgesByPredicate.supports_claim_with_boundary?.length ?? 0) === expectedSupportEdgeCount,
  `${edgesByPredicate.catalogs_source_anchor?.length ?? 0}/${evidenceSources.length} catalog edges; ` +
    `${edgesByPredicate.supports_claim_with_boundary?.length ?? 0}/${expectedSupportEdgeCount} support edges`
);
record(
  "evidence-graph:review-edge-completeness",
  (edgesByPredicate.falsifies_or_downgrades_claim?.length ?? 0) === expectedFalsifierEdgeCount &&
    (edgesByPredicate.has_endpoint_candidate?.length ?? 0) === expectedEndpointEdgeCount,
  `${edgesByPredicate.falsifies_or_downgrades_claim?.length ?? 0}/${expectedFalsifierEdgeCount} falsifier edges; ` +
    `${edgesByPredicate.has_endpoint_candidate?.length ?? 0}/${expectedEndpointEdgeCount} endpoint edges`
);
record(
  "evidence-graph:support-edge-provenance",
  (edgesByPredicate.supports_claim_with_boundary?.length ?? 0) > 0 &&
    edgesByPredicate.supports_claim_with_boundary.every(
      (edge) => edge.evidence_id && edge.boundary && sourceIds.has(edge.evidence_id)
    ),
  "support edges retain source IDs and transfer boundaries"
);

const sitemapFiles = [...sitemapIndex.matchAll(/<loc>[^<]*\/([^/]+\.xml)<\/loc>/g)].map((match) => match[1]);
const sitemapBody = sitemapFiles.map((file) => read(file)).join("\n");

for (const page of knowledge.entry_points ?? []) {
  const file = routeFile(page.route);
  const html = read(file);
  const canonical = `${publicOrigin}${base}${page.route}`;
  const pageId = page.route === "/" ? "home" : page.route.replace(/^\//, "").replace(/\/$/, "");

  record(`page:${pageId}:canonical`, html.includes(`rel="canonical" href="${canonical}"`), canonical);
  record(`page:${pageId}:author`, html.includes('name="author" content="tradecatlabs"'), "publisher is explicit");
  record(`page:${pageId}:og`, html.includes('property="og:title"') && html.includes('property="og:url"'), "Open Graph metadata");
  record(`page:${pageId}:twitter`, html.includes('name="twitter:card"'), "Twitter card metadata");
  record(`page:${pageId}:jsonld`, html.includes('type="application/ld+json"'), "Schema.org JSON-LD");
  record(
    `page:${pageId}:semantic-main`,
    html.includes("<main") || /<article[^>]+class="[^"]*ltx_document/.test(html),
    "main/article document structure"
  );
  record(
    `page:${pageId}:project-base`,
    base === "" || !new RegExp(`(?:href|src)="/(?!${base.slice(1)}/)`).test(html),
    base === ""
      ? "root deployment does not require a path prefix"
      : `no project-internal asset or navigation URL escapes ${base}`
  );
  record(
    `page:${pageId}:file-url-suffix`,
    !/(?:href|src)="[^"]+\.(?:css|js|json|txt|xml|png|svg|webmanifest)\//.test(html),
    "file endpoints and static assets do not receive a directory-style trailing slash"
  );
  const linkedTargets = [...html.matchAll(/(?:href|src)="([^"]+)"/g)]
    .map((match) => publishedTargetFile(match[1]))
    .filter(Boolean);
  const missingTargets = [...new Set(linkedTargets.filter((target) => !existsSync(resolve(dist, target))))];
  record(
    `page:${pageId}:internal-targets`,
    missingTargets.length === 0,
    missingTargets.length === 0 ? `${linkedTargets.length} internal targets resolve in dist` : missingTargets.join(", ")
  );
  record(`sitemap:${pageId}`, sitemapBody.includes(canonical), canonical);
}

const passed = checks.filter((check) => check.status === "pass").length;
const failed = checks.length - passed;
const report = {
  schema_version: "human-infra-geo-readiness-audit.v1",
  generated_at: new Date().toISOString(),
  public_origin: publicOrigin,
  build_base: base,
  summary: {
    status: failed === 0 ? "pass" : "fail",
    checks: checks.length,
    passed,
    failed,
    readiness_percent: Number(((passed / checks.length) * 100).toFixed(2))
  },
  scope: {
    public_pages: knowledge.entry_points?.length ?? 0,
    registered_domains: knowledge.domains?.length ?? 0,
    bounded_claims: factCards.length,
    source_anchors: evidenceSources.length,
    evidence_graph_edges: evidenceEdges.length,
    sitemap_files: sitemapFiles.length
  },
  checks
};

writeFileSync(resolve(dist, "geo-readiness-audit.json"), `${JSON.stringify(report, null, 2)}\n`);
console.log(JSON.stringify(report.summary, null, 2));

if (failed > 0) {
  for (const check of checks.filter((item) => item.status === "fail")) {
    console.error(`FAIL ${check.id}: ${check.details}`);
  }
  process.exitCode = 1;
}
