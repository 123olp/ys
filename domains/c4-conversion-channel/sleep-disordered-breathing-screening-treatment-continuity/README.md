# Sleep Disordered Breathing Screening Treatment Continuity

`sleep-disordered-breathing-screening-treatment-continuity/` 研究阻塞性睡眠呼吸暂停、夜间低氧、日间嗜睡、诊断转介、治疗坚持和设备可及如何影响主体持续性。

> 核心问题：睡眠呼吸障碍不是单纯睡眠质量问题，而是通过低氧、觉醒碎片、心血管压力、事故风险和认知疲劳持续改变有效时间与死亡风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖睡眠中的呼吸稳定维持脑、心血管和代谢恢复
  -> 睡眠呼吸障碍可在长期未识别状态下造成低氧、疲劳、事故和心血管负荷
  -> 结果取决于症状识别、诊断可及、设备/行为治疗可及、坚持和随访
  -> 因此睡眠呼吸障碍是恢复系统与风险预防之间的关键执行域
```

## 关注对象

- Obstructive sleep apnea、sleep-disordered breathing、nocturnal hypoxemia、daytime sleepiness、screening uncertainty、sleep study access、CPAP / oral appliance adherence、driving and work safety。
- 与 `sleep-circadian-recovery/` 的边界：该域关注睡眠、昼夜节律和恢复总机制；本域关注呼吸障碍、低氧和治疗连续性。
- 与 `respiratory-oxygenation/` 的关系：本域处理睡眠阶段的呼吸和氧合断点。

## Human Infra 模型链路

```text
睡眠呼吸障碍识别与治疗系统 T
  -> 改变低氧负荷、觉醒碎片、白天警觉性、治疗坚持和设备可及变量 X
  -> 改变脑恢复、心血管压力、代谢状态、事故暴露和认知疲劳 S
  -> 改变有效时间损失、心血管事件、工作/驾驶风险和长期失能 λ(t)
  -> 影响主体学习、行动、恢复、判断和未来选择权
```

## 非目标

- 不提供个人筛查量表解读、睡眠监测判读、CPAP 设置、口腔矫治器选择、用药、驾驶限制或治疗建议。
- 不生成个人诊断、睡眠报告解释、设备购买建议、保险申诉或职业安全判定。
- 不收集个案睡眠、呼吸、血氧、体重、病史、药物、驾驶或设备数据。

## Source Signals

- NHLBI sleep apnea: https://www.nhlbi.nih.gov/health/sleep-apnea
- USPSTF obstructive sleep apnea screening statement: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/obstructive-sleep-apnea-in-adults-screening
- CDC sleep and sleep disorders: https://www.cdc.gov/sleep/

## 下一步

- 建立 Sleep Breathing Continuity Card：symptoms, oxygen burden, study access, treatment access, adherence, safety exposure, follow-up。
- 与 `sleep-circadian-recovery/`、`respiratory-oxygenation/` 和 `cardiovascular-resilience/` 建立接口。
