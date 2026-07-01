# Contact Lens Hygiene Eye Infection Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/contact-lens-hygiene-eye-infection-continuity` |
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

`contact-lens-hygiene-eye-infection-continuity` 研究隐形眼镜佩戴、清洁、储存、替换、护理液、处方更新和感染风险如何影响视觉任务、工作学习、出行和眼部安全连续性。

> 核心问题：隐形眼镜不是单纯屈光矫正用品；它把视觉带宽、手部卫生、耗材供应、佩戴习惯、感染入口和眼科转诊连成一个日常风险系统。

## 关注对象

- 隐形眼镜、护理液、镜盒、替换周期、处方有效性、佩戴场景和卫生行为。
- 角膜感染、疼痛、红眼、视力变化、眼表损伤和医疗延迟的任务影响。
- 学校、工作、运动、旅行、灾害、住房不稳、清洁水可及和替代眼镜路径。
- 与屈光矫正、眼表舒适、眼外伤、WASH、医疗器械和药店/眼科服务的接口。

## Human Infra 链路

```text
隐形眼镜卫生连续
  -> 主体能够稳定获得清晰视觉输入且不把矫正工具变成感染入口
  -> 清洁水、护理液、镜盒、替换周期和转诊入口的断点被提前识别
  -> 阅读、驾驶、屏幕任务、学习、工作和空间行动的低层视觉摩擦下降
  -> 有效时间、行动安全和未来选择权增强
```

## 非目标

- 不提供验光、隐形眼镜处方、品牌推荐、佩戴时长、感染判断、眼科治疗或急症处置建议。
- 不替代眼科医生、验光师、FDA、CDC、NEI 或产品标签。
- 不把隐形眼镜作为绕过职业安全、防护眼镜或眼伤转诊的替代方案。

## Source Signals

- CDC Contact Lenses: https://www.cdc.gov/contact-lenses/
- NEI Contact Lenses: https://www.nei.nih.gov/eye-health-information/healthy-vision/contact-lenses
- FDA Medical Devices - Contact Lenses search entry may move; prefer CDC/NEI for stable hygiene and eye health facts.

## 下一步

- 建立 `lens type -> hygiene dependency -> supply dependency -> eye risk -> task impact` 变量表。
- 区分日常佩戴、游泳/淋浴、睡眠佩戴、旅行、灾害、青少年和住房/水卫生不稳场景。
- 与 `refractive-error-glasses-contact-lens-continuity`、`dry-eye-ocular-surface-comfort-continuity` 和 `eye-injury-urgent-vision-protection-continuity` 建立边界。
