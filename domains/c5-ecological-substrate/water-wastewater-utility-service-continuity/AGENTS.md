# Water Wastewater Utility Service Continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/water-wastewater-utility-service-continuity` |
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


本目录承载饮用水、污水处理和水务公用事业服务连续性研究，关注水务系统如何支撑卫生、医疗、家庭和社区恢复。

## 目录结构

```text
water-wastewater-utility-service-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 研究取水、饮用水处理、配水、储水、污水收集处理、管网维护、水质监测、应急供水和服务恢复。
- 上游连接水资源、电网、公共工程、实验室、监管和资金；下游连接家庭卫生、医疗清洁、公共空间、感染控制和灾后恢复。
- 不提供设施操作、化学投加、采样检测、工程维修、排污绕行、设施弱点、水质个案判断、缴费争议或法律建议。

## 维护规则

- 水务资料必须区分公开韧性框架、统计数据、消费者公告和敏感设施信息。
- 不记录可用于攻击、污染、规避、绕排或破坏水务/污水设施的细节。
- 涉及实时水质、停水、煮沸通知或污染事件时，只引用官方公告，不做操作指挥。
