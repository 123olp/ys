# child-care-subsidy-ccdf-payment-continuity 目录说明

`child-care-subsidy-ccdf-payment-continuity/` 是 Human Infra 的托育补贴、CCDF 与支付连续性执行域，负责研究补贴资格、授权、续期、共付和 provider payment 如何影响家庭托育稳定性。

## 目录结构

```text
child-care-subsidy-ccdf-payment-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义托育补贴支付域的对象、链路、非目标和来源信号。
- 本域只整理政策机制、行政负担和支付连续性变量，不做个体资格判断、申请代办或申诉建议。
- 家庭收入、儿童身份、税务资料、补贴材料、雇佣证明和账号凭据不得进入本域。

## 上下游关系

- 上游：`social-protection-benefits-delivery/`、`administrative-burden-procedural-friction/`、`childcare-family-continuity/`。
- 下游：`child-care-availability-affordability-continuity/`、`financial-resilience-access/`、`workforce-employment-services/`。

## 维护规则

- 新增资料必须说明它影响资格、授权、续期、共付、支付、provider 参与、行政负担还是服务中断。
- 禁止输出福利申请、资格规避、虚假材料、支付套利、法律或税务建议。
