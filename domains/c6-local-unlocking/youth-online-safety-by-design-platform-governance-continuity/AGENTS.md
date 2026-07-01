# youth-online-safety-by-design-platform-governance-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/youth-online-safety-by-design-platform-governance-continuity` |
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


## 目录结构

```text
youth-online-safety-by-design-platform-governance-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 是本域稳定入口，说明青少年线上安全设计与平台治理连续性的对象、价值、边界、上下游和资料线索。
- 本域只做平台安全设计和治理资料整理，不提供平台合规、个案安全、年龄验证、家长控制或内容审核规避建议。

## 维护规则

- 新增资料优先引用 HHS、NTIA、FTC、AAP、OECD 或公开平台治理资料。
- 必须区分安全默认、年龄适配、透明度、研究访问、举报响应和监管边界。
- 不得把未成年人保护写成儿童监控、画像扩张、歧视性识别或审查扩张。
