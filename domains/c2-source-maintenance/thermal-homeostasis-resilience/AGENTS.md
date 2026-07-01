# thermal-homeostasis-resilience 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/thermal-homeostasis-resilience` |
| 所属层级 | `C2` - 可能性源体维护层 |
| 父级容器 | `domains/c2-source-maintenance` |
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


`domains/c2-source-maintenance/thermal-homeostasis-resilience/` 保存热稳态与温度韧性研究域。它关注体温调节和温度极端如何影响主体持续性。

## 目录结构

```text
thermal-homeostasis-resilience/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责体温调节、热暴露、寒冷暴露、热适应、出汗、散热和温度风险。
- 本域可整理公开热健康、低温安全、气候健康和老年安全资料。
- 本域不提供中暑、低体温、补水、电解质、用药、降温、取暖或急救建议。

## 维护规则

- 任何热稳态主张必须说明变量、对象、证据等级、适用人群和跨域边界。
- 涉及急性热病、低体温或灾害场景时只写公共资料和非操作性安全边界。
- 新增文件或子目录时，同步更新本文件。
