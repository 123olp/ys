import type {APIRoute} from "astro";
import {SITE, publicUrl} from "../lib/site";

export const prerender = true;

const metrics = [
  ["crawl_entry_coverage", "automated", "percent", 100, "robots, sitemap, llms and canonical entry points"],
  ["public_page_metadata_coverage", "automated", "percent", 100, "canonical, description, author, OG, Twitter and JSON-LD"],
  ["public_page_sitemap_coverage", "automated", "percent", 100, "registered public pages present in sitemap"],
  ["domain_registry_coverage", "automated", "percent", 100, "classified domains present in knowledge-index.json"],
  ["bounded_claim_source_coverage", "automated", "percent", 100, "every published bounded claim references an existing source anchor"],
  ["bounded_claim_falsifier_coverage", "automated", "percent", 100, "every published bounded claim exposes at least one falsifier or downgrade condition"],
  ["source_transfer_boundary_coverage", "automated", "percent", 100, "every published source anchor exposes its transfer boundary"],
  ["evidence_graph_referential_integrity", "automated", "percent", 100, "every evidence-graph edge resolves to existing subject and object nodes"],
  ["internal_root_path_violations", "automated", "count", 0, "project-page builds must not emit origin-root internal URLs"],
  ["ai_brand_presence_rate", "external_sampling_required", "percent", null, "repeated prompt-bank samples per engine"],
  ["ai_candidate_rate", "external_sampling_required", "percent", null, "Human Infra appears as a relevant candidate"],
  ["ai_recommendation_rate", "external_sampling_required", "percent", null, "explicit recommendation in eligible prompts"],
  ["answer_citation_rate", "external_sampling_required", "percent", null, "answers cite a canonical Human Infra source"],
  ["description_accuracy_rate", "external_sampling_required", "percent", null, "answers preserve definition and safety boundaries"],
  ["qualified_visit_conversion", "analytics_required", "percent", null, "visit reaches research, repository, community or citation action"]
].map(([id, observability, unit, target, definition]) => ({id, observability, unit, target, definition}));

export const GET: APIRoute = () =>
  new Response(
    JSON.stringify(
      {
        schema_version: "human-infra-geo-metrics.v1",
        canonical_url: publicUrl("/geo-metrics.json"),
        publisher: SITE.publisher,
        last_reviewed: SITE.lastReviewed,
        attribution_levels: ["observed", "recoverable", "unobservable"],
        measurement_rule:
          "Technical readiness is measured in build output. AI visibility metrics require engine-specific repeated samples, a fixed prompt bank, a baseline window, an observation window, and external-event notes. No ranking or citation uplift is claimed without those observations.",
        metrics
      },
      null,
      2
    ),
    {headers: {"Content-Type": "application/json; charset=utf-8"}}
  );
