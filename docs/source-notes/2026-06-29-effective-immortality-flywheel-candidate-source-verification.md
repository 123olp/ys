# 有效永生飞轮 Candidate Source Verification v0.1

日期：2026-06-29

用途：对 Search Execution Register v0.1 中的候选来源做 Phase 2 source verification。该文档只确认候选来源的 URL、DOI/持久标识、题名一致性、出版状态和使用边界，不把候选来源升级为正式引用。

## Verification Summary

| ID | SER | URL / metadata | Canonical title status | Verdict | Use boundary |
| --- | --- | --- | --- | --- | --- |
| SEV1 | SER1 | PMC 200；Crossref DOI `10.3348/kjr.2022.0061` | exact | `VERIFY_PASS_METHOD_GATE` | 可用于 RMST 方法门禁，不证明干预延寿。 |
| SEV2 | SER2 | Journal page 200；DOI `10.18608/jla.2023.8093` | normalized title | `VERIFY_PASS_SOURCE_CARD_CANDIDATE` | 可用于学习分析干预和日志变量候选，不证明寿命延长带来高质量学习轮次。 |
| SEV3 | SER3 | Springer 200；DOI `10.1007/s10648-025-10028-0` | title drift detected | `VERIFY_PASS_SOURCE_CARD_CANDIDATE` | 可用于 SRL 变量和多模态数据候选，需用规范题名。 |
| SEV4 | SER4 | Publisher page 403；Crossref DOI `10.1287/orsc.1120.0810` | exact | `VERIFY_PASS_METADATA_ONLY` | 只能作为 metadata-verified 候选；全文未读前不能承担强主张。 |
| SEV5 | SER5 | BIS official page 200；BIS Working Papers No. 1208 | exact | `VERIFY_PASS_SOURCE_CARD_CANDIDATE` | 工作论文状态，必须明确标注，不能外推为通用能力或寿命收益。 |
| SEV6 | SER6 | RePEc / IZA page 200；IZA Discussion Paper No. 18560 | title drift detected | `VERIFY_PASS_METHOD_GATE` | 可用于可能性空间测量方法候选，需标注工作论文状态。 |
| SEV7 | SER7 | PMC 200；Crossref DOI `10.3390/healthcare14020277` | normalized title | `VERIFY_PASS_SOURCE_CARD_CANDIDATE` | 可用于社会支持干预和生存终点候选，需风险偏倚提取。 |
| SEV8 | SER8 | NIST official PDF 200；`NIST.AI.800-4` | exact | `VERIFY_PASS_METHOD_GATE` | 可用于 AI 部署后监测治理语言，不提供效果量。 |
| SEV9 | SER9 | PMC 200；Crossref DOI `10.57264/cer-2025-0180` | normalized title | `VERIFY_PASS_METHOD_GATE` | 可用于 target-trial protocol 方法门禁，不验证任何 Human Infra 干预。 |

## Promotion Rules

- `VERIFY_PASS_METHOD_GATE`：只能进入方法、报告、审计、建模或治理门禁，不能写成效果证据。
- `VERIFY_PASS_SOURCE_CARD_CANDIDATE`：允许进入全文阅读和 Source Card 草案，但仍需提取支持范围、不可支持范围和反证条件。
- `VERIFY_PASS_METADATA_ONLY`：只能说明元数据存在；全文未读前不得进入强 claim-to-source map。
- working paper / discussion paper：必须在正文和 Reference Registry 中显式标注，不得和同行评议文章混用。
- title drift：必须使用规范题名更新候选记录后，才可进入正式 Reference Registry。

## Blocking Items

- SER4：publisher page 本地抓取返回 403，需通过机构访问、出版社摘要、作者稿或其他合法全文入口完成全文核查。
- SER5：需确认质量指标、QA/rework 成本、分配机制和工作论文状态。
- SER6：需记录工作论文状态，并确认测量方法是否适合 Human Infra 的 `O_t`。
- SER7：需做非随机研究风险偏倚提取，避免把 meta-analysis 形式直接升级为强因果结论。

## Current Interpretation

候选来源验证把“可检索”推进到“可筛选”。当前 9 条候选都有可追踪 URL 或 DOI/持久标识，但没有任何一条因此自动成为正式论文证据。下一步是全文阅读和 Source Card 晋升。
