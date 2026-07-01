# Household Operating Map Handoff Continuity

`household-operating-map-handoff-continuity` 研究家庭运行地图、关键位置、日常流程、照护任务、设备依赖、供应位置、宠物/儿童/老人交接和临时代理说明如何影响家庭从单人掌控转向多人可接手的连续性。

> 核心问题：很多家庭能运转，是因为一个人记住了“所有东西在哪里、谁负责什么、坏了找谁、什么时候做什么”；当这个人出差、生病、失能、死亡或灾害中断时，家庭任务会因为隐性知识消失而坍塌。

## 关注对象

- 家庭运行地图、关键位置索引、服务联系人、供应品位置、设备依赖、日常例行、宠物/儿童/老人照护交接、药品/医疗设备资料边界和离线备份。
- 照护者交接、house-sitting、临时离家、住院、灾害撤离、远程家庭管理、共同居住和死亡后事务过渡。
- 家庭资料如何在隐私、安全和最小必要原则下支持代理执行，而不是变成监控或过度数据收集。
- 与应急文件、家庭通信计划、服务联系人目录、设备记录、关断位置标识和后死亡交接的接口。

## Human Infra 链路

```text
家庭运行知识显性化
  -> 日常任务、关键位置、责任入口和照护流程不再依赖单点记忆
  -> 临时代理、家庭成员、照护者和恢复人员能接手必要任务
  -> 失能、住院、旅行、灾害、死亡和照护交接造成的家庭系统断裂下降
  -> 家庭从个人经验系统转化为可交接、可恢复、可协作的基础设施
```

## 非目标

- 不提供家庭监控、定位追踪、儿童/伴侣控制、详细安防资料、门禁共享、医疗处方、法律/遗产建议、个案照护计划或个人资料模板。
- 不收集家庭成员、住址、门禁、钥匙位置、资产、药品、账户、设备序列号、联系人或照护对象资料。
- 不替代家庭应急计划、医疗代理、法律文件、物业管理、照护评估、专业社工或应急服务。

## Source Signals

- Ready.gov Make a Plan: https://www.ready.gov/plan
- Ready.gov Financial Preparedness: https://www.ready.gov/financial-preparedness
- FEMA Emergency Financial First Aid Kit: https://www.fema.gov/emergency-financial-first-aid-kit

## 下一步

- 建立 `implicit household knowledge -> operating map ->代理执行/交接 -> continuity outcome` 变量表。
- 区分最小必要资料、敏感资料、离线备份、更新责任、访问权限和销毁/撤权边界。
- 与 `emergency-financial-document-cash-readiness-continuity`、`family-emergency-communication-reunification-continuity`、`home-service-provider-emergency-contact-directory-continuity` 和 `estate-inventory-asset-liability-handoff-continuity` 建立边界。
