# decontamination-exposure-triage-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/decontamination-exposure-triage-continuity` |
| 所属层级 | `C6` - 局部可能性解锁层 |
| 父级容器 | `domains/c6-local-unlocking` |
| 路径真相源 | `domains/_possibility-space-control/classification.tsv` |
| 复核状态 | `heuristic-v0.1` |

### 文件职责

- `README.md` 面向读者，说明研究对象、Human Infra 价值链路、证据边界、非目标和下一步资料入口。
- `AGENTS.md` 面向维护者和代理，说明目录结构、上下游依赖、禁止事项、更新规则和验证要求。

### 更新规则

- 修改本域对象、边界或上下游关系时，必须同步检查 README、AGENTS 和分类表中的 `physical_path`。
- 新增资料优先沉淀为 Source Signals、Source Cards、Claim-Evidence Matrix 或明确的证据段落，不把未经核验的摘要写成稳定结论。
- 若发现当前层级不符合“可能性空间控制力”标尺，先修改 `_possibility-space-control/rubric.md` 或 `classification.tsv`，再移动目录。

### 禁止事项

- 不把研究域写成个体行动处方、临床建议、法律建议、投资建议、工程操作手册或规避规则指南。
- 不在本目录保存无来源、无边界、无证据等级的断言。
- 不绕过父级 C1-C6 物理目录直接在 `domains/` 根目录新增正式研究域。
<!-- domain-agent-contract:end -->


`domains/c6-local-unlocking/decontamination-exposure-triage-continuity/` 是 Human Infra 的暴露后去污与分诊连续性域，负责把危险材料暴露后的系统入口、医疗转介和尊严保护建模为恢复基础设施。

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
