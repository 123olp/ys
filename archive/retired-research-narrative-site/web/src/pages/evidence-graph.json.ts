import type {APIRoute} from "astro";
import {loadEvidenceRegistry} from "../lib/evidence-registry";
import {SITE, publicUrl} from "../lib/site";

export const prerender = true;

export const GET: APIRoute = () => {
  const registry = loadEvidenceRegistry();
  const domainIds = [...new Set(registry.claims.map((claim) => claim.domain_id))];
  const nodes: Array<Record<string, unknown>> = [
    {
      id: "human-infra",
      type: "ResearchProject",
      name: SITE.name,
      url: SITE.publicUrl
    },
    ...domainIds.map((domainId) => {
      const claim = registry.claims.find((candidate) => candidate.domain_id === domainId)!;
      return {
        id: `domain:${domainId}`,
        type: "ResearchDomain",
        name: domainId,
        tier: claim.tier,
        repository_path: claim.repository_path
      };
    }),
    ...registry.sources,
    ...registry.claims.flatMap((claim) => [
      {
        id: claim.id,
        type: claim.type,
        text: claim.claim,
        model_position: claim.model_position,
        review_status: claim.review_status,
        evidence_boundary: claim.evidence_boundary,
        transfer_boundary: claim.transfer_boundary,
        prohibited_uses: claim.prohibited_uses
      },
      ...claim.falsifiers.map((falsifier) => ({
        id: falsifier.id,
        type: "Falsifier",
        condition: falsifier.condition,
        downgrade_action: falsifier.downgradeAction,
        evidence_needed: falsifier.evidenceNeeded
      })),
      ...claim.endpoint_candidates.map((endpoint, index) => ({
        id: `${claim.id}-E${index + 1}`,
        type: "EndpointCandidate",
        name: endpoint,
        admission_status: "candidate-not-calibrated"
      }))
    ])
  ];

  const edges: Array<Record<string, unknown>> = [
    ...domainIds.map((domainId) => ({
      id: `edge:project:${domainId}`,
      subject: "human-infra",
      predicate: "contains_domain",
      object: `domain:${domainId}`,
      provenance: "domains/_possibility-space-control/classification.tsv"
    })),
    ...registry.sources.map((source) => ({
      id: `edge:project-source:${source.id}`,
      subject: "human-infra",
      predicate: "catalogs_source_anchor",
      object: source.id,
      provenance: registry.source_registry_ids.source_register
    }))
  ];
  for (const claim of registry.claims) {
    const domainId = `domain:${claim.domain_id}`;
    edges.push({
      id: `edge:domain-claim:${claim.id}`,
      subject: domainId,
      predicate: "has_bounded_claim",
      object: claim.id,
      provenance: registry.source_registry_ids.claim_matrix
    });

    claim.source_ids.forEach((sourceId) => {
      edges.push({
        id: `edge:source-claim:${sourceId}:${claim.id}`,
        subject: sourceId,
        predicate: "supports_claim_with_boundary",
        object: claim.id,
        evidence_id: sourceId,
        boundary: registry.sources.find((source) => source.id === sourceId)?.transfer_boundary
      });
    });
    claim.falsifiers.forEach((falsifier) => {
      edges.push({
        id: `edge:falsifier-claim:${falsifier.id}`,
        subject: falsifier.id,
        predicate: "falsifies_or_downgrades_claim",
        object: claim.id,
        provenance: registry.source_registry_ids.falsifier_register
      });
    });
    claim.endpoint_candidates.forEach((_endpoint, index) => {
      edges.push({
        id: `edge:claim-endpoint:${claim.id}:${index + 1}`,
        subject: claim.id,
        predicate: "has_endpoint_candidate",
        object: `${claim.id}-E${index + 1}`,
        provenance: registry.source_registry_ids.field_register
      });
    });
  }

  const body = {
    schema_version: "human-infra-evidence-graph.v1",
    canonical_url: publicUrl("/evidence-graph.json"),
    publisher: SITE.publisher,
    last_reviewed: SITE.lastReviewed,
    generated_from: Object.entries(registry.source_registry_ids).map(([role, id]) => ({role, id})),
    summary: {
      ...registry.summary,
      node_count: nodes.length,
      edge_count: edges.length
    },
    evidence_status: "bounded-source-anchor-projection-not-calibrated-model-input",
    limitations: registry.limitations,
    relation_vocabulary: {
      contains_domain: "The project registry contains the research domain.",
      catalogs_source_anchor: "The project evidence registry catalogs the bounded source anchor.",
      has_bounded_claim: "The domain has a claim constrained by evidence and transfer boundaries.",
      supports_claim_with_boundary: "The source supports only the stated evidence role and boundary.",
      falsifies_or_downgrades_claim: "The condition blocks, falsifies, or downgrades the claim.",
      has_endpoint_candidate: "The claim exposes a candidate outcome that still requires source-specific extraction."
    },
    fact_cards: registry.claims,
    sources: registry.sources,
    graph: {nodes, edges}
  };

  return new Response(JSON.stringify(body, null, 2), {
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "public, max-age=3600"
    }
  });
};
