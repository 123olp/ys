# civic-participation-election-access 目录说明

`civic-participation-election-access/` 是 Human Infra 的公民参与与选举接入域，负责研究主体如何通过登记、投票、无障碍参与和公共反馈影响共同规则。

## 目录结构

```text
civic-participation-election-access/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义公民参与与选举接入域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做登记可达、投票可及、无障碍、选举标准、信任、审计和公共反馈资料整理。
- 竞选策略、政治操控、投票压制、选举干扰、设备攻击和个体法律建议不属于本域。

## 上下游关系

- 上游：`legal-identity-civil-registration/`、`information-integrity-trust/`、`digital-inclusion-connectivity/`。
- 下游：`governance-rights/`、`access-to-justice-legal-aid/`、`resource-social-infra/`。

## 维护规则

- 新增资料必须说明它影响登记、投票方式、无障碍、语言可达、信任、审计、争议处理还是公共反馈。
- 禁止输出竞选操控、微定向说服、投票压制、虚假信息、设备篡改、计票操控或选举干扰建议。
