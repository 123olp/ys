# veterans-health-benefits-navigation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/veterans-health-benefits-navigation-continuity` |
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


本目录维护退伍军人健康、福利与导航连续性域。它是 Human Infra 的“军转民制度转换”层，负责 VA health care、benefits、records、community care、住房、就业和家庭支持如何影响主体持续性。

## 目录结构

```text
veterans-health-benefits-navigation-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明退伍军人服务导航、医疗福利、记录、创伤支持、住房、就业和家庭照护如何影响主体持续性。
- 本域只做公开退伍军人健康、福利导航、军转民衔接和社区服务资料整理。
- 不提供个体福利申请、claims、appeals、医疗、心理危机、住房、就业、法律或军事记录纠错建议。

## 维护规则

- 新增材料必须区分医疗照护、福利资格、记录、住房、就业、家庭支持和危机服务系统。
- 不把退伍军人健康风险写成污名画像、个体失败或商业获客入口。
- 涉及危机、医疗、福利和法律服务时，只写结构性资料，不写个体操作建议。
