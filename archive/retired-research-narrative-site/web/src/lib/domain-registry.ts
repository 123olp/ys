import {readFileSync} from "node:fs";
import {resolve} from "node:path";
import {tsvParse} from "d3";
import {TIER_DEFINITIONS} from "./site";

export type DomainRecord = {
  domain: string;
  tier: string;
  tierName: string;
  controlAxis: string;
  physicalPath: string;
  rationale: string;
  reviewStatus: string;
};

const registryPath = resolve(
  process.cwd(),
  "../domains/_possibility-space-control/classification.tsv"
);

let registryCache: DomainRecord[] | undefined;

export function loadDomainRegistry(): DomainRecord[] {
  if (registryCache) return registryCache;

  const rows = tsvParse(readFileSync(registryPath, "utf8"));
  registryCache = rows
    .map((row) => ({
      domain: row.domain?.trim() ?? "",
      tier: row.tier?.trim() ?? "",
      tierName: row.tier_name?.trim() ?? "",
      controlAxis: row.control_axis?.trim() ?? "",
      physicalPath: row.physical_path?.trim() ?? "",
      rationale: row.rationale?.trim() ?? "",
      reviewStatus: row.review_status?.trim() ?? ""
    }))
    .filter((row) => row.domain && row.physicalPath)
    .sort((a, b) => a.tier.localeCompare(b.tier) || a.domain.localeCompare(b.domain));

  return registryCache;
}

export function domainTierSummary() {
  const domains = loadDomainRegistry();
  return TIER_DEFINITIONS.map((tier) => ({
    ...tier,
    domains: domains.filter((domain) => domain.tier === tier.id),
    count: domains.filter((domain) => domain.tier === tier.id).length
  }));
}
