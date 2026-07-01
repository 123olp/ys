# Household Emergency Preparedness Resilience

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/household-emergency-preparedness-resilience` |
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


`household-emergency-preparedness-resilience/` 研究家庭、个人和小型照护单元如何在灾害、停电、极端天气、通信中断、撤离和短期服务断点前建立最低准备能力。

> 核心问题：公共应急系统存在不等于主体能被及时接住；灾害发生前的家庭准备、文件备份、药物连续性、通信计划和特殊需求安排，会决定冲击是短期扰动还是主体持续性的断裂。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须穿越低频高冲击事件
  -> 公共救援抵达前存在家庭级时间窗口
  -> 该窗口需要食物、水、药物、通信、文件、照护和撤离准备
  -> 家庭准备不足会放大灾害、停电、极端天气和医疗断点风险
  -> 因此家庭应急准备是主体持续性的前置韧性域
```

## 关注对象

- 家庭应急计划、联系人、会合点、撤离准备、避难准备、宠物和家庭成员特殊需求。
- 应急物资包、水、食物、照明、通信、电源、急救用品、常用药物和重要文件副本。
- 慢病、残障、老年人、儿童、语言障碍、交通困难和居家医疗设备带来的准备差异。
- 与 `emergency-preparedness-response/` 的边界：本域关注家庭和个人准备；`emergency-preparedness-response/` 关注公共响应系统。
- 与 `emergency-alerts-communications/` 的边界：本域关注接收警报后的家庭行动准备；警报域关注公共预警和求助入口。

## Human Infra 模型链路

```text
家庭应急准备 T
  -> 改变物资储备、通信计划、文件可用性、药物连续性、照护安排和撤离准备变量 X
  -> 改变主体在救援抵达前维持生命、联系外部、获得服务和恢复秩序的状态 S
  -> 改变灾害中断、慢病断药、通信失联、撤离失败、照护断裂和恢复延迟风险 λ(t)
  -> 影响生存概率、有效时间、家庭连续性和灾后未来选择权
```

## 非目标

- 不提供实时灾害指挥、撤离路线、急救医疗、危险物储存、武器防卫、用电改造或极端生存主义指南。
- 不把家庭准备写成可以替代公共救援、无障碍应急服务、社区互助和制度责任。
- 不鼓励恐慌囤积、排他性资源抢占、谣言传播或绕过官方应急指令。

## Source Signals

- American Red Cross Preparedness: https://www.redcross.org/get-help/how-to-prepare-for-emergencies.html
- CDC Prepare Your Health: https://www.cdc.gov/orr/ready/index.htm
- Ready.gov Make a Plan: https://www.ready.gov/plan
- Ready.gov Emergency Kit: https://www.ready.gov/kit
- NOAA Weather-Ready Nation: https://www.weather.gov/wrn/

## 下一步

- 建立家庭准备变量表：物资、水、药物、文件、通信、电源、照护、交通、宠物、特殊需求和恢复入口。
- 与 `disaster-recovery-relief-continuity/`、`medicine-access-treatment-continuity/`、`energy-access-resilience/` 和 `caregiving-long-term-care/` 建立接口。
