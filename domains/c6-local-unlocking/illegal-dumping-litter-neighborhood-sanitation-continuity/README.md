# Illegal Dumping Litter Neighborhood Sanitation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/illegal-dumping-litter-neighborhood-sanitation-continuity` |
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


`illegal-dumping-litter-neighborhood-sanitation-continuity` 研究非法倾倒、乱扔垃圾、废旧家具/轮胎/床垫堆积、巷道空地卫生、举报入口、清理延迟和邻里环境质量如何影响行动安全、害虫风险、财产价值、心理压力和公共信任。

> 核心问题：废弃物治理失败不只发生在家庭内部；当公共或邻里空间被非法倾倒占据，步行、儿童活动、住房稳定、社区信任和公共卫生都会被外部残余物侵蚀。

## 关注对象

- 非法倾倒、乱扔垃圾、废旧家具、床垫、轮胎、建筑废料、巷道/空地堆积、路边长期未清物和热点地图。
- 举报入口、清理责任、执法边界、环境正义、害虫/火灾/受伤风险、邻里污名化和清理延迟。
- 低收入社区、多户住宅周边、搬家/驱逐/拆迁后废弃物、无车家庭、公共空间通行和儿童活动场景。
- 与家庭固废收运、大件收运、危险废物、灾后碎片、公共卫生和社区韧性的接口。

## Human Infra 链路

```text
非法倾倒、乱扔垃圾与邻里卫生连续
  -> 邻里空间中的异常废弃物能被发现、报告、归责和清理
  -> 害虫、火灾、受伤、污名化、通行障碍和环境不公风险下降
  -> 步行、儿童活动、住房稳定、社区信任和恢复空间保持可用
  -> 主体公共行动半径、心理安全和社区韧性提高
```

## 非目标

- 不提供非法倾倒、规避监控、规避执法、私自清理危险废物、现场取证对抗、邻里冲突升级或个案法律策略。
- 不替代地方固废部门、311/举报系统、环境执法、物业、公共卫生、消防、警务、灾后清理或法律渠道。
- 不把某个社区、群体或住户标签化为污染源；本域关注结构性服务、清理责任和环境正义边界。

## Source Signals

- EPA Illegal Dumping: https://www.epa.gov/large-scale-residential-demolition/illegal-dumping
- EPA Report Environmental Violations: https://echo.epa.gov/report-environmental-violations

## 下一步

- 建立 `dumped material -> location/responsibility -> exposure/access risk -> neighborhood task -> continuity outcome` 变量表。
- 区分大件垃圾、轮胎、建筑废料、危险材料、搬家/驱逐/拆迁后堆积、长期热点和灾后碎片。
- 与 `residential-solid-waste-collection-bin-sanitation-continuity`、`disaster-debris-waste-sanitation-cleanup-continuity`、`waste-management-hazardous-materials-continuity` 建立边界。
