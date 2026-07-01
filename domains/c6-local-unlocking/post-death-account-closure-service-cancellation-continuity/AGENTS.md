# post-death-account-closure-service-cancellation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/post-death-account-closure-service-cancellation-continuity` |
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


本目录承载死亡后账号关闭、服务取消和自动扣款收束连续性资料。它关注现代主体外部账户系统在死亡后如何停止产生费用、风险和任务摩擦。

## 结构

```text
post-death-account-closure-service-cancellation-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分 account closure、service cancellation、automatic payment stop、deceased account handling、data export 和 memorialization。
- 必须记录死亡证明要求、授权代表、身份盗用、资料误删、退款、隐私和平台政策差异。
- 不保存账号、密码、账单、死亡证明、银行卡、身份文件、联系人或平台资料。
