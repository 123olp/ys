# 0060 Add Fifty-Sixth-Wave Outpatient Access Clinical Service Execution Domains

## Status

Accepted

## Context

Human Infra 已有 `healthcare-access-continuity`、`medicine-access-treatment-continuity`、`clinical-laboratory-diagnostic-quality`、`care-transitions-discharge-continuity`、`home-health-hospice-palliative-care-continuity`、`patient-data-interoperability` 和第五十五波治疗执行域。

这些域能解释医疗可及、治疗物质、检验质量、出院转移和居家照护为什么重要，但仍缺少一个门诊执行层：主体如何找到网络内 provider、进入初级照护、完成专科转诊、排上预约、完成门诊检验/影像/操作，并在非急诊时段获得合适分诊。

若这个执行层失败，保险覆盖、临床能力、检查项目和治疗方案都不能自动转化为主体持续性收益。

## Decision

新增第 56 波 8 个门诊访问与临床服务执行连续性域：

- `provider-directory-network-adequacy-continuity`
- `primary-care-panel-appointment-access-continuity`
- `specialist-referral-authorization-navigation-continuity`
- `appointment-availability-wait-time-continuity`
- `outpatient-laboratory-specimen-result-routing-continuity`
- `diagnostic-imaging-order-scheduling-report-continuity`
- `ambulatory-procedure-surgery-center-continuity`
- `after-hours-urgent-care-triage-continuity`

每个域只建立最小 `README.md` 和 `AGENTS.md`，同步更新根目录、docs、domain map、atlas、radar、applications、ethics 和 repository check，不新增数据目录、采集脚本或 Web 产品入口。

## Consequences

- Human Infra 能从“有医疗系统/保险/检查能力”继续追问到“主体是否能实际预约、转诊、完成服务、拿到结果和进入下一步”。
- Provider directory、network adequacy、primary care panel、specialist referral、wait time、lab specimen routing、imaging scheduling、ambulatory procedure 和 urgent care triage 被拆成独立执行接口。
- 新域必须严格禁止个体医疗建议、转诊策略、排队规避、抢号脚本、检查选择、影像/检验解读、手术准备、急救替代和敏感健康/保险资料采集。

## Validation

- `python3 tools/check_repository.py`
- `git diff --check`
- `make check`
