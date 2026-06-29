# 有效永生飞轮 Candidate Source Extraction v0.1

日期：2026-06-29

用途：在 Candidate Source Verification v0.1 之后，记录候选来源可抓取正文、摘要、官方页或 PDF 中实际抽取到的内容。该文档不把候选来源升级为正式证据，而是决定下一步是否写 Source Card 草案、是否保留方法门禁、是否暂停。

## Extraction Summary

| ID | Source | Read scope | Promotion decision | Main boundary |
| --- | --- | --- | --- | --- |
| SEE1 | RMST quick guide | PMC page headings and method metadata | `METHOD_SOURCE_CARD_DRAFT` | 只支持 RMST 报告语言，不支持主体连续性或干预效果。 |
| SEE2 | Learning analytics review | journal abstract | `SOURCE_CARD_DRAFT` | 支持 LMS log / learning analytics 作为学习轮次观测入口，不支持寿命自动转化为学习。 |
| SEE3 | SRL multimodal data review | Springer abstract | `SOURCE_CARD_DRAFT_WITH_TITLE_FIX` | 支持 SRL 过程和多模态数据测量，不支持长期迁移或跨域能力增长。 |
| SEE4 | Dynamic capabilities article | Crossref metadata only | `HOLD_METADATA_ONLY` | 只能证明书目存在，不能进入强 claim-to-source map。 |
| SEE5 | BIS GenAI coding field experiment | BIS official summary | `SOURCE_CARD_DRAFT_WITH_WORKING_PAPER_CAVEAT` | 支持限定编码任务中的 A -> Q 候选证据，不支持通用能力或健康寿命收益。 |
| SEE6 | Capability set measurement paper | RePEc / IZA abstract | `METHOD_SOURCE_CARD_DRAFT_WITH_WORKING_PAPER_CAVEAT` | 支持机会集合测量问题，不证明任务质量必然扩大真实选项。 |
| SEE7 | Social support survival meta-analysis | PMC abstract | `SOURCE_CARD_DRAFT_WITH_RISK_OF_BIAS_GATE` | 非随机试验 meta-analysis，部分生存结果未达统计显著，不能写成强因果结论。 |
| SEE8 | NIST deployed AI monitoring report | PDF abstract, executive summary and TOC | `METHOD_SOURCE_CARD_DRAFT` | 支持部署后监测治理语言，不提供任何具体 AI 系统效果量。 |
| SEE9 | Target trial emulation article | PMC abstract | `METHOD_SOURCE_CARD_DRAFT` | 支持因果协议字段，不验证任何 Human Infra 干预。 |

## Promotion Rules

- `METHOD_SOURCE_CARD_DRAFT`：只写方法卡片，进入模型契约、报告规范、审计门禁或治理语汇。
- `SOURCE_CARD_DRAFT`：允许写来源卡片草案，但必须补支持范围、不可支持范围、证据等级和外推边界。
- `SOURCE_CARD_DRAFT_WITH_WORKING_PAPER_CAVEAT`：允许草案，但正文必须显式标注 working paper / discussion paper 状态。
- `SOURCE_CARD_DRAFT_WITH_RISK_OF_BIAS_GATE`：允许草案，但必须先补风险偏倚或非随机设计审查。
- `HOLD_METADATA_ONLY`：只保留候选，不进入 Source Cards、Reference Registry 或 Citation Context Register。

## Current Interpretation

这一步把“候选已核验”推进为“候选已抽取”。当前真正可进入下一步的是方法卡片和边界明确的来源卡片草案；SER4 仍暂停，SER5/SER6 必须带工作论文 caveat，SER7 必须带风险偏倚门禁。
