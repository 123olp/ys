# 行李与旅行个人物品连续性目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/baggage-personal-property-travel-continuity` |
| 所属层级 | `C3` - 可能性生成引擎层 |
| 父级容器 | `domains/c3-generation-engine` |
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


## 目录结构

```text
baggage-personal-property-travel-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义行李、关键随身物品、物品中断和责任边界如何影响移动主体的行动能力。
- `AGENTS.md`：说明本域维护边界和禁止用途。

## 维护规则

- 只沉淀行李中断、关键物品依赖、责任边界和恢复变量，不写个人索赔、违禁品或防盗处置建议。
- 涉及美国制度时优先使用 U.S. DOT、TSA、CBP、FTC 和 USA.gov 等公开资料。
- 不把本域写成行李理赔、机场找物、防盗追踪、海关规避或个人财产管理服务。
