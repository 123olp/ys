# Tornado Warning Safe Room Shelter Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/tornado-warning-safe-room-shelter-continuity` |
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


`tornado-warning-safe-room-shelter-continuity/` 研究龙卷风 watch/warning、短窗口避险、安全室、室内避难、移动房屋风险和灾后救援如何影响主体持续性。

> 核心问题：龙卷风把警报理解、室内空间选择、家庭团聚、无障碍移动和建筑脆弱性压缩到分钟级窗口。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须在极短时间内从日常行动切换到保护姿态
  -> 龙卷风会击穿建筑、交通、通信和户外暴露边界
  -> 若警报、就地庇护、移动房屋转移或灾后救援失败，急性死亡和伤害风险快速上升
  -> 因而龙卷风预警与安全空间是主体短窗口避险执行域
```

## 关注对象

- Tornado watch/warning、sirens、WEA、NOAA Weather Radio、家庭警报冗余和夜间风险。
- 地下室、安全室、室内小房间、移动/制造房屋、学校、工作场所、户外场景和灾后搜救入口。
- 与 `emergency-alerts-communications/` 的边界：该域关注公共警报基础设施；本域关注龙卷风警报后的空间避险执行。

## Human Infra 模型链路

```text
龙卷风预警与安全空间系统 T
  -> 改变警报接收、风险理解、避难位置、移动时间、建筑脆弱性和团聚变量 X
  -> 改变主体在风暴窗口中的保护状态 S
  -> 改变创伤、坠物、失联、心理冲击和服务中断风险 λ(t)
  -> 影响急性生存、恢复负担和家庭连续性
```

## 非目标

- 不提供实时龙卷风判断、避难点选择、建筑安全鉴定、风暴追逐、救援行动或灾损索赔建议。
- 不替代 NWS、SPC、地方应急管理、建筑规范或公共安全机构。
- 不鼓励户外观察、追逐风暴、忽视官方警报或进入受损结构。

## Source Signals

- NWS Tornado Safety: https://www.weather.gov/safety/tornado
- Storm Prediction Center: https://www.spc.noaa.gov/
- Ready.gov Tornadoes: https://www.ready.gov/tornadoes

## 下一步

- 建立 watch/warning、夜间警报、移动房屋、学校/工作场所避险和灾后搜救 source card。
- 与 `home-lighting-nighttime-pathway-visibility-continuity/`、`manufactured-housing-park-tenure-safety-continuity/` 和 `disaster-behavioral-health-distress-recovery-continuity/` 对齐。
