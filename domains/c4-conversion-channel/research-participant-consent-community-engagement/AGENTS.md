# research-participant-consent-community-engagement 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/research-participant-consent-community-engagement` |
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


本目录维护研究参与者同意、社区参与和研究信任基础设施。它确保长期人体研究以主体权利和社区合法性为前提。

## 目录结构

```text
research-participant-consent-community-engagement/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义知情同意、撤回、社区参与、参与者回馈和研究信任如何支撑 Human Infra。
- 本目录只维护研究参与者治理框架，不保存个人身份、同意书原件或研究参与者数据。
- 所有资料必须区分伦理原则、法规要求、项目实践和社区反馈。

## 上下游关系

- 上游来自 `governance-rights/`、`health-data-privacy-governance/`、OHRP/PCORI/NIH 等资料。
- 下游服务纵向队列、样本库、登记系统、真实世界数据和人体研究论文页。
- 不替代 IRB、法律合规、隐私工程或社区代表机构。

## 维护规则

- 不提供规避同意、限制退出、隐瞒风险或诱导参与的操作。
- 不把“参与”写成单向宣传；必须保留反馈、再联系、退出和风险说明。
- 若新增人体研究数据域，必须检查本目录的同意与社区参与边界是否被引用。
