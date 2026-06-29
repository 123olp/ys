# Fresh Reviewer Citation Audit Protocol

Date: 2026-06-29T00:00:00.000Z
Output JSON: `web/src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json`

## Summary

Verdict: `READY_FOR_FRESH_REVIEWER`

Reason: `external_sentence_level_review_protocol_exported`

The citation-context queue, reviewer independence contract, pass gate, and per-context prompts are ready for an external fresh reviewer. This artifact does not replace the reviewer run.

This protocol does not clear the citation-audit warning. It turns the remaining independent sentence-level citation-context review into an executable queue.

| Metric | Count |
| --- | ---: |
| Contexts in queue | 12 |
| High or blocker contexts | 1 |
| Medium contexts | 7 |
| Low contexts | 4 |

## Reviewer Independence Contract

- Use a fresh reviewer thread or a reviewer with no prior exposure to this paper's local conclusions.
- Re-open source pages or PDFs; do not rely on memory or the local review artifacts as proof.
- Check existence, metadata, and exact claim-to-source fit.
- Treat wrong-context support as more serious than metadata drift.
- Keep source-boundary language: a method source cannot become evidence for effective immortality.

## Pass Gate

- Every row in the queue must receive a reviewer verdict.
- No row may remain `WRONG`, `PRESENT`, `REMOVE`, or `REPLACE_SOURCE` before formal submission.
- Every `WEAK` or `POSSIBLE` row must trigger a prose downgrade, boundary strengthening, or citation replacement.
- High-risk contexts must be resolved before medium and low contexts are treated as clean.
- The final audit trace must record reviewer identity class, source URLs, verdicts, and required text changes.

## Review Queue

| Priority | Context | Risk tier | Score | Source group | Claims | Required action |
| ---: | --- | --- | ---: | --- | --- | --- |
| 1 | CTX2 | HIGH | 6 | Grossman Health Capital; WHO HALE; NICE QALY | CL1, CL2 | Resolve before any submission-facing claim can be treated as clean. |
| 2 | CTX3 | MEDIUM | 4 | Hallmarks of Aging; GrimAge; Cognitive Reserve | CL7 | Review after high-risk contexts; keep registered boundary language. |
| 3 | CTX5 | MEDIUM | 4 | Human Capital; Social Capital; Social Relationships Mortality | CL1, CL2, CL5 | Review after high-risk contexts; keep registered boundary language. |
| 4 | CTX7 | MEDIUM | 4 | Generative AI at Work; Noy and Zhang; GitHub Copilot; Jagged Technological Frontier | CL1, CL2, CL4, CL7 | Review after high-risk contexts; keep registered boundary language. |
| 5 | CTX10 | MEDIUM | 4 | Apple Heart Study; Personal Informatics; Lived Informatics; Dynamic Digital Twin | CL6 | Review after high-risk contexts; keep registered boundary language. |
| 6 | CTX11 | MEDIUM | 4 | Extended Mind; Engelbart; Cognition in the Wild | CL6 | Review after high-risk contexts; keep registered boundary language. |
| 7 | CTX12 | MEDIUM | 4 | Capability Approach; WHO SDOH; WHO Primary Health Care | CL1, CL2, CL5 | Review after high-risk contexts; keep registered boundary language. |
| 8 | CTX9 | MEDIUM | 3 | Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI | CL3, CL6, CL7 | Review after high-risk contexts; keep registered boundary language. |
| 9 | CTX1 | LOW | 2 | Kaplan-Meier 1958; Cox 1972 | CL2, CL3, CL7 | Review after high-risk contexts; keep registered boundary language. |
| 10 | CTX4 | LOW | 2 | Deliberate Practice; Law of Practice; Self-Regulated Learning; Feedback Intervention Theory | CL1, CL2 | Review after high-risk contexts; keep registered boundary language. |
| 11 | CTX6 | LOW | 2 | TAM; UTAUT; Diffusion of Innovations | CL1, CL2 | Review after high-risk contexts; keep registered boundary language. |
| 12 | CTX8 | LOW | 2 | NIST AI RMF; Guidelines for Human-AI Interaction; NASA-TLX; Automation taxonomy | CL2, CL4, CL6, CL7 | Review after high-risk contexts; keep registered boundary language. |

## Context Protocol

### 1. CTX2: Grossman Health Capital; WHO HALE; NICE QALY

- Risk tier: HIGH
- Risk score: 6
- Claims: CL1, CL2
- Used for: 把日历寿命转译为健康质量、有效时间和质量调整时间。
- Safe use: T -> E 的测量语言和健康质量调整视角。
- Forbidden use: 不能完整定义主体连续性，也不能替代个体医学判断。
- Local review verdict: KEEP_WITH_STRICT_BOUNDARY
- Required action before submission: Resolve before any submission-facing claim can be treated as clean.

Reviewer questions:
  - 优先检查是否把测量语言、规范语言或任务内效果外推成主体持续性、寿命或未来选择权结论。
  - 拒绝从方法、关联或指标语言直接跳到具体延寿效果。
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
  - 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
  - 该来源是否支持 safe use 中登记的最小用途？
  - 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
  - 如果只支持部分用途，需要把哪一句改成更弱表述？
  - 高风险检查：是否把指标、机制、治理、任务内效果或预测语言外推为永生、寿命收益或飞轮成立的实证证据？

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `grossman1972healthcapital` | crossref-verified | PASS | 把健康资本、有效时间和日历时间区分开。 |
| `niceEconomicEvaluation` | official-url-200 | PASS | 提供 QALY 与健康经济评价的政策语言。 |
| `whohale7752` | official-url-200 | PASS | 提供健康寿命指标的官方定义入口。 |

Suggested fresh-reviewer prompt:

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

### 2. CTX3: Hallmarks of Aging; GrimAge; Cognitive Reserve

- Risk tier: MEDIUM
- Risk score: 4
- Claims: CL7
- Used for: 提出身体状态、衰老机制、生物年龄信号和认知储备候选变量。
- Safe use: 状态变量和风险信号的机制/关联入口。
- Forbidden use: 不能把机制综述、预测关联或认知储备直接写成干预效果。
- Local review verdict: KEEP_WITH_BOUNDARY
- Required action before submission: Review after high-risk contexts; keep registered boundary language.

Reviewer questions:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
  - 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
  - 该来源是否支持 safe use 中登记的最小用途？
  - 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
  - 如果只支持部分用途，需要把哪一句改成更弱表述？

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `lopezotin2013hallmarks` | crossref-verified | PASS | 提出衰老状态变量和机制入口。 |
| `lu2019grimage` | crossref-verified | PASS | 作为生物年龄、死亡风险和健康寿命信号入口。 |
| `stern2012cognitiveReserve` | crossref-verified | PASS | 说明认知储备作为状态变量和风险信号的边界。 |

Suggested fresh-reviewer prompt:

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

### 3. CTX5: Human Capital; Social Capital; Social Relationships Mortality

- Risk tier: MEDIUM
- Risk score: 4
- Claims: CL1, CL2, CL5
- Used for: 说明经验、资源、信誉和协作网络如何进入 C 与 O，并可能反哺 T/E。
- Safe use: 积累资本、社会支持和死亡风险关联的讨论。
- Forbidden use: 不能把社会关系关联直接升级成具体干预的因果延寿结论。
- Local review verdict: KEEP_WITH_BOUNDARY
- Required action before submission: Review after high-risk contexts; keep registered boundary language.

Reviewer questions:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
  - 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
  - 该来源是否支持 safe use 中登记的最小用途？
  - 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
  - 如果只支持部分用途，需要把哪一句改成更弱表述？

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `coleman1988socialCapital` | doi-verified | PASS | 说明关系、信任、规范和网络如何成为能力形成条件。 |
| `holtlunstad2010social` | crossref-verified | PASS | 讨论社会关系与死亡风险的关联证据边界。 |
| `mincer1974humanCapital` | official-archive | PASS | 说明教育、经验和长期积累如何进入人力资本模型。 |

Suggested fresh-reviewer prompt:

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

### 4. CTX7: Generative AI at Work; Noy and Zhang; GitHub Copilot; Jagged Technological Frontier

- Risk tier: MEDIUM
- Risk score: 4
- Claims: CL1, CL2, CL4, CL7
- Used for: 支持 A -> Q 在限定任务中的生产率、速度、质量或任务边界证据。
- Safe use: 生成式 AI 在客服、写作、编程或知识工作实验中的任务内效果与异质性。
- Forbidden use: 不能泛化为通用智能增强、健康寿命延长或永生收益。
- Local review verdict: KEEP_WITH_BOUNDARY
- Required action before submission: Review after high-risk contexts; keep registered boundary language.

Reviewer questions:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
  - 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
  - 该来源是否支持 safe use 中登记的最小用途？
  - 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
  - 如果只支持部分用途，需要把哪一句改成更弱表述？

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `brynjolfsson2025generative` | crossref-verified-corrected-doi | PASS | 支持限定客服任务中的 AI productivity 证据。 |
| `dellacqua2026jagged` | crossref-verified | PASS | 支持 AI 收益与风险具有任务边界。 |
| `noy2023productivity` | crossref-verified | PASS | 支持写作任务内的生成式 AI 生产率证据。 |
| `peng2023copilot` | arxiv-api-verified | PASS | 支持限定编程任务中的 AI pair programmer 生产率入口。 |

Suggested fresh-reviewer prompt:

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

### 5. CTX10: Apple Heart Study; Personal Informatics; Lived Informatics; Dynamic Digital Twin

- Risk tier: MEDIUM
- Risk score: 4
- Claims: CL6
- Used for: 说明观测、反馈、个人数据系统和生命过程建模如何进入状态观测层。
- Safe use: observation -> action 的路径和自我追踪/数字孪生的系统问题。
- Forbidden use: 早筛、追踪或数字孪生概念不等于死亡风险下降或医疗结局改善。
- Local review verdict: KEEP_WITH_BOUNDARY
- Required action before submission: Review after high-risk contexts; keep registered boundary language.

Reviewer questions:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
  - 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
  - 该来源是否支持 safe use 中登记的最小用途？
  - 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
  - 如果只支持部分用途，需要把哪一句改成更弱表述？

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `epstein2015lived` | crossref-verified | PASS | 说明长期自我追踪系统的生活嵌入、维护负担和断裂点。 |
| `li2010personalInformatics` | crossref-verified | PASS | 提供个人信息学的准备、收集、整合、反思和行动阶段。 |
| `mulder2022dynamicDigitalTwin` | publisher-verified | PASS | 说明生命过程中的状态观测、预测、预防和数字孪生建模入口。 |
| `perez2019appleHeart` | crossref-verified | PASS | 说明可穿戴设备进入大规模风险提示和临床确认通道。 |

Suggested fresh-reviewer prompt:

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

### 6. CTX11: Extended Mind; Engelbart; Cognition in the Wild

- Risk tier: MEDIUM
- Risk score: 4
- Claims: CL6
- Used for: 支撑工具、记忆外化、分布式认知和认知增强进入主体系统的理论位置。
- Safe use: 主体能力可以由人、工具、表征、环境和协作流程共同支撑。
- Forbidden use: 哲学和系统框架不提供数值效应估计，也不能证明数字副本等同于本人。
- Local review verdict: KEEP_WITH_BOUNDARY
- Required action before submission: Review after high-risk contexts; keep registered boundary language.

Reviewer questions:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
  - 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
  - 该来源是否支持 safe use 中登记的最小用途？
  - 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
  - 如果只支持部分用途，需要把哪一句改成更弱表述？

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `burwell2017bciEthics` | doi-verified | PASS | 为脑机接口、神经技术、同意、身份和主体边界提供风险治理入口。 |
| `clark1998extended` | crossref-verified | PASS | 支撑工具、记忆外化和认知扩展进入主体系统。 |
| `engelbart1962augmenting` | official-archive-registered | PASS | 提供人、工具、概念和方法作为增强系统的经典框架。 |
| `hutchins1995cognition` | author-page-verified | PASS | 提供分布式认知和环境嵌入式问题求解框架。 |

Suggested fresh-reviewer prompt:

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

### 7. CTX12: Capability Approach; WHO SDOH; WHO Primary Health Care

- Risk tier: MEDIUM
- Risk score: 4
- Claims: CL1, CL2, CL5
- Used for: 定义 O 可能性空间为真实可进入路径，并把资源、制度、医疗和社会条件纳入反哺路径。
- Safe use: 真实选择权、健康决定因素、医疗可及和连续照护的规范/公共卫生框架。
- Forbidden use: 规范框架不提供寿命预测，也不能替代具体政策或医疗干预评估。
- Local review verdict: KEEP_WITH_BOUNDARY
- Required action before submission: Review after high-risk contexts; keep registered boundary language.

Reviewer questions:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
  - 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
  - 该来源是否支持 safe use 中登记的最小用途？
  - 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
  - 如果只支持部分用途，需要把哪一句改成更弱表述？

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `robeyns2021capability` | official-web-registered | PASS | 定义真实可行能力和可能性空间。 |
| `whoSdhPhc` | official-urls-200 | PASS | 把健康和持续性放回收入、教育、住房、工作、环境和医疗可及条件中。 |

Suggested fresh-reviewer prompt:

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

### 8. CTX9: Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI

- Risk tier: MEDIUM
- Risk score: 3
- Claims: CL3, CL6, CL7
- Used for: 定义 U_t -> causal claim 的因果门禁和预测模型报告门禁。
- Safe use: population、intervention、comparator、time zero、outcome、estimand、试验登记、AI 干预报告、验证、校准和偏倚审查。
- Forbidden use: 不能消除所有不可测混杂，也不证明任何注册试验或预测模型有效。
- Local review verdict: KEEP_WITH_BOUNDARY
- Required action before submission: Review after high-risk contexts; keep registered boundary language.

Reviewer questions:
  - 拒绝从任务内 AI 效果直接跳到通用能力增强、健康寿命收益或永生收益。
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
  - 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
  - 该来源是否支持 safe use 中登记的最小用途？
  - 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
  - 如果只支持部分用途，需要把哪一句改成更弱表述？

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `clinicaltrialsGov` | official-url-200 | PASS | 提供临床试验登记、人群、比较组、结局和结果回填入口。 |
| `clinicaltrialsGovApi` | official-url-200 | PASS | 提供结构化试验注册与结果数据的机器读取入口，用于后续试验证据采集和协议字段回填。 |
| `consortAi2020` | doi-verified | PASS | 约束 AI 干预临床试验结果报告中的干预说明、输入输出、人机交互和错误案例分析。 |
| `gradeHandbook` | official-web | PASS | 提供证据确定性、收益风险权衡和从证据到建议的政策语言。 |
| `hernan2022targetTrial` | crossref-verified | PASS | 定义因果协议门禁和观察数据因果推断边界。 |
| `probastAi2025` | doi-and-official-site-verified | PASS | 提供 AI 预测模型研究的偏倚风险、适用性、可信度、公平性和质量审查门禁。 |
| `robins2000marginalStructural` | pubmed-verified | PASS | 说明时间变化混杂下的因果估计入口和边界。 |
| `spiritAi2020` | doi-verified | PASS | 约束 AI 干预临床试验方案中的协议透明度、输入输出、人机交互和错误分析计划。 |
| `tripodAi2024` | doi-and-official-site-verified | PASS | 提供 AI/机器学习临床预测模型的报告清单、外部验证、校准和透明度门禁。 |
| `tripodProbast` | official-urls-200 | PASS | 约束预测模型报告质量、偏倚风险、校准和外部验证。 |
| `whoIctrp` | official-url-200 | PASS | 提供国际临床试验注册网络、WHO 数据集和试验透明度原则的上位入口。 |

Suggested fresh-reviewer prompt:

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

### 9. CTX1: Kaplan-Meier 1958; Cox 1972

- Risk tier: LOW
- Risk score: 2
- Claims: CL2, CL3, CL7
- Used for: 定义 T、生存函数 S(t)、删失数据和风险函数 lambda(t) 的统计语言。
- Safe use: 事件时间、删失、生存曲线和协变量风险建模的基础方法。
- Forbidden use: 不证明任何具体延寿、健康、AI 或资源干预有效。
- Local review verdict: KEEP_AS_METHOD_OR_FRAME_LANGUAGE
- Required action before submission: Review after high-risk contexts; keep registered boundary language.

Reviewer questions:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
  - 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
  - 该来源是否支持 safe use 中登记的最小用途？
  - 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
  - 如果只支持部分用途，需要把哪一句改成更弱表述？

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `cox1972regression` | crossref-verified | PASS | 定义协变量、风险函数和 lambda(t) 的统计语言。 |
| `kaplan1958incomplete` | crossref-verified | PASS | 定义生存曲线、删失数据和 T 的统计语言。 |

Suggested fresh-reviewer prompt:

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

### 10. CTX4: Deliberate Practice; Law of Practice; Self-Regulated Learning; Feedback Intervention Theory

- Risk tier: LOW
- Risk score: 2
- Claims: CL1, CL2
- Used for: 解释 E -> R -> C：有效时间如何在有目标、有反馈和可修正的任务中沉淀为能力。
- Safe use: 学习轮次、反馈质量、练习曲线和能力积累的条件。
- Forbidden use: 时间本身不会自动产生能力；错误反馈和低质量重复可能反向损害表现。
- Local review verdict: KEEP_WITH_BOUNDARY
- Required action before submission: Review after high-risk contexts; keep registered boundary language.

Reviewer questions:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
  - 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
  - 该来源是否支持 safe use 中登记的最小用途？
  - 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
  - 如果只支持部分用途，需要把哪一句改成更弱表述？

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `ericsson1993deliberatePractice` | crossref-verified | PASS | 解释有效时间进入有反馈练习轮次的条件。 |
| `kluger1996feedback` | crossref-verified | PASS | 说明反馈可能提升表现，也可能因设计错误降低表现。 |
| `newell1981lawPractice` | crossref-verified-corrected-doi | PASS | 为重复轮次、练习曲线和能力增长提供认知模型入口。 |
| `zimmerman2002selfRegulated` | doi-verified | PASS | 说明学习轮次需要目标设定、自我监控、反馈和策略调整。 |

Suggested fresh-reviewer prompt:

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

### 11. CTX6: TAM; UTAUT; Diffusion of Innovations

- Risk tier: LOW
- Risk score: 2
- Claims: CL1, CL2
- Used for: 解释 C -> A：技术采用受有用性、易用性、促进条件、资源和社会影响约束。
- Safe use: 技术采用能力的分解：access、understanding、evaluation、trial、integration。
- Forbidden use: 不能证明采用后的技术一定有效，也不能覆盖所有高风险医学或神经技术。
- Local review verdict: KEEP_WITH_BOUNDARY
- Required action before submission: Review after high-risk contexts; keep registered boundary language.

Reviewer questions:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
  - 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
  - 该来源是否支持 safe use 中登记的最小用途？
  - 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
  - 如果只支持部分用途，需要把哪一句改成更弱表述？

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `davis1989tam` | crossref-verified | PASS | 解释技术采用能力中的有用性和易用性。 |
| `rogers2003diffusion` | bibliographic-record-verified-isbn | PASS | 说明技术成熟、扩散、采用者差异和社会系统时间窗口。 |
| `venkatesh2003utaut` | crossref-verified | PASS | 解释技术采用中的促进条件、社会影响和努力预期。 |

Suggested fresh-reviewer prompt:

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

### 12. CTX8: NIST AI RMF; Guidelines for Human-AI Interaction; NASA-TLX; Automation taxonomy

- Risk tier: LOW
- Risk score: 2
- Claims: CL2, CL4, CL6, CL7
- Used for: 给 A/Q -> risk、QA 成本、任务负荷、自动化等级和人机控制权提供治理语言。
- Safe use: 风险识别、测量、纠错、回滚和人机协作设计边界。
- Forbidden use: 治理框架和交互指南不提供收益估计，也不证明 AI 能延寿。
- Local review verdict: KEEP_AS_METHOD_OR_FRAME_LANGUAGE
- Required action before submission: Review after high-risk contexts; keep registered boundary language.

Reviewer questions:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
  - 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
  - 该来源是否支持 safe use 中登记的最小用途？
  - 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
  - 如果只支持部分用途，需要把哪一句改成更弱表述？

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `amershi2019hai` | crossref-verified | PASS | 提供人机协作设计、纠错和控制权边界。 |
| `burwell2017bciEthics` | doi-verified | PASS | 为脑机接口、神经技术、同意、身份和主体边界提供风险治理入口。 |
| `dellacqua2026jagged` | crossref-verified | PASS | 支持 AI 收益与风险具有任务边界。 |
| `nasaTlx` | official-web-registered | PASS | 提供任务负荷、时间压力、努力和挫败感测量入口。 |
| `nist2023airmf` | official-url-200 | PASS | 提供 AI 风险识别、测量、治理和回滚语言。 |
| `parasuraman2000automation` | crossref-verified | PASS | 拆分自动化类型、等级和人机控制权。 |

Suggested fresh-reviewer prompt:

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

