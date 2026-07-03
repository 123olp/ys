# Human Infra Maturity Roadmap

本文档定义 Human Infra 从“讲清楚价值”走向“严肃研究框架”和“可运行定量模型”的 100% 状态。它不是宣传稿，而是验收契约：任何阶段都必须能说明目标、对象、边界、证据、模型和不能外推的部分。

机器可读缺口账本见 [`human-infra-maturity-gap-register.json`](human-infra-maturity-gap-register.json)。路线图负责解释 100% 状态，缺口账本负责把当前未完成项拆成 gate、证据路径、缺失证据和下一步动作，并由 `make maturity-gap-audit` 检查。

模型准入契约见 [`human-infra-model-admission-contract.json`](human-infra-model-admission-contract.json)，由 `make model-admission-contract-audit` 检查 L0-L5 准入层级、MAC gates、hard abort gates、方法锚点和当前 B1-B5 reviewed artifacts 的 L1/L2-only 边界。该契约只打开“如何拒绝错误准入”和“如何进入下一步候选注册表”，不打开校准预测、干预效果或个体用途。

模型准入候选注册表见 [`human-infra-model-admission-candidate-registry.json`](human-infra-model-admission-candidate-registry.json)，由 `make model-admission-candidate-registry-audit` 检查 7 个 reviewed artifact registers、1170 个 reviewed artifacts、32 个 blocked rows、现有 L3 synthetic / public aggregate baseline 和 blocked L4 NHATS candidates 的准入边界。该注册表只证明“当前哪些材料被拒绝升格”，不证明任何 calibrated model 已成立。

页面级主张一致性账本见 [`human-infra-page-claim-consistency.json`](human-infra-page-claim-consistency.json)，由 `make page-claim-audit` 检查 README、Web 首页、论文页和关键 reference 页面是否都保留同一组 Claim ID 与禁止用途边界。

受众-主张映射账本见 [`human-infra-audience-claim-map.json`](human-infra-audience-claim-map.json)，由 `make audience-claim-map-audit` 检查研究者、构建者、长寿读者、基础设施读者、治理审查者和模型开发者是否都通过同一 Claim spine 理解项目，并保留邻近项目边界与禁止误读。

论文页强主张账本见 [`human-infra-paper-claim-register.json`](human-infra-paper-claim-register.json)，由 `make paper-claim-audit` 检查每个 arXiv-style 论文页是否注册了论文级强主张、核心 Claim ID、反证条件、降级动作和禁止用途边界。

域级反证覆盖账本见 [`human-infra-domain-falsifier-coverage.json`](human-infra-domain-falsifier-coverage.json)，由 `make domain-falsifier-audit` 检查 C1 全域和优先 C2 域是否具备强主张、变量接口、反证条件、降级动作和禁止用途脚手架。

反证 Source Card 锚点回填账本见 [`human-infra-falsifier-source-card-backfill.json`](human-infra-falsifier-source-card-backfill.json)，由 `make falsifier-source-audit` 检查当前论文强主张和 C1/C2 优先域反证是否具备来源锚点、证据角色、可用范围、迁移边界和后续 Source Card 动作。

反证 Source Card 字段级抽取账本见 [`human-infra-falsifier-source-card-extraction.json`](human-infra-falsifier-source-card-extraction.json)，由 `make falsifier-source-extraction-audit` 检查当前全部来源锚点是否进入来源身份、域、论文 claim、模型位置、反证用途、迁移边界和人工可读包。

域级 Claim-Evidence Matrix 见 [`human-infra-domain-claim-evidence-matrix.json`](human-infra-domain-claim-evidence-matrix.json)，由 `make domain-claim-matrix-audit` 检查当前 26 个优先研究域是否 join 到域强主张来源、变量契约来源、反证来源、字段级 Source Card ID、禁止用途和下一步抽取动作。

域 Source Card 字段抽取账本见 [`human-infra-domain-source-card-field-extraction.json`](human-infra-domain-source-card-field-extraction.json)，由 `make domain-field-extraction-audit` 检查当前 26 个优先研究域是否具备 endpoint 候选、population 槽位、uncertainty 槽位、transfer-boundary 槽位、禁止用途和 source-specific 深读动作。

域-来源深读队列见 [`human-infra-domain-source-specific-extraction-queue.json`](human-infra-domain-source-specific-extraction-queue.json)，由 `make domain-source-queue-audit` 检查 26 个域字段行是否派生为 81 个 domain-source 精读任务，并确认 exact claim、endpoint、population、uncertainty 和 transfer-boundary 精读完成前仍禁止校准预测、个体建议和域主张升级。

域-来源精读完成寄存器见 [`human-infra-domain-source-specific-extraction-register.json`](human-infra-domain-source-specific-extraction-register.json)，由 `make domain-source-extraction-audit` 检查 81/81 个 domain-source 精读字段行是否已经绑定到 exact claim、endpoint、population、uncertainty、transfer-boundary 和模型准入阻塞语义。当前已完成方法锚点、生物机制、价值框架、认知扩展、脑保存、数字孪生、未来等待、AI 治理和筛查偏倚边界的字段级抽取；这些行仍必须经过外部文献 fresh review、变量卡晋升和模型校准门禁，才能进入更高等级证据。

域-来源卡片晋升队列见 [`human-infra-domain-source-card-promotion-queue.json`](human-infra-domain-source-card-promotion-queue.json)，由 `make domain-source-promotion-audit` 检查 81 个完成字段行是否一一派生为 source-context fresh review、Source Card、变量卡、endpoint 卡、uncertainty 卡、transfer-boundary 卡和 downgrade check 任务。该队列只是下一步执行队列，不证明任何晋升任务已经完成，也不打开校准预测、个体建议或干预排序。

来源语境本地复核账本见 [`human-infra-source-context-local-review-register.json`](human-infra-source-context-local-review-register.json)，由 `make source-context-local-review-audit` 检查当前 20 个来源锚点是否反查到 81 个晋升任务、26 个受影响域、来源证据、阻塞用途和索引入口。该账本只是本地 source-context 复核，不等于独立 fresh review、Source Card 晋升完成或模型准入。

卡片晋升预注册账本见 [`human-infra-card-promotion-prep-register.json`](human-infra-card-promotion-prep-register.json)，由 `make card-promotion-prep-audit` 检查当前 81 个本地复核晋升任务是否已经预分配 486 个 Source/变量/endpoint/uncertainty/transfer/downgrade 待产物 ID、评审问题、阻塞用途和索引入口。该账本只是卡片晋升执行前的准备包，不等于独立 fresh review 或卡片完成。

独立 fresh review 协议见 [`human-infra-independent-fresh-review-protocol.json`](human-infra-independent-fresh-review-protocol.json)，由 `make independent-fresh-review-protocol-audit` 检查 81 个准备包如何按四个批次进入独立审查。该协议只定义审查批次、字段和晋升规则，不保存任何 fresh review verdict。

独立 fresh review verdict 账本见 [`human-infra-independent-fresh-review-verdict-register.json`](human-infra-independent-fresh-review-verdict-register.json)，由 `make independent-fresh-review-verdict-audit` 检查 FRB-01 到 FRB-04 的 20 个来源锚点、81 个准备包是否全部完成独立 fresh review verdict，并确认这些 verdict 只允许 bounded artifact filling，不打开校准预测、个体建议、个体死亡日期、干预排序、域主张升级或临床有效性声明。

Reviewed card artifact 账本见 [`human-infra-reviewed-card-artifact-register.json`](human-infra-reviewed-card-artifact-register.json)，由 `make reviewed-card-artifact-audit` 检查 81 个已审查晋升包是否落成 486 个 reviewed Source/variable/endpoint/uncertainty/transfer-boundary/downgrade artifact 实体，并确认它们仍不打开模型准入、个体建议、个体死亡日期、干预排序、域主张升级或临床有效性声明。

Future-boundary route card 账本见 [`human-infra-future-boundary-route-card-register.json`](human-infra-future-boundary-route-card-register.json)，由 `make future-boundary-route-card-audit` 检查未来等待、生物停滞、神经身份连续性和 AI 加速四条高优先路线是否统一暴露技术窗口、接入、采用、持续期、可组合性、尾部风险和机会成本门，并确认路线可行性、校准预测和个体用途仍被阻塞。

C2 长尾覆盖账本见 [`human-infra-c2-longtail-coverage-register.json`](human-infra-c2-longtail-coverage-register.json)，由 `make c2-longtail-coverage-audit` 检查 `classification.tsv` 中全部 204 个 C2 源体维护域是否进入覆盖账本，并明确当前 20 个 priority reviewed-artifact covered 域与 184 个仍缺 Claim-Evidence/source/fresh-review/card artifact 的长尾域。

C2 长尾第一批晋升队列见 [`human-infra-c2-longtail-first-batch-promotion-queue.json`](human-infra-c2-longtail-first-batch-promotion-queue.json)，由 `make c2-longtail-first-batch-promotion-audit` 检查 24 个高影响未覆盖 C2 域是否绑定覆盖账本、候选来源、claim seed、variable seed、晋升步骤和禁止用途边界。该队列只是执行入口，不证明 Source Card、fresh review、变量卡、endpoint 卡、downgrade check 或模型准入已经完成。

C2 长尾第一批来源深读队列见 [`human-infra-c2-longtail-first-batch-source-extraction-queue.json`](human-infra-c2-longtail-first-batch-source-extraction-queue.json)，由 `make c2-longtail-first-batch-source-extraction-audit` 检查 C2-LT-B1 是否已经派生为 48 个 domain-source 深读任务，并要求后续逐源抽取 exact claim、endpoint、population/setting、mechanism/effect、uncertainty、transfer boundary、downgrade trigger 和 model position。该队列不证明来源已读完，不打开模型准入。

C2 长尾第一批来源抽取试运行见 [`human-infra-c2-longtail-first-batch-source-extraction-register.json`](human-infra-c2-longtail-first-batch-source-extraction-register.json)，由 `make c2-longtail-first-batch-source-extraction-register-audit` 检查 48/48 个来源是否已经进入字段级抽取。当前覆盖第一批 24 个高影响 C2 长尾域；它不等于 fresh review、Source Card 晋升或模型准入完成。

C2 长尾第一批本地来源语境复核见 [`human-infra-c2-longtail-first-batch-local-review-register.json`](human-infra-c2-longtail-first-batch-local-review-register.json)，由 `make c2-longtail-first-batch-local-review-audit` 检查 48/48 个来源抽取行是否完成本地结构复核、反查队列与抽取账本、保持禁止用途，并且只允许进入 independent fresh review。它不等于 reviewed artifacts、Source Card 晋升或模型准入完成。

C2 长尾第一批独立 fresh review 协议见 [`human-infra-c2-longtail-first-batch-independent-fresh-review-protocol.json`](human-infra-c2-longtail-first-batch-independent-fresh-review-protocol.json)，由 `make c2-longtail-first-batch-independent-fresh-review-protocol-audit` 检查 48 个本地复核行是否拆成 4 个 fresh-review 批次，并把 verdict 字段、降级动作和禁止用途写入协议。

C2 长尾第一批独立 fresh review 判定见 [`human-infra-c2-longtail-first-batch-independent-fresh-review-verdict-register.json`](human-infra-c2-longtail-first-batch-independent-fresh-review-verdict-register.json)，由 `make c2-longtail-first-batch-independent-fresh-review-verdict-audit` 检查当前 48/48 个来源是否已有外部核验证据、reviewer verdict、artifact promotion decision 和阻塞边界。该账本当前已经完成四批 verdict 收口；下一步只允许把 eligible rows 晋升为 reviewed artifacts，仍不打开模型准入。

C2 长尾第一批 reviewed artifact 账本见 [`human-infra-c2-longtail-first-batch-reviewed-card-artifact-register.json`](human-infra-c2-longtail-first-batch-reviewed-card-artifact-register.json)，由 `make c2-longtail-first-batch-reviewed-card-artifact-audit` 检查 42 个 eligible verdict rows 是否晋升为 252 个 reviewed Source/variable/endpoint/uncertainty/transfer-boundary/downgrade artifact，并确认 5 个 downgrade-before-fill 与 1 个 cannot-evaluate 行仍保持 blocked。该账本仍不打开模型准入，也不代表剩余 184 个 C2 长尾域闭合。

C2 长尾第一批 blocked source resolution 账本见 [`human-infra-c2-longtail-first-batch-blocked-source-resolution-register.json`](human-infra-c2-longtail-first-batch-blocked-source-resolution-register.json)，由 `make c2-longtail-first-batch-blocked-source-resolution-audit` 检查 6 个非 eligible rows 是否已经准备来源校正、时效核验和替代候选。该账本只解除下一轮重审的输入阻塞；它不改变原 verdict，不创建 reviewed artifacts，也不打开模型准入。

C2 长尾第一批 source-resolution fresh review 判定账本见 [`human-infra-c2-longtail-first-batch-source-resolution-fresh-review-verdict-register.json`](human-infra-c2-longtail-first-batch-source-resolution-fresh-review-verdict-register.json)，由 `make c2-longtail-first-batch-source-resolution-fresh-review-verdict-audit` 检查 6 个非 eligible rows 的来源纠偏候选是否已经完成 fresh review、16 个候选是否都有用途判定、哪些行只能 route/split，以及所有行是否仍禁止 direct artifact fill 和模型准入。该账本只允许 corrected source re-extraction，不创建 reviewed artifacts。

C2 长尾第一批 corrected source re-extraction 队列见 [`human-infra-c2-longtail-first-batch-corrected-source-reextraction-queue.json`](human-infra-c2-longtail-first-batch-corrected-source-reextraction-queue.json)，由 `make c2-longtail-first-batch-corrected-source-reextraction-queue-audit` 检查 6 个来源纠偏行中的 10 个 selected corrected candidates 是否被派生成重新抽取任务，并确认 6 个 route-only/context 候选只保留为拆分边界。该队列仍不等于 corrected extraction 完成、reviewed artifact 晋升或模型准入。

C2 长尾第一批 corrected source re-extraction 完成寄存器见 [`human-infra-c2-longtail-first-batch-corrected-source-reextraction-register.json`](human-infra-c2-longtail-first-batch-corrected-source-reextraction-register.json)，由 `make c2-longtail-first-batch-corrected-source-reextraction-register-audit` 检查 10/10 个 corrected candidates 是否已经完成 bounded source re-extraction，并确认 6 行只可进入下一轮 independent fresh review 候选、4 行仍保持 route/index/fulltext 阻塞。该寄存器仍不等于 fresh review 通过、reviewed artifact 晋升或模型准入。

C2 长尾第一批 corrected source fresh review 判定账本见 [`human-infra-c2-longtail-first-batch-corrected-source-fresh-review-verdict-register.json`](human-infra-c2-longtail-first-batch-corrected-source-fresh-review-verdict-register.json)，由 `make c2-longtail-first-batch-corrected-source-fresh-review-verdict-audit` 检查 10/10 个 corrected extraction outputs 是否已完成 independent fresh review、5 行是否只允许进入 bounded reviewed artifact prep、5 行是否继续保持 lineage/route/index/fulltext 阻塞。该账本仍不等于 reviewed artifact 已创建或模型准入。

C2 长尾第一批 corrected source reviewed artifact 账本见 [`human-infra-c2-longtail-first-batch-corrected-source-reviewed-card-artifact-register.json`](human-infra-c2-longtail-first-batch-corrected-source-reviewed-card-artifact-register.json)，由 `make c2-longtail-first-batch-corrected-source-reviewed-card-artifact-audit` 检查 5 个 eligible corrected rows 是否晋升为 30 个 bounded reviewed artifacts、5 个 blocked rows 是否仍保持 lineage/route/index/fulltext 边界。该账本仍不打开模型准入，也不代表剩余 184 个 C2 长尾域闭合。

C2 长尾第二批晋升队列见 [`human-infra-c2-longtail-second-batch-promotion-queue.json`](human-infra-c2-longtail-second-batch-promotion-queue.json)，由 `make c2-longtail-second-batch-promotion-audit` 检查 12 个非 B1 的剩余 C2 长尾域是否已绑定 24 个 web-checked 候选来源、晋升步骤和模型阻塞边界。该队列只扩展下一轮 source-specific 深读入口，不等于 Source Card、fresh review、reviewed artifact 或模型准入。

C2 长尾第二批来源深读队列见 [`human-infra-c2-longtail-second-batch-source-extraction-queue.json`](human-infra-c2-longtail-second-batch-source-extraction-queue.json)，由 `make c2-longtail-second-batch-source-extraction-audit` 检查 24 个第二批 domain-source 任务是否具备 exact claim、endpoint、population/setting、mechanism/effect、uncertainty、transfer boundary、downgrade trigger 和 model position 抽取槽位。该队列不证明来源已读完，不打开 fresh review、reviewed artifact 或模型准入。

C2 长尾第二批来源抽取寄存器见 [`human-infra-c2-longtail-second-batch-source-extraction-register.json`](human-infra-c2-longtail-second-batch-source-extraction-register.json)，由 `make c2-longtail-second-batch-source-extraction-register-audit` 检查 24/24 个第二批来源是否已经完成本地字段级抽取，并确认它们只可进入本地来源语境复核。该寄存器不等于 independent fresh review、reviewed artifact 或模型准入完成。

C2 长尾第二批本地来源语境复核见 [`human-infra-c2-longtail-second-batch-local-review-register.json`](human-infra-c2-longtail-second-batch-local-review-register.json)，由 `make c2-longtail-second-batch-local-review-audit` 检查 24/24 个第二批抽取行是否完成本地结构复核、反查队列与抽取寄存器、保持禁止用途，并且只允许进入 independent fresh review。它不等于 reviewed artifacts、Source Card 晋升或模型准入完成。

C2 长尾第二批 independent fresh review 协议见 [`human-infra-c2-longtail-second-batch-independent-fresh-review-protocol.json`](human-infra-c2-longtail-second-batch-independent-fresh-review-protocol.json)，由 `make c2-longtail-second-batch-independent-fresh-review-protocol-audit` 检查 24 个本地复核行是否拆成 2 个 fresh-review 批次，并把 required verdict fields、verdict taxonomy、artifact promotion decisions 和 blocked uses 写入协议。该协议不存放 reviewer verdict，不创建 reviewed artifacts，也不打开模型准入。

C2 长尾第二批 independent fresh review 判定见 [`human-infra-c2-longtail-second-batch-independent-fresh-review-verdict-register.json`](human-infra-c2-longtail-second-batch-independent-fresh-review-verdict-register.json)，由 `make c2-longtail-second-batch-independent-fresh-review-verdict-audit` 检查 24/24 个来源是否已有 fresh-review evidence、reviewer verdict、artifact promotion decision 和阻塞边界。当前 18 行 support-with-boundary、5 行 bounded-support、1 行 downgrade-required；下一步只允许 23 个 eligible rows 晋升为 bounded reviewed artifacts，仍不打开模型准入。

C2 长尾第二批 reviewed artifact 账本见 [`human-infra-c2-longtail-second-batch-reviewed-card-artifact-register.json`](human-infra-c2-longtail-second-batch-reviewed-card-artifact-register.json)，由 `make c2-longtail-second-batch-reviewed-card-artifact-audit` 检查 23 个 eligible verdict rows 是否晋升为 138 个 reviewed Source/variable/endpoint/uncertainty/transfer-boundary/downgrade artifacts，并确认 1 个 downgrade-before-fill row 仍保持 blocked。该账本仍不打开模型准入，也不代表剩余 C2 长尾域闭合。

C2 长尾第三批晋升队列见 [`human-infra-c2-longtail-third-batch-promotion-queue.json`](human-infra-c2-longtail-third-batch-promotion-queue.json)，由 `make c2-longtail-third-batch-promotion-audit` 检查 12 个非 B1/B2 的神经-感知-认知连续性域是否已绑定 24 个 web-checked 候选来源、晋升步骤和模型阻塞边界。该队列只扩展下一轮 source-specific 深读入口，不等于 Source Card、fresh review、reviewed artifact 或模型准入。

C2 长尾第三批来源深读队列见 [`human-infra-c2-longtail-third-batch-source-extraction-queue.json`](human-infra-c2-longtail-third-batch-source-extraction-queue.json)，由 `make c2-longtail-third-batch-source-extraction-audit` 检查 24 个第三批 domain-source 任务是否具备 exact claim、endpoint、population/setting、mechanism/effect、uncertainty、transfer boundary、downgrade trigger 和 model position 抽取槽位。该队列不证明来源已读完，不打开 fresh review、reviewed artifact 或模型准入。

C2 长尾第三批来源抽取寄存器见 [`human-infra-c2-longtail-third-batch-source-extraction-register.json`](human-infra-c2-longtail-third-batch-source-extraction-register.json)，由 `make c2-longtail-third-batch-source-extraction-register-audit` 检查 24/24 个第三批来源是否已经完成本地字段级来源语境抽取，并确认错源、标题/分卷错配、访问受限、降级触发和模型阻塞边界被保留。该寄存器不等于本地复核、independent fresh review、reviewed artifacts 或模型准入完成。

C2 长尾第三批本地来源语境复核见 [`human-infra-c2-longtail-third-batch-local-review-register.json`](human-infra-c2-longtail-third-batch-local-review-register.json)，由 `make c2-longtail-third-batch-local-review-audit` 检查 24/24 个第三批来源抽取行是否完成本地结构复核、反查队列与抽取寄存器、保持禁止用途，并保留 5 个错源/错配/访问受限问题行。该账本只允许进入 independent fresh review 或 source-resolution，不等于 reviewed artifacts、Source Card 晋升或模型准入完成。

C2 长尾第三批 source-resolution 账本见 [`human-infra-c2-longtail-third-batch-source-resolution-register.json`](human-infra-c2-longtail-third-batch-source-resolution-register.json)，由 `make c2-longtail-third-batch-source-resolution-audit` 检查 5 个本地复核问题行是否已准备 7 个 corrected、split 或 route-normalized 候选，并确认它们仍必须进入 independent fresh review、corrected re-extraction 和 reviewed artifact 门禁。该账本不创建 reviewed artifacts，也不打开模型准入。

C2 长尾第三批 independent fresh review 协议见 [`human-infra-c2-longtail-third-batch-independent-fresh-review-protocol.json`](human-infra-c2-longtail-third-batch-independent-fresh-review-protocol.json)，由 `make c2-longtail-third-batch-independent-fresh-review-protocol-audit` 检查 24 个本地复核行是否拆成 2 个 fresh-review 批次，并把 5 个 source-resolution issue rows 纳入纠偏来源检查。该协议不存放 reviewer verdict，不创建 reviewed artifacts，也不打开模型准入。

C2 长尾第三批 independent fresh review 判定见 [`human-infra-c2-longtail-third-batch-independent-fresh-review-verdict-register.json`](human-infra-c2-longtail-third-batch-independent-fresh-review-verdict-register.json)，由 `make c2-longtail-third-batch-independent-fresh-review-verdict-audit` 检查 24/24 个第三批来源是否已有 reviewer verdict、fresh-review evidence、artifact promotion decision、source-resolution routing 和阻塞边界。当前 18 行只允许 bounded artifact fill，5 行只允许 corrected-source re-extraction，1 行必须 downgrade-before-fill；该账本仍不创建 reviewed artifacts，也不打开模型准入。

C2 长尾第三批 corrected source re-extraction 队列见 [`human-infra-c2-longtail-third-batch-corrected-source-reextraction-queue.json`](human-infra-c2-longtail-third-batch-corrected-source-reextraction-queue.json)，由 `make c2-longtail-third-batch-corrected-source-reextraction-queue-audit` 检查 5 个 source-resolution-supported 问题行中的 7 个 corrected/split/route-normalized 候选是否被派生成 source-specific re-extraction 任务。该队列仍不等于 corrected extraction 完成、reviewed artifact 晋升或模型准入。

C2 长尾第三批 corrected source re-extraction 完成寄存器见 [`human-infra-c2-longtail-third-batch-corrected-source-reextraction-register.json`](human-infra-c2-longtail-third-batch-corrected-source-reextraction-register.json)，由 `make c2-longtail-third-batch-corrected-source-reextraction-register-audit` 检查 7/7 个 corrected candidates 是否已经完成 bounded source re-extraction，并确认 5 行只可进入下一轮 independent fresh review 候选、2 行仍保持 route/split 阻塞。该寄存器仍不等于 fresh review 通过、reviewed artifact 晋升或模型准入。

C2 长尾第三批 corrected source fresh review 判定账本见 [`human-infra-c2-longtail-third-batch-corrected-source-fresh-review-verdict-register.json`](human-infra-c2-longtail-third-batch-corrected-source-fresh-review-verdict-register.json)，由 `make c2-longtail-third-batch-corrected-source-fresh-review-verdict-audit` 检查 7/7 个 corrected extraction outputs 是否已完成 independent fresh review、6 行是否只允许进入 bounded reviewed artifact prep、1 行是否继续保持 duplicate/split route 阻塞，并确认 AAO-HNS publisher route 可读事实只进入有界 artifact 准备。该账本仍不等于模型准入。

C2 长尾第三批 reviewed artifact 账本见 [`human-infra-c2-longtail-third-batch-reviewed-card-artifact-register.json`](human-infra-c2-longtail-third-batch-reviewed-card-artifact-register.json)，由 `make c2-longtail-third-batch-reviewed-card-artifact-audit` 检查 18 个原始 eligible 行和 6 个 corrected eligible 行是否生成 144 个 bounded reviewed artifacts，并确认 EXT-022 downgrade-before-fill 与 C2LTB3-CREXT-004 duplicate/split route blocked row 被显式保留。该账本仍不等于剩余 C2 长尾域闭合或模型准入。

C2 长尾第四批晋升队列见 [`human-infra-c2-longtail-fourth-batch-promotion-queue.json`](human-infra-c2-longtail-fourth-batch-promotion-queue.json)，由 `make c2-longtail-fourth-batch-promotion-audit` 检查 12 个非 B1/B2/B3 的代谢、内分泌、肾肝、电解质和携氧稳态连续性域是否已绑定 24 个 web-checked 候选来源、晋升步骤和模型阻塞边界。该队列只扩展下一轮 source-specific 深读入口，不等于 Source Card、fresh review、reviewed artifact 或模型准入。

C2 长尾第四批来源深读队列见 [`human-infra-c2-longtail-fourth-batch-source-extraction-queue.json`](human-infra-c2-longtail-fourth-batch-source-extraction-queue.json)，由 `make c2-longtail-fourth-batch-source-extraction-audit` 检查 24 个第四批 domain-source 任务是否具备 exact claim、endpoint、population/setting、mechanism/effect、uncertainty、transfer boundary、downgrade trigger 和 model position 抽取槽位。该队列不证明来源已读完，不打开 local review、fresh review、reviewed artifact 或模型准入。

C2 长尾第四批来源抽取寄存器见 [`human-infra-c2-longtail-fourth-batch-source-extraction-register.json`](human-infra-c2-longtail-fourth-batch-source-extraction-register.json)，由 `make c2-longtail-fourth-batch-source-extraction-register-audit` 检查 24/24 个第四批来源是否已经完成本地字段级来源语境抽取，并确认无摘要全文复核、重复共识路线、降级触发和模型阻塞边界被保留。该寄存器不等于本地复核、independent fresh review、reviewed artifacts 或模型准入完成。

C2 长尾第四批本地来源语境复核见 [`human-infra-c2-longtail-fourth-batch-local-review-register.json`](human-infra-c2-longtail-fourth-batch-local-review-register.json)，由 `make c2-longtail-fourth-batch-local-review-audit` 检查 24/24 个第四批来源抽取行是否完成本地结构复核、是否反查队列与抽取账本、是否保留 1 个重复共识路线行和 3 个无摘要需全文行，以及是否继续阻塞 reviewed artifacts、Source Card 晋升和模型准入。该账本只打开 independent fresh review / source-resolution 的下一步路由，不等于 fresh review 判定或 artifact 晋升完成。

C2 长尾第四批 source-resolution 账本见 [`human-infra-c2-longtail-fourth-batch-source-resolution-register.json`](human-infra-c2-longtail-fourth-batch-source-resolution-register.json)，由 `make c2-longtail-fourth-batch-source-resolution-audit` 检查 4 个第四批问题行是否已经准备 8 个重复路线、官方指南页、DOI 或全文路线候选，并确认所有候选继续阻塞 fresh review、manual fulltext extraction、reviewed artifacts 和模型准入。该账本不等于全文复核完成，不等于 fresh-review verdict，也不打开 artifact 晋升。

C2 长尾第四批 manual/fulltext extraction 账本见 [`human-infra-c2-longtail-fourth-batch-manual-fulltext-extraction-register.json`](human-infra-c2-longtail-fourth-batch-manual-fulltext-extraction-register.json)，由 `make c2-longtail-fourth-batch-manual-fulltext-extraction-audit` 检查 8 个 source-resolution 候选是否已完成有界全文/官方页路线抽取，并确认 3 个 bounded fresh-review 候选与 5 个 duplicate、route-only 或 manual-access 阻塞行被分开保留。该账本不是 independent fresh-review verdict，不创建 reviewed artifacts，也不打开模型准入。

C2 长尾第四批 manual/fulltext fresh review 判定账本见 [`human-infra-c2-longtail-fourth-batch-manual-fulltext-fresh-review-verdict-register.json`](human-infra-c2-longtail-fourth-batch-manual-fulltext-fresh-review-verdict-register.json)，由 `make c2-longtail-fourth-batch-manual-fulltext-fresh-review-verdict-audit` 检查 8/8 个 manual/fulltext extraction 行是否完成 independent fresh review、3 行是否只允许进入 bounded reviewed artifact prep、5 行是否继续保持 duplicate、route-only、manual-access 或 context-only 阻塞。该账本仍不创建 reviewed artifacts，也不打开模型准入。

C2 长尾第四批 manual/fulltext reviewed artifact 账本见 [`human-infra-c2-longtail-fourth-batch-manual-fulltext-reviewed-card-artifact-register.json`](human-infra-c2-longtail-fourth-batch-manual-fulltext-reviewed-card-artifact-register.json)，由 `make c2-longtail-fourth-batch-manual-fulltext-reviewed-card-artifact-audit` 检查 3 个 eligible manual/fulltext fresh-review rows 是否生成 18 个 bounded reviewed artifacts，并确认 5 个 duplicate、route-only、manual-access 或 context-only blockedRows 被显式保留。该账本只完成有界研究卡片晋升，不等于校准模型准入、个体建议、干预排序、临床有效性主张或死亡日期输出。

C2 长尾第五批晋升队列见 [`human-infra-c2-longtail-fifth-batch-promotion-queue.json`](human-infra-c2-longtail-fifth-batch-promotion-queue.json)，由 `make c2-longtail-fifth-batch-promotion-audit` 检查 12 个第五批细胞质量控制、细胞器通信、分子运输、膜脂韧性、清除和屏障底座 C2 长尾域是否已绑定 24 个 web/API-checked 候选来源、晋升步骤和模型阻塞边界。第五批来源深读队列见 [`human-infra-c2-longtail-fifth-batch-source-extraction-queue.json`](human-infra-c2-longtail-fifth-batch-source-extraction-queue.json)，由 `make c2-longtail-fifth-batch-source-extraction-audit` 检查 24 个候选来源是否已派生成 exact claim、endpoint、population、uncertainty、transfer-boundary、downgrade 和 model-position 抽取任务。第五批来源抽取寄存器见 [`human-infra-c2-longtail-fifth-batch-source-extraction-register.json`](human-infra-c2-longtail-fifth-batch-source-extraction-register.json)，由 `make c2-longtail-fifth-batch-source-extraction-register-audit` 检查 24/24 个来源语境字段抽取是否完成，并确认无开放全文、跨域复用来源、模型生物/综述边界和模型准入阻塞仍被显式保留。第五批本地来源语境复核见 [`human-infra-c2-longtail-fifth-batch-local-review-register.json`](human-infra-c2-longtail-fifth-batch-local-review-register.json)，由 `make c2-longtail-fifth-batch-local-review-audit` 检查 24/24 个抽取行是否完成本地结构复核，并确认 8 个无开放全文或跨域复用问题行仍需 source-resolution/manual fulltext 后才能进入 bounded fresh review。第五批 source-resolution 账本见 [`human-infra-c2-longtail-fifth-batch-source-resolution-register.json`](human-infra-c2-longtail-fifth-batch-source-resolution-register.json)，由 `make c2-longtail-fifth-batch-source-resolution-audit` 检查 8 个问题行是否整理为 14 个 PubMed、Europe PMC、DOI 或 PMC route 候选，并确认 manual/fulltext extraction、fresh review、reviewed artifacts 和模型准入仍被阻塞。第五批 manual/fulltext extraction 账本见 [`human-infra-c2-longtail-fifth-batch-manual-fulltext-extraction-register.json`](human-infra-c2-longtail-fifth-batch-manual-fulltext-extraction-register.json)，由 `make c2-longtail-fifth-batch-manual-fulltext-extraction-audit` 检查 14 个候选是否已完成有界路线/全文上下文抽取，并确认只有 2 个 PMC 主路线进入 bounded fresh-review 候选、12 个 route-only/manual-access/duplicate 行继续阻塞。第五批 independent fresh review 判定账本见 [`human-infra-c2-longtail-fifth-batch-independent-fresh-review-verdict-register.json`](human-infra-c2-longtail-fifth-batch-independent-fresh-review-verdict-register.json)，由 `make c2-longtail-fifth-batch-independent-fresh-review-verdict-audit` 检查 16 个非问题来源抽取行和 14 个 manual/fulltext 行是否已完成 independent fresh review、17 行是否只允许进入 bounded reviewed artifact prep、13 个 manual route-only、manual-access、duplicate 或 context-only 行是否继续阻塞，并确认模型准入仍为 0。第五批 reviewed artifact 账本见 [`human-infra-c2-longtail-fifth-batch-reviewed-card-artifact-register.json`](human-infra-c2-longtail-fifth-batch-reviewed-card-artifact-register.json)，由 `make c2-longtail-fifth-batch-reviewed-card-artifact-audit` 检查 17 个 eligible fresh-review rows 是否生成 102 个有界 reviewed artifacts、13 个 blocked manual rows 是否显式保留，并确认模型准入仍阻塞。

C2 长尾第六批晋升队列见 [`human-infra-c2-longtail-sixth-batch-promotion-queue.json`](human-infra-c2-longtail-sixth-batch-promotion-queue.json)，由 `make c2-longtail-sixth-batch-promotion-audit` 检查 12 个第六批跨代连续性、生殖力、孕产新生儿、儿童免疫、儿童铅暴露、儿童喂养吞咽、哺乳和儿童口腔健康 C2 长尾域是否已绑定 24 个 web-checked 候选来源、晋升步骤和模型阻塞边界。第六批来源深读队列见 [`human-infra-c2-longtail-sixth-batch-source-extraction-queue.json`](human-infra-c2-longtail-sixth-batch-source-extraction-queue.json)，由 `make c2-longtail-sixth-batch-source-extraction-audit` 检查 24 个候选来源是否已派生成 exact claim、endpoint、population、uncertainty、transfer-boundary、downgrade 和 model-position 抽取任务。第六批来源抽取寄存器见 [`human-infra-c2-longtail-sixth-batch-source-extraction-register.json`](human-infra-c2-longtail-sixth-batch-source-extraction-register.json)，由 `make c2-longtail-sixth-batch-source-extraction-register-audit` 检查 24/24 个来源语境字段抽取是否完成，并确认 guideline route、publisher/manual review、source-lineage、降级触发和模型准入阻塞仍被显式保留。第六批本地来源语境复核见 [`human-infra-c2-longtail-sixth-batch-local-review-register.json`](human-infra-c2-longtail-sixth-batch-local-review-register.json)，由 `make c2-longtail-sixth-batch-local-review-audit` 检查 24/24 个抽取行是否完成本地结构复核，并确认 7 个 guideline route、publisher/manual review 或 source-lineage 问题行仍需 source-resolution/manual fulltext 后才能进入 bounded fresh review。该寄存器不完成 independent fresh review、reviewed artifacts 或模型准入。

## Claim Spine

本路线图对齐 `HI-CL1`、`HI-CL2`、`HI-CL3`、`HI-CL4`、`HI-CL6` 和 `HI-CL7`：主体持续性是价值成立条件，Human Infra 的对象是主体持续性的基础条件集合，定量模型必须区分寿命、健康寿命、有效时间和未来选择权，并把技术放入变量、状态、风险函数和证据链中审查。边界：不是医疗建议；不输出个体死亡日期；不证明具体技术已经实现有效永生。

## 总判断

截至 2026-07-03，项目已经完成了价值追问、域地图、主流 LEV 路线和 Web 叙事的主体搭建，但尚未达到完整研究工程系统。

| 轴线 | 当前成熟度 | 100% 状态 | 当前最大缺口 |
| --- | ---: | --- | --- |
| 项目价值 | 100% | 不同受众能用同一核心命题理解 Human Infra 的必要性 | 已有核心命题、多视角价值解析、页面级 Claim ID 一致性门禁、受众-主张映射和邻近项目边界对照；后续只需防止页面漂移 |
| 研究框架 | 99% | 每条主张都进入 Source Card、Claim-Evidence Matrix、变量表和反证条件 | 已有核心主张矩阵、页面级 Claim ID 门禁、arXiv-style 论文页强主张门禁、C1/20 个优先 C2 反证覆盖门禁、v0.1 反证 Source Card 锚点回填、当前 21 个来源锚点字段级 Source Card 抽取、26 个优先域的域级 Claim-Evidence Matrix seed、26 个优先域的 endpoint 候选和 source-specific 深读槽位、81 个 domain-source 深读任务队列、81/81 个 domain-source 精读完成行、81 项卡片晋升队列、20 个来源锚点本地来源语境复核账本、81 项卡片晋升预注册包、独立 fresh review 协议、FRB-01 到 FRB-04 合计 81/81 个 fresh-review verdict、486 个 reviewed card artifacts、4 条 future-boundary route cards、204 个 C2 域长尾覆盖账本、本地审计门禁、第一批 24 个高影响 C2 长尾域晋升队列、48 个 C2-LT-B1 逐源深读任务、48/48 个 C2-LT-B1 来源抽取试运行行、48/48 个 C2-LT-B1 本地来源语境复核门禁、C2-LT-B1 48 行独立 fresh-review 协议、48/48 个 C2-LT-B1 独立 fresh-review verdict、42 个 eligible C2-LT-B1 来源行晋升出的 252 个 reviewed artifacts、6 个非 eligible 行的 blocked source resolution 候选、6 个来源纠偏行的 source-resolution fresh review verdict、10 个 corrected source re-extraction 任务、10/10 个 corrected source re-extraction 输出、10/10 个 corrected source fresh review verdict、5 个 eligible corrected rows 晋升出的 30 个 corrected reviewed artifacts，以及第二批 12 个剩余 C2 长尾域的晋升队列、24 个 web-checked 候选来源、24/24 个本地抽取行、24/24 个本地来源语境复核行、2 批 independent fresh review 协议和 24/24 个 fresh-review verdict，其中 23 行可进入 bounded artifact fill、1 行 downgrade-before-fill，并已把 23 个 eligible rows 晋升为 138 个 bounded reviewed artifacts；第三批又选择 12 个神经-感知-认知连续性 C2 长尾域，绑定 24 个 web-checked 候选来源，派生 24 个深读任务，完成 24/24 个本地来源语境字段抽取、24/24 个本地来源语境复核、5 个问题行的 7 个 corrected/split/route-normalized source-resolution candidates、2 批 independent fresh-review 协议和 24/24 个 fresh-review verdict，其中 18 行可进入 bounded artifact fill、5 行只允许 corrected-source re-extraction、1 行 downgrade-before-fill，并已把 7 个 corrected/split/route-normalized 候选完成 bounded source re-extraction 和 7/7 corrected source fresh-review verdict，其中 6 行可进入 bounded artifact prep、1 行保持 duplicate/split route 阻塞；现在又把 18 个原始 eligible 行和 6 个 corrected eligible 行晋升为 144 个 bounded reviewed artifacts，并保留 EXT-022 downgrade-before-fill 与 C2LTB3-CREXT-004 duplicate/split route blocked row；第四批又选择 12 个代谢、内分泌、肾肝、电解质和携氧稳态连续性 C2 长尾域，绑定 24 个 web-checked 候选来源，派生 24 个 source-specific 深读任务，并完成 24/24 个本地来源语境字段抽取、24/24 个本地来源语境复核、4 个问题行的 source-resolution 候选准备、8 个候选的 manual/fulltext extraction、8/8 个 manual/fulltext fresh-review verdict，并把 3 个 eligible manual/fulltext fresh-review rows 晋升为 18 个 bounded reviewed artifacts，显式保留 5 个 duplicate/route-only/manual-access/context-only 阻塞行、3 个无摘要需全文复核行、1 个重复共识路线行和 8 个来源路线候选；第五批又选择 12 个细胞质量控制、细胞器通信、分子运输、膜脂韧性、清除和屏障底座 C2 长尾域，绑定 24 个 web/API-checked 候选来源，派生 24 个 source-specific 深读任务，完成 24/24 个本地来源语境字段抽取、24/24 个本地来源语境复核，并把 8 个无开放全文或跨域复用问题行整理为 14 个 PubMed、Europe PMC、DOI 或 PMC route 候选；剩余缺口是 C2 长尾域 B1/B2/B3/B4/B5 之外的批次覆盖、B5 manual/fulltext extraction/fresh review/reviewed artifacts 和校准模型准入 |
| 定量模型 | 80% | 有可运行、可复现、可审查的场景级模型管线 | 已有 toy model、合成敏感性分析、审计器、NCHS 2021 U.S. Life Tables 公开聚合死亡率锚点、校准预备契约、真实队列候选注册表、NHATS 数据准入草案、变量字典草案、extraction manifest 草案、acquisition-readiness gates、R13/R14 file-tier table、第一版 estimand protocol、变量确认矩阵、cohort-flow endpoint protocol、disclosure / survey-design / missingness / route-field / Colectica value-label protocol validator / Colectica value-label execution validator / Colectica access-route probe validator / Colectica authenticated capture template validator / L2 variable-family admission validator / pre-outcome aggregation validator、模型准入契约和模型准入候选注册表；但还没有 Colectica 登录、变量页实捕获、value labels 精确确认、question text / universe / skip logic 确认、真实提取、真实 NHATS route classification、真实 NHATS 输出披露审查、真实 survey-design 加权估计、外部验证、校准后的敏感性分析和任何 L4 calibrated admission |

## 价值层 100%

价值层的 100% 不是写更多宏大叙事，而是让项目在不同入口都指向同一个第一原理：

```text
一切目标、价值和创造都预设一个能够持续行动的主体
  -> 主体持续性不是普通目标之一，而是所有目标成立的边界条件
  -> Human Infra 的对象是维持、延展、增强主体持续性所需的生命、认知、时间、资源、工具、环境和协作系统
  -> 项目价值不是单点延寿，而是扩大主体未来仍能存在、行动、学习、修正和选择的可能性空间
```

验收条件：

- 有一个 100 字内总定义，能解释目标、对象和约束。
- 有至少三种价值视角：主体持续性、通用资源增量、反稀缺工程。
- 每种视角都能说明它改变的稀缺资源：寿命、健康寿命、有效时间、注意力、认知、恢复、资金、社会支持、环境和未来选择权。
- 能区分 Human Infra 与健康管理、长寿知识库、AI 工具箱、社会政策百科和医学建议系统。
- 能把价值语言连接到外部理论脊柱：能力方法、健康作为身体/心理/社会福祉、福祉测量、复杂干预和预测模型报告规范。

## 研究框架 100%

研究框架的 100% 是让每个研究域和每条主张都能被审查。

最低结构：

```text
研究问题
  -> 研究域对象
  -> 变量表
  -> 机制链路
  -> Source Cards
  -> Claim-Evidence Matrix
  -> 反证条件
  -> 模型位置
  -> 治理边界
```

验收条件：

- 研究域必须进入 C1-C6 物理分级目录，并在 README / AGENTS 中说明对象、非目标和上下游。
- 每个进入主论文或 Web 页的强主张必须绑定来源、证据等级、适用范围和禁止外推边界。
- 每个定量相关主张必须区分相关性、因果效应、预测能力、机制合理性和治理判断。
- 每条路线必须拆出概率门：技术窗口、可及性、采用概率、持续时间、组合性、尾部风险、机会成本。
- 模型必须区分 `screening model`、`toy model`、`calibrated predictive model` 和 `decision model`。
- 高风险领域必须写明中止条件，而不是只写“未来可能”。

## 定量模型 100%

定量模型的 100% 不是预测个人死亡日期，而是建立可复现的场景级生命路径模型。

目标形态：

```text
versioned inputs
  -> executable model
  -> generated scenario outputs
  -> Web visualization
  -> model card
  -> sanity checks
  -> governance boundary
```

最小可运行模型必须做到：

- 从版本化 JSON / TSV 输入读取场景，而不是把参数只写在前端脚本里。
- 命令行能生成 Web 数据文件。
- 输出群体/合成队列的风险函数、生存曲线、健康质量积分、有效时间和 LEV 阈值状态。
- 不输出个体死亡日期，不给个体医疗建议，不声明真实疗效。
- 包含模型卡：用途、非用途、输入来源、证据等级、主要假设、已知限制和升级条件。
- 包含 sanity checks：生存曲线单调、概率范围合法、无个人预测字段、场景 ID 唯一。
- 包含审计产物：机器可读 JSON 和人可读 Markdown，证明模型输出满足本地报告契约。
- 包含校准预备契约：target population、time zero、outcome、estimand、predictor、censoring、validation、calibration、sensitivity、bias/applicability 和 prohibited use 的最低字段。

## 外部方法锚点

这些锚点只提供方法约束，不直接证明 Human Infra 的任何具体主张。

| 来源 | Human Infra 使用位置 | 边界 |
| --- | --- | --- |
| Stanford Encyclopedia of Philosophy: Capability Approach | 把项目价值从资源占有转向真实能力、功能和选择空间 | 不把能力方法直接等同于永生伦理 |
| WHO Constitution | 把健康理解为身体、心理和社会福祉，而非仅无病 | 不把 WHO 定义当作具体干预证据 |
| MRC complex interventions framework | 复杂干预需要开发、评估、实施和语境分析 | 不替代具体临床试验 |
| TRIPOD+AI | 预测模型需要透明报告、开发/验证/更新边界 | 不表示当前 toy model 已达临床预测标准 |
| PROBAST / PROBAST+AI | 预测模型偏倚和适用性需要系统评估 | 不表示当前模型已具备低偏倚 |
| ISPOR Modeling Good Research Practices | 模型需要结构、参数、验证、报告和决策语境 | 不表示当前模型可用于真实资源分配 |
| DYNAMO-HIA / Future Elderly Model / OHDSI PLP | 可参考群体健康模拟、老龄化微观仿真和患者级预测工程 | 不直接复用为 Human Infra 校准模型 |

## 阶段路线

### Stage 1: 价值和边界冻结

完成条件：

- README、Web 首页、论文页和 reference 文档都使用同一套目标、对象、约束语言。
- 价值视角不再互相竞争，而是作为同一第一原理的不同投影。
- 每个传播性概念都有正式研究名和禁止误读说明。

### Stage 2: 研究域证据闭环

完成条件：

- C1 / C2 核心域优先完成 Source Cards 和 Claim-Evidence Matrix。
- 每个主流 LEV 路线都有路线卡、概率门、负向链路和证据边界。
- 所有强主张都能回到本地文档、来源链接和审查状态。

### Stage 3: Toy model 可运行

完成条件：

- 存在独立脚本可从版本化输入导出 Web 模型数据。
- Web 页面消费导出数据，而不是只用内嵌示意参数。
- CI / make check 能至少编译模型脚本。

### Stage 4: 校准模型预备

完成条件：

- 明确 target population、estimand、time zero、outcome、predictors、censoring 和 validation plan。
- 明确可用数据源、数据质量、缺失、代表性和伦理边界。
- 引入 TRIPOD+AI、PROBAST+AI、MRC 和 ISPOR 的最低报告字段。
- 机器审计必须证明当前仍然不能校准：没有真实队列、没有外部验证、没有个人用途许可。

### Stage 5: 严肃研究系统

完成条件：

- 模型、文档、Source Cards、Web 可视化和审计账本可一起复现。
- 能清楚说明某个技术或资源如何改变变量、状态、风险函数、生存曲线、有效时间和未来选择权。
- 能清楚说明当前不能算什么、为什么不能算、缺什么数据才能算。

## 当前下一步

当前已经完成最小 toy model 管线和校准预备契约：

```text
life_path_toy_model_scenarios.json
  -> run_life_path_toy_model.py
  -> life-path-toy-model.json
  -> run_life_path_sensitivity_analysis.py
  -> life-path-sensitivity-analysis.json
  -> audit_life_path_toy_model.py
  -> life-path-toy-model-audit.json / .md
  -> life_path_calibration_readiness.json
  -> human-infra-model-admission-contract.json
  -> human-infra-model-admission-candidate-registry.json
  -> life_path_data_source_candidates.json
  -> life-path-data-source-cards.md
  -> life-path-data-card-template.md
  -> life-path-data-card-nhats.md
  -> life-path-variable-dictionary-nhats.md
  -> life-path-extraction-manifest-nhats-draft.md
  -> life_path_nhats_acquisition_readiness.json
  -> life_path_nhats_file_tier_table.json
  -> life_path_nhats_first_estimand_protocol.json
  -> life_path_nhats_variable_confirmation_matrix.json
  -> life_path_nhats_cohort_flow_endpoint_protocol.json
  -> life_path_nhats_disclosure_control_policy.json
  -> life_path_nhats_disclosure_control_test_cases.json
  -> validate_nhats_disclosure_outputs.py
  -> life-path-nhats-disclosure-control-validation.json
  -> life_path_nhats_survey_design_protocol.json
  -> life_path_nhats_survey_design_test_cases.json
  -> validate_nhats_survey_design_plan.py
  -> life-path-nhats-survey-design-validation.json
  -> life_path_nhats_missingness_route_protocol.json
  -> life_path_nhats_missingness_route_test_cases.json
  -> validate_nhats_missingness_route_map.py
  -> life-path-nhats-missingness-route-validation.json
  -> life_path_nhats_route_field_discovery_register.json
  -> validate_nhats_route_field_discovery.py
  -> life-path-nhats-route-field-discovery-validation.json
  -> life_path_nhats_colectica_value_label_review_protocol.json
  -> validate_nhats_colectica_value_label_protocol.py
  -> life-path-nhats-colectica-value-label-validation.json
  -> life_path_nhats_colectica_value_label_review_execution_register.json
  -> validate_nhats_colectica_value_label_review_execution.py
  -> life-path-nhats-colectica-value-label-review-execution-validation.json
  -> life_path_nhats_colectica_access_route_probe_register.json
  -> validate_nhats_colectica_access_route_probe.py
  -> life-path-nhats-colectica-access-route-probe-validation.json
  -> life_path_nhats_colectica_authenticated_capture_template.json
  -> validate_nhats_colectica_authenticated_capture_template.py
  -> life-path-nhats-colectica-authenticated-capture-template-validation.json
  -> life_path_nhats_l2_variable_family_admission_register.json
  -> validate_nhats_l2_variable_family_admission.py
  -> life-path-nhats-l2-variable-family-admission-validation.json
  -> life_path_nhats_preoutcome_aggregation_protocol.json
  -> validate_nhats_preoutcome_aggregation_protocol.py
  -> life-path-nhats-preoutcome-aggregation-validation.json
  -> /model/ Web 图表
  -> model card + sanity checks + synthetic sensitivity checks + calibration-readiness audit checks + data-source candidate audit checks + source-card/data-card readiness checks + NHATS data-admission checks + pre-extraction manifest checks + machine-readable acquisition-readiness checks + file-tier table checks + first-estimand protocol checks + variable-confirmation matrix checks + cohort-flow endpoint-routing protocol checks + synthetic disclosure-control checks + synthetic survey-design checks + synthetic missingness-route checks + official route-field discovery checks + Colectica value-label review protocol checks + Colectica value-label review execution checks + Colectica access-route probe checks + Colectica authenticated capture template checks + NHATS L2 variable-family admission checks + NHATS pre-outcome aggregation checks
```

这一步已经把项目从“有定量想法的研究叙事”推进到“有最小可执行、可审计模型管线的研究系统”，并且开始把合成敏感性分析、真实队列候选、治理边界、第一份 NHATS 数据准入草案、NHATS 机器可读 acquisition-readiness gates、R13/R14 file-tier table、第一版 NHATS estimand protocol、NHATS variable confirmation matrix、NHATS cohort-flow endpoint-routing protocol、synthetic disclosure-control validator、synthetic survey-design validator、synthetic missingness-route validator、NHATS route-field discovery validator、NHATS Colectica value-label review protocol validator、NHATS Colectica value-label review execution validator、NHATS Colectica access-route probe validator、NHATS Colectica authenticated capture template validator、NHATS L2 variable-family admission validator、NHATS pre-outcome aggregation validator、模型准入契约、模型准入候选注册表和核心主张证据矩阵纳入机器审计。下一步不是继续膨胀新域，而是补四件硬东西：

- 继续用 `human-infra-core-claim-evidence-matrix.md` 作为核心主张入口，把 README、论文页和 Web 页的强叙事都回连到同一组 Claim ID、来源角色和禁止外推边界。
- C2 长尾深读已经形成五批推进线：B1 完成 48/48 fresh-review verdict、252 个原始 reviewed artifacts、10 个 corrected source re-extraction、10/10 corrected source fresh-review verdict 和 30 个 corrected reviewed artifacts；B2 完成 24/24 fresh-review verdict，并把 23 个 eligible rows 晋升为 138 个 bounded reviewed artifacts；B3 已完成 24/24 字段抽取、24/24 本地来源语境复核、24/24 independent fresh-review verdict、5 个问题行的 7 个 corrected/split/route-normalized 候选、7/7 corrected source re-extraction、7/7 corrected source fresh-review verdict，以及 144 个 bounded reviewed artifacts；EXT-022 downgrade-before-fill 与 C2LTB3-CREXT-004 duplicate/split route 均已显式保留为 blocked row；B4 已选定 12 个代谢、内分泌、肾肝、电解质和携氧稳态连续性域，绑定 24 个 web-checked 候选来源，派生 24 个 source-specific 深读任务，并完成 24/24 个本地来源语境字段抽取、24/24 个本地来源语境复核、4 个问题行的 source-resolution 候选准备、8 个候选的 manual/fulltext extraction、8/8 个 manual/fulltext fresh-review verdict，以及 3 个 eligible manual/fulltext fresh-review rows 对应的 18 个 bounded reviewed artifacts；5 个 duplicate/route-only/manual-access/context-only blockedRows 被显式保留。B5 已选定 12 个细胞质量控制、细胞器通信、分子运输、膜脂韧性、清除和屏障底座 C2 长尾域，绑定 24 个 web/API-checked 候选来源，派生 24 个 source-specific 深读任务，完成 24/24 个本地来源语境字段抽取、24/24 个本地来源语境复核，并把 8 个问题行整理为 14 个 source-resolution route candidates；下一步执行 B5 manual/fulltext extraction、independent fresh review 和 reviewed artifact prep，并在所有模型门禁完成前保持模型准入禁止。
- 把 NHATS manifest、route-field discovery register、Colectica value-label review protocol、Colectica value-label review execution register、Colectica access-route probe register、Colectica authenticated capture template、L2 variable-family admission register、pre-outcome aggregation protocol 和 first estimand protocol 从 draft / partial-executed / login-required / template-only / L2-only / protocol-only 推进到 governed acquisition-ready，补 Colectica 登录复核、variable page capture hash、value labels、question text、universe/skip logic、精确字段名、轮次、变量级缺失码、公开/敏感/受限状态、权重、endpoint 定义、cohort flow、survey design、代码本来源、真实聚合前置证据和输出抑制规则。
- 把 sensitivity analysis 从合成一因素扰动推进到基于真实队列、预注册范围和校准诊断的敏感性分析。

## 当前已具备的定量门禁

`npm run export:life-path-toy` 生成场景级模型输出。

`npm run audit:life-path-toy` 生成 `web/src/data/life-path-toy-model-audit.json` 和 `web/src/data/life-path-toy-model-audit.md`，当前检查包括：

- schema version 是否正确；
- source path 和 sha256 是否回到输入场景；
- model card 是否包含必需字段；
- prohibited use 是否明确禁止个体死亡日期和个体预测；
- evidence boundary 是否明确为 synthetic；
- scenario ID 是否唯一且包含 baseline；
- 每个场景是否包含必需 metrics；
- 生存曲线是否单调非增；
- survival / health-quality 是否处于 `[0, 1]`；
- resource budget 是否处于 `[0, 100]`；
- `LEV >= 1` 是否显示开放边界；
- 是否不存在个体死亡日期字段。
- 合成敏感性分析是否存在；
- 合成敏感性分析是否回到当前 toy model 的 source hash；
- 合成敏感性分析是否覆盖风险倍率、健康质量位移、能力倍率、主观时间、LEV 进度和尾部风险；
- 合成敏感性分析是否生成 48 个一因素扰动结果、场景稳定性摘要和禁止个体死亡日期字段检查；
- 校准预备契约是否存在；
- 是否明确当前没有真实队列、校准、外部验证和个体用途；
- 是否包含 TRIPOD+AI、PROBAST/PROBAST+AI、ISPOR、MRC 和 OHDSI PLP 方法锚点；
- 是否包含 target population、time zero、outcome、estimand、predictor、data requirement、censoring、validation、calibration、sensitivity、bias/applicability、reporting 和 prohibited use 字段。
- 候选数据源注册表是否存在；
- 候选数据源是否明确 no data download、no access grant、no individual data、no calibration claim 和 no causal claim；
- 候选数据源是否覆盖 mortality、function、biomarkers、cognition、resource/social 和 external validation 的最低需求；
- 每个候选源是否使用官方 HTTPS URL、写明 access/governance status，并禁止个体预测、校准过度主张和因果过度主张。
- 数据源 Source Cards 是否存在、覆盖每个候选源 ID 和官方 URL，并保留 candidate-only、未下载真实数据、未建立校准、禁止个体死亡日期预测和未外部验证边界；
- Data Card 模板是否存在，是否包含 Header、Governance、Study Design、Outcomes、Predictors、Data Quality、Model Use、Decision 和 Source Trace，并禁止个体死亡日期预测、个人医疗建议、个人寿命排名和未验证的校准声明。
- NHATS Data Card 是否存在，是否包含 source_card_id、draft/cannot-evaluate-yet 状态、官方来源追踪、禁止个体预测、禁止个人医疗建议、禁止 raw data 上传到公共 AI 系统、有效时间代理、不可评估决策和中止条件。
- NHATS 变量字典草案是否存在，是否保持 candidate-only 边界，并覆盖 design/identity、outcome boundary、function/mobility、cognition/attention、resources/support、environment/access 和 effective_time_proxy 这些模型角色。
- NHATS extraction manifest 草案是否存在，是否绑定 source card、Data Card 和变量字典，是否保持 cannot-extract-yet 状态，是否记录官方访问条款、Colectica/codebook 依赖、候选变量组、禁止 raw data 入库 / public LLM 上传、允许/禁止输出和中止条件。
- NHATS acquisition readiness 机器契约是否存在，是否保持 `cannot-extract-yet`，是否覆盖官方来源刷新、注册状态、文件层级、Colectica 变量确认、round window、survey design、endpoint、披露控制、AI 边界、存储销毁、禁止动作和下一步证据。
- NHATS file-tier table 是否存在，是否覆盖 R13/R14 annual public files、clock drawing images、sensitive SP/OP files 和 R13 seasonality weights，是否记录 access tier、官方路径、候选用途、方法文档依赖，并继续禁止下载、抽取、raw data 入库、public AI 上传、校准和个体预测。
- NHATS first estimand protocol 是否存在，是否预注册 R13/R14 cohort-level functional-survival 研究问题、target population、time zero、outcome、predictor family、censoring/missingness、survey design、readiness gates、aggregate-only 输出边界，并继续禁止下载、抽取、校准、验证和个体预测。
- NHATS variable confirmation matrix 是否存在，是否记录 Colectica/codebook 字段真相源、User Guide 变量命名/缺失码线索、Technical Paper 55 权重/方差线索、R13/R14 候选字段模式、变量组、cohort-flow 模板、readiness gates、禁止动作和官方来源追踪，并继续阻止从候选字段直接写抽取脚本。
- NHATS cohort-flow endpoint-routing protocol 是否存在，是否记录 R13/R14 队列流转行、R14 终点路由类、aggregate-only 输出契约、n < 5 披露控制、readiness gates、禁止动作和官方来源追踪，并继续阻止下载、抽取、公开导出、校准和个体预测。
- NHATS disclosure-control policy 是否存在，是否记录 aggregate-only、n < 5 suppression、row-level block、public AI block、允许输出类型、禁止输出类型和官方来源追踪，并继续阻止真实 public export、校准和个体预测。
- NHATS disclosure-control synthetic test cases 是否存在，是否覆盖 allow-export 与 block-export、small-cell unsuppressed、small-cell suppressed、row-level leak、public AI upload 和 forbidden output type。
- NHATS disclosure-control validation 是否存在，是否回到当前 policy/test-case hash，是否 `PASS`，是否 6 个合成用例全通过，并保留 synthetic-only、no-real-data、no-calibration 和 no-individual-prediction 边界。
- NHATS survey-design protocol / test cases / validation 是否存在，是否回到当前 protocol/test-case hash，是否 `PASS`，是否覆盖权重、分层、PSU/variance unit、方差方法、domain rule、route-map、round linkage 和 disclosure prerequisites，并继续保留 synthetic-only、no-real-data、no-calibration 和 no-individual-prediction 边界。
- NHATS missingness-route protocol / test cases / validation 是否存在，是否回到当前 protocol/test-case hash，是否 `PASS`，是否覆盖 alive self、alive proxy、alive facility/residential、death boundary、missing/nonresponse、not-classifiable、small-cell suppression、alive/death 冲突和禁止 missingness-as-outcome 边界。
- NHATS route-field discovery register / validation 是否存在，是否回到当前 register hash，是否 `PASS`，是否记录官方 R13/R14 crosswalk 字段候选、Colectica value-labels-pending 状态、sensitive death-date exclusion、阻塞门、source evidence 和禁止真实 route classification / weighted route counts / public AI / individual prediction 边界。
- NHATS Colectica value-label review protocol / validation 是否存在，是否回到当前 protocol hash，是否 `PASS`，是否记录 source evidence、review artifact requirements、route-field review units、blocking gates、sensitive death-date exclusion、no confirmed value-label map，并继续阻止 route classifier、endpoint classification、weighted route counts、public export、calibration 和 individual prediction。
- NHATS Colectica value-label review execution register / validation 是否存在，是否回到当前 execution register、protocol 和 route-field discovery hash，是否 `PASS`，是否只打开官方来源追踪、字段级 source-trace 骨架和 standard negative-code family 边界，并继续阻止 Colectica 登录、value labels、question text、skip logic、route-value map、classifier、weighted counts、public export、calibration 和 individual prediction。
- NHATS Colectica access-route probe register / validation 是否存在，是否回到当前 probe register 和 execution register hash，是否 `PASS`，是否只证明官方 Cross-Year Search 入口、匿名访问登录页边界、技术指南 workflow 和受控 capture sequence，并继续阻止账号、登录、变量页捕获、value labels、question text、exports、calibration 和 individual prediction。
- NHATS Colectica authenticated capture template / validation 是否存在，是否回到当前 template、probe register、execution register、protocol 和 route-field discovery hash，是否 `PASS`，是否只证明受控登录后变量页捕获槽、敏感死亡字段排除、source hash 要求和二次复核门已固定，并继续阻止账号状态、登录、变量页实捕获、value labels、question text、universe/skip logic、route classifier、公开导出、校准和 individual prediction。
- NHATS L2 variable-family admission register / validation 是否存在，是否回到当前 first estimand、变量确认矩阵、模型准入契约、候选注册表和 capture template hash，是否 `PASS`，是否只把 6 个候选变量族固定为 L2-only，并继续阻止精确字段确认、真实提取、route classification、校准、L4 admission 和 individual prediction。
- NHATS pre-outcome aggregation protocol / validation 是否存在，是否回到当前 L2 准入、变量确认、cohort-flow、survey-design 和 disclosure source hash，是否 `PASS`，是否只冻结 8 条 L2-only 聚合规则和 7 个 synthetic allow/block cases，并继续阻止真实聚合、weighted aggregation、L4 admission、calibration 和 individual prediction。

## 参考入口

- Stanford Encyclopedia of Philosophy, Capability Approach: https://plato.stanford.edu/entries/capability-approach/
- WHO Constitution: https://www.who.int/about/governance/constitution
- MRC framework for complex interventions: https://www.bmj.com/content/374/bmj.n2061
- TRIPOD statement: https://www.tripod-statement.org/
- PROBAST: https://www.probast.org/
- ISPOR Good Practices Reports: https://www.ispor.org/heor-resources/good-practices
- DYNAMO-HIA: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0033317
- Future Elderly Model: https://schaeffer.usc.edu/data/future-elderly-model/
- OHDSI Patient-Level Prediction: https://www.ohdsi.org/web/wiki/doku.php?id=projects:workgroups:patient-level_prediction
- WHO HALE metadata: https://www.who.int/data/gho/indicator-metadata-registry/imr-details/7752
