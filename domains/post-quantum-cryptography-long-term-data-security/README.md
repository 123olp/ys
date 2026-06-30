# Post Quantum Cryptography Long Term Data Security

`post-quantum-cryptography-long-term-data-security/` 研究后量子密码、长周期数据安全、加密迁移、身份凭据寿命和“现在收集、未来解密”风险，如何影响 Human Infra 的数字主体连续性。

> 核心问题：有效永生和主体持续性需要跨几十年甚至更长时间保存身份、医疗、研究、财务、作品和授权记录。若密码体系在未来被量子计算击穿，当前数据连续性会变成长期暴露风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 数字身份、医疗记录、研究资料和个人档案必须长期保密、完整和可验证
  -> 长期安全依赖密码算法、密钥管理、迁移计划、库存盘点和协议更新
  -> 若量子威胁或加密迁移失败，未来主体的隐私、身份和资源入口会被反向击穿
  -> 因此后量子密码是长周期数字主体连续性的安全域
```

## 关注对象

- 后量子公钥加密、签名、密钥交换、加密库存、协议迁移和 cryptographic agility。
- “harvest now, decrypt later” 风险、长期医疗/基因/神经数据、研究数据、数字身份和档案安全。
- 与 `cybersecurity-resilience-critical-services/` 的边界：网络安全域关注广义攻防和恢复；本域关注量子威胁下的长期密码迁移。
- 与 `digital-identity-security/` 的边界：数字身份域关注账号和凭据入口；本域关注底层密码算法寿命与迁移。

## Human Infra 模型链路

```text
后量子密码与长期数据安全 T
  -> 改变算法强度、密钥寿命、加密库存、迁移能力、协议敏捷性和长期保密变量 X
  -> 改变身份、医疗、研究、财务和个人档案的保密完整状态 S
  -> 改变未来解密、身份盗用、数据勒索、权限篡改和主体资料失控风险 λ(t)
  -> 影响数字连续性、资源入口、研究信任和主体持续性
```

## 非目标

- 不提供攻击、破解、规避审计、窃取密钥或绕过身份验证方案。
- 不替代组织级密码迁移、合规评估、密钥管理和安全工程审计。
- 不把某个算法或产品写成永久安全承诺。

## Source Signals

- NIST Post-Quantum Cryptography: https://csrc.nist.gov/projects/post-quantum-cryptography
- NIST finalized post-quantum encryption standards: https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards
- CISA Post-Quantum Cryptography Initiative: https://www.cisa.gov/quantum
- NSA CNSA 2.0: https://www.nsa.gov/Press-Room/News-Highlights/Article/Article/3148990/nsa-releases-future-quantum-resistant-qr-algorithm-requirements-for-national-se/

## 下一步

- 建立长期数据安全变量表：数据敏感期、算法、密钥长度、协议、库存、迁移状态、签名寿命和验证路径。
- 与 `digital-identity-security/`、`health-data-privacy-governance/`、`life-logging-personal-archives-continuity/` 和 `long-term-digital-preservation-format-migration/` 建立接口。
