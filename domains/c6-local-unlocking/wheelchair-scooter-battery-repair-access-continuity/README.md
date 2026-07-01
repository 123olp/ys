# Wheelchair Scooter Battery Repair Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/wheelchair-scooter-battery-repair-access-continuity` |
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


`wheelchair-scooter-battery-repair-access-continuity` 研究手动轮椅、电动轮椅、代步车、电池/充电器、维修、备件、供应商响应、运输适配和备用行动方案如何影响移动、照护、医疗、工作、学校和撤离连续性。

> 核心问题：轮椅和代步车是行动能力的外部底盘；设备断电、损坏、维修等待或运输不兼容，会把身体功能限制放大成服务不可达和主体被困。

## 关注对象

- 手动轮椅、电动轮椅、代步车、坐垫、轮胎、刹车、控制器、电池、充电器和维修/替换等待。
- 家庭、街道、公共交通、paratransit、医疗预约、学校、工作场所和灾害撤离中的设备依赖。
- 供应商网络、备件、维修授权、运输装载、电梯/坡道接口和备用设备。
- 与 DME、无障碍建成环境、个人照护、应急准备和残障权利的接口。

## Human Infra 链路

```text
轮椅/代步设备运行连续
  -> 主体能把身体能力与外部移动底盘稳定耦合
  -> 断电、损坏、维修等待和运输断点减少
  -> 医疗、工作、教育、社区和撤离行动更可达
  -> 独立性、尊严、照护效率和未来选择权增强
```

## 非目标

- 不提供轮椅处方、坐姿评估、设备改装、维修步骤、品牌推荐、购买建议、保险申诉或个体 DME 覆盖判断。
- 不替代康复医生、物理/作业治疗师、DME 供应商、Medicare、Medicaid、交通机构或制造商说明。
- 不把设备运行问题简化为个人习惯问题；供应商、支付、环境和交通接口必须同时审查。

## Source Signals

- Medicare Wheelchairs and Scooters: https://www.medicare.gov/coverage/wheelchairs-scooters
- MedlinePlus Mobility Aids: https://medlineplus.gov/mobilityaids.html

## 下一步

- 建立 `device state -> power/repair/supplier dependency -> mobility task -> participation consequence` 变量表。
- 区分手动轮椅、电动轮椅、代步车、短期伤病、长期残障、老年照护和灾害撤离场景。
- 与 `durable-medical-equipment-supplier-repair-continuity`、`paratransit-nemt-access-continuity` 和 `built-environment-accessibility-universal-design` 建立边界。
