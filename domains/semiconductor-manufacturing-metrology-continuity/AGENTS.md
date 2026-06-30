# semiconductor-manufacturing-metrology-continuity 目录说明

本目录维护半导体制造与计量连续性资料。它是 Human Infra 技术加速飞轮的上游硬件制造层。

## 目录结构

```text
semiconductor-manufacturing-metrology-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义制造计量、良率、设备校准和供应连续性如何影响主体持续性。
- 本目录只保存公开、非操作性研究资料，不保存工艺配方、设备参数、厂商机密、采购合同或规避控制方法。

## 上下游关系

- 上游来自 NIST CHIPS、半导体计量、标准组织和公开产业韧性资料。
- 下游服务 AI 算力、医疗设备、传感器、机器人、通信和自动化相关域。
- 不替代 `critical-minerals-materials-resilience/`；该域关注材料，本目录关注制造与计量。

## 维护规则

- 只记录证据边界、供应连续性和模型接口。
- 不输出制造操作步骤、规避监管或采购建议。
- 新增资料必须标注公开来源、适用制程层级和证据边界。
