# social-connection-relational-infra 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/social-connection-relational-infra` |
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


`domains/c6-local-unlocking/social-connection-relational-infra/` 保存社会连接与关系基础设施研究域。它关注关系网络如何支撑主体行动、恢复、照护和未来选择权。

## 目录结构

```text
social-connection-relational-infra/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责孤独、社会隔离、社会支持、家庭照护、社区信任和协作网络的研究整理。
- 本域可整理公共健康资料、关系变量、风险模型和服务连接问题。
- 本域不提供心理治疗、危机服务替代、社交操控或组织控制方案。

## 维护规则

- 任何关系主张必须区分结构性连接、主观孤独、支持质量和服务可及。
- 与心理健康、资源基础设施、治理权利和照护系统交叉时必须标注主拥有域。
- 新增文件或子目录时，同步更新本文件。
