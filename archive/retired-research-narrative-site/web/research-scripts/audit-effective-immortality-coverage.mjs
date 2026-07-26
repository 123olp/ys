import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(webRoot, "..");
const dataPath = path.join(webRoot, "src/data/effective-immortality-evidence.json");
const sourceCardsPath = path.join(
  repoRoot,
  "docs/source-notes/2026-06-28-effective-immortality-flywheel-source-cards.md",
);
const outputDir = path.join(webRoot, "src/data/effective-immortality-flywheel");
const auditJsonPath = path.join(outputDir, "COVERAGE_AUDIT.json");
const auditMdPath = path.join(outputDir, "COVERAGE_AUDIT.md");

const aliasMap = {
  "AI productivity": {
    cards: [
      "Generative AI Writing Productivity",
      "Generative AI at Work QJE Field Evidence",
      "GitHub Copilot Productivity Experiment",
      "Jagged Technological Frontier",
    ],
    refs: ["noy2023productivity", "brynjolfsson2025generative", "peng2023copilot", "dellacqua2026jagged"],
  },
  "AI productivity evidence": {
    cards: [
      "Generative AI Writing Productivity",
      "Generative AI at Work QJE Field Evidence",
      "GitHub Copilot Productivity Experiment",
      "Jagged Technological Frontier",
    ],
    refs: ["noy2023productivity", "brynjolfsson2025generative", "peng2023copilot", "dellacqua2026jagged"],
  },
  "Apple Heart Study": {
    cards: ["Apple Heart Study"],
    refs: ["perez2019appleHeart"],
  },
  "Augmenting Human Intellect": {
    cards: ["Augmenting Human Intellect"],
    refs: ["engelbart1962augmenting"],
  },
  "BCI ethics": {
    cards: ["BCI Ethics and Neurotechnology Governance"],
    refs: ["burwell2017bciEthics"],
  },
  "Capability Approach": {
    cards: ["Capability Approach"],
    refs: ["robeyns2021capability"],
  },
  "Care access": {
    cards: ["WHO Primary Health Care"],
    refs: ["whoSdhPhc"],
  },
  "ClinicalTrials.gov": {
    cards: ["ClinicalTrials.gov Trial Registry"],
    refs: ["clinicaltrialsGov"],
  },
  "ClinicalTrials.gov API": {
    cards: ["ClinicalTrials.gov Trial Registry"],
    refs: ["clinicaltrialsGovApi"],
  },
  "Cognition in the Wild": {
    cards: ["Cognition in the Wild"],
    refs: ["hutchins1995cognition"],
  },
  Cox: {
    cards: ["Cox Proportional Hazards"],
    refs: ["cox1972regression"],
  },
  "Deliberate Practice": {
    cards: ["Deliberate Practice"],
    refs: ["ericsson1993deliberatePractice"],
  },
  "Diffusion of Innovations": {
    cards: ["Diffusion of Innovations"],
    refs: ["rogers2003diffusion"],
  },
  "Digital Twin": {
    cards: ["Dynamic Digital Twin"],
    refs: ["mulder2022dynamicDigitalTwin"],
  },
  "Dynamic Digital Twin": {
    cards: ["Dynamic Digital Twin"],
    refs: ["mulder2022dynamicDigitalTwin"],
  },
  Engelbart: {
    cards: ["Augmenting Human Intellect"],
    refs: ["engelbart1962augmenting"],
  },
  "Evidence policy": {
    cards: ["GRADE Evidence Certainty"],
    refs: ["gradeHandbook"],
  },
  "Extended Mind": {
    cards: ["Extended Mind"],
    refs: ["clark1998extended"],
  },
  "Feedback Intervention Theory": {
    cards: ["Feedback Intervention Theory"],
    refs: ["kluger1996feedback"],
  },
  "Generative AI at Work": {
    cards: ["Generative AI at Work QJE Field Evidence"],
    refs: ["brynjolfsson2025generative"],
  },
  "GitHub Copilot": {
    cards: ["GitHub Copilot Productivity Experiment"],
    refs: ["peng2023copilot"],
  },
  GRADE: {
    cards: ["GRADE Evidence Certainty"],
    refs: ["gradeHandbook"],
  },
  GrimAge: {
    cards: ["DNAm GrimAge"],
    refs: ["lu2019grimage"],
  },
  "Guidelines for Human-AI Interaction": {
    cards: ["Guidelines for Human-AI Interaction"],
    refs: ["amershi2019hai"],
  },
  HALE: {
    cards: ["HALE / QALY Effective-Time Language"],
    refs: ["whohale7752"],
  },
  Hallmarks: {
    cards: ["Hallmarks of Aging"],
    refs: ["lopezotin2013hallmarks"],
  },
  "Health Capital": {
    cards: ["Health Capital"],
    refs: ["grossman1972healthcapital"],
  },
  "Human Capital": {
    cards: ["Human Capital"],
    refs: ["mincer1974humanCapital"],
  },
  "Human-AI Interaction Guidelines": {
    cards: ["Guidelines for Human-AI Interaction"],
    refs: ["amershi2019hai"],
  },
  "Jagged Frontier": {
    cards: ["Jagged Technological Frontier"],
    refs: ["dellacqua2026jagged"],
  },
  "Jagged Technological Frontier": {
    cards: ["Jagged Technological Frontier"],
    refs: ["dellacqua2026jagged"],
  },
  "Kaplan-Meier": {
    cards: ["Kaplan-Meier Survival Curve"],
    refs: ["kaplan1958incomplete"],
  },
  "Law of Practice": {
    cards: ["Law of Practice"],
    refs: ["newell1981lawPractice"],
  },
  "Lived Informatics": {
    cards: ["Lived Informatics"],
    refs: ["epstein2015lived"],
  },
  "Marginal Structural Models": {
    cards: ["Marginal Structural Models"],
    refs: ["robins2000marginalStructural"],
  },
  "NASA-TLX": {
    cards: ["NASA Task Load Index"],
    refs: ["nasaTlx"],
  },
  "NIST AI RMF": {
    cards: ["NIST AI Risk Management Framework"],
    refs: ["nist2023airmf"],
  },
  "Noy & Zhang": {
    cards: ["Generative AI Writing Productivity"],
    refs: ["noy2023productivity"],
  },
  PROBAST: {
    cards: ["TRIPOD and PROBAST"],
    refs: ["probastAi2025", "tripodProbast"],
  },
  "PROBAST+AI": {
    cards: ["TRIPOD and PROBAST"],
    refs: ["probastAi2025"],
  },
  "Prediction Model Governance": {
    cards: ["TRIPOD and PROBAST"],
    refs: ["tripodAi2024", "probastAi2025", "consortAi2020", "spiritAi2020"],
  },
  QALY: {
    cards: ["HALE / QALY Effective-Time Language"],
    refs: ["niceEconomicEvaluation"],
  },
  "Self-Regulated Learning": {
    cards: ["Self-Regulated Learning"],
    refs: ["zimmerman2002selfRegulated"],
  },
  "Social Capital": {
    cards: ["Social Capital"],
    refs: ["coleman1988socialCapital"],
  },
  "Social Relationships": {
    cards: ["Social Relationships and Mortality Risk"],
    refs: ["holtlunstad2010social"],
  },
  "Social relationships mortality": {
    cards: ["Social Relationships and Mortality Risk"],
    refs: ["holtlunstad2010social"],
  },
  "Stage-Based Personal Informatics": {
    cards: ["Stage-Based Model of Personal Informatics"],
    refs: ["li2010personalInformatics"],
  },
  TAM: {
    cards: ["Technology Acceptance"],
    refs: ["davis1989tam"],
  },
  "Target Trial": {
    cards: ["Target Trial Emulation"],
    refs: ["hernan2022targetTrial"],
  },
  "Target Trial Emulation": {
    cards: ["Target Trial Emulation"],
    refs: ["hernan2022targetTrial"],
  },
  "TRIPOD": {
    cards: ["TRIPOD and PROBAST"],
    refs: ["tripodAi2024", "tripodProbast"],
  },
  "TRIPOD+AI": {
    cards: ["TRIPOD and PROBAST"],
    refs: ["tripodAi2024"],
  },
  "Types and Levels of Automation": {
    cards: ["Types and Levels of Automation"],
    refs: ["parasuraman2000automation"],
  },
  UTAUT: {
    cards: ["Unified Theory of Acceptance and Use of Technology"],
    refs: ["venkatesh2003utaut"],
  },
  "WHO HALE": {
    cards: ["HALE / QALY Effective-Time Language"],
    refs: ["whohale7752"],
  },
  "WHO Primary Health Care": {
    cards: ["WHO Primary Health Care"],
    refs: ["whoSdhPhc"],
  },
  "WHO SDOH": {
    cards: ["WHO Social Determinants of Health"],
    refs: ["whoSdhPhc"],
  },
  "WHO ICTRP": {
    cards: ["ClinicalTrials.gov Trial Registry"],
    refs: ["whoIctrp"],
  },
  "CONSORT-AI": {
    cards: ["TRIPOD and PROBAST"],
    refs: ["consortAi2020"],
  },
  "SPIRIT-AI": {
    cards: ["TRIPOD and PROBAST"],
    refs: ["spiritAi2020"],
  },
};

function sha256(content) {
  return `sha256:${createHash("sha256").update(content).digest("hex")}`;
}

function unique(values) {
  return [...new Set(values)].sort((a, b) => a.localeCompare(b));
}

function extractCardTitles(markdown) {
  return [...markdown.matchAll(/^## Card \d+: (.+)$/gm)].map((match) => match[1].trim());
}

function collectAliases(evidence) {
  return unique([
    ...evidence.evidenceEdges.flatMap((edge) => edge.sources || []),
    ...evidence.technologyFamilies.flatMap((family) => family.evidenceSources || []),
  ]);
}

function collectAiTaskReferenceKeys(evidence) {
  return unique((evidence.aiTaskEvidenceRegister || []).map((entry) => entry.referenceKey).filter(Boolean));
}

const requiredAiTaskFields = [
  "id",
  "referenceKey",
  "taskFamily",
  "sampleAndDesign",
  "intervention",
  "comparator",
  "effectEstimate",
  "uncertaintyOrStats",
  "qaOrValidation",
  "downsideChannel",
  "externalBoundary",
  "evidenceLevel",
  "sourceVerification",
  "methodAudit",
];

const requiredAiTaskMethodAuditFields = [
  "primaryTableOrFigure",
  "mainSpecification",
  "statisticalColumns",
  "uncertaintyDetail",
  "qualityScoringProtocol",
  "qaCostQuantification",
  "externalValidityNote",
];

const requiredResearchDeclarations = [
  "Data availability",
  "Code availability",
  "Ethics and safety",
  "AI assistance disclosure",
  "Competing interests",
  "Funding",
  "Author contribution",
  "Use limitation",
];

const requiredResearchDeclarationFields = ["declaration", "statement", "artifact"];

const requiredEstimandFields = [
  "edge",
  "population",
  "interventionOrExposure",
  "comparator",
  "timeZero",
  "outcome",
  "estimand",
  "identificationRisk",
  "currentStatus",
];

const requiredAnalysisPlanFields = [
  "edge",
  "studyQuestion",
  "candidateDesign",
  "minimumData",
  "primaryEstimator",
  "diagnostics",
  "sensitivityChecks",
  "reportingOutput",
  "currentStatus",
];

const requiredFailureModeIds = ["FM1", "FM2", "FM3", "FM4", "FM5", "FM6", "FM7"];

const requiredFailureModeFields = [
  "modeId",
  "failureMode",
  "appliesTo",
  "riskInThisPaper",
  "currentEvidence",
  "control",
  "status",
  "blockCondition",
  "nextAction",
];

const requiredRivalModelFields = [
  "model",
  "coreExplanation",
  "prediction",
  "distinguishingTest",
  "risk",
];

const minimumRivalModelCount = 7;

const requiredModelComparisonProtocolFields = [
  "stage",
  "purpose",
  "implementation",
  "upgradeSignal",
  "failureSignal",
];

const minimumModelComparisonProtocolCount = 7;

const requiredCandidateModelSpecificationFields = [
  "modelId",
  "model",
  "includedVariables",
  "feedbackTerms",
  "primaryOutcome",
  "comparisonRole",
  "minimumData",
  "winningCondition",
  "downgradeCondition",
];

const minimumCandidateModelSpecificationCount = 7;

const requiredModelComparisonReportingFields = [
  "reportItem",
  "purpose",
  "requiredOutput",
  "passCriterion",
  "failurePattern",
];

const minimumModelComparisonReportingCount = 12;

const requiredModelComparisonResultContractFields = [
  "field",
  "meaning",
  "requiredFor",
  "validValuesOrFormat",
  "failureIfMissing",
];

const minimumModelComparisonResultContractCount = 17;

const requiredResearchQuestionBriefFields = [
  "version",
  "mode",
  "topicArea",
  "primaryQuestion",
  "finerAssessment",
  "scope",
  "subQuestions",
  "selectedBecause",
];

const requiredMethodologyBlueprintFields = [
  "version",
  "paradigm",
  "paradigmJustification",
  "methodType",
  "specificMethod",
  "dataStrategy",
  "analyticalFramework",
  "validityCriteria",
  "limitationsByDesign",
  "ethics",
  "reportingStandard",
  "preregistration",
];

const requiredSystematicSearchProtocolFields = [
  "version",
  "protocolType",
  "reviewQuestion",
  "searchDate",
  "databases",
  "dateRange",
  "languages",
  "documentTypes",
  "inclusionCriteria",
  "screeningFlow",
  "qualitySignals",
  "outputs",
];

const requiredDatabaseFields = ["source", "use", "recordedFields"];
const requiredInclusionCriterionFields = ["criterion", "include", "exclude"];
const requiredScreeningFlowFields = ["pass", "decision", "records"];
const requiredSearchSeedFields = ["branch", "query", "purpose", "include", "exclude"];
const requiredScreeningRubricFields = ["decision", "meaning", "requiredAction"];
const requiredLiteratureGapFields = ["edge", "currentCoverage", "gap", "nextSearch"];
const requiredSearchExecutionFields = [
  "id",
  "edge",
  "searchSeedBranch",
  "database",
  "query",
  "retrievalDate",
  "candidateTitle",
  "candidateUrl",
  "evidenceRole",
  "screeningDecision",
  "boundaryUse",
  "candidateStatus",
  "nextAction",
];
const requiredSearchExecutionVerificationFields = [
  "id",
  "searchExecutionId",
  "urlStatus",
  "metadataSource",
  "canonicalTitle",
  "titleMatch",
  "doiOrPersistentId",
  "publicationStatus",
  "evidenceLevel",
  "verificationVerdict",
  "coiOrVenueNote",
  "useDecision",
  "requiredExtraction",
  "blockingIssue",
];
const requiredSearchExecutionExtractionFields = [
  "id",
  "verificationId",
  "searchExecutionId",
  "readScope",
  "extractionStatus",
  "extractedClaim",
  "modelUse",
  "variablesTouched",
  "supports",
  "doesNotSupport",
  "promotionDecision",
  "nextSourceCardAction",
];
const requiredScreeningDecisions = ["SOURCE_CARD", "BACKGROUND_ONLY", "METHOD_GATE", "REJECT"];
const minimumSystematicSearchDatabaseCount = 6;
const minimumSearchSeedCount = 5;
const minimumSearchExecutionCount = 9;
const minimumSearchExecutionVerificationCount = 9;
const minimumSearchExecutionExtractionCount = 9;

function renderMarkdown(audit) {
  const aliasRows = audit.details.alias_coverage
    .map((row) => `| ${row.alias} | ${row.cards.join("<br>")} | ${row.refs.join("<br>")} | ${row.status} |`)
    .join("\n");
  const gapRows = audit.details.gaps.length
    ? audit.details.gaps.map((gap) => `- ${gap}`).join("\n")
    : "- None";

  return `# Effective Immortality Coverage Audit

Date: ${audit.generated_at}
Verdict: \`${audit.verdict}\`
Reason: \`${audit.reason_code}\`

${audit.summary}

## Summary

| Metric | Count |
| --- | ---: |
| Evidence source aliases | ${audit.details.source_alias_count} |
| AI task reference keys | ${audit.details.ai_task_reference_key_count} |
| AI task required fields | ${audit.details.ai_task_required_field_count} |
| AI task method-audit fields | ${audit.details.ai_task_method_audit_field_count} |
| Research declarations | ${audit.details.research_declaration_count} |
| Research declaration required types | ${audit.details.research_declaration_required_type_count} |
| Estimand registry rows | ${audit.details.estimand_registry_count} |
| Estimand required fields | ${audit.details.estimand_required_field_count} |
| Analysis plan registry rows | ${audit.details.analysis_plan_registry_count} |
| Analysis plan required fields | ${audit.details.analysis_plan_required_field_count} |
| AI research failure mode rows | ${audit.details.failure_mode_audit_count} |
| AI research failure mode required types | ${audit.details.failure_mode_required_type_count} |
| Rival model rows | ${audit.details.rival_model_count} |
| Rival model required fields | ${audit.details.rival_model_required_field_count} |
| Model comparison protocol rows | ${audit.details.model_comparison_protocol_count} |
| Model comparison protocol required fields | ${audit.details.model_comparison_protocol_required_field_count} |
| Candidate model specification rows | ${audit.details.candidate_model_specification_count} |
| Candidate model specification required fields | ${audit.details.candidate_model_specification_required_field_count} |
| Model comparison reporting rows | ${audit.details.model_comparison_reporting_count} |
| Model comparison reporting required fields | ${audit.details.model_comparison_reporting_required_field_count} |
| Model comparison result contract rows | ${audit.details.model_comparison_result_contract_count} |
| Model comparison result contract required fields | ${audit.details.model_comparison_result_contract_required_field_count} |
| Research question brief required fields | ${audit.details.research_question_brief_required_field_count} |
| Methodology blueprint required fields | ${audit.details.methodology_blueprint_required_field_count} |
| Search strategy seeds | ${audit.details.search_strategy_seed_count} |
| Search strategy seed required fields | ${audit.details.search_strategy_seed_required_field_count} |
| Systematic search protocol databases | ${audit.details.systematic_search_database_count} |
| Systematic search protocol required fields | ${audit.details.systematic_search_protocol_required_field_count} |
| Literature screening rubric rows | ${audit.details.literature_screening_rubric_count} |
| Literature gap map rows | ${audit.details.literature_gap_map_count} |
| Search execution register rows | ${audit.details.search_execution_register_count} |
| Search execution required fields | ${audit.details.search_execution_required_field_count} |
| Search execution verification rows | ${audit.details.search_execution_verification_count} |
| Search execution verification required fields | ${audit.details.search_execution_verification_required_field_count} |
| Search execution extraction rows | ${audit.details.search_execution_extraction_count} |
| Search execution extraction required fields | ${audit.details.search_execution_extraction_required_field_count} |
| Source Card titles | ${audit.details.source_card_count} |
| Reference Registry entries | ${audit.details.reference_registry_count} |
| Coverage gaps | ${audit.details.gaps.length} |

## Alias Coverage

| Alias | Source Cards | Reference Registry keys | Status |
| --- | --- | --- | --- |
${aliasRows}

## Gaps

${gapRows}

## Scope

This audit checks structural coverage only: every evidence source alias used by \`evidenceEdges\` and \`technologyFamilies\` must resolve to at least one Source Card and at least one Reference Registry entry, every \`aiTaskEvidenceRegister[*].referenceKey\` must exist in the Reference Registry, every AI task evidence row must include the required full-text and method-audit fields, every required research declaration must be present, every evidence edge must have both an \`estimandRegistry\` row and an \`analysisPlanRegistry\` row with required protocol fields, all seven AI research failure modes must have audit rows, the rival-model comparison must preserve the minimum model set and required fields, the model-comparison protocol must preserve the minimum stage set and required fields, the candidate model specification registry must preserve the minimum model set and required fields, the model-comparison reporting matrix must preserve the minimum reporting set and required fields, and the ARS Phase 1/2 research design must preserve a complete research question brief, methodology blueprint, search strategy seeds, systematic search protocol, screening rubric, literature gap map, search execution register, candidate source verification register, and candidate source extraction register. It does not verify full-text citation context, external metadata freshness, or empirical validity.
`;
}

const evidenceContent = fs.readFileSync(dataPath, "utf8");
const sourceCardsContent = fs.readFileSync(sourceCardsPath, "utf8");
const evidence = JSON.parse(evidenceContent);
const sourceCardTitles = extractCardTitles(sourceCardsContent);
const sourceCardTitleSet = new Set(sourceCardTitles);
const referenceKeySet = new Set(evidence.referenceRegistry.map((entry) => entry.key));
const aliases = collectAliases(evidence);
const aiTaskReferenceKeys = collectAiTaskReferenceKeys(evidence);
const knownContextIds = new Set(evidence.citationContextRegister.map((context) => context.id));
const knownEdges = new Set(evidence.evidenceEdges.map((edge) => edge.edge));
const knownClaims = new Set(evidence.claimRegister.map((claim) => claim.id));
const gaps = [];

const researchQuestionBrief = evidence.researchQuestionBrief || {};
for (const field of requiredResearchQuestionBriefFields) {
  if (!researchQuestionBrief[field]) {
    gaps.push(`Research question brief missing field: ${field}`);
  }
}
if ((researchQuestionBrief.finerAssessment || []).length < 5) {
  gaps.push(`Research question brief FINER assessment below minimum count: ${(researchQuestionBrief.finerAssessment || []).length}/5`);
}
for (const field of ["inScope", "outOfScope", "assumptions"]) {
  if (!Array.isArray(researchQuestionBrief.scope?.[field]) || !researchQuestionBrief.scope[field].length) {
    gaps.push(`Research question brief scope missing non-empty list: ${field}`);
  }
}

const methodologyBlueprint = evidence.methodologyBlueprint || {};
for (const field of requiredMethodologyBlueprintFields) {
  if (!methodologyBlueprint[field]) {
    gaps.push(`Methodology blueprint missing field: ${field}`);
  }
}
for (const field of ["dataType", "sources", "sampling", "timeFrame"]) {
  if (!methodologyBlueprint.dataStrategy?.[field]) {
    gaps.push(`Methodology blueprint dataStrategy missing field: ${field}`);
  }
}
if ((methodologyBlueprint.validityCriteria || []).length < 5) {
  gaps.push(`Methodology blueprint validityCriteria below minimum count: ${(methodologyBlueprint.validityCriteria || []).length}/5`);
}

const searchStrategySeeds = evidence.searchStrategySeeds || [];
if (searchStrategySeeds.length < minimumSearchSeedCount) {
  gaps.push(`Search strategy seeds below minimum count: ${searchStrategySeeds.length}/${minimumSearchSeedCount}`);
}
for (const entry of searchStrategySeeds) {
  for (const field of requiredSearchSeedFields) {
    if (!entry[field]) gaps.push(`Search strategy seed ${entry.branch || "UNKNOWN"} missing field: ${field}`);
  }
}

const systematicSearchProtocol = evidence.systematicSearchProtocol || {};
for (const field of requiredSystematicSearchProtocolFields) {
  if (!systematicSearchProtocol[field]) {
    gaps.push(`Systematic search protocol missing field: ${field}`);
  }
}
const systematicSearchDatabases = systematicSearchProtocol.databases || [];
if (systematicSearchDatabases.length < minimumSystematicSearchDatabaseCount) {
  gaps.push(
    `Systematic search protocol databases below minimum count: ${systematicSearchDatabases.length}/${minimumSystematicSearchDatabaseCount}`,
  );
}
for (const entry of systematicSearchDatabases) {
  for (const field of requiredDatabaseFields) {
    if (!entry[field] || (Array.isArray(entry[field]) && !entry[field].length)) {
      gaps.push(`Systematic search database ${entry.source || "UNKNOWN"} missing field: ${field}`);
    }
  }
}
for (const entry of systematicSearchProtocol.inclusionCriteria || []) {
  for (const field of requiredInclusionCriterionFields) {
    if (!entry[field]) gaps.push(`Systematic search inclusion criterion ${entry.criterion || "UNKNOWN"} missing field: ${field}`);
  }
}
for (const entry of systematicSearchProtocol.screeningFlow || []) {
  for (const field of requiredScreeningFlowFields) {
    if (!entry[field]) gaps.push(`Systematic search screening flow ${entry.pass || "UNKNOWN"} missing field: ${field}`);
  }
}

const literatureScreeningRubric = evidence.literatureScreeningRubric || [];
const screeningDecisionSet = new Set(literatureScreeningRubric.map((entry) => entry.decision));
for (const decision of requiredScreeningDecisions) {
  if (!screeningDecisionSet.has(decision)) gaps.push(`Literature screening rubric missing decision: ${decision}`);
}
for (const entry of literatureScreeningRubric) {
  for (const field of requiredScreeningRubricFields) {
    if (!entry[field]) gaps.push(`Literature screening rubric ${entry.decision || "UNKNOWN"} missing field: ${field}`);
  }
}

const aliasCoverage = aliases.map((alias) => {
  const mapping = aliasMap[alias];
  if (!mapping) {
    gaps.push(`Missing alias mapping: ${alias}`);
    return { alias, cards: [], refs: [], status: "MISSING_ALIAS_MAPPING" };
  }

  for (const card of mapping.cards) {
    if (!sourceCardTitleSet.has(card)) gaps.push(`Alias ${alias} points to missing Source Card: ${card}`);
  }
  for (const ref of mapping.refs) {
    if (!referenceKeySet.has(ref)) gaps.push(`Alias ${alias} points to missing Reference Registry key: ${ref}`);
  }

  const status = mapping.cards.every((card) => sourceCardTitleSet.has(card))
    && mapping.refs.every((ref) => referenceKeySet.has(ref))
    ? "PASS"
    : "BROKEN_LINK";
  return { alias, cards: mapping.cards, refs: mapping.refs, status };
});

for (const entry of evidence.referenceRegistry) {
  for (const contextId of entry.citationContexts || []) {
    if (!knownContextIds.has(contextId)) {
      gaps.push(`Reference ${entry.key} points to unknown citation context: ${contextId}`);
    }
  }
}

for (const claim of evidence.claimEvidenceMap) {
  if (!knownClaims.has(claim.claimId)) gaps.push(`Claim evidence map points to unknown claim: ${claim.claimId}`);
  for (const contextId of claim.citationContexts || []) {
    if (!knownContextIds.has(contextId)) {
      gaps.push(`Claim ${claim.claimId} points to unknown citation context: ${contextId}`);
    }
  }
  for (const edge of claim.evidenceEdges || []) {
    if (!knownEdges.has(edge)) gaps.push(`Claim ${claim.claimId} points to unknown evidence edge: ${edge}`);
  }
}

for (const key of aiTaskReferenceKeys) {
  if (!referenceKeySet.has(key)) {
    gaps.push(`AI task evidence points to missing Reference Registry key: ${key}`);
  }
}

for (const entry of evidence.aiTaskEvidenceRegister || []) {
  for (const field of requiredAiTaskFields) {
    if (!entry[field]) gaps.push(`AI task evidence ${entry.id || entry.referenceKey || "UNKNOWN"} is missing field: ${field}`);
  }
  for (const field of ["venue", "method", "coiFlag", "verificationStatus"]) {
    if (!entry.sourceVerification?.[field]) {
      gaps.push(`AI task evidence ${entry.id || entry.referenceKey || "UNKNOWN"} sourceVerification missing field: ${field}`);
    }
  }
  for (const field of requiredAiTaskMethodAuditFields) {
    if (!entry.methodAudit?.[field]) {
      gaps.push(`AI task evidence ${entry.id || entry.referenceKey || "UNKNOWN"} methodAudit missing field: ${field}`);
    }
  }
}

const researchDeclarations = evidence.researchDeclarations || [];
const researchDeclarationNames = new Set(researchDeclarations.map((entry) => entry.declaration));
for (const declaration of requiredResearchDeclarations) {
  if (!researchDeclarationNames.has(declaration)) {
    gaps.push(`Missing research declaration: ${declaration}`);
  }
}

for (const entry of researchDeclarations) {
  for (const field of requiredResearchDeclarationFields) {
    if (!entry[field]) {
      gaps.push(`Research declaration ${entry.declaration || "UNKNOWN"} missing field: ${field}`);
    }
  }
}

const estimandRegistry = evidence.estimandRegistry || [];
const estimandEdges = new Set(estimandRegistry.map((entry) => entry.edge));
for (const edge of knownEdges) {
  if (!estimandEdges.has(edge)) {
    gaps.push(`Missing estimand registry row for edge: ${edge}`);
  }
}

for (const entry of estimandRegistry) {
  if (!knownEdges.has(entry.edge)) {
    gaps.push(`Estimand registry row points to unknown edge: ${entry.edge || "UNKNOWN"}`);
  }
  for (const field of requiredEstimandFields) {
    if (!entry[field]) {
      gaps.push(`Estimand registry ${entry.edge || "UNKNOWN"} missing field: ${field}`);
    }
  }
}

const analysisPlanRegistry = evidence.analysisPlanRegistry || [];
const analysisPlanEdges = new Set(analysisPlanRegistry.map((entry) => entry.edge));
for (const edge of knownEdges) {
  if (!analysisPlanEdges.has(edge)) {
    gaps.push(`Missing analysis plan registry row for edge: ${edge}`);
  }
}

for (const entry of analysisPlanRegistry) {
  if (!knownEdges.has(entry.edge)) {
    gaps.push(`Analysis plan registry row points to unknown edge: ${entry.edge || "UNKNOWN"}`);
  }
  for (const field of requiredAnalysisPlanFields) {
    if (!entry[field]) {
      gaps.push(`Analysis plan registry ${entry.edge || "UNKNOWN"} missing field: ${field}`);
    }
  }
}

const failureModeAudit = evidence.aiResearchFailureModeAudit || [];
const failureModeIds = new Set(failureModeAudit.map((entry) => entry.modeId));
for (const modeId of requiredFailureModeIds) {
  if (!failureModeIds.has(modeId)) {
    gaps.push(`Missing AI research failure mode audit row: ${modeId}`);
  }
}

for (const entry of failureModeAudit) {
  if (!requiredFailureModeIds.includes(entry.modeId)) {
    gaps.push(`AI research failure mode audit row has unknown modeId: ${entry.modeId || "UNKNOWN"}`);
  }
  for (const field of requiredFailureModeFields) {
    if (!entry[field]) {
      gaps.push(`AI research failure mode ${entry.modeId || "UNKNOWN"} missing field: ${field}`);
    }
  }
}

const rivalModels = evidence.rivalModels || [];
if (rivalModels.length < minimumRivalModelCount) {
  gaps.push(`Rival models below minimum count: ${rivalModels.length}/${minimumRivalModelCount}`);
}

for (const entry of rivalModels) {
  for (const field of requiredRivalModelFields) {
    if (!entry[field]) {
      gaps.push(`Rival model ${entry.model || "UNKNOWN"} missing field: ${field}`);
    }
  }
}

const modelComparisonProtocol = evidence.modelComparisonProtocol || [];
if (modelComparisonProtocol.length < minimumModelComparisonProtocolCount) {
  gaps.push(
    `Model comparison protocol below minimum count: ${modelComparisonProtocol.length}/${minimumModelComparisonProtocolCount}`,
  );
}

for (const entry of modelComparisonProtocol) {
  for (const field of requiredModelComparisonProtocolFields) {
    if (!entry[field]) {
      gaps.push(`Model comparison protocol ${entry.stage || "UNKNOWN"} missing field: ${field}`);
    }
  }
}

const candidateModelSpecifications = evidence.candidateModelSpecifications || [];
if (candidateModelSpecifications.length < minimumCandidateModelSpecificationCount) {
  gaps.push(
    `Candidate model specifications below minimum count: ${candidateModelSpecifications.length}/${minimumCandidateModelSpecificationCount}`,
  );
}

for (const entry of candidateModelSpecifications) {
  for (const field of requiredCandidateModelSpecificationFields) {
    if (!entry[field]) {
      gaps.push(`Candidate model specification ${entry.modelId || "UNKNOWN"} missing field: ${field}`);
    }
  }
}

const modelComparisonReportingMatrix = evidence.modelComparisonReportingMatrix || [];
if (modelComparisonReportingMatrix.length < minimumModelComparisonReportingCount) {
  gaps.push(
    `Model comparison reporting matrix below minimum count: ${modelComparisonReportingMatrix.length}/${minimumModelComparisonReportingCount}`,
  );
}

for (const entry of modelComparisonReportingMatrix) {
  for (const field of requiredModelComparisonReportingFields) {
    if (!entry[field]) {
      gaps.push(`Model comparison reporting item ${entry.reportItem || "UNKNOWN"} missing field: ${field}`);
    }
  }
}

const modelComparisonResultContract = evidence.modelComparisonResultContract || [];
if (modelComparisonResultContract.length < minimumModelComparisonResultContractCount) {
  gaps.push(
    `Model comparison result contract below minimum count: ${modelComparisonResultContract.length}/${minimumModelComparisonResultContractCount}`,
  );
}

const literatureGapMap = evidence.literatureGapMap || [];
const literatureGapEdges = new Set(literatureGapMap.map((entry) => entry.edge));
for (const edge of knownEdges) {
  if (!literatureGapEdges.has(edge)) {
    gaps.push(`Literature gap map missing row for edge: ${edge}`);
  }
}
for (const entry of literatureGapMap) {
  if (!knownEdges.has(entry.edge)) {
    gaps.push(`Literature gap map row points to unknown edge: ${entry.edge || "UNKNOWN"}`);
  }
  for (const field of requiredLiteratureGapFields) {
    if (!entry[field]) gaps.push(`Literature gap map ${entry.edge || "UNKNOWN"} missing field: ${field}`);
  }
}

const searchExecutionRegister = evidence.searchExecutionRegister || [];
if (searchExecutionRegister.length < minimumSearchExecutionCount) {
  gaps.push(`Search execution register below minimum count: ${searchExecutionRegister.length}/${minimumSearchExecutionCount}`);
}
const searchExecutionEdges = new Set(searchExecutionRegister.map((entry) => entry.edge));
for (const edge of knownEdges) {
  if (!searchExecutionEdges.has(edge)) {
    gaps.push(`Search execution register missing row for edge: ${edge}`);
  }
}
const searchExecutionIds = new Set();
for (const entry of searchExecutionRegister) {
  if (searchExecutionIds.has(entry.id)) gaps.push(`Duplicate search execution id: ${entry.id}`);
  searchExecutionIds.add(entry.id);
  if (!knownEdges.has(entry.edge)) {
    gaps.push(`Search execution row points to unknown edge: ${entry.edge || "UNKNOWN"}`);
  }
  for (const field of requiredSearchExecutionFields) {
    if (!entry[field]) gaps.push(`Search execution ${entry.id || "UNKNOWN"} missing field: ${field}`);
  }
  if (entry.screeningDecision && !requiredScreeningDecisions.includes(entry.screeningDecision)) {
    gaps.push(`Search execution ${entry.id || "UNKNOWN"} has invalid screeningDecision: ${entry.screeningDecision}`);
  }
}

const searchExecutionVerificationRegister = evidence.searchExecutionVerificationRegister || [];
if (searchExecutionVerificationRegister.length < minimumSearchExecutionVerificationCount) {
  gaps.push(
    `Search execution verification register below minimum count: ${searchExecutionVerificationRegister.length}/${minimumSearchExecutionVerificationCount}`,
  );
}
const knownSearchExecutionIds = new Set(searchExecutionRegister.map((entry) => entry.id));
const verifiedSearchExecutionIds = new Set(searchExecutionVerificationRegister.map((entry) => entry.searchExecutionId));
for (const searchExecutionId of knownSearchExecutionIds) {
  if (!verifiedSearchExecutionIds.has(searchExecutionId)) {
    gaps.push(`Search execution verification register missing row for: ${searchExecutionId}`);
  }
}
const searchExecutionVerificationIds = new Set();
for (const entry of searchExecutionVerificationRegister) {
  if (searchExecutionVerificationIds.has(entry.id)) gaps.push(`Duplicate search execution verification id: ${entry.id}`);
  searchExecutionVerificationIds.add(entry.id);
  if (!knownSearchExecutionIds.has(entry.searchExecutionId)) {
    gaps.push(`Search execution verification row points to unknown searchExecutionId: ${entry.searchExecutionId || "UNKNOWN"}`);
  }
  for (const field of requiredSearchExecutionVerificationFields) {
    if (!entry[field]) gaps.push(`Search execution verification ${entry.id || "UNKNOWN"} missing field: ${field}`);
  }
}

const searchExecutionExtractionRegister = evidence.searchExecutionExtractionRegister || [];
if (searchExecutionExtractionRegister.length < minimumSearchExecutionExtractionCount) {
  gaps.push(
    `Search execution extraction register below minimum count: ${searchExecutionExtractionRegister.length}/${minimumSearchExecutionExtractionCount}`,
  );
}
const knownSearchVerificationIds = new Set(searchExecutionVerificationRegister.map((entry) => entry.id));
const extractedSearchExecutionIds = new Set(searchExecutionExtractionRegister.map((entry) => entry.searchExecutionId));
const extractedSearchVerificationIds = new Set(searchExecutionExtractionRegister.map((entry) => entry.verificationId));
for (const searchExecutionId of knownSearchExecutionIds) {
  if (!extractedSearchExecutionIds.has(searchExecutionId)) {
    gaps.push(`Search execution extraction register missing row for searchExecutionId: ${searchExecutionId}`);
  }
}
for (const verificationId of knownSearchVerificationIds) {
  if (!extractedSearchVerificationIds.has(verificationId)) {
    gaps.push(`Search execution extraction register missing row for verificationId: ${verificationId}`);
  }
}
const searchExecutionExtractionIds = new Set();
for (const entry of searchExecutionExtractionRegister) {
  if (searchExecutionExtractionIds.has(entry.id)) gaps.push(`Duplicate search execution extraction id: ${entry.id}`);
  searchExecutionExtractionIds.add(entry.id);
  if (!knownSearchExecutionIds.has(entry.searchExecutionId)) {
    gaps.push(`Search execution extraction row points to unknown searchExecutionId: ${entry.searchExecutionId || "UNKNOWN"}`);
  }
  if (!knownSearchVerificationIds.has(entry.verificationId)) {
    gaps.push(`Search execution extraction row points to unknown verificationId: ${entry.verificationId || "UNKNOWN"}`);
  }
  for (const field of requiredSearchExecutionExtractionFields) {
    if (!entry[field] || (Array.isArray(entry[field]) && !entry[field].length)) {
      gaps.push(`Search execution extraction ${entry.id || "UNKNOWN"} missing field: ${field}`);
    }
  }
}

for (const entry of modelComparisonResultContract) {
  for (const field of requiredModelComparisonResultContractFields) {
    if (!entry[field]) {
      gaps.push(`Model comparison result contract field ${entry.field || "UNKNOWN"} missing field: ${field}`);
    }
  }
}

const duplicateCards = sourceCardTitles.filter((title, index) => sourceCardTitles.indexOf(title) !== index);
for (const title of unique(duplicateCards)) gaps.push(`Duplicate Source Card title: ${title}`);

const audit = {
  audit_skill: "effective-immortality-coverage-audit",
  verdict: gaps.length ? "FAIL" : "PASS",
  reason_code: gaps.length ? "coverage_gaps_found" : "all_aliases_resolve",
  summary: gaps.length
    ? "Some evidence source aliases, AI task evidence fields, research declarations, estimand protocol rows, analysis plan rows, AI research failure mode rows, rival model rows, model comparison protocol rows, candidate model specification rows, model comparison reporting rows, model comparison result contract rows, ARS Phase 1/2 research-design fields, search execution records, candidate source verification records, candidate source extraction records, citation contexts, claims, or card titles do not resolve cleanly."
    : "All evidence source aliases resolve to Source Cards and Reference Registry entries; AI task evidence rows include required full-text verification and method-audit fields; research declarations, estimand protocol rows, analysis plan rows, AI research failure mode rows, rival model rows, model comparison protocol rows, candidate model specification rows, model comparison reporting rows, model comparison result contract rows, ARS Phase 1/2 research-design fields, search execution records, candidate source verification records, and candidate source extraction records are present; claim/context/edge references are internally consistent.",
  generated_at: `${evidence.updated}T00:00:00.000Z`,
  audited_input_hashes: {
    "src/data/effective-immortality-evidence.json": sha256(evidenceContent),
    "../docs/source-notes/2026-06-28-effective-immortality-flywheel-source-cards.md": sha256(sourceCardsContent),
  },
  details: {
    schema_version: evidence.schemaVersion,
    source_alias_count: aliases.length,
    ai_task_reference_key_count: aiTaskReferenceKeys.length,
    ai_task_required_field_count: requiredAiTaskFields.length,
    ai_task_method_audit_field_count: requiredAiTaskMethodAuditFields.length,
    research_declaration_count: researchDeclarations.length,
    research_declaration_required_type_count: requiredResearchDeclarations.length,
    estimand_registry_count: estimandRegistry.length,
    estimand_required_field_count: requiredEstimandFields.length,
    analysis_plan_registry_count: analysisPlanRegistry.length,
    analysis_plan_required_field_count: requiredAnalysisPlanFields.length,
    failure_mode_audit_count: failureModeAudit.length,
    failure_mode_required_type_count: requiredFailureModeIds.length,
    rival_model_count: rivalModels.length,
    rival_model_required_field_count: requiredRivalModelFields.length,
    model_comparison_protocol_count: modelComparisonProtocol.length,
    model_comparison_protocol_required_field_count: requiredModelComparisonProtocolFields.length,
    candidate_model_specification_count: candidateModelSpecifications.length,
    candidate_model_specification_required_field_count: requiredCandidateModelSpecificationFields.length,
    model_comparison_reporting_count: modelComparisonReportingMatrix.length,
    model_comparison_reporting_required_field_count: requiredModelComparisonReportingFields.length,
    model_comparison_result_contract_count: modelComparisonResultContract.length,
    model_comparison_result_contract_required_field_count: requiredModelComparisonResultContractFields.length,
    research_question_brief_required_field_count: requiredResearchQuestionBriefFields.length,
    methodology_blueprint_required_field_count: requiredMethodologyBlueprintFields.length,
    search_strategy_seed_count: searchStrategySeeds.length,
    search_strategy_seed_required_field_count: requiredSearchSeedFields.length,
    systematic_search_database_count: systematicSearchDatabases.length,
    systematic_search_protocol_required_field_count: requiredSystematicSearchProtocolFields.length,
    literature_screening_rubric_count: literatureScreeningRubric.length,
    literature_gap_map_count: literatureGapMap.length,
    search_execution_register_count: searchExecutionRegister.length,
    search_execution_required_field_count: requiredSearchExecutionFields.length,
    search_execution_verification_count: searchExecutionVerificationRegister.length,
    search_execution_verification_required_field_count: requiredSearchExecutionVerificationFields.length,
    search_execution_extraction_count: searchExecutionExtractionRegister.length,
    search_execution_extraction_required_field_count: requiredSearchExecutionExtractionFields.length,
    source_card_count: sourceCardTitles.length,
    reference_registry_count: evidence.referenceRegistry.length,
    alias_coverage: aliasCoverage,
    gaps,
  },
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(auditJsonPath, `${JSON.stringify(audit, null, 2)}\n`);
fs.writeFileSync(auditMdPath, renderMarkdown(audit));

console.log(`coverage verdict ${audit.verdict}`);
console.log(`source aliases ${aliases.length}`);
console.log(`ai task reference keys ${aiTaskReferenceKeys.length}`);
console.log(`rival models ${rivalModels.length}`);
console.log(`model comparison protocol rows ${modelComparisonProtocol.length}`);
console.log(`candidate model specifications ${candidateModelSpecifications.length}`);
console.log(`model comparison reporting rows ${modelComparisonReportingMatrix.length}`);
console.log(`model comparison result contract rows ${modelComparisonResultContract.length}`);
console.log(`search execution register rows ${searchExecutionRegister.length}`);
console.log(`search execution verification rows ${searchExecutionVerificationRegister.length}`);
console.log(`search execution extraction rows ${searchExecutionExtractionRegister.length}`);
console.log(`source cards ${sourceCardTitles.length}`);
console.log(`reference registry ${evidence.referenceRegistry.length}`);
console.log(`wrote ${path.relative(webRoot, auditJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, auditMdPath)}`);

if (gaps.length) {
  for (const gap of gaps) console.error(`coverage gap: ${gap}`);
  process.exitCode = 1;
}
