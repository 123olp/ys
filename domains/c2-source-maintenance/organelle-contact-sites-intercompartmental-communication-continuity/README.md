# Organelle Contact Sites Intercompartmental Communication Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/organelle-contact-sites-intercompartmental-communication-continuity` |
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


This domain studies how membrane contact sites between organelles coordinate lipid transfer, calcium signaling, stress response, metabolism, and cell fate.

> Core question: can cells keep organelles coordinated when aging, stress, and damage require rapid cross-compartment regulation?

## 先验位置

有效永生要求细胞器不是孤立运行，而是持续通信、交换物质、同步压力响应并协调命运决策。ER-mitochondria contact sites、mitochondria-associated membranes and broader contact sites connect calcium, lipid, metabolism, autophagy, apoptosis, inflammation, and senescence.

## 关注对象

- ER-mitochondria contacts、MAMs 和其他 membrane contact sites。
- 钙信号、脂质转运、代谢耦合、线粒体动力学和自噬接口。
- 细胞衰老、炎症、凋亡和应激协调。
- 细胞器通信失败如何变成系统性失衡。

## Human Infra 模型链路

```text
细胞器接触位点和跨区室通信
-> 钙、脂质、代谢、应激和命运决策协调
-> 细胞状态、炎症、衰老和组织功能改变
-> 恢复能力、疾病风险和有效时间改变
-> 主体持续性改变
```

## 非目标

- 不提供细胞器接触位点调节、线粒体-ER 干预、补剂、药物、检测解释或治疗建议。
- 不把 contact site 信号写成个体健康或寿命预测。
- 不提供实验操作、成像协议、基因调控、药筛或人体试验建议。

## Source Signals

- PubMed: [Mitochondria-associated membranes in aging and senescence: structure, function, and dynamics](https://pubmed.ncbi.nlm.nih.gov/29491385/).
- PubMed: [Mitochondria-endoplasmic reticulum contact sites in hepatocytic senescence](https://pubmed.ncbi.nlm.nih.gov/41521283/).
- PubMed: [Mitochondrial lipid trafficking](https://pubmed.ncbi.nlm.nih.gov/24001776/).
