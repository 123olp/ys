# illegal-dumping-litter-neighborhood-sanitation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/illegal-dumping-litter-neighborhood-sanitation-continuity` |
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


本目录承载非法倾倒、乱扔垃圾和邻里卫生连续性研究域，关注家庭外部废弃物治理如何影响公共行动半径、住房稳定和社区韧性。

## 目录结构

```text
illegal-dumping-litter-neighborhood-sanitation-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义非法倾倒、乱扔垃圾、清理责任、环境正义和邻里任务连续性的关系。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 EPA、地方固废/311/环境执法、公共卫生、消防和环境正义资料。
- 不写非法倾倒、规避监控、规避执法、私自清理危险废物、现场对抗或法律策略。
- 新增指标必须注明口径：废弃物类型、地点责任、举报/清理路径、通行风险、害虫/火灾风险或社区影响。
- 涉及危险材料、灾后碎片、私人财产、执法或邻里冲突时，必须保留专业和地方规则边界。
