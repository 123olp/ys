# hazwoper-responder-ppe-safety-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/hazwoper-responder-ppe-safety-continuity` |
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


`domains/c6-local-unlocking/hazwoper-responder-ppe-safety-continuity/` 是 Human Infra 的 HAZWOPER 响应者 PPE 与安全连续性域，负责把响应者保护建模为危险材料事故公共服务连续性基础设施。

## 目录结构

```text
hazwoper-responder-ppe-safety-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 HAZWOPER、PPE、呼吸防护、热压力、污染转移、疲劳和组织支持边界。
- 本域只整理公开培训制度、组织变量和风险边界。
- PPE 操作、呼吸器适配、现场等级判断、救援动作和职业合规建议不属于本域。

## 上下游关系

- 上游：`occupational-exposure-industrial-hygiene/`、`health-workforce-capacity/`、`chemical-safety-poison-control-toxicology/`。
- 下游：`hazmat-incident-command-emergency-response-continuity/`、`decontamination-exposure-triage-continuity/`、`healthcare-surge-triage-capacity-continuity/`。

## 维护规则

- 新增资料必须说明它支持响应者训练、PPE、呼吸防护、疲劳热压力、污染控制还是组织容量。
- 不得写入穿脱操作、进入危险区域、现场处置、规避监管或降低安全标准的信息。
