# Renal Hepatic Clearance

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/renal-hepatic-clearance` |
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


Renal Hepatic Clearance 负责整理肾脏、肝脏、解毒、代谢、药物清除、尿毒素、胆汁代谢和系统稳态。

核心问题：

> 主体长期运行需要持续清除代谢废物、处理药物和维持体液/代谢稳态；肝肾功能下降会限制治疗选择、恢复能力和长期生存。

## 先验位置

```text
主体持续性最大化
  -> 身体必须持续清除废物、代谢药物并维持内环境稳定
  -> 肾脏和肝脏承担过滤、代谢、解毒、体液和营养处理功能
  -> 清除能力下降会提高毒性、药物副作用、疲劳、感染和死亡风险
  -> 因此肝肾清除能力是长期医学可用性和主体恢复能力的基础条件
```

## 关注对象

- 慢性肾病、肾功能、肝病、药物代谢、毒性负担、尿毒素、胆汁代谢和清除能力。
- 肝肾功能与营养、心血管、糖尿病、感染、药物安全和衰老的关系。
- 肝肾指标、药物剂量边界、临床终点和治疗可及性限制。
- 与 `longevity-evidence/` 的关系：长寿证据域可记录干预；本域关注清除器官作为系统约束。

## Human Infra 模型链路

```text
肝肾维护 / 暴露控制 T
  -> 改变过滤、代谢、解毒、药物清除和内环境变量 X
  -> 改变系统清除状态 S
  -> 改变毒性、药物副作用、慢病进展、治疗选择和死亡风险
  -> 改变健康寿命、治疗可用性和恢复能力
```

## 非目标

- 不提供检测解释、用药、剂量调整、饮食、透析、移植或治疗建议。
- 不把单个肝肾指标写成整体健康结论。
- 不忽略药物、补剂和暴露在肝肾功能下降时的风险。

## Source Signals

- NIDDK Chronic Kidney Disease: https://www.niddk.nih.gov/health-information/kidney-disease/chronic-kidney-disease-ckd
- NIDDK Liver Disease: https://www.niddk.nih.gov/health-information/liver-disease
