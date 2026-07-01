# Burn Injury Critical Care Rehabilitation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/burn-injury-critical-care-rehabilitation-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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

- 界定生命载体变量：细胞、组织、器官、脑、免疫、代谢、急性风险或衰老损伤。
- 说明影响机制：修复、替换、再生、控制、筛查、预防、维持或风险降低。
- 列出可观察状态：功能指标、生物标志物、疾病终点、失能时间、恢复能力或死亡风险。
- 记录副作用、过度干预、癌变、免疫、长期安全性和尾部风险。
- 区分机制合理性、体外证据、动物证据、人体早期数据、临床终点和长期安全性。

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

`burn-injury-critical-care-rehabilitation-continuity/` 研究烧伤预防、烧伤中心、液体/感染/疼痛/手术照护、皮肤屏障修复、瘢痕和长期康复如何影响主体身体连续性。

> 核心问题：严重烧伤同时破坏皮肤屏障、体液稳态、感染防线、疼痛控制、运动功能和身份体验。它是身体边界被急性摧毁后的长期重建域。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖皮肤屏障、体温、液体平衡、感染防线和行动功能
  -> 严重烧伤可同时造成休克、感染、疼痛、瘢痕、功能损失和心理创伤
  -> 生存和恢复依赖烧伤中心、重症照护、手术修复、康复和长期支持
  -> 因此烧伤损伤是身体边界毁损后的急性救援与长期重建域
```

## 关注对象

- Burn center access、burn severity、fluid loss、infection risk、pain, grafting/reconstruction, scar, rehabilitation, return to function。
- 与 `skin-barrier-wound-healing/` 的边界：皮肤屏障域关注屏障和伤口机制；本域关注严重烧伤的系统性重症和康复链。
- 与 `trauma-system-hemorrhage-control-continuity/` 的关系：烧伤也可作为特殊创伤系统的一部分。

## Human Infra 模型链路

```text
烧伤重症与康复基础设施 T
  -> 改变烧伤中心可达、液体管理、感染控制、手术修复、疼痛和康复变量 X
  -> 改变休克、感染、皮肤屏障、运动功能、瘢痕和心理恢复状态 S
  -> 改变死亡、感染、长期残障、疼痛和社会参与损失风险 λ(t)
  -> 影响主体身体连续性、有效时间和行动能力
```

## 非目标

- 不提供烧伤急救、伤口处理、敷料、液体、止痛、抗感染、手术、瘢痕处理或个体医疗建议。
- 不生成烧伤中心选择、转运策略、工伤/保险/法律建议或事故处置方案。
- 不收集伤口照片、身份、定位、病历、烧伤机制、暴力/工伤证据或敏感康复资料。

## Source Signals

- WHO Burns Fact Sheet: https://www.who.int/news-room/fact-sheets/detail/burns
- American Burn Association: https://ameriburn.org/
- CDC Fire Safety: https://www.cdc.gov/fire-safety/

## 下一步

- 建立 Burn Continuity Card：severity, center access, infection, reconstruction, pain, scar, rehab, social reintegration。
- 与 `skin-barrier-wound-healing/`、`trauma-system-hemorrhage-control-continuity/` 和 `rehabilitation-functioning/` 建立接口。
