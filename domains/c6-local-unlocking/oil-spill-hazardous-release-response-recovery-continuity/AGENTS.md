# oil-spill-hazardous-release-response-recovery-continuity 目录说明

`domains/c6-local-unlocking/oil-spill-hazardous-release-response-recovery-continuity/` 是 Human Infra 的油污与危险释放响应恢复连续性域，负责把水域/海岸污染事件建模为健康、收入、食物水源和社区恢复接口。

## 目录结构

```text
oil-spill-hazardous-release-response-recovery-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义油污和危险释放、海岸水域恢复、工人安全、收入断点和长期监测边界。
- 本域只整理公开响应恢复资料、变量模型和禁止用途。
- 清理操作、围控分散、采样、索赔策略、法律判断和现场行动不属于本域。

## 上下游关系

- 上游：`water-resources-hydrology-flood-drought-management/`、`waste-management-hazardous-materials-continuity/`、`chemical-safety-poison-control-toxicology/`。
- 下游：`food-security-nutrition-access/`、`workforce-employment-services/`、`disaster-recovery-relief-continuity/`。

## 维护规则

- 新增资料必须说明它支持污染识别、响应恢复、水域海岸、工人安全、收入食物水源还是长期监测。
- 不得写入清理步骤、现场进入、法律索赔、责任规避或污染制造信息。
