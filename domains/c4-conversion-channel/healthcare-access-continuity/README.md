# Healthcare Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/healthcare-access-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 主要把科学、医疗、数据、制度或技术从潜在能力转成真实可用路径。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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


`healthcare-access-continuity/` 研究医疗服务能否持续、可及、可负担、可信地接住主体，把可修复问题转化为真实恢复机会。

> 核心问题：主体出现疾病、损伤、衰弱或风险信号时，是否能够及时进入连续医疗系统，而不是因为距离、费用、质量、断点或制度摩擦被排除。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 身体和功能风险必须被发现、解释、转诊、治疗和随访
  -> 医疗服务必须可及、连续、可负担、可信且质量可审查
  -> 可修复风险才可能转化为恢复、健康寿命和未来选择权
```

## 关注对象

- 初级卫生保健、急诊、专科转诊、预防服务和长期随访。
- 医疗可及性、地理距离、等待时间、费用、保险覆盖、质量差异和服务连续性。
- 医疗服务断点、复诊失败、转诊失败、照护碎片化和健康不平等。
- 与健康素养、数字身份、药品供应、远程医疗、康复和长期照护的接口。

## Human Infra 模型链路

```text
医疗服务连续性
  -> 风险被及时发现和解释
  -> 诊断、治疗、转诊、随访和恢复路径不被中断
  -> 可修复疾病和功能损伤的持续时间缩短
  -> 健康寿命、有效时间和行动能力保留
  -> 主体持续性和未来选择权增强
```

## 非目标

- 不提供医疗诊断、治疗方案、用药、急救或个体风险结论。
- 不推荐具体医生、医院、保险计划、支付路径或个体就医决策。
- 不把医疗可及性指标写成个体寿命预测或确定健康结论。

## Source Signals

- WHO Universal Health Coverage: https://www.who.int/health-topics/universal-health-coverage
- WHO Primary Health Care: https://www.who.int/health-topics/primary-health-care
- Healthy People 2030 Access to Health Services: https://odphp.health.gov/healthypeople/priority-areas/social-determinants-health/literature-summaries/access-health-services

## 下一步

- 建立医疗服务连续性变量表：可及性、等待、费用、质量、转诊、随访和恢复。
- 将医疗接入与 `health-literacy-navigation/`、`financial-resilience-access/`、`supply-chain-continuity/` 的边界拆清。
- 整理 UHC、PHC、医疗质量、保险覆盖和服务不平等的 Source Cards。
