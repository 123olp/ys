# Emergency Alerts Communications

`emergency-alerts-communications/` 研究公共预警、应急通信、911/NG911、天气广播、移动警报和第一响应通信如何保护主体免于低频高冲击事件。

> 核心问题：灾害和急症发生时，主体首先需要收到可信警报、理解风险、联系求助入口，并让响应系统找到自己；通信断裂会把可响应风险变成不可逆伤害。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须能在灾害、事故、暴力、疾病和环境极端中收到预警并求助
  -> 预警、911、NG911、天气广播和第一响应通信构成危机时的行动接口
  -> 警报失败、通信失败、位置失败或误报会放大生命风险和恢复成本
  -> 因此应急预警与通信是主体持续性的危机入口域
```

## 关注对象

- FEMA IPAWS、Wireless Emergency Alerts、Emergency Alert System、NOAA Weather Radio、911、NG911 和 FirstNet。
- 警报到达率、可理解性、定位、冗余通信、无障碍、语言可达和误报/漏报治理。
- 与 `emergency-preparedness-response/` 的边界：本域专注预警与通信入口；应急准备与响应覆盖更广泛的准备、医疗、安置和恢复。

## Human Infra 模型链路

```text
应急预警通信系统 T
  -> 改变警报到达、理解、定位、求助、冗余通信和响应协调变量 X
  -> 改变主体在危机中的可响应状态 S
  -> 改变伤害、延误、失联、撤离失败和救援失败风险 λ(t)
  -> 影响生存概率、恢复窗口、家庭连续性和未来选择权
```

## 非目标

- 不提供实时应急指挥、撤离路线、急救操作、无线电操作、调度替代或公共警报发布方法。
- 不支持伪造警报、干扰通信、冒充响应人员、滥用 911 或绕过官方系统。
- 不把本域资料当作官方警报或现场安全判断。

## Source Signals

- FEMA IPAWS: https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system
- FCC Wireless Emergency Alerts: https://www.fcc.gov/consumers/guides/wireless-emergency-alerts-wea
- FCC Emergency Alert System: https://www.fcc.gov/emergency-alert-system
- NOAA Weather Radio: https://www.weather.gov/nwr/
- 911.gov: https://www.911.gov/
- NG911: https://www.911.gov/issues/ng911/
- FirstNet: https://www.firstnet.gov/

## 下一步

- 建立变量表：警报渠道、覆盖、理解、定位、冗余、响应互操作、误报、漏报和无障碍。
- 与 `emergency-preparedness-response/`、`digital-inclusion-connectivity/`、`language-access-plain-communication/` 和 `risk-engineering/` 拆分边界。
