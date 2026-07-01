# 0098 Add Ninety-Fourth Wave Urinary and Renal Replacement Continuity Domains

## Status

Accepted.

## Context

Human Infra 已有 `urogenital-continuity/`、`renal-hepatic-clearance/`、`acute-kidney-injury-renal-replacement-continuity/`、`chronic-kidney-disease-screening-progression-continuity/` 和 `pelvic-floor-continence-function-continuity/`。这些域能覆盖泌尿生殖、清除系统、AKI、CKD 和盆底功能，但仍缺少更细的执行层：尿路感染、导尿设备、尿潴留、夜尿、结石、BPH、尿流改道、透析通路、家庭透析和肾移植。

这些对象不是同一个问题。它们分别对应感染入口、设备化排尿出口、机械排空失败、睡眠有效时间损耗、尿路梗阻、男性下尿路症状、外部化排泄出口、肾脏替代治疗接口、家庭生命支持供应链和移植后长期免疫治理。

## Decision

新增第九十四波 10 个研究域：

- `domains/c2-source-maintenance/urinary-tract-infection-pyelonephritis-urosepsis-continuity/`
- `domains/c2-source-maintenance/catheter-associated-uti-device-infection-continuity/`
- `domains/c6-local-unlocking/urinary-retention-bladder-emptying-continuity/`
- `domains/c6-local-unlocking/overactive-bladder-nocturia-sleep-continuity/`
- `domains/c2-source-maintenance/kidney-stone-obstruction-renal-colic-continuity/`
- `domains/c6-local-unlocking/benign-prostatic-hyperplasia-luts-continuity/`
- `domains/c6-local-unlocking/urinary-diversion-urostomy-supplies-continuity/`
- `domains/c2-source-maintenance/dialysis-access-vascular-peritoneal-continuity/`
- `domains/c2-source-maintenance/home-dialysis-supply-self-management-continuity/`
- `domains/c2-source-maintenance/kidney-transplant-immunosuppression-graft-continuity/`

## Consequences

- `urogenital-continuity/` 继续作为泌尿生殖总框架，不承载所有尿路感染、排空、夜尿、结石、BPH 和尿流改道细节。
- `renal-hepatic-clearance/` 继续作为清除系统总框架；透析通路、家庭透析和肾移植作为清除能力外部化或重建后的独立执行域。
- 所有新域必须保持公共知识、证据边界和模型索引定位，不提供个人尿检解释、用药、导尿、透析参数、造口护理、移植用药、急诊分诊或个体医疗建议。

## Source Signals

- NIDDK urinary tract infection, urinary retention, kidney stones, prostate enlargement, hemodialysis, peritoneal dialysis, kidney transplant and urinary diversion resources.
- CDC catheter-associated urinary tract infection resources.
- National Kidney Foundation dialysis access, home dialysis, kidney transplant and kidney stone resources.
- MedlinePlus public patient education materials for UTI, urinary retention, kidney stones, BPH and urostomy.
