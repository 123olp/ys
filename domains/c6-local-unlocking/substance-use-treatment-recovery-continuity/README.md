# Substance Use Treatment Recovery Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/substance-use-treatment-recovery-continuity` |
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


物质使用障碍治疗与恢复连续性域研究：当成瘾、过量风险、复发、污名、刑事化和治疗断点影响主体持续性时，治疗入口、恢复支持、减害、同伴支持和长期照护如何把风险重新接回恢复路径。

## 对象

- 物质使用障碍、成瘾治疗、恢复支持、FindTreatment.gov、同伴支持、恢复社区和长期随访。
- 过量预防、减害框架、污名、服务可及、保险覆盖、羁押释放、无家可归和农村服务断点。
- 治疗保留、复发风险、家庭关系、就业、住房、心理健康、慢病和公共卫生接口。
- 物质使用障碍对死亡风险、认知控制、资源消耗、关系网络、有效时间和未来选择权的影响。

## Human Infra 价值

`substance-exposure-control/` 关注暴露和风险，本域关注已经形成障碍后的治疗、恢复和社会重新连接。成瘾不是单一意志问题，而是一个需要服务入口、持续照护、关系支持和反污名机制共同承接的长期恢复系统。

```text
治疗和恢复支持不断线
  -> 过量、复发、污名、住房断裂和刑事化风险下降
  -> 主体恢复健康、关系、工作和自我控制窗口
  -> 有效时间、行动能力和未来选择权提高
```

## 边界

本域只整理公开物质使用障碍治疗、恢复支持、过量预防、减害治理和服务连续性资料。

不提供：

- 个体诊断、戒断、排毒、药物、剂量、替代治疗、复发处理或医疗建议。
- 非法物质获取、制造、配方、剂量、混用、规避检测、运输、销售或危险使用指南。
- 过量现场处置、急救步骤、法律策略、执法规避、保险/福利个案或机构选择建议。
- 把成瘾、复发或过量风险写成道德失败、治安标签、商业营销或剥削性定位。

## 上游与下游

- 上游：`substance-exposure-control/`、`mental-health-affective-stability/`、`medicine-access-treatment-continuity/`、`community-health-workers-peer-support/`。
- 下游：`homelessness-unsheltered-health-continuity/`、`correctional-health-reentry-continuity/`、`workforce-employment-services/`、`social-connection-relational-infra/`。

## 初始资料线索

- SAMHSA FindTreatment.gov and treatment resources。
- CDC overdose prevention resources。
- NIDA substance use and addiction resources。
- Public materials on peer support, recovery support and harm reduction governance。
