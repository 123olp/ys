# Home Service Provider Emergency Contact Directory Continuity

`home-service-provider-emergency-contact-directory-continuity` 研究家庭服务联系人、物业/房东、公用事业、维修服务、医疗设备供应商、邻里支持和应急热线目录如何影响家庭故障、灾害、失能和临时照护中的恢复连续性。

> 核心问题：家庭事故和维修恢复常常不是缺知识，而是找不到正确责任方、热线、账户入口、物业联系人、设备供应商或可信服务路径；联系人目录是家庭系统从“知道问题”走向“能发起恢复”的接口。

## 关注对象

- 房东/物业、HOA、燃气/电力/水务/通信公司、plumber/electrician/HVAC、家电维修、医疗设备供应商、保险、毒物中心、非紧急公共服务和邻里支持联系人。
- 联系方式、服务范围、账户/地址引用口径、营业时间、紧急与非紧急边界、授权联系人和更新周期。
- 老年照护、残障支持、短期离家、儿童看护、租房、灾害恢复和家庭托管场景。
- 与家庭应急通信、维修承包商、应急财务文件、医疗设备连续性和家庭运行地图的接口。

## Human Infra 链路

```text
家庭服务联系人目录可用
  -> 故障、事故、照护中断或灾后恢复时能快速找到责任入口
  -> 错误拨打、重复解释、延迟排程、服务诈骗和责任推诿摩擦下降
  -> 水电热网、设备、住房、医疗耗材和照护支持更快恢复
  -> 家庭从单人记忆驱动转化为可交接的服务网络
```

## 非目标

- 不推荐具体服务商、价格、合同、理赔路径、维修方案、投诉策略、法律意见或个案应急决策。
- 不收集真实联系人、地址、账户、门禁、家庭成员、医疗设备供应商或服务合同资料。
- 不替代 911、消防、燃气公司、毒物中心、物业、房东、持证专业人员、保险或消费者保护机构。

## Source Signals

- Ready.gov Make a Plan: https://www.ready.gov/plan
- FTC Home Improvement Scams: https://consumer.ftc.gov/articles/how-spot-avoid-and-report-home-improvement-scams
- Poison Help: https://www.poisonhelp.org/

## 下一步

- 建立 `service directory -> responsible contact -> restoration initiation -> continuity outcome` 变量表。
- 区分紧急热线、非紧急服务、物业/房东、医疗设备供应商、保险和邻里支持。
- 与 `family-emergency-communication-reunification-continuity`、`household-maintenance-repair-contractor-continuity` 和 `emergency-financial-document-cash-readiness-continuity` 建立边界。
