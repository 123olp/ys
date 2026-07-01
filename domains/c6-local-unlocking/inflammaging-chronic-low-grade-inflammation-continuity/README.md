# Inflammaging Chronic Low Grade Inflammation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/inflammaging-chronic-low-grade-inflammation-continuity` |
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


Inflammaging Chronic Low Grade Inflammation Continuity 负责整理炎症衰老、慢性低度炎症、免疫代谢、组织损伤信号和多病共存风险。

核心问题：

> 慢性低度炎症不是单一疾病，而是多个衰老、感染、代谢、组织损伤和社会环境因素汇合后的系统状态；它会持续抬高风险底噪并压缩恢复能力。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要长期保持低损伤、可恢复、可适应的系统状态
  -> 年龄、感染、代谢失衡、衰老细胞、组织损伤和压力暴露会累积炎症信号
  -> 慢性低度炎症会影响心血管、代谢、神经、免疫和癌症风险
  -> 风险底噪升高会降低恢复能力、行动质量和健康寿命
  -> 因此 inflammaging 是连接多个机制域的系统性风险条件
```

## 关注对象

- inflammaging、chronic low-grade inflammation、immune-metabolic crosstalk、CRP/IL-6/TNF 等炎症信号边界。
- 衰老细胞、感染、肥胖、睡眠、压力、污染、牙周炎、肠道屏障和社会逆境的交叉影响。
- 与 `cellular-senescence-clearance/` 的关系：衰老细胞/SASP 是来源之一，不是全部 inflammaging。
- 与 `immune-maintenance/` 的关系：本域关注低度慢炎症状态；免疫域关注整体防御、耐受和监视。

## Human Infra 模型链路

```text
炎症调节 / 暴露治理 T
  -> 改变慢性炎症信号、免疫代谢和组织损伤反馈 X
  -> 改变系统恢复与风险底噪状态 S
  -> 改变心血管、代谢、神经退行、癌症、感染和衰弱风险
  -> 改变健康寿命、有效时间和主体行动稳定性
```

## 非目标

- 不提供抗炎药、补剂、饮食、运动、睡眠、检验解读或个体治疗建议。
- 不把单一炎症指标下降写成寿命延长。
- 不把 inflammaging 作为包打天下的解释，必须追问上游来源和下游终点。

## Source Signals

- NIA Biology of Aging Program: https://www.nia.nih.gov/research/dab/biology-aging-program
- Immune aging, immunosenescence, and inflammaging review: https://pmc.ncbi.nlm.nih.gov/articles/PMC12286891/
- Chronic inflammation and the hallmarks of aging: https://pmc.ncbi.nlm.nih.gov/articles/PMC10359950/
