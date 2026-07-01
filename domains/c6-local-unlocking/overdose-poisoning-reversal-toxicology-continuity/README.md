# Overdose Poisoning Reversal Toxicology Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/overdose-poisoning-reversal-toxicology-continuity` |
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


`overdose-poisoning-reversal-toxicology-continuity/` 研究药物过量、中毒、毒物中心、解毒/逆转窗口、呼吸抑制、监测转运和恢复服务如何降低可逆毒性暴露导致的死亡。

> 核心问题：许多中毒和过量事件具有可逆窗口。主体持续性需要把毒性暴露从“无人识别的死亡”转化为可咨询、可逆转、可转运、可恢复的系统事件。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体可能被药物、化学品、酒精、阿片类或混合暴露急性终止
  -> 生存依赖早识别、毒物咨询、逆转窗口、呼吸支持、转运和后续恢复
  -> 如果没有可达毒理响应，许多可逆暴露会变成死亡或脑损伤
  -> 因此过量/中毒逆转是可逆外源性死亡风险的急性救援域
```

## 关注对象

- Poison control、overdose surveillance、naloxone access、respiratory depression、toxic exposure, antidote availability, ED transfer, linkage to treatment。
- 与 `chemical-safety-poison-control-toxicology/` 的边界：化学安全域关注毒理和风险沟通整体；本域聚焦急性中毒/过量逆转和救援窗口。
- 与 `substance-use-treatment-recovery-continuity/` 的关系：过量逆转后需要恢复和长期治疗入口。

## Human Infra 模型链路

```text
过量/中毒逆转基础设施 T
  -> 改变暴露识别、毒物咨询、逆转药可得、呼吸支持和转运变量 X
  -> 改变呼吸抑制、毒性负荷、脑缺氧、急诊转归和恢复连接状态 S
  -> 改变中毒死亡、缺氧脑损伤、复发过量和长期失能风险 λ(t)
  -> 影响主体存活、恢复入口和自主性保护
```

## 非目标

- 不提供中毒处理、剂量、解毒药、纳洛酮操作、物质使用、急救、药物相互作用或个体医疗建议。
- 不生成过量规避、药物滥用、毒物制备、检测规避、执法规避或自伤方法。
- 不收集物质使用史、用药、定位、身份、病历、急救记录或敏感法律资料。

## Source Signals

- Poison Help: https://www.poisonhelp.org/
- CDC Drug Overdose: https://www.cdc.gov/overdose-prevention/
- NIH Naloxone DrugFacts: https://nida.nih.gov/publications/drugfacts/naloxone

## 下一步

- 建立 Toxic Exposure Rescue Card：exposure type, recognition, poison center, reversal window, respiratory support, ED transfer, recovery linkage。
- 与 `chemical-safety-poison-control-toxicology/`、`substance-use-treatment-recovery-continuity/` 和 `emergency-medical-services-prehospital-care/` 建立接口。
