# Fresh Reviewer Context Packet: CTX6

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`
Packet hash: `sha256:8327d94320874e3628d33e2585da1146f6a469794015fb76b1edb24f58d5e2e5`

## Review Boundary

This packet is for an external fresh reviewer. Do not treat local review verdicts as proof. Re-open the listed sources or PDFs, then judge whether the sources support the registered safe use and whether the manuscript violates the forbidden-use boundary.

## Context

| Field | Value |
| --- | --- |
| Priority | 11 |
| Context | CTX6 |
| Risk tier | LOW |
| Risk score | 2 |
| Source group | TAM; UTAUT; Diffusion of Innovations |
| Claims | CL1, CL2 |
| Used for | 解释 C -> A：技术采用受有用性、易用性、促进条件、资源和社会影响约束。 |
| Safe use | 技术采用能力的分解：access、understanding、evaluation、trial、integration。 |
| Forbidden use | 不能证明采用后的技术一定有效，也不能覆盖所有高风险医学或神经技术。 |
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
| `davis1989tam` | Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology | crossref-verified | PASS | 解释技术采用能力中的有用性和易用性。 |
| `rogers2003diffusion` | Diffusion of Innovations | bibliographic-record-verified-isbn | PASS | 说明技术成熟、扩散、采用者差异和社会系统时间窗口。 |
| `venkatesh2003utaut` | User Acceptance of Information Technology: Toward a Unified View | crossref-verified | PASS | 解释技术采用中的促进条件、社会影响和努力预期。 |

## Prompt

```text
你是独立引用语境审稿人。不要使用项目作者的本地结论作为证据，必须重新打开来源并检查正文语境。

Context: CTX6
Source group: TAM; UTAUT; Diffusion of Innovations
Risk: LOW / score 2
Claims: CL1, CL2
Used for: 解释 C -> A：技术采用受有用性、易用性、促进条件、资源和社会影响约束。
Safe use: 技术采用能力的分解：access、understanding、evaluation、trial、integration。
Forbidden use: 不能证明采用后的技术一定有效，也不能覆盖所有高风险医学或神经技术。

References:
- davis1989tam: Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology (crossref-verified; PASS)
- rogers2003diffusion: Diffusion of Innovations (bibliographic-record-verified-isbn; PASS)
- venkatesh2003utaut: User Acceptance of Information Technology: Toward a Unified View (crossref-verified; PASS)

请逐项输出：
1. reference_existence: PASS / FAIL / UNCERTAIN，并给出核验 URL。
2. safe_use_support: SUPPORTS / WEAK / WRONG，并说明来源文本如何支持或不支持。
3. forbidden_use_violation: NONE / POSSIBLE / PRESENT。
4. required_action: KEEP / SOFTEN / REWRITE / REMOVE / REPLACE_SOURCE。
5. one_sentence_reason: 一句话说明 verdict。
```

## Result Stub

Copy this object into `results/CTX6.json` after review, replacing null values with the external reviewer verdict. Keep that per-context file in the results directory; `npm run assemble:fresh-reviewer-results` is the only supported way to create `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`.

```json
{
  "context_id": "CTX6",
  "priority": 11,
  "risk_tier": "LOW",
  "source_group": "TAM; UTAUT; Diffusion of Innovations",
  "claims": [
    "CL1",
    "CL2"
  ],
  "references": [
    "davis1989tam",
    "rogers2003diffusion",
    "venkatesh2003utaut"
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
