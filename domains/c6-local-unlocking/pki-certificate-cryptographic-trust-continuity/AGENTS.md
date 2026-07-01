# pki-certificate-cryptographic-trust-continuity 目录说明

本目录承载 PKI、证书与密码信任连续性研究域，关注证书、密钥和根信任链如何支撑数字服务持续可信。

## 目录结构

```text
pki-certificate-cryptographic-trust-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义 PKI、TLS 证书、CA、密钥管理、吊销、根信任、证书透明度和算法迁移如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 CA/Browser Forum、NIST、IETF、CISA 和厂商证书生命周期公开文档。
- 不写伪造证书、TLS 绕过、流量截获、CA 滥用、密钥窃取或攻击配置。
- 涉及证书事故时只讨论公开案例、变量、治理边界和恢复模式。
- 新增指标必须注明口径：到期风险、密钥轮换、吊销机制、根信任、算法迁移或服务影响。
