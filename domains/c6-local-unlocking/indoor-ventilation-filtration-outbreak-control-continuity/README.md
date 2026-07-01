# Indoor Ventilation Filtration Outbreak Control Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/indoor-ventilation-filtration-outbreak-control-continuity` |
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


`indoor-ventilation-filtration-outbreak-control-continuity/` 研究暴发场景中的室内通风、过滤、空气净化、CO2 代理指标和建筑运营如何降低感染传播并维持任务执行。

> 核心问题：室内空气是共享基础设施；暴发时，它决定学校、工作、照护和公共服务能否以较低传播风险继续运行。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体长期行动大量发生在室内空间
  -> 空气传播暴发会把室内空间变成风险放大器
  -> 通风和过滤把空间本身改造为降低传播风险的基础设施
```

## 关注对象

- 通风、过滤、空气净化、HVAC 运行、CO2 代理指标、学校/工作场所室内空气策略、维护责任和公平可达。
- 与 `air-quality-ventilation-exposure-control/` 的关系：上位域关注空气暴露治理；本域聚焦传染病暴发时的室内空气控制执行。

## Human Infra 模型链路

```text
室内通风与过滤控制
  -> 改变室内空气交换、过滤、污染物稀释和感染暴露概率
  -> 改变学校、工作、照护、公共服务和医疗空间的开放风险
  -> 降低停课停工、感染扩散和长期健康负担
  -> 增强有效时间、公共空间信任和主体持续性
```

## 非目标

- 不提供 HVAC 设计、施工、维修、设备采购、滤材安装、现场调试或职业合规建议。
- 不提供个体感染风险计算、场所安全认证、实时开放建议或法律责任判断。
- 不把通风资料写成替代口罩、检测、疫苗或隔离的单一方案。

## Source Signals

- CDC ventilation in buildings: https://www.cdc.gov/covid/php/building-water-system/ventilation.html
- EPA indoor air quality: https://www.epa.gov/indoor-air-quality-iaq
- ASHRAE epidemic resources: https://www.ashrae.org/technical-resources/resources
- WHO ventilation roadmap and IPC resources: https://www.who.int/

## 下一步

- 建立变量表：通风率、过滤等级、空气净化、CO2 代理指标、维护状态、空间拥挤、能耗和公平差异。
- 与 `school-workplace-outbreak-operations-continuity/`、`mask-respirator-source-control-fit-access-continuity/` 和 `building-fire-life-safety-codes/` 建立接口。
