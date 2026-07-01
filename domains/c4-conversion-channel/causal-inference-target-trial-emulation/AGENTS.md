# Causal Inference Target Trial Emulation 目录说明

## 目录结构

```text
causal-inference-target-trial-emulation/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义因果推断、目标试验模拟、识别条件和 Human Infra 干预评估链路。
- `AGENTS.md`：说明本目录的职责边界和维护规则。

## 边界

本目录只承载因果评估框架、变量定义、证据边界和研究设计语言。它不承载个人医疗建议、治疗策略、试验报名建议、个体风险预测或真实世界数据处理脚本。

## 维护规则

- 新增内容必须明确区分相关、预测和因果。
- 涉及干预结论时必须写清目标试验要素：对象、时间零点、策略、对照、随访、结局和分析。
- 所有来源必须回到论文、指南或公开方法学资料。
- 不允许把机制合理性、动物实验或短期 biomarker 变化直接写成寿命因果结论。
