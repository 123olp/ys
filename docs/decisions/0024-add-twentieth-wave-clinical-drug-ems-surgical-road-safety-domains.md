# 0024. Add Twentieth-Wave Clinical, Drug, EMS, Surgical And Road Safety Domains

Date: 2026-06-30

## Status

Accepted

## Context

Human Infra 已经覆盖医疗服务可及、药品可及、公共卫生实验室、医疗设备、感染控制、交通可达和患者安全。但继续做先验追问后，仍有一组“临床可靠性与急性风险窗口”没有独立归属：

- 个体医疗路径需要临床检验和诊断质量，不能只依赖公共卫生实验室。
- 药物进入真实世界后需要上市后安全监测和药物警戒。
- 药品可及还必须满足制造质量、供应完整性、假劣药防控和短缺治理。
- 急性事件需要 EMS 和院前照护在可逆窗口内接住主体。
- 手术和麻醉是高风险修复通道，需要独立围手术期安全治理。
- 交通系统不只提供可达性，也可能制造死亡、严重伤害和长期失能。

这些方向不能只放进 `healthcare-access-continuity/`、`medicine-access-treatment-continuity/`、`public-health-laboratory-diagnostic-capacity/`、`patient-safety-organizational-learning/`、`transportation-access-mobility/` 或 `risk-engineering/`，因为临床检验质量、药物警戒、药品质量、院前急救、围手术期安全和道路伤害预防各自有独立来源体系、失败模式和禁止用途边界。

## Decision

新增第二十波 6 个研究域骨架：

- `domains/clinical-laboratory-diagnostic-quality/`
- `domains/pharmacovigilance-drug-safety-monitoring/`
- `domains/pharmaceutical-quality-supply-integrity/`
- `domains/emergency-medical-services-prehospital-care/`
- `domains/surgical-anesthesia-perioperative-safety/`
- `domains/road-traffic-injury-prevention-safe-mobility/`

每个域只创建 `README.md` 与 `AGENTS.md`，作为长期研究容器和边界说明，不新增数据、脚本、模型或操作协议。

## Consequences

- Research Domain Atlas 和 Domain Map 能把“临床观测质量、真实世界药品安全、药品质量、急性院前响应、围手术期安全和道路伤害预防”纳入主体持续性成立条件。
- 伦理边界需要新增检验解读、用药、药品制造、急救操作、手术麻醉和道路安全的禁止用途。
- 仓库检查脚本需要把 6 个域和本 ADR 纳入 required files / dirs。

## Non-Goals

- 不提供检验解读、用药、停药、药品采购、药品制备、急救操作、手术麻醉操作、驾驶路线、事故责任或法律建议。
- 不提供样本操作、实验 SOP、监管规避、假药制造、设备/车辆改装、危险驾驶、急救现场处置或临床操作步骤。
- 不把这些高风险临床与安全域写成个人可执行方案。
