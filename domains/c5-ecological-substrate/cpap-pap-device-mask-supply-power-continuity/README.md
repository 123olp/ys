# CPAP PAP Device Mask Supply Power Continuity

`cpap-pap-device-mask-supply-power-continuity` 研究 CPAP/BiPAP/PAP 设备、面罩、管路、滤芯、清洁、供电、旅行、召回、供应商和依从支持如何影响睡眠、日间警觉、心血管风险、驾驶安全和恢复能力。

> 核心问题：PAP 治疗的收益依赖设备每天晚上可用；面罩漏气、耗材断供、停电、旅行断点或供应商摩擦会把可治疗睡眠风险重新变成恢复失败。

## 关注对象

- CPAP、BiPAP、PAP 设备、面罩、管路、滤芯、加湿器、清洁维护、供电、旅行电源、召回和耗材替换。
- 睡眠呼吸暂停、日间嗜睡、疲劳、驾驶/工作安全、心血管风险和照护者观察。
- 供应商、医保合规、依从记录、设备数据、隐私和远程监测接口。
- 与睡眠、呼吸、家庭医疗设备、备用电、召回和医疗服务连续性的接口。

## Human Infra 链路

```text
PAP 设备运行连续
  -> 主体夜间呼吸支持和睡眠恢复更稳定
  -> 面罩、耗材、供电、召回和供应商断点造成的治疗中断下降
  -> 日间警觉、认知、驾驶/工作安全和长期恢复能力增强
  -> 有效时间、风险控制和未来选择权提高
```

## 非目标

- 不提供睡眠呼吸暂停诊断、PAP 处方、压力参数、面罩选择、清洁步骤、设备购买、维修、召回个案或保险申诉建议。
- 不替代睡眠医生、呼吸治疗师、DME 供应商、NHLBI、CMS、FDA 或设备说明。
- 不把设备依从性简化为意志问题；面罩适配、费用、供电、隐私、召回和供应商接口必须纳入。

## Source Signals

- Medicare CPAP Devices: https://www.medicare.gov/coverage/continuous-positive-airway-pressure-devices
- CMS CPAP Devices and Accessories: https://www.cms.gov/training-education/medicare-learning-networkr-mln/compliance/medicare-provider-compliance-tips/cpap-devices-accessories

## 下一步

- 建立 `PAP device state -> mask/supply/power/provider dependency -> sleep recovery -> daytime function` 变量表。
- 区分居家、旅行、停电、召回、依从记录、隐私和长期供应商维护场景。
- 与 `sleep-disordered-breathing-screening-treatment-continuity`、`home-oxygen-respiratory-equipment-supply-continuity` 和 `refrigerated-medication-medical-device-power-outage-continuity` 建立边界。
