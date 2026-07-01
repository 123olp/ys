# Contact Lens Hygiene Eye Infection Continuity

`contact-lens-hygiene-eye-infection-continuity` 研究隐形眼镜佩戴、清洁、储存、替换、护理液、处方更新和感染风险如何影响视觉任务、工作学习、出行和眼部安全连续性。

> 核心问题：隐形眼镜不是单纯屈光矫正用品；它把视觉带宽、手部卫生、耗材供应、佩戴习惯、感染入口和眼科转诊连成一个日常风险系统。

## 关注对象

- 隐形眼镜、护理液、镜盒、替换周期、处方有效性、佩戴场景和卫生行为。
- 角膜感染、疼痛、红眼、视力变化、眼表损伤和医疗延迟的任务影响。
- 学校、工作、运动、旅行、灾害、住房不稳、清洁水可及和替代眼镜路径。
- 与屈光矫正、眼表舒适、眼外伤、WASH、医疗器械和药店/眼科服务的接口。

## Human Infra 链路

```text
隐形眼镜卫生连续
  -> 主体能够稳定获得清晰视觉输入且不把矫正工具变成感染入口
  -> 清洁水、护理液、镜盒、替换周期和转诊入口的断点被提前识别
  -> 阅读、驾驶、屏幕任务、学习、工作和空间行动的低层视觉摩擦下降
  -> 有效时间、行动安全和未来选择权增强
```

## 非目标

- 不提供验光、隐形眼镜处方、品牌推荐、佩戴时长、感染判断、眼科治疗或急症处置建议。
- 不替代眼科医生、验光师、FDA、CDC、NEI 或产品标签。
- 不把隐形眼镜作为绕过职业安全、防护眼镜或眼伤转诊的替代方案。

## Source Signals

- CDC Contact Lenses: https://www.cdc.gov/contact-lenses/
- NEI Contact Lenses: https://www.nei.nih.gov/eye-health-information/healthy-vision/contact-lenses
- FDA Medical Devices - Contact Lenses search entry may move; prefer CDC/NEI for stable hygiene and eye health facts.

## 下一步

- 建立 `lens type -> hygiene dependency -> supply dependency -> eye risk -> task impact` 变量表。
- 区分日常佩戴、游泳/淋浴、睡眠佩戴、旅行、灾害、青少年和住房/水卫生不稳场景。
- 与 `refractive-error-glasses-contact-lens-continuity`、`dry-eye-ocular-surface-comfort-continuity` 和 `eye-injury-urgent-vision-protection-continuity` 建立边界。
