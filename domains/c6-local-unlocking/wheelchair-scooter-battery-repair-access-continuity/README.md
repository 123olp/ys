# Wheelchair Scooter Battery Repair Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/wheelchair-scooter-battery-repair-access-continuity` |
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

`wheelchair-scooter-battery-repair-access-continuity` 研究手动轮椅、电动轮椅、代步车、电池/充电器、维修、备件、供应商响应、运输适配和备用行动方案如何影响移动、照护、医疗、工作、学校和撤离连续性。

> 核心问题：轮椅和代步车是行动能力的外部底盘；设备断电、损坏、维修等待或运输不兼容，会把身体功能限制放大成服务不可达和主体被困。

## 关注对象

- 手动轮椅、电动轮椅、代步车、坐垫、轮胎、刹车、控制器、电池、充电器和维修/替换等待。
- 家庭、街道、公共交通、paratransit、医疗预约、学校、工作场所和灾害撤离中的设备依赖。
- 供应商网络、备件、维修授权、运输装载、电梯/坡道接口和备用设备。
- 与 DME、无障碍建成环境、个人照护、应急准备和残障权利的接口。

## Human Infra 链路

```text
轮椅/代步设备运行连续
  -> 主体能把身体能力与外部移动底盘稳定耦合
  -> 断电、损坏、维修等待和运输断点减少
  -> 医疗、工作、教育、社区和撤离行动更可达
  -> 独立性、尊严、照护效率和未来选择权增强
```

## 非目标

- 不提供轮椅处方、坐姿评估、设备改装、维修步骤、品牌推荐、购买建议、保险申诉或个体 DME 覆盖判断。
- 不替代康复医生、物理/作业治疗师、DME 供应商、Medicare、Medicaid、交通机构或制造商说明。
- 不把设备运行问题简化为个人习惯问题；供应商、支付、环境和交通接口必须同时审查。

## Source Signals

- Medicare Wheelchairs and Scooters: https://www.medicare.gov/coverage/wheelchairs-scooters
- MedlinePlus Mobility Aids: https://medlineplus.gov/mobilityaids.html

## 下一步

- 建立 `device state -> power/repair/supplier dependency -> mobility task -> participation consequence` 变量表。
- 区分手动轮椅、电动轮椅、代步车、短期伤病、长期残障、老年照护和灾害撤离场景。
- 与 `durable-medical-equipment-supplier-repair-continuity`、`paratransit-nemt-access-continuity` 和 `built-environment-accessibility-universal-design` 建立边界。
