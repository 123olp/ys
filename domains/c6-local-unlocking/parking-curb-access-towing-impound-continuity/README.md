# Parking Curb Access Towing Impound Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/parking-curb-access-towing-impound-continuity` |
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


`parking-curb-access-towing-impound-continuity` 研究停车、路缘上下客、装卸、残障停车、罚单、拖车、扣押、取回流程和费用如何影响主体能否完成出行并保留车辆移动能力。

> 核心问题：到达目的地不等于完成出行；如果停车、路缘访问、拖车和扣押链失控，移动任务会在最后几十米、罚费和车辆取回流程上失败。

## 关注对象

- 停车位、路缘管理、上下客、装卸、残障停车、停车支付、罚单、拖车、扣押、取回和费用。
- 医疗、照护、学校、工作、配送、搬家、灾害撤离和低收入车辆依赖场景。
- 与城市规划、公共交通、道路安全、消费者保护、法律援助和财务韧性的接口。

## Human Infra 链路

```text
停车与路缘访问连续
  -> 出行的最后一段、上下客和车辆保留可执行
  -> 罚单、拖车、扣押和费用冲击不再轻易切断移动能力
  -> 目的地可达性从地图路径转化为真实任务完成
  -> 主体医疗、工作、照护和公共服务接入增强
```

## 非目标

- 不提供逃避停车执法、规避罚单、隐藏车辆、绕过拖车、伪造残障许可或法律个案策略。
- 不替代本地交通部门、停车机构、DMV、法院、律师、执法、拖车场或消费者保护机构。
- 不收集车牌、停车记录、罚单、扣押单、位置轨迹、残障许可或个人支付信息。

## Source Signals

- U.S. DOT Curb Management resources: https://www.transportation.gov/
- FHWA Curbside Inventory / Curb Management materials: https://ops.fhwa.dot.gov/
- ADA.gov Parking guidance: https://www.ada.gov/
- USA.gov Traffic Tickets: https://www.usa.gov/traffic-tickets

## 下一步

- 建立 `destination -> curb/parking access -> payment/enforcement -> vehicle retention -> task completion` 变量表。
- 区分残障停车、医疗上下客、商业装卸、住宅停车、拖车扣押和罚费负担。
- 与 `urban-planning-land-use-zoning-resilience`、`transportation-access-mobility`、`access-to-justice-legal-aid` 和 `financial-resilience-access` 建立边界。
