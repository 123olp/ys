# ECMO Extracorporeal Life Support Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/ecmo-extracorporeal-life-support-continuity` |
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

`ecmo-extracorporeal-life-support-continuity/` 研究 ECMO/ECLS、体外循环支持、心肺桥接、中心容量、转运、并发症和退出策略如何把极端心肺衰竭转化为可等待恢复或移植的窗口。

> 核心问题：ECMO 是把主体从心肺功能临界失败中暂时外接出来的桥接技术。它的价值不在“神奇救命”，而在能否安全买到恢复、治疗或下一步决策的时间。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 心肺衰竭可能让主体在常规支持失败后终止
  -> ECMO 可临时替代部分心肺功能并争取恢复或转归窗口
  -> 但它依赖中心经验、抗凝、并发症控制、转运和退出条件
  -> 因此 ECMO 是极端器官支持和等待窗口工程的高风险域
```

## 关注对象

- VV/VA ECMO、ECLS center、indication governance、complication, anticoagulation risk, transport, bridge-to-recovery, bridge-to-transplant, withdrawal/exit。
- 与 `mechanical-ventilation-respiratory-failure-continuity/` 的关系：ECMO 可用于部分呼吸衰竭的升级支持。
- 与 `future-waiting/` 的概念关系：ECMO 是现实医学中的短期“等待恢复/治疗窗口”，但不是未来等待或永生方案。

## Human Infra 模型链路

```text
ECMO / ECLS T
  -> 改变心肺支持、氧合、灌注、抗凝、中心经验和退出变量 X
  -> 改变极端衰竭中的存活窗口、并发症和可恢复状态 S
  -> 改变死亡、出血、血栓、感染、神经损伤和长期失能风险 λ(t)
  -> 影响主体能否从极端器官失败中保留未来选择权
```

## 非目标

- 不提供 ECMO 适应证、禁忌证、抗凝、转运、设备、撤机、预后或个体医疗建议。
- 不生成中心选择、转院策略、家属决策、伦理判断或替代临床团队的内容。
- 不收集 ECMO 个案、参数、影像、血液数据、转运信息、费用或病历资料。

## Source Signals

- Extracorporeal Life Support Organization: https://www.elso.org/
- ELSO Guidelines: https://www.elso.org/ecmo-resources/elso-ecmo-guidelines.aspx
- NIH ECMO overview: https://www.nhlbi.nih.gov/health/ecmo

## 下一步

- 建立 ECLS Bridge Card：support mode, center capacity, complications, bridge target, exit path, neurological outcome。
- 与 `mechanical-ventilation-respiratory-failure-continuity/`、`intensive-care-organ-support-delirium-continuity/` 和 `transfusion-blood-management-hemorrhage-continuity/` 建立接口。
