# Pancreatic Cancer High Risk Detection Treatment Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pancreatic-cancer-high-risk-detection-treatment-continuity` |
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


`pancreatic-cancer-high-risk-detection-treatment-continuity/` 研究胰腺癌高风险人群识别、早期症状、诊断延迟、治疗可及、营养/疼痛负担、家庭照护和生活质量如何影响主体持续性。

> 核心问题：胰腺癌常在晚期发现，主体持续性损失来自诊断延迟、体重/营养崩塌、疼痛、治疗窗口窄和家庭照护高负担。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖高致死癌种的风险窗口被尽可能提前识别
  -> 胰腺癌高风险识别、症状重视、诊断速度和治疗可及改变死亡风险
  -> 营养、疼痛、家庭照护和服务协调决定主体有效时间是否快速坍塌
  -> 因此胰腺癌是癌症连续性中的高致死风险和支持照护负担域
```

## 关注对象

- Pancreatic cancer, high-risk detection, early symptoms, diagnostic delay, treatment access, nutrition, pain, caregiver burden, palliative / supportive continuity。
- 与 `nutrition-metabolic-health/` 的关系：胰腺癌常直接冲击体重、消化、营养和能量状态。
- 与 `palliative-care-serious-illness-planning-continuity/` 和 `caregiving-family-support-continuity/` 的关系：支持照护和家庭照护是核心连续性变量。

## Human Infra 模型链路

```text
胰腺癌连续性系统 T
  -> 改变高风险识别、症状重视、诊断延迟、治疗可及、营养/疼痛和照护变量 X
  -> 改变癌症阶段、体重/能量、疼痛、治疗耐受性、家庭资源和心理状态 S
  -> 改变死亡、失能、有效时间坍塌和照护资源消耗 λ(t)
  -> 影响主体健康寿命、行动能力、尊严和未来选择权
```

## 非目标

- 不提供高风险判定、症状诊断、影像/肿瘤标志物判读、筛查建议、分期、治疗方案、疼痛处理、营养处理、临床试验选择或个体建议。
- 不生成个人胰腺癌风险计算器、影像解释、标志物解释、治疗排序、疼痛/营养方案或商业检测推广。
- 不收集个案症状、影像、CA19-9、病理、遗传检测、体重、疼痛或治疗资料。

## Source Signals

- NCI pancreatic cancer: https://www.cancer.gov/types/pancreatic
- NCI pancreatic cancer treatment: https://www.cancer.gov/types/pancreatic/patient/pancreatic-treatment-pdq
- PanCAN patient information: https://pancan.org/facing-pancreatic-cancer/

## 下一步

- 建立 Pancreatic Cancer Continuity Card：high-risk boundary, symptom delay, diagnostic pathway, treatment access, nutrition, pain, caregiver load。
- 与 `cancer-control/`、`nutrition-metabolic-health/` 和 `palliative-care-serious-illness-planning-continuity/` 建立接口。
