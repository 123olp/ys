# Citation Context Risk Triage

Date: 2026-06-29T00:00:00.000Z
Input: `web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_REVIEW_PACKET.json`
Output JSON: `web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_RISK_TRIAGE.json`

## Summary

Verdict: `REQUIRES_FRESH_REVIEW`

Reason: `local_triage_ready_external_review_required`

Citation contexts have been ranked for local overclaim and boundary risk so a fresh reviewer can prioritize exact source-to-claim verification.

This is a local structural risk triage. It does not replace fresh reviewer sentence-level citation-context judgment.

| Tier | Count |
| --- | ---: |
| BLOCKER | 0 |
| HIGH | 1 |
| MEDIUM | 7 |
| LOW | 4 |

## Context Triage

| Context | Tier | Score | Claims | References | Required action |
| --- | --- | ---: | --- | ---: | --- |
| CTX1 | LOW | 2 | CL2, CL3, CL7 | 2 | Fresh reviewer can sample after higher-risk contexts are resolved. |
| CTX2 | HIGH | 6 | CL1, CL2 | 3 | Fresh reviewer must inspect exact source-to-claim support and boundary wording. |
| CTX3 | MEDIUM | 4 | CL7 | 3 | Fresh reviewer should confirm the context is scoped and not overgeneralized. |
| CTX4 | LOW | 2 | CL1, CL2 | 4 | Fresh reviewer can sample after higher-risk contexts are resolved. |
| CTX5 | MEDIUM | 4 | CL1, CL2, CL5 | 3 | Fresh reviewer should confirm the context is scoped and not overgeneralized. |
| CTX6 | LOW | 2 | CL1, CL2 | 3 | Fresh reviewer can sample after higher-risk contexts are resolved. |
| CTX7 | MEDIUM | 4 | CL1, CL2, CL4, CL7 | 4 | Fresh reviewer should confirm the context is scoped and not overgeneralized. |
| CTX8 | LOW | 2 | CL2, CL4, CL6, CL7 | 6 | Fresh reviewer can sample after higher-risk contexts are resolved. |
| CTX9 | MEDIUM | 3 | CL3, CL6, CL7 | 11 | Fresh reviewer should confirm the context is scoped and not overgeneralized. |
| CTX10 | MEDIUM | 4 | CL6 | 4 | Fresh reviewer should confirm the context is scoped and not overgeneralized. |
| CTX11 | MEDIUM | 4 | CL6 | 4 | Fresh reviewer should confirm the context is scoped and not overgeneralized. |
| CTX12 | MEDIUM | 4 | CL1, CL2, CL5 | 2 | Fresh reviewer should confirm the context is scoped and not overgeneralized. |

## Claim Triage

| Claim | Tier | Type | Contexts | Required action |
| --- | --- | --- | --- | --- |
| CL1 | HIGH | Conceptual framing | CTX2, CTX4, CTX5, CTX6, CTX7, CTX12 | Fresh reviewer should inspect high-priority contexts first: CTX2. |
| CL2 | HIGH | Model interface | CTX1, CTX2, CTX4, CTX5, CTX6, CTX7, CTX8, CTX12 | Fresh reviewer should inspect high-priority contexts first: CTX2. |
| CL3 | MEDIUM | Method claim | CTX1, CTX9 | No high-priority local risk context; keep standard fresh-review coverage. |
| CL4 | MEDIUM | Task-limited empirical claim | CTX7, CTX8 | No high-priority local risk context; keep standard fresh-review coverage. |
| CL5 | MEDIUM | Normative and measurement claim | CTX5, CTX12 | No high-priority local risk context; keep standard fresh-review coverage. |
| CL6 | MEDIUM | Governance claim | CTX8, CTX9, CTX10, CTX11 | No high-priority local risk context; keep standard fresh-review coverage. |
| CL7 | MEDIUM | Prohibited claim boundary | CTX1, CTX3, CTX7, CTX8, CTX9 | No high-priority local risk context; keep standard fresh-review coverage. |

## Detailed Reviewer Queue

### CTX1: Kaplan-Meier 1958; Cox 1972

- Risk tier: LOW
- Risk score: 2
- Claims: CL2, CL3, CL7
- References: cox1972regression, kaplan1958incomplete
- Risk factors: explicit does-not-support boundary
- Safe use: 事件时间、删失、生存曲线和协变量风险建模的基础方法。
- Forbidden use: 不证明任何具体延寿、健康、AI 或资源干预有效。
- Required action: Fresh reviewer can sample after higher-risk contexts are resolved.
- Reviewer focus:
  - Check whether the does-not-support boundary is preserved in prose and figure captions.
  - Check whether the source supports only the local usedFor statement, not the broader Human Infra theory.

### CTX2: Grossman Health Capital; WHO HALE; NICE QALY

- Risk tier: HIGH
- Risk score: 6
- Claims: CL1, CL2
- References: grossman1972healthcapital, niceEconomicEvaluation, whohale7752
- Risk factors: boundary-sensitive citation context; explicit does-not-support boundary; life-extension or mortality-adjacent use
- Safe use: T -> E 的测量语言和健康质量调整视角。
- Forbidden use: 不能完整定义主体连续性，也不能替代个体医学判断。
- Required action: Fresh reviewer must inspect exact source-to-claim support and boundary wording.
- Reviewer focus:
  - Check whether the does-not-support boundary is preserved in prose and figure captions.
  - Check whether the source supports only the local usedFor statement, not the broader Human Infra theory.
  - Reject any upgrade from method, association, or framework language to concrete lifespan-extension evidence.

### CTX3: Hallmarks of Aging; GrimAge; Cognitive Reserve

- Risk tier: MEDIUM
- Risk score: 4
- Claims: CL7
- References: lopezotin2013hallmarks, lu2019grimage, stern2012cognitiveReserve
- Risk factors: boundary-sensitive citation context; explicit does-not-support boundary
- Safe use: 状态变量和风险信号的机制/关联入口。
- Forbidden use: 不能把机制综述、预测关联或认知储备直接写成干预效果。
- Required action: Fresh reviewer should confirm the context is scoped and not overgeneralized.
- Reviewer focus:
  - Check whether the does-not-support boundary is preserved in prose and figure captions.
  - Check whether the source supports only the local usedFor statement, not the broader Human Infra theory.

### CTX4: Deliberate Practice; Law of Practice; Self-Regulated Learning; Feedback Intervention Theory

- Risk tier: LOW
- Risk score: 2
- Claims: CL1, CL2
- References: ericsson1993deliberatePractice, kluger1996feedback, newell1981lawPractice, zimmerman2002selfRegulated
- Risk factors: boundary-sensitive citation context
- Safe use: 学习轮次、反馈质量、练习曲线和能力积累的条件。
- Forbidden use: 时间本身不会自动产生能力；错误反馈和低质量重复可能反向损害表现。
- Required action: Fresh reviewer can sample after higher-risk contexts are resolved.
- Reviewer focus:
  - Check whether the does-not-support boundary is preserved in prose and figure captions.
  - Check whether the source supports only the local usedFor statement, not the broader Human Infra theory.

### CTX5: Human Capital; Social Capital; Social Relationships Mortality

- Risk tier: MEDIUM
- Risk score: 4
- Claims: CL1, CL2, CL5
- References: coleman1988socialCapital, holtlunstad2010social, mincer1974humanCapital
- Risk factors: boundary-sensitive citation context; explicit does-not-support boundary
- Safe use: 积累资本、社会支持和死亡风险关联的讨论。
- Forbidden use: 不能把社会关系关联直接升级成具体干预的因果延寿结论。
- Required action: Fresh reviewer should confirm the context is scoped and not overgeneralized.
- Reviewer focus:
  - Check whether the does-not-support boundary is preserved in prose and figure captions.
  - Check whether the source supports only the local usedFor statement, not the broader Human Infra theory.

### CTX6: TAM; UTAUT; Diffusion of Innovations

- Risk tier: LOW
- Risk score: 2
- Claims: CL1, CL2
- References: davis1989tam, rogers2003diffusion, venkatesh2003utaut
- Risk factors: boundary-sensitive citation context
- Safe use: 技术采用能力的分解：access、understanding、evaluation、trial、integration。
- Forbidden use: 不能证明采用后的技术一定有效，也不能覆盖所有高风险医学或神经技术。
- Required action: Fresh reviewer can sample after higher-risk contexts are resolved.
- Reviewer focus:
  - Check whether the does-not-support boundary is preserved in prose and figure captions.
  - Check whether the source supports only the local usedFor statement, not the broader Human Infra theory.

### CTX7: Generative AI at Work; Noy and Zhang; GitHub Copilot; Jagged Technological Frontier

- Risk tier: MEDIUM
- Risk score: 4
- Claims: CL1, CL2, CL4, CL7
- References: brynjolfsson2025generative, dellacqua2026jagged, noy2023productivity, peng2023copilot
- Risk factors: boundary-sensitive citation context; explicit does-not-support boundary
- Safe use: 生成式 AI 在客服、写作、编程或知识工作实验中的任务内效果与异质性。
- Forbidden use: 不能泛化为通用智能增强、健康寿命延长或永生收益。
- Required action: Fresh reviewer should confirm the context is scoped and not overgeneralized.
- Reviewer focus:
  - Check whether the does-not-support boundary is preserved in prose and figure captions.
  - Check whether the source supports only the local usedFor statement, not the broader Human Infra theory.

### CTX8: NIST AI RMF; Guidelines for Human-AI Interaction; NASA-TLX; Automation taxonomy

- Risk tier: LOW
- Risk score: 2
- Claims: CL2, CL4, CL6, CL7
- References: amershi2019hai, burwell2017bciEthics, dellacqua2026jagged, nasaTlx, nist2023airmf, parasuraman2000automation
- Risk factors: explicit does-not-support boundary
- Safe use: 风险识别、测量、纠错、回滚和人机协作设计边界。
- Forbidden use: 治理框架和交互指南不提供收益估计，也不证明 AI 能延寿。
- Required action: Fresh reviewer can sample after higher-risk contexts are resolved.
- Reviewer focus:
  - Check whether the does-not-support boundary is preserved in prose and figure captions.
  - Check whether the source supports only the local usedFor statement, not the broader Human Infra theory.

### CTX9: Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI

- Risk tier: MEDIUM
- Risk score: 3
- Claims: CL3, CL6, CL7
- References: clinicaltrialsGov, clinicaltrialsGovApi, consortAi2020, gradeHandbook, hernan2022targetTrial, probastAi2025, robins2000marginalStructural, spiritAi2020, tripodAi2024, tripodProbast, whoIctrp
- Risk factors: explicit does-not-support boundary; AI or prediction transfer risk
- Safe use: population、intervention、comparator、time zero、outcome、estimand、试验登记、AI 干预报告、验证、校准和偏倚审查。
- Forbidden use: 不能消除所有不可测混杂，也不证明任何注册试验或预测模型有效。
- Required action: Fresh reviewer should confirm the context is scoped and not overgeneralized.
- Reviewer focus:
  - Check whether the does-not-support boundary is preserved in prose and figure captions.
  - Check whether the source supports only the local usedFor statement, not the broader Human Infra theory.
  - Reject any upgrade from task-limited AI evidence to general intelligence, healthspan, or immortality benefit.

### CTX10: Apple Heart Study; Personal Informatics; Lived Informatics; Dynamic Digital Twin

- Risk tier: MEDIUM
- Risk score: 4
- Claims: CL6
- References: epstein2015lived, li2010personalInformatics, mulder2022dynamicDigitalTwin, perez2019appleHeart
- Risk factors: boundary-sensitive citation context; explicit does-not-support boundary
- Safe use: observation -> action 的路径和自我追踪/数字孪生的系统问题。
- Forbidden use: 早筛、追踪或数字孪生概念不等于死亡风险下降或医疗结局改善。
- Required action: Fresh reviewer should confirm the context is scoped and not overgeneralized.
- Reviewer focus:
  - Check whether the does-not-support boundary is preserved in prose and figure captions.
  - Check whether the source supports only the local usedFor statement, not the broader Human Infra theory.

### CTX11: Extended Mind; Engelbart; Cognition in the Wild

- Risk tier: MEDIUM
- Risk score: 4
- Claims: CL6
- References: burwell2017bciEthics, clark1998extended, engelbart1962augmenting, hutchins1995cognition
- Risk factors: boundary-sensitive citation context; explicit does-not-support boundary
- Safe use: 主体能力可以由人、工具、表征、环境和协作流程共同支撑。
- Forbidden use: 哲学和系统框架不提供数值效应估计，也不能证明数字副本等同于本人。
- Required action: Fresh reviewer should confirm the context is scoped and not overgeneralized.
- Reviewer focus:
  - Check whether the does-not-support boundary is preserved in prose and figure captions.
  - Check whether the source supports only the local usedFor statement, not the broader Human Infra theory.

### CTX12: Capability Approach; WHO SDOH; WHO Primary Health Care

- Risk tier: MEDIUM
- Risk score: 4
- Claims: CL1, CL2, CL5
- References: robeyns2021capability, whoSdhPhc
- Risk factors: boundary-sensitive citation context; explicit does-not-support boundary
- Safe use: 真实选择权、健康决定因素、医疗可及和连续照护的规范/公共卫生框架。
- Forbidden use: 规范框架不提供寿命预测，也不能替代具体政策或医疗干预评估。
- Required action: Fresh reviewer should confirm the context is scoped and not overgeneralized.
- Reviewer focus:
  - Check whether the does-not-support boundary is preserved in prose and figure captions.
  - Check whether the source supports only the local usedFor statement, not the broader Human Infra theory.


## Scope

This triage ranks citation contexts by local overclaim risk, boundary sensitivity, reference verification WARN/FAIL state, and claim type. It does not read full source text and must not be cited as evidence that a reference supports a claim.
