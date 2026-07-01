# ai-model-supply-chain-provenance-release-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-model-supply-chain-provenance-release-continuity` |
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


本目录维护 AI 模型供应链、来源证明和发布治理资料。它是模型 artifact 进入 Human Infra 工具链前的可信消费层。

## 目录结构

```text
ai-model-supply-chain-provenance-release-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义模型来源、权重、依赖、许可证、发布说明和撤回机制如何影响主体持续性。
- 本目录只维护供应链治理框架，不保存未授权权重、密钥、token、私有日志或受限 artifact。
- 资料进入本域时必须保留版本、来源、许可证、哈希/签名、依赖边界和撤回状态。

## 上下游关系

- 上游来自 OpenSSF/SLSA、Sigstore、CISA、NIST SSDF、model card 和软件供应链文献。
- 下游服务 `model-cards-ai-audit-documentation/`、`ai-agent-tool-permission-sandbox-continuity/` 和 AI 工具消费策略。
- 不替代 `software-supply-chain-dependency-provenance/`；该域关注通用软件供应链，本目录关注 AI 模型 artifact。

## 维护规则

- 不记录模型盗取、供应链投毒、签名伪造、许可证规避或私有 artifact 抓取方法。
- 不把公开可访问写成授权可使用。
- 若新增发布字段影响模型卡或工具链文档，必须同步更新索引。
