# Chip Design EDA Verification IP Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/chip-design-eda-verification-ip-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->


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
