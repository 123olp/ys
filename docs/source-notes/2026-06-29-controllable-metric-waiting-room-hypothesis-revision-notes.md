# 可控度规等待室假设论文页收口记录

日期：2026-06-29

## 目标

把“通过控制重力、制造黑洞或类黑洞等待室来等待技术革命”的原始设想，压缩为一个可审查的 Human Infra working paper 对象：可控度规等待室假设。

本轮不证明人工黑洞、类黑洞结构、重力控制或人体强引力等待已经可行。它只建立研究对象、变量、状态机、公式边界、场景比较、引用语境和本地审计门禁。

## 核心重构

原始叙事过强：

```text
制造黑洞或类黑洞等待室
  -> 产生时间差
  -> 等待技术革命
  -> 出来使用新技术
  -> 再等待
```

收口后的研究对象是：

```text
可控度规等待室
  -> 主体世界线和外部技术参考系之间产生固有时差分
  -> 主体以较少固有时等待外部技术系统发展
  -> 主体必须可进入、可停留、可通信、可退出、可回收
  -> 外部技术必须可接触、可理解、可获得、可采用
  -> 等待收益必须扣除生命风险、工程风险、尾部风险和机会成本
  -> 只有净主体持续性增益为正，才进入下一轮递归等待
```

## 理论命名

正式页面标题采用：

```text
Controllable Metric Waiting Room Hypothesis
可控度规等待室假设
```

命名理由：

- “黑洞等待室”适合传播，但会把对象误锁定为黑洞。
- “度规红移固有时差分路径”适合描述物理核心，但不够覆盖“可控、生命周期、退出、采用、递归”的系统对象。
- “可控度规等待室”把关键约束放在度规控制、固有时差分和等待室生命周期闭合上。

## 最小公式对象

页面把路径价值压缩成 toy NCG，不作为预测器：

```text
Delta_tau_subject = integral_gamma sqrt(-g_mu_nu dx_mu dx_nu) / c
K = Delta_t_external / Delta_tau_subject
P_access = P_enter * P_stay * P_exit * P_adopt * P_cont
B_wait = K * U_upgrade(Delta_t_external)
R_total = R_life + R_engineering + R_tail + C_wait
NCG = B_wait * P_access - R_total
```

其中：

- `K` 只表示等待倍率，不等于收益。
- `P_exit`、`P_adopt`、`P_cont` 是必要概率门。
- `R_tail` 可以作为硬否决门，而不只是线性扣减项。
- `NCG` 是路径排序和反证对象，不输出个体寿命或工程可行性。

## 本轮产物

- 论文页：`web/src/pages/papers/controllable-metric-waiting-room-hypothesis.astro`
- 结构化数据源：`web/src/data/controllable-metric-waiting-room-hypothesis.json`
- 工具 seed：`web/src/data/controllable-metric-waiting-room-hypothesis/TOOL_GENERATED_PAGE_SEED.astro`
- 推导包：`web/src/data/controllable-metric-waiting-room-hypothesis/DERIVATION_PACKAGE.md`
- 来源核验：`web/src/data/controllable-metric-waiting-room-hypothesis/REFERENCE_VERIFICATION.json`
- 引用语境外部审查包：`web/src/data/controllable-metric-waiting-room-hypothesis/CITATION_CONTEXT_REVIEW_PACKET.json`
- 引用语境本地审查：`web/src/data/controllable-metric-waiting-room-hypothesis/CITATION_CONTEXT_LOCAL_REVIEW.json`
- 预提交审查：`web/src/data/controllable-metric-waiting-room-hypothesis/PRE_SUBMISSION_REVIEW.json`
- 覆盖审计：`web/src/data/controllable-metric-waiting-room-hypothesis/COVERAGE_AUDIT.json`

## 页面结构

页面保留 arXiv HTML Paper Reuse Kit 的 CSS、JS、字体和 DOM 契约，只替换正文内容。

正文结构：

```text
Abstract
  -> 研究对象
  -> 理论命名
  -> 核心假设
  -> 物理接口
  -> 形式化推导
  -> 命题与证据
  -> 系统状态机
  -> 递归等待链路
  -> 变量契约
  -> 场景比较
  -> 失败条件
  -> 研究协议
  -> 治理边界
  -> 工具链记录
  -> References
```

## 场景比较

页面把“黑洞等待室”拆成五类场景：

| 场景 | 当前用途 | 判断 |
| --- | --- | --- |
| 天然超大质量黑洞附近等待 | 压力测试反例 | 高 K 不等于高 NCG |
| 类黑洞人工强红移结构 | 远期假设对象 | 缺少重力控制、能源、材料和安全证据 |
| 等效度规工程等待区 | 主研究对象 | 适合构造 toy metric 和 scenario card |
| 高速相对论飞船 | 比较路径 | 区分运动学时间膨胀和度规等待室 |
| 人体冷冻或低代谢休眠 | 机制对照组 | 防止混淆生物保存和强引力等待 |

## 本地门禁

新增命令：

```bash
cd web
npm run audit:controllable-metric-waiting-room
```

当前审计状态：

```text
Reference verification: PASS
Citation context packet: READY_FOR_EXTERNAL_REVIEW
Citation context local review: LOCAL_REVIEW_COMPLETE_REQUIRES_FRESH_REVIEW
Pre-submission review: NEEDS_EXTERNAL_REVIEW_BEFORE_FORMAL_SUBMISSION
Coverage audit: PASS
Sections: 14
TOC entries: 14
Duplicate class patterns: 0
```

## 剩余边界

- 仍需外部物理学 reviewer 检查固有时、度规、黑洞边界和强场简化。
- 仍需外部 citation-context reviewer 逐句判断来源是否支持当前语境。
- 仍缺少 toy metric、数值示例、敏感性分析和场景卡片扩展。
- 当前页面只能作为 Human Infra working paper，不是正式物理论文、工程可行性论文、医学建议或个体决策材料。
