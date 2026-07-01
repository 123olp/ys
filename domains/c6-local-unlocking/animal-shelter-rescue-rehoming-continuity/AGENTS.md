# animal-shelter-rescue-rehoming-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/animal-shelter-rescue-rehoming-continuity` |
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


本目录承载动物收容、救助、寄养、领养和再安置连续性资料。它关注家庭照护断点中的转接系统，不提供领养、弃养、交易或现场救助建议。

## 结构

```text
animal-shelter-rescue-rehoming-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分收容容量、失主重聚、寄养领养、动物福利、公共卫生、志愿者安全和个案转接边界。
- 资料优先回到 AVMA、USDA APHIS、FEMA/Ready.gov、地方动物控制和公开收容政策资料。
- 不保存领养申请、家庭地址、动物照片、行为记录、虐待细节、机构内部资料或个案纠纷证据。
