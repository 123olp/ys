# cybersecurity-resilience-critical-services 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/cybersecurity-resilience-critical-services` |
| 所属层级 | `C5` - 可能性生态承载层 |
| 父级容器 | `domains/c5-ecological-substrate` |
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


本目录承载网络安全、关键服务韧性、事件响应和数字系统恢复如何保护主体持续性。

## 结构

```text
cybersecurity-resilience-critical-services/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 是本域的边界、模型链路、非目标和来源入口。
- 本域只讨论防御、韧性、治理和恢复，不提供攻击、入侵、绕过认证、漏洞利用或规避检测策略。
- 后续新增材料应优先是防御框架 Source Card、关键服务韧性变量、事件响应边界和安全治理模型。

## 上下游关系

- 上游：`digital-identity-security/`、`supply-chain-continuity/`、`standards-metrology-quality-infrastructure/`。
- 下游：`healthcare-access-continuity/`、`financial-inclusion-payment-systems/`、`public-service-design-accessibility/`。
- 相邻域：`ai-agency-safety/`、`health-data-privacy-governance/`、`emergency-alerts-communications/`。

## 维护规则

- 不提供攻击链、漏洞利用、权限提升、绕过认证、恶意软件、钓鱼或规避检测步骤。
- 不对具体目标做攻击面枚举或可执行利用建议。
- 若新增安全框架、事件模型或韧性指标，必须同步维护本文件和相关索引。
