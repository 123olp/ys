# Privacy Preserving Computation Federated Learning 目录说明

## 目录结构

```text
privacy-preserving-computation-federated-learning/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义隐私保护计算、联邦学习、差分隐私和安全协作学习在 Human Infra 中的职责边界。
- `AGENTS.md`：说明本目录的职责边界和维护规则。

## 边界

本目录只承载隐私保护计算机制、威胁模型和研究治理语言。它不承载攻击方法、再识别方法、密码协议实现、生产安全参数或个人数据处理流程。

## 维护规则

- 所有资料必须区分 privacy claim、utility claim 和 governance claim。
- 不允许把任何隐私增强技术写成绝对安全。
- 不允许提供模型反演、成员推断、再识别或隐私绕过步骤。
- 涉及同意、退出、授权和数据权利时必须链接到 `health-data-privacy-governance/`。
