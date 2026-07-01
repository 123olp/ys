# health-data-privacy-governance 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/health-data-privacy-governance` |
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


`domains/c4-conversion-channel/health-data-privacy-governance/` 是 Human Infra 的健康数据隐私治理域，负责把敏感健康、基因、行为、神经和服务使用数据的权利、安全和用途边界建模为主体持续性的信任条件。

## 目录结构

```text
health-data-privacy-governance/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义健康数据隐私治理的对象、链路、非目标和来源信号。
- 本域只做公开制度资料、治理变量、失败模式和伦理边界整理。
- 法律意见、合规认证、真实数据处理架构、去标识化保证、数据共享许可和安全攻击方法不属于本域。

## 上下游关系

- 上游：`governance-rights/`、`digital-identity-security/` 和 `measurement-feedback/`。
- 下游：`patient-data-interoperability/`、`healthcare-access-continuity/`、`longevity-evidence/` 和 `synthetic-biology-biosecurity/`。

## 维护规则

- 新增资料必须说明它支持的是同意、撤回、隐私、安全、共享、受试者保护、基因数据治理还是信息阻断边界。
- 不能把治理资料写成法律结论、合规保证、数据处理建议或绕过隐私边界的方法。
