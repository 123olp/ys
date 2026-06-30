# Uncertainty Quantification Model Calibration 目录说明

## 目录结构

```text
uncertainty-quantification-model-calibration/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义不确定性量化、模型校准、外部验证、漂移监测和报告边界。
- `AGENTS.md`：说明本目录的职责边界和维护规则。

## 边界

本目录只承载模型可信度、校准和不确定性治理。它不承载个人预测服务、临床诊断系统、保险/雇佣评分、自动化决策或未验证模型营销材料。

## 维护规则

- 所有模型输出必须标注验证状态和适用边界。
- 不允许把 toy model 或 conceptual chart 写成现实预测。
- 涉及个体风险时必须默认禁止输出确定日期、确定寿命和自动化决策。
- 新增方法必须说明验证指标、漂移风险、数据依赖和失败触发条件。
