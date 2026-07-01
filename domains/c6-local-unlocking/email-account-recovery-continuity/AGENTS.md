# email-account-recovery-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/email-account-recovery-continuity` |
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


本目录承载邮箱账号恢复连续性研究域，关注邮箱作为数字身份、通知、密码重置和服务恢复入口时的主体持续性价值。

## 目录结构

```text
email-account-recovery-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义邮箱账号、恢复邮箱、密码重置、通知和邮件归档如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 FTC、CISA、NIST、主要邮箱服务商公开文档和组织 IT 最佳实践。
- 不写个人邮箱找回、绕过验证、社工、账号接管、取证、入侵响应或法律建议。
- 涉及账号安全时只讨论变量、断裂模式和治理边界，不处理邮箱地址、验证码、密码、恢复码、邮件内容或登录记录。
- 新增指标必须注明口径：账号可访问性、恢复通道、通知可达性、归档完整性、停权风险或接管风险。
