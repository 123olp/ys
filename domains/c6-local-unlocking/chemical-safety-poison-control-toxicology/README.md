# Chemical Safety Poison Control Toxicology

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/chemical-safety-poison-control-toxicology` |
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


化学安全、中毒控制与毒理响应域研究：当主体持续性依赖“化学暴露、中毒、毒性材料和化学事故能被预防、识别、咨询和治理”时，需要哪些毒理、监管、毒物中心、监测和风险沟通基础设施。

## 对象

- 化学品安全、毒性暴露、急慢性中毒、家庭/工作/环境化学风险。
- 毒物中心、毒理咨询、暴露监测、不良事件数据和风险沟通。
- 化学品监管、标签、限制、替代、职业安全和环境健康接口。
- 化学事故、消费品暴露、农药/工业化学品、清洁剂和混合暴露风险。
- 化学风险与神经、肝肾清除、呼吸、皮肤、儿童发展和心理安全的接口。

## Human Infra 价值

化学风险的特点是常见、分散、混合、不可直观判断。化学安全和毒物控制基础设施把暴露从“个体孤立判断”转化为可咨询、可监测、可监管和可预防的公共能力，减少急性中毒、慢性伤害和环境不平等。

```text
化学品进入生活、工作和环境
  -> 标签、限制、监测、毒物中心和毒理证据
  -> 暴露误判、急性中毒和慢性毒性风险下降
  -> 主体健康、行动能力和家庭安全得到保护
```

## 边界

本域只整理公开安全资料、监管框架、毒理概念、毒物中心角色和非操作性风险治理。

不提供：

- 中毒诊断、治疗、解毒、剂量判断、家庭处置或急救替代建议。
- 化学合成、混配、提纯、获取、规避标签或危险实验步骤。
- 毒性利用、投毒、规避检测、制造暴露或隐藏暴露的信息。
- 企业合规、个体职业暴露申诉、产品选择或实时事故处置建议。

## 上游与下游

- 上游：`substance-exposure-control/`、`planetary-health-environment/`、`occupational-work-design/`、`product-safety-recall-systems/`。
- 下游：`renal-hepatic-clearance/`、`respiratory-oxygenation/`、`skin-barrier-wound-healing/`、`emergency-preparedness-response/`。

## 初始资料线索

- EPA chemicals under TSCA resources。
- America’s Poison Centers / Poison Help resources。
- CDC / NIOSH chemical safety resources。
- WHO chemical safety resources。
