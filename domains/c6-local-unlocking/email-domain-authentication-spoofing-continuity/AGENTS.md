# Email Domain Authentication Spoofing Continuity 架构说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/email-domain-authentication-spoofing-continuity` |
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


本目录承载邮件认证、域名冒充、phishing 和通知可信度研究资料。它只整理标准和边界，不提供钓鱼、绕过、投递优化或真实系统配置操作。

## 目录结构

```text
email-domain-authentication-spoofing-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须回到 CISA、NIST、IETF、FTC 或其他权威来源。
- 区分邮件来源认证、内容安全、邮箱账号安全、域名注册和通知可达性。
- 不收集真实邮件、邮件头、联系人、账号、DNS 管理权限、钓鱼样本或机构通信。
