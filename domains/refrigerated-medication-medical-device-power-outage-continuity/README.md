# Refrigerated Medication Medical Device Power Outage Continuity

`refrigerated-medication-medical-device-power-outage-continuity/` 研究停电、冷链中断、温控药品、居家医疗设备和电力依赖主体如何影响治疗连续性。

> 核心问题：停电对健康的影响不只来自照明和通信，更来自药物温控、设备供电、处方替代、供应联络和临床判断无法及时完成。

## 先验位置

```text
主体要持续被治疗
  -> 必须让关键药品和医疗设备在停电中保持可用
  -> 冷链、设备供电、处方信息和临床联络任一断裂都会放大风险
  -> 因而停电中的药物设备连续性是慢病主体的生命支持接口
```

## 关注对象

- 胰岛素等温控药品、冷藏药物、家庭医疗设备、充电设备、备用电、处方信息、供应商联络和停电时的医疗服务入口。
- 糖尿病患者、氧疗/呼吸设备用户、透析或输注设备用户、居家照护者、老年人和电力依赖医疗设备用户。

## Human Infra 模型链路

```text
药物设备停电连续性系统 T
  -> 改变药物温控、设备供电、处方资料、供应联络和临床替代变量 X
  -> 改变主体治疗可执行状态 S
  -> 改变低/高血糖、呼吸恶化、治疗中断、住院、药物失效和延迟求助风险 λ(t)
  -> 改变慢病稳定性、有效时间和灾后恢复能力
```

## 非目标

- 不提供药物是否可用判断、冷藏时间、剂量调整、设备接线、备用电配置、处方替代或医疗建议。
- 不收集诊断、药品名、设备型号、处方、供应商、停电地址、血糖/生命体征或医疗记录。

## Source Signals

- FDA emergency preparedness for medicines and medical devices: https://www.fda.gov/drugs/emergency-preparedness-drugs/emergency-preparedness-medicines
- HHS emPOWER Program materials: https://empowerprogram.hhs.gov/
