# AI Hardware Accelerator Performance Continuity

`ai-hardware-accelerator-performance-continuity/` 研究 GPU、TPU、NPU、AI accelerator、benchmark、能效、内存带宽、互连、软件栈和可用性如何决定 AI 增强能否持续、可负担、可复现地运行。

> 核心问题：AI 能力不是只由模型决定；硬件性能、能效、内存、驱动和基准有效性共同决定主体是否真正获得可用智能。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要 AI 长期扩展研究、诊断、自动化、学习和问题求解
  -> AI 运行依赖加速器硬件、内存、互连、驱动、编译器和能效
  -> 硬件不可得、性能不可测或软件栈不稳定会让 AI 增强失效
  -> 因此 AI 硬件加速器性能是 AI 连续性从模型走向可运行能力的执行域
```

## 关注对象

- GPU/TPU/NPU、training/inference benchmark、memory bandwidth、interconnect、compiler、driver、runtime、power efficiency 和 cluster availability。
- 性能基准有效性、硬件供应、驱动兼容、算子支持、能耗、排队、故障率和复现实验环境。
- 与 `ai-resource-cost-latency-budget-continuity/` 的边界：预算域关注使用侧成本和延迟；本域关注底层硬件能力和性能可信性。
- 与 `ai-evaluation-benchmark-validity-continuity/` 的关系：AI 评测域关注模型任务能力；本域关注硬件性能与能效评测。

## Human Infra 模型链路

```text
AI 加速器性能 T
  -> 改变吞吐、延迟、能效、内存容量、互连、驱动稳定和硬件可得性 X
  -> 改变 AI 工具、科研仿真、自动化 agent 和多模态系统运行状态 S
  -> 改变任务排队、成本上升、能力不可复现和服务中断风险 λ(t)
  -> 影响主体的认知增强、研究速度、有效时间和未来技术采用能力
```

## 非目标

- 不提供绕过云配额、挖矿、盗用 GPU、破解驱动、规避许可或供应链攻击方法。
- 不输出硬件采购、投资、交易或个体部署建议。
- 不把单一 benchmark 分数写成真实主体收益。

## Source Signals

- MLCommons Benchmarks: https://mlcommons.org/benchmarks/
- MLPerf: https://mlcommons.org/
- NIST AI: https://www.nist.gov/artificial-intelligence
- Green Software Foundation: https://greensoftware.foundation/

## 下一步

- 建立 AI Hardware Card：accelerator class, training/inference workload, memory, interconnect, energy, benchmark, runtime stack, availability, cost coupling。
