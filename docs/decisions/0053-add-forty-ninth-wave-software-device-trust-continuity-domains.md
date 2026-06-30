# 0053 Add Forty Ninth Wave Software Device Trust Continuity Domains

Date: 2026-06-30

## Status

Accepted

## Context

Human Infra 已覆盖数字账户、通信可达、账号恢复和资料可携带，但主体的数字行动还依赖更下层的设备、网络、软件、更新、开源维护者、证书信任、云服务退出和 API 运行时。账号存在并不等于主体可行动；如果设备不可维修、家庭网络失控、软件供应链被污染、补丁无法到达、开源维护断裂、PKI 失效、云服务锁定或关键 API 中断，主体仍会失去工作、学习、医疗、金融、创作和协作能力。

## Decision

新增第 49 波 8 个软件、设备与信任连续性域：

- `personal-computing-device-lifecycle-repair-continuity/`
- `home-network-router-iot-security-continuity/`
- `software-supply-chain-dependency-provenance-continuity/`
- `software-update-vulnerability-patch-continuity/`
- `open-source-maintainer-sustainability-continuity/`
- `pki-certificate-cryptographic-trust-continuity/`
- `cloud-service-exit-interoperability-continuity/`
- `api-platform-dependency-runtime-continuity/`

## Boundary

这些域只研究设备、网络、软件供应链、更新、开源维护、证书信任、云退出和 API 依赖如何影响主体持续性，不提供漏洞利用、绕过补丁、恶意软件供应链投毒、证书滥用、路由器入侵、账号规避、云锁定规避或具体安全事件处置。

## Consequences

- `README.md`、`docs/README.md`、`domains/README.md`、`docs/reference/domain-map.md`、`docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md` 和 `tools/check_repository.py` 必须把这 8 个域纳入索引。
- 后续资料卡片应优先回到 NIST SSDF、NIST IoT baseline、CISA Secure by Design、CISA KEV、CISA Open Source Roadmap、OpenSSF/SLSA、FTC Right to Repair、FCC Cyber Trust Mark、CA/Browser Forum、NIST key management 和 EU Data Act。
- 软件信任和设备连续性内容必须保留安全边界，只能讨论治理变量、断裂模式和审计框架。
