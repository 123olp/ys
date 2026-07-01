# 生命事件与核心民事记录连续性目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/vital-records-life-event-continuity` |
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


## 目录结构

```text
vital-records-life-event-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义生命事件记录如何支撑身份、家庭关系、服务资格和长期制度识别。
- `AGENTS.md`：说明本域维护边界和禁止用途。

## 维护规则

- 只沉淀公共制度、记录类型、跨系统依赖和证据边界，不写个体证件办理流程。
- 涉及美国制度时优先使用 USA.gov、CDC/NCHS、州/地方 vital records 官方入口；涉及其他地区时必须标注地区适用性。
- 不把生命统计资料写成个人法律、移民、税务、福利、继承或家庭法院建议。
