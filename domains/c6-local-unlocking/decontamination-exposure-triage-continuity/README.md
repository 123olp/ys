# Decontamination Exposure Triage Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/decontamination-exposure-triage-continuity` |
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


`decontamination-exposure-triage-continuity/` 研究危险材料暴露后的去污入口、医疗分流、医院准备、隐私尊严、衣物/财物处理、心理压力和家庭重聚如何影响主体恢复。

> 核心问题：去污和分诊如果只被看成技术动作，会忽略人的尊严、照护依赖、语言理解、残障需求、医院二次污染和家庭接续。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 暴露后主体需要从危险现场转入医疗和恢复系统
  -> 去污、分诊、转运、信息记录和家庭重聚决定伤害是否被放大
  -> 暴露后连续性把污染控制、医疗入口和人的尊严接在一起
```

## 关注对象

- 去污入口、暴露分流、医院去污准备、二次污染风险、衣物/财物、隐私、语言、残障、儿童和家庭重聚。
- 与 `overdose-poisoning-reversal-toxicology-continuity/` 的关系：中毒逆转域关注急性毒性救援窗口；本域关注危险材料暴露后的系统入口和分流连续性。

## Human Infra 模型链路

```text
暴露后去污与分诊连续性
  -> 改变二次污染、就医延迟、尊严损害、家庭断裂和医疗挤兑
  -> 改变急性伤害、长期功能损失、信任和恢复速度
  -> 支撑主体从事故暴露回到可行动状态
```

## 非目标

- 不提供去污步骤、暴露处理、化学品急救、医疗分诊、医院流程设计或现场操作。
- 不提供个体诊断、解毒、药物、剂量、采样、证据保存或法律建议。
- 不提供规避去污、规避医疗、隐藏暴露、污染转移或危险材料处置方法。

## Source Signals

- HHS CHEMM: https://chemm.hhs.gov/
- ATSDR Medical Management Guidelines: https://wwwn.cdc.gov/TSP/MMG/
- OSHA HAZWOPER decontamination context: https://www.osha.gov/hazwoper
- ASPR TRACIE hospital preparedness resources: https://asprtracie.hhs.gov/

## 下一步

- 建立 Exposure Triage Card：exposure context, decontamination interface, medical referral, dignity/privacy, family reunification, hospital surge。
- 与 `healthcare-surge-triage-capacity-continuity/`、`emergency-medical-services-prehospital-care/` 和 `language-access-plain-communication/` 建立接口。
