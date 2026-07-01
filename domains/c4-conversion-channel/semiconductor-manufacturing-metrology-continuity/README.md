# Semiconductor Manufacturing Metrology Continuity

`semiconductor-manufacturing-metrology-continuity/` 研究半导体制造、工艺控制、量测、良率、洁净室、设备校准和制造供应连续性如何限制 AI、医学、传感器、通信和自动化工具的长期可得性。

> 核心问题：主体持续性的很多未来路径依赖芯片，但芯片不是抽象算力，而是由制造能力、计量能力、良率和供应链共同支撑的物理基础设施。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要 AI、传感器、医疗设备、自动化和通信持续升级
  -> 这些系统依赖稳定、可验证、可扩展的半导体制造
  -> 制造计量失准、良率下降或设备断供会压缩算力和工具供给
  -> 因此半导体制造计量是技术加速飞轮的上游物理约束域
```

## 关注对象

- Lithography、deposition、etch、metrology、inspection、yield learning、process control、contamination control 和 cleanroom operations。
- 量测标准、参考材料、校准链、缺陷检测、先进节点制造、成熟制程供给和制造韧性。
- 与 `compute-data-center-ai-infrastructure/` 的边界：算力基础设施域关注部署后的算力供给；本域关注芯片如何被制造出来。
- 与 `critical-minerals-materials-resilience/` 的关系：关键材料域关注上游物质输入；本域关注制造过程和计量可信性。

## Human Infra 模型链路

```text
半导体制造计量 T
  -> 改变芯片良率、制程稳定性、设备可用性、缺陷率和制造吞吐 X
  -> 改变 AI、医疗设备、传感器和通信硬件供给状态 S
  -> 改变技术采用延迟、设备短缺、工具成本上升和创新降速风险 λ(t)
  -> 影响主体可获得的计算、感知、诊断、自动化和未来选择权
```

## 非目标

- 不提供芯片制造工艺配方、设备绕过、出口管制规避、供应链规避或商业采购建议。
- 不把国家产业政策、公司产能声明或投资叙事写成主体持续性收益证明。
- 不替代 `semiconductor-advanced-packaging-continuity/`、`chip-design-eda-verification-ip-continuity/` 或 `ai-hardware-accelerator-performance-continuity/`。

## Source Signals

- NIST CHIPS for America: https://www.nist.gov/chips
- NIST CHIPS Metrology: https://www.nist.gov/chips/metrology
- CHIPS Manufacturing USA Institute: https://www.nist.gov/chips/research-and-development-programs
- SEMI Standards: https://www.semi.org/en/standards

## 下一步

- 建立 Semiconductor Manufacturing Card：node class, metrology dependency, yield risk, tool dependency, materials dependency, export/control boundary, continuity impact。
