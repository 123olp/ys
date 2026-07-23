import type {APIRoute} from "astro";
import {domainTierSummary, loadDomainRegistry} from "../lib/domain-registry";
import {PUBLIC_PAGES, SITE, publicUrl} from "../lib/site";

export const prerender = true;

export const GET: APIRoute = () => {
  const domains = loadDomainRegistry();
  const tiers = domainTierSummary();
  const tierText = tiers
    .map(
      (tier) =>
        `## ${tier.id}: ${tier.name} (${tier.count})\n\n${tier.question}\n\n${tier.domains
          .map((domain) => `- ${domain.domain}: ${domain.rationale}`)
          .join("\n")}`
    )
    .join("\n\n");

  const pages = PUBLIC_PAGES.map(
    (page) => `- ${page.title}: ${publicUrl(page.route)} — ${page.description}`
  ).join("\n");

  const body = `# Human Infra: full machine context

Publisher: ${SITE.publisher}
Canonical URL: ${SITE.publicUrl}
Repository: ${SITE.repository}
Last reviewed: ${SITE.lastReviewed}
Registry source: domains/_possibility-space-control/classification.tsv
Registered domains: ${domains.length}

## Normative definition

${SITE.definition}

Human Infra treats subject continuity as a boundary condition for value realization. Goals, judgments, learning, creation, and future choice presuppose a subject that can continue to exist and act. The project therefore studies the biological, cognitive, technical, environmental, resource, institutional, and collaborative conditions that keep that subject available.

## C0-C6 implementation chain

C0 subject continuity -> C1 rewrite boundaries -> C2 maintain the source body -> C3 strengthen generation -> C4 open conversion channels -> C5 sustain the ecology -> C6 unlock local blockers.

The tier system measures possibility-space control, rootness, and long-horizon effect. It does not rank present-day feasibility or clinical readiness.

## Claim boundary

The repository is an evidence-governed knowledge base and research protocol system. A registered domain is a research object, not proof that an intervention works. Synthetic life-path models are not individualized predictions. Speculative papers do not prove physical or engineering feasibility. Health-related material is not medical advice.

## Primary public pages

${pages}

## Evidence controls

- Evidence policy: ${SITE.repository}/blob/main/docs/reference/evidence-policy.md
- Core claim-evidence matrix: ${SITE.repository}/blob/main/docs/reference/human-infra-core-claim-evidence-matrix.md
- Project boundary: ${SITE.repository}/blob/main/docs/reference/project-boundary-v0.1.md
- Ethics and safety: ${SITE.repository}/blob/main/docs/reference/ethics-and-safety-boundaries.md
- Research standards: ${publicUrl("/research-standards/")}
- Machine knowledge index: ${publicUrl("/knowledge-index.json")}
- Human-readable evidence map: ${publicUrl("/evidence-map/")}
- Bounded claim-evidence graph: ${publicUrl("/evidence-graph.json")}

The evidence graph currently projects 30 priority-domain claims, 21 source anchors, candidate endpoints, falsifiers, and prohibited uses from repository registers. It is a bounded source-anchor projection. It is not an independent fresh review and does not admit claims to calibrated prediction or intervention ranking.

${tierText}
`;

  return new Response(body, {headers: {"Content-Type": "text/plain; charset=utf-8"}});
};
