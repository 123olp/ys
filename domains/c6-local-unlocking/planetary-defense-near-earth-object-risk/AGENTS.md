# AGENTS.md

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/planetary-defense-near-earth-object-risk` |
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


## 职责

本目录维护近地天体、行星防御和撞击尾部风险对 Human Infra 的影响。重点是监测、预警、偏转、响应和文明级连续性。

## 文件

```text
planetary-defense-near-earth-object-risk/
├── AGENTS.md
└── README.md
```

## 上游

- `domains/c6-local-unlocking/risk-engineering/`
- `domains/c6-local-unlocking/space-extreme-habitation/`
- `domains/c5-ecological-substrate/weather-climate-observation-forecasting/`
- `domains/c5-ecological-substrate/continuity-of-government-public-administration-resilience/`

## 下游

- 行星级尾部风险、食品系统、公共服务、基础设施和长期未来选择权。

## 边界

- 不做具体天体风险预测。
- 不输出恐慌、军事化、规避公共响应或私人避险操作指南。
- 证据必须回到 NASA、CNEOS、IAWN 或同等级权威来源。
