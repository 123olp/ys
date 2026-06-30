# ECMO Extracorporeal Life Support Continuity

`ecmo-extracorporeal-life-support-continuity/` 研究 ECMO/ECLS、体外循环支持、心肺桥接、中心容量、转运、并发症和退出策略如何把极端心肺衰竭转化为可等待恢复或移植的窗口。

> 核心问题：ECMO 是把主体从心肺功能临界失败中暂时外接出来的桥接技术。它的价值不在“神奇救命”，而在能否安全买到恢复、治疗或下一步决策的时间。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 心肺衰竭可能让主体在常规支持失败后终止
  -> ECMO 可临时替代部分心肺功能并争取恢复或转归窗口
  -> 但它依赖中心经验、抗凝、并发症控制、转运和退出条件
  -> 因此 ECMO 是极端器官支持和等待窗口工程的高风险域
```

## 关注对象

- VV/VA ECMO、ECLS center、indication governance、complication, anticoagulation risk, transport, bridge-to-recovery, bridge-to-transplant, withdrawal/exit。
- 与 `mechanical-ventilation-respiratory-failure-continuity/` 的关系：ECMO 可用于部分呼吸衰竭的升级支持。
- 与 `future-waiting/` 的概念关系：ECMO 是现实医学中的短期“等待恢复/治疗窗口”，但不是未来等待或永生方案。

## Human Infra 模型链路

```text
ECMO / ECLS T
  -> 改变心肺支持、氧合、灌注、抗凝、中心经验和退出变量 X
  -> 改变极端衰竭中的存活窗口、并发症和可恢复状态 S
  -> 改变死亡、出血、血栓、感染、神经损伤和长期失能风险 λ(t)
  -> 影响主体能否从极端器官失败中保留未来选择权
```

## 非目标

- 不提供 ECMO 适应证、禁忌证、抗凝、转运、设备、撤机、预后或个体医疗建议。
- 不生成中心选择、转院策略、家属决策、伦理判断或替代临床团队的内容。
- 不收集 ECMO 个案、参数、影像、血液数据、转运信息、费用或病历资料。

## Source Signals

- Extracorporeal Life Support Organization: https://www.elso.org/
- ELSO Guidelines: https://www.elso.org/ecmo-resources/elso-ecmo-guidelines.aspx
- NIH ECMO overview: https://www.nhlbi.nih.gov/health/ecmo

## 下一步

- 建立 ECLS Bridge Card：support mode, center capacity, complications, bridge target, exit path, neurological outcome。
- 与 `mechanical-ventilation-respiratory-failure-continuity/`、`intensive-care-organ-support-delirium-continuity/` 和 `transfusion-blood-management-hemorrhage-continuity/` 建立接口。
