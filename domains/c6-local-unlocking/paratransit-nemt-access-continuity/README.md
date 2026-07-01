# Paratransit NEMT Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/paratransit-nemt-access-continuity` |
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

`paratransit-nemt-access-continuity` 研究 ADA paratransit、非紧急医疗交通 NEMT、预约、资格、等待、上门接送、陪同、报销和取消如何影响残障、慢病、老年和低收入主体能否到达医疗与基本服务。

> 核心问题：医疗和公共服务存在不等于人能到达；如果 paratransit 和 NEMT 断裂，可治疗、可复诊、可康复的问题会被交通失败转成健康损失。

## 关注对象

- ADA paratransit、NEMT、上门接送、轮椅车辆、陪同、预约窗口、等待时间、取消、no-show、报销和资格更新。
- 透析、癌症治疗、康复、产检、精神健康、药房、福利办公室和社区服务场景。
- 与医疗可及、残障独立生活、公共交通、照护、医保/Medicaid 和行政负担的接口。

## Human Infra 链路

```text
辅助交通与医疗交通连续
  -> 行动受限主体能到达医疗、康复、药品和公共服务
  -> 预约失败、延误治疗、照护负担和急诊替代风险下降
  -> 医学可及性从名义覆盖转化为真实到达
  -> 健康寿命、功能恢复和主体自主性增强
```

## 非目标

- 不提供资格规避、虚假医疗交通申请、报销欺诈、调度攻击、个案申诉策略或医疗建议。
- 不替代 Medicaid、FTA、交通运营商、医疗机构、照护协调员、保险、法律或本地服务渠道。
- 不收集病历、残障证明、医保号、预约记录、出行轨迹、接送地址或个人身份资料。

## Source Signals

- FTA ADA Paratransit: https://www.transit.dot.gov/regulations-and-guidance/civil-rights-ada/ada-regulations
- FTA ADA Circular: https://www.transit.dot.gov/regulations-and-guidance/fta-circulars/americans-disabilities-act-guidance
- Medicaid NEMT: https://www.medicaid.gov/medicaid/benefits/non-emergency-medical-transportation/index.html
- ADA.gov Transportation: https://www.ada.gov/topics/transportation/

## 下一步

- 建立 `eligibility -> trip request -> pickup/dropoff -> service reliability -> care outcome` 变量表。
- 区分 ADA paratransit、Medicaid NEMT、老年服务交通、社区志愿交通和医疗机构交通协调。
- 与 `healthcare-access-continuity`、`disability-services-independent-living`、`public-transit-service-operations-continuity` 和 `administrative-burden-procedural-friction` 建立边界。
