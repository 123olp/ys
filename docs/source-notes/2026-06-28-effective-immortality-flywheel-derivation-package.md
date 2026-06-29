# Effective Immortality Flywheel Derivation Package

## Target

把“有效永生带来的主体持续性加速回报飞轮”整理成可进入论文和 Web 模型的公式主线。本产物不承担永生可行性证明；它给出一套可审查的动态决策框架：技术或干预如何通过状态转移、风险函数、有效时间、行动质量和可能性空间影响主体持续性。

## Status

COHERENT AFTER REFRAMING

当前链路在原始表述中容易被误读为“寿命越长自然越强”。重构后的对象是“折现主体持续性价值”，寿命长度只作为外层边界之一。该重构让模型可以同时纳入健康质量、学习轮次、技术采用、行动质量、可能性空间、风险和伦理约束。

## Invariant Object

折现主体持续性价值：

```text
V_pi = E[sum_t delta^t * (E_t + alpha Q_t + beta O_t - gamma Risk_t)]
```

其中 `pi` 是策略，`delta` 是折现因子，`E_t` 是有效时间，`Q_t` 是单位时间行动质量，`O_t` 是真实可能性空间，`Risk_t` 是副作用、依赖、误用、监控、剥削和尾部风险扣减。

该对象比单一寿命长度更稳定，因为 Human Infra 关心的是主体能否持续存在、行动、学习、恢复和进入未来。

## Assumptions

- 时间是离散的，`t` 可按年、季度、月或项目周期设定。
- 主体状态可以先用低维代理 `X_t=(T_t,E_t,R_t,C_t,A_t,Q_t,O_t,Risk_t)` 表达。
- `T` 表示主体持续时间，`E` 表示有效时间，`R` 表示学习/修正轮次，`C` 表示积累资本，`A` 表示技术采用能力，`Q` 表示单位时间行动质量，`O` 表示可能性空间。
- 行动与干预向量写作 `U_t=(medical,AI,wearable,knowledge_system,automation,resource_environment)`，避免和变量 `A` 冲突。
- 技术或干预只通过 `P(X_{t+1}|X_t,U_t)` 或 `lambda(t|X_t,U_t)` 进入模型。
- 所有因果主张必须声明 population、intervention、comparator、time zero、outcome、estimand 和识别假设。
- 模型只用于研究展示、变量解释和群体级路径位移，不输出个体死亡日期。

## Notation

| 符号 | 含义 | 类型 |
| --- | --- | --- |
| `X_t` | 主体在时间 `t` 的状态向量 | state |
| `U_t` | 主体在时间 `t` 接受或采取的行动/干预向量 | action |
| `T_t` | 主体持续时间或生存窗口 | survival/time |
| `E_t` | 有效时间 | quality-adjusted agency time |
| `R_t` | 学习、试错、复盘和修正轮次 | process count |
| `C_t` | 经验、能力、资源、信誉和协作网络存量 | stock |
| `A_t` | 技术采用能力 | adoption capacity |
| `Q_t` | 单位时间行动质量 | performance rate |
| `O_t` | 真实可进入的可能性空间 | feasible option set |
| `Risk_t` | 负向通道和尾部风险 | risk term |
| `lambda(t|X_t,U_t)` | 给定状态和干预下的死亡、失能或主体失效风险 | hazard |
| `S(t)` | 生存函数，`P(T>t)` | survival function |

## Derivation Strategy

推导路线采用“全局对象 -> 低维状态代理 -> 行动算子 -> 目标函数 -> 解释边界”：

1. 先选定全局对象 `V_pi`，防止单一寿命长度替代主体持续性价值。
2. 用 `T/E/R/C/A/Q/O/Risk` 建立低维状态代理。
3. 用 `U_t` 表示医学、AI、检测、知识系统、自动化和资源环境等行动/干预。
4. 把每个技术族放入状态转移算子或风险算子。
5. 用约束项阻止模型越界为个人死亡预测、医疗建议或无证据因果主张。

## Derivation Map

1. `V_pi` 依赖 `E_t`、`Q_t`、`O_t` 和 `Risk_t`，对应有效时间、行动质量、未来选择权和负向通道。
2. `E_t` 由 `T_t`、健康质量、认知功能、恢复能力和主体性共同决定。
3. `R_t` 由 `E_t` 和学习率决定，只有带目标、反馈和修正的时间才进入轮次。
4. `C_{t+1}` 由上一期 `C_t`、轮次收益和衰减项共同决定。
5. `A_t` 由积累资本、数字素养、资源可及性和技术访问条件共同决定。
6. `Q_t` 由基础行动质量、技术收益、质量控制成本和摩擦项共同决定。
7. `O_{t+1}` 由行动质量、积累资本、协作网络和进入门槛共同决定。
8. `T_{t+1}` 与 `E_{t+1}` 通过资源、照护、恢复、风险治理和风险函数反向受到 `O_t` 影响。

## Main Derivation

Step 1. 定义低维状态代理。

```text
X_t = (T_t,E_t,R_t,C_t,A_t,Q_t,O_t,Risk_t)
```

这是近似，不是完整人体、心理、社会和技术系统。

Step 2. 定义行动/干预向量。

```text
U_t = (medical,AI,wearable,knowledge_system,automation,resource_environment)
```

`U_t` 中的元素不直接写成“加寿命”。它们必须说明影响的变量、机制和证据门。

Step 3. 定义技术进入模型的位置。

```text
P(X_{t+1}|X_t,U_t)
lambda(t|X_t,U_t)
```

第一项表示状态转移，第二项表示风险函数。医学干预可能主要进入两者；AI 工具常进入观测、策略和行动质量；可穿戴主要进入观测；资源环境可进入恢复、照护和可能性空间。

Step 4. 建立玩具状态更新。

```text
E_t = T_t * health_quality_t * agency_t
R_t = learning_rate_t * E_t
C_{t+1} = C_t + accumulation_efficiency_t * R_t - decay_t
A_t = adoption_capacity(C_t, literacy_t, resources_t, access_t)
Q_t = base_action_quality_t + technology_gain_t * A_t - friction_t
O_{t+1} = O_t + option_gain(Q_t, C_t, network_t) - option_loss_t
T_{t+1} = T_t + continuity_gain(O_t, health_t, recovery_t, risk_control_t) - hazard_pressure_t
```

这些公式是机制近似，用于表达变量位置和方向，不承担实证估计。

Step 5. 写出受约束目标函数。

```text
maximize_pi E[sum_t delta^t * (E_t + alpha Q_t + beta O_t - gamma Risk_t)]

subject to:
  identity_continuity >= threshold
  evidence_gate(U_t) == pass
  consent_and_rights == protected
  no_personal_death_date_output == true
  causal_claim_requires_population_comparator_time_zero_outcome_estimand == true
```

该目标函数把有效永生放入动态策略问题：选择什么样的医学、AI、检测、知识系统、自动化和资源环境策略，能够在约束下提高主体持续性价值。

## Remarks and Interpretation

- `T` 是边界变量，`E` 是桥梁变量。寿命窗口必须转化为有效时间，才可能进入学习和行动。
- `R` 和 `C` 区分“时间变多”和“能力变强”。没有反馈和迁移，轮次不会稳定沉淀为资本。
- `A` 是主体能力变量，不是技术清单。技术存在、技术可及、技术可靠采用是三件事。
- `Q` 负责处理单位时间行动质量，必须同时统计质量控制成本、返工、幻觉、过度依赖和任务边界。
- `O` 必须是真实可进入路径集合。抽象机会、宣传愿景和不可访问资源不能直接计入。
- `Risk` 是模型内生项。任何增强技术都要写正向通道、负向通道、停止条件和回滚条件。

## Boundaries and Non-Claims

- 本推导不证明永生已经实现。
- 本推导不预测任何个人死亡日期。
- 本推导不替代医学、法律、伦理或政策判断。
- 本推导不把机制合理、观察相关或短期任务收益升级成寿命延长结论。
- 本推导不把数字副本、记忆外化或工具增强自动视为同一主体的延续。
- 本推导不保证正反馈成立；健康断点、学习断点、资源断点、技术断点和治理断点都可能让飞轮停滞或反转。

## Open Risks

- 权重 `alpha`、`beta`、`gamma` 不是自然常数，需要公开价值假设和敏感性分析。
- `E_t`、`Q_t`、`O_t` 的代理指标可能跨人群、地区和制度环境失真。
- `O -> T/E` 的反哺路径目前证据较分散，需要拆成医疗可及、恢复资源、社会支持、资源冗余和风险治理。
- AI 工具对 `Q` 的证据主要来自限定任务，不能外推到所有问题求解。
- 医学干预必须经过临床证据、长期安全性、适应证和可及性审查。
- 模型如果缺少反证指标和停止条件，容易退化成技术乐观主义叙事。

## Maintenance

- Related data: [`web/src/data/effective-immortality-evidence.json`](../../web/src/data/effective-immortality-evidence.json)
- Related paper: [Effective Immortality Acceleration Flywheel](../explanations/effective-immortality-acceleration-flywheel.md)
- Related matrix: [Evidence Matrix v1.3](2026-06-28-effective-immortality-flywheel-evidence-matrix.md)
- Review trigger: 变量字典、目标函数、行动向量、因果协议或 Web 图表模型发生变化时同步复审。
