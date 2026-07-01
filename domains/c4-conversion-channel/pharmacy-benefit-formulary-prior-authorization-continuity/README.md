# Pharmacy Benefit Formulary Prior Authorization Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/pharmacy-benefit-formulary-prior-authorization-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
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


## 定位

本域研究处方药福利、处方集、step therapy、prior authorization、coverage determination、exception、药房网络和患者成本如何影响主体能否持续获得医生已计划的药物治疗。

它不是医保申诉代写、规避保险规则或药品价格套利入口。

## 先验问题

```text
治疗可及何以成立？
  -> 药物必须被保险或支付系统承认
  -> 处方集、限制和授权流程必须可理解、可追踪、可申诉
  -> 成本和流程不能把处方变成不可执行任务
  -> 否则医学方案会在支付治理层失败
```

## 研究对象

- Medicare Part D、commercial PBM、处方集层级和药房网络。
- Prior authorization、step therapy、quantity limits、coverage determination 和 exception。
- Copay、coinsurance、deductible、coverage gap、患者援助和可负担性。
- 处方转换、拒付、延迟、续期和跨计划迁移。

## 关键变量

- 授权通过率、等待时间、拒付率和申诉成功率。
- 自付费用、药物级别、网络内药房覆盖和限制类型。
- 治疗中断天数、弃药率、替代治疗延迟和行政负担。

## 证据入口

- CMS / Medicare Part D manual、formulary、coverage determination 和 exceptions 资料。
- Medicare Plan Finder、CMS formulary 文件和公开计划资料。
- KFF、AHRQ、JAMA / Health Affairs 等药品福利研究。

## 非目标

- 不生成医保申诉、prior authorization 材料、诊断证明、临床理由或法律策略。
- 不指导规避处方集、药房网络、身份核验、copay、保险限制或资格规则。
- 不收集保险卡、member ID、处方、诊断、收入、申诉文件或个人支付记录。

## 上下游

- 上游：`medicine-access-treatment-continuity/`、`financial-resilience-access/`、`insurance-risk-transfer/`。
- 下游：`retail-pharmacy-prescription-dispensing-continuity/`、`medication-reconciliation-regimen-adherence-continuity/`。
