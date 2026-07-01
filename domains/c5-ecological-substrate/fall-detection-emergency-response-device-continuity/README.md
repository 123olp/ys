# Fall Detection Emergency Response Device Continuity

`fall-detection-emergency-response-device-continuity` 研究跌倒检测、个人紧急响应设备、传感器、按钮、佩戴/充电、蜂窝/网络连接、误报漏报、照护者通知和 911/EMS 连接如何影响独居、老年、残障和高跌倒风险主体的求助连续性。

> 核心问题：跌倒后的关键不是设备存在，而是事件被发现、信号被传出、联系人能响应、服务能到达；任何一环断裂都会把可救助事件变成长时间无人发现。

## 关注对象

- 跌倒检测设备、个人紧急响应按钮、床椅传感器、穿戴设备、充电、电池、网络连接、照护者通知和 EMS/911 连接。
- 误报、漏报、设备未佩戴、隐私、监控疲劳、照护者负担和服务响应时间。
- 独居老人、残障主体、术后恢复、认知衰退、家庭照护、长期照护机构和灾害通信断点。
- 与跌倒预防、家庭安全、应急通信、照护网络和医疗警报设备治理的接口。

## Human Infra 链路

```text
跌倒检测与紧急响应设备连续
  -> 主体在跌倒或急性失能后更可能被及时发现
  -> 佩戴、供电、连接、通知和响应链断点下降
  -> 长时间无人救助、并发损伤和照护者不确定性减少
  -> 安全感、独立生活、关系支持和未来选择权增强
```

## 非目标

- 不提供设备选购、品牌推荐、安装配置、急救指令、医学分诊、911 使用建议、监控方案或机构采购建议。
- 不替代 CDC、NIA、FDA、EMS、照护计划、家庭安全评估或医疗专业人员。
- 不把跌倒检测替代为跌倒预防；它只处理跌倒发生后的发现、通知和响应链。

## Source Signals

- CDC Older Adult Falls: https://www.cdc.gov/falls/about/index.html
- FDA Fall Prevention Alarm: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpcd/classification.cfm?id=PJO

## 下一步

- 建立 `event detection -> device power/connectivity -> notification routing -> response arrival -> outcome` 变量表。
- 区分居家独居、认知衰退、长期照护、术后恢复、灾害通信和误报疲劳场景。
- 与 `fall-risk-prevention-home-safety-continuity`、`emergency-contact-next-of-kin-notification-continuity` 和 `emergency-alerts-communications` 建立边界。
