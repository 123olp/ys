# Dental Pain Emergency Infection Continuity

`dental-pain-emergency-infection-continuity/` 负责整理牙痛、急性牙科事件、感染、急诊摩擦和任务中断。

核心问题：

> 急性牙痛会直接劫持注意力、睡眠、工作和照护；牙科感染则把可预防的口腔问题升级为急性系统风险。

## 先验位置

```text
主体持续性最大化
  -> 主体必须维持可承受疼痛、稳定睡眠和及时处理感染的能力
  -> 龋病、牙周病、创伤和修复失败可触发急性牙痛和感染
  -> 牙痛和感染会造成急诊使用、抗生素摩擦、缺勤和照护中断
  -> 因此牙科急性事件连续性是有效时间保护和风险升级阻断条件
```

## 关注对象

- 牙痛、牙源性感染、脓肿、面部肿胀、急诊就医和治疗延迟。
- 急诊系统、抗生素使用、止痛负担、睡眠中断、工作缺勤和照护责任冲突。
- 牙科可及性、预约等待、支付摩擦、低收入人群和农村地区服务缺口。
- 与 `pain-suffering-control/` 的关系：本域关注牙源性痛和感染路径；痛苦域关注整体痛苦负担。

## Human Infra 模型链路

```text
牙科急性事件服务 T
  -> 改变牙痛、感染控制、睡眠、急诊使用、支付摩擦和治疗延迟变量 X
  -> 改变主体急性风险和资源状态 S
  -> 改变缺勤、照护中断、感染扩散和慢性痛苦风险
  -> 增加有效时间、恢复能力和系统信任
```

## 非目标

- 不提供急诊分诊、抗生素、止痛药、剂量、排脓、拔牙或居家处理建议。
- 不根据症状、照片或影像判断感染严重程度。
- 不替代牙医、急诊、口腔颌面外科或公共卫生服务。

## Source Signals

- CDC Oral Health: https://www.cdc.gov/oral-health/
- NIDCR Tooth Decay: https://www.nidcr.nih.gov/health-info/tooth-decay
- NIDCR Gum Disease: https://www.nidcr.nih.gov/health-info/gum-disease

## 下一步

- 建立牙痛急性事件 Source Card，区分疼痛负担、感染升级和服务可及性。
- 与龋病、牙周病、牙科可及性和劳动连续性域建立交叉索引。
