# chemical-release-shelter-evacuation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/chemical-release-shelter-evacuation-continuity` |
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


`domains/c6-local-unlocking/chemical-release-shelter-evacuation-continuity/` 是 Human Infra 的化学释放就地避险与撤离连续性域，负责把危险信号、保护行动、转移和恢复入口建模为事故期间主体持续性的执行基础设施。

## 目录结构

```text
chemical-release-shelter-evacuation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义化学释放避险、撤离、警报理解、交通转移和恢复入口的对象、链路、非目标和来源信号。
- 本域只整理公开应急资料、变量模型、风险边界和禁止用途。
- 现场处置、路线建议、去污步骤、防护操作、中毒处理和事故指挥不属于本域。

## 上下游关系

- 上游：`chemical-safety-poison-control-toxicology/`、`emergency-alerts-communications/`、`weather-climate-observation-forecasting/`。
- 下游：`disaster-recovery-relief-continuity/`、`transportation-access-mobility/`、`housing-built-environment-stability/`、`healthcare-access-continuity/`。

## 维护规则

- 新增资料必须说明它支持警报、避险、撤离、转介、恢复还是特殊人群连续性。
- 不得写入可执行事故处置、化学品操作、规避监管、恐慌传播或个体医疗建议。
