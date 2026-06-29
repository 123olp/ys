# Human Infra Web

`web/` 是 Human Infra 的正式 Web 应用目录，采用 Astro + D3 组织科研叙事、书籍转译、预测模型和交互图表。

Astro 负责页面结构、长文叙事、组件化和静态发布；D3 负责机制图、预测有效寿命曲线、LEV 阈值和模型状态读数。MDX 已作为内容层能力接入，后续可用于资料卡片和长文研究页。

## 目录结构

```text
web/
├── AGENTS.md
├── README.md
├── astro.config.mjs
├── package.json
├── public/
│   ├── static/browse/0.3.4/
│   └── use.typekit.net/
│       ├── font-files/
│       └── utz6mli.css
├── scripts/
│   ├── audit-claim-context-alignment.mjs
│   ├── audit-citation-context-risk-triage.mjs
│   ├── audit-citation-context-local-review.mjs
│   ├── audit-effective-immortality-coverage.mjs
│   ├── audit-metric-redshift-paper.mjs
│   ├── audit-controllable-metric-waiting-room-paper.mjs
│   ├── audit-metric-redshift-citation-context-local-review.mjs
│   ├── audit-proper-time-differential-paper.mjs
│   ├── audit-proper-time-differential-citation-context-local-review.mjs
│   ├── audit-proper-time-differential-pre-submission-review.mjs
│   ├── verify-controllable-metric-waiting-room-references.mjs
│   ├── export-controllable-metric-waiting-room-citation-context-review-packet.mjs
│   ├── audit-controllable-metric-waiting-room-citation-context-local-review.mjs
│   ├── audit-controllable-metric-waiting-room-pre-submission-review.mjs
│   ├── export-proper-time-differential-citation-context-review-packet.mjs
│   ├── verify-proper-time-differential-references.mjs
│   ├── export-metric-redshift-citation-context-review-packet.mjs
│   ├── evaluate-metric-redshift-scenarios.mjs
│   ├── audit-fresh-reviewer-citation-results.mjs
│   ├── audit-fresh-reviewer-handoff.mjs
│   ├── audit-high-risk-citation-contexts.mjs
│   ├── audit-pre-submission-review.mjs
│   ├── assemble-fresh-reviewer-citation-results.mjs
│   ├── export-citation-context-review-packet.mjs
│   ├── export-fresh-reviewer-citation-audit-protocol.mjs
│   ├── export-fresh-reviewer-context-packets.mjs
│   ├── export-fresh-reviewer-handoff.mjs
│   ├── export-reference-registry.mjs
│   └── verify-reference-registry.mjs
└── src/
    ├── components/
    │   ├── Hero.astro
    │   ├── MetricGrid.astro
    │   └── SectionHeader.astro
    ├── data/
    │   ├── book-signals.json
    │   ├── effective-immortality-evidence.json
    │   ├── metric-redshift-recursive-waiting.json
    │   ├── proper-time-differential-waiting-hypothesis.json
    │   ├── controllable-metric-waiting-room-hypothesis.json
    │   ├── metric-redshift-recursive-waiting/
    │   │   ├── COVERAGE_AUDIT.json
    │   │   ├── COVERAGE_AUDIT.md
    │   │   ├── CITATION_CONTEXT_REVIEW_PACKET.json
    │   │   ├── CITATION_CONTEXT_REVIEW_PACKET.md
    │   │   ├── CITATION_CONTEXT_LOCAL_REVIEW.json
    │   │   ├── CITATION_CONTEXT_LOCAL_REVIEW.md
    │   │   ├── SCENARIO_EVALUATION_AUDIT.json
    │   │   └── SCENARIO_EVALUATION_AUDIT.md
    │   ├── proper-time-differential-waiting-hypothesis/
    │   │   ├── COVERAGE_AUDIT.json
    │   │   ├── COVERAGE_AUDIT.md
    │   │   ├── CITATION_CONTEXT_REVIEW_PACKET.json
    │   │   ├── CITATION_CONTEXT_REVIEW_PACKET.md
    │   │   ├── CITATION_CONTEXT_LOCAL_REVIEW.json
    │   │   ├── CITATION_CONTEXT_LOCAL_REVIEW.md
    │   │   ├── PRE_SUBMISSION_REVIEW.json
    │   │   ├── PRE_SUBMISSION_REVIEW.md
    │   │   ├── REFERENCE_VERIFICATION.json
    │   │   ├── REFERENCE_VERIFICATION.md
    │   │   └── TOOL_GENERATED_PAGE_SEED.astro
    │   ├── controllable-metric-waiting-room-hypothesis/
    │   │   ├── COVERAGE_AUDIT.json
    │   │   ├── COVERAGE_AUDIT.md
    │   │   ├── CITATION_CONTEXT_REVIEW_PACKET.json
    │   │   ├── CITATION_CONTEXT_REVIEW_PACKET.md
    │   │   ├── CITATION_CONTEXT_LOCAL_REVIEW.json
    │   │   ├── CITATION_CONTEXT_LOCAL_REVIEW.md
    │   │   ├── DERIVATION_PACKAGE.md
    │   │   ├── PRE_SUBMISSION_REVIEW.json
    │   │   ├── PRE_SUBMISSION_REVIEW.md
    │   │   ├── REFERENCE_VERIFICATION.json
    │   │   ├── REFERENCE_VERIFICATION.md
    │   │   └── TOOL_GENERATED_PAGE_SEED.astro
    │   └── effective-immortality-flywheel/
    │       ├── CITATION_AUDIT.json
    │       ├── CITATION_AUDIT.md
    │       ├── CITATION_CONTEXT_REVIEW_PACKET.json
    │       ├── CITATION_CONTEXT_REVIEW_PACKET.md
    │       ├── CITATION_CONTEXT_RISK_TRIAGE.json
    │       ├── CITATION_CONTEXT_RISK_TRIAGE.md
    │       ├── CITATION_CONTEXT_LOCAL_REVIEW.json
    │       ├── CITATION_CONTEXT_LOCAL_REVIEW.md
    │       ├── FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json
    │       ├── FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.md
    │       ├── FRESH_REVIEWER_CITATION_AUDIT_RESULTS_AUDIT.json
    │       ├── FRESH_REVIEWER_CITATION_AUDIT_RESULTS_AUDIT.md
    │       ├── FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.json
    │       ├── FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.md
    │       ├── fresh-reviewer-context-packets/
    │       │   ├── HANDOFF.json
    │       │   ├── HANDOFF.md
    │       │   ├── HANDOFF_AUDIT.json
    │       │   ├── HANDOFF_AUDIT.md
    │       │   ├── RESULT_SCHEMA.json
    │       │   ├── RESULT_SCHEMA.md
    │       │   ├── INDEX.json
    │       │   ├── INDEX.md
    │       │   ├── CTX*.json
    │       │   ├── CTX*.md
    │       │   └── results/
    │       ├── CLAIM_CONTEXT_AUDIT.json
    │       ├── CLAIM_CONTEXT_AUDIT.md
    │       ├── COVERAGE_AUDIT.json
    │       ├── COVERAGE_AUDIT.md
    │       ├── HIGH_RISK_CITATION_CONTEXT_REVIEW.json
    │       ├── HIGH_RISK_CITATION_CONTEXT_REVIEW.md
    │       ├── PRE_SUBMISSION_REVIEW.json
    │       ├── PRE_SUBMISSION_REVIEW.md
    │       ├── REFERENCE_VERIFICATION.json
    │       ├── REFERENCE_VERIFICATION.md
    │       └── references.bib
    ├── layouts/
    │   ├── PaperReaderLayout.astro
    │   └── ResearchLayout.astro
    ├── pages/
    │   ├── index.astro
    │   ├── paper.astro
    │   ├── papers/
    │   │   ├── effective-immortality-flywheel.astro
    │   │   ├── metric-redshift-recursive-waiting.astro
    │   │   ├── proper-time-differential-waiting-hypothesis.astro
    │   │   └── controllable-metric-waiting-room-hypothesis.astro
    │   ├── book.astro
    │   ├── model.astro
    │   └── research-standards.astro
    ├── scripts/
    │   ├── evidence-graph.js
    │   └── model-charts.js
    └── styles/
        └── global.css
```

## 页面职责

- `src/pages/index.astro`：首页，把《奇点更近》学习资料、Human Infra 主体持续性和预测模型放在同一个叙事入口。
- `src/pages/paper.astro`：arXiv HTML papers 风格论文页，用学术阅读器展示 Human Infra 的理论、模型和工具链。
- `src/pages/papers/effective-immortality-flywheel.astro`：独立 arXiv-style working paper 页面，展示有效永生带来的主体持续性加速回报飞轮，不覆盖旧 `/paper/`。
- `src/pages/papers/metric-redshift-recursive-waiting.astro`：独立 arXiv-style working paper 页面，提出度规红移递归等待假设，不覆盖旧 `/paper/` 或有效永生飞轮论文页。
- `src/pages/papers/proper-time-differential-waiting-hypothesis.astro`：独立 arXiv-style working paper 页面，提出“度规红移固有时差分路径”，把黑洞等待室收敛为可审查的未来等待假设。
- `src/pages/papers/controllable-metric-waiting-room-hypothesis.astro`：独立 arXiv-style working paper 页面，提出“可控度规等待室假设”，承载“等待室 -> 技术升级 -> 退出采用 -> 再等待”的递归未来等待模型。
- `src/pages/book.astro`：书籍介绍与 Human Infra 转译，承载章节主线、技术链路和边界说明。
- `src/pages/model.astro`：交互预测模型页，展示寿命、有效时间、主观时间、相对时间和未来选择权的模型位置。
- `src/pages/research-standards.astro`：科研标准页，记录论文阅读、预测模型报告、因果推断、可视化和工具链标准。
- `src/scripts/evidence-graph.js`：D3 证据链图脚本，从页面嵌入的 Evidence Matrix JSON 生成主链、反哺路径、风险通道和因果门禁 SVG。
- `src/scripts/model-charts.js`：D3 图表和模型计算脚本，只表达演示模型，不输出个体死亡日期。
- `public/static/browse/0.3.4/`、`public/use.typekit.net/`：从 arXiv HTML papers 页面下载并复用的 CSS、JS、图标、webmanifest 和归一化 Typekit 字体资源。
- `src/data/book-signals.json`：书籍观点到 Human Infra 变量的结构化映射。
- `src/data/effective-immortality-evidence.json`：有效永生飞轮论文页的结构化数据源，承载 Research Question Brief、Methodology Blueprint、Research Execution Roadmap、Search Strategy Seeds、Systematic Search Protocol、Literature Screening Rubric、Literature Gap Map、Search Execution Register、Candidate Source Verification Register、Candidate Source Extraction Register、Claim Register、Claim Evidence Map、AI Research Failure Mode Audit、AI Task Evidence Register、Reference Registry、变量字典、模型契约、推导图、链路边、技术族和证据等级。
- `src/data/metric-redshift-recursive-waiting.json`：度规红移递归等待假设论文页的结构化研究数据源，承载 Problem Anchor、Paper Plan、贡献注册表、Claim Register、Claim-Evidence Matrix、Claim Maturity Register、Falsifier Register、Source Cards、Source Card Ledger、Scenario Card Template、Scenario Evaluation Registry、Toy NCG Evaluation Protocol、Toy NCG Evaluation Registry、NCG Formula Decomposition、Pre-Submission Review Register、变量契约、模型假设、命题注册表、生命周期状态机、图表计划、引用语境预审、研究协议、失败条件和页面审查契约。
- `src/data/proper-time-differential-waiting-hypothesis.json`：度规红移固有时差分路径专项论文页的结构化研究数据源，承载概念表、核心假设、贡献注册表、生命周期状态机、NCG 变量、可达性阶梯、反证条件、Source Cards、Claim-Evidence Matrix、Scenario Cards、Scenario Evaluation Registry、Qualitative NCG Scale、Scenario Variable Matrix、Toy NCG Evaluation Protocol、NCG Formula Decomposition、数据驱动 SVG 场景比较图、图表计划、引用边界、Citation Context Review Packet、Reference Registry 和页面审计契约。
- `src/data/controllable-metric-waiting-room-hypothesis.json`：可控度规等待室论文页的结构化研究数据源，承载概念表、核心假设、Research Questions、形式化假设、公式、命题、Claim-Evidence、Citation Context、状态机、递归等待链路、变量契约、场景比较、Qualitative Gate Scale、Scenario Evaluation、Scenario Gate Matrix、失败条件、研究协议、Evidence Needs、Evaluation Roadmap、Pre-Submission Review、来源和页面审计契约。
- `src/data/metric-redshift-recursive-waiting/`：红移等待论文页的工具生成 seed、citation context packet、citation context local review、scenario evaluation audit 与 coverage audit 账本，当前包括由 `tools/arxiv_html_paper_tool.py write-page` 生成的 `TOOL_GENERATED_PAGE_SEED.astro`，由 `npm run export:metric-redshift-citation-contexts` 生成的 `CITATION_CONTEXT_REVIEW_PACKET.json` / `CITATION_CONTEXT_REVIEW_PACKET.md`，由 `npm run audit:metric-redshift-citation-contexts-local` 生成的 `CITATION_CONTEXT_LOCAL_REVIEW.json` / `CITATION_CONTEXT_LOCAL_REVIEW.md`，由 `npm run evaluate:metric-redshift` 生成的 `SCENARIO_EVALUATION_AUDIT.json` / `SCENARIO_EVALUATION_AUDIT.md`，以及 `npm run audit:metric-redshift` 生成的 `COVERAGE_AUDIT.json` / `COVERAGE_AUDIT.md`。
- `src/data/proper-time-differential-waiting-hypothesis/`：度规红移固有时差分路径专项论文页的 arXiv 工具 seed、reference verification、citation context packet、citation context local review、pre-submission review 与 coverage audit 目录，当前保存 `TOOL_GENERATED_PAGE_SEED.astro`、`REFERENCE_VERIFICATION.json`、`REFERENCE_VERIFICATION.md`、`CITATION_CONTEXT_REVIEW_PACKET.json`、`CITATION_CONTEXT_REVIEW_PACKET.md`、`CITATION_CONTEXT_LOCAL_REVIEW.json`、`CITATION_CONTEXT_LOCAL_REVIEW.md`、`PRE_SUBMISSION_REVIEW.json`、`PRE_SUBMISSION_REVIEW.md`、`COVERAGE_AUDIT.json` 和 `COVERAGE_AUDIT.md`，用于证明页面由 `tools/arxiv_html_paper_tool.py write-page` 创建、正文消费结构化 JSON 数据源、参考来源可达、引用上下文已打包给外部 reviewer、预提交边界已本地审查，并通过本地结构审计。
- `src/data/controllable-metric-waiting-room-hypothesis/`：可控度规等待室论文页的 arXiv 工具 seed、reference verification、citation context packet、citation context local review、pre-submission review、公式推导包和 coverage audit 目录，当前保存 `TOOL_GENERATED_PAGE_SEED.astro`、`REFERENCE_VERIFICATION.json`、`REFERENCE_VERIFICATION.md`、`CITATION_CONTEXT_REVIEW_PACKET.json`、`CITATION_CONTEXT_REVIEW_PACKET.md`、`CITATION_CONTEXT_LOCAL_REVIEW.json`、`CITATION_CONTEXT_LOCAL_REVIEW.md`、`PRE_SUBMISSION_REVIEW.json`、`PRE_SUBMISSION_REVIEW.md`、`DERIVATION_PACKAGE.md`、`COVERAGE_AUDIT.json` 和 `COVERAGE_AUDIT.md`，用于证明页面由 `tools/arxiv_html_paper_tool.py write-page` 创建，来源入口可达，引用上下文已打包给外部 reviewer，本地提交边界已审查，公式推导符合 formula-derivation 结构，并通过本地结构审计。
- `src/data/effective-immortality-flywheel/`：由 Reference Registry、citation-context review packet、citation-context risk triage、high-risk citation context review、citation-context local review、fresh reviewer citation audit protocol、fresh reviewer context packets、fresh reviewer handoff、fresh reviewer citation results assembly、fresh reviewer citation results audit、primary-source verification、claim-context alignment audit、coverage audit 和 pre-submission review 生成的 `references.bib`、`CITATION_AUDIT.json`、`CITATION_AUDIT.md`、`CITATION_CONTEXT_REVIEW_PACKET.json`、`CITATION_CONTEXT_REVIEW_PACKET.md`、`CITATION_CONTEXT_RISK_TRIAGE.json`、`CITATION_CONTEXT_RISK_TRIAGE.md`、`HIGH_RISK_CITATION_CONTEXT_REVIEW.json`、`HIGH_RISK_CITATION_CONTEXT_REVIEW.md`、`CITATION_CONTEXT_LOCAL_REVIEW.json`、`CITATION_CONTEXT_LOCAL_REVIEW.md`、`FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json`、`FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.md`、`fresh-reviewer-context-packets/`、`FRESH_REVIEWER_CITATION_AUDIT_RESULTS_AUDIT.json`、`FRESH_REVIEWER_CITATION_AUDIT_RESULTS_AUDIT.md`、`FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.json`、`FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.md`、`CLAIM_CONTEXT_AUDIT.json`、`CLAIM_CONTEXT_AUDIT.md`、`REFERENCE_VERIFICATION.json`、`REFERENCE_VERIFICATION.md`、`COVERAGE_AUDIT.json`、`COVERAGE_AUDIT.md`、`PRE_SUBMISSION_REVIEW.json` 和 `PRE_SUBMISSION_REVIEW.md`。正式 `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json` 只有在外部逐项 `results/CTX*.json` 齐全并由 assembler 汇总后才会出现。
- `scripts/audit-effective-immortality-coverage.mjs`：本地覆盖审计器，检查 evidence source alias、AI task fields、research declarations、estimand registry、analysis plan registry 和 AI research failure mode audit 是否能回到 Source Card、Reference Registry 与研究协议契约。
- `scripts/export-metric-redshift-citation-context-review-packet.mjs`：本地红移等待 citation context 外部审查输入包生成器，读取 MRW Claim Register、Claim Evidence Map、Citation Context Register 和 Source Cards，输出 fresh reviewer 可消费的 `CITATION_CONTEXT_REVIEW_PACKET.json` 与 `CITATION_CONTEXT_REVIEW_PACKET.md`。
- `scripts/audit-metric-redshift-citation-context-local-review.mjs`：本地红移等待引用语境边界审查器，读取 citation context packet，输出 `CITATION_CONTEXT_LOCAL_REVIEW.json` 与 `CITATION_CONTEXT_LOCAL_REVIEW.md`；它只记录 safe use、forbidden use、risk tier 和 fresh reviewer focus，不替代外部逐项审查。
- `scripts/evaluate-metric-redshift-scenarios.mjs`：本地红移等待 scenario evaluator，读取 Scenario Evaluation Registry 与 Toy NCG Evaluation Registry，导出 `SCENARIO_EVALUATION_AUDIT.json` 和 `SCENARIO_EVALUATION_AUDIT.md`，用于复现 calibration-only、blocked、cannot-evaluate 等方向性分类。
- `scripts/audit-metric-redshift-paper.mjs`：本地红移等待论文覆盖审计器，检查 Paper Plan、Claim Register、Claim-Evidence Matrix、Claim Maturity Register、Falsifier Register、Source Cards、Source Card Ledger、Scenario Card Template、Scenario Evaluation Registry、Toy NCG Evaluation Protocol、Toy NCG Evaluation Registry、NCG Formula Decomposition、Pre-Submission Review Register、变量契约、模型假设、命题注册表、图表计划、引用语境预审、工具生成 seed、页面必需字符串和 arXiv 论文页章节是否对齐，并输出 coverage audit 账本。
- `scripts/audit-proper-time-differential-paper.mjs`：本地度规红移固有时差分路径论文覆盖审计器，读取结构化 JSON 数据源、页面源码和工具 seed，检查数据集合最低行数、Source Card 引用闭合、Scenario Evaluation 指向已登记场景、Scenario Variable Matrix 使用受控等级且 NCG 分类与场景评估一致、NCG Formula Block 指向已登记变量、F4 `scenario-ncg-matrix-svg` 场景比较图、15 个章节和 TOC、页面数据消费、arXiv DOM 契约和重复 class 属性，并输出 `COVERAGE_AUDIT.json` 与 `COVERAGE_AUDIT.md`。
- `scripts/audit-controllable-metric-waiting-room-paper.mjs`：本地可控度规等待室论文覆盖审计器，读取结构化 JSON 数据源、页面源码、工具 seed、reference verification、citation context packet、citation context local review、pre-submission review 和公式推导包，检查数据集合最低行数、14 个章节和 TOC、Research Questions、Evidence Needs、Evaluation Roadmap、Qualitative Gate Scale、Scenario Evaluation、Scenario Gate Matrix、F1/F2/F3 图表、推导包必需段落、页面数据消费、arXiv DOM 契约和重复 class 属性，并输出 `COVERAGE_AUDIT.json` 与 `COVERAGE_AUDIT.md`。
- `scripts/verify-controllable-metric-waiting-room-references.mjs`：本地可控度规等待室参考来源可达性核验器，读取 `sourceRows`，使用 curl 和本地路由检查生成 `REFERENCE_VERIFICATION.json` 与 `REFERENCE_VERIFICATION.md`；它证明来源入口可达，不证明来源支持具体主张。
- `scripts/export-controllable-metric-waiting-room-citation-context-review-packet.mjs`：本地可控度规等待室 citation context 外部审查输入包生成器，读取 Claim-Evidence、Citation Context 和 Source Rows，输出 fresh reviewer 可消费的 `CITATION_CONTEXT_REVIEW_PACKET.json` 与 `CITATION_CONTEXT_REVIEW_PACKET.md`。
- `scripts/audit-controllable-metric-waiting-room-citation-context-local-review.mjs`：本地可控度规等待室引用语境边界审查器，读取 citation context packet，输出 `CITATION_CONTEXT_LOCAL_REVIEW.json` 与 `CITATION_CONTEXT_LOCAL_REVIEW.md`；它只记录 safe use、forbidden use、risk tier 和 fresh reviewer focus，不替代外部逐项审查。
- `scripts/audit-controllable-metric-waiting-room-pre-submission-review.mjs`：本地可控度规等待室预提交审查器，读取结构化数据、页面源码、reference verification、citation context packet 和 citation context local review，检查 working paper 边界、非预测器边界、外部审查边界、文风和提交阻塞项，输出 `PRE_SUBMISSION_REVIEW.json` 与 `PRE_SUBMISSION_REVIEW.md`。
- `scripts/export-proper-time-differential-citation-context-review-packet.mjs`：本地度规红移固有时差分路径 citation context 外部审查输入包生成器，读取 Source Cards、Claim-Evidence Matrix、Citation Context Rows 和 Reference Registry，输出 fresh reviewer 可消费的 `CITATION_CONTEXT_REVIEW_PACKET.json` 与 `CITATION_CONTEXT_REVIEW_PACKET.md`。
- `scripts/audit-proper-time-differential-citation-context-local-review.mjs`：本地度规红移固有时差分路径引用语境边界审查器，读取 citation context packet，输出 `CITATION_CONTEXT_LOCAL_REVIEW.json` 与 `CITATION_CONTEXT_LOCAL_REVIEW.md`；它只记录 safe use、forbidden use、risk tier 和 fresh reviewer focus，不替代外部逐项审查。
- `scripts/verify-proper-time-differential-references.mjs`：本地度规红移固有时差分路径参考来源可达性核验器，读取 Reference Registry，使用 curl 和本地路由检查生成 `REFERENCE_VERIFICATION.json` 与 `REFERENCE_VERIFICATION.md`；它证明来源入口可达，不证明来源支持具体主张。
- `scripts/audit-proper-time-differential-pre-submission-review.mjs`：本地度规红移固有时差分路径预提交审查器，读取结构化数据、页面源码、Reference Verification、Citation Context Review Packet 和 Citation Context Local Review，检查提交边界、非预测器边界、外部审查边界、AI 文风词和 em dash，输出 `PRE_SUBMISSION_REVIEW.json` 与 `PRE_SUBMISSION_REVIEW.md`；当前只允许作为 Human Infra working paper，不允许被标记为正式物理、工程可行性或医学决策论文。
- `scripts/audit-claim-context-alignment.mjs`：本地 claim-context 对齐审计器，检查 CL1-CL7、CTX1-CTX12、supports / doesNotSupport、Reference Registry 反向覆盖和 Reference Verification FAIL 状态。
- `scripts/audit-pre-submission-review.mjs`：本地预提交审查器，检查论文、页面和 source-note 的版本漂移、必需边界、AI 文风词、em dash、核心审计产物和已知提交阻塞项。
- `scripts/export-citation-context-review-packet.mjs`：本地外部审查输入包生成器，把 CL1-CL7、CTX1-CTX12、Reference Registry、supports 和 doesNotSupport 边界组织成 fresh reviewer 可直接消费的 JSON/Markdown。
- `scripts/audit-citation-context-risk-triage.mjs`：本地 L3 引用语境风险分诊器，把 12 个 citation context 按过度外推风险、边界敏感性、参考文献 WARN/FAIL 和主张类型分层，输出 fresh reviewer 优先级队列。
- `scripts/audit-high-risk-citation-contexts.mjs`：本地 HIGH/BLOCKER 引用语境来源边界审查器，只处理风险分诊中最高风险上下文，输出来源角色、支持范围、不可支持范围和后续 fresh reviewer 要求。
- `scripts/audit-citation-context-local-review.mjs`：本地全量引用语境来源边界审查器，覆盖 CTX1-CTX12 的 safe use、forbidden use、reference state 和 fresh reviewer focus，输出全量本地审查账本。
- `scripts/export-fresh-reviewer-citation-audit-protocol.mjs`：外部 fresh reviewer 审稿协议导出器，读取 citation-context packet、risk triage、local review、high-risk review、Reference Verification 和 Citation Audit，输出 reviewer independence contract、pass gate、review queue 和逐项 prompt。
- `scripts/export-fresh-reviewer-context-packets.mjs`：外部 fresh reviewer 分件包导出器，把 CTX1-CTX12 拆成独立 JSON/Markdown packet 和可复制结果 stub，方便逐条审稿和回填。
- `scripts/export-fresh-reviewer-handoff.mjs`：外部 fresh reviewer 单文件交接包生成器，读取 fresh reviewer protocol、packet index 和所有 CTX packet，输出 `fresh-reviewer-context-packets/HANDOFF.json`、`HANDOFF.md`、`RESULT_SCHEMA.json` 与 `RESULT_SCHEMA.md`，把独立性契约、返回文件清单、verdict schema、阻塞条件、结果回填 schema 和完整 packet 内容合并成可交给外部审稿人的独立材料；它不生成 reviewer verdict。
- `scripts/audit-fresh-reviewer-handoff.mjs`：外部 fresh reviewer handoff 审计器，验证 `HANDOFF.*`、`RESULT_SCHEMA.*`、`INDEX.*` 和各 CTX packet 的覆盖、schema 编译、source trace hash、结果文件清单和 Markdown 完整性，输出 `HANDOFF_AUDIT.json` 与 `HANDOFF_AUDIT.md`。
- `scripts/assemble-fresh-reviewer-citation-results.mjs`：外部 fresh reviewer 结果汇总器，读取 `fresh-reviewer-context-packets/results/CTX*.json`，先用 Ajv / `RESULT_SCHEMA.json` 做 JSON Schema 校验，再执行本地语义门禁；只有全部 12 个 context 齐全且结构校验通过后，才生成正式 `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`，并写入每个输入文件的 SHA-256；它不会替代 reviewer verdict。
- `scripts/audit-fresh-reviewer-citation-results.mjs`：外部 fresh reviewer 结果账本审计器，生成 reviewer results 模板，若存在真实 `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json` 则验证它是否由 assembler 生成、是否能回到 `results/CTX*.json` 输入文件、hash 是否匹配、每个 context 是否含 reviewer verdict、source URL、resolution status 和 blocking conditions。
- `scripts/export-reference-registry.mjs`：本地引用产物生成器，读取 Reference Registry 并生成 BibTeX 与 citation-audit 账本。
- `scripts/verify-reference-registry.mjs`：本地联网参考文献核验器，使用 DOI/Crossref、arXiv API、官方 URL 和本地 artifact 生成 primary-source verification 账本。

arXiv-style 论文页的可复用工具链已经沉淀在 [`../tools/arxiv-html-paper/`](../tools/arxiv-html-paper/README.md)。校验当前资源：

```bash
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public
```

## 依赖边界

- `astro` / `@astrojs/mdx`：页面构建、MDX 内容层和静态发布。
- `d3`：科研图表和模型可视化。
- `ajv` / `ajv-formats`：只用于本地 fresh reviewer result JSON Schema 验收，不进入浏览器运行时逻辑。

## 正式路线

仓库根目录里的单文件 HTML 只保留为历史原型或快速展示，不再作为新增交互页面的默认位置。

新增 Web 内容按下面顺序进入：

```text
资料卡片
  -> 结构化数据
  -> 页面叙事
  -> D3 组件
  -> 构建校验
```

页面分工保持清晰：

| 页面 | 主要任务 | 不承载 |
| --- | --- | --- |
| `index.astro` | 对外解释 Human Infra 与专项资料的整体价值 | 细节方法论堆叠 |
| `paper.astro` | 承载论文式理论、定义、谱系、模型契约和工具链说明 | 自定义论文阅读器样式或控件逻辑 |
| `papers/effective-immortality-flywheel.astro` | 承载有效永生飞轮 working paper、变量、假设、证据脊梁和研究路线 | 旧 `/paper/` 的 Human Infra 总论文内容 |
| `papers/metric-redshift-recursive-waiting.astro` | 承载度规红移递归等待假设、等待倍率、递归升级和反证边界 | 黑洞接近、轨道控制、太空任务或人体实验步骤 |
| `papers/proper-time-differential-waiting-hypothesis.astro` | 承载度规红移固有时差分路径、物理接口、状态机、净收益模型和反证条件 | 人工黑洞可行性承诺、工程操作方案或个体永生方案 |
| `book.astro` | 承载书籍、作者观点和 Human Infra 转译 | 模型参数实现 |
| `model.astro` | 承载生命路径、有效时间、主观时间、相对时间和未来选择权的模型可视化 | 医疗建议或个人结论 |
| `research-standards.astro` | 承载论文、工具、模型报告和可视化规范 | 宣传文案 |

实现优先级：

1. 先把外部资料做成 [资料卡片](../docs/reference/source-card-system.md)。
2. 再把卡片中的变量、技术信号和限制写入 `src/data/`。
3. 最后在 `src/scripts/` 或 `src/components/` 中实现可复用 D3 / Astro 组件。

## 本地运行

```bash
cd web
npm install
npm run dev -- --host 0.0.0.0 --port 18764
```

Windows 浏览器访问：

```text
http://localhost:18764/
```

构建静态站点：

```bash
cd web
npm run build
```

构建产物在 `web/dist/`，该目录不进入仓库。

检查度规红移递归等待论文数据和页面对齐：

```bash
cd web
npm run audit:metric-redshift
```

该命令会从 `src/data/metric-redshift-recursive-waiting.json` 和 `src/pages/papers/metric-redshift-recursive-waiting.astro` 生成 `src/data/metric-redshift-recursive-waiting/COVERAGE_AUDIT.json` 与 `COVERAGE_AUDIT.md`。

其中 `npm run audit:metric-redshift` 会先运行 `npm run export:metric-redshift-citation-contexts`、`npm run audit:metric-redshift-citation-contexts-local` 和 `npm run evaluate:metric-redshift`，生成引用语境审查输入包、本地引用边界审查账本和 scenario evaluation audit，再执行页面覆盖审计。

检查度规红移固有时差分路径论文页面结构：

```bash
cd web
npm run audit:proper-time-differential
```

该命令会先生成 `REFERENCE_VERIFICATION.*`、`CITATION_CONTEXT_REVIEW_PACKET.*`、`CITATION_CONTEXT_LOCAL_REVIEW.*` 和 `PRE_SUBMISSION_REVIEW.*`，再从 `src/pages/papers/proper-time-differential-waiting-hypothesis.astro` 和 `src/data/proper-time-differential-waiting-hypothesis/TOOL_GENERATED_PAGE_SEED.astro` 生成 `COVERAGE_AUDIT.json` 与 `COVERAGE_AUDIT.md`，检查 15 个章节、Source Cards、Claim-Evidence Matrix、Citation Context Rows、Scenario Cards、F4 `scenario-ncg-matrix-svg` 场景比较图、图表计划、引用 URL、提交边界和 arXiv DOM 契约是否齐全。

检查可控度规等待室论文页面结构：

```bash
cd web
npm run audit:controllable-metric-waiting-room
```

该命令会先生成 `REFERENCE_VERIFICATION.*`、`CITATION_CONTEXT_REVIEW_PACKET.*`、`CITATION_CONTEXT_LOCAL_REVIEW.*` 和 `PRE_SUBMISSION_REVIEW.*`，再从 `src/data/controllable-metric-waiting-room-hypothesis.json`、`src/pages/papers/controllable-metric-waiting-room-hypothesis.astro`、`src/data/controllable-metric-waiting-room-hypothesis/TOOL_GENERATED_PAGE_SEED.astro` 和 `DERIVATION_PACKAGE.md` 生成 `COVERAGE_AUDIT.json` 与 `COVERAGE_AUDIT.md`，检查工具 seed、14 个章节、F1/F2/F3 图表、形式化推导、Claim-Evidence、Citation Context、Pre-Submission Review、Scenario Gate Matrix、引用 URL、结构化数据渲染和 arXiv DOM 契约是否齐全。

导出有效永生飞轮论文引用产物：

```bash
cd web
npm run export:references
```

该命令会从 `src/data/effective-immortality-evidence.json` 生成 `src/data/effective-immortality-flywheel/references.bib`、`CITATION_AUDIT.json` 和 `CITATION_AUDIT.md`。

联网核验有效永生飞轮论文参考文献：

```bash
cd web
npm run verify:references
```

该命令会从 `src/data/effective-immortality-evidence.json` 读取 Reference Registry，对 DOI/Crossref、arXiv API、官方 URL 和本地 artifact 做 primary-source verification，并生成 `REFERENCE_VERIFICATION.json` 与 `REFERENCE_VERIFICATION.md`。

检查有效永生飞轮论文主张和引用上下文对齐：

```bash
cd web
npm run audit:claim-context
```

该命令会检查 CL1-CL7 是否都有 claim evidence row，CTX1-CTX12 是否都有 supports / doesNotSupport 边界，每个 context 是否能回到 Reference Registry，并确认 `REFERENCE_VERIFICATION.json` 中没有 FAIL，最后生成 `CLAIM_CONTEXT_AUDIT.json` 与 `CLAIM_CONTEXT_AUDIT.md`。

导出逐句 citation-context 外部审查输入包：

```bash
cd web
npm run export:citation-contexts
```

该命令会把 Claim Register、Claim Evidence Map、Citation Context Register 和 Reference Registry 组织成 fresh reviewer 可直接核对的 `CITATION_CONTEXT_REVIEW_PACKET.json` 与 `CITATION_CONTEXT_REVIEW_PACKET.md`。它不是审查结论，只是外部审查输入。

生成逐句 citation-context 风险分诊：

```bash
cd web
npm run audit:citation-risk
```

该命令会读取 citation-context review packet、Reference Verification 和 Claim Context Audit，输出 `CITATION_CONTEXT_RISK_TRIAGE.json` 与 `CITATION_CONTEXT_RISK_TRIAGE.md`。它只做本地风险分层，不替代 fresh reviewer 的逐句来源判断。

审查 HIGH/BLOCKER 引用语境来源边界：

```bash
cd web
npm run audit:high-risk-citations
```

该命令会读取 citation-context risk triage，只处理 HIGH/BLOCKER 上下文，输出 `HIGH_RISK_CITATION_CONTEXT_REVIEW.json` 与 `HIGH_RISK_CITATION_CONTEXT_REVIEW.md`。它记录可访问来源、支持范围、不可支持范围和后续 fresh reviewer 要求，不替代独立逐句审查。

审查全部 citation context 本地来源边界：

```bash
cd web
npm run audit:citation-contexts-local
```

该命令会读取 citation-context review packet、risk triage、Reference Verification、Claim Context Audit 和 high-risk review，覆盖 CTX1-CTX12，输出 `CITATION_CONTEXT_LOCAL_REVIEW.json` 与 `CITATION_CONTEXT_LOCAL_REVIEW.md`。它固定 safe use、forbidden use、reference state 和 fresh reviewer focus，不替代独立逐句审查。

导出 fresh reviewer 引用语境审稿协议：

```bash
cd web
npm run export:fresh-reviewer-protocol
```

该命令会读取 citation-context review packet、risk triage、local review、high-risk review、Reference Verification 和 Citation Audit，输出 `FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json` 与 `FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.md`。它把剩余外部审稿变成 reviewer independence contract、pass gate、review queue 和逐项 prompt，不替代 reviewer verdict。

导出 fresh reviewer 分件审稿包：

```bash
cd web
npm run export:fresh-reviewer-context-packets
```

该命令会读取 `FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json`，把 12 个 citation context 拆成 `fresh-reviewer-context-packets/INDEX.*` 和 `CTX*.json` / `CTX*.md`。每个 packet 都包含 reviewer prompt、来源表、safe use、forbidden use 和可复制的 result stub，方便外部审稿人逐项回填。

导出 fresh reviewer 单文件交接包：

```bash
cd web
npm run export:fresh-reviewer-handoff
```

该命令会读取 `FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json`、`fresh-reviewer-context-packets/INDEX.*` 和全部 `CTX*.json` / `CTX*.md`，生成 `fresh-reviewer-context-packets/HANDOFF.json`、`HANDOFF.md`、`RESULT_SCHEMA.json` 与 `RESULT_SCHEMA.md`。`HANDOFF.md` 是给外部审稿人的独立消费包，包含 independence contract、返回文件清单、verdict schema、阻塞条件、source trace 和全部 packet 内容；`RESULT_SCHEMA.json` 是每个 `results/CTX*.json` 的回填契约。它们不替代 reviewer verdict，也不会写出正式 results 账本。

审计 fresh reviewer 单文件交接包：

```bash
cd web
npm run audit:fresh-reviewer-handoff
```

该命令会验证 `HANDOFF.*`、`RESULT_SCHEMA.*`、`INDEX.*` 和各 CTX packet 是否完整、hash 可回溯、schema 可编译、packet 覆盖 12 个 context，并生成 `fresh-reviewer-context-packets/HANDOFF_AUDIT.json` 与 `HANDOFF_AUDIT.md`。它不替代 reviewer verdict。

汇总 fresh reviewer 逐项结果：

```bash
cd web
npm run assemble:fresh-reviewer-results
```

该命令会读取 `fresh-reviewer-context-packets/results/CTX*.json`。只有全部 12 个 context 结果文件齐全，且每个文件包含 reviewer identity、source URL、verdict、resolution status、reason 和 trace path 时，才会写出正式 `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`。正式账本会记录每个输入文件的 SHA-256；若未齐全，只更新 `results/README.md` 并保持外部审稿 gate pending。

生成或验证 fresh reviewer 结果账本：

```bash
cd web
npm run audit:fresh-reviewer-results
```

该命令会生成 `FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.json`、`FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.md`、`FRESH_REVIEWER_CITATION_AUDIT_RESULTS_AUDIT.json` 和 `FRESH_REVIEWER_CITATION_AUDIT_RESULTS_AUDIT.md`。如果真实 reviewer 结果文件还不存在，verdict 为 `PENDING_EXTERNAL_REVIEW_RESULTS`；如果将来存在 `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`，该命令会验证它是否由 assembler 生成、是否保留逐项 `results/CTX*.json` 输入、hash 是否匹配、是否覆盖 12 个 context、是否含 source URL、是否存在 WRONG/PRESENT/未解决改写等阻塞项。

检查有效永生飞轮论文证据覆盖：

```bash
cd web
npm run audit:effective-immortality
```

该命令会检查 `evidenceEdges[*].sources`、`technologyFamilies[*].evidenceSources` 中的来源别名是否能回到 Source Card 和 Reference Registry，检查 `aiTaskEvidenceRegister[*].referenceKey` 是否存在于 Reference Registry，并检查 AI task evidence 是否补齐 full-text verification 与 method-audit 必填字段，同时检查 Research Question Brief、Methodology Blueprint、Search Strategy Seeds、Systematic Search Protocol、Literature Screening Rubric、Literature Gap Map、Search Execution Register、Candidate Source Verification Register、Candidate Source Extraction Register、research declarations、`estimandRegistry`、`analysisPlanRegistry` 和 `aiResearchFailureModeAudit` 是否齐全，最后生成 `COVERAGE_AUDIT.json` 与 `COVERAGE_AUDIT.md`。

检查有效永生飞轮论文预提交状态：

```bash
cd web
npm run audit:pre-submission
```

该命令会检查 working paper、Web paper page、Evidence Matrix、derivation package、citation audit notes 和结构化数据是否存在版本漂移，确认必需非主张边界存在，扫描常见 AI 文风词和 em dash，并检查核心审计产物状态，最后生成 `PRE_SUBMISSION_REVIEW.json` 与 `PRE_SUBMISSION_REVIEW.md`。

一键重建有效永生飞轮论文科研完整性产物：

```bash
cd web
npm run audit:paper-integrity
```

该命令按顺序执行引用导出、citation-context review packet 导出、primary-source reference verification、claim-context alignment audit、citation-context risk triage、high-risk citation context review、citation-context local review、fresh reviewer protocol export、fresh reviewer results audit、fresh reviewer context packet export、fresh reviewer handoff export、fresh reviewer handoff audit、fresh reviewer results assembly、第二次 fresh reviewer results audit、coverage audit 和 pre-submission review，适合在论文页提交或推送前运行。

## 设计边界

- 本目录是 Web 展示和研究解释层，不承载采集脚本、个人预测服务或医学决策逻辑。
- 预测模型图表只展示群体/模型层面的路径位移、阈值和预算变化。
- 正式研究结论必须回到 `docs/reference/` 的模型契约、证据政策和治理文档。
