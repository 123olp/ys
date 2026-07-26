import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");

const dataPath = path.join(webRoot, "src/data/metric-redshift-recursive-waiting.json");
const pagePath = path.join(webRoot, "src/pages/papers/metric-redshift-recursive-waiting.astro");
const outputDir = path.join(webRoot, "src/data/metric-redshift-recursive-waiting");
const toolSeedPath = path.join(outputDir, "TOOL_GENERATED_PAGE_SEED.astro");
const citationContextPacketPath = path.join(outputDir, "CITATION_CONTEXT_REVIEW_PACKET.json");
const citationContextLocalReviewPath = path.join(outputDir, "CITATION_CONTEXT_LOCAL_REVIEW.json");
const scenarioEvaluationAuditPath = path.join(outputDir, "SCENARIO_EVALUATION_AUDIT.json");
const auditJsonPath = path.join(outputDir, "COVERAGE_AUDIT.json");
const auditMdPath = path.join(outputDir, "COVERAGE_AUDIT.md");

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function unique(values) {
  return [...new Set(values)];
}

function missingFields(row, fields) {
  return fields.filter((field) => row[field] === undefined || row[field] === null || row[field] === "");
}

function pushFinding(findings, severity, code, message) {
  findings.push({ severity, code, message });
}

const data = readJson(dataPath);
const page = fs.readFileSync(pagePath, "utf8");
const toolSeed = fs.existsSync(toolSeedPath) ? fs.readFileSync(toolSeedPath, "utf8") : "";
const citationContextPacket = fs.existsSync(citationContextPacketPath)
  ? readJson(citationContextPacketPath)
  : null;
const citationContextLocalReview = fs.existsSync(citationContextLocalReviewPath)
  ? readJson(citationContextLocalReviewPath)
  : null;
const scenarioEvaluationAudit = fs.existsSync(scenarioEvaluationAuditPath)
  ? readJson(scenarioEvaluationAuditPath)
  : null;
const findings = [];

const minimumCounts = data.auditContract?.minimumCounts || {};
const requiredPageStrings = data.auditContract?.requiredPageStrings || [];

const collections = {
  claims: data.claimRegister || [],
  sources: data.sourceCards || [],
  variables: data.variableDictionary || [],
  claimEvidenceMap: data.claimEvidenceMap || [],
  stateMachineStates: data.stateMachine || [],
  researchProtocolCards: data.researchProtocolCards || [],
  figurePlan: data.figurePlan || [],
  citationContextRegister: data.citationContextRegister || [],
  modelAssumptions: data.modelAssumptions || [],
  propositionRegister: data.propositionRegister || [],
  claimMaturityRegister: data.claimMaturityRegister || [],
  falsifierRegister: data.falsifierRegister || [],
  sourceCardLedger: data.sourceCardLedger || [],
  scenarioCardTemplateRequiredCards: data.scenarioCardTemplate?.requiredCards || [],
  scenarioEvaluationRegistry: data.scenarioEvaluationRegistry || [],
  toyNcgEvaluationSpecSteps: data.toyNcgEvaluationSpec?.evaluationSteps || [],
  toyNcgEvaluationRegistry: data.toyNcgEvaluationRegistry || [],
  ncgFormulaDecompositionBlocks: data.ncgFormulaDecompositionFigure?.blocks || [],
  preSubmissionReviewRegister: data.preSubmissionReviewRegister || [],
  citationContextReviewPacketRows: citationContextPacket?.details?.contextPackets || [],
  citationContextLocalReviewRows: citationContextLocalReview?.details?.contextReviews || [],
  scenarioEvaluationAuditRows: scenarioEvaluationAudit?.evaluations || [],
};

const paperPlan = data.paperPlan || {};

for (const [key, minimum] of Object.entries(minimumCounts)) {
  const actual = collections[key]?.length || 0;
  if (actual < minimum) {
    pushFinding(findings, "fail", "minimum-count", `${key} count ${actual} is below minimum ${minimum}.`);
  }
}

for (const required of requiredPageStrings) {
  if (!page.includes(required)) {
    pushFinding(findings, "fail", "page-string-missing", `Page is missing required string: ${required}`);
  }
}

const sourceKeys = new Set(collections.sources.map((source) => source.key));
const claimIds = new Set(collections.claims.map((claim) => claim.id));
const variableSymbols = new Set(collections.variables.map((variable) => variable.symbol));
const assumptionIds = new Set(collections.modelAssumptions.map((assumption) => assumption.id));
const propositionIds = new Set(collections.propositionRegister.map((proposition) => proposition.id));
const maturityClaimIds = new Set(collections.claimMaturityRegister.map((entry) => entry.claimId));
const falsifierClaimIds = new Set(collections.falsifierRegister.map((entry) => entry.claimId));
const ledgerSourceKeys = new Set(collections.sourceCardLedger.map((entry) => entry.sourceKey));
const scenarioIds = new Set(collections.scenarioEvaluationRegistry.map((entry) => entry.id));
const toyNcgEvaluationIds = new Set(collections.toyNcgEvaluationRegistry.map((entry) => entry.id));
const figureIds = new Set(collections.figurePlan.map((figure) => figure.id));
const preSubmissionReviewIds = new Set(collections.preSubmissionReviewRegister.map((entry) => entry.id));
const citationContextPacketIds = new Set(collections.citationContextReviewPacketRows.map((entry) => entry.id));
const citationContextLocalReviewIds = new Set(collections.citationContextLocalReviewRows.map((entry) => entry.contextId));
const scenarioEvaluationAuditIds = new Set(collections.scenarioEvaluationAuditRows.map((entry) => entry.id));

if (sourceKeys.size !== collections.sources.length) {
  pushFinding(findings, "fail", "duplicate-source-key", "Source cards contain duplicate keys.");
}

if (claimIds.size !== collections.claims.length) {
  pushFinding(findings, "fail", "duplicate-claim-id", "Claim register contains duplicate IDs.");
}

if (variableSymbols.size !== collections.variables.length) {
  pushFinding(findings, "fail", "duplicate-variable-symbol", "Variable dictionary contains duplicate symbols.");
}

if (assumptionIds.size !== collections.modelAssumptions.length) {
  pushFinding(findings, "fail", "duplicate-assumption-id", "Model assumptions contain duplicate IDs.");
}

if (propositionIds.size !== collections.propositionRegister.length) {
  pushFinding(findings, "fail", "duplicate-proposition-id", "Proposition register contains duplicate IDs.");
}

if (maturityClaimIds.size !== collections.claimMaturityRegister.length) {
  pushFinding(findings, "fail", "duplicate-claim-maturity", "Claim maturity register contains duplicate claim IDs.");
}

if (falsifierClaimIds.size !== collections.falsifierRegister.length) {
  pushFinding(findings, "fail", "duplicate-falsifier", "Falsifier register contains duplicate claim IDs.");
}

if (ledgerSourceKeys.size !== collections.sourceCardLedger.length) {
  pushFinding(findings, "fail", "duplicate-source-ledger", "Source card ledger contains duplicate source keys.");
}

if (scenarioIds.size !== collections.scenarioEvaluationRegistry.length) {
  pushFinding(findings, "fail", "duplicate-scenario-id", "Scenario evaluation registry contains duplicate IDs.");
}

if (toyNcgEvaluationIds.size !== collections.toyNcgEvaluationRegistry.length) {
  pushFinding(findings, "fail", "duplicate-toy-ncg-id", "Toy NCG evaluation registry contains duplicate IDs.");
}

if (preSubmissionReviewIds.size !== collections.preSubmissionReviewRegister.length) {
  pushFinding(findings, "fail", "duplicate-pre-submission-review-id", "Pre-submission review register contains duplicate IDs.");
}

if (citationContextPacketIds.size !== collections.citationContextReviewPacketRows.length) {
  pushFinding(findings, "fail", "duplicate-citation-context-packet-id", "Citation context review packet contains duplicate context IDs.");
}

if (citationContextLocalReviewIds.size !== collections.citationContextLocalReviewRows.length) {
  pushFinding(findings, "fail", "duplicate-citation-context-local-review-id", "Citation context local review contains duplicate context IDs.");
}

if (scenarioEvaluationAuditIds.size !== collections.scenarioEvaluationAuditRows.length) {
  pushFinding(findings, "fail", "duplicate-scenario-evaluation-audit-id", "Scenario evaluation audit rows contain duplicate IDs.");
}

const paperPlanMissing = missingFields(paperPlan, [
  "workingTitle",
  "oneSentenceContribution",
  "paperType",
  "targetForm",
  "readerPromise",
]);
if (paperPlanMissing.length > 0) {
  pushFinding(findings, "fail", "paper-plan-fields-missing", `paperPlan missing fields: ${paperPlanMissing.join(", ")}.`);
}

if (!Array.isArray(paperPlan.sectionPlan) || paperPlan.sectionPlan.length < 5) {
  pushFinding(findings, "fail", "paper-plan-section-count", "paperPlan.sectionPlan must contain at least 5 macro sections.");
} else {
  for (const section of paperPlan.sectionPlan) {
    const missing = missingFields(section, ["section", "purpose", "mustContain"]);
    if (missing.length > 0) {
      pushFinding(findings, "fail", "paper-plan-section-fields-missing", `${section.section || "unknown section"} missing fields: ${missing.join(", ")}.`);
    }
    if (!Array.isArray(section.mustContain) || section.mustContain.length === 0) {
      pushFinding(findings, "fail", "paper-plan-section-must-contain-empty", `${section.section || "unknown section"} mustContain is empty.`);
    }
  }
}

for (const source of collections.sources) {
  const missing = missingFields(source, ["key", "title", "authors", "year", "url", "evidenceLayer", "supports", "doesNotSupport"]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "source-fields-missing", `${source.key || "unknown source"} missing fields: ${missing.join(", ")}.`);
  }
}

for (const claim of collections.claims) {
  const missing = missingFields(claim, ["id", "claim", "claimType", "section"]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "claim-fields-missing", `${claim.id || "unknown claim"} missing fields: ${missing.join(", ")}.`);
  }
}

for (const variable of collections.variables) {
  const missing = missingFields(variable, ["symbol", "name", "definition", "modelRole", "notEquivalentTo"]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "variable-fields-missing", `${variable.symbol || "unknown variable"} missing fields: ${missing.join(", ")}.`);
  }
}

for (const assumption of collections.modelAssumptions) {
  const missing = missingFields(assumption, ["id", "assumption", "role", "usedBy", "failureMode"]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "assumption-fields-missing", `${assumption.id || "unknown assumption"} missing fields: ${missing.join(", ")}.`);
  }
  if (!Array.isArray(assumption.usedBy) || assumption.usedBy.length === 0) {
    pushFinding(findings, "fail", "assumption-usedby-empty", `${assumption.id || "unknown assumption"} has no usedBy proposition list.`);
  }
  for (const propositionId of assumption.usedBy || []) {
    if (!propositionIds.has(propositionId)) {
      pushFinding(findings, "fail", "assumption-unknown-proposition", `${assumption.id || "unknown assumption"} references unknown proposition ${propositionId}.`);
    }
  }
}

for (const proposition of collections.propositionRegister) {
  const missing = missingFields(proposition, ["id", "statement", "type", "formula", "dependsOn", "claimIds", "interpretation", "nonClaim"]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "proposition-fields-missing", `${proposition.id || "unknown proposition"} missing fields: ${missing.join(", ")}.`);
  }
  if (!Array.isArray(proposition.dependsOn) || proposition.dependsOn.length === 0) {
    pushFinding(findings, "fail", "proposition-dependson-empty", `${proposition.id || "unknown proposition"} has no dependsOn assumptions.`);
  }
  if (!Array.isArray(proposition.claimIds) || proposition.claimIds.length === 0) {
    pushFinding(findings, "fail", "proposition-claimids-empty", `${proposition.id || "unknown proposition"} has no claimIds.`);
  }
  for (const assumptionId of proposition.dependsOn || []) {
    if (!assumptionIds.has(assumptionId)) {
      pushFinding(findings, "fail", "proposition-unknown-assumption", `${proposition.id || "unknown proposition"} references unknown assumption ${assumptionId}.`);
    }
  }
  for (const claimId of proposition.claimIds || []) {
    if (!claimIds.has(claimId)) {
      pushFinding(findings, "fail", "proposition-unknown-claim", `${proposition.id || "unknown proposition"} references unknown claim ${claimId}.`);
    }
  }
}

for (const maturity of collections.claimMaturityRegister) {
  const missing = missingFields(maturity, [
    "claimId",
    "maturityLevel",
    "evidenceState",
    "currentSupport",
    "missingEvidence",
    "promotionGate",
  ]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "claim-maturity-fields-missing", `${maturity.claimId || "unknown claim"} missing fields: ${missing.join(", ")}.`);
  }
  if (!claimIds.has(maturity.claimId)) {
    pushFinding(findings, "fail", "claim-maturity-unknown-claim", `Claim maturity references unknown claim ${maturity.claimId}.`);
  }
}

for (const falsifier of collections.falsifierRegister) {
  const missing = missingFields(falsifier, [
    "claimId",
    "falsifier",
    "downgradeAction",
    "requiredCheck",
  ]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "falsifier-fields-missing", `${falsifier.claimId || "unknown claim"} missing fields: ${missing.join(", ")}.`);
  }
  if (!claimIds.has(falsifier.claimId)) {
    pushFinding(findings, "fail", "falsifier-unknown-claim", `Falsifier references unknown claim ${falsifier.claimId}.`);
  }
}

for (const ledger of collections.sourceCardLedger) {
  const missing = missingFields(ledger, [
    "sourceKey",
    "sourceRole",
    "mappedClaims",
    "mappedVariables",
    "mechanismUse",
    "allowedUse",
    "forbiddenUse",
    "falsifier",
    "nextAction",
  ]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "source-ledger-fields-missing", `${ledger.sourceKey || "unknown source"} missing fields: ${missing.join(", ")}.`);
  }
  if (!sourceKeys.has(ledger.sourceKey)) {
    pushFinding(findings, "fail", "source-ledger-unknown-source", `Source ledger references unknown source ${ledger.sourceKey}.`);
  }
  if (!Array.isArray(ledger.mappedClaims) || ledger.mappedClaims.length === 0) {
    pushFinding(findings, "fail", "source-ledger-claims-empty", `${ledger.sourceKey || "unknown source"} has no mappedClaims.`);
  }
  if (!Array.isArray(ledger.mappedVariables) || ledger.mappedVariables.length === 0) {
    pushFinding(findings, "fail", "source-ledger-variables-empty", `${ledger.sourceKey || "unknown source"} has no mappedVariables.`);
  }
  for (const claimId of ledger.mappedClaims || []) {
    if (!claimIds.has(claimId)) {
      pushFinding(findings, "fail", "source-ledger-unknown-claim", `${ledger.sourceKey || "unknown source"} references unknown claim ${claimId}.`);
    }
  }
  for (const symbol of ledger.mappedVariables || []) {
    if (!variableSymbols.has(symbol)) {
      pushFinding(findings, "fail", "source-ledger-unknown-variable", `${ledger.sourceKey || "unknown source"} references unknown variable ${symbol}.`);
    }
  }
}

for (const source of collections.sources) {
  if (!ledgerSourceKeys.has(source.key)) {
    pushFinding(findings, "fail", "source-without-ledger", `${source.key} has no sourceCardLedger entry.`);
  }
}

const scenarioTemplate = data.scenarioCardTemplate || {};
const templateMissing = missingFields(scenarioTemplate, ["templateVersion", "purpose", "requiredCards", "entryGate", "nonGoal"]);
if (templateMissing.length > 0) {
  pushFinding(findings, "fail", "scenario-template-fields-missing", `scenarioCardTemplate missing fields: ${templateMissing.join(", ")}.`);
}

for (const card of collections.scenarioCardTemplateRequiredCards) {
  const missing = missingFields(card, ["card", "requiredFields", "rejectIfMissing"]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "scenario-template-card-fields-missing", `${card.card || "unknown card"} missing fields: ${missing.join(", ")}.`);
  }
  if (!Array.isArray(card.requiredFields) || card.requiredFields.length === 0) {
    pushFinding(findings, "fail", "scenario-template-required-empty", `${card.card || "unknown card"} has no requiredFields.`);
  }
  if (!Array.isArray(card.rejectIfMissing) || card.rejectIfMissing.length === 0) {
    pushFinding(findings, "fail", "scenario-template-reject-empty", `${card.card || "unknown card"} has no rejectIfMissing fields.`);
  }
}

const templateCardNames = new Set(collections.scenarioCardTemplateRequiredCards.map((card) => card.card));
for (const scenario of collections.scenarioEvaluationRegistry) {
  const missing = missingFields(scenario, [
    "id",
    "name",
    "scenarioType",
    "status",
    "linkedClaims",
    "purpose",
    "cardStatus",
    "keyVariables",
    "ncgStatus",
    "stopGate",
    "nextEvidenceNeeded",
    "nonClaim",
  ]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "scenario-fields-missing", `${scenario.id || "unknown scenario"} missing fields: ${missing.join(", ")}.`);
  }
  if (!Array.isArray(scenario.linkedClaims) || scenario.linkedClaims.length === 0) {
    pushFinding(findings, "fail", "scenario-claims-empty", `${scenario.id || "unknown scenario"} has no linkedClaims.`);
  }
  if (!Array.isArray(scenario.keyVariables) || scenario.keyVariables.length === 0) {
    pushFinding(findings, "fail", "scenario-variables-empty", `${scenario.id || "unknown scenario"} has no keyVariables.`);
  }
  for (const claimId of scenario.linkedClaims || []) {
    if (!claimIds.has(claimId)) {
      pushFinding(findings, "fail", "scenario-unknown-claim", `${scenario.id || "unknown scenario"} references unknown claim ${claimId}.`);
    }
  }
  for (const symbol of scenario.keyVariables || []) {
    if (!variableSymbols.has(symbol)) {
      pushFinding(findings, "fail", "scenario-unknown-variable", `${scenario.id || "unknown scenario"} references unknown variable ${symbol}.`);
    }
  }
  for (const cardName of templateCardNames) {
    if (!scenario.cardStatus || !Object.prototype.hasOwnProperty.call(scenario.cardStatus, cardName)) {
      pushFinding(findings, "fail", "scenario-card-status-missing", `${scenario.id || "unknown scenario"} is missing cardStatus for ${cardName}.`);
    }
  }
}

const toyNcgSpec = data.toyNcgEvaluationSpec || {};
const toyNcgSpecMissing = missingFields(toyNcgSpec, [
  "protocolVersion",
  "purpose",
  "inputContract",
  "normalizationRule",
  "formula",
  "evaluationSteps",
  "interpretationRule",
  "forbiddenUse",
  "promotionGate",
]);
if (toyNcgSpecMissing.length > 0) {
  pushFinding(findings, "fail", "toy-ncg-spec-fields-missing", `toyNcgEvaluationSpec missing fields: ${toyNcgSpecMissing.join(", ")}.`);
}

for (const input of toyNcgSpec.inputContract || []) {
  const missing = missingFields(input, ["field", "sourceCard", "variable", "requiredStatus", "rejectIfMissing"]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "toy-ncg-input-fields-missing", `${input.field || "unknown input"} missing fields: ${missing.join(", ")}.`);
  }
  if (input.variable && !variableSymbols.has(input.variable)) {
    pushFinding(findings, "fail", "toy-ncg-input-unknown-variable", `${input.field || "unknown input"} references unknown variable ${input.variable}.`);
  }
  if (input.sourceCard && !templateCardNames.has(input.sourceCard)) {
    pushFinding(findings, "fail", "toy-ncg-input-unknown-card", `${input.field || "unknown input"} references unknown scenario card ${input.sourceCard}.`);
  }
}

for (const step of collections.toyNcgEvaluationSpecSteps) {
  const missing = missingFields(step, ["step", "operation", "reason", "failureIf"]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "toy-ncg-step-fields-missing", `${step.step || "unknown step"} missing fields: ${missing.join(", ")}.`);
  }
}

for (const evaluation of collections.toyNcgEvaluationRegistry) {
  const missing = missingFields(evaluation, [
    "id",
    "scenarioId",
    "evaluationStatus",
    "normalizedInputs",
    "expectedNcgDirection",
    "dominantBlocker",
    "decision",
    "linkedClaims",
    "requiredNextWork",
    "nonClaim",
  ]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "toy-ncg-evaluation-fields-missing", `${evaluation.id || "unknown evaluation"} missing fields: ${missing.join(", ")}.`);
  }
  if (!scenarioIds.has(evaluation.scenarioId)) {
    pushFinding(findings, "fail", "toy-ncg-evaluation-unknown-scenario", `${evaluation.id || "unknown evaluation"} references unknown scenario ${evaluation.scenarioId}.`);
  }
  if (!Array.isArray(evaluation.linkedClaims) || evaluation.linkedClaims.length === 0) {
    pushFinding(findings, "fail", "toy-ncg-evaluation-claims-empty", `${evaluation.id || "unknown evaluation"} has no linkedClaims.`);
  }
  if (!Array.isArray(evaluation.normalizedInputs) || evaluation.normalizedInputs.length === 0) {
    pushFinding(findings, "fail", "toy-ncg-evaluation-inputs-empty", `${evaluation.id || "unknown evaluation"} has no normalizedInputs.`);
  }
  for (const claimId of evaluation.linkedClaims || []) {
    if (!claimIds.has(claimId)) {
      pushFinding(findings, "fail", "toy-ncg-evaluation-unknown-claim", `${evaluation.id || "unknown evaluation"} references unknown claim ${claimId}.`);
    }
  }
  for (const input of evaluation.normalizedInputs || []) {
    const missingInput = missingFields(input, ["symbol", "status", "notes"]);
    if (missingInput.length > 0) {
      pushFinding(findings, "fail", "toy-ncg-evaluation-input-fields-missing", `${evaluation.id || "unknown evaluation"} has normalized input missing fields: ${missingInput.join(", ")}.`);
    }
    if (input.symbol && !variableSymbols.has(input.symbol)) {
      pushFinding(findings, "fail", "toy-ncg-evaluation-unknown-variable", `${evaluation.id || "unknown evaluation"} references unknown variable ${input.symbol}.`);
    }
  }
}

const ncgFigure = data.ncgFormulaDecompositionFigure || {};
const ncgFigureMissing = missingFields(ncgFigure, [
  "figureId",
  "title",
  "purpose",
  "layout",
  "formula",
  "blocks",
  "caption",
  "designAudit",
]);
if (ncgFigureMissing.length > 0) {
  pushFinding(findings, "fail", "ncg-figure-fields-missing", `ncgFormulaDecompositionFigure missing fields: ${ncgFigureMissing.join(", ")}.`);
}
if (ncgFigure.figureId && !figureIds.has(ncgFigure.figureId)) {
  pushFinding(findings, "fail", "ncg-figure-unknown-figure-id", `NCG formula figure references unknown figure ${ncgFigure.figureId}.`);
}
for (const block of collections.ncgFormulaDecompositionBlocks) {
  const missing = missingFields(block, ["id", "group", "operation", "variables", "role", "interpretation"]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "ncg-figure-block-fields-missing", `${block.id || "unknown block"} missing fields: ${missing.join(", ")}.`);
  }
  if (!Array.isArray(block.variables) || block.variables.length === 0) {
    pushFinding(findings, "fail", "ncg-figure-block-variables-empty", `${block.id || "unknown block"} has no variables.`);
  }
  for (const symbol of block.variables || []) {
    if (!variableSymbols.has(symbol)) {
      pushFinding(findings, "fail", "ncg-figure-block-unknown-variable", `${block.id || "unknown block"} references unknown variable ${symbol}.`);
    }
  }
}

const validReviewSeverities = new Set(["CRITICAL", "MAJOR", "MINOR"]);
const validReviewStatuses = new Set(["blocks-submission", "major-revision-needed", "polish-before-submission"]);
for (const review of collections.preSubmissionReviewRegister) {
  const missing = missingFields(review, [
    "id",
    "dimension",
    "severity",
    "finding",
    "quotedEvidence",
    "blockingGate",
    "suggestedFix",
    "linkedSections",
    "status",
  ]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "pre-submission-review-fields-missing", `${review.id || "unknown review"} missing fields: ${missing.join(", ")}.`);
  }
  if (review.severity && !validReviewSeverities.has(review.severity)) {
    pushFinding(findings, "fail", "pre-submission-review-bad-severity", `${review.id || "unknown review"} uses invalid severity ${review.severity}.`);
  }
  if (review.status && !validReviewStatuses.has(review.status)) {
    pushFinding(findings, "fail", "pre-submission-review-bad-status", `${review.id || "unknown review"} uses invalid status ${review.status}.`);
  }
  if (!Array.isArray(review.linkedSections) || review.linkedSections.length === 0) {
    pushFinding(findings, "fail", "pre-submission-review-sections-empty", `${review.id || "unknown review"} has no linkedSections.`);
  }
}
if (!collections.preSubmissionReviewRegister.some((review) => review.severity === "CRITICAL")) {
  pushFinding(findings, "fail", "pre-submission-review-no-critical", "Pre-submission review register must keep at least one CRITICAL blocker until external evidence and reproducibility gaps are closed.");
}

if (!citationContextPacket) {
  pushFinding(findings, "fail", "citation-context-packet-missing", `Citation context review packet is missing: ${path.relative(webRoot, citationContextPacketPath)}`);
} else {
  if (citationContextPacket.verdict !== "READY_FOR_EXTERNAL_REVIEW") {
    pushFinding(findings, "fail", "citation-context-packet-verdict", `Citation context packet verdict is ${citationContextPacket.verdict}.`);
  }
  for (const row of collections.citationContextReviewPacketRows) {
    const missing = missingFields(row, ["id", "context", "claimIds", "sourceKeys", "safeUse", "forbiddenUse", "localReviewStatus", "reviewerPrompt"]);
    if (missing.length > 0) {
      pushFinding(findings, "fail", "citation-context-packet-fields-missing", `${row.id || "unknown context"} missing fields: ${missing.join(", ")}.`);
    }
    if (!collections.citationContextRegister.some((context) => context.id === row.id)) {
      pushFinding(findings, "fail", "citation-context-packet-unknown-context", `${row.id || "unknown context"} is not in citationContextRegister.`);
    }
  }
}

if (!citationContextLocalReview) {
  pushFinding(findings, "fail", "citation-context-local-review-missing", `Citation context local review is missing: ${path.relative(webRoot, citationContextLocalReviewPath)}`);
} else {
  if (citationContextLocalReview.verdict !== "LOCAL_REVIEW_COMPLETE_REQUIRES_FRESH_REVIEW") {
    pushFinding(findings, "fail", "citation-context-local-review-verdict", `Citation context local review verdict is ${citationContextLocalReview.verdict}.`);
  }
  for (const row of collections.citationContextLocalReviewRows) {
    const missing = missingFields(row, ["contextId", "riskTier", "localVerdict", "claimIds", "sourceKeys", "safeUse", "forbiddenUse", "freshReviewerFocus"]);
    if (missing.length > 0) {
      pushFinding(findings, "fail", "citation-context-local-review-fields-missing", `${row.contextId || "unknown context"} missing fields: ${missing.join(", ")}.`);
    }
    if (!collections.citationContextRegister.some((context) => context.id === row.contextId)) {
      pushFinding(findings, "fail", "citation-context-local-review-unknown-context", `${row.contextId || "unknown context"} is not in citationContextRegister.`);
    }
  }
}

if (!scenarioEvaluationAudit) {
  pushFinding(findings, "fail", "scenario-evaluation-audit-missing", `Scenario evaluation audit is missing: ${path.relative(webRoot, scenarioEvaluationAuditPath)}`);
} else {
  if (scenarioEvaluationAudit.verdict !== "PASS") {
    pushFinding(findings, "fail", "scenario-evaluation-audit-not-pass", `Scenario evaluation audit verdict is ${scenarioEvaluationAudit.verdict}.`);
  }
  for (const row of collections.scenarioEvaluationAuditRows) {
    const missing = missingFields(row, [
      "id",
      "scenarioId",
      "scenarioName",
      "evaluationStatus",
      "evaluationClass",
      "expectedNcgDirection",
      "canEnterQuantitativeNcg",
      "dominantBlocker",
      "decision",
      "requiredNextWork",
      "nonClaim",
    ]);
    if (missing.length > 0) {
      pushFinding(findings, "fail", "scenario-evaluation-audit-fields-missing", `${row.id || "unknown row"} missing fields: ${missing.join(", ")}.`);
    }
    if (!scenarioIds.has(row.scenarioId)) {
      pushFinding(findings, "fail", "scenario-evaluation-audit-unknown-scenario", `${row.id || "unknown row"} references unknown scenario ${row.scenarioId}.`);
    }
    if (!toyNcgEvaluationIds.has(row.id)) {
      pushFinding(findings, "fail", "scenario-evaluation-audit-unknown-evaluation", `${row.id || "unknown row"} has no matching toy NCG evaluation.`);
    }
  }
}

for (const claim of collections.claims) {
  if (!maturityClaimIds.has(claim.id)) {
    pushFinding(findings, "fail", "claim-without-maturity", `${claim.id} has no claimMaturityRegister entry.`);
  }
  if (!falsifierClaimIds.has(claim.id)) {
    pushFinding(findings, "fail", "claim-without-falsifier", `${claim.id} has no falsifierRegister entry.`);
  }
}

for (const figure of collections.figurePlan) {
  const missing = missingFields(figure, ["id", "type", "description", "dataSource", "priority", "caption", "designAudit", "status"]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "figure-plan-fields-missing", `${figure.id || "unknown figure"} missing fields: ${missing.join(", ")}.`);
  }
}

for (const context of collections.citationContextRegister) {
  const missing = missingFields(context, ["id", "claimIds", "sourceKeys", "context", "safeUse", "forbiddenUse", "reviewStatus"]);
  if (missing.length > 0) {
    pushFinding(findings, "fail", "citation-context-fields-missing", `${context.id || "unknown context"} missing fields: ${missing.join(", ")}.`);
  }
  if (!Array.isArray(context.claimIds) || context.claimIds.length === 0) {
    pushFinding(findings, "fail", "citation-context-claim-empty", `${context.id || "unknown context"} has no claimIds.`);
  }
  if (!Array.isArray(context.sourceKeys) || context.sourceKeys.length === 0) {
    pushFinding(findings, "fail", "citation-context-source-empty", `${context.id || "unknown context"} has no sourceKeys.`);
  }
  for (const claimId of context.claimIds || []) {
    if (!claimIds.has(claimId)) {
      pushFinding(findings, "fail", "citation-context-unknown-claim", `${context.id || "unknown context"} references unknown claim ${claimId}.`);
    }
  }
  for (const sourceKey of context.sourceKeys || []) {
    if (!sourceKeys.has(sourceKey)) {
      pushFinding(findings, "fail", "citation-context-unknown-source", `${context.id || "unknown context"} references unknown source ${sourceKey}.`);
    }
  }
  if (context.reviewStatus !== "LOCAL_PRECHECK_ONLY") {
    pushFinding(findings, "fail", "citation-context-review-status", `${context.id || "unknown context"} must use LOCAL_PRECHECK_ONLY before external reviewer results exist.`);
  }
}

const mappedClaimIds = new Set(collections.claimEvidenceMap.map((entry) => entry.claimId));
for (const claim of collections.claims) {
  if (!mappedClaimIds.has(claim.id)) {
    pushFinding(findings, "fail", "claim-without-evidence-map", `${claim.id} has no claimEvidenceMap entry.`);
  }
}

for (const entry of collections.claimEvidenceMap) {
  if (!claimIds.has(entry.claimId)) {
    pushFinding(findings, "fail", "unknown-claim-map", `claimEvidenceMap references unknown claim ${entry.claimId}.`);
  }
  for (const sourceKey of entry.sourceKeys || []) {
    if (!sourceKeys.has(sourceKey)) {
      pushFinding(findings, "fail", "unknown-source-key", `${entry.claimId} references unknown source ${sourceKey}.`);
    }
  }
  for (const symbol of entry.requiredVariables || []) {
    if (!variableSymbols.has(symbol)) {
      pushFinding(findings, "fail", "unknown-variable-symbol", `${entry.claimId} references unknown variable ${symbol}.`);
    }
  }
  if (!entry.boundary) {
    pushFinding(findings, "fail", "missing-boundary", `${entry.claimId} is missing boundary text.`);
  }
}

const allMappedSources = unique(collections.claimEvidenceMap.flatMap((entry) => entry.sourceKeys || []));
for (const source of collections.sources) {
  if (!allMappedSources.includes(source.key)) {
    pushFinding(findings, "warn", "unused-source-card", `${source.key} is not used by any claimEvidenceMap entry.`);
  }
}

for (const sectionId of ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S13", "S14", "S15", "S16", "S17", "S18", "S19"]) {
  if (!page.includes(`id="${sectionId}"`)) {
    pushFinding(findings, "fail", "page-section-missing", `Page is missing section ${sectionId}.`);
  }
}

if (!toolSeed) {
  pushFinding(findings, "fail", "tool-seed-missing", `Tool-generated seed is missing: ${path.relative(webRoot, toolSeedPath)}`);
} else {
  for (const required of ["PaperReaderLayout", "ltx_page_navbar", "ltx_TOC", "ltx_document", "ltx_abstract", "ltx_bibliography"]) {
    if (!toolSeed.includes(required)) {
      pushFinding(findings, "fail", "tool-seed-contract-missing", `Tool seed is missing ${required}.`);
    }
  }
}

const hasFail = findings.some((finding) => finding.severity === "fail");
const hasWarn = findings.some((finding) => finding.severity === "warn");
const verdict = hasFail ? "FAIL" : hasWarn ? "WARN" : "PASS";

const audit = {
  audit: "metric-redshift-recursive-waiting-coverage",
  generatedAt: new Date().toISOString(),
  verdict,
  counts: Object.fromEntries(Object.entries(collections).map(([key, value]) => [key, value.length])),
  findings,
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(auditJsonPath, `${JSON.stringify(audit, null, 2)}\n`);

const md = [
  "# Metric Redshift Recursive Waiting Coverage Audit",
  "",
  `**Generated**: ${audit.generatedAt}`,
  `**Verdict**: ${audit.verdict}`,
  "",
  "## Counts",
  "",
  "| Item | Count |",
  "| --- | ---: |",
  ...Object.entries(audit.counts).map(([key, value]) => `| ${key} | ${value} |`),
  "",
  "## Findings",
  "",
  findings.length === 0
    ? "No findings."
    : findings.map((finding) => `- **${finding.severity.toUpperCase()} ${finding.code}**: ${finding.message}`).join("\n"),
  "",
].join("\n");

fs.writeFileSync(auditMdPath, md);

console.log(`metric-redshift coverage verdict ${verdict}`);
console.log(`claims ${collections.claims.length}`);
console.log(`sources ${collections.sources.length}`);
console.log(`variables ${collections.variables.length}`);
console.log(`findings ${findings.length}`);
console.log(`wrote ${path.relative(webRoot, auditJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, auditMdPath)}`);

if (verdict === "FAIL") {
  process.exitCode = 1;
}
