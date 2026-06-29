# Fresh Reviewer Context Packet: CTX2

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`
Packet hash: `sha256:6e1b5510b3cfc90a42b83baa2296fcf00d95cfa2110090862278132faf348b47`

## Review Boundary

This packet is for an external fresh reviewer. Do not treat local review verdicts as proof. Re-open the listed sources or PDFs, then judge whether the sources support the registered safe use and whether the manuscript violates the forbidden-use boundary.

## Context

| Field | Value |
| --- | --- |
| Priority | 1 |
| Context | CTX2 |
| Risk tier | HIGH |
| Risk score | 6 |
| Source group | Grossman Health Capital; WHO HALE; NICE QALY |
| Claims | CL1, CL2 |
| Used for | 把日历寿命转译为健康质量、有效时间和质量调整时间。 |
| Safe use | T -> E 的测量语言和健康质量调整视角。 |
| Forbidden use | 不能完整定义主体连续性，也不能替代个体医学判断。 |
| Local verdict | KEEP_WITH_STRICT_BOUNDARY |
| Required action before submission | Resolve before any submission-facing claim can be treated as clean. |

## Reviewer Questions

- 优先检查是否把测量语言、规范语言或任务内效果外推成主体持续性、寿命或未来选择权结论。
- 拒绝从方法、关联或指标语言直接跳到具体延寿效果。
- 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
- 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
- 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
- 该来源是否支持 safe use 中登记的最小用途？
- 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
- 如果只支持部分用途，需要把哪一句改成更弱表述？
- 高风险检查：是否把指标、机制、治理、任务内效果或预测语言外推为永生、寿命收益或飞轮成立的实证证据？

## References

| Reference | Title | Audit status | Live status | Registered use |
| --- | --- | --- | --- | --- |
| `grossman1972healthcapital` | On the Concept of Health Capital and the Demand for Health | crossref-verified | PASS | 把健康资本、有效时间和日历时间区分开。 |
| `niceEconomicEvaluation` | Economic evaluation | official-url-200 | PASS | 提供 QALY 与健康经济评价的政策语言。 |
| `whohale7752` | Healthy life expectancy (HALE) metadata | official-url-200 | PASS | 提供健康寿命指标的官方定义入口。 |

## Prompt

```text
你是独立引用语境审稿人。不要使用项目作者的本地结论作为证据，必须重新打开来源并检查正文语境。

Context: CTX2
Source group: Grossman Health Capital; WHO HALE; NICE QALY
Risk: HIGH / score 6
Claims: CL1, CL2
Used for: 把日历寿命转译为健康质量、有效时间和质量调整时间。
Safe use: T -> E 的测量语言和健康质量调整视角。
Forbidden use: 不能完整定义主体连续性，也不能替代个体医学判断。

References:
- grossman1972healthcapital: On the Concept of Health Capital and the Demand for Health (crossref-verified; PASS)
- niceEconomicEvaluation: Economic evaluation (official-url-200; PASS)
- whohale7752: Healthy life expectancy (HALE) metadata (official-url-200; PASS)

请逐项输出：
1. reference_existence: PASS / FAIL / UNCERTAIN，并给出核验 URL。
2. safe_use_support: SUPPORTS / WEAK / WRONG，并说明来源文本如何支持或不支持。
3. forbidden_use_violation: NONE / POSSIBLE / PRESENT。
4. required_action: KEEP / SOFTEN / REWRITE / REMOVE / REPLACE_SOURCE。
5. one_sentence_reason: 一句话说明 verdict。
```

## Result Stub

Copy this object into `results/CTX2.json` after review, replacing null values with the external reviewer verdict. Keep that per-context file in the results directory; `npm run assemble:fresh-reviewer-results` is the only supported way to create `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`.

```json
{
  "context_id": "CTX2",
  "priority": 1,
  "risk_tier": "HIGH",
  "source_group": "Grossman Health Capital; WHO HALE; NICE QALY",
  "claims": [
    "CL1",
    "CL2"
  ],
  "references": [
    "grossman1972healthcapital",
    "niceEconomicEvaluation",
    "whohale7752"
  ],
  "source_protocol_hash": "sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de",
  "reviewer_identity_class": null,
  "reviewed_at": null,
  "source_urls": [],
  "reference_existence": null,
  "safe_use_support": null,
  "forbidden_use_violation": null,
  "required_action": null,
  "resolution_status": "NOT_REVIEWED",
  "reviewer_reason": null,
  "manuscript_change_required": null,
  "manuscript_change_summary": null,
  "reviewer_trace_path": null
}
```
