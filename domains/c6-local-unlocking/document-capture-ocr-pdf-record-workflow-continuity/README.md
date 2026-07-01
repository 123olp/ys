# Document Capture OCR PDF Record Workflow Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/document-capture-ocr-pdf-record-workflow-continuity` |
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

`document-capture-ocr-pdf-record-workflow-continuity` 研究扫描、拍照、OCR、PDF、PDF/A、表单、签收、归档、文件命名、元数据和记录工作流如何影响主体把纸面事实转化为可检索、可提交、可保存的数字证据。

> 核心问题：许多权利、服务、报销、学习和照护任务依赖文件；文件不可读、不可找、不可提交或不可长期保存，会让事实失去效力。

## 关注对象

- 扫描、手机拍照、OCR、PDF/PDF-A、图像质量、文件压缩、表单填写、附件上传和收据/证明留存。
- 元数据、文件命名、版本、归档、保管期限、长期可读性、可访问 PDF、数字记录交接和备份。
- 医疗、保险、税务、学校、就业、法律、福利、移民、采购和科研记录工作流。
- OCR 错误、低质量图像、格式锁定、上传失败、附件丢失、隐私泄露和长期格式失效。

## Human Infra 链路

```text
文件捕获与记录工作流连续
  -> 纸面事实、证明、表单和附件可被数字化、校验、提交和归档
  -> 文件丢失、不可读、不可检索、不可提交和长期格式失效下降
  -> 主体更能完成服务申请、权利证明、照护交接、学习工作和证据保存
  -> 制度可达性、记忆外化和未来纠错能力增强
```

## 非目标

- 不提供伪造文件、篡改记录、规避审核、破解 DRM、绕过签名、伪造 OCR 或隐私窃取方法。
- 不替代法律、税务、医疗、学校、雇主或公共机构的正式文件要求。
- 不收集身份证件、病历、税务文件、法律文件、合同、成绩单或敏感扫描件。

## Source Signals

- Library of Congress PDF/A format description: https://www.loc.gov/preservation/digital/formats/fdd/fdd000125.shtml
- NARA electronic records guidance: https://www.archives.gov/records-mgmt
- Federal Agencies Digital Guidelines Initiative: https://www.digitizationguidelines.gov/
- PDF Association PDF/A resources: https://pdfa.org/

## 下一步

- 建立 `paper fact -> capture -> OCR -> metadata -> submission -> archive -> retrieval` 变量表。
- 区分个人资料、医疗记录、财务/税务文件、教育文件、法律文件、组织记录和科研资料。
- 与 `life-logging-personal-archives-continuity`、`cloud-backup-file-sync-data-portability-continuity`、`notary-document-authentication-signature-continuity` 和 `search-index-discovery-retrieval-continuity` 建立边界。
