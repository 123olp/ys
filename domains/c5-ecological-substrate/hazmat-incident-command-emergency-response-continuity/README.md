# Hazmat Incident Command Emergency Response Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/hazmat-incident-command-emergency-response-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->


`hazmat-incident-command-emergency-response-continuity/` 研究危险材料事故中指挥体系、跨机构协作、消防/EMS/公共卫生/环境部门接口和公众服务连续性如何降低响应混乱。

> 核心问题：危险材料事故不是单一专业问题；如果现场指挥、公共沟通、医疗转运、环境监测和恢复系统无法协同，风险会在组织边界之间扩散。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体面对事故时依赖多个机构同时工作
  -> 危险材料事故跨越消防、医疗、执法、环境、交通和公共卫生
  -> 事故指挥与应急响应连续性把多机构行动编排成可理解、可交接、可恢复的系统
```

## 关注对象

- NIMS/ICS、HazMat 事件指挥、统一指挥、跨机构通信、公众信息、转运和恢复交接。
- 指挥混乱、职责重叠、通信失败、资源调度延迟、现场与社区风险沟通断裂。
- 与 `emergency-preparedness-response/` 的关系：上位应急域关注总体准备；本域聚焦危险材料事故指挥和跨机构执行链。

## Human Infra 模型链路

```text
HazMat 事件指挥
  -> 改变跨机构协作、资源调度、公众沟通和转运恢复能力
  -> 改变暴露控制、救援延迟、医疗挤兑和社区恢复风险
  -> 增强事故中的主体生存、服务接续和社会信任
```

## 非目标

- 不提供现场指挥、战术部署、隔离距离、去污步骤、消防操作或化学品处置方法。
- 不提供执法、责任认定、企业合规、设施安全测试或事件模拟攻击。
- 不替代本地应急部门、消防、EMS、公共卫生或环境监管机构。

## Source Signals

- FEMA National Incident Management System: https://www.fema.gov/emergency-managers/nims
- FEMA Incident Command System resources: https://training.fema.gov/emiweb/is/icsresource/
- PHMSA Emergency Response Guidebook: https://www.phmsa.dot.gov/hazmat/erg/emergency-response-guidebook-erg
- U.S. Fire Administration hazardous materials resources: https://www.usfa.fema.gov/

## 下一步

- 建立 HazMat Response Interface Card：command, agencies, public information, medical transfer, environmental monitoring, recovery handoff。
- 与 `emergency-alerts-communications/`、`emergency-medical-services-prehospital-care/`、`public-health-laboratory-diagnostic-capacity/` 和 `disaster-recovery-relief-continuity/` 建立接口。
