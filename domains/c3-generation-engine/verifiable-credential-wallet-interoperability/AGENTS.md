# verifiable-credential-wallet-interoperability

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/verifiable-credential-wallet-interoperability` |
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


本目录承载可验证凭证钱包与互操作资料。它研究主体如何长期携带可机器验证的身份、资格、学历、技能和授权证明，以及数字钱包、密钥和信任注册表失效如何造成资格断裂。

## 目录结构

```text
verifiable-credential-wallet-interoperability/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明本域对象、Human Infra 价值、边界、上下游和初始资料线索。
- 后续资料应区分签发者、持有者、验证者、钱包、DID、撤销状态、选择性披露、信任注册表和恢复机制。
- 本域不保存个人凭证、密钥或身份资料，不提供钱包部署、KYC、法律、金融、移民或个人申请建议。

## 维护规则

- 引用资料优先来自 W3C、NIST、Open Badges、官方标准组织和公开互操作案例。
- 必须保留隐私、同意、最小披露、撤销、密钥恢复、可访问性、平台锁定和反伪造边界。
- 不把可验证凭证写成规避身份核验、伪造资格、自动信任或永久安全方案。
