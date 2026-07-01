# public-seating-shade-rest-cooling-access-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/public-seating-shade-rest-cooling-access-continuity` |
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


本目录承载公共座椅、遮阴、休息与降温可达连续性研究域，关注公共空间是否允许主体安全停留、恢复和继续行动。

## 目录结构

```text
public-seating-shade-rest-cooling-access-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义公共休息、遮阴、降温和冷却中心如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 CDC heat health、EPA heat islands、Ready.gov、地方公共卫生、交通和公园公开资料。
- 不写公共空间规避、设施占用、敌意设计破坏、露宿策略、实时人流跟踪或个案执法建议。
- 涉及公共休息设施时只讨论恢复能力、热暴露、无障碍、分布公平、维护和任务连续性。
