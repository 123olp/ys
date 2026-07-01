# Freight Logistics Port Cold Chain Continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/freight-logistics-port-cold-chain-continuity` |
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


本目录承载货运、港口、仓储、冷链和关键物资物流连续性研究，关注资源如何真实到达人。

## 目录结构

```text
freight-logistics-port-cold-chain-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 研究货运网络、港口、仓储、冷链、运输节点、最后一公里和关键物资配送。
- 上游连接供应链、制造、农业、药品和关键材料；下游连接医疗、食物、灾害恢复和日常服务连续性。
- 不提供走私、规避海关、制裁规避、非法运输、物流攻击、商业操作或投资建议。

## 维护规则

- 物流资料必须区分公共研究、企业运营、国家安全和商业敏感信息。
- 不发布可帮助破坏、规避或攻击物流节点和安全控制的信息。
- 涉及药品、疫苗、食物和救灾物资时，必须保留冷链、质量和监管边界。
