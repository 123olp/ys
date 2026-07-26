import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const webRoot = path.resolve(__dirname, "..");

const dataPath = path.join(webRoot, "src/data/metric-redshift-recursive-waiting.json");
const outputDir = path.join(webRoot, "src/data/metric-redshift-recursive-waiting");
const outputJsonPath = path.join(outputDir, "SCENARIO_EVALUATION_AUDIT.json");
const outputMdPath = path.join(outputDir, "SCENARIO_EVALUATION_AUDIT.md");

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function countBy(values) {
  return values.reduce((acc, value) => {
    acc[value] = (acc[value] || 0) + 1;
    return acc;
  }, {});
}

function cardCompleteness(cardStatus) {
  const statuses = Object.values(cardStatus || {});
  const total = statuses.length;
  const complete = statuses.filter((status) => status === "complete").length;
  const partial = statuses.filter((status) => status === "partial").length;
  const blocked = statuses.filter((status) => status === "blocked").length;
  const missing = statuses.filter((status) => status === "missing").length;
  const notApplicable = statuses.filter((status) => status === "not-applicable").length;
  return { total, complete, partial, blocked, missing, notApplicable };
}

function deriveEvaluationClass(evaluation, scenario) {
  if (!scenario) {
    return "invalid-scenario";
  }
  if (evaluation.evaluationStatus === "calibration-only") {
    return "calibration-only";
  }
  if (evaluation.evaluationStatus === "cannot-evaluate") {
    return "cannot-evaluate";
  }
  if (evaluation.evaluationStatus.includes("blocked")) {
    return "blocked";
  }
  if (evaluation.expectedNcgDirection?.includes("negative")) {
    return "negative-direction";
  }
  return "requires-review";
}

function canEnterQuantitativeNcg(evaluation, scenario) {
  if (!scenario) {
    return false;
  }
  if (evaluation.evaluationStatus === "calibration-only" || scenario.status === "not-a-waiting-room") {
    return false;
  }
  if (evaluation.evaluationStatus.includes("blocked") || evaluation.evaluationStatus === "cannot-evaluate") {
    return false;
  }
  const inputs = evaluation.normalizedInputs || [];
  const hasMissingInput = inputs.some((input) => input.status.includes("missing") || input.status.includes("blocked"));
  const cardStats = cardCompleteness(scenario.cardStatus);
  return !hasMissingInput && cardStats.missing === 0 && cardStats.blocked === 0 && evaluation.expectedNcgDirection !== "cannot-evaluate";
}

function makeMarkdown(audit) {
  const rows = audit.evaluations.map((row) => (
    `| ${row.id} | ${row.scenarioId} | ${row.evaluationClass} | ${row.expectedNcgDirection} | ${row.canEnterQuantitativeNcg ? "yes" : "no"} | ${row.dominantBlocker} |`
  ));

  return [
    "# Metric Redshift Scenario Evaluation Audit",
    "",
    `**Generated**: ${audit.generatedAt}`,
    `**Verdict**: ${audit.verdict}`,
    "",
    "## Summary",
    "",
    `- Scenarios: ${audit.summary.scenarios}`,
    `- Toy evaluations: ${audit.summary.toyEvaluations}`,
    `- Quantitative-ready evaluations: ${audit.summary.quantitativeReady}`,
    `- Evaluation classes: ${JSON.stringify(audit.summary.evaluationClasses)}`,
    "",
    "## Evaluations",
    "",
    "| Evaluation | Scenario | Class | NCG Direction | Quantitative-ready | Dominant blocker |",
    "| --- | --- | --- | --- | --- | --- |",
    ...rows,
    "",
    "## Findings",
    "",
    audit.findings.length === 0
      ? "No findings."
      : audit.findings.map((finding) => `- **${finding.severity.toUpperCase()} ${finding.code}**: ${finding.message}`).join("\n"),
    "",
  ].join("\n");
}

const data = readJson(dataPath);
const scenarios = data.scenarioEvaluationRegistry || [];
const evaluations = data.toyNcgEvaluationRegistry || [];
const scenarioById = new Map(scenarios.map((scenario) => [scenario.id, scenario]));
const findings = [];

const evaluatedRows = evaluations.map((evaluation) => {
  const scenario = scenarioById.get(evaluation.scenarioId);
  const inputStates = (evaluation.normalizedInputs || []).map((input) => ({
    symbol: input.symbol,
    status: input.status,
    notes: input.notes,
  }));
  const evaluationClass = deriveEvaluationClass(evaluation, scenario);
  const quantitativeReady = canEnterQuantitativeNcg(evaluation, scenario);

  if (!scenario) {
    findings.push({
      severity: "fail",
      code: "unknown-scenario",
      message: `${evaluation.id} references unknown scenario ${evaluation.scenarioId}.`,
    });
  }

  return {
    id: evaluation.id,
    scenarioId: evaluation.scenarioId,
    scenarioName: scenario?.name || "unknown scenario",
    scenarioStatus: scenario?.status || "unknown",
    evaluationStatus: evaluation.evaluationStatus,
    evaluationClass,
    expectedNcgDirection: evaluation.expectedNcgDirection,
    canEnterQuantitativeNcg: quantitativeReady,
    cardCompleteness: cardCompleteness(scenario?.cardStatus),
    normalizedInputs: inputStates,
    dominantBlocker: evaluation.dominantBlocker,
    decision: evaluation.decision,
    requiredNextWork: evaluation.requiredNextWork,
    nonClaim: evaluation.nonClaim,
  };
});

const scenarioIdsWithEvaluation = new Set(evaluations.map((evaluation) => evaluation.scenarioId));
for (const scenario of scenarios) {
  if (!scenarioIdsWithEvaluation.has(scenario.id)) {
    findings.push({
      severity: "fail",
      code: "scenario-without-evaluation",
      message: `${scenario.id} has no toy NCG evaluation entry.`,
    });
  }
}

const quantitativeReady = evaluatedRows.filter((row) => row.canEnterQuantitativeNcg).length;
const hasFail = findings.some((finding) => finding.severity === "fail");
const verdict = hasFail ? "FAIL" : "PASS";

const audit = {
  audit: "metric-redshift-scenario-evaluation",
  generatedAt: new Date().toISOString(),
  verdict,
  protocolVersion: data.toyNcgEvaluationSpec?.protocolVersion || "unknown",
  summary: {
    scenarios: scenarios.length,
    toyEvaluations: evaluations.length,
    quantitativeReady,
    evaluationClasses: countBy(evaluatedRows.map((row) => row.evaluationClass)),
  },
  evaluations: evaluatedRows,
  findings,
};

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(outputJsonPath, `${JSON.stringify(audit, null, 2)}\n`);
fs.writeFileSync(outputMdPath, makeMarkdown(audit));

console.log(`metric-redshift scenario evaluation verdict ${verdict}`);
console.log(`scenarios ${scenarios.length}`);
console.log(`toy evaluations ${evaluations.length}`);
console.log(`quantitative-ready ${quantitativeReady}`);
console.log(`findings ${findings.length}`);
console.log(`wrote ${path.relative(webRoot, outputJsonPath)}`);
console.log(`wrote ${path.relative(webRoot, outputMdPath)}`);

if (verdict === "FAIL") {
  process.exitCode = 1;
}
