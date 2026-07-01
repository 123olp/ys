# Cellular Senescence Clearance

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cellular-senescence-clearance` |
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


Cellular Senescence Clearance 负责整理细胞衰老、SASP、senolytics、senomorphics、组织炎症和衰老细胞负担。

核心问题：

> 衰老细胞并非只是“老细胞”，它们可能通过分泌信号改变组织环境；清除或调节这类细胞同时涉及修复收益、炎症、癌症防御和副作用风险。

## 先验位置

```text
主体持续性最大化
  -> 组织需要清除不可修复细胞并维持局部环境稳定
  -> 衰老细胞积累和 SASP 会改变炎症、再生、免疫和邻近细胞状态
  -> 衰老细胞也可能承担肿瘤抑制和伤口修复角色
  -> 因此衰老细胞清除是收益与风险并存的维护条件
```

## 关注对象

- cellular senescence、SASP、senolytics、senomorphics、组织微环境和慢性炎症。
- 衰老细胞与癌症、免疫、再生医学、纤维化、代谢和神经退行的关系。
- 衰老细胞负担测量、组织特异性、治疗窗口和安全边界。
- 与 `immune-maintenance/` 的关系：本域关注细胞状态和 SASP；免疫域关注免疫监视、感染防御和炎症系统。

## Human Infra 模型链路

```text
衰老细胞清除 / 调节 T
  -> 改变 senescence burden、SASP、局部炎症和组织微环境 X
  -> 改变组织维护状态 S
  -> 改变再生能力、炎症、纤维化、癌症和功能衰退风险
  -> 改变健康寿命、恢复能力和有效时间
```

## 非目标

- 不提供 senolytic 药物、剂量、用法、补剂或人体实验建议。
- 不把清除衰老细胞写成单向有益。
- 不忽略细胞衰老在肿瘤抑制、伤口修复和组织稳态中的可能作用。

## Source Signals

- Hallmarks of Aging: https://pubmed.ncbi.nlm.nih.gov/36599349/
- NIA Biology of Aging: https://www.nia.nih.gov/research/dab/biology-aging-program
