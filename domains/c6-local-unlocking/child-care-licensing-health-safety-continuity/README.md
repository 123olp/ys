# Child Care Licensing Health Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/child-care-licensing-health-safety-continuity` |
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


`child-care-licensing-health-safety-continuity/` 研究托育许可、检查、健康安全标准、人员比例、背景审查和应急准备如何把“有人看护”转化为可审查的儿童照护安全。

> 核心问题：托育可及不能以儿童安全为代价；许可、健康安全、检查和信息透明是家庭信任和儿童发展连续性的底层护栏。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 儿童照护必须同时满足可达和安全
  -> 家庭需要可信信息判断照护环境风险
  -> 许可、检查、健康安全标准和事件报告必须可审查
  -> 儿童健康、照护者信任和家庭运行才不会被隐性风险破坏
```

## 关注对象

- 托育许可、检查记录、健康与安全标准、人员资质、儿童-成人比例、背景审查和安全睡眠。
- 疾病暴露、事故预防、应急计划、报告机制、家长信息透明和监管执行。
- 与 `childcare-family-continuity/`、`child-protection-family-safety/`、`infant-safe-sleep-suid-risk-reduction-continuity/` 和 `toy-small-parts-choking-ingestion-continuity/` 的接口。

## Human Infra 模型链路

```text
托育服务使用
  -> 许可、检查、健康安全标准和事件透明
  -> 儿童伤害、感染和照护失效风险下降
  -> 家庭信任、照护连续性和工作学习连续性提高
  -> 儿童主体与照护者主体的长期选择权增加
```

## 非目标

- 不认证、评级、推荐或背书任何托育机构。
- 不解释个体检查记录、事故责任、儿童症状、伤害处置或法律合规结论。
- 不收集儿童照片、事故材料、机构投诉、医疗记录、监控影像或身份信息。

## Source Signals

- ChildCare.gov: https://childcare.gov/
- ACF Office of Child Care: https://www.acf.hhs.gov/occ
- Child Care and Development Fund: https://www.acf.hhs.gov/occ/programs/ccdf
- CDC Child Development: https://www.cdc.gov/child-development/

## 下一步

- 建立变量表：许可状态、检查频率、健康安全标准、人员比例、背景审查、事件报告和应急计划。
- 整理 ChildCare.gov、ACF OCC、CCDF 和 CDC 儿童发展资料 Source Cards。
- 与产品安全、儿童保护和家庭伤害预防域明确边界。
