# Biometric Identifier Template Governance Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/biometric-identifier-template-governance-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->


Biometric Identifier Template Governance Continuity 关注人脸、指纹、声纹、虹膜、步态、掌纹和其他 biometric template 如何影响身份认证、安全、监控、误识别、不可撤销暴露和主体连续性。

## 对象

- Biometric identifier、biometric template、facial recognition、voiceprint、fingerprint、iris、liveness 和 matching threshold。
- 误识别、偏差、模板泄露、不可撤销性、身份盗用、访问控制、公共空间监控和供应商治理。
- 医疗、金融、学校、工作场所、公共安全、旅行、设备解锁和门禁中的生物特征使用。

## Human Infra 价值

```text
主体持续性需要身体特征不被不可逆地变成脆弱凭据
-> 生物特征把身体、声音和行为转成身份凭据和监控信号
-> 一旦模板泄露、误识别或被不当复用，主体难以像密码一样重置自己
-> 模板治理、最小化、准确性审查、替代路径和用途限制降低不可逆身份风险
-> 主体更能安全进入服务，同时保留退出、纠错和免受错误识别的能力
```

## 边界

- 本域不提供人脸识别部署、绕过生物认证、deepfake、声纹伪造、指纹复制、门禁规避或反识别规避方法。
- 不判断某 biometric system 是否合规、某次匹配是否准确或某机构是否可以使用生物特征。
- 不收集、生成、存储或分析真实人脸、声纹、指纹、虹膜、步态或模板数据。
- 只整理公开资料、治理变量、准确性风险、替代路径和禁止用途。

## 上下游

- 上游：`digital-identity-security/`、`data-breach-notification-identity-recovery-continuity/`、`health-data-privacy-governance/`。
- 下游：`aviation-security-screening-identity-continuity/`、`workplace-accommodation-return-to-work-continuity/`、`online-safety-digital-harm-prevention/`。

## Source Signals

- NIST face recognition and biometric evaluation resources.
- Federal Trade Commission biometric information and privacy enforcement materials.
- NIST Privacy Framework and Digital Identity Guidelines.
