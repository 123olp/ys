# Substance Use Treatment Recovery Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/substance-use-treatment-recovery-continuity` |
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

物质使用障碍治疗与恢复连续性域研究：当成瘾、过量风险、复发、污名、刑事化和治疗断点影响主体持续性时，治疗入口、恢复支持、减害、同伴支持和长期照护如何把风险重新接回恢复路径。

## 对象

- 物质使用障碍、成瘾治疗、恢复支持、FindTreatment.gov、同伴支持、恢复社区和长期随访。
- 过量预防、减害框架、污名、服务可及、保险覆盖、羁押释放、无家可归和农村服务断点。
- 治疗保留、复发风险、家庭关系、就业、住房、心理健康、慢病和公共卫生接口。
- 物质使用障碍对死亡风险、认知控制、资源消耗、关系网络、有效时间和未来选择权的影响。

## Human Infra 价值

`substance-exposure-control/` 关注暴露和风险，本域关注已经形成障碍后的治疗、恢复和社会重新连接。成瘾不是单一意志问题，而是一个需要服务入口、持续照护、关系支持和反污名机制共同承接的长期恢复系统。

```text
治疗和恢复支持不断线
  -> 过量、复发、污名、住房断裂和刑事化风险下降
  -> 主体恢复健康、关系、工作和自我控制窗口
  -> 有效时间、行动能力和未来选择权提高
```

## 边界

本域只整理公开物质使用障碍治疗、恢复支持、过量预防、减害治理和服务连续性资料。

不提供：

- 个体诊断、戒断、排毒、药物、剂量、替代治疗、复发处理或医疗建议。
- 非法物质获取、制造、配方、剂量、混用、规避检测、运输、销售或危险使用指南。
- 过量现场处置、急救步骤、法律策略、执法规避、保险/福利个案或机构选择建议。
- 把成瘾、复发或过量风险写成道德失败、治安标签、商业营销或剥削性定位。

## 上游与下游

- 上游：`substance-exposure-control/`、`mental-health-affective-stability/`、`medicine-access-treatment-continuity/`、`community-health-workers-peer-support/`。
- 下游：`homelessness-unsheltered-health-continuity/`、`correctional-health-reentry-continuity/`、`workforce-employment-services/`、`social-connection-relational-infra/`。

## 初始资料线索

- SAMHSA FindTreatment.gov and treatment resources。
- CDC overdose prevention resources。
- NIDA substance use and addiction resources。
- Public materials on peer support, recovery support and harm reduction governance。
