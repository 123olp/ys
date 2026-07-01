# digital-identity-security 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/digital-identity-security` |
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


`domains/c4-conversion-channel/digital-identity-security/` 保存数字身份安全研究域。它关注身份、账号、凭据、恢复流程和服务入口如何影响主体持续性。

## 目录结构

```text
digital-identity-security/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责数字身份、账号恢复、认证、授权、委托访问和服务入口连续性。
- 本域可整理身份盗用、账户接管、数据可携带和数字遗产的高层风险框架。
- 本域不提供钓鱼、绕过认证、账号接管、漏洞利用或规避审查方法。

## 维护规则

- 任何数字身份主张必须说明对象、入口、恢复路径、失败模式和权利边界。
- 涉及账号安全时只写防护、治理和非操作性安全边界。
- 新增文件或子目录时，同步更新本文件。
