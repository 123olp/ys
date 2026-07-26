import {readFileSync} from "node:fs";
import {resolve} from "node:path";

type SourceAnchor = {
  sourceId: string;
  sourceType: string;
  title: string;
  url: string;
  evidenceRole: string;
  supports: string[];
  transferBoundary: string;
  localUse: string;
};

type DomainClaimRow = {
  domainClaimId: string;
  domainId: string;
  sourceCardIds: string[];
};

type DomainEntry = {
  domainId: string;
  tier: string;
  path: string;
  requiredClaims: string[];
  strongClaim: string;
  modelPosition: string;
  variables: {
    inputs: string[];
    mediators: string[];
    outputs: string[];
  };
  falsifiers: Array<{
    condition: string;
    downgradeAction: string;
    evidenceNeeded: string;
  }>;
  prohibitedUses: string[];
  nextEvidenceAction: string;
};

type FieldRow = {
  fieldCardId: string;
  domainClaimId: string;
  domainId: string;
  sourceCardIds: string[];
  endpointCandidates: string[];
  nextFieldExtractionAction: string;
};

type ClaimMatrix = {
  schemaVersion: string;
  matrixId: string;
  status: string;
  rowDefaults: {
    evidenceBoundary: string;
    modelUseAllowed: string[];
    modelUseBlocked: string[];
  };
  domainClaimRows: DomainClaimRow[];
};

type FalsifierRegister = {
  schemaVersion: string;
  registerId: string;
  status: string;
  entries: DomainEntry[];
};

type FieldRegister = {
  schemaVersion: string;
  registerId: string;
  status: string;
  rowDefaults: {
    populationBoundary: string;
    uncertaintyChannels: string[];
    transferBoundary: string;
    fieldExtractionStatus: string;
    blockedUses: string[];
  };
  fieldRows: FieldRow[];
};

type SourceRegister = {
  schemaVersion: string;
  registerId: string;
  status: string;
  sourceAnchors: SourceAnchor[];
  nonClaims: string[];
};

const referenceRoot = resolve(process.cwd(), "../docs/reference");

function readRegistry<T>(filename: string): T {
  return JSON.parse(readFileSync(resolve(referenceRoot, filename), "utf8")) as T;
}

let evidenceCache: ReturnType<typeof buildEvidenceRegistry> | undefined;

function requireUnique(values: string[], label: string) {
  if (new Set(values).size !== values.length) {
    throw new Error(`${label} contains duplicate identifiers`);
  }
}

function buildEvidenceRegistry() {
  const claimMatrix = readRegistry<ClaimMatrix>("human-infra-domain-claim-evidence-matrix.json");
  const falsifierRegister = readRegistry<FalsifierRegister>("human-infra-domain-falsifier-coverage.json");
  const fieldRegister = readRegistry<FieldRegister>("human-infra-domain-source-card-field-extraction.json");
  const sourceRegister = readRegistry<SourceRegister>("human-infra-falsifier-source-card-backfill.json");

  requireUnique(claimMatrix.domainClaimRows.map((row) => row.domainClaimId), "domain claim matrix");
  requireUnique(falsifierRegister.entries.map((entry) => entry.domainId), "domain falsifier register");
  requireUnique(fieldRegister.fieldRows.map((row) => row.domainClaimId), "domain field register");
  requireUnique(sourceRegister.sourceAnchors.map((source) => source.sourceId), "source anchor register");

  const domainById = new Map(falsifierRegister.entries.map((entry) => [entry.domainId, entry]));
  const fieldByClaimId = new Map(fieldRegister.fieldRows.map((row) => [row.domainClaimId, row]));
  const sourceById = new Map(sourceRegister.sourceAnchors.map((source) => [source.sourceId, source]));

  const claims = claimMatrix.domainClaimRows.map((row) => {
    const domain = domainById.get(row.domainId);
    const field = fieldByClaimId.get(row.domainClaimId);
    if (!domain || !field) {
      throw new Error(`evidence registry cannot join ${row.domainClaimId} (${row.domainId})`);
    }

    const missingSources = row.sourceCardIds.filter((sourceId) => !sourceById.has(sourceId));
    if (missingSources.length > 0) {
      throw new Error(`${row.domainClaimId} references missing sources: ${missingSources.join(", ")}`);
    }
    if (field.domainId !== row.domainId) {
      throw new Error(`${row.domainClaimId} field card points to ${field.domainId}`);
    }

    return {
      id: row.domainClaimId,
      type: "BoundedDomainClaim",
      domain_id: row.domainId,
      tier: domain.tier,
      repository_path: domain.path,
      claim: domain.strongClaim,
      model_position: domain.modelPosition,
      required_core_claims: domain.requiredClaims,
      source_ids: row.sourceCardIds,
      variables: domain.variables,
      endpoint_candidates: field.endpointCandidates,
      falsifiers: domain.falsifiers.map((falsifier, index) => ({
        id: `${row.domainClaimId}-F${index + 1}`,
        ...falsifier
      })),
      prohibited_uses: domain.prohibitedUses,
      evidence_boundary: claimMatrix.rowDefaults.evidenceBoundary,
      population_boundary: fieldRegister.rowDefaults.populationBoundary,
      transfer_boundary: fieldRegister.rowDefaults.transferBoundary,
      uncertainty_channels: fieldRegister.rowDefaults.uncertaintyChannels,
      model_use_allowed: claimMatrix.rowDefaults.modelUseAllowed,
      model_use_blocked: claimMatrix.rowDefaults.modelUseBlocked,
      review_status: fieldRegister.rowDefaults.fieldExtractionStatus,
      next_evidence_action: field.nextFieldExtractionAction || domain.nextEvidenceAction
    };
  });

  const sources = sourceRegister.sourceAnchors.map((source) => ({
    id: source.sourceId,
    type: "SourceAnchor",
    source_type: source.sourceType,
    title: source.title,
    url: source.url,
    evidence_role: source.evidenceRole,
    supports: source.supports,
    transfer_boundary: source.transferBoundary,
    local_use: source.localUse,
    review_status: "source-anchor-backfill-not-independent-fresh-review"
  }));

  return {
    schema_version: "human-infra-bounded-evidence-registry.v1",
    source_registry_ids: {
      claim_matrix: claimMatrix.matrixId,
      falsifier_register: falsifierRegister.registerId,
      field_register: fieldRegister.registerId,
      source_register: sourceRegister.registerId
    },
    source_registry_status: {
      claim_matrix: claimMatrix.status,
      falsifier_register: falsifierRegister.status,
      field_register: fieldRegister.status,
      source_register: sourceRegister.status
    },
    summary: {
      claim_count: claims.length,
      source_count: sources.length,
      c1_claim_count: claims.filter((claim) => claim.tier === "C1").length,
      falsifier_count: claims.reduce((total, claim) => total + claim.falsifiers.length, 0),
      endpoint_candidate_count: claims.reduce(
        (total, claim) => total + claim.endpoint_candidates.length,
        0
      )
    },
    limitations: [
      "This is a bounded projection of repository research registers, not independent validation of external sources.",
      "Source anchors identify evidence roles and transfer boundaries; they do not prove intervention efficacy.",
      "Population, effect-size, uncertainty, time-horizon and applicability extraction remain incomplete.",
      "No claim in this projection is admitted to calibrated prediction, intervention ranking or individual recommendation."
    ],
    non_claims: sourceRegister.nonClaims,
    sources,
    claims
  };
}

export function loadEvidenceRegistry() {
  evidenceCache ??= buildEvidenceRegistry();
  return evidenceCache;
}

