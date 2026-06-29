# Fresh Reviewer Context Packet: CTX11

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`
Packet hash: `sha256:bbe21dd388f5df084be08f67f09be10bc24e1f3e0b61715344a0bde6ba272dbf`

## Review Boundary

This packet is for an external fresh reviewer. Do not treat local review verdicts as proof. Re-open the listed sources or PDFs, then judge whether the sources support the registered safe use and whether the manuscript violates the forbidden-use boundary.

## Context

| Field | Value |
| --- | --- |
| Priority | 6 |
| Context | CTX11 |
| Risk tier | MEDIUM |
| Risk score | 4 |
| Source group | Extended Mind; Engelbart; Cognition in the Wild |
| Claims | CL6 |
| Used for | 支撑工具、记忆外化、分布式认知和认知增强进入主体系统的理论位置。 |
| Safe use | 主体能力可以由人、工具、表征、环境和协作流程共同支撑。 |
| Forbidden use | 哲学和系统框架不提供数值效应估计，也不能证明数字副本等同于本人。 |
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
| `burwell2017bciEthics` | Ethical aspects of brain computer interfaces: a scoping review | doi-verified | PASS | 为脑机接口、神经技术、同意、身份和主体边界提供风险治理入口。 |
| `clark1998extended` | The Extended Mind | crossref-verified | PASS | 支撑工具、记忆外化和认知扩展进入主体系统。 |
| `engelbart1962augmenting` | Augmenting Human Intellect: A Conceptual Framework | official-archive-registered | PASS | 提供人、工具、概念和方法作为增强系统的经典框架。 |
| `hutchins1995cognition` | Cognition in the Wild | author-page-verified | PASS | 提供分布式认知和环境嵌入式问题求解框架。 |

## Prompt

```text
你是独立引用语境审稿人。不要使用项目作者的本地结论作为证据，必须重新打开来源并检查正文语境。

Context: CTX11
Source group: Extended Mind; Engelbart; Cognition in the Wild
Risk: MEDIUM / score 4
Claims: CL6
Used for: 支撑工具、记忆外化、分布式认知和认知增强进入主体系统的理论位置。
Safe use: 主体能力可以由人、工具、表征、环境和协作流程共同支撑。
Forbidden use: 哲学和系统框架不提供数值效应估计，也不能证明数字副本等同于本人。

References:
- burwell2017bciEthics: Ethical aspects of brain computer interfaces: a scoping review (doi-verified; PASS)
- clark1998extended: The Extended Mind (crossref-verified; PASS)
- engelbart1962augmenting: Augmenting Human Intellect: A Conceptual Framework (official-archive-registered; PASS)
- hutchins1995cognition: Cognition in the Wild (author-page-verified; PASS)

请逐项输出：
1. reference_existence: PASS / FAIL / UNCERTAIN，并给出核验 URL。
2. safe_use_support: SUPPORTS / WEAK / WRONG，并说明来源文本如何支持或不支持。
3. forbidden_use_violation: NONE / POSSIBLE / PRESENT。
4. required_action: KEEP / SOFTEN / REWRITE / REMOVE / REPLACE_SOURCE。
5. one_sentence_reason: 一句话说明 verdict。
```

## Result Stub

Copy this object into `results/CTX11.json` after review, replacing null values with the external reviewer verdict. Keep that per-context file in the results directory; `npm run assemble:fresh-reviewer-results` is the only supported way to create `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`.

```json
{
  "context_id": "CTX11",
  "priority": 6,
  "risk_tier": "MEDIUM",
  "source_group": "Extended Mind; Engelbart; Cognition in the Wild",
  "claims": [
    "CL6"
  ],
  "references": [
    "burwell2017bciEthics",
    "clark1998extended",
    "engelbart1962augmenting",
    "hutchins1995cognition"
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
