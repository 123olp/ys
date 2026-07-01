# Powered Industrial Truck Forklift Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/powered-industrial-truck-forklift-safety-continuity` |
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


`powered-industrial-truck-forklift-safety-continuity/` 研究叉车和 powered industrial trucks 的驾驶、载荷、行人隔离、视线盲区、翻倒、撞击、培训和仓储节奏如何影响主体持续性。

核心问题：

> 物流和仓储把物资流动变成社会运行能力，但叉车把重载、速度、盲区和行人混行压缩到同一空间，安全失效会直接切断身体和供应链。

## 先验位置

```text
有效永生 / 主体持续性
  -> 主体依赖仓储、物流和制造场景获取物资与收入
  -> 叉车等工业车辆在共享空间移动重载
  -> 翻倒、撞击、夹挤和行人混行会造成急性死亡和长期失能
  -> 因此叉车安全是供应链执行与劳动持续性的共同条件
```

## 关注对象

- Powered industrial trucks、forklifts、operator training、pedestrian separation、load stability、tip-over、blind spots、warehouse traffic。
- 风险链：车辆/行人共享空间 -> 视线/载荷/速度失配 -> 撞击/翻倒/夹挤 -> 创伤/死亡 -> 供应和收入中断。
- 制度链：training、authorization、traffic management、maintenance、incident reporting、production pressure。

## Human Infra 模型位置

```text
仓储/物流任务 T
  -> 改变工业车辆与行人暴露 X
  -> 改变身体安全和供应执行状态 S
  -> 改变急性创伤/死亡风险 lambda(t)
  -> 改变物资连续性、工作年限和未来选择权
```

## 非目标

- 不提供叉车驾驶、载荷计算、培训、路线设计、仓库交通控制、检查表、维修、认证、合规或事故处理建议。
- 不判断个人驾驶资格、复工、责任、工伤、赔偿、OSHA 违规或法律策略。
- 不帮助绕过培训、降低安全间隔、提升产能压过安全或规避监管。

## Source Signals

- OSHA Powered Industrial Trucks - Forklifts: https://www.osha.gov/powered-industrial-trucks
- OSHA Workers: https://www.osha.gov/workers

## 下一步

- 建立 Forklift Safety Continuity Card：vehicle type、pedestrian interface、load/visibility risk、training boundary、traffic pattern、incident pathway。
- 与 `freight-logistics-port-cold-chain-continuity/`、`occupational-exposure-industrial-hygiene/` 和 `workers-compensation-occupational-injury-benefit-continuity/` 建立接口。
