# Catheter-Associated UTI and Device Infection Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/catheter-associated-uti-device-infection-continuity` |
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


`catheter-associated-uti-device-infection-continuity/` 研究导尿管、长期留置装置、CAUTI、设备依赖、护理流程和感染控制断点如何影响主体持续性。

> 核心问题：导尿管能维持排尿出口，但也会把身体边界打开成感染、限制行动、羞耻、照护依赖和抗菌药压力的设备接口。

## 先验位置

```text
有效永生
  -> 主体需要在排尿受限时建立替代出口
  -> 替代出口依赖设备、护理、感染控制和撤除判断
  -> 因此 CAUTI 与导尿设备是排泄出口设备化后的风险域
```

## 关注对象

- Indwelling catheter, intermittent catheterization context, CAUTI, device duration, hygiene workflow, mobility, privacy, antimicrobial exposure, long-term care burden。
- 与 `urinary-retention-bladder-emptying-continuity/` 的关系：尿潴留域关注膀胱排空失败，本域关注导尿设备带来的感染与照护接口。

## Human Infra 模型链路

```text
导尿设备与护理流程 T
  -> 改变设备暴露时间、感染控制、行动半径、隐私和照护负担 X
  -> 改变排泄出口稳定性、感染风险、尊严和恢复状态 S
  -> 改变 CAUTI、尿源性脓毒症、跌倒、住院和抗菌药压力 lambda(t)
  -> 改变有效时间、照护依赖和未来选择权
```

## 非目标

- 不提供导尿、拔管、冲洗、消毒、设备选择、护理操作、尿液判断或感染处理建议。
- 不替代护理、泌尿、感染控制、长期照护监管或本地医疗流程。

## Source Signals

- CDC catheter-associated urinary tract infection resources.
- AHRQ / CDC healthcare-associated infection materials.
- MedlinePlus catheter and urinary infection public materials.
