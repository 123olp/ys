# AI Agency Safety

AI Agency Safety 负责整理 AI 代理、工具调用、授权、监督、审计和失效隔离如何影响主体持续性。

核心问题：

> AI 会放大主体能力，但当 AI 代表主体行动时，也可能越权、误导、泄露、替代或制造不可逆后果。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要用 AI 扩展认知、执行、研究和协作能力
  -> AI 代理会逐步获得工具、权限、记忆和外部行动接口
  -> 若代理不可控，主体能力放大会转化为自主性、隐私和安全风险
  -> 因此 AI 代理安全是认知增强进入长期行动系统的治理域
```

## 关注对象

- AI 代理、工具调用、权限分层、审批、回滚、审计和人类监督。
- 提示注入、数据泄露、幻觉、越权执行、目标漂移和不可逆行动。
- 人机协作、任务委托、长期记忆、代理身份、责任归属和失败隔离。
- AI 风险治理、生成式 AI 风险、评估、监测、事故响应和持续改进。

## Human Infra 模型链路

```text
AI 代理安全措施 T
  -> 改变授权边界、监督质量、审计能力和失效隔离 X
  -> 改变主体使用 AI 扩展行动的系统状态 S
  -> 降低代理越权、误导、泄露和不可逆执行风险 λ(t)
  -> 提高单位时间行动质量并保护主体自主性
```

## 非目标

- 不提供越狱、提示注入攻击、恶意自动化、数据窃取或规避安全控制的方法。
- 不把 AI 代理当成主体替代物；Human Infra 关注主体能力增强和可撤销委托。
- 不输出个体医疗、法律、金融或安全决策的自动执行建议。

## Source Signals

- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI RMF Generative AI Profile: https://www.nist.gov/itl/ai-risk-management-framework/ai-risk-management-framework-generative-ai-profile
- CISA AI resources: https://www.cisa.gov/ai

## 下一步

1. 建立 AI 代理权限与失败模式表：observe、suggest、draft、act、commit、recover。
2. 与 `cognitive-augmentation/`、`digital-identity-security/`、`governance-rights/` 建立代理授权和主体权利边界。
