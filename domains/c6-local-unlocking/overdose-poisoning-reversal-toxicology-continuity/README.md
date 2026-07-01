# Overdose Poisoning Reversal Toxicology Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/overdose-poisoning-reversal-toxicology-continuity` |
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

`overdose-poisoning-reversal-toxicology-continuity/` 研究药物过量、中毒、毒物中心、解毒/逆转窗口、呼吸抑制、监测转运和恢复服务如何降低可逆毒性暴露导致的死亡。

> 核心问题：许多中毒和过量事件具有可逆窗口。主体持续性需要把毒性暴露从“无人识别的死亡”转化为可咨询、可逆转、可转运、可恢复的系统事件。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体可能被药物、化学品、酒精、阿片类或混合暴露急性终止
  -> 生存依赖早识别、毒物咨询、逆转窗口、呼吸支持、转运和后续恢复
  -> 如果没有可达毒理响应，许多可逆暴露会变成死亡或脑损伤
  -> 因此过量/中毒逆转是可逆外源性死亡风险的急性救援域
```

## 关注对象

- Poison control、overdose surveillance、naloxone access、respiratory depression、toxic exposure, antidote availability, ED transfer, linkage to treatment。
- 与 `chemical-safety-poison-control-toxicology/` 的边界：化学安全域关注毒理和风险沟通整体；本域聚焦急性中毒/过量逆转和救援窗口。
- 与 `substance-use-treatment-recovery-continuity/` 的关系：过量逆转后需要恢复和长期治疗入口。

## Human Infra 模型链路

```text
过量/中毒逆转基础设施 T
  -> 改变暴露识别、毒物咨询、逆转药可得、呼吸支持和转运变量 X
  -> 改变呼吸抑制、毒性负荷、脑缺氧、急诊转归和恢复连接状态 S
  -> 改变中毒死亡、缺氧脑损伤、复发过量和长期失能风险 λ(t)
  -> 影响主体存活、恢复入口和自主性保护
```

## 非目标

- 不提供中毒处理、剂量、解毒药、纳洛酮操作、物质使用、急救、药物相互作用或个体医疗建议。
- 不生成过量规避、药物滥用、毒物制备、检测规避、执法规避或自伤方法。
- 不收集物质使用史、用药、定位、身份、病历、急救记录或敏感法律资料。

## Source Signals

- Poison Help: https://www.poisonhelp.org/
- CDC Drug Overdose: https://www.cdc.gov/overdose-prevention/
- NIH Naloxone DrugFacts: https://nida.nih.gov/publications/drugfacts/naloxone

## 下一步

- 建立 Toxic Exposure Rescue Card：exposure type, recognition, poison center, reversal window, respiratory support, ED transfer, recovery linkage。
- 与 `chemical-safety-poison-control-toxicology/`、`substance-use-treatment-recovery-continuity/` 和 `emergency-medical-services-prehospital-care/` 建立接口。
