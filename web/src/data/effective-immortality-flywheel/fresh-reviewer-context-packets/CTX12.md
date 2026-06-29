# Fresh Reviewer Context Packet: CTX12

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`
Packet hash: `sha256:ff776a253dc911981be4c1029c16c123929689cf6acba9c4a5eda93125f64794`

## Review Boundary

This packet is for an external fresh reviewer. Do not treat local review verdicts as proof. Re-open the listed sources or PDFs, then judge whether the sources support the registered safe use and whether the manuscript violates the forbidden-use boundary.

## Context

| Field | Value |
| --- | --- |
| Priority | 7 |
| Context | CTX12 |
| Risk tier | MEDIUM |
| Risk score | 4 |
| Source group | Capability Approach; WHO SDOH; WHO Primary Health Care |
| Claims | CL1, CL2, CL5 |
| Used for | 定义 O 可能性空间为真实可进入路径，并把资源、制度、医疗和社会条件纳入反哺路径。 |
| Safe use | 真实选择权、健康决定因素、医疗可及和连续照护的规范/公共卫生框架。 |
| Forbidden use | 规范框架不提供寿命预测，也不能替代具体政策或医疗干预评估。 |
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
| `robeyns2021capability` | The Capability Approach | official-web-registered | PASS | 定义真实可行能力和可能性空间。 |
| `whoSdhPhc` | Social determinants of health and primary health care | official-urls-200 | PASS | 把健康和持续性放回收入、教育、住房、工作、环境和医疗可及条件中。 |

## Prompt

```text
你是独立引用语境审稿人。不要使用项目作者的本地结论作为证据，必须重新打开来源并检查正文语境。

Context: CTX12
Source group: Capability Approach; WHO SDOH; WHO Primary Health Care
Risk: MEDIUM / score 4
Claims: CL1, CL2, CL5
Used for: 定义 O 可能性空间为真实可进入路径，并把资源、制度、医疗和社会条件纳入反哺路径。
Safe use: 真实选择权、健康决定因素、医疗可及和连续照护的规范/公共卫生框架。
Forbidden use: 规范框架不提供寿命预测，也不能替代具体政策或医疗干预评估。

References:
- robeyns2021capability: The Capability Approach (official-web-registered; PASS)
- whoSdhPhc: Social determinants of health and primary health care (official-urls-200; PASS)

请逐项输出：
1. reference_existence: PASS / FAIL / UNCERTAIN，并给出核验 URL。
2. safe_use_support: SUPPORTS / WEAK / WRONG，并说明来源文本如何支持或不支持。
3. forbidden_use_violation: NONE / POSSIBLE / PRESENT。
4. required_action: KEEP / SOFTEN / REWRITE / REMOVE / REPLACE_SOURCE。
5. one_sentence_reason: 一句话说明 verdict。
```

## Result Stub

Copy this object into `results/CTX12.json` after review, replacing null values with the external reviewer verdict. Keep that per-context file in the results directory; `npm run assemble:fresh-reviewer-results` is the only supported way to create `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`.

```json
{
  "context_id": "CTX12",
  "priority": 7,
  "risk_tier": "MEDIUM",
  "source_group": "Capability Approach; WHO SDOH; WHO Primary Health Care",
  "claims": [
    "CL1",
    "CL2",
    "CL5"
  ],
  "references": [
    "robeyns2021capability",
    "whoSdhPhc"
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
