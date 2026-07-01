# ai-model-supply-chain-provenance-release-continuity 目录说明

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
