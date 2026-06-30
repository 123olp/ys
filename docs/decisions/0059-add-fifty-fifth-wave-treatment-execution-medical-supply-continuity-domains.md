# 0059 Add Fifty-Fifth-Wave Treatment Execution Medical Supply Continuity Domains

## Status

Accepted

## Context

Human Infra 已有 `medicine-access-treatment-continuity`、`pharmaceutical-quality-supply-integrity`、`pharmacovigilance-drug-safety-monitoring`、`medical-device-equipment-safety-maintenance`、`multimorbidity-polypharmacy-care-coordination` 和 `care-transitions-discharge-continuity` 等上位域。

这些域能解释药物、设备、治疗和安全监测为什么重要，但仍缺少一个执行层：处方、福利、标签、药房、DME、氧疗、糖尿病耗材和居家设备如何真实进入主体日常生活。

若这个执行层失败，临床计划、药物存在、设备存在和保险名义覆盖都不能自动转化为主体持续性收益。

## Decision

新增第 55 波 8 个治疗获得与医用品执行连续性域：

- `retail-pharmacy-prescription-dispensing-continuity`
- `pharmacy-benefit-formulary-prior-authorization-continuity`
- `medication-reconciliation-regimen-adherence-continuity`
- `patient-medication-labeling-counseling-continuity`
- `unused-medicine-takeback-disposal-continuity`
- `durable-medical-equipment-supplier-repair-continuity`
- `home-oxygen-respiratory-equipment-supply-continuity`
- `diabetes-insulin-glucose-monitoring-supplies-continuity`

每个域只建立最小 `README.md` 和 `AGENTS.md`，同步更新根目录、docs、domain map、atlas、radar、applications、ethics 和 repository check，不新增数据目录、采集脚本或 Web 产品入口。

## Consequences

- Human Infra 能从“医学方案存在”继续追问到“治疗物质、设备、耗材、信息和支付路径是否进入主体日常执行”。
- 药品、DME、氧疗、糖尿病耗材和用药理解的证据边界被拆开，避免把它们混入单一药品可及性或医疗设备安全桶。
- 新域必须严格禁止个体医疗建议、处方处理、保险申诉代写、设备维修教程、药物处置操作和敏感健康/保险资料采集。

## Validation

- `python3 tools/check_repository.py`
- `git diff --check`
- `make check`
