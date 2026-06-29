# Fresh Reviewer Context Packet: CTX8

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`
Packet hash: `sha256:da10b8b501204fcc98a220c29488963000b8070ce220e9d00b24bd0617807cc3`

## Review Boundary

This packet is for an external fresh reviewer. Do not treat local review verdicts as proof. Re-open the listed sources or PDFs, then judge whether the sources support the registered safe use and whether the manuscript violates the forbidden-use boundary.

## Context

| Field | Value |
| --- | --- |
| Priority | 12 |
| Context | CTX8 |
| Risk tier | LOW |
| Risk score | 2 |
| Source group | NIST AI RMF; Guidelines for Human-AI Interaction; NASA-TLX; Automation taxonomy |
| Claims | CL2, CL4, CL6, CL7 |
| Used for | 给 A/Q -> risk、QA 成本、任务负荷、自动化等级和人机控制权提供治理语言。 |
| Safe use | 风险识别、测量、纠错、回滚和人机协作设计边界。 |
| Forbidden use | 治理框架和交互指南不提供收益估计，也不证明 AI 能延寿。 |
| Local verdict | KEEP_AS_METHOD_OR_FRAME_LANGUAGE |
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
| `amershi2019hai` | Guidelines for Human-AI Interaction | crossref-verified | PASS | 提供人机协作设计、纠错和控制权边界。 |
| `burwell2017bciEthics` | Ethical aspects of brain computer interfaces: a scoping review | doi-verified | PASS | 为脑机接口、神经技术、同意、身份和主体边界提供风险治理入口。 |
| `dellacqua2026jagged` | Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality | crossref-verified | PASS | 支持 AI 收益与风险具有任务边界。 |
| `nasaTlx` | NASA Task Load Index | official-web-registered | PASS | 提供任务负荷、时间压力、努力和挫败感测量入口。 |
| `nist2023airmf` | Artificial Intelligence Risk Management Framework (AI RMF 1.0) | official-url-200 | PASS | 提供 AI 风险识别、测量、治理和回滚语言。 |
| `parasuraman2000automation` | A model for types and levels of human interaction with automation | crossref-verified | PASS | 拆分自动化类型、等级和人机控制权。 |

## Prompt

```text
你是独立引用语境审稿人。不要使用项目作者的本地结论作为证据，必须重新打开来源并检查正文语境。

Context: CTX8
Source group: NIST AI RMF; Guidelines for Human-AI Interaction; NASA-TLX; Automation taxonomy
Risk: LOW / score 2
Claims: CL2, CL4, CL6, CL7
Used for: 给 A/Q -> risk、QA 成本、任务负荷、自动化等级和人机控制权提供治理语言。
Safe use: 风险识别、测量、纠错、回滚和人机协作设计边界。
Forbidden use: 治理框架和交互指南不提供收益估计，也不证明 AI 能延寿。

References:
- amershi2019hai: Guidelines for Human-AI Interaction (crossref-verified; PASS)
- burwell2017bciEthics: Ethical aspects of brain computer interfaces: a scoping review (doi-verified; PASS)
- dellacqua2026jagged: Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality (crossref-verified; PASS)
- nasaTlx: NASA Task Load Index (official-web-registered; PASS)
- nist2023airmf: Artificial Intelligence Risk Management Framework (AI RMF 1.0) (official-url-200; PASS)
- parasuraman2000automation: A model for types and levels of human interaction with automation (crossref-verified; PASS)

请逐项输出：
1. reference_existence: PASS / FAIL / UNCERTAIN，并给出核验 URL。
2. safe_use_support: SUPPORTS / WEAK / WRONG，并说明来源文本如何支持或不支持。
3. forbidden_use_violation: NONE / POSSIBLE / PRESENT。
4. required_action: KEEP / SOFTEN / REWRITE / REMOVE / REPLACE_SOURCE。
5. one_sentence_reason: 一句话说明 verdict。
```

## Result Stub

Copy this object into `results/CTX8.json` after review, replacing null values with the external reviewer verdict. Keep that per-context file in the results directory; `npm run assemble:fresh-reviewer-results` is the only supported way to create `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`.

```json
{
  "context_id": "CTX8",
  "priority": 12,
  "risk_tier": "LOW",
  "source_group": "NIST AI RMF; Guidelines for Human-AI Interaction; NASA-TLX; Automation taxonomy",
  "claims": [
    "CL2",
    "CL4",
    "CL6",
    "CL7"
  ],
  "references": [
    "amershi2019hai",
    "burwell2017bciEthics",
    "dellacqua2026jagged",
    "nasaTlx",
    "nist2023airmf",
    "parasuraman2000automation"
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
