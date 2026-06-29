# 有效永生飞轮候选来源晋升综合 v0.1

日期：2026-06-29  
上游资料：[Candidate Source Verification](2026-06-29-effective-immortality-flywheel-candidate-source-verification.md)、[Candidate Source Extraction](2026-06-29-effective-immortality-flywheel-candidate-source-extraction.md)  
目标论文：[Effective Immortality Acceleration Flywheel](../explanations/effective-immortality-acceleration-flywheel.md)

## 结论

候选来源已经从“可访问 / 元数据存在”推进到“能否承担科研角色”的阶段。当前 9 条候选来源中，5 条只应作为方法或治理卡片，3 条可进入来源卡片草案但必须保留 working paper、题名修正或风险偏倚边界，1 条只能保留为 metadata-only 暂停项。Source Cards v0.5 已完成 P1 晋升：SEE1、SEE2、SEE3、SEE8、SEE9 已进入 Source Card 草案，并同步补入 Reference Registry。下一轮科研重点转向 SEE5、SEE6、SEE7 的 P2 细读和风险偏倚门禁。

## Promotion Matrix

| 类别 | 数量 | 来源 | 可进入位置 | 不得进入位置 |
| --- | ---: | --- | --- | --- |
| `METHOD_SOURCE_CARD_DRAFT` | 3 | SEE1、SEE8、SEE9 | RMST 有效时间表达、部署后 AI 监测、target-trial style 因果协议 | 干预效果、寿命收益、主体增强结论 |
| `METHOD_SOURCE_CARD_DRAFT_WITH_WORKING_PAPER_CAVEAT` | 1 | SEE6 | 机会集合 / capability set 测量方法 | 任务质量必然扩大真实选项的结论 |
| `SOURCE_CARD_DRAFT` | 1 | SEE2 | 学习分析、LMS 日志、反馈事件和学习轮次观测 | 寿命自动转化为学习轮次 |
| `SOURCE_CARD_DRAFT_WITH_TITLE_FIX` | 1 | SEE3 | 自我调节学习、过程数据、多模态学习轨迹 | 长期迁移、跨域能力增长或抗遗忘结论 |
| `SOURCE_CARD_DRAFT_WITH_WORKING_PAPER_CAVEAT` | 1 | SEE5 | 限定编码任务中的 AI 工具采用与单位时间产出 | 通用智力增强、健康寿命收益、长期无条件生产率收益 |
| `SOURCE_CARD_DRAFT_WITH_RISK_OF_BIAS_GATE` | 1 | SEE7 | 社会支持干预与生存结局的研究分支 | 强因果结论或稳定生存收益结论 |
| `HOLD_METADATA_ONLY` | 1 | SEE4 | 候选队列和后续全文检索任务 | Source Card、Reference Registry、Citation Context Register |

## Synthesis

这 9 条候选来源不是同一种证据。SEE1、SEE8、SEE9 的价值在于给模型建立报告语言和治理门禁：如何报告有限随访窗口内的有效时间，如何监测部署后的 AI 系统，如何把观察性问题转写为 target-trial style 协议。它们能降低论文的方法风险，但不能直接增加任何链路边的效应强度。

SEE2 和 SEE3 共同补强 `E -> R -> C`：有效时间必须被转化为有记录、有反馈、有调节的学习过程，才可能进入能力积累。两者的限制也一致：学习日志和多模态轨迹可以观察过程，不证明时间延长必然带来高质量学习，也不证明能力会长期迁移。

SEE5 是 `A -> Q` 的候选任务级证据，但当前只能带 working-paper caveat 使用。它适合支持“AI 工具可能在限定编码任务中改变产出”的弱命题，不适合支持“AI 让主体能力普遍增强”的强命题。

SEE6 和 SEE7 分别提醒 `Q -> O` 与 `O -> T/E` 的难点：机会集合不是可观察结果的简单同义词；社会支持与生存结局之间即便存在干预研究，也要受非随机设计、异质性和显著性边界约束。

SEE4 暂停。没有可读摘要、正文或作者稿之前，它只能证明书目存在，不能参与正文主张。

## Action Status

| 优先级 | 动作 | 产物 |
| --- | --- | --- |
| DONE | 为 SEE1、SEE8、SEE9 写方法 Source Card 草案 | Source Cards v0.5 Card 43、46、47 |
| DONE | 为 SEE2、SEE3 写学习过程测量卡片 | Source Cards v0.5 Card 44、45 |
| P2 | 为 SEE5 补 full-text 或工作论文 PDF 细读 | AI 编码任务证据卡片草案 |
| P2 | 为 SEE7 补 ROBINS-I / 非随机试验风险偏倚摘要 | 社会支持干预边界卡片 |
| P3 | 为 SEE6 补 opportunity-set 测量假设与数据要求 | `Q -> O` 方法卡片 |
| HOLD | 为 SEE4 找合法全文、作者稿或可读摘要 | 保留候选，不晋升 |

## Boundary

本综合只决定候选资料的下一步科研用途，不构成正式引用审查结论。正式投稿前仍必须完成 fresh reviewer citation-context audit，并把每条正文主张与来源可支持范围逐句对齐。
