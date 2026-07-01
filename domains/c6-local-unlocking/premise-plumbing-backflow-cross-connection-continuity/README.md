# Premise Plumbing Backflow Cross Connection Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/premise-plumbing-backflow-cross-connection-continuity` |
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

`premise-plumbing-backflow-cross-connection-continuity` 研究建筑内部 plumbing、交叉连接、回流防护、压力变化、检测维护和污染逆流如何影响饮水、医疗设备、食品服务和公共卫生信任。

> 核心问题：供水安全不止发生在水厂和管网；建筑内部连接错误、回流防护失效和压力事件也可能把污染物带入本应安全的使用点。

## 关注对象

- Premise plumbing、cross-connection、backflow、backpressure、backsiphonage、回流防护装置、测试维护和记录。
- 住宅、多户建筑、学校、医疗机构、食品服务、灌溉、锅炉、实验室和工业用户接口。
- 水压变化、施工改造、设备连接、责任主体、检测周期、通知和污染事件复盘。
- 与公共饮水、建筑维护、食品安全、医疗感染控制和消费者信任的接口。

## Human Infra 链路

```text
回流与交叉连接防护连续
  -> 建筑内部污染逆流路径更可见并可阻断
  -> 饮水、食品、医疗和清洁任务的使用点安全更可靠
  -> 暴露事件、通知延迟和责任不清风险下降
  -> 健康安全、服务信任和日常执行稳定性增强
```

## 非目标

- 不提供管道施工、回流装置安装、检测步骤、维修教程、建筑合规判断、事故处置或个案责任建议。
- 不替代 EPA、地方水务、plumbing code、持证 plumber、建筑管理、公共卫生或监管检查。
- 不把回流防护写成通用 DIY 维修；本域只处理风险链、责任边界和执行连续性。

## Source Signals

- EPA Cross-Connection Control and Backflow Prevention issue paper: https://www.epa.gov/sites/default/files/2015-09/documents/2007_05_18_disinfection_tcr_issuepaper_tcr_crossconnection-backflow.pdf

## 下一步

- 建立 `plumbing connection -> pressure/backflow condition -> contaminant path -> task exposure -> continuity outcome` 变量表。
- 区分住宅、多户建筑、学校、医疗、食品服务和灌溉/锅炉接口场景。
- 与 `water-wastewater-utility-service-continuity`、`household-maintenance-repair-contractor-continuity` 和 `clinical-engineering-medical-device-maintenance` 建立边界。
