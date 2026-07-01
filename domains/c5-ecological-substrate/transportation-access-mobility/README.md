# Transportation Access Mobility

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/transportation-access-mobility` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 主要提供主体展开未来所需的基础环境、资源、治理或基础设施。 |
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


`transportation-access-mobility/` 研究交通接入和日常移动系统能否把主体连接到医疗、工作、食物、照护、社区和应急资源。

> 核心问题：主体不只需要身体能动，还需要外部交通系统让行动能力转化为真实可达性；不能到达，就等于资源不可用。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须到达服务、资源、关系、工作和安全地点
  -> 交通系统必须可达、可靠、可负担、无障碍且低风险
  -> 医疗、照护、食物、工作和社区资源才会从名义存在变成可用支持
```

## 关注对象

- 公共交通、主动交通、无障碍交通、辅助出行、交通成本和出行时间。
- 医疗交通、工作通勤、食物可达、社区参与、灾害撤离和交通安全。
- 交通贫困、服务荒漠、出行负担、道路风险、无车人群和行动障碍群体。
- 与身体移动能力、住房位置、医疗可及、职业设计和应急响应的接口。

## Human Infra 模型链路

```text
交通接入与日常移动
  -> 主体能够到达医疗、照护、工作、食物、关系和应急资源
  -> 等待成本、缺席、延误、孤立和服务断点减少
  -> 行动半径、有效时间、恢复机会和社会参与增加
  -> 主体持续性从内部能力扩展到外部可达性
```

## 非目标

- 不提供个体路线、驾驶、车辆、交通法律、应急撤离或出行安全操作建议。
- 不替代专业交通规划、医疗交通服务、无障碍评估或应急指挥。
- 不将交通可达性简化为个人努力，忽视城市设计、服务覆盖和制度约束。

## Source Signals

- CDC Transportation and Health: https://www.cdc.gov/transportation/
- U.S. Department of Transportation Health: https://www.transportation.gov/mission/health
- CDC Healthy Places Transportation Toolkit: https://www.cdc.gov/healthy-places/php/toolkit/transportation.html

## 下一步

- 建立交通接入变量表：出行时间、可靠性、成本、无障碍、交通安全、服务距离和撤离能力。
- 整理交通健康、医疗交通、交通公平、无障碍交通和日常移动数据 Source Cards。
- 与 `physical-activity-mobility/` 明确分工：本域研究外部交通可达性，后者研究身体移动能力。
