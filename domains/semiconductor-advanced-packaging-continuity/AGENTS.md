# semiconductor-advanced-packaging-continuity 目录说明

本目录维护半导体先进封装连续性资料。它解释芯片从晶圆能力转化为系统级算力的封装接口。

## 目录结构

```text
semiconductor-advanced-packaging-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义先进封装、chiplet、HBM、互连、测试和热管理如何影响主体持续性。
- 本目录不保存工艺参数、封装设计文件、供应商报价、采购策略或出口管制规避材料。

## 上下游关系

- 上游来自 CHIPS packaging program、JEDEC、SEMI 和公开封装可靠性资料。
- 下游服务 AI 硬件、数据中心、边缘智能、医学设备和传感器平台。
- 不替代 `semiconductor-manufacturing-metrology-continuity/`；本目录只管封装与系统集成层。

## 维护规则

- 每条资料必须说明它支持的是封装能力、测试可靠性、产能韧性还是算力转化边界。
- 不把产业路线图写成确定的主体收益。
