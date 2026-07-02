import {mkdir, readFile, writeFile} from "node:fs/promises";
import {dirname, resolve} from "node:path";
import {fileURLToPath} from "node:url";

const scriptDir = dirname(fileURLToPath(import.meta.url));
const webRoot = resolve(scriptDir, "..");
const repoRoot = resolve(webRoot, "..");

const inputs = {
  higherOrderEffects: resolve(
    repoRoot,
    "domains/c1-boundary-rewriting/longevity-evidence/data/manual/higher_order_effects.tsv"
  ),
  routeCards: resolve(
    repoRoot,
    "domains/c1-boundary-rewriting/longevity-evidence/data/manual/lev_route_cards.tsv"
  )
};

const outputPath = resolve(webRoot, "src/data/lev-model.json");

function parseTsv(text, fileLabel) {
  const lines = text.trim().split(/\r?\n/);
  const headers = lines.shift()?.split("\t") ?? [];
  if (!headers.length) {
    throw new Error(`${fileLabel}: missing header`);
  }
  return lines.map((line, index) => {
    const values = line.split("\t");
    if (values.length !== headers.length) {
      throw new Error(`${fileLabel}:${index + 2}: expected ${headers.length} fields, got ${values.length}`);
    }
    return Object.fromEntries(headers.map((header, columnIndex) => [header, values[columnIndex]]));
  });
}

function splitList(value) {
  return value
    .split(";")
    .map((item) => item.trim())
    .filter(Boolean);
}

function requireFields(rows, fields, label) {
  for (const [index, row] of rows.entries()) {
    for (const field of fields) {
      if (!row[field] || row[field].trim() === "") {
        throw new Error(`${label}:${index + 2}: missing required field ${field}`);
      }
    }
  }
}

function countBy(items, accessor) {
  const counts = new Map();
  for (const item of items) {
    for (const value of accessor(item)) {
      counts.set(value, (counts.get(value) ?? 0) + 1);
    }
  }
  return [...counts.entries()]
    .map(([id, count]) => ({id, count}))
    .sort((a, b) => b.count - a.count || a.id.localeCompare(b.id));
}

const higherOrderEffects = parseTsv(await readFile(inputs.higherOrderEffects, "utf8"), "higher_order_effects.tsv");
const routeCards = parseTsv(await readFile(inputs.routeCards, "utf8"), "lev_route_cards.tsv");

requireFields(
  higherOrderEffects,
  ["finding_id", "finding", "resource", "effect_order", "probability_gate", "positive_chain", "negative_chain", "domain_refs", "source_refs", "tags"],
  "higher_order_effects.tsv"
);
requireFields(
  routeCards,
  [
    "route_id",
    "route_name",
    "direct_route_type",
    "primary_tags",
    "direct_effect",
    "first_order_effect",
    "second_order_effect",
    "multi_order_effect",
    "probability_gates",
    "positive_chain",
    "negative_chain",
    "bottleneck_domains",
    "source_refs",
    "boundary"
  ],
  "lev_route_cards.tsv"
);

const model = {
  schemaVersion: "human-infra.lev-model.v1",
  generatedAt: new Date().toISOString(),
  sourcePaths: {
    higherOrderEffects:
      "domains/c1-boundary-rewriting/longevity-evidence/data/manual/higher_order_effects.tsv",
    routeCards: "domains/c1-boundary-rewriting/longevity-evidence/data/manual/lev_route_cards.tsv"
  },
  higherOrderEffects: higherOrderEffects.map((row) => ({
    ...row,
    resources: splitList(row.resource),
    gates: splitList(row.probability_gate),
    domains: splitList(row.domain_refs),
    sources: splitList(row.source_refs),
    tagList: splitList(row.tags)
  })),
  routeCards: routeCards.map((row) => ({
    ...row,
    tags: splitList(row.primary_tags),
    gates: splitList(row.probability_gates),
    domains: splitList(row.bottleneck_domains),
    sources: splitList(row.source_refs)
  }))
};

model.summaries = {
  effectCount: model.higherOrderEffects.length,
  routeCount: model.routeCards.length,
  gateCounts: countBy([...model.higherOrderEffects, ...model.routeCards], (row) => row.gates ?? []),
  routeTypeCounts: countBy(model.routeCards, (row) => [row.direct_route_type]),
  tagCounts: countBy([...model.higherOrderEffects, ...model.routeCards], (row) => row.tagList ?? row.tags ?? [])
};

await mkdir(dirname(outputPath), {recursive: true});
await writeFile(outputPath, `${JSON.stringify(model, null, 2)}\n`, "utf8");
console.log(`wrote ${outputPath}`);
console.log(`routes=${model.routeCards.length} higher_order_effects=${model.higherOrderEffects.length}`);
