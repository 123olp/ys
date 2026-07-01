# 0129 Add One-Hundred-Twenty-Fourth Wave Reproductive Technology Governance Domains

Date: 2026-07-01

Status: Accepted

## Context

Human Infra 已有 `reproductive-fertility-continuity/`、围产期连续性和儿科早期筛查域，但辅助生殖技术的执行链仍被压在上位“生殖与生育连续性”中。ART/IVF 周期、诊所成功率报告、生育保存冷冻储存、供体筛查追溯、PGT 胚胎选择治理和第三方生殖法律伦理分别有独立资料源、失败模式、时间窗口、权利边界和禁止用途。

如果不拆出独立域，IVF 周期会被误写成普通生殖健康，ART 成功率会被误读成个人预后，生育保存会被混入一般冷链或遗产继承，供体筛查会被混入普通生物样本，PGT 会被误写成基因编辑或优生工具，代孕/供体/跨境生殖也会被混入普通家庭法或医疗可及。

## Decision

新增第一百二十四波 6 个生殖技术与生育保存治理连续性域：

- `domains/assisted-reproductive-technology-ivf-cycle-continuity/`
- `domains/art-clinic-success-rate-quality-reporting-continuity/`
- `domains/fertility-preservation-gamete-embryo-cryostorage-continuity/`
- `domains/reproductive-tissue-donor-screening-traceability-continuity/`
- `domains/preimplantation-genetic-testing-embryo-selection-governance-continuity/`
- `domains/third-party-reproduction-surrogacy-donor-legal-ethics-continuity/`

这些域只整理公开资料、变量、流程边界、证据等级、风险门槛和伦理/治理接口，不提供个体不孕、生殖医疗、IVF、PGT、供体、代孕、胚胎处置、法律、保险、诊所选择或跨境服务建议。

## Consequences

- Human Infra 可以把“生殖未来选择权”拆到 ART 周期、观测数据、材料保存、供体追溯、遗传检测选择和多主体法律伦理这些可审查执行层。
- 这批域把山中因子、细胞重编程、再生医学和生殖技术之间的未来路径接口收敛为资料治理问题，而不是把远期技术承诺写成现实可用方案。
- 项目边界更严格：任何个体治疗、成功率解释、胚胎选择、供体识别、代孕安排、跨境规避或商业推荐都必须留在禁止区。
