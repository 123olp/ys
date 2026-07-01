# Wildfire Smoke Clean Air Respiratory Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/wildfire-smoke-clean-air-respiratory-continuity` |
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


`wildfire-smoke-clean-air-respiratory-continuity/` 研究野火烟雾、PM2.5、空气质量、清洁空气房间、过滤、呼吸风险和工作/学校中断如何影响主体持续性。

> 核心问题：野火烟雾让火灾风险从火线扩展到远距离室内外空气暴露，主体持续性取决于能否把空气质量信号转化为可执行的暴露控制。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要可呼吸空气、睡眠、工作学习和慢病稳定
  -> 野火烟雾会跨区域进入住宅、学校、工作和交通空间
  -> 若空气质量理解、室内过滤、活动调整和高风险人群保护失败，烟雾会变成急性和慢性健康税
  -> 因而野火烟雾清洁空气是呼吸暴露执行连续性域
```

## 关注对象

- 野火烟雾、颗粒物、AQI、室内空气、过滤、清洁空气房间、学校/工作调整和高风险人群。
- 哮喘、COPD、心血管疾病、儿童、老年人、孕产人群、户外劳动者和无住所人群。
- 与 `wildfire-landscape-fire-resilience/` 的边界：该域关注景观火灾、燃料和社区韧性；本域关注烟雾暴露、清洁空气和呼吸连续性。

## Human Infra 模型链路

```text
野火烟雾暴露控制系统 T
  -> 改变 AQI 理解、室内颗粒物、过滤、活动调整、呼吸防护和服务安排变量 X
  -> 改变主体空气暴露和慢病稳定状态 S
  -> 改变哮喘/COPD 加重、心血管事件、睡眠中断、缺勤和医疗挤兑风险 λ(t)
  -> 影响有效时间、恢复能力、工作学习连续性和未来选择权
```

## 非目标

- 不提供空气净化器/口罩购买建议、个人医疗处置、职业合规、学校停课决策、房屋改造或实时 AQI 行动指令。
- 不替代 AirNow、CDC、EPA、NWS、地方公共卫生、学校或雇主安全机构。
- 不鼓励忽视 evacuation/fire order、使用不合规设备、传播伪造空气质量数据或替代医疗建议。

## Source Signals

- AirNow Wildfire Smoke: https://www.airnow.gov/wildfires/
- CDC Wildfire Smoke: https://www.cdc.gov/wildfires/
- EPA Wildfire Smoke and Indoor Air: https://www.epa.gov/indoor-air-quality-iaq/wildfires-and-indoor-air-quality-iaq

## 下一步

- 建立 AQI、清洁空气房间、学校/工作暴露、户外劳动、高风险人群和慢病加重 source card。
- 与 `respiratory-oxygenation/`、`asthma-copd-maintenance-control-continuity/` 和 `shelter-in-place-clean-air-room-indoor-protection-continuity/` 对齐。
