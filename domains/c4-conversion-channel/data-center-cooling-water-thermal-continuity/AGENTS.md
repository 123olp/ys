# data-center-cooling-water-thermal-continuity 目录说明

本目录维护数据中心冷却、水与热管理连续性资料。它关注算力设施的热约束和环境承载边界。

## 目录结构

```text
data-center-cooling-water-thermal-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义冷却、水耗、热密度、冗余和环境约束如何影响 AI 与数字服务连续性。
- 本目录不保存施工方案、冷却系统操作步骤、供应商报价、现场参数或许可建议。

## 上下游关系

- 上游来自 IEA、DOE、ASHRAE、OCP 和公开数据中心可持续资料。
- 下游服务 AI 算力、云服务、数字保存、科研计算和远程协作。
- 不替代 `compute-data-center-ai-infrastructure/`；本目录只拆冷却和热管理层。

## 维护规则

- 必须区分能源指标、水指标、可靠性指标和环境影响指标。
- 不把单一效率指标写成整体可持续结论。
