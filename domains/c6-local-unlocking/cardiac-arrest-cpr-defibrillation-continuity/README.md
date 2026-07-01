# Cardiac Arrest CPR Defibrillation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/cardiac-arrest-cpr-defibrillation-continuity` |
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


`cardiac-arrest-cpr-defibrillation-continuity/` 研究心脏骤停识别、旁观者 CPR、AED/除颤、调度、院前复苏和复苏后转运如何决定主体是否能从突然死亡边界返回。

> 核心问题：心脏骤停不是慢性风险，而是分钟级主体中断事件。有效永生需要把突然终止事件转化为可识别、可响应、可逆转的救援链。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体可能被心脏骤停在分钟内终止
  -> 生存依赖识别、呼救、CPR、除颤、EMS 和复苏后照护连续
  -> 任一环节延迟都会显著压缩可逆窗口
  -> 因此心脏骤停 CPR 与除颤是主体突发中断风险的急性救援域
```

## 关注对象

- Chain of survival、旁观者 CPR、AED 可达性、调度辅助 CPR、EMS response、ROSC、复苏后照护和神经结局。
- 公共场所 AED、社区培训、数据登记、质量改进、院前到院内交接、复苏系统绩效。
- 与 `emergency-medical-services-prehospital-care/` 的边界：EMS 域关注院前系统整体；本域聚焦心脏骤停这一分钟级死亡边界。
- 与 `cerebrovascular-stroke-brain-perfusion-resilience/` 的关系：心脏骤停救援最终也服务脑灌注和神经连续性。

## Human Infra 模型链路

```text
心脏骤停救援基础设施 T
  -> 改变识别时间、CPR 启动、AED 可达、除颤时间和转运变量 X
  -> 改变复苏成功、脑灌注、复苏后恢复和残障状态 S
  -> 改变突发死亡、缺氧脑损伤和长期失能风险 λ(t)
  -> 影响主体继续存在、认知连续性和未来选择权
```

## 非目标

- 不提供个人急救、CPR 操作教学、AED 操作指令、复苏决策、预后判断、药物或医疗建议。
- 不输出替代急救电话、EMS、AHA/红十字培训、医生或官方急救指南的内容。
- 不收集个案心电图、急救记录、定位、身份、医疗史或复苏视频。

## Source Signals

- American Heart Association Chain of Survival: https://cpr.heart.org/en/resources/cpr-facts-and-stats/out-of-hospital-chain-of-survival
- AHA Guidelines for CPR and ECC: https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines
- CDC Cardiac Arrest Registry to Enhance Survival: https://www.cdc.gov/heart-disease/php/data-research/cardiac-arrest-registry-to-enhance-survival.html

## 下一步

- 建立 Cardiac Arrest Rescue Card：recognition, call, CPR, AED, EMS, ROSC, post-arrest care, neurological outcome。
- 与 `emergency-medical-services-prehospital-care/`、`cerebrovascular-stroke-brain-perfusion-resilience/` 和 `intensive-care-organ-support-delirium-continuity/` 建立急性救援链路。
