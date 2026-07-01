# 0119. Add One-Hundred-Fourteenth Wave Early Child Care Execution Domains

Date: 2026-07-01

## Status

Accepted

## Context

`childcare-family-continuity/` 已经把托育、早期儿童发展、父母工作连续性和家庭压力纳入 Human Infra 的主体持续性框架。但随着域地图继续下钻，原域仍然过宽：托育供给与费用、许可安全、补贴支付、Head Start、IDEA Part C 早期干预、课外/暑期学习照护各自有独立制度入口、证据来源、敏感数据、失败模式和禁止用途。

如果继续只保留一个上位托育域，后续研究会把市场供给、监管安全、补贴支付、早期综合服务、发育干预和学校日历外照护混在一起，难以判断每个机制具体改变哪些变量，也难以给出足够清晰的伦理边界。

## Decision

新增第 114 波 6 个早期儿童照护执行连续性研究域：

- `child-care-availability-affordability-continuity/`
- `child-care-licensing-health-safety-continuity/`
- `child-care-subsidy-ccdf-payment-continuity/`
- `head-start-early-head-start-family-support-continuity/`
- `early-intervention-idea-part-c-developmental-services-continuity/`
- `out-of-school-time-afterschool-summer-learning-continuity/`

这些域共同把“儿童需要照护和发展支持”拆成可审查执行链：服务名额与费用、许可与健康安全、补贴与支付、综合早期服务、早期干预和学校日历外照护。

## Consequences

- `childcare-family-continuity/` 保持上位家庭连续性域，不再承载全部执行细节。
- 早期儿童服务被建模为家庭有效时间、儿童发展、父母就业、收入稳定、学习轮次和未来选择权的共同基础设施。
- 资料使用必须回到 ACF OCC、CCDF、ChildCare.gov、Head Start、IDEA Part C、21st CCLC、CDC Child Development、Census child care 和 NSECE 等公开来源。
- 禁止把这些域转化为个体托育机构选择、补贴申请、儿童诊断、治疗计划、学校安置、法律、家庭纠纷或儿童安全处置建议。

## Verification

- 每个新增域必须包含 `README.md` 和 `AGENTS.md`。
- 根 `README.md`、根 `AGENTS.md`、`domains/README.md`、`domains/AGENTS.md`、`docs/reference/domain-map.md`、`docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md`、`docs/reference/applications-and-literature.md` 和 `docs/reference/ethics-and-safety-boundaries.md` 必须同步索引。
- `tools/check_repository.py` 必须登记新增目录、README/AGENTS 和本 ADR。
