# telehealth-remote-monitoring-access 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/telehealth-remote-monitoring-access` |
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


`domains/c4-conversion-channel/telehealth-remote-monitoring-access/` 是 Human Infra 的远程医疗与居家监测接入域，负责把虚拟照护、远程随访、居家监测、设备和升级路径建模为医疗连续性的空间扩展条件。

## 目录结构

```text
telehealth-remote-monitoring-access/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义远程医疗、远程患者监测、居家设备、数字照护连续性和服务升级边界。
- 本域只做公开资料整理、变量建模、证据边界和远程照护断点分析。
- 诊断、分诊、设备处方、治疗建议、报销判断、平台背书和急诊替代不属于本域。

## 上下游关系

- 上游：`digital-inclusion-connectivity/`、`patient-data-interoperability/` 和 `health-literacy-navigation/`。
- 下游：`healthcare-access-continuity/`、`caregiving-long-term-care/`、`measurement-feedback/` 和慢病相关健康域。

## 维护规则

- 新增资料必须说明它支持的是服务可达、监测可见、设备可靠、升级路径、覆盖规则、隐私安全还是临床责任变量。
- 不能把远程医疗资料写成具体医疗服务、设备、保险或治疗建议。
