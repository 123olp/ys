# Urinary Diversion, Urostomy and Supplies Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/urinary-diversion-urostomy-supplies-continuity` |
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


`urinary-diversion-urostomy-supplies-continuity/` 研究尿流改道、尿路造口、造口袋/皮肤屏障供应、皮肤并发症、身体形象和照护训练如何影响主体持续性。

> 核心问题：尿流改道能维持排泄出口，但它把排泄连续性外部化为耗材、皮肤、训练、隐私、旅行和保险供应链问题。

## 先验位置

```text
有效永生
  -> 主体需要可持续排泄出口
  -> 原生尿路不可用时，出口被改造为外部设备系统
  -> 因此尿路造口是排泄系统外部化后的供应链与尊严域
```

## 关注对象

- Urinary diversion, urostomy, ostomy pouching systems, skin barrier, leakage, supplies, body image, travel, insurance and long-term care training。
- 与 `durable-medical-equipment-supplier-repair-continuity/` 的关系：DME 域关注设备供应总框架，本域关注尿流改道特有的排泄与皮肤接口。

## Human Infra 模型链路

```text
尿路造口供应与照护训练 T
  -> 改变耗材可得性、皮肤完整性、泄漏、气味、隐私和旅行能力 X
  -> 改变排泄安全、社交参与、工作可靠性和身体形象 S
  -> 改变感染、皮肤损伤、照护依赖和有效时间损失 lambda(t)
  -> 改变独立生活和未来选择权
```

## 非目标

- 不提供造口护理步骤、产品推荐、皮肤问题处理、手术选择、保险申诉或个体医疗建议。
- 不输出个人供应清单、旅行方案、感染判断、伤口判断或护理责任结论。

## Source Signals

- NIDDK urinary diversion materials.
- MedlinePlus urostomy public materials.
- United Ostomy Associations of America public education materials.
