# decontamination-exposure-triage-continuity 目录说明

`domains/decontamination-exposure-triage-continuity/` 是 Human Infra 的暴露后去污与分诊连续性域，负责把危险材料暴露后的系统入口、医疗转介和尊严保护建模为恢复基础设施。

## 目录结构

```text
decontamination-exposure-triage-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义去污入口、暴露分流、医院准备、隐私尊严、家庭重聚和二次污染边界。
- 本域只整理公开准备框架、变量模型和风险边界。
- 去污步骤、医疗处理、分诊操作、采样、解毒和现场处置不属于本域。

## 上下游关系

- 上游：`hazmat-incident-command-emergency-response-continuity/`、`chemical-release-shelter-evacuation-continuity/`、`hazwoper-responder-ppe-safety-continuity/`。
- 下游：`healthcare-surge-triage-capacity-continuity/`、`overdose-poisoning-reversal-toxicology-continuity/`、`trauma-ptsd-adversity-recovery-continuity/`。

## 维护规则

- 新增资料必须说明它支持暴露入口、分流、医院准备、尊严保护、语言可达、家庭重聚还是二次污染风险。
- 不得写入去污操作、急救处理、规避医疗、污染转移或个体诊疗建议。
