# Osteoarthritis Joint Function Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/osteoarthritis-joint-function-continuity` |
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

`osteoarthritis-joint-function-continuity/` 研究骨关节炎、关节疼痛、移动能力、体重与负荷、保守治疗、关节置换路径和长期参与如何影响主体持续性。

> 核心问题：骨关节炎把慢性关节退变转化为移动半径、工作能力、照护负担和独立生活能力的长期压缩。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要稳定步行、站立、抓握和日常活动能力
  -> 骨关节炎会通过疼痛、僵硬和活动受限降低行动密度
  -> 结果取决于体重负荷、运动支持、疼痛管理、辅助技术和手术/康复路径
  -> 因此骨关节炎是移动寿命、独立生活和长期参与的关键维护域
```

## 关注对象

- Osteoarthritis、joint pain、stiffness、mobility limitation、exercise access、weight/load factors、assistive devices、joint replacement pathway、rehabilitation。
- 与 `musculoskeletal-integrity/` 的边界：该域关注肌骨完整性总机制；本域聚焦退行性关节病对移动和独立生活的影响。
- 与 `assistive-technology-access/` 的关系：辅助器具、环境改造和康复服务会改变关节病程对主体行动的实际损耗。

## Human Infra 模型链路

```text
骨关节炎关节功能维护系统 T
  -> 改变疼痛、僵硬、移动能力、体重负荷、辅助器具、康复和手术路径变量 X
  -> 改变步行半径、跌倒风险、工作参与、照护需求和生活自理状态 S
  -> 改变失能时间、有效时间损耗、独立生活概率和未来选择权 λ(t)
  -> 影响主体长期行动能力、恢复成本和资源消耗
```

## 非目标

- 不提供个人关节炎诊断、影像判读、运动处方、止痛药、注射、补充剂、手术、假体、康复或体重建议。
- 不生成个人治疗计划、设备购买、手术时机、残障、保险或工伤判断。
- 不收集个案疼痛、影像、药物、活动追踪、体重或手术资料。

## Source Signals

- NIAMS osteoarthritis: https://www.niams.nih.gov/health-topics/osteoarthritis
- CDC arthritis information: https://www.cdc.gov/arthritis/
- WHO musculoskeletal conditions: https://www.who.int/news-room/fact-sheets/detail/musculoskeletal-conditions

## 下一步

- 建立 Joint Function Card：joint site, pain interference, mobility limitation, assistive technology, rehabilitation access, surgery pathway。
- 与 `musculoskeletal-integrity/`、`assistive-technology-access/` 和 `fall-risk-prevention-home-safety-continuity/` 建立接口。
