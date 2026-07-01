# Breast Cancer Screening Treatment Survivorship Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/breast-cancer-screening-treatment-survivorship-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
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


`breast-cancer-screening-treatment-survivorship-continuity/` 研究乳腺癌筛查、异常影像追踪、诊断闭环、治疗负担、复发监测、身体形象、工作参与和幸存者连续性如何影响主体持续性。

> 核心问题：乳腺癌不是单一“早筛”问题；它贯穿风险识别、影像异常、组织诊断、治疗毒性、复发恐惧、性别化污名、家庭照护和长期生活质量。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖恶性增殖风险被提前发现并被长期管理
  -> 乳腺癌改变死亡风险、身体完整性、劳动参与、关系安全和心理负担
  -> 筛查、异常追踪、治疗入口、复发监测和幸存者支持决定风险是否被闭环
  -> 因此乳腺癌是癌症连续性中的器官特异高负担域
```

## 关注对象

- Breast cancer screening, diagnostic follow-up, treatment burden, recurrence monitoring, survivorship, body image, fertility / sexuality concerns, family work load。
- 与 `cancer-screening-early-detection-continuity/` 的边界：该域关注通用癌筛逻辑；本域关注乳腺癌特有的影像路径、治疗负担和幸存者断点。
- 与 `reproductive-fertility-continuity/`、`mental-health-continuity/` 和 `caregiving-family-support-continuity/` 的关系：乳腺癌常同时改变生殖、心理、家庭和工作连续性。

## Human Infra 模型链路

```text
乳腺癌连续性系统 T
  -> 改变筛查覆盖、异常追踪、治疗可及、复发监测、身体形象和支持变量 X
  -> 改变癌症阶段、治疗毒性、复发风险、心理负担和工作参与状态 S
  -> 改变死亡、失能、治疗后功能损失和有效时间损失 λ(t)
  -> 影响主体健康寿命、家庭资源、身份连续性和未来选择权
```

## 非目标

- 不提供乳腺影像判读、筛查年龄、筛查频率、遗传风险、病理分型、分期、治疗方案、用药、手术、放疗、化疗、内分泌治疗或个体建议。
- 不生成个人乳腺癌风险计算器、影像第二意见、治疗排序、复发判断、保险申诉或商业检测推广。
- 不收集个案乳腺影像、病理、基因检测、症状、治疗记录或家庭史。

## Source Signals

- NCI breast cancer: https://www.cancer.gov/types/breast
- NCI cancer survivorship: https://www.cancer.gov/about-cancer/coping/survivorship
- CDC breast cancer: https://www.cdc.gov/breast-cancer/

## 下一步

- 建立 Breast Cancer Continuity Card：screening, abnormal follow-up, diagnosis, treatment burden, recurrence monitoring, survivorship, equity。
- 与 `cancer-control/`、`diagnostic-imaging-order-scheduling-report-continuity/` 和 `cancer-survivorship-late-effects-continuity/` 建立接口。
