# SBI/OI Literature Review

Source draft: `<windows-home>\Downloads\sbi_oi_literature_review_draft.md`.

This review summarizes the local Cortical Labs / SBI / OI literature packet as a Human Infra research-domain artifact. It is not a fact of engineering maturity, a claim of consciousness, or an experimental protocol.

## 摘要

体外神经系统研究正在从传统神经发育、疾病建模和药物筛选，扩展为一种可嵌入数字环境的信息处理平台。Synthetic Biological Intelligence, Organoid Intelligence 和 Bioengineered Intelligence 形成了相互交叉但目标不同的路线：SBI 偏向工程化闭环信息处理，OI 偏向脑类器官学习/记忆机制与生物计算，BI 偏向工程构建可用的神经回路。

现有文献显示，体外神经网络在高密度多电极阵列、实时闭环刺激记录、结构化反馈和生命支持系统耦合下，能够表现任务相关活动重组、有限形式学习、近临界动力学变化，以及对药物干预的行为层面响应。这些结果提示，体外神经组织不仅可以作为细胞状态模型，也可能成为研究生物学习、主动推断、样本效率和信息处理层级的实验系统。

证据边界必须明确：DishBrain/Pong 证明的是简化环境中的闭环适应，不是通用智能或现象意识；OI 的学习记忆构件证明的是分子、突触和网络基础，不等于完整认知主体；agency 和 sentience 只能在操作定义下讨论，不能混写为 consciousness。

## 研究问题

```text
体外神经组织
-> 连接传感输入、输出动作和反馈机制
-> 形成实时闭环信息环境
-> 是否产生可重复、任务相关、非随机的活动变化
-> 这些变化属于反射、学习、主动推断、代理性前体还是更高层级认知
-> 如何建立证据、术语和伦理边界
```

## 概念谱系

| 概念 | 工作定义 | Human Infra 位置 |
| --- | --- | --- |
| SBI | 将体外生物神经材料与数字硬件、软件和反馈系统整合，用于目标导向或其他形式的信息处理行为 | 外部认知基础设施和活体计算平台 |
| OI | 以脑类器官为核心的生物计算和 intelligence-in-a-dish 路线 | 学习、记忆和类脑组织机制模型 |
| BI | 通过工程方式构建神经回路，不必严格追求生理真实性 | 可控、可设计的生物信息处理网络 |
| learning | 操作性表现随时间改善或网络状态因反馈而改变 | 可测量但不可直接外推为认知主体 |
| sentience | 对感觉印象作出反应并通过内部过程适应的操作定义 | 道德风险讨论入口，不等同现象意识 |
| agency | 系统转换输入的规则可随过去活动改变的必要条件候选 | 代理性前体，不是充分条件 |
| consciousness | 主观体验或现象意识 | 当前资料不提供稳健测量或证明 |

## 技术基础

### Wetware

Wetware 包括动物原代神经元、人源 iPSC 神经元、NGN2 诱导神经元、海马 DG/CA3/CA1 亚区神经元、脑类器官和脑微生理系统。核心变量包括细胞来源、成熟度、兴奋/抑制平衡、胶质比例、长期稳定性、区域特异性和批次差异。

### Hardware

Hardware 包括高密度多电极阵列、刺激/记录接口、微流控灌流、温控、培养基管理、无菌系统、生命支持和长期运行监测。对于 SBI/OI，接口时延、同步、刺激语义和实验可复现性是核心问题。

### Software

Software 定义神经组织所处的信息景观：把神经输出转化为环境动作，再把动作后果以结构化方式反馈给神经网络。闭环软件不是附属脚本，而是决定“系统在什么世界里行动”的实验条件。

## 核心证据

### DishBrain 与闭环学习

Kagan 等 2022 年 Neuron 论文将人源 hiPSC 神经元和鼠源皮层神经元接入高密度多电极阵列，并嵌入简化 Pong 环境。闭环反馈条件下的网络在数分钟内出现任务表现改善，而缺少反馈的刺激控制组未出现同等学习趋势。

边界：这支持“简化闭环任务中的适应”，不支持“通用智能”或“现象意识”。

### 样本效率

Khajehnejad 等研究将生物神经网络与 DQN、A2C、PPO 等深度强化学习算法放入同一简化任务中比较。结果提示，在低样本、实时反馈、稀疏输入的条件下，体外神经系统可能具有值得研究的样本效率优势。

边界：该结论依赖任务、指标、时间尺度和平台；需要更多任务族、独立实验室和跨平台复现。

### 近临界动力学

Habibollahi 等 2023 年 Nature Communications 论文显示，结构化任务信息可使网络更接近临界动力学，任务表现与接近临界性的程度相关。

边界：临界性不能单独证明学习、意识或道德状态；缺少反馈时，不应把临界性解释成任务学习。

### 药物功能读数

Watmuff 等 2025 年 Communications Biology 论文将 DishBrain 范式用于神经微生理系统药物评估。药物可以改变自发放电和 gameplay 指标，提示闭环信息处理指标可能提供传统自发活动指标之外的功能维度。

边界：闭环任务指标是否能预测疾病机制或临床药效仍未充分证明。

### 类器官学习记忆构件

OI 文献显示，脑类器官可能表达学习和记忆相关的分子、突触和网络动力学基础，包括功能连接、突触可塑性指标、即时早期基因反应和刺激后增强。

边界：这支持“基础构件存在”，不等于类器官已经表现任务层面学习或主体性。

## 理论解释

主动推断和自由能原理为闭环神经文化提供一种解释语言：系统可能通过行动和内部状态更新来改善对环境后果的预测。该语言可帮助区分 reactive、sentient 和 intentional behavior，但不能自动把任何闭环适应上升为意图或意识。

信息处理层级文献提出 Class I/II/III 框架：Class I 是无记忆反应系统，Class II 有内部状态但规则固定，Class III 的输入转换规则会随过去活动改变。Class III 可作为 agency 的必要但不充分条件。

## 应用前景

- 基础神经科学：研究学习、可塑性、功能连接、临界动力学和主动推断。
- 疾病建模与药物筛选：用闭环任务表现补充传统自发活动或标志物读数。
- 生物计算与 NeuroAI：研究低样本、低能耗、持续学习和神经启发算法。
- 平台化实验服务：通过 CL1、CL API 和共享接口提高可重复性。
- 伦理研究平台：使用复杂度递进的系统迭代测试道德相关状态候选指标。

## 伦理与治理

```text
人源神经材料
-> 捐赠者同意、数据权益和商业化边界
-> 闭环环境中出现学习/适应信号
-> 术语解释和公众叙事风险上升
-> 需要嵌入式伦理、术语治理和中止条件
```

治理重点：

- 区分 sentience 与 consciousness。
- 区分 learning 指标与 moral status。
- 区分平台能力与成熟工程产品。
- 区分神经组织实验系统与主体连续性载体。
- 对人源细胞、数据、商业化、专利和实验退出条件保持审计。

## 研究缺口

1. 任务生态过窄，核心证据仍集中在简化 Pong 或类似任务。
2. 复现性不足，关键研究需要独立实验室和多平台验证。
3. 指标体系未稳定，learning、sample efficiency、criticality、agency 和 moral state 需要分层定义。
4. wetware 标准化不足，细胞来源、成熟度、胶质比例和三维结构影响可比性。
5. hardware/software 接口需要开放化，时延、同步、刺激语义和数据记录决定复现质量。
6. 伦理治理需要前置嵌入，而不是争议出现后再补。

## 文献矩阵

| 编号 | 文献 | 类型/状态 | 位置 | 关键贡献 |
| ---: | --- | --- | --- | --- |
| 1 | Hogan et al., CL API, 2026 | arXiv preprint | 平台与软件 | 实时闭环 API、刺激语义、同步和复现接口 |
| 2 | Abu-Bonsrah et al., hippocampal neuronal sub-populations, 2026 | bioRxiv preprint | wetware | 生成 DG/CA3/CA1 和区域特异性胶质细胞 |
| 3 | Kagan et al., Information-Processing Hierarchy and Agency, 2026 | arXiv preprint | 理论与伦理 | Class I/II/III 信息处理阶序 |
| 4 | Patel et al., NeuroAI and SBI, 2025 | arXiv review | 总体框架 | 用 wetware/hardware/software 组织 SBI |
| 5 | Kagan and Kitchen, AI progress and synthetic biology, 2025 | 缺全文 | 背景/待补 | AI 与生物智能机制关系 |
| 6 | Kagan, Two roads diverged, 2025 | Perspective | 概念谱系 | 区分 OI 与 BI 路线 |
| 7 | Khajehnejad et al., Dynamic Network Plasticity and Sample Efficiency, 2025 | peer-reviewed | 样本效率 | BNN 与深度 RL 比较 |
| 8 | Kagan, CL1 platform technology, 2025 | 缺全文 | 平台/待补 | CL1 平台方向 |
| 9 | Kagan et al., In vitro neurons learn, 2022 | Neuron | 核心实证 | DishBrain 闭环反馈任务表现改善 |
| 10 | Habibollahi et al., Critical dynamics, 2023 | Nature Communications | 网络动力学 | 结构化输入与近临界动力学 |
| 11 | Watmuff et al., Drug treatment alters performance, 2025 | Communications Biology | 应用 | 药物改变闭环信息处理表现 |
| 12 | Kagan et al., Harnessing Intelligence from Brain Cells In Vitro, 2025 | Review | 技术基础 | wetware/hardware/software 集成 |
| 13 | Smirnova et al., Organoid intelligence, 2023 | Lead article | OI 框架 | OI 行动计划、微流控、3D MEA、嵌入式伦理 |
| 14 | Kagan et al., Technology opportunities and challenges of SBI, 2023 | Review | SBI 框架 | SBI 技术路径、应用和伦理 |
| 15 | Khajehnejad et al., Biological Neurons Compete with Deep RL, 2024 | arXiv preprint | 版本追踪 | 样本效率预印本，不与 7 重复计权 |
| 16 | Kagan et al., Nomenclature consensus, 2024 | Perspective | 术语治理 | diverse intelligent systems 术语共识 |
| 17 | Tanveer et al., Starting an SBI lab, 2025 | Methods/practice | 实验建设 | SBI/OI 实验室跨学科组件 |
| 18 | Kagan et al., Embodied Neural Systems and Morally Relevant States, 2024 | Commentary | 伦理 | 用复杂度递进系统测试道德相关状态 |
| 19 | Alam El Din et al., Human Neural Organoid MPS, 2024 | bioRxiv preprint | OI 实证 | 学习记忆构件和突触可塑性指标 |
| 20 | Kagan et al., Neurons Embodied in a Virtual World, 2022 | Commentary | 伦理 | 区分 sentience 与 consciousness |
| 21 | Friston et al., Active Inference and Intentional Behavior, 2025 | Theory | 理论解释 | 区分 reactive、sentient、intentional behavior |
| 22 | Barros et al., Intersection between biological and digital, 2025 | Editorial | 领域定位 | SBI/OI 生物-数字交叉定位 |

## 待补材料

- 补齐 Springer 章节全文，避免只凭题录进入核心论证。
- 补齐 Nature Reviews Bioengineering CL1 文章全文。
- 判断样本效率预印本与正式论文的重叠，正式写作优先引用同行评议版本。
- 对预印本添加状态标记，避免与同行评议论文同等权重。
- 补充外部对照文献：传统 MEA 闭环刺激、脑类器官伦理、active inference、neuromorphic computing、deep RL sample efficiency 基准。
