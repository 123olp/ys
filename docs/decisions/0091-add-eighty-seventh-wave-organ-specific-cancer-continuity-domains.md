# ADR 0091: Add Eighty-Seventh-Wave Organ-Specific Cancer Continuity Domains

## Status

Accepted

## Date

2026-07-01

## Context

Human Infra 已经有 `cancer-control/` 和 `cancer-screening-early-detection-continuity/`，但器官/阶段特异癌症仍容易被压扁成一个“癌症筛查”或“癌症治疗”概念桶。乳腺癌、结直肠癌、肺癌、前列腺癌、宫颈癌、卵巢癌、胰腺癌、肝癌、儿童癌症和癌症幸存者晚期效应各自有独立筛查路径、症状/异常闭环、治疗负担、复发模式、长期功能结果、污名风险和禁止用途边界。

官方资料来源包括 NCI 对 breast、colorectal、lung、prostate、cervical、ovarian、pancreatic、liver、childhood cancers 和 survivorship 的资料，以及 CDC 对相关癌症与幸存者的公开资料。

## Decision

新增第八十七波 10 个正式研究域：

- `domains/c2-source-maintenance/breast-cancer-screening-treatment-survivorship-continuity/`
- `domains/c2-source-maintenance/colorectal-cancer-screening-treatment-continuity/`
- `domains/c2-source-maintenance/lung-cancer-screening-treatment-continuity/`
- `domains/c2-source-maintenance/prostate-cancer-screening-treatment-continuity/`
- `domains/c2-source-maintenance/cervical-cancer-hpv-prevention-screening-continuity/`
- `domains/c2-source-maintenance/ovarian-cancer-symptom-detection-treatment-continuity/`
- `domains/c2-source-maintenance/pancreatic-cancer-high-risk-detection-treatment-continuity/`
- `domains/c2-source-maintenance/liver-cancer-cirrhosis-surveillance-treatment-continuity/`
- `domains/c2-source-maintenance/childhood-cancer-treatment-survivorship-continuity/`
- `domains/c2-source-maintenance/cancer-survivorship-late-effects-continuity/`

每个域只创建 `README.md` 和 `AGENTS.md`。本轮不创建数据采集脚本、筛查推荐器、诊断工具、治疗方案、个体风险评分或医疗决策系统。

## Consequences

- 癌症连续性从通用筛查/控制扩展到器官和生命阶段特异模型。
- 高负担癌种的筛查、异常追踪、治疗毒性、复发监测、晚期效应、家庭/工作/保险和幸存者生活质量获得独立索引。
- 所有相关资料必须保留来源、适用对象、不确定性和禁止用途。
- 仓库结构检查必须把 10 个新目录、20 个新域文件和本 ADR 纳入 required set。
