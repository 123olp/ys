# Semiconductor Advanced Packaging Continuity

`semiconductor-advanced-packaging-continuity/` 研究先进封装、chiplet、interposer、HBM 集成、热管理、测试和封装供应连续性如何影响高性能计算、AI 加速器和低功耗边缘设备。

> 核心问题：未来算力不只来自更小晶体管，也来自封装、互连、内存靠近计算和系统级集成；封装断点会把芯片能力卡在制造之后、部署之前。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要更高能效、更高带宽、更高可靠性的计算硬件
  -> 先进封装决定 chiplet、HBM、互连、散热和系统集成能力
  -> 封装瓶颈会限制 AI、仿真、医学建模和边缘智能扩展
  -> 因此先进封装是算力增长从晶圆走向可用系统的转化域
```

## 关注对象

- Advanced packaging、chiplet architecture、2.5D/3D integration、HBM、substrate、interposer、test、thermal interface 和 reliability。
- 封装产能、标准接口、测试覆盖、热失效、供应集中、可维修性和系统级可靠性。
- 与 `semiconductor-manufacturing-metrology-continuity/` 的边界：制造域关注晶圆和制程；本域关注晶片之后的系统级封装。
- 与 `ai-hardware-accelerator-performance-continuity/` 的关系：AI 硬件性能依赖封装，但本域不评测模型性能。

## Human Infra 模型链路

```text
先进封装 T
  -> 改变带宽、能效、热密度、良率、可靠性和系统集成变量 X
  -> 改变 AI 训练推理、科学仿真、医疗建模和边缘设备状态 S
  -> 改变算力短缺、硬件失效、能耗上升和技术采用延迟风险 λ(t)
  -> 影响主体可使用的智能增强、研究速度和长期工具可得性
```

## 非目标

- 不提供封装工艺参数、供应商选择、采购路线、出口管制规避或商业投资建议。
- 不把封装路线图当成确定的算力增长承诺。
- 不替代芯片制造、芯片设计、数据中心或 AI 硬件评测域。

## Source Signals

- CHIPS National Advanced Packaging Manufacturing Program: https://www.nist.gov/chips/research-and-development-programs/national-advanced-packaging-manufacturing-program
- NIST CHIPS R&D Programs: https://www.nist.gov/chips/research-and-development-programs
- JEDEC Standards: https://www.jedec.org/
- SEMI Standards: https://www.semi.org/en/standards

## 下一步

- 建立 Packaging Continuity Card：package class, memory integration, thermal envelope, test coverage, supplier concentration, reliability risk, compute impact。
