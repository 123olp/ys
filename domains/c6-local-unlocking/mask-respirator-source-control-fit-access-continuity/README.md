# Mask Respirator Source Control Fit Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/mask-respirator-source-control-fit-access-continuity` |
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

`mask-respirator-source-control-fit-access-continuity/` 研究口罩、呼吸防护、源头控制、适配、可得性和使用治理如何降低暴发期间的空气传播风险。

> 核心问题：呼吸防护不是单个用品选择；它是公共空间能否继续学习、工作、照护和服务的低摩擦风险控制层。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 暴发期间呼吸暴露会压缩公共空间行动能力
  -> 口罩、呼吸防护和源头控制改变单位接触风险
  -> 防护可得性和适配决定主体能否在必要场景中继续行动
```

## 关注对象

- 口罩、呼吸器、源头控制、适配、可得性、工作场所呼吸防护、学校/公共场所政策和风险沟通。
- 与 `air-quality-ventilation-exposure-control/` 的关系：空气质量域关注空间暴露环境；本域关注个人/人群层的呼吸源头控制与防护接口。

## Human Infra 模型链路

```text
口罩与呼吸防护可达性
  -> 改变空气传播暴露、源头控制、工作学校开放风险和高风险主体保护
  -> 改变感染概率、停工停课概率和公共空间信任
  -> 降低暴发期间行动中断和医疗系统负担
  -> 增强有效行动、关系参与和主体持续性
```

## 非目标

- 不提供个人产品推荐、佩戴教程、fit testing 指令、职业合规、医疗建议或法律建议。
- 不提供防护规避、假冒认证、PPE 抢占、场所对抗或风险补偿策略。
- 不替代 OSHA/NIOSH、雇主 respiratory protection program 或医疗判断。

## Source Signals

- CDC masks and respirators: https://www.cdc.gov/respiratory-viruses/prevention/masks.html
- CDC NIOSH respirators: https://www.cdc.gov/niosh/npptl/topics/respirators/
- OSHA respiratory protection: https://www.osha.gov/respiratory-protection
- WHO mask guidance portal: https://www.who.int/

## 下一步

- 建立变量表：源头控制、过滤效率、适配、可得性、成本、接受度、工作场所要求、高风险主体保护和沟通误差。
- 与 `indoor-ventilation-filtration-outbreak-control-continuity/`、`occupational-exposure-industrial-hygiene/` 和 `school-workplace-outbreak-operations-continuity/` 建立接口。
