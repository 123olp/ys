# open-source-maintainer-sustainability-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/open-source-maintainer-sustainability-continuity` |
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


本目录承载开源维护者可持续性研究域，关注维护劳动、治理和资助如何影响关键软件生态连续性。

## 目录结构

```text
open-source-maintainer-sustainability-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义维护者时间、资金、安全响应、治理、交接、项目健康和关键依赖如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 OpenSSF、CISA、Linux Foundation、GitHub 公开报告、基金会治理资料和项目健康研究。
- 不写项目接管、社工、供应链攻击、漏洞披露滥用、骚扰或维护者隐私挖掘。
- 涉及具体项目时只使用公开资料，并避免把单个维护者暴露为风险靶点。
- 新增指标必须注明口径：维护者负载、bus factor、release cadence、安全响应、资助覆盖或治理交接。
