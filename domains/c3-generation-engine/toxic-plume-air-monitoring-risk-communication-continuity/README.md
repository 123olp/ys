# Toxic Plume Air Monitoring Risk Communication Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/toxic-plume-air-monitoring-risk-communication-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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


`toxic-plume-air-monitoring-risk-communication-continuity/` 研究有毒羽流、空气监测、模型工具、阈值沟通、不确定性表达和公众行动接口如何降低事故中的错误感知和错误行动。

> 核心问题：有毒羽流不可见且随风、地形、时间变化；如果监测和沟通不能解释不确定性，人会在恐慌、迟疑和误导之间失去行动窗口。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体在空气风险中依赖可观测、可信、可理解的信息
  -> 有毒羽流把位置、时间、气象和化学特性耦合成动态暴露
  -> 空气监测与风险沟通把不确定暴露转化为可更新的公共判断边界
```

## 关注对象

- 空气监测、羽流模型、气象接口、公众信息、阈值解释、不确定性、误报/漏报和行动触发。
- 与 `air-quality-ventilation-exposure-control/` 的关系：空气质量域关注常态和建筑暴露；本域关注事故性有毒羽流的监测沟通链。

## Human Infra 模型链路

```text
有毒羽流监测与沟通
  -> 改变风险可见性、行动时机、地点判断和公众信任
  -> 改变暴露剂量、错误避险、医疗挤兑和恢复沟通成本
  -> 增强主体在事故空气风险中的行动能力和恢复能力
```

## 非目标

- 不提供实时羽流预测、传感器部署、阈值解释、撤离命令、暴露诊断或防护操作。
- 不提供化学品扩散优化、攻击模拟、设施侦察、恐慌传播或规避检测。
- 不替代环境监管、消防、公共卫生或气象部门的现场判断。

## Source Signals

- EPA CAMEO software suite: https://www.epa.gov/cameo
- EPA ALOHA air hazard modeling: https://www.epa.gov/cameo/aloha-software
- NOAA Office of Response and Restoration response tools: https://response.restoration.noaa.gov/
- CDC/ATSDR toxic substances portal: https://wwwn.cdc.gov/TSP/

## 下一步

- 建立 Toxic Plume Communication Card：source signal, monitoring, model, weather, uncertainty, public action interface, equity risk。
- 与 `weather-climate-observation-forecasting/`、`air-quality-ventilation-exposure-control/` 和 `emergency-alerts-communications/` 建立接口。
