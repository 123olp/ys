# Swallowing Dysphagia Aspiration Nutrition

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/swallowing-dysphagia-aspiration-nutrition` |
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


吞咽、误吸与营养连续性域整理吞咽安全、气道保护、误吸、营养水分、进食尊严和照护负担。

核心问题：

> 食物和水只有安全进入身体才是资源；吞咽失效会让进食从恢复输入变成窒息、肺炎、营养不足、脱水和尊严损害。

## 先验位置

```text
主体持续性最大化
  -> 主体必须持续获得水分、能量和营养
  -> 吞咽把外部资源安全送入消化系统，同时保护气道
  -> 吞咽障碍增加误吸、窒息、肺炎、营养不足和照护负担
  -> 因而吞咽安全是营养入口、呼吸保护和尊严连续性的交叉基础设施
```

## 关注对象

- 吞咽障碍、误吸、窒息、吸入性肺炎、营养不良、脱水和饮食参与。
- 卒中、神经退行、TBI、头颈疾病、老年衰弱和 ICU 后等相关吞咽风险。
- 吞咽评估、饮食质地、管饲、口腔护理、照护者负担和进食尊严的证据边界。
- 与 `oral-health-continuity/` 的关系：口腔域关注咀嚼、疼痛、感染和口腔入口；本域关注吞咽、气道保护和营养水分安全进入。
- 与 `gastrointestinal-barrier-absorption/` 的关系：消化吸收域关注进入胃肠后的吸收；本域关注入口和误吸风险。

## Human Infra 模型链路

```text
吞咽筛查 / 言语吞咽治疗 / 照护流程 T
  -> 改变吞咽安全、气道保护、进食效率、营养水分入口和照护负担 X
  -> 改变主体肺部风险、营养状态、恢复能力、尊严和照护依赖状态 S
  -> 降低误吸、肺炎、窒息、脱水、营养不良和住院风险 λ(t)
  -> 增加恢复窗口、有效时间、生活质量和未来选择权
```

## 非目标

- 不提供吞咽诊断、吞咽造影/内镜解释、饮食质地调整、管饲、急救、康复动作或照护处置建议。
- 不把吞咽资料写成个体饮食、药物、护理或风险判断。
- 不替代言语语言治疗、营养、康复、耳鼻喉、呼吸或临床照护专业服务。

## Source Signals

- NIDCD dysphagia resources。
- ASHA swallowing disorders public resources as professional context。
- CDC pneumonia and older adult safety materials as secondary risk context。
