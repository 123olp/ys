# machine-guarding-amputation-prevention-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/machine-guarding-amputation-prevention-continuity` |
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


本目录承载机器防护、危险点暴露和截肢预防连续性资料，只做研究域建模，不输出机器改装、现场安全、合规、维修或事故处理建议。

## 结构

```text
machine-guarding-amputation-prevention-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 定义 machine guarding、point of operation、nip point、rotating part、amputation hazard、interlock 和 maintenance bypass。
- 新增资料必须区分防护装置、危险点、维护状态、LOTO 接口、培训、near miss 和事故学习。
- 不保存机器照片、工艺参数、guard 设计、维修记录、事故材料、工伤资料或可识别企业/个人信息。

## 上下游

- 上游：`occupational-exposure-industrial-hygiene/`、`hazardous-energy-lockout-tagout-continuity/`、`human-factors-ergonomics-task-system-continuity/`。
- 下游：`trauma-system-hemorrhage-control-continuity/`、`workers-compensation-occupational-injury-benefit-continuity/`、`rehabilitation-functioning/`。

## 维护规则

- 资料优先回到 OSHA、NIOSH、BLS、公开安全警报和同行评审职业安全资料。
- 个案机器防护、事故、合规、产线恢复或法律问题必须转回雇主安全计划、OSHA/州监管、专业安全人员、设备制造商、工伤或法律渠道。
