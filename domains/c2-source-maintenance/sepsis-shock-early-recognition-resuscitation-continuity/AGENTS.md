# sepsis-shock-early-recognition-resuscitation-continuity 目录说明

本目录维护脓毒症、感染性休克、早期识别和急性复苏资料。它是感染风险进入多器官失效和急性死亡边界的研究域。

## 目录结构

```text
sepsis-shock-early-recognition-resuscitation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义脓毒症和休克如何改变急性死亡、恢复能力和长期有效时间。
- 本目录只维护系统级变量、来源和边界，不保存个案实验室、培养、生命体征、药物或 ICU 资料。
- 资料进入本域时必须保留病程阶段、系统层级、时间窗、结局指标、证据强度和禁止用途。

## 上下游关系

- 上游来自 Surviving Sepsis Campaign、CDC、WHO、SCCM 和感染控制资料。
- 下游服务 `antimicrobial-resilience/`、`clinical-laboratory-diagnostic-quality/` 和 ICU 器官支持建模。
- 不替代医生、急诊、ICU、感染科、医院路径、公共卫生机构或个体医疗建议。

## 维护规则

- 不写抗生素、液体、升压药、源控制或 ICU 转诊建议。
- 不把系统性风险研究写成个人 triage 或治疗工具。
- 新增变量必须区分早识别、复苏、器官支持和恢复后负担。
