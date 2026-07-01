# planetary-health-environment 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/planetary-health-environment` |
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


`domains/c6-local-unlocking/planetary-health-environment/` 保存星球健康与环境研究域。它关注空气、水、气候、污染、生态系统和食物系统如何影响主体持续性。

## 目录结构

```text
planetary-health-environment/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责环境暴露、气候风险、污染、生态系统和自然资源底座。
- 本域与 `risk-engineering/`、`resource-social-infra/` 和 `antimicrobial-resilience/` 交叉。
- 本域不提供违法规避、危险行为或个体化环境医学建议。

## 维护规则

- 任何环境主张必须说明暴露路径、受影响主体变量和系统性风险。
- 不把结构性环境风险压缩成个人生活方式建议。
- 新增文件或子目录时，同步更新本文件。
