# software-supply-chain-dependency-provenance-continuity 目录说明

本目录承载软件供应链、依赖与来源证明连续性研究域，关注软件制品能否被信任、审计和恢复。

## 目录结构

```text
software-supply-chain-dependency-provenance-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义依赖、包管理器、构建、SBOM、签名、来源证明和供应链完整性如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 NIST SSDF、CISA SBOM/Secure by Design、OpenSSF、SLSA、Sigstore 和主流包管理生态公开文档。
- 不写供应链攻击、恶意包、依赖混淆、构建入侵、签名绕过或漏洞利用方法。
- 涉及安全事件时只讨论公开变量、治理框架、证据链和恢复边界。
- 新增指标必须注明口径：依赖可追溯性、SBOM 完整性、构建来源、签名覆盖、漏洞暴露或恢复时间。
