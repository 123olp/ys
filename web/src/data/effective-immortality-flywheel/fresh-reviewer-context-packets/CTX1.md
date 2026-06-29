# Fresh Reviewer Context Packet: CTX1

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`
Packet hash: `sha256:4451f9eff9343c8ed3de8fadc56b2bdd582f2888a345febc0280d46b9ee0f16a`

## Review Boundary

This packet is for an external fresh reviewer. Do not treat local review verdicts as proof. Re-open the listed sources or PDFs, then judge whether the sources support the registered safe use and whether the manuscript violates the forbidden-use boundary.

## Context

| Field | Value |
| --- | --- |
| Priority | 9 |
| Context | CTX1 |
| Risk tier | LOW |
| Risk score | 2 |
| Source group | Kaplan-Meier 1958; Cox 1972 |
| Claims | CL2, CL3, CL7 |
| Used for | 定义 T、生存函数 S(t)、删失数据和风险函数 lambda(t) 的统计语言。 |
| Safe use | 事件时间、删失、生存曲线和协变量风险建模的基础方法。 |
| Forbidden use | 不证明任何具体延寿、健康、AI 或资源干预有效。 |
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
| `cox1972regression` | Regression Models and Life-Tables | crossref-verified | PASS | 定义协变量、风险函数和 lambda(t) 的统计语言。 |
| `kaplan1958incomplete` | Nonparametric Estimation from Incomplete Observations | crossref-verified | PASS | 定义生存曲线、删失数据和 T 的统计语言。 |

## Prompt

```text
你是独立引用语境审稿人。不要使用项目作者的本地结论作为证据，必须重新打开来源并检查正文语境。

Context: CTX1
Source group: Kaplan-Meier 1958; Cox 1972
Risk: LOW / score 2
Claims: CL2, CL3, CL7
Used for: 定义 T、生存函数 S(t)、删失数据和风险函数 lambda(t) 的统计语言。
Safe use: 事件时间、删失、生存曲线和协变量风险建模的基础方法。
Forbidden use: 不证明任何具体延寿、健康、AI 或资源干预有效。

References:
- cox1972regression: Regression Models and Life-Tables (crossref-verified; PASS)
- kaplan1958incomplete: Nonparametric Estimation from Incomplete Observations (crossref-verified; PASS)

请逐项输出：
1. reference_existence: PASS / FAIL / UNCERTAIN，并给出核验 URL。
2. safe_use_support: SUPPORTS / WEAK / WRONG，并说明来源文本如何支持或不支持。
3. forbidden_use_violation: NONE / POSSIBLE / PRESENT。
4. required_action: KEEP / SOFTEN / REWRITE / REMOVE / REPLACE_SOURCE。
5. one_sentence_reason: 一句话说明 verdict。
```

## Result Stub

Copy this object into `results/CTX1.json` after review, replacing null values with the external reviewer verdict. Keep that per-context file in the results directory; `npm run assemble:fresh-reviewer-results` is the only supported way to create `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`.

```json
{
  "context_id": "CTX1",
  "priority": 9,
  "risk_tier": "LOW",
  "source_group": "Kaplan-Meier 1958; Cox 1972",
  "claims": [
    "CL2",
    "CL3",
    "CL7"
  ],
  "references": [
    "cox1972regression",
    "kaplan1958incomplete"
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
