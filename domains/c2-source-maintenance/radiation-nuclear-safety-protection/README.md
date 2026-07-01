# Radiation Nuclear Safety Protection

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/radiation-nuclear-safety-protection` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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


辐射、核安全与防护域研究：当主体持续性依赖“电离辐射、核设施、放射性材料和辐射事故风险被监测、限制和响应”时，需要哪些防护、监管、监测、应急和长期环境治理基础设施。

## 对象

- 电离辐射防护、职业/医疗/环境辐射风险和剂量治理。
- 核设施安全、放射性材料安全、辐射监测和环境监测网络。
- 辐射应急、风险沟通、长期污染治理和公众防护框架。
- 医疗、能源、科研、工业和空间场景中的辐射风险边界。
- 辐射风险与癌症、免疫、造血、神经、胎儿发育和生态系统的接口。

## Human Infra 价值

辐射风险具有低频高冲击、不可见、可累积和长期潜伏特征。辐射核安全基础设施把不可感知的能量暴露转化为可测量、可监管、可限制、可响应的风险对象，防止一次事故或慢性暴露截断主体持续性。

```text
辐射源与核系统存在
  -> 监测、剂量限制、设施安全和应急治理
  -> 暴露、污染和长期健康风险下降
  -> 医疗、能源、科研和环境系统可在安全边界内运行
```

## 边界

本域只整理公开安全标准、监管框架、监测网络、风险类型和非操作性治理资料。

不提供：

- 放射源、核材料、设施、仪器或污染现场的操作、获取、规避、处置或防护步骤。
- 核设施攻击、规避监管、绕过监测、制造或扩散放射性风险的信息。
- 个体剂量解释、医疗影像选择、放射治疗建议或辐射事故现场指挥。
- 避难、撤离、去污、碘剂或个人防护的实时操作建议。

## 上游与下游

- 上游：`risk-engineering/`、`space-extreme-habitation/`、`cancer-control/`、`public-health-laboratory-diagnostic-capacity/`。
- 下游：`emergency-preparedness-response/`、`planetary-health-environment/`、`healthcare-access-continuity/`、`governance-rights/`。

## 初始资料线索

- IAEA radiation protection and nuclear safety resources。
- U.S. Nuclear Regulatory Commission public resources。
- EPA RadNet resources。
- CDC radiation emergencies resources。
