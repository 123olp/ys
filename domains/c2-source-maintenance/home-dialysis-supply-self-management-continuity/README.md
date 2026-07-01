# Home Dialysis Supply and Self-Management Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/home-dialysis-supply-self-management-continuity` |
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


`home-dialysis-supply-self-management-continuity/` 研究家庭血透、腹膜透析、耗材配送、用水/用电、训练、照护者负担、远程监测和灾害中断如何影响主体持续性。

> 核心问题：家庭透析把医院能力迁移到家庭，但同时把供应链、训练、住房、卫生、电力、水和照护者能力变成生命支持接口。

## 先验位置

```text
有效永生
  -> 外部清除能力必须长期可达
  -> 家庭化治疗把清除系统迁移到居住环境
  -> 因此家庭透析是医疗能力家庭化后的供应与执行域
```

## 关注对象

- Home hemodialysis, peritoneal dialysis, supply delivery, training, caregiver workload, water/electricity dependence, infection control, disaster interruption, remote support。
- 与 `dialysis-access-vascular-peritoneal-continuity/` 的关系：通路域关注身体接口，本域关注家庭执行系统和供应链。

## Human Infra 模型链路

```text
家庭透析执行系统 T
  -> 改变耗材、训练、电水依赖、感染控制、远程支持和照护负担 X
  -> 改变清除稳定性、居住可行性、家庭压力和行动自由 S
  -> 改变治疗中断、住院、感染、照护崩溃和死亡风险 lambda(t)
  -> 改变独立生活、有效时间和未来选择权
```

## 非目标

- 不提供家庭透析资格、参数、操作、用品购买、消毒、故障处理、饮食/用药或个体治疗建议。
- 不输出个人居家适配、灾害应对、设备维修、保险或供应商选择建议。

## Source Signals

- NIDDK peritoneal dialysis and hemodialysis materials.
- National Kidney Foundation home dialysis materials.
- CMS ESRD and dialysis facility public materials.
