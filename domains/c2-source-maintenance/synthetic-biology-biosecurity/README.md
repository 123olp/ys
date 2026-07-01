# Synthetic Biology Biosecurity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/synthetic-biology-biosecurity` |
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


Synthetic Biology Biosecurity 负责整理合成生物学、生物安全、生物安保、双重用途风险和治理边界如何影响主体持续性。

核心问题：

> 生物技术既可能修复身体、制造疗法和降低疾病风险，也可能扩大病原体、实验外泄和双重用途风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续性依赖未来生物技术修复、诊断和制造能力
  -> 同一能力也可能降低制造生物风险的门槛
  -> 生物风险可同时改变个体、群体和文明层面的风险函数
  -> 因此生物安全和生物安保是生物技术进入主体持续性系统的治理域
```

## 关注对象

- 合成生物学、重组或合成核酸研究、生物安全、生物安保和双重用途治理。
- DNA 合成筛查、实验室安全文化、机构审查、事故报告和责任边界。
- 疫情风险、病原体风险、医疗创新、平台生物技术和风险沟通。
- 高风险研究主张的证据边界、禁止用途、审查门槛和中止条件。

## Human Infra 模型链路

```text
生物安全治理措施 T
  -> 改变风险识别、审查、筛查、隔离、报告和治理能力 X
  -> 改变生物技术系统的安全状态 S
  -> 降低误用、外泄、事故和群体健康冲击风险 λ(t)
  -> 保留生物技术修复主体的正向窗口并限制尾部风险
```

## 非目标

- 不提供病原体工程、培养、传播、规避筛查、实验协议或湿实验步骤。
- 不提供可用于增强危害、逃避免疫、规避检测或绕过生物安全审查的信息。
- 不把生物安全治理写成对具体实验的操作建议。

## Source Signals

- NIH Guidelines for Research Involving Recombinant or Synthetic Nucleic Acid Molecules: https://osp.od.nih.gov/policies/biosafety-and-biosecurity-policy/#tab2/
- WHO Laboratory Biosafety Manual: https://www.who.int/publications/i/item/9789240011311
- National Academies reports on biosecurity: https://www.nationalacademies.org/topics/biosecurity

## 下一步

1. 建立生物技术双重用途边界表：收益类型、风险类型、审查对象、禁止输出。
2. 与 `cellular-reprogramming/`、`regenerative-medicine/`、`risk-engineering/`、`governance-rights/` 建立生物创新和安全治理边界。
