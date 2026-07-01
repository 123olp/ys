# 0132 Add One-Hundred-Twenty-Seventh Wave Endocrine Feedback Axis Domains

Date: 2026-07-01

Status: Accepted

## Context

Human Infra 已有上位 `endocrine-hormonal-regulation/` 和 `thyroid-disease-endocrine-function-continuity/`，也已有第 126 波生殖内分泌、盆腔疼痛、不育与性功能域。

仍然缺少内分泌反馈系统的关键轴：皮质醇不足、皮质醇过量、垂体多轴调度、GH/IGF-1 过量、性腺功能低下和 POI。它们分别影响压力响应、危象风险、代谢骨骼负担、视觉/神经接口、心血管代谢、睡眠、肌肉、骨密度、生育窗口、情绪认知和未来选择权。

如果不拆成独立域，Human Infra 会把激素轴失衡写成泛化“内分泌问题”或“生殖问题”，无法识别不同来源、状态变量、监测边界、急性风险、商业夸大、隐私敏感性和禁止用途。

## Decision

新增第一百二十七波 6 个激素反馈轴连续性域：

- `domains/c2-source-maintenance/adrenal-insufficiency-cortisol-stress-response-continuity/`
- `domains/c2-source-maintenance/cushing-syndrome-hypercortisolism-metabolic-bone-continuity/`
- `domains/c2-source-maintenance/pituitary-disorders-hormone-axis-continuity/`
- `domains/c2-source-maintenance/acromegaly-growth-hormone-cardiometabolic-continuity/`
- `domains/c2-source-maintenance/hypogonadism-testosterone-sex-hormone-continuity/`
- `domains/c2-source-maintenance/primary-ovarian-insufficiency-hormone-fertility-continuity/`

这些域只整理公开资料、变量接口、机制链、监测边界、功能结果、隐私/污名风险、过度诊疗风险和禁止用途，不提供诊断、化验/影像/视野/报告解释、激素、用药、剂量、急救、手术、放疗、生育、性功能、健身、保险、法律或个体医疗建议。

## Consequences

- `endocrine-hormonal-regulation/` 保持激素轴上位机制域；新增域负责肾上腺、垂体、GH/IGF-1、性腺和 POI 等具体反馈轴失效模式。
- `thyroid-disease-endocrine-function-continuity/` 继续负责甲状腺轴；新增域补齐皮质醇轴、垂体调度、性腺轴和 GH/IGF-1 轴。
- 第 126 波生殖内分泌/盆腔/性功能域继续处理 PCOS、内异症、肌瘤、男性因素不育、ED 和外阴阴道疼痛；本波只处理更上游的激素反馈轴和病程负担。
- 项目边界更严格：任何个体激素检测解释、用药剂量、应激剂量、影像判读、青春期/生育/性功能判断、照片判断或急救替代都必须留在禁止区。
