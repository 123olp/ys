# Derivation Package

## Target

推导“可控度规等待室假设”的最小净主体持续性增益表达式。目标不是证明等待室可工程实现，而是把传播性命题拆成可审查变量：度规导致的固有时差分、生命周期闭合、外部技术采用、主体连续性、风险扣减和递归升级条件。

## Status

COHERENT AFTER REFRAMING / EXTRA ASSUMPTION

原始叙事“制造黑洞或类黑洞等待室即可等待技术革命”过强。经重构后，正确对象不是黑洞，而是“可控度规等待室”：一个在主体世界线和外部技术参考系之间产生可用固有时差分，并且具备进入、停留、退出、采用和连续性闭环的假设系统。

## Invariant Object

顶层不变量是净主体持续性增益：

```text
NCG = net continuity gain
```

它不是寿命预测值，也不是物理可行性证明，而是一个排序和反证用的研究对象。所有收益项和风险项都必须回到 NCG，不允许用等待倍率 K 单独替代路径价值。

## Assumptions

- A1: 存在候选等待区 W，并且 W 的边界、进入条件和退出条件可被定义。
- A2: 主体路径可表示为等待前、等待中、退出后的一条连续世界线或可审查的连续性链。
- A3: 存在外部技术参考系 E，用于比较外部技术系统经历的时间。
- A4: 主体固有时 Delta_tau_subject 和外部参考时间 Delta_t_external 都可定义。
- A5: 等待倍率 K 有限且可比较，不把坐标奇点、无限红移或无限未来写成收益。
- A6: 外部技术升级 G_external 能被主体接触、理解、获得和采用。
- A7: 生命风险、工程风险、尾部风险和机会成本可作为扣减项进入模型。
- A8: 至少存在一个比较路径，如人体冷冻、休眠、相对论飞船或 AI 医学等待。

## Notation

- W: 候选可控度规等待区。
- gamma: 主体世界线。
- g_mu_nu: 时空度规。
- Delta_tau_subject: 主体在一轮等待中经历的固有时。
- Delta_t_external: 外部技术参考系经历的比较时间。
- K: 未来等待倍率，K = Delta_t_external / Delta_tau_subject。
- P_enter: 主体成功进入等待区的概率。
- P_stay: 主体在等待区内维持生命和系统功能的概率。
- P_exit: 主体成功退出或被回收的概率。
- P_adopt: 主体成功采用外部升级技术的概率。
- P_cont: 主体连续性保持概率。
- U_upgrade: 外部技术升级对主体持续性的效用代理。
- R_life: 生命风险。
- R_engineering: 工程风险。
- R_tail: 尾部风险。
- C_wait: 机会成本。
- X_n: 第 n 轮等待前的主体状态。
- G_n: 第 n 轮外部技术状态。

## Derivation Strategy

采用“物理时间接口 -> 生命周期访问概率 -> 等待收益代理 -> 风险扣减 -> 递归状态转移”的路线。

这个路线把精确物理定义和解释性模型分开。固有时公式是广义相对论语言中的定义；P_access、B_wait 和 NCG 是 Human Infra 用于比较候选路径的启发式模型，不是物理定理。

## Derivation Map

1. E1 用度规和世界线定义主体固有时。
2. E2 用外部参考时间和主体固有时定义等待倍率 K。
3. E3 把进入、停留、退出、采用和连续性合成访问概率 P_access。
4. E4 把 K 和外部升级效用合成等待收益代理 B_wait。
5. E5 把生命、工程、尾部和机会成本合成风险扣减 R_total。
6. E6 定义 NCG = B_wait * P_access - R_total。
7. E7 把一轮等待写成主体状态转移。
8. E8 给出递归等待飞轮的必要条件。

## Main Derivation

Step 1. 固有时定义。

```text
Delta_tau_subject = integral_gamma sqrt(-g_mu_nu dx_mu dx_nu) / c
```

这是定义层。它说明主体经历的时间沿自身世界线积累，而不是由远方日历时间直接给出。

Step 2. 等待倍率定义。

```text
K = Delta_t_external / Delta_tau_subject
```

这是定义层。K 表示外部技术参考系经历的时间相对主体固有时的倍率。K 较大只说明等待时间差分更大。

Step 3. 生命周期访问概率近似。

```text
P_access = P_enter * P_stay * P_exit * P_adopt * P_cont
```

这是近似层。它把多个必要环节合成一个访问概率。真实系统中这些项可能相关，不能默认独立；乘积形式只用于揭示任一必要项接近 0 时总访问概率也会塌缩。

Step 4. 等待收益代理。

```text
B_wait = K * U_upgrade(Delta_t_external)
```

这是解释层。它表示等待倍率只有在外部技术产生可用升级时才形成候选收益。U_upgrade 不等于技术进步总量，而是主体可采用的持续性增益代理。

Step 5. 风险扣减。

```text
R_total = R_life + R_engineering + R_tail + C_wait
```

这是近似层。它把生命风险、工程风险、尾部风险和机会成本放入同一扣减项。不同版本可以使用加权和、非线性惩罚或约束门禁，但不能删除这些扣减对象。

Step 6. 净主体持续性增益。

```text
NCG = B_wait * P_access - R_total
```

这是定义层。NCG 用于排序候选路径和暴露反证条件，不用于输出个体寿命、个体死亡日期或工程可行性承诺。

Step 7. 一轮等待的状态转移。

```text
X_next = Adopt(Exit(Wait(X_current, W)), G_external)
```

这是解释层。它表明等待室不是静态设施，而是一个跨越等待、退出和技术采用的状态转移。

Step 8. 递归增强条件。

```text
Recursive gain requires:
  NCG_n > 0
  X_next improves feasible future waiting
```

这是命题层。只有新状态 X_next 提高下一轮等待的安全、修复、采用、资源或治理条件时，才构成加速回报飞轮。

## Remarks and Interpretation

- K 是必要但不充分变量。高 K 可以被 P_exit、P_adopt、P_cont 或风险项完全抵消。
- 黑洞不是模型不变量。模型不变量是由度规和世界线定义的固有时差分，以及它能否进入主体持续性闭环。
- 递归等待不是“永生证明”。它只是说，如果每轮等待能扩大下一轮可行性，才可能进入复利结构。
- Human Infra 的关键转译是：等待未来本身不是价值，能在未来继续行动、学习、修复和选择才是价值。

## Boundaries and Non-Claims

- 不证明人工黑洞、类黑洞结构或重力控制已经可行。
- 不输出个体寿命、个体死亡日期或医疗建议。
- 不把黑洞科普资料当作工程证据。
- 不把 Malament-Hogarth 时空写成现实宇宙中的部署方案。
- 不把“外部技术会进步”写成必然事实。
- 不把复制体、数字备份或记忆记录自动等同为同一主体连续性。

## Open Risks

- 缺少具体可控度规方案时，W 仍是抽象占位符。
- P_access 的乘积形式忽略变量相关性，后续定量模型需要改成因果图或状态转移模型。
- U_upgrade 需要从医学、AI、材料、能源、认知增强和治理能力中拆分估计。
- R_tail 可能不是可线性扣减变量，而是硬约束门禁。
- 比较路径尚未统一量纲，等待室、冷冻、休眠、相对论飞船和 AI 医学需要共同 NCG 规范。
