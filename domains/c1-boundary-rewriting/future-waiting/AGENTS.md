# Future Waiting 架构说明

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
