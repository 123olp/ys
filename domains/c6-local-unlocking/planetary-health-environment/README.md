# Planetary Health And Environment

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/planetary-health-environment` |
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


Planetary Health And Environment 负责整理空气、水、气候、生态系统、污染、热风险、食物系统和自然环境对主体持续性的影响。

核心问题：

> 主体依赖环境系统；如果空气、水、气候、生态和食物系统失稳，个体技术无法单独维持主体持续性。

## 先验位置

```text
主体持续性最大化
  -> 主体必须依赖空气、水、食物、温度和生态系统服务
  -> 环境退化会增加疾病、灾害、迁移、资源断裂和死亡风险
  -> 个体层面的健康技术无法替代外部环境底座
  -> 因此星球健康与环境是主体持续性的宏观条件
```

## 关注对象

- 空气污染、水质、热风险、气候变化、极端天气、生态系统和食物系统。
- 环境暴露、社区韧性、迁移、公共健康和长期风险函数。
- 与 `risk-engineering/` 和 `resource-social-infra/` 的关系：环境是风险和资源的上游条件。

## Human Infra 模型链路

```text
环境条件 T
  -> 改变污染暴露、热暴露、水食物安全和灾害风险 X
  -> 改变主体外部生存状态 S
  -> 改变呼吸、心血管、感染、营养、迁移和灾害死亡风险 λ(t)
  -> 改变长期健康寿命和未来选择权
```

## 非目标

- 不把环境风险归咎于个人选择。
- 不提供危险环境规避违法建议。
- 不把单一环境指标等同于完整生态和公共健康风险。

## Source Signals

- WHO Air Pollution: https://www.who.int/health-topics/air-pollution
- Lancet Planetary Health: https://www.thelancet.com/journals/lanplh/home
