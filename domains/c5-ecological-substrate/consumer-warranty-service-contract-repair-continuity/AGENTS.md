# 消费品保修、服务合同与维修连续性目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/consumer-warranty-service-contract-repair-continuity` |
| 所属层级 | `C5` - 可能性生态承载层 |
| 父级容器 | `domains/c5-ecological-substrate` |
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
consumer-warranty-service-contract-repair-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义消费品保修、服务合同、维修承诺和替换承诺如何影响产品故障后的主体恢复能力。
- `AGENTS.md`：说明本域维护边界和禁止用途。

## 维护规则

- 只沉淀保修、服务合同、维修承诺、记录链和产品可维护性变量，不写个案索赔或维修操作。
- 涉及美国制度时优先使用 FTC、州消费者保护机构和官方公开资料。
- 不把本域写成保修索赔、维修建议、产品推荐、合同审查、诉讼策略或规避保修条件指南。
