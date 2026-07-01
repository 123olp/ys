# Healthcare Language Interpreter Effective Communication Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/healthcare-language-interpreter-effective-communication-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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


## 定位

本域研究医疗语言服务、interpreter access、translated materials、effective communication、CLAS 和 LEP 场景如何影响主体能否理解、表达和执行医疗任务。

它不是翻译认证、医疗解释、法律意见、个案口译安排或临床沟通代写工具。

## 先验问题

```text
医疗理解何以成立？
  -> 医疗信息必须以主体能理解的语言和形式到达
  -> 口译、翻译和有效沟通必须覆盖预约、同意、结果、账单和出院
  -> 家属临时翻译不能替代系统性语言服务
  -> 否则主体无法可靠表达症状、理解风险、执行计划或保护权利
```

## 研究对象

- Healthcare interpreter services、language assistance、translated notices、CLAS standards。
- LEP、Deaf/Hard of Hearing、auxiliary aids、plain language、teach-back 和 culturally appropriate communication。
- 预约、急诊、住院、同意、结果、药物、出院、账单和投诉中的语言断点。

## 关键变量

- 语言需求识别率、口译等待时间、材料翻译覆盖率和沟通错误率。
- 口译模式、质量、隐私、术语负担、健康素养和文化适配。
- 语言服务费用、责任方、远程口译、紧急场景和投诉路径。

## 证据入口

- HHS National CLAS Standards、LEP.gov 和 HHS OCR language access 资料。
- ADA effective communication、CDC health literacy 和 plain language 资料。
- 医疗口译、语言可及、沟通错误和 patient safety 文献。

## 非目标

- 不提供医学翻译、诊断解释、治疗解释、口译替代、法律建议或认证翻译。
- 不安排 interpreter、投诉、预约、授权、账单沟通或语言服务请求。
- 不收集医疗记录、语言身份、移民状态、PHI、联系方式或音视频资料。

## 上下游

- 上游：`language-access-plain-communication/`、`health-literacy-navigation/`。
- 下游：`informed-consent-refusal-shared-decision-continuity/`、`clinical-results-notification-followup-continuity/`。
