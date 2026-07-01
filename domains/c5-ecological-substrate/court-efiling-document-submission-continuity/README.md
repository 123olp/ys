# Court E-Filing and Document Submission Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/court-efiling-document-submission-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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


This domain studies whether people can submit, receive, correct, and preserve court documents through electronic filing, paper alternatives, mail, clerk counters, and hybrid submission channels.

Human Infra value: a right or defense can fail if documents cannot be filed, fees cannot be paid or waived, notices are missed, formats are rejected, or digital filing excludes people without devices, accounts, bandwidth, or legal knowledge.

## Scope

- Court e-filing systems
- Paper and in-person alternatives
- Document formats, signatures, exhibits, and service copies
- Filing status, rejection, correction, and timestamp visibility
- Account recovery and notification routing
- Fee waiver interfaces
- Accessibility, language, and digital divide risks

## Non-Goals

- No legal advice, filing strategy, document drafting, document review, deadline calculation, or e-filing walkthrough for a live case.
- No automation for mass filing, abusive litigation, fake documents, forged signatures, or court-system probing.
- No bypassing court rules, payment systems, account security, or access controls.

## Source Spine

- National Center for State Courts e-courts, technology, and access-to-justice resources.
- U.S. Courts CM/ECF and PACER public materials for federal context.
- State court e-filing and self-help materials as local implementation examples.
- W3C accessibility and digital public service guidance for interface risk.

## Upstream

- `self-represented-litigant-court-self-help-continuity`
- `court-notice-service-process-default-judgment-continuity`
- `digital-inclusion-connectivity`
- `document-capture-ocr-pdf-record-workflow-continuity`

## Downstream

- `remote-hybrid-court-hearing-access-continuity`
- `court-fees-fines-ability-to-pay-continuity`
- `small-claims-civil-dispute-resolution-continuity`
