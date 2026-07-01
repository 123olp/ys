# Residential Solid Waste Collection Bin Sanitation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/residential-solid-waste-collection-bin-sanitation-continuity` |
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


`residential-solid-waste-collection-bin-sanitation-continuity` 研究住宅生活垃圾、回收物、庭院废弃物、垃圾桶、收运频率、错过收运、大件预约和多户住宅垃圾间如何影响家庭卫生、害虫风险、邻里关系和居住恢复。

> 核心问题：家庭任务结束后会产生残余物；如果日常固废收集、容器管理和收运服务失败，厨房、卫生间、照护、学习和恢复空间会被气味、害虫、堆积和邻里冲突反向占据。

## 关注对象

- 住宅生活垃圾、可回收物、庭院废弃物、垃圾桶、垃圾间、收运频率、错过收运、大件收运和节假日/天气中断。
- 公寓、多户住宅、行动受限家庭、儿童家庭、照护家庭、无车家庭和高温天气下的垃圾暂存压力。
- 气味、害虫、泄漏、桶容量、路缘摆放、楼梯/电梯动线、物业规则和市政服务边界。
- 与家庭清洁、害虫控制、食品储存、公共卫生、非法倾倒和灾后废弃物清理的接口。

## Human Infra 链路

```text
住宅固废收运与垃圾桶卫生连续
  -> 家庭任务产生的残余物能按类别、容量和时间窗口离开居住空间
  -> 气味、害虫、泄漏、堆积和邻里摩擦被降低
  -> 厨房、卫生间、照护、睡眠、学习和恢复空间保持可用
  -> 主体居住稳定、卫生连续和行动恢复能力提高
```

## 非目标

- 不提供垃圾分类执法规避、非法倾倒、偷倒、焚烧、危险废物混入、隐私资料丢弃、物业纠纷或个案投诉策略。
- 不替代地方固废部门、物业、房东、市政收运服务、公共卫生部门、代码执法、害虫控制或环境执法渠道。
- 不把“垃圾越快消失”视为唯一目标；本域关注分类、容量、频率、卫生、可达和服务连续性。

## Source Signals

- EPA Recycling Basics and Benefits: https://www.epa.gov/recycle/recycling-basics-and-benefits
- EPA Facts and Figures about Materials, Waste and Recycling: https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling
- EPA Illegal Dumping: https://www.epa.gov/large-scale-residential-demolition/illegal-dumping

## 下一步

- 建立 `household waste stream -> container/service state -> sanitation risk -> household task -> continuity outcome` 变量表。
- 区分单户、多户、公寓垃圾间、行动受限者、高温天气、节假日中断和大件收运等待场景。
- 与 `household-cleaning-disinfection-pest-control-continuity`、`waste-management-hazardous-materials-continuity`、`illegal-dumping-litter-neighborhood-sanitation-continuity` 建立边界。
