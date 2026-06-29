# 度规红移固有时差分路径专项论文页优化记录

日期：2026-06-29

## 目标

把“黑洞等待室”从传播性概念收敛成一个可审查的 Human Infra 工作论文对象：度规红移固有时差分路径。

本轮不声称人工黑洞、类黑洞工程或人体等待方案可行，只完成论文对象、工具链、证据边界和本地审计门禁。

## 本轮产物

- 论文页：`web/src/pages/papers/proper-time-differential-waiting-hypothesis.astro`
- 结构化数据源：`web/src/data/proper-time-differential-waiting-hypothesis.json`
- 工具 seed：`web/src/data/proper-time-differential-waiting-hypothesis/TOOL_GENERATED_PAGE_SEED.astro`
- Citation context 导出脚本：`web/scripts/export-proper-time-differential-citation-context-review-packet.mjs`
- Citation context 审查输入包：`web/src/data/proper-time-differential-waiting-hypothesis/CITATION_CONTEXT_REVIEW_PACKET.json`
- Citation context 审查输入摘要：`web/src/data/proper-time-differential-waiting-hypothesis/CITATION_CONTEXT_REVIEW_PACKET.md`
- Citation context 本地审查脚本：`web/scripts/audit-proper-time-differential-citation-context-local-review.mjs`
- Citation context 本地审查账本：`web/src/data/proper-time-differential-waiting-hypothesis/CITATION_CONTEXT_LOCAL_REVIEW.json`
- Citation context 本地审查摘要：`web/src/data/proper-time-differential-waiting-hypothesis/CITATION_CONTEXT_LOCAL_REVIEW.md`
- 参考来源核验脚本：`web/scripts/verify-proper-time-differential-references.mjs`
- 参考来源核验账本：`web/src/data/proper-time-differential-waiting-hypothesis/REFERENCE_VERIFICATION.json`
- 参考来源核验摘要：`web/src/data/proper-time-differential-waiting-hypothesis/REFERENCE_VERIFICATION.md`
- 覆盖审计脚本：`web/scripts/audit-proper-time-differential-paper.mjs`
- 覆盖审计产物：`web/src/data/proper-time-differential-waiting-hypothesis/COVERAGE_AUDIT.json`
- 覆盖审计摘要：`web/src/data/proper-time-differential-waiting-hypothesis/COVERAGE_AUDIT.md`

## 结构补强

论文页从 v0.1 概念页补强为 v0.2 可审查工作论文：

- 贡献注册表：C1-C5
- Source Cards：SC1-SC5
- Claim-Evidence Matrix：CL1-CL5
- Scenario Cards：SCN0-SCN4
- 图表计划：F1-F4
- 引用边界表：物理来源、科普来源、内部 Human Infra 文档、玩具模型
- 15 个正文章节和 TOC 对齐

## 结构化数据晋升

论文页从 v0.2 的页面内数组晋升为 v0.3 数据驱动页面：

- `proper-time-differential-waiting-hypothesis.json` 成为概念表、假设表、贡献注册表、状态机、变量表、可达性阶梯、反证条件、Source Cards、Claim-Evidence Matrix、Scenario Cards、图表计划、引用边界和 Reference Registry 的真相源。
- `proper-time-differential-waiting-hypothesis.astro` 只负责 arXiv-style DOM、章节叙事和表格渲染，不再内联研究表格数据。
- `audit-proper-time-differential-paper.mjs` 同时读取 JSON、页面源码和工具 seed，检查数据集合最低行数、Source Card 引用闭合、页面数据消费、章节 TOC 和 arXiv DOM 契约。
- 该结构为下一步 scenario 定性等级、D3 NCG 可视化和外部 citation-context review 留出稳定入口。

## 场景评估与 Toy NCG

论文页从 v0.3 继续补强为 v0.4 玩具模型审查入口：

- 补齐 NCG 变量表，把 `NCG`、`R_life`、`R_engineering` 和 `C_opportunity` 写入结构化数据，避免公式变量没有定义。
- 新增 Scenario Evaluation Registry：把 SCN0-SCN4 分别归类为 baseline、blocked-negative、cannot-evaluate、comparator 和 mechanism-comparator。
- 新增 Toy NCG Evaluation Protocol：固定 E1-E6 的最小审查流程，先审参考系、K、概率门、风险扣减、方向性分类和阻塞项，再允许进入后续可视化。
- 新增 NCG Formula Decomposition：把 K/U、P_exit/P_adopt/P_cont、R_life/R_engineering、R_tail/C_opportunity 和 NCG 输出拆成可审查模块。
- 审计脚本新增 Scenario Evaluation 指向已登记场景、NCG Formula Block 指向已登记变量的交叉引用检查。

## 场景变量矩阵

论文页从 v0.4 继续补强为 v0.5 变量等级矩阵：

- 新增 Qualitative NCG Scale：把 `high`、`medium`、`low`、`blocked`、`missing`、`not-applicable` 固定为进入定量模型前的等级字典。
- 新增 Scenario Variable Matrix：对 SCN0-SCN4 逐一标注 K、U、P_exit、P_adopt、P_cont、R_life、R_engineering、R_tail、C_opportunity 和 NCG 分类。
- 审计脚本新增受控等级检查、场景引用检查和 NCG 分类一致性检查；本轮审计曾抓到矩阵缺少 `C_opportunity` 列，已通过补齐数据修复。

## 引用上下文审查包

论文页从 v0.5 继续补强为 v0.6 引用上下文门禁入口：

- 新增 Citation Context Rows：PTD-CTX1 到 PTD-CTX5，把 CL1-CL5 分别绑定到 SC1-SC5，并明确 safe use、forbidden use 和 review status。
- 新增 `export-proper-time-differential-citation-context-review-packet.mjs`：读取 Source Cards、Claim-Evidence Matrix、Citation Context Rows 和 Reference Registry，导出 fresh reviewer 可消费的 `CITATION_CONTEXT_REVIEW_PACKET.json` 与 `CITATION_CONTEXT_REVIEW_PACKET.md`。
- `npm run audit:proper-time-differential` 现在会先导出 citation context packet，再运行 coverage audit；审计会检查上下文是否指向已登记 claim 和 source card，导出包计数是否与数据源一致。
- 当前导出包只声明 `READY_FOR_EXTERNAL_REVIEW`，不是外部审稿结论；它的作用是防止把物理来源、科普来源或内部模型外推成工程可行性、人体可采用性或个体永生方案。

## 本地完整性门禁

论文页从 v0.6 继续补强为 v0.7 本地完整性门禁：

- 新增 `verify-proper-time-differential-references.mjs`，对 Reference Registry 做来源可达性核验，外部 URL 使用 curl，本地 Human Infra 页面使用路由文件存在性检查。
- 新增 `audit-proper-time-differential-citation-context-local-review.mjs`，对 PTD-CTX1 到 PTD-CTX5 做本地 safe use、forbidden use、risk tier 和 fresh reviewer focus 登记。
- `audit-proper-time-differential-paper.mjs` 现在同时要求 `REFERENCE_VERIFICATION.*`、`CITATION_CONTEXT_REVIEW_PACKET.*`、`CITATION_CONTEXT_LOCAL_REVIEW.*` 和 `COVERAGE_AUDIT.*` 闭合。
- 本轮核验发现 `Hogarth / nLab summary` 链接返回 404；已替换为更稳定且更适合作为正式参考的 arXiv 条目 `Etesi-Nemeti 2001, Non-Turing computations via Malament-Hogarth space-times`，地址为 `https://arxiv.org/abs/gr-qc/0104023`。

## 预提交审查

论文页从 v0.7 继续补强为 v0.8 预提交审查入口：

- 新增 Pre-Submission Review Rows：PSR1 到 PSR5，分别审查研究对象边界、来源入口、引用上下文、模型图表边界和提交建议。
- 新增 `audit-proper-time-differential-pre-submission-review.mjs`：读取结构化数据、页面源码、Reference Verification、Citation Context Review Packet 和 Citation Context Local Review，检查边界声明、非预测器声明、外部审查声明、AI 文风词和 em dash。
- 新增 `PRE_SUBMISSION_REVIEW.json` 与 `PRE_SUBMISSION_REVIEW.md`：当前 verdict 为 `NEEDS_EXTERNAL_REVIEW_BEFORE_FORMAL_SUBMISSION`，表示本地机械门禁清洁，但仍需要外部 citation-context reviewer 和更强形式化模型后才能进入正式提交。
- `audit-proper-time-differential-paper.mjs` 已把 `PRE_SUBMISSION_REVIEW.*` 纳入 coverage gate，页面也显式暴露 `PRE_SUBMISSION_REVIEW.json`、`CITATION_CONTEXT_LOCAL_REVIEW.json` 和 `REFERENCE_VERIFICATION.json`。
- 本轮继续保留硬边界：不声称黑洞等待室、人工黑洞或类黑洞工程已经可行；不得宣称人工黑洞可制造；不输出个体永生方案；当前 NCG 只是概念排序和阻塞识别工具，不是预测器。

## 数据驱动场景图

论文页从 v0.8 继续补强为 v0.9 图表可审查入口：

- 新增 Figure 4：`NCG Scenario Comparison`，以页面内联 SVG 渲染 `scenario-ncg-matrix-svg`。
- Figure 4 直接消费 `Scenario Variable Matrix`，把 K、U、P_exit、P_adopt、P_cont、R_life、R_engineering、R_tail、C_opportunity 和 NCG 分类放在同一张矩阵中。
- 图形采用颜色与文字双编码：`高`、`中`、`低`、`阻`、`缺`、`无`，避免只靠颜色表达状态。
- 该图的主要论点是：高 K 不等于正收益；当退出、采用、主体连续性或风险项被阻断时，场景应进入 blocked-negative、cannot-evaluate 或 comparator。
- `audit-proper-time-differential-paper.mjs` 已强制检查 `id="F4"` 和 `id="scenario-ncg-matrix-svg"`，避免图表计划停留在文字表格层。
- 该图仍然是玩具模型分类图，不是参数敏感性图、真实预测器或个体方案生成器。

## 模型边界

核心公式仍是玩具模型，不是预测器：

```text
NCG_i = K_i * U_i * P_exit_i * P_adopt_i * P_cont_i
        - R_life_i - R_engineering_i - R_tail_i - C_opportunity_i
```

其中 `K` 只是未来等待倍率；路径价值必须同时审查退出概率、技术采用概率、主体连续性和尾部风险。

## 工具与门禁

新增命令：

```bash
cd web
npm run audit:proper-time-differential
```

当前结果：

```text
Verdict: PASS
Reference verification: PASS
Citation context local review: LOCAL_REVIEW_COMPLETE_REQUIRES_FRESH_REVIEW
Pre-submission review: NEEDS_EXTERNAL_REVIEW_BEFORE_FORMAL_SUBMISSION
Sections: 15
TOC entries: 15
Source cards: 5
Claim-evidence rows: 5
Scenario cards: 5
Scenario evaluations: 5
Qualitative NCG scale rows: 6
Scenario variable rows: 5
Toy NCG protocol rows: 6
NCG formula blocks: 5
Figure plan rows: 4
Citation context rows: 5
Scenario comparison SVG: present
Duplicate class patterns: 0
Data source: src/data/proper-time-differential-waiting-hypothesis.json
```

## 下一步

- 增加 D3 或 Matplotlib 参数敏感性图，展示 `K` 很高但 `P_exit` 或 `P_cont` 很低时 NCG 为负。
- 把 `CITATION_CONTEXT_REVIEW_PACKET.*`、`CITATION_CONTEXT_LOCAL_REVIEW.*` 和 `PRE_SUBMISSION_REVIEW.*` 交给外部 fresh reviewer，回填逐项 PASS / WARN / FAIL 结果，避免把物理来源外推成工程可行性来源。
