# Chronic Kidney Disease Screening Progression Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/chronic-kidney-disease-screening-progression-continuity` |
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


`chronic-kidney-disease-screening-progression-continuity/` 研究慢性肾病筛查、白蛋白尿/eGFR 观测、进展风险、心肾代谢交互、肾脏保护治疗可及和透析前准备如何影响主体持续性。

> 核心问题：慢性肾病常在无症状阶段进展，直到贫血、心衰、电解质失衡、尿毒症或 AKI 叠加才显性化。有效永生需要把 CKD 建模为长期内环境储备和心血管风险的关键状态变量。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖肾脏维持容量、电解质、酸碱、毒素和内分泌稳定
  -> CKD 会长期降低内环境缓冲能力并放大心血管和 AKI 风险
  -> 结果取决于筛查、进展风险识别、保护治疗、随访和替代治疗准备
  -> 因此 CKD 筛查与进展治理是急性肾衰之前的上游储备域
```

## 关注对象

- CKD detection, eGFR / albuminuria, risk stratification, progression, kidney protective care, nephrology access, dialysis / transplant preparation boundaries。
- 与 `renal-hepatic-clearance/` 的边界：该域关注清除系统机制；本域关注 CKD 作为长期可观测、可分层、可延缓的进展路径。
- 与 `acute-kidney-injury-renal-replacement-continuity/` 的关系：本域处理慢性储备下降，后者处理急性内环境失控。

## Human Infra 模型链路

```text
CKD 筛查与进展治理 T
  -> 改变 eGFR/白蛋白尿观测、风险分层、保护治疗、随访和转诊变量 X
  -> 改变肾脏储备、容量/电解质缓冲、心血管风险和替代治疗准备状态 S
  -> 改变 ESRD、AKI、心衰、死亡和有效时间损失 λ(t)
  -> 影响主体长期健康寿命、治疗负担和未来选择权
```

## 非目标

- 不提供 eGFR、肌酐、尿检、白蛋白尿、饮食、补液、药物、透析、移植、检查排序或个体肾病建议。
- 不生成个人 CKD 分期、风险评分、用药调整、饮食限制、透析选择或保险申诉。
- 不收集个案实验室、血压、糖尿病、用药、尿检、影像或诊疗资料。

## Source Signals

- KDIGO CKD evaluation and management: https://kdigo.org/guidelines/ckd-evaluation-and-management/
- NIDDK kidney disease information: https://www.niddk.nih.gov/health-information/kidney-disease
- National Kidney Foundation CKD materials: https://www.kidney.org/kidney-topics/chronic-kidney-disease-ckd

## 下一步

- 建立 CKD Progression Card：detection, albuminuria/eGFR, risk stratification, protective care, referral, transition planning。
- 与 `renal-hepatic-clearance/`、`acute-kidney-injury-renal-replacement-continuity/` 和 `hypertension-detection-control-continuity/` 建立接口。
