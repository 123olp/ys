# Household Hazardous Waste Chemical Disposal Continuity

`household-hazardous-waste-chemical-disposal-continuity` 研究家庭危险废物、清洁剂、油漆、溶剂、农药、汽车化学品、易燃品和地方 HHW 回收日如何影响中毒、火灾、污染、儿童安全和居住卫生。

> 核心问题：家庭危险废物不是普通垃圾；当有毒、腐蚀、易燃或反应性材料没有安全的识别、暂存和处置入口时，居住空间会积累低频高后果风险。

## 关注对象

- 家庭危险废物、清洁化学品、油漆、溶剂、农药、汽车用品、含汞物品、易燃材料和未知旧容器。
- HHW drop-off、回收日、地方收集点、标签可读性、儿童接触、火灾风险、下水道/土壤/空气污染风险。
- 租房搬家、老人家庭、车库/地下室储存、多语种标签、灾后清理和物业集中处置场景。
- 与毒物控制、家庭清洁、农药标签、危险材料事故、非法倾倒和灾后废弃物清理的接口。

## Human Infra 链路

```text
家庭危险废物与化学处置连续
  -> 有毒、腐蚀、易燃或反应性家庭材料被识别并进入合规处置入口
  -> 中毒、火灾、儿童接触、下水道污染和非法混入风险下降
  -> 储藏、清洁、维修、搬家和灾后恢复任务不被危险材料拖累
  -> 主体居住安全、恢复速度和风险治理能力提高
```

## 非目标

- 不提供化学品混合、处理、稀释、燃烧、倾倒、下水道排放、危险废物运输、现场清理或容器打开教程。
- 不替代地方 HHW 项目、消防部门、毒物控制中心、EPA/RCRA 规则、物业、危险废物承包商、公共卫生或环境执法渠道。
- 不判断某个未知容器、泄漏、气味、暴露、火灾或儿童接触事件应如何个案处置。

## Source Signals

- EPA Household Hazardous Waste: https://www.epa.gov/hw/household-hazardous-waste-hhw
- Poison Help: https://www.poisonhelp.org/
- EPA Recycling Basics and Benefits: https://www.epa.gov/recycle/recycling-basics-and-benefits

## 下一步

- 建立 `chemical waste type -> hazard class -> access pathway -> exposure/fire/pollution risk -> continuity outcome` 变量表。
- 区分油漆、溶剂、农药、汽车用品、含汞物品、未知旧容器、搬家清空和灾后清理场景。
- 与 `chemical-safety-poison-control-toxicology`、`pesticide-label-exposure-poison-control-continuity`、`waste-management-hazardous-materials-continuity` 建立边界。
