# Walker Cane Crutch Fit Maintenance Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/walker-cane-crutch-fit-maintenance-continuity` |
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


`walker-cane-crutch-fit-maintenance-continuity` 研究手杖、拐杖、助行器、助行轮、橡胶脚垫、刹车、调高、损坏替换和使用训练如何影响跌倒风险、移动范围、康复恢复和日常参与。

> 核心问题：低技术移动辅助器不是“小工具”，而是步态、平衡和环境之间的执行接口；尺寸不合、磨损、缺件或训练不足会把辅助转化为跌倒风险。

## 关注对象

- 手杖、拐杖、助行器、助行轮、脚垫、把手、刹车、折叠机构、调高和替换维护。
- 家庭、浴室、楼梯、门槛、街道、医疗机构、学校、工作和交通接驳中的辅助器使用断点。
- 伤后短期恢复、老年衰弱、神经肌肉疾病、术后康复和低资源环境。
- 与跌倒预防、康复功能、DME、居家安全和建筑无障碍的接口。

## Human Infra 链路

```text
助行器具运行连续
  -> 主体把平衡、力量和环境支持组合成可执行移动
  -> 磨损、尺寸不合、刹车失效和替换断点导致的跌倒风险下降
  -> 康复、就医、家务、工作和社区参与更稳定
  -> 独立生活、有效时间和恢复窗口增强
```

## 非目标

- 不提供步态诊断、辅助器处方、尺寸调节步骤、康复训练、设备购买、维修教程或个体跌倒风险判断。
- 不替代物理治疗师、作业治疗师、康复医生、DME 供应商、MedlinePlus 或 Medicare。
- 不把助行器具视为建筑无障碍、力量训练、药物审查或照护支持的替代品。

## Source Signals

- MedlinePlus Mobility Aids: https://medlineplus.gov/mobilityaids.html
- Medicare Durable Medical Equipment context: https://www.medicare.gov/coverage/wheelchairs-scooters

## 下一步

- 建立 `aid condition -> fit/maintenance/training dependency -> gait task -> fall/participation outcome` 变量表。
- 区分手杖、拐杖、助行器、术后短期使用、长期衰弱和家庭/社区场景。
- 与 `gait-balance-assessment-fall-screening-continuity`、`fall-risk-prevention-home-safety-continuity` 和 `rehabilitation-functioning` 建立边界。
