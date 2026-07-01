# Venous Thromboembolism Pulmonary Embolism Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/venous-thromboembolism-pulmonary-embolism-continuity` |
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

`venous-thromboembolism-pulmonary-embolism-continuity/` 研究深静脉血栓、肺栓塞、住院/术后/妊娠/癌症相关风险、诊断路径、抗凝系统和长期功能影响如何改变主体持续性。

> 核心问题：静脉血栓栓塞把血液凝固、移动、住院、手术、癌症和妊娠等条件连接成突发死亡风险。肺栓塞尤其会在短时间内改变氧合、右心负荷和死亡风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖血液在血管内保持可流动且不过度凝固
  -> 静脉血栓可脱落进入肺循环，造成氧合和右心急性失效
  -> 结果取决于风险识别、诊断路径、抗凝连续性和复发预防
  -> 因此 VTE/PE 是血液-循环-呼吸交界的急性死亡风险域
```

## 关注对象

- DVT、pulmonary embolism、hospital-acquired VTE、postoperative risk、cancer-associated thrombosis、pregnancy-associated thrombosis、anticoagulation continuity、post-PE syndrome。
- 与 `blood-oxygen-hemostasis/` 的边界：该域关注凝血/止血生理；本域关注 VTE/PE 事件链和系统连续性。
- 与 `transfusion-blood-management-hemorrhage-continuity/` 的关系：抗凝和出血风险构成双向治理边界。

## Human Infra 模型链路

```text
VTE/PE 预防识别系统 T
  -> 改变风险识别、诊断延迟、抗凝连续性、出血权衡和复发预防变量 X
  -> 改变肺循环负荷、氧合、右心功能、住院和长期运动能力 S
  -> 改变急性死亡、复发、慢性血栓栓塞和有效时间损失 λ(t)
  -> 影响主体存活、行动能力和长期选择权
```

## 非目标

- 不提供血栓诊断、D-dimer/影像解读、抗凝、溶栓、滤器、旅行、术后、妊娠或个体治疗建议。
- 不生成 VTE 风险评分、PE 分层、抗凝选择、出血权衡或停药建议。
- 不收集个案症状、影像、凝血结果、用药、肿瘤史、妊娠状态或住院资料。

## Source Signals

- ESC pulmonary embolism guideline materials: https://www.escardio.org/
- CDC blood clots / VTE materials: https://www.cdc.gov/blood-clots/
- NHLBI pulmonary embolism materials: https://www.nhlbi.nih.gov/health/pulmonary-embolism

## 下一步

- 建立 VTE/PE Continuity Card：risk context, diagnosis path, anticoagulation continuity, bleeding tradeoff, recurrence, long-term function。
- 与 `blood-oxygen-hemostasis/`、`transfusion-blood-management-hemorrhage-continuity/` 和 `pregnancy-parental-work-continuity/` 建立接口。
