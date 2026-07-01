# Diabetic Retinopathy Screening Treatment Continuity

`diabetic-retinopathy-screening-treatment-continuity/` 负责整理糖尿病视网膜病变、眼底筛查、黄斑水肿、治疗衔接和糖尿病视觉并发症连续性。

核心问题：

> 糖尿病视网膜病变把代谢控制、筛查系统、眼科治疗和视觉功能串成一条链；任何一段断裂，都会把可管理风险转化为不可逆视觉损害。

## 先验位置

```text
主体持续性最大化
  -> 主体必须同时维护代谢状态和感官输入
  -> 糖尿病会通过微血管损伤影响视网膜和黄斑功能
  -> 筛查缺失、随访失败或治疗延迟会放大可预防视觉损失
  -> 因此糖尿病视网膜病变连续性是代谢-视觉交叉基础设施
```

## 关注对象

- 糖尿病视网膜病变、糖尿病黄斑水肿、眼底筛查、影像转诊和眼科治疗衔接。
- 糖尿病管理、初级保健、眼科服务、远程眼底筛查和结果追踪。
- 视觉损害对工作、驾驶、用药自理、血糖监测和生活独立性的影响。
- 与 `diabetes-insulin-glucose-monitoring-supplies-continuity/` 的关系：本域关注糖尿病视觉并发症和眼科链路。

## Human Infra 模型链路

```text
糖尿病眼底筛查 / 眼科随访 / 治疗衔接 T
  -> 改变视网膜病变发现时间、黄斑状态、转诊延迟和治疗连续性变量 X
  -> 改变主体视觉功能、糖尿病自我管理和工作生活状态 S
  -> 改变严重视损、失明、照护依赖、任务失败和医疗复杂度风险
  -> 保护有效时间、自我管理能力和未来选择权
```

## 非目标

- 不提供糖尿病视网膜病变诊断、眼底图判读、注射/激光/手术建议或糖尿病用药调整。
- 不根据眼底筛查结果输出个人风险等级、治疗优先级、复查间隔或医疗机构选择。
- 不把 AI 眼底筛查或远程筛查写成替代眼科评估的完整方案。

## Source Signals

- National Eye Institute Diabetic Retinopathy: https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/diabetic-retinopathy
- CDC Diabetes and Vision Loss: https://www.cdc.gov/diabetes/diabetes-complications/diabetes-and-vision-loss.html
- CDC Vision Health: https://www.cdc.gov/vision-health/

## 下一步

- 建立糖尿病视网膜病变 Source Card，区分筛查、转诊、治疗、随访和主体功能终点。
- 对接糖尿病供应、慢病随访、临床影像和医疗可及性域。
