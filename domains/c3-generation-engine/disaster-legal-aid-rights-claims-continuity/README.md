# Disaster Legal Aid Rights Claims Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/disaster-legal-aid-rights-claims-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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


`disaster-legal-aid-rights-claims-continuity/` 研究灾害后的法律援助、住房租赁、保险理赔、文件替换、消费者欺诈、公共福利和家庭安全问题如何影响主体恢复。

> 核心问题：灾害后的恢复经常被法律和权利问题卡住；没有法律援助和权利解释，主体可能因租约、保险、身份文件、债务或诈骗而失去恢复机会。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体恢复不仅需要物资，还需要权利、文件、合同和制度入口可执行
  -> 灾害后租赁、保险、欺诈、福利、身份文件和家庭安全问题集中出现
  -> 法律援助把权利冲突转成可解释、可转介、可处理的恢复路径
  -> 因此灾害法律援助是主体恢复连续性的权利接口域
```

## 关注对象

- FEMA Disaster Legal Services、Legal Services Corporation disaster resources、租客/房主、保险、文件替换、消费者诈骗、福利和家庭暴力安全转介。
- 权利信息可达、低收入法律援助、语言服务、无障碍、诈骗识别、隐私和创伤知情转介。
- 与 `court-access-civil-procedure-continuity/` 的边界：该域关注日常司法访问；本域关注灾害触发的恢复法律问题。

## Human Infra 模型链路

```text
灾害法律援助系统 T
  -> 改变权利理解、文件恢复、租约保险处理、诈骗防护和转介变量 X
  -> 改变主体灾后制度防御状态 S
  -> 改变住房丧失、理赔失败、债务扩大、身份断裂和安全风险 λ(t)
  -> 影响恢复能力、资源保全和未来选择权
```

## 非目标

- 不提供法律意见、个案评估、诉讼策略、保险理赔策略、租约解释、诈骗调查或律师替代服务。
- 不收集案件事实、合同、保险单、身份文件、家庭安全信息或法律通信。
- 不替代持证律师、法律援助机构、法院、保险监管机构或公共福利机构。

## Source Signals

- FEMA Disaster Legal Services: https://www.fema.gov/assistance/individual/disaster-legal-services
- Legal Services Corporation Disaster Resources: https://www.lsc.gov/about-lsc/what-legal-aid/disaster-resources
- DisasterAssistance.gov: https://www.disasterassistance.gov/
