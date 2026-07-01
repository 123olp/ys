# 0088 Add Eighty-Fourth Wave Life Course Preventive Continuity Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra 已经拆出急性救援、急性内科时间窗、预防筛查与风险因子控制域，但主体持续性最大化还需要补齐一组横跨恢复、生殖、性健康、中年转轨、慢性感染和环境暴露的生活史预防执行域。

睡眠呼吸障碍、慢性失眠、STI/HIV、病毒性肝炎、避孕与家庭计划、月经健康、围绝经期、盆底功能和皮肤 UV/皮肤癌风险并不总是直接表现为立即死亡风险，却会持续改变有效时间、恢复能力、身体自主、关系安全、感染传播、肝脏储备、工作参与、尊严、行动半径和未来选择权。如果这些对象只停留在更宽泛的 `sleep-circadian-recovery/`、`reproductive-fertility-continuity/`、`chronic-infectious-disease-care-continuity/`、`urogenital-continuity/`、`cancer-control/` 或 `planetary-health-environment/` 中，模型会丢失关键执行断点。

## Decision

新增第八十四波生活史预防与功能连续性研究域：

- `sleep-disordered-breathing-screening-treatment-continuity/`
- `chronic-insomnia-cbti-access-continuity/`
- `sexual-health-sti-prevention-continuity/`
- `hiv-testing-prep-prevention-continuity/`
- `chronic-viral-hepatitis-screening-liver-protection-continuity/`
- `contraception-family-planning-access-continuity/`
- `menstrual-health-cycle-literacy-continuity/`
- `perimenopause-menopause-midlife-health-continuity/`
- `pelvic-floor-continence-function-continuity/`
- `skin-cancer-uv-protection-early-detection-continuity/`

每个域只建立 `README.md` 和 `AGENTS.md`，用于定义先验位置、关注对象、Human Infra 模型链路、非目标和 Source Signals。暂不创建个体筛查器、诊断工具、用药建议、性健康建议、避孕选择器、周期预测器、睡眠治疗计划、皮肤照片判读、设备配置、风险评分、数据采集或自动化脚本。

## Consequences

- 第八十四波把生活史阶段中的恢复、性/生殖、中年健康、控尿控便、慢性感染和 UV/皮肤癌预防执行层独立出来。
- `docs/reference/domain-map.md`、`research-domain-atlas.md`、`research-domain-radar.md`、`applications-and-literature.md` 和 `ethics-and-safety-boundaries.md` 必须同步新增索引与边界。
- `tools/check_repository.py` 必须把新增域和 ADR 纳入结构门禁。
- 公开表达必须持续强调：这些域是研究、建模和证据边界，不是个人诊断、治疗、性健康、避孕、睡眠、皮肤、肝炎、HIV、盆底康复、用药、检查频率、保险或法律建议。

## Source Signals

- NHLBI sleep apnea signals: https://www.nhlbi.nih.gov/health/sleep-apnea
- USPSTF obstructive sleep apnea screening signals: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/obstructive-sleep-apnea-in-adults-screening
- ACP insomnia and AASM behavioral sleep treatment signals: https://www.acpjournals.org/doi/10.7326/M15-2175 and https://jcsm.aasm.org/doi/10.5664/jcsm.8986
- CDC STI prevention and treatment guideline signals: https://www.cdc.gov/std/treatment-guidelines/default.htm and https://www.cdc.gov/sti/prevention/
- CDC HIV testing / PrEP and USPSTF HIV / PrEP signals: https://www.cdc.gov/hiv/testing/ and https://www.cdc.gov/hivnexus/hcp/prep/
- CDC viral hepatitis and USPSTF hepatitis C screening signals: https://www.cdc.gov/hepatitis/php/testing/index.html and https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/hepatitis-c-screening
- CDC U.S. MEC / U.S. SPR contraception signals: https://www.cdc.gov/contraception/hcp/usmec/ and https://www.cdc.gov/contraception/hcp/usspr/
- NICHD / HHS menstrual health signals: https://www.nichd.nih.gov/health/topics/menstruation and https://www.womenshealth.gov/menstrual-cycle
- NIA / HHS menopause signals: https://www.nia.nih.gov/health/menopause/what-menopause and https://www.womenshealth.gov/menopause
- NIDDK urinary and fecal incontinence signals: https://www.niddk.nih.gov/health-information/urologic-diseases/bladder-control-problems and https://www.niddk.nih.gov/health-information/digestive-diseases/fecal-incontinence
- CDC / USPSTF / NCI skin cancer and UV prevention signals: https://www.cdc.gov/skin-cancer/prevention/ and https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/skin-cancer-counseling
