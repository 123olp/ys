# 0104 Add One Hundredth Wave Infectious Disease Outbreak Response Execution Domains

## Status

Accepted

## Context

Human Infra 已有 `immunization-public-health-surveillance/`、`public-health-laboratory-diagnostic-capacity/`、`sterilization-disinfection-infection-control/`、`air-quality-ventilation-exposure-control/`、`chronic-infectious-disease-care-continuity/` 和 `water-wastewater-utility-service-continuity/` 等公共卫生相关域。

这些域覆盖免疫与监测、诊断确认、感染控制、空气暴露、慢性感染照护和水务服务，但仍缺少一个关键执行层：当传染病暴发已经发生时，病例、接触者、学校、工作场所、医疗系统、物资储备和社区预警如何把公开信号转化为连续行动。

## Decision

新增第 100 波传染病暴发响应执行连续性域：

- `outbreak-case-investigation-contact-tracing-continuity/`
- `isolation-quarantine-work-school-continuity/`
- `community-testing-screening-access-continuity/`
- `vaccination-campaign-booster-delivery-continuity/`
- `mask-respirator-source-control-fit-access-continuity/`
- `indoor-ventilation-filtration-outbreak-control-continuity/`
- `school-workplace-outbreak-operations-continuity/`
- `healthcare-surge-triage-capacity-continuity/`
- `medical-countermeasure-stockpile-distribution-continuity/`
- `wastewater-pathogen-surveillance-early-warning-continuity/`

这些域不替代既有公共卫生总域，而是把暴发执行链拆成可审查接口：发现、通知、隔离、检测、免疫递送、呼吸防护、室内空气、组织运营、医疗容量、医疗对策和早期预警。

## Consequences

- `immunization-public-health-surveillance/` 继续作为群体监测和免疫屏障总域。
- 新域只处理暴发执行连续性，不输出个体诊断、治疗、隔离天数、返工返校许可、检测解释、疫苗建议、PPE 操作、HVAC 设计、医疗分诊或物资抢占内容。
- `docs/reference/ethics-and-safety-boundaries.md` 必须同步新增禁止用途边界，防止公共卫生资料被转化为监控、污名化、规避措施或现场指挥。
- `tools/check_repository.py` 必须把新域 README/AGENTS 和本 ADR 纳入结构检查。

## Source Signals

- CDC case investigation and contact tracing: https://www.cdc.gov/covid/php/contact-tracing/index.html
- CDC respiratory viruses guidance: https://www.cdc.gov/respiratory-viruses/guidance/
- CDC testing: https://www.cdc.gov/covid/testing/
- FDA COVID-19 tests: https://www.fda.gov/medical-devices/coronavirus-covid-19-and-medical-devices/covid-19-tests
- CDC masks and respirators: https://www.cdc.gov/respiratory-viruses/prevention/masks.html
- OSHA respiratory protection: https://www.osha.gov/respiratory-protection
- CDC ventilation in buildings: https://www.cdc.gov/covid/php/building-water-system/ventilation.html
- ASPR TRACIE: https://asprtracie.hhs.gov/
- ASPR Strategic National Stockpile: https://aspr.hhs.gov/SNS/
- CDC National Wastewater Surveillance System: https://www.cdc.gov/nwss/
