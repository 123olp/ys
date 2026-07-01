# Public Works Civil Infrastructure Asset Management

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/public-works-civil-infrastructure-asset-management` |
| 所属层级 | `C4` - 可能性转换通道层 |
| 父级容器 | `domains/c4-conversion-channel` |
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


本目录承载公共工程和土木基础设施资产管理研究，关注实体资产生命周期如何支撑日常行动和公共服务。

## 目录结构

```text
public-works-civil-infrastructure-asset-management/
├── AGENTS.md
└── README.md
```

## 职责边界

- 研究道路、桥梁、隧道、排水、公共设施、资产登记、状态评估、维护优先级、生命周期成本和服务水平。
- 上游连接公共预算、采购、标准、材料和气候风险；下游连接交通、医疗可达、物流、应急、城市运行和居住安全。
- 不提供工程设计、施工、检查、维修、采购、敏感弱点、绕行、破坏、投标、索赔或法律建议。

## 维护规则

- 公共工程资料必须区分公开资产管理框架、统计报告、标准和具体设施敏感信息。
- 不记录可用于攻击、规避、破坏或利用基础设施弱点的细节。
- 涉及工程安全和采购时，只保留公共研究材料，不做个案判断。
