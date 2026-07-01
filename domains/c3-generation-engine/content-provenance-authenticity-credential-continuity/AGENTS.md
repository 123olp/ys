# Content Provenance Authenticity Credential Continuity 架构说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/content-provenance-authenticity-credential-continuity` |
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


本目录承载内容来源、内容凭据、发布者身份和真实性验证连续性研究资料。它只组织公开标准、变量和边界，不提供伪造、绕过、取证结论或平台处置方案。

## 目录结构

```text
content-provenance-authenticity-credential-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须回到 C2PA、Content Credentials、NIST、W3C 或其他权威来源。
- 区分来源证明、内容真实性、法律证据、平台审核和新闻事实核查，不把它们混成一个概念。
- 不收集真实文件、元数据、个人身份、平台账号、未公开证据或待验证争议内容。
