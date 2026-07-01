# 0037 Add Thirty Third Wave Future Technology Continuity Domains

## Status

Accepted

## Context

Human Infra 已经补齐生物基底、定量方法学、知识治理、技术扩散和科研证据基础设施。继续沿着先验追问往上追溯，会出现另一层必要条件：未来技术窗口能否被生成、保存、验证和安全运行。

有效永生不只依赖当前健康管理，也依赖未来医学、分子递送、基因表达调控、脑信息连续性、长期数字安全、档案可读性和安全关键软件可信度。如果这些条件缺失，主体即使获得更长等待时间，也可能无法把未来技术窗口转化为真实持续性收益。

## Decision

新增第三十三波 7 个正式研究域：

- `domains/c6-local-unlocking/nanomedicine-targeted-delivery-molecular-repair/`
- `domains/c3-generation-engine/ai-drug-discovery-protein-design/`
- `domains/c6-local-unlocking/epigenetic-editing-gene-regulation-therapeutics/`
- `domains/c1-boundary-rewriting/brain-preservation-connectomics-emulation/`
- `domains/c4-conversion-channel/post-quantum-cryptography-long-term-data-security/`
- `domains/c4-conversion-channel/safety-critical-software-formal-methods/`
- `domains/c5-ecological-substrate/long-term-digital-preservation-format-migration/`

同步更新根 README、AGENTS、`domains/` 索引、`docs/` 索引、域地图、研究域图谱、潜在域雷达、伦理边界、真实应用与文献索引，以及仓库结构检查脚本。

## Alternatives Considered

- Option A: 全部归入 `technology-foresight-horizon-scanning/`。拒绝，因为这些方向不是弱信号清单，而是具有独立变量、证据、失败模式和治理边界的技术基础层。
- Option B: 归入既有生物医学域。拒绝，因为纳米递送、AI 药物发现、表观编辑和脑信息保存分别改变递送、发现、调控和信息连续性机制，不能压进单一医学域。
- Option C: 归入数字身份或网络安全域。拒绝，因为后量子密码和长期数字保存分别处理算法寿命与档案可读性，独立于账号恢复和通用网络安全。

## Consequences

更容易：

- 把未来技术窗口拆成可追踪的技术生成、递送、调控、保存、验证和安全运行条件。
- 防止把“AI 发现药物”“纳米机器人”“表观编辑”“mind uploading”或“数字永生”写成未经审查的确定路径。
- 为 Future Waiting、有效永生飞轮和主体持续性模型增加更具体的远期技术变量。

更困难：

- 域数量继续增加，后续需要更强的图谱、标签和 Source Card 管理。
- 这些域远期性更强，必须持续标注证据阶段和禁止外推边界。

必须关注：

- 不提供可执行生物设计、人体实验、脑保存操作、攻击密码系统、绕过安全关键系统或规避档案权限的材料。
- 不把概念验证、动物实验、模型生成结果、保存材料或标准发布写成个体疗效、上传可行性或永久安全承诺。

## Safety And Evidence Boundary

本决策不证明任何纳米医学、AI 药物发现、表观编辑、脑保存、后量子密码、形式化方法或数字保存方案可以实现永生。新增域只说明：若 Human Infra 要研究主体持续性最大化，就必须审查未来技术如何被生成、递送、调控、保存、验证、保护和长期运行。
