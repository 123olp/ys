# Streetlight Outage Nighttime Visibility Continuity

`streetlight-outage-nighttime-visibility-continuity/` 研究路灯、夜间可见性、照明故障报告、行人路径感知和夜间公共空间安全如何影响主体在黑暗时段的行动连续性。

## 先验链路

```text
主体需要在夜间继续出行、照护、工作和求助
  -> 夜间路径必须可见、可辨认、可被其他道路使用者识别
  -> 路灯故障、遮挡、照明不足或报告失败会降低路径可读性
  -> 可见性下降会增加跌倒、交通冲突、恐惧、绕行和时间成本
  -> 夜间行动半径收缩，服务可达、社交参与和恢复能力下降
```

## 研究对象

- streetlight outage、nighttime visibility、pedestrian lighting、roadway lighting、reporting channel、repair status、dark corridor、transit stop lighting 和视觉可读性。

## 不能做

- 不提供电气维修、灯杆操作、布线、照明设计、安防布控、犯罪风险判断、路线建议、监控或个案安全建议。
- 不收集、复制或要求精确住址、夜间行程、照片元数据、个人位置、监控画面或执法资料。

## Source Signals

- FHWA nighttime visibility: https://highways.dot.gov/safety/other/nighttime-visibility
- FHWA pedestrian and bicyclist safety: https://highways.dot.gov/safety/pedestrian-bicyclist
- Illuminating Engineering Society road and pedestrian lighting context: https://www.ies.org/
- Open311 GeoReport v2: https://wiki.open311.org/GeoReport_v2/

## 上下游关系

- 上游：`walking-bicycling-micromobility-continuity/`、`light-circadian-environment/`、`municipal-311-service-request-continuity/`。
- 下游：`public-transit-service-operations-continuity/`、`personal-safety-violence-prevention/`、`fall-risk-prevention-home-safety-continuity/`。
