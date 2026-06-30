# 0087 Add Eighty-Third Wave Preventive Risk Factor Control Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra 已经拆出急性救援、急性内科时间窗、心血管韧性、营养代谢、物质暴露、肌骨完整性和癌症控制等上位域，但主体持续性最大化还需要更上游的“无症状风险因子与筛查控制”层。

高血压、血脂/动脉粥样硬化、糖尿病前期、肥胖/脂肪分布、烟草/尼古丁、酒精风险、慢性肾病、癌症筛查、骨质疏松和跌倒风险都常在长期无症状阶段改变未来死亡、失能、急症进入、有效时间和资源消耗。如果它们只停留在宽泛的 `cardiovascular-resilience/`、`nutrition-metabolic-health/`、`substance-exposure-control/`、`musculoskeletal-integrity/` 或 `cancer-control/` 中，模型会丢失“风险如何被筛查、确认、转介、坚持、随访和复发预防”的执行层。

## Decision

新增第八十三波预防筛查与风险因子控制研究域：

- `hypertension-detection-control-continuity/`
- `lipid-atherosclerosis-risk-management-continuity/`
- `prediabetes-diabetes-prevention-continuity/`
- `obesity-adiposity-metabolic-risk-continuity/`
- `tobacco-nicotine-cessation-continuity/`
- `alcohol-use-risk-reduction-continuity/`
- `chronic-kidney-disease-screening-progression-continuity/`
- `cancer-screening-early-detection-continuity/`
- `osteoporosis-fracture-prevention-bone-health-continuity/`
- `fall-risk-prevention-home-safety-continuity/`

每个域只建立 `README.md` 和 `AGENTS.md`，用于定义先验位置、关注对象、Human Infra 模型链路、非目标和 Source Signals。暂不创建个体风险评分、筛查推荐器、行为处方、戒断方案、营养方案、用药建议、数据采集或自动化脚本。

## Consequences

- 第八十三波把急症上游的慢性风险识别与风险因子执行层独立出来。
- `docs/reference/domain-map.md`、`research-domain-atlas.md`、`research-domain-radar.md`、`applications-and-literature.md` 和 `ethics-and-safety-boundaries.md` 必须同步新增索引与边界。
- `tools/check_repository.py` 必须把新增域和 ADR 纳入结构门禁。
- 公开表达必须持续强调：这些域是研究、建模和证据边界，不是个人筛查、诊断、用药、戒断、减重、饮食、运动、检查排序、保险或医疗建议。

## Source Signals

- USPSTF hypertension screening signals: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/hypertension-in-adults-screening
- USPSTF statin primary prevention signals: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/statin-use-in-adults-preventive-medication
- USPSTF prediabetes/type 2 diabetes screening signals: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/screening-for-prediabetes-and-type-2-diabetes
- CDC National Diabetes Prevention Program signals: https://www.cdc.gov/diabetes/prevention/
- CDC obesity and USPSTF behavioral weight interventions signals: https://www.cdc.gov/obesity/ and https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/obesity-in-adults-interventions
- CDC tobacco cessation and USPSTF tobacco cessation signals: https://www.cdc.gov/tobacco/ and https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/tobacco-use-in-adults-and-pregnant-women-counseling-and-interventions
- NIAAA and USPSTF unhealthy alcohol use signals: https://www.niaaa.nih.gov/ and https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/unhealthy-alcohol-use-in-adolescents-and-adults-screening-and-behavioral-counseling-interventions
- KDIGO CKD evaluation and management signals: https://kdigo.org/guidelines/ckd-evaluation-and-management/
- USPSTF cancer screening signals: https://www.uspreventiveservicestaskforce.org/
- USPSTF osteoporosis screening and CDC STEADI signals: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/osteoporosis-screening and https://www.cdc.gov/steadi/
