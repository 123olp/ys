#!/usr/bin/env node
"use strict";

const assert = require("node:assert/strict");
const path = require("node:path");
const core = require(path.join(__dirname, "..", "docs", "reference", "history-timeline", "preview-core.js"));

function sampleEvent(overrides) {
  return Object.assign({
    start_date: { year: -2353, month: 1, day: 2 },
    text: { headline: "测试事件" },
    meta: {
      event_id: "HIT-MTH-001",
      period_label: "上古",
      path_family: "philosophical",
      path_family_label: "哲学判据",
      event_type: "myth",
      event_type_label: "神话与宗教",
      evidence_grade: "I",
      verification_status: "unreviewed",
      publication_status: "candidate",
      source_refs: ["SRC-001", "SRC-002"]
    }
  }, overrides || {});
}

function baseState(overrides) {
  return Object.assign({
    q: "",
    scope: "all",
    period: "",
    path: "",
    type: "",
    evidence: "",
    window: "all"
  }, overrides || {});
}

const event = sampleEvent();
event._searchText = [
  event.text.headline,
  event.meta.event_id,
  event.meta.period_label,
  event.meta.path_family,
  event.meta.path_family_label,
  event.meta.event_type,
  event.meta.event_type_label,
  event.meta.evidence_grade,
  event.meta.verification_status,
  event.meta.publication_status,
  event.meta.source_refs.join(" ")
].join(" ").toLowerCase();

assert.equal(core.dateLabel(event), "公元前 2353 年 1 月 2 日");

const row = core.eventRow(event);
assert.deepEqual(row, [
  "测试事件",
  "HIT-MTH-001",
  "公元前 2353 年 1 月 2 日",
  "上古",
  "哲学判据",
  "神话与宗教",
  "I / unreviewed",
  "候选资料",
  "SRC-001, SRC-002"
]);

const table = core.renderPsqlTable(["标题", "编号"], [row.slice(0, 2)]);
assert.ok(table.startsWith("+"));
assert.ok(table.includes("测试事件"));
assert.ok(table.includes("HIT-MTH-001"));
assert.ok(table.endsWith("+"));

const compact = core.psqlTable(["标题", "编号"], [row.slice(0, 2)]);
assert.ok(compact.includes("测试事件"));
assert.ok(compact.includes("HIT-MTH-001"));

assert.equal(core.matchesEvent(event, baseState()), true);
assert.equal(core.matchesEvent(event, baseState({ scope: "works" })), false);
assert.equal(core.matchesEvent(event, baseState({ scope: "reviewed" })), false);
assert.equal(core.matchesEvent(event, baseState({ period: "上古" })), true);
assert.equal(core.matchesEvent(event, baseState({ period: "近代" })), false);
assert.equal(core.matchesEvent(event, baseState({ path: "philosophical" })), true);
assert.equal(core.matchesEvent(event, baseState({ path: "maintenance" })), false);
assert.equal(core.matchesEvent(event, baseState({ type: "myth" })), true);
assert.equal(core.matchesEvent(event, baseState({ type: "technology" })), false);
assert.equal(core.matchesEvent(event, baseState({ evidence: "I" })), true);
assert.equal(core.matchesEvent(event, baseState({ evidence: "T" })), false);
assert.equal(core.matchesEvent(event, baseState({ window: "ancient" })), true);
assert.equal(core.matchesEvent(event, baseState({ window: "classical" })), false);
assert.equal(core.matchesEvent(event, baseState({ q: "哲学" })), true);
assert.equal(core.matchesEvent(event, baseState({ q: "不存在" })), false);

const selected = sampleEvent({ meta: Object.assign({}, event.meta, { publication_status: "selected" }) });
assert.equal(core.matchesEvent(selected, baseState({ scope: "works" })), true);

console.log("status=OK history_timeline_core=pass");
