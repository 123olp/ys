# HAZWOPER Responder PPE Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/hazwoper-responder-ppe-safety-continuity` |
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


`hazwoper-responder-ppe-safety-continuity/` 研究危险物质响应人员的培训、PPE、呼吸防护、热压力、污染转移、轮换和心理/组织支持如何决定事故响应是否可持续。

> 核心问题：如果响应者不能安全持续工作，公众保护、医疗转运、去污、环境监测和恢复都会失去执行主体。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 社区事故响应依赖一线响应者持续可行动
  -> 危险材料响应把毒性、缺氧、热压力、装备负担和组织压力集中到响应者身上
  -> HAZWOPER 与 PPE 安全把响应者保护转化为公共服务连续性条件
```

## 关注对象

- HAZWOPER、PPE、呼吸防护、训练、医疗监测、热压力、污染转移、轮班疲劳和机构责任。
- 与 `occupational-exposure-industrial-hygiene/` 的关系：工业卫生域关注长期工作暴露；本域关注应急响应者在危险材料事故中的保护和持续行动能力。

## Human Infra 模型链路

```text
响应者 PPE 与 HAZWOPER 安全
  -> 改变响应者伤害、疲劳、热压力、交叉污染和任务持续能力
  -> 改变事故控制、公众保护、医疗转运和恢复速度
  -> 支撑社区主体持续性和应急系统可信度
```

## 非目标

- 不提供 PPE 选择、穿脱、呼吸器适配、现场等级判断、训练替代或职业合规建议。
- 不提供进入危险区域、采样、去污、泄漏控制、消防或救援操作步骤。
- 不输出规避 HAZWOPER、规避 PPE、规避监管或降低安全标准的信息。

## Source Signals

- OSHA HAZWOPER: https://www.osha.gov/hazwoper
- OSHA respiratory protection: https://www.osha.gov/respiratory-protection
- NIOSH emergency response resources: https://www.cdc.gov/niosh/emres/
- NIOSH personal protective equipment: https://www.cdc.gov/niosh/ppe/

## 下一步

- 建立 Responder Safety Card：training, PPE, respiratory protection, heat/fatigue, contamination control, medical monitoring, staffing rotation。
- 与 `occupational-exposure-industrial-hygiene/`、`mask-respirator-source-control-fit-access-continuity/` 和 `health-workforce-capacity/` 建立接口。
