# Lymphatic Glymphatic Clearance

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/lymphatic-glymphatic-clearance` |
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


Lymphatic Glymphatic Clearance 负责整理淋巴系统、脑淋巴/类淋巴清除、组织液、免疫运输、水肿和脑废物清除如何影响主体持续性。

核心问题：

> 主体不仅需要输入氧气和营养，也需要把液体、废物、免疫信号和组织损伤产物持续清出；清除网络失效会让恢复系统变慢、变脆弱。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须长期维持组织液平衡、免疫运输和代谢废物清除
  -> 淋巴系统连接免疫、炎症、水肿、脂质吸收和组织修复
  -> 脑淋巴/类淋巴清除连接睡眠、脑废物、神经退行和认知连续性
  -> 因此淋巴与脑淋巴清除是恢复和废物管理域
```

## 关注对象

- 淋巴管、淋巴结、组织液、免疫细胞运输、水肿、脂质吸收和炎症清除。
- 脑膜淋巴、glymphatic clearance、睡眠相关脑废物清除和神经退行风险。
- 淋巴水肿、感染、癌症转移、术后恢复、慢性炎症和组织修复。
- 清除网络与睡眠、免疫、神经、肾肝、运动、皮肤、癌症和衰老的交叉。

## Human Infra 模型链路

```text
淋巴/脑淋巴状态 T
  -> 改变组织液平衡、免疫运输、炎症清除和脑废物清除 X
  -> 改变恢复速度、认知连续性、感染/水肿和组织修复状态 S
  -> 改变失能、神经退行、感染和长期功能下降风险 λ(t)
  -> 影响有效时间、恢复能力和学习行动窗口
```

## 非目标

- 不提供淋巴引流、按摩、设备、药物、睡眠处方、癌症治疗或个体康复建议。
- 不把 glymphatic 假说写成确定的人体治疗路径。
- 不替代 `sleep-circadian-recovery/`、`immune-maintenance/`、`neuro-continuity/` 或 `renal-hepatic-clearance/`。

## Source Signals

- PMC lymphatic aging review: https://pmc.ncbi.nlm.nih.gov/articles/PMC9026931/
- PubMed glymphatic system review: https://pubmed.ncbi.nlm.nih.gov/25947369/
- PMC meningeal lymphatics and brain clearance review: https://pmc.ncbi.nlm.nih.gov/articles/PMC6198085/

## 下一步

1. 建立清除网络变量表：组织液、淋巴运输、炎症清除、脑废物清除、睡眠耦合和水肿风险。
2. 与 `sleep-circadian-recovery/`、`immune-maintenance/`、`neuro-continuity/` 和 `renal-hepatic-clearance/` 建立边界。
