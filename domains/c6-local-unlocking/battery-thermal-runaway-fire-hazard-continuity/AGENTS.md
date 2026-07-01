# battery-thermal-runaway-fire-hazard-continuity 目录说明

`domains/c6-local-unlocking/battery-thermal-runaway-fire-hazard-continuity/` 是 Human Infra 的电池热失控与火灾风险连续性域，负责把电池化工具、储能和充电环境的失效风险建模为居住、消防、能源和产品安全接口。

## 目录结构

```text
battery-thermal-runaway-fire-hazard-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义锂离子电池、热失控、微出行、储能、召回、火灾烟气和住房接口。
- 本域只整理公开安全资料、变量模型和禁止用途。
- 电池维修、拆解、改装、充电方案、灭火操作、储能设计和产品推荐不属于本域。

## 上下游关系

- 上游：`product-safety-recall-systems/`、`building-fire-life-safety-codes/`、`grid-scale-storage-flexibility-continuity/`。
- 下游：`backup-power-generator-safety-continuity/`、`housing-built-environment-stability/`、`emergency-preparedness-response/`。

## 维护规则

- 新增资料必须说明它支持设备类别、充电环境、召回、火灾烟气、住房接口还是能源冗余权衡。
- 不得写入电池操作、拆解改装、灭火步骤、规避召回或制造热失控信息。
