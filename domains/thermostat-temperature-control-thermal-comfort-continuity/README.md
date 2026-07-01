# Thermostat Temperature Control Thermal Comfort Continuity

`thermostat-temperature-control-thermal-comfort-continuity` 研究温控器、设定点、传感器、自动化、占用模式、远程控制和误配置如何影响室内热舒适、睡眠、能耗和脆弱人群保护。

> 核心问题：供暖和制冷能力需要被温控系统转化为真实室内状态；温控错误会让能源、设备和健康目标之间发生冲突。

## 关注对象

- 传统温控器、可编程温控器、智能温控器、温度传感器、设定点、日程、远程控制和占用检测。
- 误配置、断网、权限共享、租房控制、能源节省目标、脆弱人群温度需求和极端天气。
- 睡眠、慢病、婴幼儿/老年照护、工作学习、能源账单和设备运行周期。
- 与供暖、制冷、能源负担、室内空气和家庭自动化安全的接口。

## Human Infra 链路

```text
温控器与室内温度控制连续
  -> 供暖制冷能力被稳定转译为可居住室内状态
  -> 过热、过冷、睡眠破坏、能耗冲突和远程误控风险下降
  -> 照护、学习、工作、恢复和慢病管理更稳定
  -> 主体有效时间和家庭运行韧性提高
```

## 非目标

- 不提供温控器安装、接线、设备购买、具体设定点处方、远程控制配置、能源账单优化或个案医疗建议。
- 不替代 HVAC 专业人员、能源援助、房东维修义务、医疗建议、消防/应急服务或设备厂商支持。
- 不把智能化本身视为目标；本域关注温控系统是否真实降低热风险和任务摩擦。

## Source Signals

- Energy Saver Thermostats: https://www.energy.gov/energysaver/thermostats
- Energy Saver Home Heating Systems: https://www.energy.gov/energysaver/home-heating-systems
- CDC Heat and Health: https://www.cdc.gov/heat-health/about/index.html

## 下一步

- 建立 `thermostat setting -> sensed indoor state -> occupant need -> task outcome -> continuity impact` 变量表。
- 区分传统温控、可编程温控、智能温控、租房权限、远程控制、断网和脆弱人群场景。
- 与 `home-heating-equipment-chimney-vent-maintenance-continuity`、`home-cooling-heat-pump-air-conditioning-maintenance-continuity` 和 `utility-affordability-shutoff-protection-continuity` 建立边界。
