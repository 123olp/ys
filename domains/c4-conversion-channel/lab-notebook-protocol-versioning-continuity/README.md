# Lab Notebook, Protocol and Versioning Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/lab-notebook-protocol-versioning-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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


## Scope

This domain studies lab notebooks, protocols, versioned methods, provenance, timestamping, protocol sharing and method drift.

Human Infra treats protocol continuity as the bridge between evidence and action: if methods are not preserved and versioned, later researchers cannot distinguish failed replication from changed procedure.

## Human Infra Chain

```text
experiment or procedure is performed
  -> result depends on materials, method, timing, environment and deviations
  -> lab notebooks and versioned protocols preserve procedural context
  -> replication, audit, troubleshooting and translation become possible
  -> evidence quality improves before it enters models or public claims
  -> research systems gain memory and error-correction capacity
```

## Non-Goals

- No wet-lab operating protocol, biosafety procedure, clinical procedure or dual-use method instruction.
- No advice on falsifying notebooks, backdating records or bypassing quality systems.
- No storage of confidential lab records, proprietary protocols, patient samples or human-subject records.
- No claim that a protocol record proves the experiment was performed correctly.

## Source Signals

- protocols.io: https://www.protocols.io/
- NIH rigor and reproducibility resources: https://grants.nih.gov/policy/reproducibility/index.htm
- FDA data integrity and compliance resources: https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/compliance-resources
- Open Science Framework: https://osf.io/

## Next Notes

- Define safe protocol metadata fields without operational hazardous details.
- Connect to biobanking chain of custody, instrumentation calibration and research software reproducibility.
- Track version drift, material substitutions, timestamp integrity and deviation disclosure.
