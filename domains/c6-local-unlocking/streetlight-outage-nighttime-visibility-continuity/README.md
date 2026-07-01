# Streetlight Outage Nighttime Visibility Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/streetlight-outage-nighttime-visibility-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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
