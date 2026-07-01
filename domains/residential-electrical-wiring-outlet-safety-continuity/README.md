# Residential Electrical Wiring Outlet Safety Continuity

`residential-electrical-wiring-outlet-safety-continuity` 研究住宅电气线路、插座、延长线、断路器、GFCI/AFCI、老化线路和过载如何影响照明、通信、医疗设备、学习、烹饪和家庭安全。

> 核心问题：家庭电力不是抽象能源，而是通过线路、插座、保护装置和使用行为进入具体任务；电气故障会把日常工具系统转成火灾、触电和服务中断风险。

## 关注对象

- 住宅线路、插座、延长线、接线板、过载、断路器、GFCI、AFCI 和老化电气系统。
- 照明、冰箱、通信设备、医疗设备、学习设备、供暖/制冷设备和充电设备的电气依赖。
- 租房、老旧住房、多设备家庭、儿童家庭、行动受限者和灾后临时用电场景。
- 与备电、设备电池、家电维护、消防报警、CO 报警和住房维修的接口。

## Human Infra 链路

```text
住宅电气线路与插座安全连续
  -> 家庭任务设备获得稳定且受保护的用电接口
  -> 过载、短路、触电和火灾风险更早被识别
  -> 照明、通信、医疗设备、学习和恢复活动不被电气故障切断
  -> 主体行动密度、居住安全和恢复能力提高
```

## 非目标

- 不提供电工维修、接线、配电箱操作、GFCI/AFCI 安装、故障诊断、消防验收或个案住房安全建议。
- 不替代持证电工、当地建筑/电气规范、消防部门、房东维修义务、保险或应急服务。
- 不把“用电更多”视为正向指标；本域关注受保护、可维护、可审计的家庭电气执行条件。

## Source Signals

- USFA Appliance and Electrical Fire Safety: https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/appliance-and-electrical/
- Ready.gov Power Outages: https://www.ready.gov/power-outages
- NFPA Electrical Safety: https://www.nfpa.org/education-and-research/home-fire-safety/electrical

## 下一步

- 建立 `electrical interface -> protection state -> household task -> failure mode -> continuity outcome` 变量表。
- 区分老旧住房、租房、医疗设备、充电设备、儿童家庭和灾后临时用电场景。
- 与 `backup-power-battery-generator-safety-continuity`、`household-appliance-maintenance-repair-continuity`、`smoke-alarm-home-fire-escape-readiness-continuity` 建立边界。
