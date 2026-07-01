# Clonal Hematopoiesis CHIP Inflammatory Risk Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/clonal-hematopoiesis-chip-inflammatory-risk-continuity` |
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


Clonal Hematopoiesis CHIP Inflammatory Risk Continuity 负责整理克隆性造血、CHIP、血液系统癌症风险、心血管风险、炎症通路和年龄相关造血系统重塑。

核心问题：

> 年龄增长不仅改变器官功能，也会改变造血干细胞克隆结构；某些克隆扩张可能同时影响癌症风险、炎症负担和心血管事件风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要长期稳定生成血液和免疫细胞
  -> 造血干细胞随年龄积累突变并可能出现克隆扩张
  -> 克隆性造血会改变血液癌症、炎症和心血管风险结构
  -> 这些风险会通过急性事件、慢性炎症、治疗复杂度和监测负担压缩生命路径
  -> 因此造血克隆结构是寿命预测和干预审查中的关键风险变量
```

## 关注对象

- clonal hematopoiesis、CHIP、hematopoietic stem cell aging、somatic mutation、clone expansion。
- 血液肿瘤风险、心血管风险、炎症信号、测序发现、监测不确定性和心理/保险/隐私边界。
- 与 `cancer-control/` 的关系：本域关注癌前/前临床克隆风险；癌症控制域关注筛查、治疗和肿瘤路径。
- 与 `immune-maintenance/` 的关系：本域关注造血克隆对免疫与炎症状态的上游影响。

## Human Infra 模型链路

```text
造血克隆检测 / 风险治理 T
  -> 改变 CHIP 状态、克隆大小、突变谱和炎症信号 X
  -> 改变血液与免疫系统风险状态 S
  -> 改变血液肿瘤、心血管事件、慢性炎症和治疗复杂度风险
  -> 改变健康寿命、死亡风险和未来治疗选择权
```

## 非目标

- 不解释个人基因测序、CHIP 检测、突变结果、癌症风险或临床随访。
- 不提供抗炎、抗凝、降脂、血液科监测或治疗建议。
- 不把 CHIP 写成确定疾病、确定寿命预测或保险/就业判断依据。

## Source Signals

- NCI / NIA Immune Aging and Cancer Therapy workshop: https://dctd.cancer.gov/about/news-events/events/iact-workshop
- Clonal hematopoiesis in human aging and disease: https://pmc.ncbi.nlm.nih.gov/articles/PMC8050831/
