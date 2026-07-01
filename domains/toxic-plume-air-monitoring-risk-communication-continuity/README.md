# Toxic Plume Air Monitoring Risk Communication Continuity

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
