# provider-directory-network-adequacy-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/provider-directory-network-adequacy-continuity` |
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

本目录承载 provider directory、网络充足性和可接诊信息连续性资料，关注医疗覆盖如何转化为真实可发现、可联系、可预约的服务入口。

## 边界

- 只整理公开资料、机制、变量、证据边界和研究问题。
- 不推荐 provider、保险计划、network tier、转诊路径、申诉策略或账单处理。
- 不保存个人保险、诊断、预约、通话、地址、残障或健康资料。

## 结构

```text
provider-directory-network-adequacy-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须标明来源、地区、适用保险类型和是否涉及网络充足性、目录准确性或可接诊状态。
- 个案选择、医疗、保险、法律和账单问题必须回到官方渠道、保险方或专业人员。
