# Reproductive Fertility Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/reproductive-fertility-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 直接维护身体、脑、器官、衰老、损伤或生命系统这些可能性源体。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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


Reproductive Fertility Continuity 负责整理生殖系统、生育力、配子质量、生殖衰老、妊娠相关风险和未来选择权如何进入主体持续性模型。

核心问题：

> 有效永生关注主体自身持续性，但主体的未来选择权也包括是否保留生育、亲缘、代际和生殖相关自主性；生殖衰老和生育风险会改变人生路径、资源配置和长期计划。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体不仅需要当前行动能力，也需要长期选择权
  -> 生殖系统、生育窗口、配子质量、妊娠风险和生殖自主性会影响人生路径和资源分配
  -> 生殖衰老、 infertility、妊娠风险或生殖权利丧失会限制未来选择空间
  -> 因此生殖与生育连续性是主体持续性的未来选择权域
```

## 关注对象

- 生育力、配子质量、卵巢储备、精子质量、生殖衰老、 menopause、妊娠风险和不孕。
- 生殖健康、亲缘选择、计划生育、生殖权利、生育保存和年龄相关生殖限制。
- 生殖系统如何进入内分泌、心理健康、资源规划、法律权利、未来选择权和主体连续性模型。
- 与泌尿生殖连续性的边界：本域关注生育窗口和未来选择权；`urogenital-continuity/` 关注排泄、感染、性功能和日常尊严。

## Human Infra 模型链路

```text
生殖与生育因素 T
  -> 改变生育力、配子质量、生殖风险、生殖自主性和资源规划变量 X
  -> 改变主体未来选择权、家庭路径、心理状态和长期计划状态 S
  -> 改变 infertility、妊娠并发症、心理负担、资源压力和选择受限风险 λ(t)
  -> 影响有效时间、未来选择权和主体持续性的扩展边界
```

## 非目标

- 不提供不孕诊断、生育治疗、激素用药、辅助生殖、妊娠管理、避孕或个体医疗建议。
- 不把生育力、年龄、激素或配子质量写成个体选择结论。
- 不把生殖连续性等同于主体持续性本身；它是未来选择权维度，不是永生证明。

## Source Signals

- WHO infertility fact sheet: https://www.who.int/news-room/fact-sheets/detail/infertility
- WHO sexual and reproductive health: https://www.who.int/health-topics/sexual-and-reproductive-health
- NICHD fertility and infertility: https://www.nichd.nih.gov/health/topics/infertility

## 下一步

1. 建立生殖与生育变量表：生育窗口、配子质量、生殖衰老、妊娠风险、生殖自主性和未来选择权。
2. 与 `endocrine-hormonal-regulation/`、`governance-rights/`、`mental-health-affective-stability/` 和 `resource-social-infra/` 建立交叉边界。
