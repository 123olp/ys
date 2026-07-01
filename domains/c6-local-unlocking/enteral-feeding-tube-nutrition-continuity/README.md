# Enteral Feeding Tube Nutrition Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/enteral-feeding-tube-nutrition-continuity` |
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


Enteral feeding tube nutrition continuity studies non-oral nutrition pathways when swallowing or intake is insufficient, focusing on nutrition delivery continuity, device dependence, infection risk, caregiver burden, dignity, and decision boundaries.

核心问题：

> 管饲不是“营养自动解决”，而是把营养入口转移到设备、护理、供应、并发症和决策权共同维护的外部系统。

## 先验位置

```text
主体持续性最大化
  -> 主体必须持续获得水分、能量和药物
  -> 口服路径不足时可能需要非口服营养通道
  -> 管路、配方、泵、护理、感染和供应链成为新的单点失效
  -> 因而管饲营养连续性是吞咽失败后的外部入口基础设施
```

## 关注对象

- 鼻胃管、胃造瘘、肠造瘘、配方供应、管路维护、泵、感染、堵管、照护者负担和意愿决策。
- 与 `nutrition-metabolic-health/` 的关系：营养域关注营养状态；本域关注管饲入口和执行链。
- 与 `advance-care-planning-medical-decision-continuity/` 的关系：决策域关注意愿和代理；本域只整理管饲作为研究对象。

## Human Infra 模型链路

```text
营养评估 / 管饲路径 / 供应链 / 护理流程 T
  -> 改变能量水分进入、设备依赖、感染风险和照护负担变量 X
  -> 改变营养状态、家庭执行、尊严和医疗依赖状态 S
  -> 改变营养不足、脱水、感染、住院和照护崩溃风险 λ(t)
  -> 影响恢复能力、主体自主性和未来选择权
```

## 非目标

- 不提供管饲适应证、置管选择、配方、速率、冲管、护理、并发症处理或伦理决策建议。
- 不根据个体吞咽、体重、疾病、管路或营养数据判断是否需要管饲。
- 不替代营养、胃肠、外科、护理、言语语言治疗、伦理咨询或临床服务。

## Source Signals

- ASPEN / ESPEN enteral nutrition guideline materials as professional context。
- MedlinePlus feeding tube public medical materials。
- Long-term care and home health literature as implementation context。
