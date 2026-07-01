# undersea-cable-internet-backbone-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/undersea-cable-internet-backbone-continuity` |
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


本目录维护海底光缆与全球互联网骨干连续性资料。它关注数字主体跨地域连接的物理网络底座。

## 目录结构

```text
undersea-cable-internet-backbone-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义海底光缆、登陆站、路由冗余和维修恢复如何影响主体持续性。
- 本目录不保存敏感位置、破坏方式、网络攻击、监控方法、运营商采购或地缘政治操作建议。

## 上下游关系

- 上游来自 FCC、ITU、CISA、ICPC 和公开通信韧性资料。
- 下游服务云、AI、远程医疗、科研协作、支付、数字保存和跨境沟通。
- 不替代 `telecommunications-network-resilience-continuity/`；本目录只拆全球骨干连接层。

## 维护规则

- 只记录公开、非敏感、聚合层面的韧性资料。
- 涉及安全敏感路径、具体脆弱点或破坏性内容必须排除。
