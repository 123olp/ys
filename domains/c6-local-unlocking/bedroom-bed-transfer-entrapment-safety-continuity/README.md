# Bedroom Bed Transfer Entrapment Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/bedroom-bed-transfer-entrapment-safety-continuity` |
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


`bedroom-bed-transfer-entrapment-safety-continuity/` 研究床、卧室布局、起身转移、床边空间、床栏/床扶手、夹陷、夜间护理和睡眠表面如何影响主体休息与行动转换。

> 核心问题：床是恢复入口，也是起身、跌倒、夹陷和照护交接入口。睡眠恢复若不能安全转回站立行动，恢复就会在转移瞬间失效。

## 先验位置

```text
主体需要通过睡眠恢复
  -> 睡眠后必须从躺卧状态安全转回坐、站、行走和照护交接
  -> 卧室空间、床高、扶手、照明和夹陷风险会影响转换
  -> 因而卧室和床转移是恢复系统与行动系统之间的接口
```

## 关注对象

- 床高、床边空间、床栏、床扶手、床垫/床架、夹陷风险、夜间起身、照护者转移、卧室路径和呼叫/提醒。
- 老年人、儿童、认知受限、术后恢复、长期照护、失眠/夜尿和移动受限场景。

## Human Infra 模型链路

```text
卧室与床转移环境 T
  -> 改变床高、空间、扶手、夹陷、照明和呼叫接口 X
  -> 改变睡眠恢复、起身、转移和照护交接状态 S
  -> 改变跌倒、夹陷、睡眠破坏、照护者损伤和机构化风险 λ(t)
  -> 改变恢复质量、独立生活和未来选择权
```

## 非目标

- 不提供床、床栏、床垫、护理床、监测设备、转移技巧、护理动作、产品购买、施工、监管合规或个体安全建议。
- 不收集卧室照片、床位信息、睡眠记录、摄像头资料、认知状态、跌倒史或护理记录。

## Source Signals

- CPSC adult portable bed rail and entrapment safety materials.
- CDC / NIA fall prevention and home safety materials.
- FDA hospital bed system safety materials as boundary reference.
