# Campus Mental Health Crisis Student Support Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/campus-mental-health-crisis-student-support-continuity` |
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

`campus-mental-health-crisis-student-support-continuity` 研究高校心理咨询、危机响应、988/社区转介、suicide prevention、leave of absence、return-to-campus、同伴支持和隐私同意如何影响学生安全、恢复和学业连续。

> 核心问题：高校阶段是身份、压力、孤独、经济负担和学习竞争叠加的阶段；心理支持若断裂，主体可能失去有效学习时间、校园关系、生命安全和返校路径。

## 关注对象

- Campus counseling、psychiatric referral、crisis response、after-hours support、988 linkage 和 community care transition。
- Suicide prevention、postvention、threat assessment boundary、leave/re-entry policy、case management、peer support 和 wellness programs。
- 隐私、FERPA/HIPAA 边界、同意、家属联系、强制休学风险、污名和歧视。
- 等候时间、服务容量、危机升级、急诊衔接、返校支持、课程压力和学生留存。

## Human Infra 链路

```text
校园心理健康与危机支持连续
  -> 情绪危机、孤立、压力负荷和自伤风险被及时接住
  -> 学习中断、急性风险、强制退出和返校失败下降
  -> 恢复时间、关系支持、学业参与和主体安全保持
  -> 主体长期学习能力、生命安全和未来选择权增强
```

## 非目标

- 不提供心理诊断、治疗、危机干预、用药、热线替代、风险评估、强制处置、申诉或个案建议。
- 不替代 988、emergency services、campus counseling、health services、community mental health、trusted professional 或法律援助。
- 不收集或处理心理健康记录、危机事件、诊断、用药、伤害风险、家属联系方式或校园事件资料。

## Source Signals

- SAMHSA 988 and behavioral health resources: https://www.samhsa.gov/
- U.S. Department of Education student mental health and well-being resources: https://www.ed.gov/
- CDC suicide prevention and youth/young adult mental health resources: https://www.cdc.gov/
- Institutional counseling, crisis response, leave and re-entry policy materials.

## 下一步

- 建立 `distress signal -> access delay -> crisis response -> leave/re-entry -> academic continuity` 变量表。
- 区分常规咨询、危机响应、社区转介、急诊衔接、同伴支持、休学返校和隐私/同意边界。
- 与 `mental-health-affective-stability`、`suicide-crisis-response-continuity`、`campus-basic-needs-student-support-continuity` 和本轮高教域建立边界。
