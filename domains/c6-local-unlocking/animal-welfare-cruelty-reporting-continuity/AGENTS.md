# animal-welfare-cruelty-reporting-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/animal-welfare-cruelty-reporting-continuity` |
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


本目录承载动物福利、虐待忽视报告和保护转介连续性资料。它关注动物福利与家庭/社区风险之间的系统边界，不提供个案报案、取证、执法或法律建议。

## 结构

```text
animal-welfare-cruelty-reporting-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分动物福利、虐待忽视、合法报告、执法转介、家庭安全、隐私和反私刑边界。
- 资料优先回到 USDA APHIS、AVMA、CDC、地方动物控制和公开动物福利资料。
- 不保存地址、照片、视频、举报线索、儿童资料、家庭暴力细节、动物伤情或个案执法资料。
