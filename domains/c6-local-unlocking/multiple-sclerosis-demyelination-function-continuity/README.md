# Multiple Sclerosis Demyelination Function Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/multiple-sclerosis-demyelination-function-continuity` |
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


`multiple-sclerosis-demyelination-function-continuity/` 研究多发性硬化、脱髓鞘、复发缓解、疲劳、感觉运动障碍、认知变化和长期功能连续性如何影响主体持续性。

## Core Question

当中枢神经髓鞘损伤造成复发、残留损害和疲劳时，主体如何维持学习、工作、移动、认知节律、服务接入和长期适配能力？

## 先验位置

- 与 `neuro-continuity/` 的关系：MS 是免疫介导的中枢脱髓鞘病程，需要独立于急性神经事件处理。
- 与 `immune-maintenance/` 的关系：免疫调节与感染风险、妊娠阶段和用药监测存在独立边界。
- 与 `functioning-quality-of-life-outcomes/` 的关系：疲劳和认知变化常比单一病灶更能解释有效时间损耗。

## 关注对象

- 复发、进展、疲劳、感觉/运动症状、视力、疼痛、认知、情绪、热敏感、工作适配和照护连续性。
- 专科可及、影像/检查边界、疾病修饰治疗可及、长期监测和失能权益接口。

## Human Infra 模型链路

```text
脱髓鞘与神经炎症
-> 复发、残留损害、疲劳和认知负担
-> 学习、工作、移动、恢复和社会参与能力波动
-> 长期项目不确定性和服务需求增加
-> 主体持续性下降
```

## 非目标

- 不提供 MS 诊断、MRI/腰穿/化验判读、药物、免疫治疗、妊娠、疫苗、复发处理或康复建议。
- 不输出个体预后、失能等级、工作许可、保险或福利资格判断。

## Source Signals

- NINDS multiple sclerosis: https://www.ninds.nih.gov/health-information/disorders/multiple-sclerosis

## 下一步

- 建立 demyelination burden card：区分复发、进展、疲劳、认知和服务连续性变量。
