# transportation-access-mobility 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/transportation-access-mobility` |
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


`transportation-access-mobility/` 是 Human Infra 的交通接入与日常移动域，负责研究外部交通系统如何让主体连接到医疗、工作、食物、照护、社区和应急资源。

## 目录结构

```text
transportation-access-mobility/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义交通接入域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做交通可达性、无障碍、出行负担、交通安全和服务连接资料整理。
- 个体路线、驾驶、车辆、交通法律、应急撤离和出行操作建议不属于本域。

## 上下游关系

- 上游：`housing-built-environment-stability/`、`physical-activity-mobility/`、`financial-resilience-access/`。
- 下游：`healthcare-access-continuity/`、`occupational-work-design/`、`social-connection-relational-infra/` 和 `emergency-preparedness-response/`。

## 维护规则

- 新增资料必须区分外部交通可达性与身体移动能力。
- 禁止输出具体路线、撤离操作、驾驶法律或车辆购买建议。
