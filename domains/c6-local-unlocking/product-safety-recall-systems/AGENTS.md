# product-safety-recall-systems 目录说明

`product-safety-recall-systems/` 是 Human Infra 的产品安全与召回系统域，负责研究外部产品缺陷如何被报告、预警、召回和纠正，避免工具系统反向伤害主体。

## 目录结构

```text
product-safety-recall-systems/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义产品安全与召回系统域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做消费品、食品、药品、医疗器械、车辆缺陷报告、召回通知、纠正措施和风险沟通资料整理。
- 个体购买、维修、改装、医疗器械使用、药品停用、车辆维修、索赔和绕过安全装置不属于本域。

## 上下游关系

- 上游：`supply-chain-continuity/`、`information-integrity-trust/`、`digital-inclusion-connectivity/`。
- 下游：`healthcare-access-continuity/`、`risk-engineering/`、`resource-social-infra/`。

## 维护规则

- 新增资料必须说明它影响产品类型、缺陷报告、不良事件、召回覆盖、通知到达、纠正、替代路径还是高风险人群。
- 禁止输出维修、改装、绕过召回、安全装置规避、药品停用、医疗器械操作、车辆处理或法律索赔建议。
