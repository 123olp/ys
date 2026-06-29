# Fresh Reviewer Citation Context Handoff

Generated at: 2026-06-29T00:00:00.000Z

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`

This handoff is the standalone external-review package for the effective immortality flywheel paper. It is a queue, contract, and evidence map for an independent citation-context reviewer. It is not reviewer evidence by itself.

## Independence Contract

- Fresh thread or independent reviewer required.
- Web or primary-source lookup required for every reviewed context.
- Local review artifacts are allowed only as a queue and boundary map, not as evidence of support.
- Every context verdict must include source URL or retrieval note.

Additional boundary: do not trust local review artifacts as evidence. Local ledgers identify what to check; only reopened sources, PDFs, DOI pages, official pages, or explicit retrieval notes can support reviewer verdicts.

## Required Workflow

1. Open HANDOFF.md in a fresh reviewer context.
2. Review contexts in priority order and reopen every listed source, DOI page, official page, PDF, or retrieval note.
3. Judge reference existence, safe-use support, forbidden-use boundary, required action, and resolution status.
4. Write one completed result file per context under fresh-reviewer-context-packets/results/CTX*.json.
5. Run the assembler and audit commands; do not hand-edit the canonical results ledger.

## Required Output Files

The reviewer must return one JSON file per citation context:

| Priority | Context | Risk | Score | Source group | Required result file |
| ---: | --- | --- | ---: | --- | --- |
| 1 | CTX2 | HIGH | 6 | Grossman Health Capital; WHO HALE; NICE QALY | `results/CTX2.json` |
| 2 | CTX3 | MEDIUM | 4 | Hallmarks of Aging; GrimAge; Cognitive Reserve | `results/CTX3.json` |
| 3 | CTX5 | MEDIUM | 4 | Human Capital; Social Capital; Social Relationships Mortality | `results/CTX5.json` |
| 4 | CTX7 | MEDIUM | 4 | Generative AI at Work; Noy and Zhang; GitHub Copilot; Jagged Technological Frontier | `results/CTX7.json` |
| 5 | CTX10 | MEDIUM | 4 | Apple Heart Study; Personal Informatics; Lived Informatics; Dynamic Digital Twin | `results/CTX10.json` |
| 6 | CTX11 | MEDIUM | 4 | Extended Mind; Engelbart; Cognition in the Wild | `results/CTX11.json` |
| 7 | CTX12 | MEDIUM | 4 | Capability Approach; WHO SDOH; WHO Primary Health Care | `results/CTX12.json` |
| 8 | CTX9 | MEDIUM | 3 | Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI | `results/CTX9.json` |
| 9 | CTX1 | LOW | 2 | Kaplan-Meier 1958; Cox 1972 | `results/CTX1.json` |
| 10 | CTX4 | LOW | 2 | Deliberate Practice; Law of Practice; Self-Regulated Learning; Feedback Intervention Theory | `results/CTX4.json` |
| 11 | CTX6 | LOW | 2 | TAM; UTAUT; Diffusion of Innovations | `results/CTX6.json` |
| 12 | CTX8 | LOW | 2 | NIST AI RMF; Guidelines for Human-AI Interaction; NASA-TLX; Automation taxonomy | `results/CTX8.json` |

After all result files exist, run:

```bash
cd web
npm run assemble:fresh-reviewer-results
npm run audit:fresh-reviewer-results
```

The canonical `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json` is accepted only when it is assembled from these per-context files and records matching SHA-256 hashes.

Schema file: `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/RESULT_SCHEMA.json`

Schema hash: `sha256:2efec5cdc63f32e4cd9bdbd1d423ef71d2e95b83302cc48020fb5069e7fece9d`

## Verdict Schema

| Field | Allowed values |
| --- | --- |
| reference_existence | PASS, FAIL, UNCERTAIN |
| safe_use_support | SUPPORTS, WEAK, WRONG |
| forbidden_use_violation | NONE, POSSIBLE, PRESENT |
| required_action | KEEP, SOFTEN, REWRITE, REMOVE, REPLACE_SOURCE |
| resolution_status | RESOLVED, ACCEPTED_WITH_BOUNDARY, PENDING_FIX, UNRESOLVED |

## Return Checklist

- Every CTX*.json contains reviewer_identity_class, reviewed_at, source_urls, reviewer_reason, manuscript_change_required, manuscript_change_summary, and reviewer_trace_path.
- Every source_urls array points to reviewer-opened sources or explicit retrieval notes.
- No result uses local author claims as evidence.
- Any SOFTEN, REWRITE, REMOVE, REPLACE_SOURCE, WEAK, WRONG, POSSIBLE, or PRESENT verdict is either resolved in manuscript text or remains blocking.
- Canonical results are produced only by npm run assemble:fresh-reviewer-results.

## Blocking Conditions

- Any FAIL or UNCERTAIN reference existence verdict without manual resolution.
- Any WRONG safe-use support verdict.
- Any PRESENT forbidden-use violation.
- Any required_action of REMOVE or REPLACE_SOURCE unresolved in manuscript text.

## Source Trace

| File | SHA-256 |
| --- | --- |
| `src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json` | `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/INDEX.json` | `sha256:f0c58a433af078dde82e9aeb4cdc019838d6b76d50a4336905efa3436aab7d7d` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/INDEX.md` | `sha256:9f501d4a91f5691765d0c439e771cbb7e1c8c86f88fa7e6e3c4a4cb302d7d53e` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX2.json` | `sha256:977041b50b7312614032958ddc5d16110ab8d7a548613c39335c1070c616ee09` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX2.md` | `sha256:46477f71e520e51270656d1bf50b7cd7d73dc70ece2365cf3406cb8c8aec936d` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX3.json` | `sha256:dafb1837adca7696d724c0b78fca1b182117b89707ed6dceeba485bbaea8b86d` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX3.md` | `sha256:819324cf29e116b00254b5b8541d4b291f88210b24abc426802e1bef20ecc0e8` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX5.json` | `sha256:bc72d7180728b65f0024327d8a6569cd58e0af890ad6423a58e16f2f31db8a12` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX5.md` | `sha256:0ecad79432476cd626c0a5fc3d6c7a0b91f02916cb6c810bbb590d6ce56dccf3` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX7.json` | `sha256:bdf6f6033b2012d38509dba96e287343c3041454f93f036ef572c999a992de0c` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX7.md` | `sha256:b86d88927f022afefceefe1b760be5dca7dd0457e3c718b05917db7b0fd0a6f8` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX10.json` | `sha256:d741a4f388ef8c6b1a0d72d38a945ebc8400f1b69d7fa9158dca038bd527c048` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX10.md` | `sha256:2da6d41d9cfdd385ed7573a3ab8c6f80bf474d6ff5b199d795ec956f4f1641b7` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX11.json` | `sha256:7b1a59a1929259fed90f980e65851ff76479e1f0635a108c97aa43844d0e3cc0` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX11.md` | `sha256:10c62ba18e1b22f77a6de4df090b8157fbc7604dd4922c4c82441e4c6fe486c0` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX12.json` | `sha256:0ff42f44f41ef57fc5326f6eb722fc0dcafa821190915d5e1fda16cfac8f0465` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX12.md` | `sha256:d0b3a4b9bcbe6d5a8e0f542af6fbeb90cd69db6fb9e081e35cf5db1cc82433a5` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX9.json` | `sha256:87949f98b4f0948bc0e3f8438f2578541bf9fd2281a38bf4d40817e1e213bc33` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX9.md` | `sha256:0ac3f28511844cf3ca5f622539321c0fd50e50a00202e14aa565398401d46211` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX1.json` | `sha256:36cb34c19c7d6a4e9ac904ff07470e7315338486204841ddd7302440dfc429f8` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX1.md` | `sha256:b09a583462214b48d9439a9c3fe87efa2b6c8032fe03b699aef8316162cd36dd` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX4.json` | `sha256:1605bc58a237fb1088dccf8ef8ee80f79efd2c1b028fa512c191116bd22b0739` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX4.md` | `sha256:fef69ae6031846e7fa931a4f5784c04689496dc6667e41e4d50a8f2a8b97b060` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX6.json` | `sha256:cde0eb81fc5ead3e9180393ba1e7f3f54ce2e4cceacf27e2ecca272ed98cb359` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX6.md` | `sha256:64d6cad519f8939e49e5c89ee5166a2165bf9cc5f78ab200b3ae3360889afecf` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX8.json` | `sha256:fb0d5f8b043304076d89108f6be9105b3936fb78f2a4ad6f54ef74027e661b0e` |
| `src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/CTX8.md` | `sha256:d77105a1e215086d639be7c9363ef2bf12b85aa2fe71b61f0b09ff89a5ce32b0` |

## Packet Contents

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


---

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


---

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


---

# Fresh Reviewer Context Packet: CTX7

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`
Packet hash: `sha256:228a264f327d03c91936ddd37efde486ea264a1e579b48ca784f804bce1f74aa`

## Review Boundary

This packet is for an external fresh reviewer. Do not treat local review verdicts as proof. Re-open the listed sources or PDFs, then judge whether the sources support the registered safe use and whether the manuscript violates the forbidden-use boundary.

## Context

| Field | Value |
| --- | --- |
| Priority | 4 |
| Context | CTX7 |
| Risk tier | MEDIUM |
| Risk score | 4 |
| Source group | Generative AI at Work; Noy and Zhang; GitHub Copilot; Jagged Technological Frontier |
| Claims | CL1, CL2, CL4, CL7 |
| Used for | 支持 A -> Q 在限定任务中的生产率、速度、质量或任务边界证据。 |
| Safe use | 生成式 AI 在客服、写作、编程或知识工作实验中的任务内效果与异质性。 |
| Forbidden use | 不能泛化为通用智能增强、健康寿命延长或永生收益。 |
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
| `brynjolfsson2025generative` | Generative AI at Work | crossref-verified-corrected-doi | PASS | 支持限定客服任务中的 AI productivity 证据。 |
| `dellacqua2026jagged` | Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality | crossref-verified | PASS | 支持 AI 收益与风险具有任务边界。 |
| `noy2023productivity` | Experimental evidence on the productivity effects of generative artificial intelligence | crossref-verified | PASS | 支持写作任务内的生成式 AI 生产率证据。 |
| `peng2023copilot` | The Impact of AI on Developer Productivity: Evidence from GitHub Copilot | arxiv-api-verified | PASS | 支持限定编程任务中的 AI pair programmer 生产率入口。 |

## Prompt

```text
你是独立引用语境审稿人。不要使用项目作者的本地结论作为证据，必须重新打开来源并检查正文语境。

Context: CTX7
Source group: Generative AI at Work; Noy and Zhang; GitHub Copilot; Jagged Technological Frontier
Risk: MEDIUM / score 4
Claims: CL1, CL2, CL4, CL7
Used for: 支持 A -> Q 在限定任务中的生产率、速度、质量或任务边界证据。
Safe use: 生成式 AI 在客服、写作、编程或知识工作实验中的任务内效果与异质性。
Forbidden use: 不能泛化为通用智能增强、健康寿命延长或永生收益。

References:
- brynjolfsson2025generative: Generative AI at Work (crossref-verified-corrected-doi; PASS)
- dellacqua2026jagged: Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality (crossref-verified; PASS)
- noy2023productivity: Experimental evidence on the productivity effects of generative artificial intelligence (crossref-verified; PASS)
- peng2023copilot: The Impact of AI on Developer Productivity: Evidence from GitHub Copilot (arxiv-api-verified; PASS)

请逐项输出：
1. reference_existence: PASS / FAIL / UNCERTAIN，并给出核验 URL。
2. safe_use_support: SUPPORTS / WEAK / WRONG，并说明来源文本如何支持或不支持。
3. forbidden_use_violation: NONE / POSSIBLE / PRESENT。
4. required_action: KEEP / SOFTEN / REWRITE / REMOVE / REPLACE_SOURCE。
5. one_sentence_reason: 一句话说明 verdict。
```

## Result Stub

Copy this object into `results/CTX7.json` after review, replacing null values with the external reviewer verdict. Keep that per-context file in the results directory; `npm run assemble:fresh-reviewer-results` is the only supported way to create `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`.

```json
{
  "context_id": "CTX7",
  "priority": 4,
  "risk_tier": "MEDIUM",
  "source_group": "Generative AI at Work; Noy and Zhang; GitHub Copilot; Jagged Technological Frontier",
  "claims": [
    "CL1",
    "CL2",
    "CL4",
    "CL7"
  ],
  "references": [
    "brynjolfsson2025generative",
    "dellacqua2026jagged",
    "noy2023productivity",
    "peng2023copilot"
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


---

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


---

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


---

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


---

# Fresh Reviewer Context Packet: CTX9

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`
Packet hash: `sha256:070e6f9334225a7de3cd2284e170dd09b0641da3a82b9563cabf13f580e082b5`

## Review Boundary

This packet is for an external fresh reviewer. Do not treat local review verdicts as proof. Re-open the listed sources or PDFs, then judge whether the sources support the registered safe use and whether the manuscript violates the forbidden-use boundary.

## Context

| Field | Value |
| --- | --- |
| Priority | 8 |
| Context | CTX9 |
| Risk tier | MEDIUM |
| Risk score | 3 |
| Source group | Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI |
| Claims | CL3, CL6, CL7 |
| Used for | 定义 U_t -> causal claim 的因果门禁和预测模型报告门禁。 |
| Safe use | population、intervention、comparator、time zero、outcome、estimand、试验登记、AI 干预报告、验证、校准和偏倚审查。 |
| Forbidden use | 不能消除所有不可测混杂，也不证明任何注册试验或预测模型有效。 |
| Local verdict | KEEP_WITH_BOUNDARY |
| Required action before submission | Review after high-risk contexts; keep registered boundary language. |

## Reviewer Questions

- 拒绝从任务内 AI 效果直接跳到通用能力增强、健康寿命收益或永生收益。
- 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
- 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
- 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
- 该来源是否支持 safe use 中登记的最小用途？
- 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
- 如果只支持部分用途，需要把哪一句改成更弱表述？

## References

| Reference | Title | Audit status | Live status | Registered use |
| --- | --- | --- | --- | --- |
| `clinicaltrialsGov` | ClinicalTrials.gov | official-url-200 | PASS | 提供临床试验登记、人群、比较组、结局和结果回填入口。 |
| `clinicaltrialsGovApi` | ClinicalTrials.gov Data API | official-url-200 | PASS | 提供结构化试验注册与结果数据的机器读取入口，用于后续试验证据采集和协议字段回填。 |
| `consortAi2020` | Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension | doi-verified | PASS | 约束 AI 干预临床试验结果报告中的干预说明、输入输出、人机交互和错误案例分析。 |
| `gradeHandbook` | GRADE Handbook | official-web | PASS | 提供证据确定性、收益风险权衡和从证据到建议的政策语言。 |
| `hernan2022targetTrial` | Target Trial Emulation | crossref-verified | PASS | 定义因果协议门禁和观察数据因果推断边界。 |
| `probastAi2025` | PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods | doi-and-official-site-verified | PASS | 提供 AI 预测模型研究的偏倚风险、适用性、可信度、公平性和质量审查门禁。 |
| `robins2000marginalStructural` | Marginal Structural Models and Causal Inference in Epidemiology | pubmed-verified | PASS | 说明时间变化混杂下的因果估计入口和边界。 |
| `spiritAi2020` | Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension | doi-verified | PASS | 约束 AI 干预临床试验方案中的协议透明度、输入输出、人机交互和错误分析计划。 |
| `tripodAi2024` | TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods | doi-and-official-site-verified | PASS | 提供 AI/机器学习临床预测模型的报告清单、外部验证、校准和透明度门禁。 |
| `tripodProbast` | TRIPOD Statement and PROBAST | official-urls-200 | PASS | 约束预测模型报告质量、偏倚风险、校准和外部验证。 |
| `whoIctrp` | International Clinical Trials Registry Platform (ICTRP) | official-url-200 | PASS | 提供国际临床试验注册网络、WHO 数据集和试验透明度原则的上位入口。 |

## Prompt

```text
你是独立引用语境审稿人。不要使用项目作者的本地结论作为证据，必须重新打开来源并检查正文语境。

Context: CTX9
Source group: Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI
Risk: MEDIUM / score 3
Claims: CL3, CL6, CL7
Used for: 定义 U_t -> causal claim 的因果门禁和预测模型报告门禁。
Safe use: population、intervention、comparator、time zero、outcome、estimand、试验登记、AI 干预报告、验证、校准和偏倚审查。
Forbidden use: 不能消除所有不可测混杂，也不证明任何注册试验或预测模型有效。

References:
- clinicaltrialsGov: ClinicalTrials.gov (official-url-200; PASS)
- clinicaltrialsGovApi: ClinicalTrials.gov Data API (official-url-200; PASS)
- consortAi2020: Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension (doi-verified; PASS)
- gradeHandbook: GRADE Handbook (official-web; PASS)
- hernan2022targetTrial: Target Trial Emulation (crossref-verified; PASS)
- probastAi2025: PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods (doi-and-official-site-verified; PASS)
- robins2000marginalStructural: Marginal Structural Models and Causal Inference in Epidemiology (pubmed-verified; PASS)
- spiritAi2020: Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension (doi-verified; PASS)
- tripodAi2024: TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods (doi-and-official-site-verified; PASS)
- tripodProbast: TRIPOD Statement and PROBAST (official-urls-200; PASS)
- whoIctrp: International Clinical Trials Registry Platform (ICTRP) (official-url-200; PASS)

请逐项输出：
1. reference_existence: PASS / FAIL / UNCERTAIN，并给出核验 URL。
2. safe_use_support: SUPPORTS / WEAK / WRONG，并说明来源文本如何支持或不支持。
3. forbidden_use_violation: NONE / POSSIBLE / PRESENT。
4. required_action: KEEP / SOFTEN / REWRITE / REMOVE / REPLACE_SOURCE。
5. one_sentence_reason: 一句话说明 verdict。
```

## Result Stub

Copy this object into `results/CTX9.json` after review, replacing null values with the external reviewer verdict. Keep that per-context file in the results directory; `npm run assemble:fresh-reviewer-results` is the only supported way to create `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`.

```json
{
  "context_id": "CTX9",
  "priority": 8,
  "risk_tier": "MEDIUM",
  "source_group": "Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI",
  "claims": [
    "CL3",
    "CL6",
    "CL7"
  ],
  "references": [
    "clinicaltrialsGov",
    "clinicaltrialsGovApi",
    "consortAi2020",
    "gradeHandbook",
    "hernan2022targetTrial",
    "probastAi2025",
    "robins2000marginalStructural",
    "spiritAi2020",
    "tripodAi2024",
    "tripodProbast",
    "whoIctrp"
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


---

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


---

# Fresh Reviewer Context Packet: CTX4

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`
Packet hash: `sha256:8316c4ef281a7ad4a59f7d3d76549c58b74b1a56724a2a7c12e2592a00b192e2`

## Review Boundary

This packet is for an external fresh reviewer. Do not treat local review verdicts as proof. Re-open the listed sources or PDFs, then judge whether the sources support the registered safe use and whether the manuscript violates the forbidden-use boundary.

## Context

| Field | Value |
| --- | --- |
| Priority | 10 |
| Context | CTX4 |
| Risk tier | LOW |
| Risk score | 2 |
| Source group | Deliberate Practice; Law of Practice; Self-Regulated Learning; Feedback Intervention Theory |
| Claims | CL1, CL2 |
| Used for | 解释 E -> R -> C：有效时间如何在有目标、有反馈和可修正的任务中沉淀为能力。 |
| Safe use | 学习轮次、反馈质量、练习曲线和能力积累的条件。 |
| Forbidden use | 时间本身不会自动产生能力；错误反馈和低质量重复可能反向损害表现。 |
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
| `ericsson1993deliberatePractice` | The role of deliberate practice in the acquisition of expert performance | crossref-verified | PASS | 解释有效时间进入有反馈练习轮次的条件。 |
| `kluger1996feedback` | The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory | crossref-verified | PASS | 说明反馈可能提升表现，也可能因设计错误降低表现。 |
| `newell1981lawPractice` | Mechanisms of Skill Acquisition and the Law of Practice: Allen Newell and Paul S. Rosenbloom | crossref-verified-corrected-doi | PASS | 为重复轮次、练习曲线和能力增长提供认知模型入口。 |
| `zimmerman2002selfRegulated` | Becoming a Self-Regulated Learner: An Overview | doi-verified | PASS | 说明学习轮次需要目标设定、自我监控、反馈和策略调整。 |

## Prompt

```text
你是独立引用语境审稿人。不要使用项目作者的本地结论作为证据，必须重新打开来源并检查正文语境。

Context: CTX4
Source group: Deliberate Practice; Law of Practice; Self-Regulated Learning; Feedback Intervention Theory
Risk: LOW / score 2
Claims: CL1, CL2
Used for: 解释 E -> R -> C：有效时间如何在有目标、有反馈和可修正的任务中沉淀为能力。
Safe use: 学习轮次、反馈质量、练习曲线和能力积累的条件。
Forbidden use: 时间本身不会自动产生能力；错误反馈和低质量重复可能反向损害表现。

References:
- ericsson1993deliberatePractice: The role of deliberate practice in the acquisition of expert performance (crossref-verified; PASS)
- kluger1996feedback: The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory (crossref-verified; PASS)
- newell1981lawPractice: Mechanisms of Skill Acquisition and the Law of Practice: Allen Newell and Paul S. Rosenbloom (crossref-verified-corrected-doi; PASS)
- zimmerman2002selfRegulated: Becoming a Self-Regulated Learner: An Overview (doi-verified; PASS)

请逐项输出：
1. reference_existence: PASS / FAIL / UNCERTAIN，并给出核验 URL。
2. safe_use_support: SUPPORTS / WEAK / WRONG，并说明来源文本如何支持或不支持。
3. forbidden_use_violation: NONE / POSSIBLE / PRESENT。
4. required_action: KEEP / SOFTEN / REWRITE / REMOVE / REPLACE_SOURCE。
5. one_sentence_reason: 一句话说明 verdict。
```

## Result Stub

Copy this object into `results/CTX4.json` after review, replacing null values with the external reviewer verdict. Keep that per-context file in the results directory; `npm run assemble:fresh-reviewer-results` is the only supported way to create `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`.

```json
{
  "context_id": "CTX4",
  "priority": 10,
  "risk_tier": "LOW",
  "source_group": "Deliberate Practice; Law of Practice; Self-Regulated Learning; Feedback Intervention Theory",
  "claims": [
    "CL1",
    "CL2"
  ],
  "references": [
    "ericsson1993deliberatePractice",
    "kluger1996feedback",
    "newell1981lawPractice",
    "zimmerman2002selfRegulated"
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


---

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


---

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

