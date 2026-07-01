# Trenching Excavation Cave-In Worker Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/trenching-excavation-cave-in-worker-continuity` |
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


`trenching-excavation-cave-in-worker-continuity/` 研究沟槽开挖、土方作业、坍塌埋压、地下设施接口、积水和救援延迟如何影响工作者主体持续性。

核心问题：

> 当主体为了建设、维修和地下基础设施工作进入开挖环境时，能否不把劳动任务转换成窒息、挤压伤、死亡和家庭恢复成本。

## 先验位置

```text
有效永生 / 主体持续性
  -> 主体需要通过建设、维修和地下基础设施工作获取资源
  -> 沟槽和开挖把主体置于坍塌、埋压、地下设施和救援延迟窗口
  -> 坍塌会快速造成窒息、挤压伤、创伤和死亡
  -> 因此沟槽开挖安全是工作持续性的基础执行条件
```

## 关注对象

- Trenching、excavation、cave-in、soil collapse、protective-system evidence boundary、spoil pile、water accumulation、underground utility interface、rescue latency。
- 风险链：开挖任务 -> 土体失稳 -> 坍塌埋压 -> 窒息/挤压伤/死亡 -> 收入、照护和家庭恢复冲击。
- 制度链：hazard identification、competent-person interface、utility locating、inspection record、incident reporting、emergency handoff。

## Human Infra 模型位置

```text
沟槽/开挖任务 T
  -> 改变坍塌暴露 X
  -> 改变身体完整性和救援可达状态 S
  -> 改变急性死亡/挤压伤风险 lambda(t)
  -> 改变有效工作年限、收入连续性和未来选择权
```

## 非目标

- 不提供沟槽设计、开挖方案、支护、放坡、台阶、盾构箱、土壤分类、地下设施定位、救援、许可、施工、合规或现场安全方案。
- 不判断个人工伤、责任、赔偿、复工、事故调查、OSHA 违规或法律策略。
- 不帮助规避安全规则、隐藏事故、绕开培训、替代雇主安全计划或现场专业人员。

## Source Signals

- OSHA Trenching and Excavation: https://www.osha.gov/trenching-excavation
- OSHA Workers: https://www.osha.gov/workers

## 下一步

- 建立 Trenching Continuity Card：cave-in exposure、depth class、protective-system evidence、competent-person interface、water/utility interface、rescue latency、incident reporting。
- 与 `occupational-exposure-industrial-hygiene/`、`workers-compensation-occupational-injury-benefit-continuity/` 和 `trauma-system-hemorrhage-control-continuity/` 建立接口。
