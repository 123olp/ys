# Glaucoma Visual Field Protection Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/glaucoma-visual-field-protection-continuity` |
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


`glaucoma-visual-field-protection-continuity/` 负责整理青光眼、视神经损伤、视野丢失、眼压管理、筛查随访和不可逆视觉损失防护。

核心问题：

> 青光眼的主体持续性风险在于慢性、隐匿、不可逆的视野压缩；一旦外周视觉和空间安全反馈丢失，移动、驾驶、跌倒防护和独立行动都会被长期削弱。

## 先验位置

```text
主体持续性最大化
  -> 主体必须保留足够视野来判断空间、危险和行动路径
  -> 青光眼可在症状明显前造成不可逆视神经损伤
  -> 视野压缩会降低移动安全、驾驶能力、环境扫描和独立生活
  -> 因此青光眼视野保护连续性是视觉输入长期防损路径
```

## 关注对象

- 青光眼、眼压、视神经损伤、视野缺损、早期发现和长期随访。
- 治疗连续性、检查可及性、用药/激光/手术路径的证据边界和依从摩擦。
- 驾驶、跌倒、空间导航、工作安全和照护需求。
- 与 `vision-eye-health-continuity/` 的关系：本域聚焦不可逆视野丢失和长期监测连续性。

## Human Infra 模型链路

```text
青光眼筛查 / 随访 / 风险控制 T
  -> 改变眼压、视神经状态、视野、检查频率和治疗连续性变量 X
  -> 改变主体空间扫描、移动安全、驾驶和环境风险识别状态 S
  -> 改变跌倒、事故、失明、照护依赖和职业任务失败风险
  -> 保护行动半径、独立生活和未来选择权
```

## 非目标

- 不提供青光眼诊断、眼压解释、视野报告判读、药物选择、手术建议或个体治疗计划。
- 不根据视野或眼压资料判断驾驶、工作、活动或保险资格。
- 不把早筛宣传成确定预防失明；必须保留假阳性、随访、可及性和个体差异边界。

## Source Signals

- National Eye Institute Glaucoma: https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/glaucoma
- CDC Vision Health: https://www.cdc.gov/vision-health/
- WHO Blindness and visual impairment: https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment

## 下一步

- 建立青光眼 Source Card，区分视野变量、服务连续性、治疗依从摩擦和主体功能终点。
- 对接跌倒预防、驾驶移动、用药连续性和低视力康复域。
