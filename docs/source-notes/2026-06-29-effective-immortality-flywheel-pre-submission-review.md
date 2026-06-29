# 有效永生飞轮 Pre-Submission Review v0.1

Status: local pre-submission review gate  
Date: 2026-06-29  
Target paper: [Effective Immortality Acceleration Flywheel](../explanations/effective-immortality-acceleration-flywheel.md)  
Generated artifacts:

- [`PRE_SUBMISSION_REVIEW.json`](../../web/src/data/effective-immortality-flywheel/PRE_SUBMISSION_REVIEW.json)
- [`PRE_SUBMISSION_REVIEW.md`](../../web/src/data/effective-immortality-flywheel/PRE_SUBMISSION_REVIEW.md)

## Scope

本轮不是外部审稿，也不是逐句 citation-context reviewer。它是本地预提交门禁，专门检查以下问题：

1. working paper、Web paper page、Evidence Matrix、derivation package 和 automated research run 是否出现版本漂移；
2. `v0.25 / schema 2.0 / Evidence Matrix v1.3 / Citation Audit v1.1` 是否同步；
3. “不证明永生已经可行、不输出个体死亡日期、不替代医学判断”等硬边界是否仍在正文和页面中；
4. Citation Audit、Citation Context Review Packet、Citation Context Risk Triage、High-Risk Citation Context Review、Citation Context Local Review、Fresh Reviewer Citation Audit Protocol、Fresh Reviewer Citation Results Audit、Reference Verification、Claim Context Audit 和 Coverage Audit 是否存在并处于预期状态；
5. active paper 和 Web paper page 是否出现 em dash、en dash 或常见 AI-tone 词；
6. 正式投稿前仍需完成的外部审查是否被显式保留，而不是被本地 PASS 掩盖。

## Result

| 项目 | 结果 |
| --- | --- |
| Overall verdict | WARN |
| CRITICAL | 0 |
| MAJOR | 1 |
| MINOR | 0 |
| Version drift | 0 |
| Em dash / en dash | 0 |
| Banned AI-tone terms | 0 |

## Remaining Queue

| Severity | Item | Reason | Action |
| --- | --- | --- | --- |
| MAJOR | fresh reviewer citation audit pending | 当前 `CITATION_AUDIT.json` 是本地 Reference Registry 导出；CTX1-CTX12 已完成本地来源边界审查，最高风险 `CTX2` 得到 `PASS_WITH_LIMITATIONS`，Fresh Reviewer Citation Audit Protocol 已把队列和 pass gate 导出，Fresh Reviewer Citation Results Audit 仍为 `PENDING_EXTERNAL_REVIEW_RESULTS` | 正式提交前运行独立 reviewer，对每个正文 claim 和 citation context 做外部核查，并把结果写入 results ledger |

## Fixes Applied Before Gate

- Working paper 从 `v0.21` 逐步升级为 `v0.25`。
- 结构化证据数据从 schema `1.8` 逐步升级为 schema `2.0`。
- Web paper page 从 `v0.21` 逐步升级为 `v0.25`。
- 旧的 `Evidence Matrix v0.8` / `Evidence Matrix v0.4` 指向统一修正为 `Evidence Matrix v1.3`。
- Automated research run 中的 `Citation Audit v0.4` 修正为 `Citation Audit v1.1`。
- Reproducibility anchors 增加 `PRE_SUBMISSION_REVIEW.json` 和 `PRE_SUBMISSION_REVIEW.md`。
- Reproducibility anchors 增加 `CITATION_CONTEXT_REVIEW_PACKET.json` 和 `CITATION_CONTEXT_REVIEW_PACKET.md`，用于后续 fresh reviewer 逐句引用语境审查。
- Reproducibility anchors 增加 `CITATION_CONTEXT_RISK_TRIAGE.json` 和 `CITATION_CONTEXT_RISK_TRIAGE.md`，把 12 个引用语境按本地过度外推风险排序。
- Reproducibility anchors 增加 `HIGH_RISK_CITATION_CONTEXT_REVIEW.json` 和 `HIGH_RISK_CITATION_CONTEXT_REVIEW.md`，先对 HIGH/BLOCKER 队列做来源边界审查。
- Reproducibility anchors 增加 `CITATION_CONTEXT_LOCAL_REVIEW.json` 和 `CITATION_CONTEXT_LOCAL_REVIEW.md`，对 CTX1-CTX12 做全量本地来源边界审查。
- Reproducibility anchors 增加 `FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json` 和 `FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.md`，把剩余逐句引用语境审查导出为外部 reviewer 可执行协议。
- Reproducibility anchors 增加 `FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.*` 和 `FRESH_REVIEWER_CITATION_AUDIT_RESULTS_AUDIT.*`，用于记录和验证真实 reviewer 结果；当前状态保持 pending。
- Reproducibility anchors 增加 Search Execution Register v0.1，把 Literature Gap Map 转成候选来源、数据库、检索式、初筛决策、边界用途和下一步动作。
- Reproducibility anchors 增加 Candidate Source Verification v0.1，记录候选来源 URL/DOI 状态、规范题名、出版状态、证据等级、使用决策和阻塞项。
- Reproducibility anchors 增加 Candidate Source Extraction v0.1，记录候选来源实际抽取内容、支持范围、不可支持范围、晋升决策和 Source Card 下一步动作。
- `rogers2003diffusion` 改用 Internet Archive 书目页，`hutchins1995cognition` 改用作者主页书籍页，Reference Verification 收敛为 `48 PASS / 0 WARN / 0 FAIL`。
- `npm run audit:paper-integrity` 现在包含 citation risk triage、high-risk citation context review、citation context local review、fresh reviewer protocol export、fresh reviewer results audit 和 pre-submission review，形成完整本地科研门禁。

## Interpretation

当前状态可以继续本地研究、页面打磨和仓库推送。本地门禁已经把全部引用语境审到来源边界层，并把外部 fresh reviewer 的审稿队列、独立性要求、pass gate、结果模板和结果验证规则导出成协议，但不能被描述为“正式投稿级 citation audit 已完成”。如果后续要把这篇 working paper 变成论文投稿，下一步必须优先补 fresh reviewer thread 的逐句引用语境审查，并把真实结果写入 `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`。

## Re-run

```bash
cd web
npm run audit:paper-integrity
```
