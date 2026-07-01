# emergency-preparedness-response 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/emergency-preparedness-response` |
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


`emergency-preparedness-response/` 是 Human Infra 的应急准备与响应域，负责研究灾害、事故、公共卫生事件和急性危机中，预警、通信、救援、医疗、安置和恢复系统如何保护主体持续性。

## 目录结构

```text
emergency-preparedness-response/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义应急准备与响应域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做应急系统、公共卫生准备、预警通信、灾后恢复和抗冲击能力资料整理。
- 个体急救、医疗处理、撤离路线、危险环境操作、武器、暴力和生存操作指南不属于本域。

## 上下游关系

- 上游：`risk-engineering/`、`planetary-health-environment/`、`supply-chain-continuity/`。
- 下游：`healthcare-access-continuity/`、`transportation-access-mobility/`、`housing-built-environment-stability/` 和 `mental-health-affective-stability/`。

## 维护规则

- 新增资料必须说明它属于预警、通信、医疗、撤离、安置、恢复还是公共卫生准备。
- 禁止输出危险操作、个体急救替代、违法获取资源或恐慌性建议。
