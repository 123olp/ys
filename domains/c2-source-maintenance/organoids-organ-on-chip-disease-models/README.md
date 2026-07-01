# Organoids Organ On Chip Disease Models

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/organoids-organ-on-chip-disease-models` |
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


`organoids-organ-on-chip-disease-models/` 研究类器官、organ-on-chip、组织芯片、患者来源模型和新方法学如何降低生物医学试错成本、提高转化预测能力。

> 核心问题：有效永生需要更快、更准地发现可用干预。类器官和组织芯片的价值不是直接延寿，而是让人体相关模型更早暴露疗效、毒性、个体差异和失败机制。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要新药、再生疗法和抗衰干预更快被发现和淘汰
  -> 动物模型和二维细胞模型常常不能预测人体反应
  -> 类器官、organ-on-chip 和患者来源模型可能提高转化预测能力
  -> 模型失真、标准化不足和验证失败会制造伪证据
  -> 因此人体相关模型是降低医学创新成本的研究域
```

## 关注对象

- 类器官、assembloids、organ-on-chip、microphysiological systems、tissue chips 和患者来源模型。
- 药物筛选、毒性预测、疾病建模、个体差异、发育模型、肿瘤模型和再生医学验证。
- 标准化、可重复性、成熟度、血管化、免疫/神经/微生物整合、伦理和模型外推边界。
- 与 `research-infrastructure-open-science-translation/` 的边界：科研基础设施域关注发现生态；本域关注人体相关实验模型。
- 与 `clinical-trials-regulatory-science-translation/` 的边界：临床转化域关注人体试验；本域关注进入人体前的模型证据。

## Human Infra 模型链路

```text
类器官 / 组织芯片模型 M
  -> 改变药物筛选、毒性识别、疾病机制和个体差异估计 X
  -> 改变候选干预进入临床前的证据状态 S
  -> 改变研发失败、迟滞转化和安全遗漏风险 λ(t)
  -> 影响未来医学技术窗口和主体持续性
```

## 非目标

- 不提供类器官培养、芯片制造、样本处理、实验步骤或药物筛选操作。
- 不把模型结果直接写成人体疗效、诊断或治疗建议。
- 不保存可识别患者样本信息、基因组数据或敏感疾病模型细节。
- 不把动物替代、新方法学或监管接受度写成已经完全成熟。

## Source Signals

- NIH / NCATS Tissue Chip program: https://ncats.nih.gov/research/research-activities/tissue-chip
- FDA Alternative Methods: https://www.fda.gov/science-research/advancing-regulatory-science/alternative-methods
- FDA Innovative Science and Technology Approaches for New Drugs: https://www.fda.gov/drugs/science-and-research-drugs/innovative-science-and-technology-approaches-new-drugs
- Human Cell Atlas: https://www.humancellatlas.org/
- ISSCR Guidelines: https://www.isscr.org/guidelines

## 下一步

1. 建立模型成熟度表：组织类型、功能成熟度、验证终点、标准化程度和外推边界。
2. 与 `organoids` 相关资料沉淀为 Source Cards，区分疾病建模、毒性预测和治疗开发。
3. 与 `clinical-trials-regulatory-science-translation/` 和 `regenerative-medicine/` 建立证据接口。
