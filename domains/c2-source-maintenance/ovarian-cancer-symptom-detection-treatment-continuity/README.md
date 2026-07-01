# Ovarian Cancer Symptom Detection Treatment Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/ovarian-cancer-symptom-detection-treatment-continuity` |
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


`ovarian-cancer-symptom-detection-treatment-continuity/` 研究卵巢癌症状识别、诊断延迟、遗传风险入口、治疗负担、复发管理、家庭照护和生活质量如何影响主体持续性。

> 核心问题：卵巢癌常缺少普通人群有效筛查路径，连续性重点不是简单“早筛”，而是症状被认真对待、风险入口不失联、诊断延迟被压缩和复发负担被管理。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖高死亡风险但筛查困难的癌种被及时识别和持续支持
  -> 卵巢癌症状非特异、诊断延迟和复发负担改变死亡风险和家庭资源消耗
  -> 症状识别、风险入口、治疗可及、复发管理和照护支持决定主体是否保留行动能力
  -> 因此卵巢癌是癌症连续性中的症状-诊断延迟治理域
```

## 关注对象

- Ovarian cancer symptoms, diagnostic delay, genetic risk pathway, treatment burden, recurrence, caregiver load, quality of life, equity。
- 与 `cancer-screening-early-detection-continuity/` 的边界：本域不假定普通筛查可行，重点放在症状识别、风险通道和诊断延迟。
- 与 `reproductive-fertility-continuity/` 和 `caregiving-family-support-continuity/` 的关系：卵巢癌强烈影响生殖系统、家庭照护和长期心理负担。

## Human Infra 模型链路

```text
卵巢癌连续性系统 T
  -> 改变症状识别、风险入口、诊断延迟、治疗可及、复发管理和照护变量 X
  -> 改变癌症阶段、治疗毒性、复发负担、家庭资源和心理状态 S
  -> 改变死亡、失能、有效时间损失和照护资源消耗 λ(t)
  -> 影响主体健康寿命、家庭系统、行动能力和未来选择权
```

## 非目标

- 不提供症状诊断、CA-125/影像判读、遗传风险解释、筛查建议、病理分型、分期、治疗方案、用药、手术或个体建议。
- 不生成个人卵巢癌风险计算器、症状分诊、影像/标志物解释、治疗排序或商业检测推广。
- 不收集个案症状、CA-125、影像、病理、遗传检测、家族史或治疗资料。

## Source Signals

- NCI ovarian cancer: https://www.cancer.gov/types/ovarian
- NCI ovarian cancer screening: https://www.cancer.gov/types/ovarian/screening
- CDC ovarian cancer: https://www.cdc.gov/ovarian-cancer/

## 下一步

- 建立 Ovarian Cancer Continuity Card：symptom recognition, diagnostic delay, hereditary risk pathway, treatment burden, recurrence, caregiver load。
- 与 `cancer-control/`、`reproductive-fertility-continuity/` 和 `cancer-survivorship-late-effects-continuity/` 建立接口。
