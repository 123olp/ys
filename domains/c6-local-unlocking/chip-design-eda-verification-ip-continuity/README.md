# Chip Design EDA Verification IP Continuity

`chip-design-eda-verification-ip-continuity/` 研究芯片设计、EDA 工具、硬件描述、验证、IP 复用、开源 ISA 和设计供应链如何决定计算硬件能否被持续创造、审查和迭代。

> 核心问题：制造能力只能生产已经设计并验证过的芯片。若设计工具、验证流程或 IP 供应链失效，算力增长会在晶圆厂之前中断。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要专用计算、低功耗设备、医疗芯片和可信硬件持续演化
  -> 芯片演化依赖 EDA、验证、IP、ISA、硬件安全和设计人才
  -> 设计失误或工具锁定会导致硬件缺陷、供应受限和创新变慢
  -> 因此芯片设计与验证是算力基础设施的前制造约束域
```

## 关注对象

- EDA toolchain、hardware description language、formal verification、simulation、emulation、IP blocks、open ISA、hardware security 和 design reuse。
- 设计可复现性、验证覆盖、IP 许可证、工具锁定、供应链来源、硬件漏洞和生命周期维护。
- 与 `safety-critical-software-formal-methods/` 的关系：形式化方法域关注安全关键软件；本域关注硬件设计验证和芯片 IP。
- 与 `software-supply-chain-dependency-provenance-continuity/` 的关系：软件供应链域关注软件依赖；本域关注硬件设计资产和 EDA 工具链。

## Human Infra 模型链路

```text
芯片设计与验证 T
  -> 改变设计周期、验证覆盖、IP 可信性、硬件缺陷率和工具可得性 X
  -> 改变专用芯片、医疗硬件、AI 加速器和边缘设备演化状态 S
  -> 改变硬件漏洞、设计返工、算力短缺和技术扩散失败风险 λ(t)
  -> 影响主体可获得的计算能力、设备安全和长期工具升级路径
```

## 非目标

- 不提供绕过芯片 IP 许可、破解 EDA、复制专有设计、硬件后门或供应链攻击方法。
- 不输出具体芯片设计、硬件安全利用或采购建议。
- 不把开源 ISA、EDA 自动化或 AI 设计工具写成无风险替代。

## Source Signals

- NIST CHIPS for America: https://www.nist.gov/chips
- RISC-V International: https://riscv.org/
- Accellera Systems Initiative: https://www.accellera.org/
- OpenROAD Project: https://theopenroadproject.org/

## 下一步

- 建立 Chip Design Continuity Card：design artifact, EDA dependency, verification method, IP license, ISA boundary, hardware security risk, maintenance path。
