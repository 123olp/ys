# Extracellular Matrix Glycation

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/extracellular-matrix-glycation` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 直接维护身体、脑、器官、衰老、损伤或生命系统这些可能性源体。 |
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


Extracellular Matrix Glycation 负责整理细胞外基质、胶原、弹性、纤维化、组织力学、糖化终产物和结构性老化如何影响主体持续性。

核心问题：

> 身体不只是细胞集合，也是一套材料结构；基质硬化、糖化和纤维化会让组织逐步失去弹性、修复性和功能余量。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要细胞之外的组织结构长期保持可修复、可传力、可灌注和可适应
  -> 细胞外基质决定组织力学、信号、迁移、修复和器官结构
  -> 糖化、交联、纤维化和硬化会改变血管、皮肤、肺、肾、肌腱、心脏和代谢环境
  -> 因此细胞外基质与糖化是结构性衰老的材料域
```

## 关注对象

- 胶原、弹性蛋白、蛋白聚糖、基底膜、细胞外基质重塑和组织力学。
- Advanced glycation end products、交联、硬化、纤维化、炎症和修复障碍。
- 血管硬化、肺/肾/肝纤维化、皮肤弹性、肌腱韧带、伤口和器官结构。
- ECM 与细胞衰老、再生医学、代谢、血管、皮肤、肌骨和癌症微环境的交叉。

## Human Infra 模型链路

```text
基质状态或糖化暴露 T
  -> 改变组织弹性、交联、纤维化、细胞信号和修复环境 X
  -> 改变器官结构、灌注、力学负荷和再生能力 S
  -> 改变失能、器官功能下降、慢病和死亡风险 λ(t)
  -> 影响健康寿命、有效时间和未来治疗可整合性
```

## 非目标

- 不提供抗糖化补剂、药物、饮食、检测解释、皮肤治疗或纤维化治疗建议。
- 不把 AGE、胶原或组织硬度指标写成个体寿命预测。
- 不替代 `musculoskeletal-integrity/`、`cardiovascular-resilience/`、`skin-barrier-wound-healing/` 或 `regenerative-medicine/`。

## Source Signals

- PMC extracellular matrix and aging review: https://pmc.ncbi.nlm.nih.gov/articles/PMC4181688/
- PMC advanced glycation end products and aging review: https://pmc.ncbi.nlm.nih.gov/articles/PMC3583887/
- NCBI extracellular matrix overview: https://www.ncbi.nlm.nih.gov/books/NBK26810/

## 下一步

1. 建立 ECM/糖化变量表：组织硬度、交联、纤维化、修复环境、器官结构和可逆性。
2. 与 `regenerative-medicine/`、`cellular-senescence-clearance/`、`skin-barrier-wound-healing/` 和 `cardiovascular-resilience/` 建立边界。
