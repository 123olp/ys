# 脑-身接口协议变量契约

## 定位

本契约服务于 `disembodied-cns` 域下的“身体功效替代 - 脑身接口协议 - 最小充分身体”框架。

它不定义任何生命支持、神经接口、灌注、刺激、植入或人体实验操作步骤。它只回答一个建模问题：

```text
如果不复制原生器官形态
  -> 需要先识别脑与身体之间交换了哪些变量
  -> 再定义这些交换变量的方向、频率、精度、误差和闭环要求
  -> 最后判断替代实现是否可能在边界内产生接口等价
```

机器可审计账本位于 [`brain-body-interface-protocol-register.json`](brain-body-interface-protocol-register.json)。本契约定义字段和边界；JSON register 保存当前协议记录、状态、证据锚点和禁止外推范围。稳定主张到证据、协议行、变量、反证和降级动作的绑定位于 [`minimal-sufficient-body-claim-evidence-matrix.json`](minimal-sufficient-body-claim-evidence-matrix.json)。

## 判定原则

本契约把“接口因果等价”设为进入本域研究的第一判据：

```text
原生器官 / 身体结构
  -> 通过脑-身接口产生特定因果作用
  -> 因果作用拆成交换内容、方向、载体、频率、延迟、精度、误差、闭环角色和主体状态依赖
  -> 候选替代实现必须逐项说明能否产生同等输入、接收同等输出并维持同等反馈效果
  -> 任一关键字段缺失、误差边界未知或主体连续性依赖不可审查
  -> 只能标记为 blocked 或 cannot-evaluate，不能进入等价或收益叙事
```

压缩成工程判据就是：

```text
器官形态相似 != 接口等价
局部功能相似 != 主体连续性
接口等价 = 同等输入 + 同等输出 + 同等闭环效果 + 明确误差边界 + 可中止治理
```

因此，协议记录先描述交换变量，再描述候选实现；先描述可观测代理和中止门槛，再讨论设备、器官、算法或神经接口。器官名称、设备外形和功能类比都不能单独构成等价证据。

### 对象优先级

本契约采用以下对象优先级，防止研究叙事退回“器官复制”：

```text
P0：主体连续性条件
  -> 同一主体是否仍能存在、感知、调节、表达、行动、学习、选择和退出

P1：脑-身接口协议
  -> 哪些交换内容、方向、载体、频率、延迟、精度、误差边界和闭环角色支撑 P0

P2：协议实现
  -> 原生器官、生物替代、机械装置、传感器、执行器、控制器或神经接口如何实现 P1

P3：器官 / 设备形态
  -> 形态、材料、尺寸、外观、位置和制造路线只作为实现细节记录
```

任何研究条目若只能说明 P3 相似，不能说明 P1 接口协议和 P0 主体连续性依赖，就只能保留为来源信号或概念草案，不能写成接口等价、身体功效替代、工程可行或主体收益主张。

### 接口等价字段门槛

`接口等价` 不是“功能相似”的同义词。候选实现必须先回答一组字段级问题，才允许进入协议寄存器或 Claim-Evidence Matrix。

| 门槛 | 必须回答的问题 | 未回答时的处理 |
| --- | --- | --- |
| 交换内容 | 这条通道交换的是血流、氧气、营养、废物、激素、免疫信号、内感受、外感受还是运动指令？ | 降级为形态类比 |
| 交换方向 | 信号是 body-to-brain、brain-to-body、bidirectional 还是 environment-mediated？ | 不能判断闭环 |
| 时间约束 | 交换是连续、周期、事件触发、低延迟还是多时间尺度？ | 不能判断控制稳定性 |
| 精度要求 | 需要多高浓度、压力、分辨率、编码保真度、噪声控制或分类准确性？ | 不能判断协议等价 |
| 误差边界 | 偏差达到何种程度会造成稳态崩坏、情绪失调、自我感破裂、行动失败或主体连续性中止？ | 不能进入收益叙事 |
| 闭环角色 | 该通道参与预测、调节、误差修正、行动准备、降级或恢复中的哪一环？ | 只能保留为单点功能信号 |
| 主体状态依赖 | 该通道依赖或影响意识、情绪、自我感、表达、行动、学习、选择或退出中的哪些状态？ | 不能进入主体连续性主张 |

因此，任何条目若只写“替代心脏”“替代肺”“替代肝肾”“替代四肢”或“替代身体”，但没有写清这些字段，只能进入 Source Signals；不能进入 `candidate-equivalence`，也不能被用于模型桥接、价值链路或传播材料。

## 协议对象

`brain_body_interface_protocol` 是单条脑-身交换通道的研究记录。每条记录只描述一个交换通道，不把多个系统混成一个大结论。

本契约采用“接口因果作用优先”的判定顺序：

```text
先问原生器官通过接口对脑产生了什么因果作用
  -> 再问这些作用由哪些交换内容、方向、频率、精度和误差边界构成
  -> 再问候选替代实现是否能产生同等输入、接收同等输出并维持同等闭环效果
  -> 最后才讨论它使用的是生物器官、机械装置、计算控制系统、神经接口还是外部执行器
```

因此，协议记录不得把“名称相似”“器官形态相似”或“设备功能相似”直接当作等价证据；必须落到交换变量、主体状态依赖、闭环作用和中止门槛。

示例通道：

- `perfusion_flow`：血流、灌注压和微循环。
- `oxygen_glucose_supply`：氧气、葡萄糖和能量底物。
- `metabolic_clearance`：二氧化碳、乳酸、尿素、酸碱和电解质。
- `endocrine_signal`：激素、压力轴、血糖调节和节律信号。
- `immune_inflammatory_signal`：免疫、炎症、损伤和感染信号。
- `interoceptive_feedback`：心跳、呼吸、饥饿、疼痛、疲劳、温度和内脏状态。
- `exteroceptive_input`：视觉、听觉、触觉、前庭和本体感觉。
- `motor_expression_output`：语言、眼动、动作意图、神经输出和执行器控制。
- `rights_identity_control`：同意、撤回、表达、代理决策和法律身份通道。

## 最小字段

| 字段 | 含义 | 缺失后果 |
| --- | --- | --- |
| `protocol_id` | 通道唯一标识 | 不能索引 |
| `channel_family` | 通道族：灌注、能量、清除、内分泌、免疫、内感受、外感受、运动表达、权利控制 | 不能归类 |
| `exchange_content` | 交换内容：具体变量、物质、信号或指令 | 不能定义接口 |
| `direction` | 交换方向：body-to-brain、brain-to-body、bidirectional、environment-mediated | 不能判断闭环 |
| `carrier` | 承载方式：血流、神经、体液、机械、数字、视觉、听觉、触觉等 | 不能比较替代实现 |
| `unit_or_scale` | 单位、量表或可观测代理 | 不能进入定量或半定量模型 |
| `frequency_or_cadence` | 频率、节律、采样周期或更新 cadence | 不能评估时间等价 |
| `latency_bound` | 最大延迟或响应时间边界 | 不能评估控制稳定性 |
| `precision_requirement` | 分辨率、噪声、保真度或分类准确性要求 | 不能评估精度等价 |
| `error_tolerance` | 允许误差与失效阈值 | 不能设定 abort gate |
| `closed_loop_role` | 该通道在反馈调节中的角色 | 不能判断接口等价 |
| `subject_state_dependency` | 依赖哪些主体状态：意识、情绪、自我感、行动、记忆、表达等 | 不能连接主体连续性 |
| `observable_proxy` | 当前可观测代理指标 | 不能做证据卡 |
| `replacement_candidate` | 候选替代实现类型 | 不能比较路径 |
| `failure_modes` | 失效模式 | 不能做风险建模 |
| `abort_gate` | 必须中止、降级或判定不可评估的条件 | 不能进入治理模型 |
| `evidence_anchor` | 来源、Source Card 或文献包锚点 | 不能成为稳定主张 |
| `scope_boundary` | 该记录不能推出什么 | 防止外推失控 |

## 状态枚举

`equivalence_status` 只能使用以下值：

| 状态 | 含义 |
| --- | --- |
| `not-specified` | 尚未定义交换字段 |
| `observed-natural-channel` | 只描述自然身体通道 |
| `partial-proxy-known` | 有部分可观测代理，但无法完整定义协议 |
| `candidate-equivalence` | 有候选替代实现，但只允许作为概念或低阶模型候选 |
| `blocked` | 缺少关键字段、风险不可接受或违反主体连续性边界 |
| `cannot-evaluate` | 信息不足，不能判断 |

禁止使用 `achieved`、`proven`、`safe`、`operational` 等会暗示现实可行的状态。

## 最小记录模板

```yaml
protocol_id:
channel_family:
exchange_content:
direction:
carrier:
unit_or_scale:
frequency_or_cadence:
latency_bound:
precision_requirement:
error_tolerance:
closed_loop_role:
subject_state_dependency:
observable_proxy:
replacement_candidate:
failure_modes:
abort_gate:
evidence_anchor:
scope_boundary:
equivalence_status: not-specified
```

## 示例：灌注通道

```yaml
protocol_id: perfusion_flow
channel_family: perfusion
exchange_content: blood flow, perfusion pressure, oxygen delivery support
direction: body-to-brain
carrier: vascular flow
unit_or_scale: pressure/flow/oxygenation proxies
frequency_or_cadence: continuous
latency_bound: low-latency continuous support required
precision_requirement: bounded physiological stability, not currently specified for disembodied subject continuity
error_tolerance: loss of perfusion or severe instability is an abort gate
closed_loop_role: substrate maintenance for neural tissue and downstream cognition
subject_state_dependency: consciousness, cognition, memory continuity, expression
observable_proxy: perfusion stability, oxygenation, tissue integrity, metabolic markers
replacement_candidate: extracorporeal circulation, artificial heart, perfusion system
failure_modes: ischemia, hemorrhage, thrombosis, infection, edema, device failure
abort_gate: cannot claim subject continuity from tissue viability alone
evidence_anchor: MSB-CARD-001, MSB-CARD-012, MSB-CARD-014
scope_boundary: supports substrate-maintenance modeling only; not revival or personal survival
equivalence_status: candidate-equivalence
```

## 示例：内感受通道

```yaml
protocol_id: interoceptive_feedback
channel_family: interoception
exchange_content: heartbeat, respiration, pain, fatigue, hunger, temperature and visceral state signals
direction: body-to-brain
carrier: neural and humoral signaling
unit_or_scale: subjective reports, neural proxies, physiological signals
frequency_or_cadence: multi-timescale
latency_bound: task- and state-dependent
precision_requirement: sufficient to preserve emotion, self-regulation and action readiness
error_tolerance: unresolved; severe distortion is a subject-continuity risk
closed_loop_role: emotion, self-model, motivation, risk perception and regulation
subject_state_dependency: emotion, motivation, selfhood, decision quality
observable_proxy: interoceptive accuracy, affective stability, physiological regulation proxies
replacement_candidate: artificial interoceptive feedback, neurofeedback, embodied simulator
failure_modes: signal loss, false body state, affective instability, dissociation, impaired agency
abort_gate: cannot treat oxygenated brain maintenance as sufficient if interoceptive feedback collapses
evidence_anchor: MSB-CARD-002, MSB-CARD-013
scope_boundary: conceptual and variable-modeling support only; no engineering claim
equivalence_status: partial-proxy-known
```

## 接入规则

- Source Signals 只记录候选来源；不能直接提升 `equivalence_status`。
- Source Cards 必须至少填 `exchange_content`、`direction`、`subject_state_dependency`、`scope_boundary`。
- Claim-Evidence Matrix 只能登记有明确 `evidence_anchor`、`protocol_ids`、`falsifier`、`downgrade_action` 和 `scope_boundary` 的通道或主张。
- Domain-to-Model Bridge 只能使用 `candidate-equivalence`、`blocked` 或 `cannot-evaluate` 的保守语言。
- 任一通道缺少 `error_tolerance`、`failure_modes` 或 `abort_gate` 时，不得进入定量收益计算。
- 修改协议字段、状态枚举、证据锚点或禁止外推范围后，必须运行 `python3 tools/audit_human_infra_brain_body_interface_protocol_register.py`。
- 修改本域主张、证据角色、Source Card 锚点、协议行锚点、反证或降级动作后，必须运行 `python3 tools/audit_human_infra_minimal_sufficient_body_claim_evidence_matrix.py`。

## 禁止外推

- 不从局部设备成功推出全身替代可行。
- 不从细胞活性、组织完整性或器官信号推出主体仍存在。
- 不从 BCI 输入输出推出人格、意志或身体替代已经可实现。
- 不从接口等价概念推出任何人体操作路线。
- 不把本契约用于个体医疗判断、工程实施、投资宣传或风险规避。
