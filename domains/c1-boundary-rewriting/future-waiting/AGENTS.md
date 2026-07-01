# Future Waiting 架构说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c1-boundary-rewriting/future-waiting` |
| 所属层级 | `C1` - 可能性边界改写层 |
| 父级容器 | `domains/c1-boundary-rewriting` |
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


`future-waiting/` 是 Human Infra 中负责“去未来 / 压缩等待”路径的研究域。它保存远期思想实验、相对论等待路径、休眠等待路径和其他低主观时间成本等待未来的概念模型。

## 目录结构

```text
future-waiting/
├── AGENTS.md
├── README.md
└── paths/
    └── black-hole-waiting-room.md
```

## 文件职责

- `README.md`：说明本子域的核心定位、当前路径、上下游关系和安全边界。
- `paths/black-hole-waiting-room.md`：记录“度规红移固有时差分路径”，并保留“黑洞等待室”作为传播名；重点维护定义、理论基础、路径对比、难点和证据边界。
- 相关 Web 论文页维护在 `web/src/pages/papers/`：`metric-redshift-recursive-waiting.astro`、`proper-time-differential-waiting-hypothesis.astro` 和 `controllable-metric-waiting-room-hypothesis.astro`，正文必须保持 arXiv HTML Paper Reuse Kit 的 DOM 契约。

## 上下游关系

- 上游依赖 `docs/reference/domain-map.md` 的子域边界。
- 上游依赖 `docs/reference/ethics-and-safety-boundaries.md` 的安全和非操作性边界。
- 上游依赖 `docs/reference/evidence-policy.md`，必须区分物理理论、思想实验、工程假设和现实可行性。

## 维护规则

- 本子域只能描述概念、证据、约束和风险，不提供可执行太空工程或人体实验方案。
- 新增路径必须说明：核心机制、主要赌注、与其他等待路径的区别、现实难点、反证点和安全边界。
- 不把“物理上存在的时间膨胀”写成“工程上可用的永生路线”。
- 不把科普材料、影视叙事或思想实验包装成已验证技术。
