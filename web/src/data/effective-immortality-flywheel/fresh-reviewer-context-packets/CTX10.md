# Fresh Reviewer Context Packet: CTX10

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`
Packet hash: `sha256:aae84842e1fa4b853f6850e7d20f44dca0246b20371cc02a14fe1a0d595a0b14`

## Review Boundary

This packet is for an external fresh reviewer. Do not treat local review verdicts as proof. Re-open the listed sources or PDFs, then judge whether the sources support the registered safe use and whether the manuscript violates the forbidden-use boundary.

## Context

| Field | Value |
| --- | --- |
| Priority | 5 |
| Context | CTX10 |
| Risk tier | MEDIUM |
| Risk score | 4 |
| Source group | Apple Heart Study; Personal Informatics; Lived Informatics; Dynamic Digital Twin |
| Claims | CL6 |
| Used for | 说明观测、反馈、个人数据系统和生命过程建模如何进入状态观测层。 |
| Safe use | observation -> action 的路径和自我追踪/数字孪生的系统问题。 |
| Forbidden use | 早筛、追踪或数字孪生概念不等于死亡风险下降或医疗结局改善。 |
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
| `epstein2015lived` | A lived informatics model of personal informatics | crossref-verified | PASS | 说明长期自我追踪系统的生活嵌入、维护负担和断裂点。 |
| `li2010personalInformatics` | A stage-based model of personal informatics systems | crossref-verified | PASS | 提供个人信息学的准备、收集、整合、反思和行动阶段。 |
| `mulder2022dynamicDigitalTwin` | Dynamic Digital Twin: Diagnosis, Treatment, Prediction, and Prevention of Disease During the Life Course | publisher-verified | PASS | 说明生命过程中的状态观测、预测、预防和数字孪生建模入口。 |
| `perez2019appleHeart` | Large-Scale Assessment of a Smartwatch to Identify Atrial Fibrillation | crossref-verified | PASS | 说明可穿戴设备进入大规模风险提示和临床确认通道。 |

## Prompt

```text
你是独立引用语境审稿人。不要使用项目作者的本地结论作为证据，必须重新打开来源并检查正文语境。

Context: CTX10
Source group: Apple Heart Study; Personal Informatics; Lived Informatics; Dynamic Digital Twin
Risk: MEDIUM / score 4
Claims: CL6
Used for: 说明观测、反馈、个人数据系统和生命过程建模如何进入状态观测层。
Safe use: observation -> action 的路径和自我追踪/数字孪生的系统问题。
Forbidden use: 早筛、追踪或数字孪生概念不等于死亡风险下降或医疗结局改善。

References:
- epstein2015lived: A lived informatics model of personal informatics (crossref-verified; PASS)
- li2010personalInformatics: A stage-based model of personal informatics systems (crossref-verified; PASS)
- mulder2022dynamicDigitalTwin: Dynamic Digital Twin: Diagnosis, Treatment, Prediction, and Prevention of Disease During the Life Course (publisher-verified; PASS)
- perez2019appleHeart: Large-Scale Assessment of a Smartwatch to Identify Atrial Fibrillation (crossref-verified; PASS)

请逐项输出：
1. reference_existence: PASS / FAIL / UNCERTAIN，并给出核验 URL。
2. safe_use_support: SUPPORTS / WEAK / WRONG，并说明来源文本如何支持或不支持。
3. forbidden_use_violation: NONE / POSSIBLE / PRESENT。
4. required_action: KEEP / SOFTEN / REWRITE / REMOVE / REPLACE_SOURCE。
5. one_sentence_reason: 一句话说明 verdict。
```

## Result Stub

Copy this object into `results/CTX10.json` after review, replacing null values with the external reviewer verdict. Keep that per-context file in the results directory; `npm run assemble:fresh-reviewer-results` is the only supported way to create `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`.

```json
{
  "context_id": "CTX10",
  "priority": 5,
  "risk_tier": "MEDIUM",
  "source_group": "Apple Heart Study; Personal Informatics; Lived Informatics; Dynamic Digital Twin",
  "claims": [
    "CL6"
  ],
  "references": [
    "epstein2015lived",
    "li2010personalInformatics",
    "mulder2022dynamicDigitalTwin",
    "perez2019appleHeart"
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
