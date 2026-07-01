# ADR 0092: Add Eighty-Eighth-Wave Oral Dental Jaw-Function Continuity Domains

## Status

Accepted

## Date

2026-07-01

## Context

Human Infra 已经有 `oral-health-continuity/` 作为总口腔健康域，但龋病、牙周病、缺牙修复、牙痛急性感染、口腔癌、儿童口腔、老年口腔、牙科服务可及性、口干唾液功能和颞下颌/口颌面痛具有不同机制、服务入口、证据体系、功能后果和禁止用途边界。如果继续只放在泛口腔健康域中，后续证据卡、模型变量、可视化和伦理边界都会混成一个概念桶。

官方资料来源包括 WHO Oral Health、CDC Oral Health、NIDCR 的 Tooth Decay、Gum Disease、Oral Cancer、Dry Mouth、TMD、Older Adults and Oral Health，以及 HRSA Oral Health 等公开资料。

## Decision

新增第八十八波 10 个正式研究域：

- `domains/c2-source-maintenance/dental-caries-prevention-restoration-continuity/`
- `domains/c6-local-unlocking/periodontal-disease-systemic-inflammation-continuity/`
- `domains/c6-local-unlocking/tooth-loss-prosthodontic-chewing-continuity/`
- `domains/c2-source-maintenance/dental-pain-emergency-infection-continuity/`
- `domains/c2-source-maintenance/oral-cancer-mucosal-lesion-early-detection-continuity/`
- `domains/c2-source-maintenance/pediatric-oral-health-development-continuity/`
- `domains/c2-source-maintenance/geriatric-long-term-care-oral-health-continuity/`
- `domains/c2-source-maintenance/dental-care-access-insurance-workforce-continuity/`
- `domains/c2-source-maintenance/xerostomia-salivary-function-oral-medication-continuity/`
- `domains/c2-source-maintenance/temporomandibular-orofacial-pain-jaw-function-continuity/`

每个域只创建 `README.md` 和 `AGENTS.md`。本轮不创建牙科诊断工具、影像判读、治疗推荐器、保险资格判断、产品推荐、用药建议、急救流程或个体护理系统。

## Consequences

- 口腔健康从总域扩展为牙体、牙周、修复、急性事件、癌症、生命历程、服务制度、唾液和颌面痛这些可独立审查的持续性条件。
- 后续证据卡可以分别追踪疼痛、感染、咀嚼、营养、沟通、费用、服务入口、儿童发育、老年照护和癌症功能后果。
- 所有相关资料必须保留来源、适用对象、不确定性和禁止用途。
- 仓库结构检查必须把 10 个新目录、20 个新域文件和本 ADR 纳入 required set。
