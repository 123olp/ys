# biostasis-cryopreservation 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c1-boundary-rewriting/biostasis-cryopreservation` |
| 所属层级 | `C1` - 可能性边界改写层 |
| 父级容器 | `domains/c1-boundary-rewriting` |
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


`domains/c1-boundary-rewriting/biostasis-cryopreservation/` 保存生物停滞与冷冻保存研究域。它关注如何降低损耗、保存结构并等待未来修复。

## 目录结构

```text
biostasis-cryopreservation/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责冷冻保存、生物停滞、低温医学、休眠和保存到未来路径。
- 本域与 `future-waiting/` 共享“等待未来”问题，但不共享机制。
- 本域不提供灌流、冷冻、复温、给药、保护剂或人体保存操作步骤。

## 维护规则

- 任何保存主张必须区分结构保存、功能可逆、未来修复依赖和主体连续性。
- 任何“复活”或“永生”表述必须降级为条件性假设。
- 新增文件或子目录时，同步更新本文件。
