# Thermal Homeostasis Resilience

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/thermal-homeostasis-resilience` |
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


Thermal Homeostasis Resilience 负责整理体温调节、热暴露、寒冷暴露、出汗、散热和温度极端如何支撑或截断主体持续性。

核心问题：

> 主体必须在可承受温度范围内运行；热失衡会把环境问题转化为心血管、神经、肾脏、体液和急性死亡风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须维持核心体温和散热/保温能力
  -> 热、冷、湿度、衣物、住房、工作强度和基础疾病共同决定温度风险
  -> 中暑、低体温、脱水或热应激会迅速压缩行动能力和生存概率
  -> 因此热稳态与温度韧性是主体持续性的环境-生理接口域
```

## 关注对象

- 核心体温、散热、出汗、血管舒缩、寒冷防护、热适应和温度感知。
- 热浪、职业热暴露、低温暴露、老年体温调节、药物影响、住房和能源可及性。
- 热应激如何影响体液、电解质、肾脏、心血管、认知、睡眠、工作和灾害韧性。
- 温度风险如何进入气候韧性、极端栖居、体液稳态、风险工程和资源基础设施模型。

## Human Infra 模型链路

```text
温度暴露或调节因素 T
  -> 改变体温、出汗、散热、脱水、电解质和心血管负荷 X
  -> 改变主体认知清醒度、行动能力、恢复状态和急性安全边界 S
  -> 改变热病、低体温、跌倒、肾损伤、心血管事件和死亡风险 λ(t)
  -> 影响健康寿命、有效时间和未来选择权
```

## 非目标

- 不提供中暑、低体温、补水、电解质、用药、降温、取暖或急救建议。
- 不把气温、体温或热感受写成个体诊断或处方。
- 不替代 `planetary-health-environment/` 或 `fluid-electrolyte-acid-base-homeostasis/`，而是承载身体热调节主接口。

## Source Signals

- CDC heat and health: https://www.cdc.gov/heat-health/
- NIA hot weather safety for older adults: https://www.nia.nih.gov/health/safety/hot-weather-safety-older-adults
- NIA cold weather safety for older adults: https://www.nia.nih.gov/health/safety/cold-weather-safety-older-adults

## 下一步

1. 建立热稳态变量表：核心体温、散热、出汗、热适应、寒冷防护、热病和低体温风险。
2. 与 `planetary-health-environment/`、`fluid-electrolyte-acid-base-homeostasis/`、`cardiovascular-resilience/` 和 `risk-engineering/` 建立交叉边界。
