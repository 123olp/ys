# Prosthetic Limb Orthotic Fit Repair Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/prosthetic-limb-orthotic-fit-repair-continuity` |
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


`prosthetic-limb-orthotic-fit-repair-continuity` 研究假肢、矫形器、socket/接受腔、支具、衬垫、皮肤接口、维修、替换、成长/体重变化和支付等待如何影响移动、工作、疼痛、皮肤完整性和身份参与。

> 核心问题：假肢与矫形器不是简单外部零件，而是身体-工具耦合界面；适配、皮肤、维修和替换失败会同时损伤行动能力、疼痛负担和主体身份。

## 关注对象

- 上下肢假肢、矫形器、支具、socket、衬垫、悬吊系统、皮肤接口、维修、替换、再适配和成长变化。
- 截肢后康复、先天肢体差异、神经肌肉疾病、脊柱/关节支撑和儿童成长场景。
- 工作、学校、交通、运动、照护、皮肤风险、疼痛、疲劳和社会参与。
- 与康复、DME/假肢矫形服务、保险支付、伤口/皮肤、行动和身份连续性的接口。

## Human Infra 链路

```text
假肢矫形运行连续
  -> 主体把身体残余功能与外部支撑结构稳定耦合
  -> 不合适、皮肤损伤、疼痛、维修等待和替换断点下降
  -> 移动、工作、学校、运动和社会参与更可持续
  -> 身体自主、尊严、身份连续和未来选择权增强
```

## 非目标

- 不提供假肢/矫形器处方、socket 调整、康复训练、皮肤处理、品牌推荐、维修步骤、保险申诉或个体覆盖判断。
- 不替代假肢矫形师、康复医生、物理/作业治疗师、Medicare、MedlinePlus 或制造商说明。
- 不把设备可得性与身体身份、疼痛、皮肤和社会参与割裂处理。

## Source Signals

- Medicare Prosthetic Devices: https://www.medicare.gov/coverage/prosthetic-devices
- MedlinePlus Artificial Limbs: https://medlineplus.gov/artificiallimbs.html

## 下一步

- 建立 `prosthetic/orthotic state -> fit/skin/repair/payment dependency -> mobility/participation task -> continuity outcome` 变量表。
- 区分成人截肢、儿童成长、运动参与、工作要求、长期维护和灾害/旅行断点。
- 与 `rehabilitation-functioning`、`musculoskeletal-integrity`、`skin-barrier-wound-healing` 和 `durable-medical-equipment-supplier-repair-continuity` 建立边界。
