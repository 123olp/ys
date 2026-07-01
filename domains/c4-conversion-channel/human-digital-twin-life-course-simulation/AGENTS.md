# Human Digital Twin Life Course Simulation 目录说明

## 目录结构

```text
human-digital-twin-life-course-simulation/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义人类数字孪生、生命历程仿真、状态转移和场景模拟边界。
- `AGENTS.md`：说明本目录的职责边界和维护规则。

## 边界

本目录只承载模型结构、场景模拟语言和治理边界。它不承载个人数据、生产模型、临床服务、保险评分、雇佣筛选或个体行为控制系统。

## 维护规则

- 所有数字孪生表述必须说明是概念模型、toy model、研究原型还是临床验证系统。
- 新增变量必须声明来源、观测频率、误差、缺失机制和伦理边界。
- 不允许把模拟输出写成命运结论。
- 涉及个人数据时必须转向 `health-data-privacy-governance/` 和模型治理文档。
