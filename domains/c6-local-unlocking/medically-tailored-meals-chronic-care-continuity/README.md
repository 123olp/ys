# Medically Tailored Meals Chronic Care Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/medically-tailored-meals-chronic-care-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

该域研究 medically tailored meals（MTM）如何作为慢病照护、出院转接、营养风险管理和 Food is Medicine 项目中的执行接口。它关注的是“餐食是否能按医学需求、时间窗口、配送和照护计划稳定到达”，不是个体菜单设计。

## 核心问题

- 医学定制餐如何从临床判断、资格、支付、供应商、配送和 follow-up 中形成连续服务。
- MTM 对慢性病、术后恢复、出院后脆弱窗口、营养风险和医疗利用可能产生哪些影响。
- 哪些断点会使餐食无法到达、无法被食用、无法符合限制条件或无法进入照护反馈。
- 如何区分服务执行证据、健康结局证据、成本利用证据和商业宣传。

## 对象

- Medically tailored meals、home-delivered therapeutic meals、chronic care nutrition support。
- 出院转接、care plan、疾病状态、营养限制、文化适配、配送、冷链、复热和食用能力。
- Medicaid HRSN、payer coverage、CBO partnership、meal vendor、outcomes evaluation。

## Human Infra 价值

慢病和恢复期主体常常不是“知道该吃什么”失败，而是因为采购、烹饪、配送、费用、功能限制和病情限制无法稳定摄入合适食物。该域把医学营养从建议层推进到可交付、可追踪、可持续的基础设施层。

## 边界

- 只整理公开项目模式、变量、证据等级、执行风险和治理边界。
- 不提供个人疾病餐单、营养治疗、疾病管理、食材替代、配送商推荐、保险覆盖判断或医疗建议。
- 不声称 MTM 能替代药物、临床治疗、急救、营养师或医生判断。

## 上游与下游

- 上游：`nutrition-insecurity-screening-referral-continuity`、`care-transitions-discharge-continuity`、`multimorbidity-polypharmacy-care-coordination`、`health-insurance-enrollment-renewal-continuity`。
- 下游：`medical-nutrition-therapy-dietitian-access-continuity`、`home-delivered-meals-congregate-nutrition-services-continuity`、`diabetes-insulin-glucose-monitoring-supplies-continuity`。

## 初始资料线索

- HHS / ASPE Food is Medicine materials.
- NIH Food is Medicine research program.
- CMS Medicaid HRSN framework and state demonstrations.
- Peer-reviewed MTM outcomes and utilization studies.
