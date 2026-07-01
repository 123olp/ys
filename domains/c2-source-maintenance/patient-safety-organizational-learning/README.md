# Patient Safety Organizational Learning

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/patient-safety-organizational-learning` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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

- 界定生命载体变量：细胞、组织、器官、脑、免疫、代谢、急性风险或衰老损伤。
- 说明影响机制：修复、替换、再生、控制、筛查、预防、维持或风险降低。
- 列出可观察状态：功能指标、生物标志物、疾病终点、失能时间、恢复能力或死亡风险。
- 记录副作用、过度干预、癌变、免疫、长期安全性和尾部风险。
- 区分机制合理性、体外证据、动物证据、人体早期数据、临床终点和长期安全性。

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

`patient-safety-organizational-learning/` 研究患者安全、团队沟通、事件报告、根因分析、CUSP、TeamSTEPPS、高可靠组织和伤害预防。

> 核心问题：医疗和照护中的错误不能只归因于个人；组织是否能报告、学习、修复和重设流程，决定可避免伤害是否会持续截断主体。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要医疗、照护和组织系统支持
  -> 复杂组织会制造交接、沟通、疲劳、设备、流程和文化风险
  -> 事件学习和系统安全决定错误能否转化为改进，而不是重复伤害
```

## 关注对象

- 患者安全、医疗伤害、事件报告、团队沟通、交接、CUSP、TeamSTEPPS、RCA2、安全文化和高可靠组织。
- 医疗组织如何降低错误、疲劳、流程断裂、沟通失败、药物错误、感染和可避免伤害。
- 与 `risk-engineering/` 的关系：风险工程域关注通用风险；本域关注医疗与照护组织中的患者安全和学习机制。
- 与 `healthcare-access-continuity/`、`medicine-access-treatment-continuity/`、`occupational-work-design/` 和 `measurement-feedback/` 的接口。

## Human Infra 模型链路

```text
患者安全与组织学习基础设施
  -> 改变事件报告、团队沟通、根因分析、流程改进和安全文化
  -> 改变医疗照护系统中错误被发现、学习、纠正和防止复发的能力
  -> 降低可避免伤害、沟通失败、照护交接断裂和重复事故风险
  -> 增强医疗可信度、恢复机会、健康寿命和主体持续性
```

## 非目标

- 不提供医疗事故法律意见、索赔策略、个案责任判断、机构排名或临床处置建议。
- 不把安全文化测量写成惩罚员工、压制报告、甩锅患者或规避责任的工具。
- 不提供医疗流程操作、急救、药物、设备、感染控制或机构管理替代方案。

## Source Signals

- WHO Global Patient Safety Action Plan 2021-2030: https://www.who.int/publications/i/item/9789240032705
- AHRQ TeamSTEPPS: https://www.ahrq.gov/teamstepps-program/index.html
- AHRQ CUSP: https://www.ahrq.gov/hai/cusp/index.html
- AHRQ Surveys on Patient Safety Culture: https://www.ahrq.gov/sops/index.html
- IHI RCA2: https://www.ihi.org/resources/tools/rca2-improving-root-cause-analyses-and-actions-prevent-harm

## 下一步

- 建立患者安全变量表：事件报告、近失误、交接、沟通、团队训练、根因分析、行动闭环、安全文化和学习速度。
- 与 `risk-engineering/` 拆分通用风险工程和医疗组织学习边界。
- 整理 WHO Patient Safety、AHRQ TeamSTEPPS、CUSP、SOPS 和 IHI RCA2 的 Source Cards。
