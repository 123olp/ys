# rural-health-access-geographic-equity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/rural-health-access-geographic-equity` |
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


本目录维护农村健康可及与地理公平域。它是 Human Infra 的“地点能否接入服务”层，负责地理距离、服务密度、宽带、交通和卫生人力如何影响主体持续性。

## 目录结构

```text
rural-health-access-geographic-equity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明农村地理、服务稀缺、交通、宽带、急救、药房和医院分布如何影响主体持续性。
- 本域只做公开农村健康、服务可达、资源分布、卫生人力和地理公平资料整理。
- 不提供个体医疗、保险、转诊、迁居、急救路线、补助申请、政策游说或商业选址建议。

## 维护规则

- 新增材料必须区分地理可达、数字可达、交通可达、卫生人力、药品可及和急救窗口。
- 不把农村差异写成个人责任、地区污名或即时资源判断。
- 涉及急救、医疗和福利服务时，只写结构性资料，不写个体操作建议。
