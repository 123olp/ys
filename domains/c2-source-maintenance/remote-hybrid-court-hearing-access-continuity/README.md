# Remote and Hybrid Court Hearing Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/remote-hybrid-court-hearing-access-continuity` |
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


This domain studies how remote, hybrid, telephonic, and in-person court hearings affect subject participation, comprehension, privacy, evidence presentation, and failure-to-appear risk.

Human Infra value: remote court can reduce travel and time costs, but it can also exclude people through connectivity gaps, device limits, privacy constraints, interpretation failures, disability barriers, and confusing attendance rules.

## Scope

- Remote and hybrid hearing access
- Telephonic participation
- Notice and login instructions
- Connectivity, device, audio, video, and privacy constraints
- Interpreter and accommodation integration
- Evidence presentation and record access at a high level
- Failure-to-appear and rescheduling friction as system risks

## Non-Goals

- No advice on whether to request remote appearance, what to say in court, how to present evidence, or how to handle a live hearing.
- No recording, surveillance, identity exposure, court disruption, or unauthorized access guidance.
- No replacement for court orders, local rules, attorneys, interpreters, or court staff.

## Source Spine

- National Center for State Courts remote hearing and access-to-justice research.
- U.S. Courts and state court public remote proceeding materials.
- ADA.gov and court accessibility resources.
- Digital inclusion and broadband access materials for remote participation constraints.

## Upstream

- `court-notice-service-process-default-judgment-continuity`
- `digital-inclusion-connectivity`
- `court-language-access-interpreter-continuity`
- `court-disability-accommodation-accessibility-continuity`

## Downstream

- `self-represented-litigant-court-self-help-continuity`
- `small-claims-civil-dispute-resolution-continuity`
- `court-fees-fines-ability-to-pay-continuity`
