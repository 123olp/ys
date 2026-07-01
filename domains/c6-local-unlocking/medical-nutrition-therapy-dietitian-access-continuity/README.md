# Medical Nutrition Therapy Dietitian Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/medical-nutrition-therapy-dietitian-access-continuity` |
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


该域研究 medical nutrition therapy（MNT）、注册营养师/营养师服务、转诊、覆盖、远程营养治疗和慢病营养管理如何成为主体持续性基础设施。它关注专业营养服务可达，不提供个人营养方案。

## 核心问题

- MNT 如何通过临床转介、保险覆盖、Medicare/CMS 规则、诊断边界、RDN workforce 和 telehealth 进入主体照护路径。
- 专业营养服务如何影响糖尿病、肾病、心血管风险、胃肠疾病、癌症照护、肥胖管理和营养不良。
- 哪些断点会让“应由专业营养服务处理”的问题被降级为泛泛饮食建议。
- 如何区分 MNT、nutrition education、health coaching、MTM、MTG 和普通健康内容。

## 对象

- Medical nutrition therapy、registered dietitian nutritionist、dietitian referral、nutrition counseling。
- Medicare / Medicaid / payer coverage、diagnosis criteria、telehealth、documentation、follow-up。
- 慢病、营养不良、肾病、糖尿病、饮食限制、语言文化适配和访问公平。

## Human Infra 价值

专业营养治疗把复杂疾病饮食、代谢风险和食品执行问题从“自我猜测”转为可评估、可跟踪、可调整的照护能力。该域用于保护主体在慢病和恢复期中的行动质量、治疗执行和有效时间。

## 边界

- 只整理公开覆盖规则、服务模型、证据和执行断点。
- 不提供个人饮食计划、营养处方、疾病管理、诊断、补剂、减重、肾病/糖尿病饮食、保险覆盖判断或转诊建议。
- 不替代医生、RDN、药师、保险计划、急救或临床照护团队。

## 上游与下游

- 上游：`nutrition-insecurity-screening-referral-continuity`、`primary-care-panel-appointment-access-continuity`、`specialist-referral-authorization-navigation-continuity`、`insurance-eligibility-benefits-verification-continuity`。
- 下游：`nutrition-metabolic-health`、`diabetes-insulin-glucose-monitoring-supplies-continuity`、`chronic-kidney-renal-replacement-continuity`、`cardiovascular-resilience`。

## 初始资料线索

- CMS Medicare medical nutrition therapy coverage materials.
- NIH / NIDDK nutrition and chronic disease research.
- HHS Food is Medicine.
- Academy and peer-reviewed MNT access / outcomes literature.
