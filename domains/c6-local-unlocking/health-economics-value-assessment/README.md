# Health Economics Value Assessment

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/health-economics-value-assessment` |
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


`health-economics-value-assessment/` 研究疾病负担、健康损失、成本效果、卫生技术评估、资源分配和公共价值边界。

> 核心问题：有效永生和主体持续性不是无限预算口号；项目必须能审查哪些问题造成最大健康/功能损失，哪些干预有可承受成本，哪些价值判断不能被 QALY、DALY 或价格完全替代。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 资源、时间、医疗能力和公共预算都是有限的
  -> 干预选择必须同时审查疾病负担、功能收益、成本、可及性、公平和权利
  -> 价值评估决定稀缺资源如何转化为更大的主体持续性收益
```

## 关注对象

- 疾病负担、死亡率、YLL、YLD、DALY、QALY、成本效果、预算影响、HTA、价值框架和支付激励。
- IHME GBD、WHO Global Health Estimates、WHO-CHOICE、NICE HTA、ICER、AHRQ MEPS 等资料。
- 与 `financial-resilience-access/` 的关系：财务韧性域关注个体和家庭支付能力；本域关注系统级资源配置与价值评估。
- 与 `functioning-quality-of-life-outcomes/`、`insurance-risk-transfer/`、`healthcare-access-continuity/` 和 `social-protection-benefits-delivery/` 的接口。

## Human Infra 模型链路

```text
健康经济与价值评估基础设施
  -> 改变疾病负担、成本、效果、预算影响和公平权重的可见性
  -> 改变干预优先级、资源配置、支付激励和公共投资方向
  -> 降低低价值投入、不可及干预、预算挤出和把人还原为价格的风险
  -> 增强公共资源转化为健康寿命、有效时间、功能和未来选择权的能力
```

## 非目标

- 不提供投资建议、报销策略、保险选择、个体治疗选择、福利申请或医疗支付建议。
- 不把 QALY、DALY、成本效果或支付模型写成决定某个人是否值得治疗的依据。
- 不用经济评价替代公平、尊严、权利、同意、风险和主体体验。

## Source Signals

- IHME Global Burden of Disease: https://www.healthdata.org/research-analysis/gbd
- WHO Global Health Estimates: https://www.who.int/data/global-health-estimates
- WHO cost-effectiveness portal: https://www.who.int/universal-health-coverage/compendium/cost-effectiveness-portal
- NICE technology appraisal guidance: https://www.nice.org.uk/what-nice-does/our-guidance/about-technology-appraisal-guidance
- ICER value assessment framework: https://icer.org/assessment/value-assessment-framework-2020/
- AHRQ MEPS: https://meps.ahrq.gov/mepsweb/

## 下一步

- 建立价值评估变量表：疾病负担、成本、效果、时间范围、视角、公平权重、预算影响、不确定性和权利边界。
- 与 `functioning-quality-of-life-outcomes/` 对齐功能/QoL 结局，与 `insurance-risk-transfer/` 拆分风险池和价值评估边界。
- 整理 GBD、GHE、WHO-CHOICE、NICE、ICER 和 MEPS 的 Source Cards。
