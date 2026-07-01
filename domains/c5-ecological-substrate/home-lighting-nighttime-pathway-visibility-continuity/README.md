# Home Lighting Nighttime Pathway Visibility Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-lighting-nighttime-pathway-visibility-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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


`home-lighting-nighttime-pathway-visibility-continuity/` 研究家庭照明、夜间路径可见性、开关可达、眩光、阴影、楼梯/浴室/卧室路径和停电影响如何改变夜间行动安全。

> 核心问题：夜间不是白天的缩小版。低照度会把视力、平衡、尿急、药物、睡眠惯性和环境障碍叠加成跌倒窗口。

## 先验位置

```text
主体需要夜间移动
  -> 必须在低照度、半醒、急迫和路径障碍中保持定向
  -> 照明不足会放大视觉、前庭、肌骨和认知负担
  -> 因而夜间路径可见性是睡眠和行动连续性的接口
```

## 关注对象

- 卧室到浴室路径、夜灯、开关位置、自动照明、楼梯照明、眩光、阴影、停电备用、眼病和夜尿场景。
- 老年人、视力受限者、儿童、照护者、夜班/睡眠中断主体。

## Human Infra 模型链路

```text
家庭照明与夜间路径 T
  -> 改变可见性、眩光、阴影、开关可达和备用照明 X
  -> 改变夜间起身、如厕、照护和应急移动状态 S
  -> 改变跌倒、碰撞、睡眠破坏、外出回避和照护依赖风险 λ(t)
  -> 改变恢复质量、有效时间和独立行动能力
```

## 非目标

- 不提供照明设计、产品推荐、电气施工、智能家居配置、跌倒评分、视力判断或个体安全建议。
- 不收集家庭平面图、夜间行动记录、摄像头数据、睡眠记录、位置轨迹或残障资料。

## Source Signals

- CDC / STEADI home fall prevention materials.
- NIA falls and home safety materials.
- CPSC home safety materials.
