# 0023. Add Nineteenth-Wave Air, Food, Occupational, Device, Sterilization And Accessibility Domains

Date: 2026-06-30

## Status

Accepted

## Context

Human Infra 已经覆盖公共卫生实验室、血液器官组织、废弃物、辐射、化学品和关键材料等外部安全与材料条件。继续按先验追问推进后，仍有一组“日常环境与工具可靠性”条件没有独立归属：

- 主体需要可呼吸、可恢复、可学习和可工作的空气环境。
- 食物需要不只可得，还要不成为病原、毒素、过敏原或污染入口。
- 工作需要不以长期暴露和未来身体损耗作为收入代价。
- 现代医学依赖可安全使用、可维护、可追踪和可召回的医疗设备。
- 医疗与照护环境需要通过清洁、消毒、灭菌和再处理防止感染扩散。
- 建成环境需要让不同身体、感官和认知状态的人持续进入、移动、使用和参与。

这些方向不能只放进 `planetary-health-environment/`、`food-security-nutrition-access/`、`occupational-work-design/`、`medicine-access-treatment-continuity/`、`antimicrobial-resilience/` 或 `assistive-technology-access/`，因为空气治理、食品污染控制、工业卫生、医疗设备生命周期、感染控制和物理空间可达性各自有独立来源体系、失败模式和禁止用途边界。

## Decision

新增第十九波 6 个研究域骨架：

- `domains/c3-generation-engine/air-quality-ventilation-exposure-control/`
- `domains/c5-ecological-substrate/food-safety-contamination-control/`
- `domains/c6-local-unlocking/occupational-exposure-industrial-hygiene/`
- `domains/c6-local-unlocking/medical-device-equipment-safety-maintenance/`
- `domains/c2-source-maintenance/sterilization-disinfection-infection-control/`
- `domains/c5-ecological-substrate/built-environment-accessibility-universal-design/`

每个域只创建 `README.md` 与 `AGENTS.md`，作为长期研究容器和边界说明，不新增数据、脚本、模型或操作协议。

## Consequences

- Research Domain Atlas 和 Domain Map 能把“空气、食品安全、职业暴露、医疗设备、感染控制和空间可达性”纳入主体持续性成立条件。
- 伦理边界需要新增空气暴露、食品污染、工业卫生、医疗设备、灭菌消毒和建成环境无障碍的禁止用途。
- 仓库检查脚本需要把 6 个域和本 ADR 纳入 required files / dirs。

## Non-Goals

- 不提供医疗、食品处理、现场暴露检测、PPE 选择、设备使用维修、灭菌消毒操作、建筑施工或合规法律建议。
- 不提供危险环境处置、污染规避、监管规避、设备破解、感染控制绕过、虚假合规或现场安全承诺。
- 不把这些基础设施域写成个人可执行方案。
