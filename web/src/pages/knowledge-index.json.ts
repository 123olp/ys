import type {APIRoute} from "astro";
import {domainTierSummary, loadDomainRegistry} from "../lib/domain-registry";
import {PUBLIC_PAGES, SITE, publicUrl} from "../lib/site";

export const prerender = true;

export const GET: APIRoute = () => {
  const domains = loadDomainRegistry();
  const tiers = domainTierSummary();
  const body = {
    schema_version: "human-infra-knowledge-index.v1",
    canonical_url: publicUrl("/knowledge-index.json"),
    source_of_truth: `${SITE.repository}/blob/main/domains/_possibility-space-control/classification.tsv`,
    last_reviewed: SITE.lastReviewed,
    project: {
      id: "human-infra",
      name: SITE.name,
      alternate_name: SITE.alternateName,
      publisher: SITE.publisher,
      definition: SITE.definition,
      description: SITE.description,
      repository: SITE.repository,
      website: SITE.publicUrl,
      primary_entity: "subject-continuity",
      non_claims: [
        "The registry does not establish clinical efficacy.",
        "The registry does not establish engineering feasibility.",
        "Synthetic models are not individual lifespan predictions.",
        "Research-domain presence does not imply model admission."
      ]
    },
    vocabulary: {
      subject_continuity:
        "The continued availability of the same subject to exist, perceive, act, learn, recover, choose, and enter the future.",
      tier_relation: "classified_as",
      evidence_relation: "uses_source",
      support_relation: "supports_claim",
      falsification_relation: "falsifies_claim",
      boundary_relation: "blocked_by_boundary",
      publication_relation: "published_as"
    },
    machine_resources: {
      concise_context: publicUrl("/llms.txt"),
      full_context: publicUrl("/llms-full.txt"),
      bounded_evidence_graph: publicUrl("/evidence-graph.json"),
      monitoring_prompt_bank: publicUrl("/geo-prompt-bank.json"),
      metrics_contract: publicUrl("/geo-metrics.json")
    },
    entry_points: PUBLIC_PAGES.map((page) => ({...page, url: publicUrl(page.route)})),
    tiers: tiers.map(({domains: _domains, ...tier}) => tier),
    domains: domains.map((domain) => ({
      id: domain.domain,
      type: "ResearchDomain",
      tier: domain.tier,
      tier_name: domain.tierName,
      control_axis: domain.controlAxis,
      rationale: domain.rationale,
      review_status: domain.reviewStatus,
      repository_path: domain.physicalPath,
      source_url: `${SITE.repository}/tree/main/${domain.physicalPath}`,
      relations: [{predicate: "classified_as", object: domain.tier}]
    })),
    evidence_controls: {
      evidence_policy: `${SITE.repository}/blob/main/docs/reference/evidence-policy.md`,
      claim_evidence_matrix: `${SITE.repository}/blob/main/docs/reference/human-infra-core-claim-evidence-matrix.md`,
      bounded_evidence_graph: publicUrl("/evidence-graph.json"),
      project_boundary: `${SITE.repository}/blob/main/docs/reference/project-boundary-v0.1.md`,
      safety_boundary: `${SITE.repository}/blob/main/docs/reference/ethics-and-safety-boundaries.md`
    }
  };

  return new Response(JSON.stringify(body, null, 2), {
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "public, max-age=3600"
    }
  });
};
