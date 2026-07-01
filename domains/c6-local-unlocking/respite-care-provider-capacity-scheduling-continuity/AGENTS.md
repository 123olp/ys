# respite-care-provider-capacity-scheduling-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/respite-care-provider-capacity-scheduling-continuity` |
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


本目录维护 respite care 供给、容量、预约排班、费用和服务中断连续性资料。它是家庭照护系统的恢复接口，不是具体照护安排建议入口。

## 目录结构

```text
respite-care-provider-capacity-scheduling-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 定义 respite capacity 和 scheduling 如何影响照护者恢复、被照护者安全和家庭照护持续性。
- 本目录只整理公开资料、制度机制、服务执行变量和边界。
- 不保存个人日程、家庭地址、健康、行为、照护者、费用或资格资料。

## 维护规则

- 新增资料必须区分 planned respite、emergency respite、adult day services、home care 和长期机构照护。
- 不输出 provider 推荐、资格判断、申请策略、护理任务、交接清单或安全监督方案。
- 涉及替代照护时，必须保留同意、信任、虐待/忽视风险和隐私边界。
