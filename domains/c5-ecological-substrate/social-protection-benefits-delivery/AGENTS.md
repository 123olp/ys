# social-protection-benefits-delivery 目录说明

`social-protection-benefits-delivery/` 是 Human Infra 的社会保护与福利递送域，负责研究公共福利和社会保护系统如何在风险冲击中接住主体。

## 目录结构

```text
social-protection-benefits-delivery/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义社会保护与福利递送域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做社会保护、福利服务、资格流程、行政负担、支付连续性和申诉路径资料整理。
- 个体福利申请、资格判断、材料准备、税务、法律、移民和规避制度不属于本域。

## 上下游关系

- 上游：`legal-identity-civil-registration/`、`health-literacy-navigation/`、`digital-identity-security/`。
- 下游：`food-security-nutrition-access/`、`housing-built-environment-stability/`、`energy-access-resilience/` 和 `financial-resilience-access/`。

## 维护规则

- 新增资料必须说明它影响资格、申请、续期、支付、申诉、等待、人工帮助还是行政负担。
- 禁止输出个体申请、规避制度、虚假材料或资格判断建议。
