# home-care-aide-personal-care-workforce-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/home-care-aide-personal-care-workforce-continuity` |
| 所属层级 | `C3` - 可能性生成引擎层 |
| 父级容器 | `domains/c3-generation-engine` |
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


本目录维护居家个人照护人员、direct care workforce、personal care attendant、排班稳定和上门服务连续性资料。它关注长期照护执行能力，不是雇佣、护理或福利建议入口。

## 目录结构

```text
home-care-aide-personal-care-workforce-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明 home care aide / personal care workforce 如何影响 ADL/IADL 支持、家庭照护负担和居家持续性。
- 本目录只整理公开资料、服务机制、劳动力条件和风险边界。
- 不保存家庭地址、排班、雇佣关系、人员身份、健康记录、工资或支付资料。

## 维护规则

- 新增资料必须区分 home health clinical care、personal care、independent living、consumer-directed care 和家庭无偿照护。
- 不输出雇佣合同、护理操作、排班策略、福利申请、工时授权或 agency 推荐。
- 涉及劳动力条件时，必须保留劳动权利、安全和隐私边界。
