# primary-care-panel-appointment-access-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/primary-care-panel-appointment-access-continuity` |
| 所属层级 | `C6` - 局部可能性解锁层 |
| 父级容器 | `domains/c6-local-unlocking` |
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


## 职责

本目录承载初级照护、panel 和常规预约可达连续性资料，关注主体如何获得可持续、可回访、可转诊的常规医疗入口。

## 边界

- 只整理公开资料、机制、变量、证据边界和研究问题。
- 不提供医生推荐、诊断、检查、治疗、预约抢号、慢病方案或个案转诊。
- 不保存个人病历、保险、症状、用药、预约、门户账号或地址资料。

## 结构

```text
primary-care-panel-appointment-access-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分初级照护容量、panel、预约可达、FQHC/community health center 和患者关系连续性。
- 个体医疗和保险问题必须回到医生、诊所、保险方或官方服务渠道。
