# Healthcare Civil Rights Nondiscrimination Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/healthcare-civil-rights-nondiscrimination-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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

本域研究医疗系统中的 civil rights、nondiscrimination、Section 1557、race/sex/disability/language discrimination、religion、age 和 gender identity 等保护如何影响主体能否持续进入公平医疗。

它不是法律意见、歧视投诉代写、身份判断、机构合规认证或医疗服务选择工具。

## 先验问题

```text
公平医疗何以成立？
  -> 医疗入口、沟通、诊疗、账单和投诉必须不因受保护特征被排除
  -> 歧视、骚扰、拒绝服务和不平等质量必须可被识别、记录和纠正
  -> 民权保护必须连接语言、残障、性别、年龄、种族和宗教场景
  -> 否则主体持续性会被制度性排除和低质量服务侵蚀
```

## 研究对象

- HHS OCR civil rights、Section 1557、Title VI、Section 504、ADA 和 age discrimination。
- 医疗歧视、语言可及、残障权利、性别和 pregnancy discrimination、LGBTQ+ healthcare access。
- Nondiscrimination notice、grievance procedure、complaint pathway、data equity 和 bias mitigation。

## 关键变量

- 服务拒绝、质量差异、投诉率、语言/残障服务可用性和 grievance procedure 可见性。
- 受保护特征、交叉性、隐私风险、retaliation fear 和机构培训。
- 数据收集边界、算法偏见、民权执行、质量改进和安全文化。

## 证据入口

- HHS OCR civil rights、Section 1557、Title VI、Section 504 和 conscience / nondiscrimination 资料。
- ADA.gov healthcare/effective communication、National CLAS Standards 和 LEP.gov。
- 医疗歧视、health equity、bias、patient experience 和 civil rights enforcement 文献。

## 非目标

- 不提供法律意见、身份资格判断、歧视认定、投诉策略、诉讼建议或胜诉承诺。
- 不代写 OCR complaint、grievance、demand letter、appeal、media statement 或机构沟通。
- 不收集受保护身份、移民状态、宗教、性别、残障、病历、PHI、证据材料或联系方式。

## 上下游

- 上游：`governance-rights/`、`healthcare-language-interpreter-effective-communication-continuity/`、`healthcare-disability-accommodation-accessibility-continuity/`。
- 下游：`patient-grievance-complaint-ombuds-continuity/`、`health-equity-disparities/`。
