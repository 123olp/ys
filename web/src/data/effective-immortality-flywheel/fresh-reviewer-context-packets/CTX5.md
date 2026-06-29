# Fresh Reviewer Context Packet: CTX5

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`
Packet hash: `sha256:49f51628c09a88d652b154cebd2dd20fb603ed9857909e4684883c8fe30f0c6b`

## Review Boundary

This packet is for an external fresh reviewer. Do not treat local review verdicts as proof. Re-open the listed sources or PDFs, then judge whether the sources support the registered safe use and whether the manuscript violates the forbidden-use boundary.

## Context

| Field | Value |
| --- | --- |
| Priority | 3 |
| Context | CTX5 |
| Risk tier | MEDIUM |
| Risk score | 4 |
| Source group | Human Capital; Social Capital; Social Relationships Mortality |
| Claims | CL1, CL2, CL5 |
| Used for | 说明经验、资源、信誉和协作网络如何进入 C 与 O，并可能反哺 T/E。 |
| Safe use | 积累资本、社会支持和死亡风险关联的讨论。 |
| Forbidden use | 不能把社会关系关联直接升级成具体干预的因果延寿结论。 |
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
| `coleman1988socialCapital` | Social Capital in the Creation of Human Capital | doi-verified | PASS | 说明关系、信任、规范和网络如何成为能力形成条件。 |
| `holtlunstad2010social` | Social Relationships and Mortality Risk: A Meta-analytic Review | crossref-verified | PASS | 讨论社会关系与死亡风险的关联证据边界。 |
| `mincer1974humanCapital` | Schooling, Experience, and Earnings | official-archive | PASS | 说明教育、经验和长期积累如何进入人力资本模型。 |

## Prompt

```text
你是独立引用语境审稿人。不要使用项目作者的本地结论作为证据，必须重新打开来源并检查正文语境。

Context: CTX5
Source group: Human Capital; Social Capital; Social Relationships Mortality
Risk: MEDIUM / score 4
Claims: CL1, CL2, CL5
Used for: 说明经验、资源、信誉和协作网络如何进入 C 与 O，并可能反哺 T/E。
Safe use: 积累资本、社会支持和死亡风险关联的讨论。
Forbidden use: 不能把社会关系关联直接升级成具体干预的因果延寿结论。

References:
- coleman1988socialCapital: Social Capital in the Creation of Human Capital (doi-verified; PASS)
- holtlunstad2010social: Social Relationships and Mortality Risk: A Meta-analytic Review (crossref-verified; PASS)
- mincer1974humanCapital: Schooling, Experience, and Earnings (official-archive; PASS)

请逐项输出：
1. reference_existence: PASS / FAIL / UNCERTAIN，并给出核验 URL。
2. safe_use_support: SUPPORTS / WEAK / WRONG，并说明来源文本如何支持或不支持。
3. forbidden_use_violation: NONE / POSSIBLE / PRESENT。
4. required_action: KEEP / SOFTEN / REWRITE / REMOVE / REPLACE_SOURCE。
5. one_sentence_reason: 一句话说明 verdict。
```

## Result Stub

Copy this object into `results/CTX5.json` after review, replacing null values with the external reviewer verdict. Keep that per-context file in the results directory; `npm run assemble:fresh-reviewer-results` is the only supported way to create `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`.

```json
{
  "context_id": "CTX5",
  "priority": 3,
  "risk_tier": "MEDIUM",
  "source_group": "Human Capital; Social Capital; Social Relationships Mortality",
  "claims": [
    "CL1",
    "CL2",
    "CL5"
  ],
  "references": [
    "coleman1988socialCapital",
    "holtlunstad2010social",
    "mincer1974humanCapital"
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
