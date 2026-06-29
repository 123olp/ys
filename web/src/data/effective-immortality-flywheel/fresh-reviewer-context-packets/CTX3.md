# Fresh Reviewer Context Packet: CTX3

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`
Packet hash: `sha256:1405d79c71101e6485bb2e6a2666a348765014ff32214081abafad499ba94772`

## Review Boundary

This packet is for an external fresh reviewer. Do not treat local review verdicts as proof. Re-open the listed sources or PDFs, then judge whether the sources support the registered safe use and whether the manuscript violates the forbidden-use boundary.

## Context

| Field | Value |
| --- | --- |
| Priority | 2 |
| Context | CTX3 |
| Risk tier | MEDIUM |
| Risk score | 4 |
| Source group | Hallmarks of Aging; GrimAge; Cognitive Reserve |
| Claims | CL7 |
| Used for | 提出身体状态、衰老机制、生物年龄信号和认知储备候选变量。 |
| Safe use | 状态变量和风险信号的机制/关联入口。 |
| Forbidden use | 不能把机制综述、预测关联或认知储备直接写成干预效果。 |
| Local verdict | KEEP_WITH_BOUNDARY |
| Required action before submission | Review after high-risk contexts; keep registered boundary language. |

## Reviewer Questions

- 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
- 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
- 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
- 该来源是否支持 safe use 中登记的最小用途？
- 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
- 如果只支持部分用途，需要把哪一句改成更弱表述？

## References

| Reference | Title | Audit status | Live status | Registered use |
| --- | --- | --- | --- | --- |
| `lopezotin2013hallmarks` | The Hallmarks of Aging | crossref-verified | PASS | 提出衰老状态变量和机制入口。 |
| `lu2019grimage` | DNA methylation GrimAge strongly predicts lifespan and healthspan | crossref-verified | PASS | 作为生物年龄、死亡风险和健康寿命信号入口。 |
| `stern2012cognitiveReserve` | Cognitive reserve in ageing and Alzheimer's disease | crossref-verified | PASS | 说明认知储备作为状态变量和风险信号的边界。 |

## Prompt

```text
你是独立引用语境审稿人。不要使用项目作者的本地结论作为证据，必须重新打开来源并检查正文语境。

Context: CTX3
Source group: Hallmarks of Aging; GrimAge; Cognitive Reserve
Risk: MEDIUM / score 4
Claims: CL7
Used for: 提出身体状态、衰老机制、生物年龄信号和认知储备候选变量。
Safe use: 状态变量和风险信号的机制/关联入口。
Forbidden use: 不能把机制综述、预测关联或认知储备直接写成干预效果。

References:
- lopezotin2013hallmarks: The Hallmarks of Aging (crossref-verified; PASS)
- lu2019grimage: DNA methylation GrimAge strongly predicts lifespan and healthspan (crossref-verified; PASS)
- stern2012cognitiveReserve: Cognitive reserve in ageing and Alzheimer's disease (crossref-verified; PASS)

请逐项输出：
1. reference_existence: PASS / FAIL / UNCERTAIN，并给出核验 URL。
2. safe_use_support: SUPPORTS / WEAK / WRONG，并说明来源文本如何支持或不支持。
3. forbidden_use_violation: NONE / POSSIBLE / PRESENT。
4. required_action: KEEP / SOFTEN / REWRITE / REMOVE / REPLACE_SOURCE。
5. one_sentence_reason: 一句话说明 verdict。
```

## Result Stub

Copy this object into `results/CTX3.json` after review, replacing null values with the external reviewer verdict. Keep that per-context file in the results directory; `npm run assemble:fresh-reviewer-results` is the only supported way to create `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`.

```json
{
  "context_id": "CTX3",
  "priority": 2,
  "risk_tier": "MEDIUM",
  "source_group": "Hallmarks of Aging; GrimAge; Cognitive Reserve",
  "claims": [
    "CL7"
  ],
  "references": [
    "lopezotin2013hallmarks",
    "lu2019grimage",
    "stern2012cognitiveReserve"
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
