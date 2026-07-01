# Colorectal Cancer Screening Treatment Continuity

`colorectal-cancer-screening-treatment-continuity/` 研究结直肠癌筛查、息肉/异常结果追踪、肠镜可及、治疗负担、肠功能、造口、复发监测和长期生活质量如何影响主体持续性。

> 核心问题：结直肠癌高度依赖前端筛查和异常闭环；断点常出现在筛查可及、肠镜容量、病理追踪、治疗副作用和长期肠功能恢复。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖可预防或可早治癌种被前移识别
  -> 结直肠癌筛查和异常追踪改变癌症阶段、治疗强度和死亡风险
  -> 肠镜、病理、治疗、造口和复发监测决定主体功能是否被长期保护
  -> 因此结直肠癌是癌症筛查闭环和功能恢复的关键器官域
```

## 关注对象

- Colorectal cancer screening, stool tests, colonoscopy access, abnormal follow-up, polyp history, treatment burden, ostomy / bowel function, recurrence surveillance。
- 与 `cancer-screening-early-detection-continuity/` 的边界：本域把通用筛查闭环落到结直肠癌特有的肠镜、息肉、肠功能和造口负担。
- 与 `gastrointestinal-digestion-microbiome/` 和 `healthcare-access-continuity/` 的关系：筛查容量和消化功能恢复是本域重要上下游。

## Human Infra 模型链路

```text
结直肠癌连续性系统 T
  -> 改变筛查覆盖、肠镜容量、异常追踪、治疗可及、肠功能和复发监测变量 X
  -> 改变癌症阶段、治疗毒性、造口/排便功能、工作参与和心理负担状态 S
  -> 改变死亡、失能、生活质量下降和有效时间损失 λ(t)
  -> 影响主体健康寿命、行动半径、尊严和未来选择权
```

## 非目标

- 不提供筛查年龄、检查频率、粪便检测/肠镜结果解释、病理判读、息肉风险、分期、治疗方案、饮食、造口护理或个体建议。
- 不生成个人结直肠癌筛查推荐器、肠镜排序、病理解释、治疗路线或商业检测推广。
- 不收集个案肠镜、病理、症状、家族史、造口照片或治疗资料。

## Source Signals

- NCI colorectal cancer: https://www.cancer.gov/types/colorectal
- NCI colon and rectal cancer screening: https://www.cancer.gov/types/colorectal/screening
- CDC colorectal cancer: https://www.cdc.gov/colorectal-cancer/

## 下一步

- 建立 Colorectal Cancer Continuity Card：screening modality, abnormal follow-up, colonoscopy capacity, treatment burden, bowel function, survivorship。
- 与 `cancer-control/`、`cancer-screening-early-detection-continuity/` 和 `cancer-survivorship-late-effects-continuity/` 建立接口。
