# Medication Reconciliation Regimen Adherence Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/medication-reconciliation-regimen-adherence-continuity` |
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


## 定位

本域研究用药核对、药历一致性、过渡期 medication reconciliation、服药计划、依从性、治疗负担和多药协调如何决定药品是否被主体正确、持续、可承受地使用。

它不是个体用药管理、停药、加药、剂量调整或健康建议入口。

## 先验问题

```text
药物进入家庭后何以继续有效？
  -> 用药清单必须准确
  -> 多个医生、药房和照护者必须共享一致药历
  -> 主体必须能按计划执行并处理漏服、冲突和副作用信号
  -> 否则药物可得性会退化为混乱和风险
```

## 研究对象

- Medication reconciliation、处方变更、出院用药、转诊和长期照护交接。
- 依从性、持药天数、refill gap、pill burden、复杂给药频率。
- 照护者、药师、电子药历、药盒、提醒和用药教育。
- 多病共存、多重用药、治疗负担和 deprescribing 研究边界。

## 关键变量

- 药历一致率、用药差错、PDC/MPR、refill gap、漏服率。
- 过渡期用药冲突、重复治疗、禁忌组合和未说明停药。
- 治疗负担、日常执行成本、照护者参与和理解度。

## 证据入口

- AHRQ medication reconciliation 与 patient safety 资料。
- CDC、FDA、ISMP 和药学组织的 medication safety 公开资料。
- 多病共存、多重用药和依从性研究。

## 非目标

- 不提供具体服药时间、剂量、漏服处理、停药、替换或药物相互作用判断。
- 不生成个人 medication list、药历、处方核对表或照护计划。
- 不收集药名、剂量、诊断、处方、药房、医生、照护者或健康数据。

## 上下游

- 上游：`retail-pharmacy-prescription-dispensing-continuity/`、`care-transitions-discharge-continuity/`、`multimorbidity-polypharmacy-care-coordination/`。
- 下游：`patient-safety-organizational-learning/`、`pharmacovigilance-drug-safety-monitoring/`、`time-allocation-effective-time/`。
