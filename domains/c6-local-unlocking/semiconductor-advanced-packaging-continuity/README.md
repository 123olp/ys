# Semiconductor Advanced Packaging Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/semiconductor-advanced-packaging-continuity` |
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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

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
