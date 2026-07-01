# Long COVID Post-Acute Infection Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/long-covid-post-acute-infection-continuity` |
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


`long-covid-post-acute-infection-continuity/` 研究 Long COVID、感染后长期症状、多系统负担、疲劳/脑雾、呼吸心血管自主神经症状和服务连续性如何影响主体持续性。

## Core Question

当感染后的长期多系统症状改变能量、认知、呼吸、心血管和工作能力时，主体如何在不确定证据和服务碎片中维持行动、恢复和未来选择权？

## 先验位置

- 与 `chronic-infectious-disease-care-continuity/` 的关系：Long COVID 是感染后长期状态，不是急性感染本身。
- 与 `respiratory-oxygenation/`、`autonomic-nervous-system-homeostasis/` 和 `fatigue-risk-alertness-continuity/` 的关系：多系统症状需要跨域接口。
- 与 `healthcare-access-continuity/` 的关系：服务碎片、污名和诊断不确定性会放大功能损耗。

## 关注对象

- 疲劳、脑雾、劳累后症状加重、呼吸、心血管、自主神经、疼痛、睡眠、心理、工作参与和服务导航。
- 证据更新、诊断边界、公共卫生监测、职业/学校适配和长期恢复不确定性。

## Human Infra 模型链路

```text
感染后长期多系统症状
-> 能量、认知、呼吸、心血管和自主调节负担增加
-> 工作、学习、照护、恢复和服务导航能力下降
-> 有效时间与未来选择权被压缩
-> 主体持续性下降
```

## 非目标

- 不提供 Long COVID 诊断、检测解释、药物、康复、运动、补剂、氧疗、工作/学校证明、残障或保险建议。
- 不根据症状、可穿戴数据或感染史输出个体风险、活动许可、治疗或预后判断。

## Source Signals

- CDC Long COVID: https://www.cdc.gov/long-covid/

## 下一步

- 建立 post-acute infection card：把多系统症状、证据不确定性、服务导航和功能参与放入同一审查框架。
