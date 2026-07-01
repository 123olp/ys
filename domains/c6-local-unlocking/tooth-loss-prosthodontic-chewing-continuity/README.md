# Tooth Loss Prosthodontic Chewing Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/tooth-loss-prosthodontic-chewing-continuity` |
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


`tooth-loss-prosthodontic-chewing-continuity/` 负责整理缺牙、修复义齿、咀嚼效率、营养和社会参与连续性。

核心问题：

> 缺牙不是外观问题；它会改变咀嚼、饮食选择、说话、面部支撑、社交尊严和长期照护负担。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能以可承受成本摄入营养、表达和参与社会
  -> 牙齿数量、咬合支持和修复稳定性决定咀嚼效率
  -> 缺牙和修复失败会导致饮食受限、营养风险、社交退缩和照护依赖
  -> 因此缺牙与修复连续性是有效时间和尊严持续的功能条件
```

## 关注对象

- 缺牙、无牙颌、义齿、种植修复、固定/活动修复和维护负担。
- 咀嚼效率、饮食多样性、营养、言语、面部支撑、社交和自尊。
- 老年照护、低收入人群、护理机构、交通和保险费用导致的修复可及性问题。
- 与 `nutrition-metabolic-health/` 的关系：本域关注口腔输入通道；营养域关注代谢和摄入质量。

## Human Infra 模型链路

```text
缺牙修复 / 咀嚼支持 T
  -> 改变牙列完整性、咀嚼效率、言语、社交、营养选择和维护成本变量 X
  -> 改变主体摄食、沟通和资源状态 S
  -> 改变营养不足、社交退缩、照护依赖和任务执行受限风险
  -> 增加有效时间、生活质量和行动密度
```

## 非目标

- 不提供种植、义齿、冠桥或任何修复方案选择建议。
- 不做咬合设计、影像判读、手术路径、材料选择或费用承诺。
- 不替代牙医、修复专科、口腔外科或营养专业评估。

## Source Signals

- WHO Oral Health: https://www.who.int/news-room/fact-sheets/detail/oral-health
- CDC Oral Health: https://www.cdc.gov/oral-health/
- NIDCR Older Adults and Oral Health: https://www.nidcr.nih.gov/health-info/older-adults

## 下一步

- 建立缺牙到营养、沟通、尊严和照护依赖的变量表。
- 与老年口腔、牙周病、龋病和服务可及性域建立交叉索引。
