# Acute Kidney Injury Renal Replacement Continuity

`acute-kidney-injury-renal-replacement-continuity/` 研究急性肾损伤、体液/电解质/酸碱失衡、透析/肾脏替代治疗、ICU 肾支持和长期肾功能恢复如何影响主体持续性。

> 核心问题：肾功能失败会让毒素、容量、电解质和酸碱平衡失控。肾脏替代治疗是把内环境崩溃转化为可支持窗口的基础技术。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要清除代谢废物并维持体液、电解质和酸碱稳态
  -> 急性肾损伤可在脓毒症、创伤、药物、手术或休克中迅速出现
  -> 肾脏替代治疗可争取恢复窗口，但受容量、血流动力学、感染和资源约束
  -> 因此 AKI 与肾脏替代治疗是内环境失败的急性支持域
```

## 关注对象

- AKI detection、KDIGO staging、fluid balance、electrolytes、acid-base、CRRT/intermittent dialysis、ICU renal support、kidney recovery、CKD transition。
- 与 `renal-hepatic-clearance/` 的边界：清除域关注长期器官功能；本域关注急性肾失败与设备支持。
- 与 `sepsis-shock-early-recognition-resuscitation-continuity/` 的关系：脓毒症和休克是 AKI 的重要上游。

## Human Infra 模型链路

```text
AKI 与肾脏替代支持 T
  -> 改变毒素、容量、电解质、酸碱、设备可用和肾恢复变量 X
  -> 改变内环境稳定、ICU 病程、长期肾功能和治疗负担状态 S
  -> 改变急性死亡、心律风险、脑功能损害、CKD 转化和再住院风险 λ(t)
  -> 影响主体恢复能力、治疗选择和有效时间
```

## 非目标

- 不提供透析适应证、参数、饮食、补液、用药、实验室解读、肾病治疗或个体医疗建议。
- 不生成 CRRT/透析设置、医院路径、设备操作、保险或转院建议。
- 不收集肌酐、电解质、尿量、透析记录、病历、设备日志或保险资料。

## Source Signals

- KDIGO Acute Kidney Injury: https://kdigo.org/guidelines/acute-kidney-injury/
- National Kidney Foundation AKI: https://www.kidney.org/kidney-topics/acute-kidney-injury-aki
- NIH Kidney Failure Treatment: https://www.niddk.nih.gov/health-information/kidney-disease/kidney-failure/choosing-treatment

## 下一步

- 建立 Renal Support Card：AKI signal, fluid/electrolyte risk, support modality, hemodynamic tolerance, recovery, CKD transition。
- 与 `renal-hepatic-clearance/`、`fluid-electrolyte-acid-base-homeostasis/` 和 `intensive-care-organ-support-delirium-continuity/` 建立接口。
