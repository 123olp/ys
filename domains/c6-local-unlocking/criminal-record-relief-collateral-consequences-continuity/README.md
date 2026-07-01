# Criminal Record Relief Collateral Consequences Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/criminal-record-relief-collateral-consequences-continuity` |
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


本域研究犯罪记录、逮捕记录、定罪记录、封存/清除、记录更正、附带后果和重返社会资格如何影响主体工作、住房、教育、证照、投票、家庭和服务接入。

> 核心问题：惩罚常常不止于判决本身；记录和附带后果会在多年后继续影响任务执行资源、社会连接和未来选择权。记录救济连续性关注的是主体如何从长期制度性尾部风险中恢复。

## 关注对象

- 刑事记录、逮捕记录、定罪记录、封存、清除、赦免、记录更正、自动清除和 clean slate。
- 附带后果：就业、住房、职业证照、教育、金融、投票、移民、家庭法、福利和公共服务限制。
- 与 `background-check-record-screening-continuity/` 的边界：背景筛查域关注第三方筛查和报告使用；本域关注记录救济、附带后果和重返资格。
- 记录质量、身份匹配、错误记录、跨辖区传播、算法筛查、申诉路径和反歧视保护。

## Human Infra 链路

```text
犯罪记录救济 / 附带后果连续性
  -> 记录、限制和恢复路径被准确识别、可更正、可审查
  -> 工作、住房、教育、证照、家庭、投票和服务入口不被无限期尾部风险切断
  -> 重返社会和长期任务执行资源恢复
  -> 主体从过去事件中重新获得未来选择权
```

## 非目标

- 不提供刑事案件、封存、清除、赦免、上诉、投票恢复、移民、就业、住房、证照或法律建议。
- 不判断个人是否有资格获得记录救济或如何处理具体背景调查结果。
- 不指导隐藏身份、伪造记录、绕过背景调查、欺骗雇主/房东/机构或骚扰记录主体。

## Source Signals

- National Inventory of Collateral Consequences of Conviction: https://niccc.nationalreentryresourcecenter.org/
- Bureau of Justice Assistance National Reentry Resource Center: https://nationalreentryresourcecenter.org/
- Bureau of Justice Statistics Criminal Justice Data: https://bjs.ojp.gov/

## 下一步

- 建立记录救济变量表：记录类型、记录质量、附带后果、救济路径、自动化清除、身份匹配、跨辖区传播和反歧视边界。
- 整理 NICCC、BJA NRRC、BJS、Clean Slate、Legal Services 和 state court record relief Source Cards。
- 与 `background-check-record-screening-continuity/` 明确分工：筛查域研究记录如何被使用，本域研究记录如何被纠错、限制、清除和恢复权利。
