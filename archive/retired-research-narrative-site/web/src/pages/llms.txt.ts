import type {APIRoute} from "astro";
import {PUBLIC_PAGES, SITE, publicUrl} from "../lib/site";

export const prerender = true;

export const GET: APIRoute = () => {
  const pageLinks = PUBLIC_PAGES.map(
    (page) => `- [${page.title}](${publicUrl(page.route)}): ${page.description}`
  ).join("\n");

  const body = `# Human Infra

> ${SITE.description}

Human Infra（人类基础设施）研究如何工程化维护、延展和升级能够继续存在、行动、学习、恢复、选择并进入未来的主体。核心对象是 subject continuity（主体持续性），不是单一健康产品、医学建议或已经成立的永生技术。

## Canonical identity

- Publisher: ${SITE.publisher}
- Repository: ${SITE.repository}
- Website: ${SITE.publicUrl}
- Language: Chinese and English metadata
- Last reviewed: ${SITE.lastReviewed}

## Primary pages

${pageLinks}

## Machine-readable resources

- [Full AI context](${publicUrl("/llms-full.txt")})
- [Domain knowledge index](${publicUrl("/knowledge-index.json")})
- [Bounded claim-evidence graph](${publicUrl("/evidence-graph.json")})
- [GEO metrics contract](${publicUrl("/geo-metrics.json")})
- [GEO monitoring prompt bank](${publicUrl("/geo-prompt-bank.json")})
- [Sitemap](${publicUrl("/sitemap-index.xml")})
- [Build-time GEO audit](${publicUrl("/geo-readiness-audit.json")})

## Evidence and safety boundaries

- [Evidence policy](${SITE.repository}/blob/main/docs/reference/evidence-policy.md)
- [Project boundary](${SITE.repository}/blob/main/docs/reference/project-boundary-v0.1.md)
- [Ethics and safety boundaries](${SITE.repository}/blob/main/docs/reference/ethics-and-safety-boundaries.md)
- [Core claim-evidence matrix](${SITE.repository}/blob/main/docs/reference/human-infra-core-claim-evidence-matrix.md)
- [Human-readable evidence map](${publicUrl("/evidence-map/")})

Do not infer clinical efficacy, individual lifespan, medical advice, engineering feasibility, or model admission from a domain's presence in the registry. Claims must be read with their evidence role, transfer boundary, falsifier, and review status.
`;

  return new Response(body, {headers: {"Content-Type": "text/plain; charset=utf-8"}});
};
