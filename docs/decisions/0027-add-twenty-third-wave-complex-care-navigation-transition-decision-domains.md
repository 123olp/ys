# 0027. Add Twenty-Third-Wave Complex Care Navigation, Transition And Decision Domains

Date: 2026-06-30

## Status

Accepted.

## Context

Human Infra 已经覆盖医疗可及、药品治疗连续性、患者数据互操作、患者安全、长期照护、健康素养、语言可达和结构性脆弱场景。但仍缺少一组高复杂度照护路径：罕见病诊断漫游、多病共存与多重用药、出院与照护转移、居家医疗/缓和医疗/安宁疗护、医疗解释与文化中介、患者倡导与共同决策。

这些不是单纯的“医疗服务”子项。它们各自有独立失败模式：诊断找不到、专科与药物冲突、出院后责任断线、严重疾病阶段目标与照护不连续、临床沟通不被理解、主体偏好无法进入决策。若不拆出，Human Infra 会低估复杂医疗场景中主体持续性失败的真实原因。

## Decision

Add six formal domains:

- `domains/c6-local-unlocking/rare-disease-diagnostic-odyssey-care-coordination/`
- `domains/c6-local-unlocking/multimorbidity-polypharmacy-care-coordination/`
- `domains/c5-ecological-substrate/care-transitions-discharge-continuity/`
- `domains/c5-ecological-substrate/home-health-hospice-palliative-care-continuity/`
- `domains/c6-local-unlocking/medical-interpreter-cultural-mediation/`
- `domains/c4-conversion-channel/patient-advocacy-shared-decision-making/`

Update root navigation, docs navigation, reference maps, radar, ethics boundaries, changelog and repository checks so the new domains are discoverable and validated.

## Consequences

- Complex care navigation becomes a first-class Human Infra layer instead of being hidden inside broad healthcare access.
- Safety boundaries must explicitly prohibit individual diagnosis, treatment, medication, discharge, hospice eligibility, legal, insurance and real-time interpreting advice.
- Future evidence work can organize source cards around diagnostic odyssey, multimorbidity, transitions, serious illness care, clinical language access and shared decision-making.

## Non-Goals

- No individual medical diagnosis, treatment, medication, deprescribing, urgent-care, discharge, home-health, hospice, palliative, interpreter, legal, insurance or complaint advice.
- No ranking, endorsement or routing recommendation for clinicians, hospitals, labs, patient organizations, trials, insurers or agencies.
- No live medical interpreting or clinical text translation that could be mistaken for authoritative care.
- No manipulation of patients, families, clinicians or institutions under the label of advocacy.
