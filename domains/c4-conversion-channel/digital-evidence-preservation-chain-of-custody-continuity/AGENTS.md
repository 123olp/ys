# Digital Evidence Preservation Chain Of Custody Continuity 架构说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/digital-evidence-preservation-chain-of-custody-continuity` |
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


本目录承载数字证据保存、链路记录、元数据和隐私最小化研究资料。它只整理公开原则和边界，不提供取证操作、越权访问、证据策略或个案判断。

## 目录结构

```text
digital-evidence-preservation-chain-of-custody-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须回到 NIST、SWGDE、NIJ、法院/平台公开材料或其他权威来源。
- 区分日常记录保存、专业数字取证、法律证据、平台申诉和隐私保护。
- 不收集真实案件材料、截图、日志、设备镜像、账号、受害者信息、未成年人资料或元数据样本。
