# xenotransplantation-bioengineered-organ-replacement 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/xenotransplantation-bioengineered-organ-replacement` |
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


`domains/c2-source-maintenance/xenotransplantation-bioengineered-organ-replacement/` 保存异种移植、工程化器官、器官保存和替代性器官供给资料。

## 目录结构

```text
xenotransplantation-bioengineered-organ-replacement/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义器官替换平台在关键器官持续性中的位置、变量、风险和来源入口。
- `AGENTS.md`：记录本目录职责、允许新增材料类型和安全边界。

## 职责边界

- 本域关注关键器官替换如何改变主体持续性变量。
- 可以整理公开监管材料、移植数据、伦理边界、平台分类和风险变量。
- 不保存手术建议、免疫抑制方案、动物处理、病原检测、器官保存操作或监管规避内容。

## 维护规则

- 新增资料必须区分个案、临床试验、监管许可、长期功能和普及可及性。
- 不把短期存活写成长期可用。
- 新增文件或子目录时同步更新本文件。
