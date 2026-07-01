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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

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
