# Synthetic Media Watermarking Disclosure Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/synthetic-media-watermarking-disclosure-continuity` |
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

Synthetic Media Watermarking Disclosure Continuity 关注 AI 生成或编辑的图片、音频、视频、文本和多模态内容如何被标注、披露、溯源、保留水印和解释边界。

## 对象

- Synthetic media、AI-generated content、watermarking、disclosure、labeling、detector limitation、content credential 和 provenance preservation。
- 合成内容在社交平台、新闻、广告、教育、司法、招聘、公共服务和医疗沟通中的披露与误读风险。
- 水印被剥离、检测误报/漏报、标签不一致、跨平台丢失、低质量披露和过度依赖检测器的失败模式。

## Human Infra 价值

```text
主体需要知道自己面对的是人类记录、机器生成还是混合编辑内容
-> 合成媒体让声音、面孔、事件和证据更容易被制造
-> 水印、披露和 provenance 能降低判断成本，但不能替代事实核验
-> 主体更能管理信任、注意力、情绪反应、证据使用和风险暴露
-> 信息环境更少把伪造真实感转化为不可逆决策
```

## 边界

- 本域不提供 deepfake 制作、模型提示、声音克隆、脸部替换、检测规避、水印移除或反检测策略。
- 不提供“检测某内容是否 AI 生成”的个案判断，也不把水印或检测器写成事实证明。
- 不做政治传播、广告投放、舆论操控、名誉攻击或证据伪造。
- 只整理公开框架、披露机制、风险边界、误差限制和治理问题。

## 上下游

- 上游：`content-provenance-authenticity-credential-continuity/`、`information-integrity-trust/`、`model-cards-ai-audit-documentation/`。
- 下游：`ai-impersonation-deepfake-fraud-continuity/`、`reputation-defamation-public-trust-repair-continuity/`、`platform-content-moderation-notice-appeal-continuity/`。

## Source Signals

- NIST synthetic content transparency and AI risk management materials.
- C2PA and Content Credentials materials.
- FTC AI, impersonation and consumer protection materials.
- Platform and standards-body synthetic media disclosure materials.
