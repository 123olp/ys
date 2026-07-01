# Emergency Medical Services Prehospital Care

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/emergency-medical-services-prehospital-care` |
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


急救医疗服务、院前照护与时间关键响应域研究：当主体面临创伤、心脏骤停、卒中、严重感染、呼吸衰竭或其他急性事件时，EMS、调度、救护车、院前分诊和转运如何决定可逆损伤是否被及时接住。

## 对象

- 911/急救呼叫、调度、EMS、救护车、急救人员、院前评估、现场稳定和目的医院选择。
- 心脏骤停、创伤、卒中、胸痛、呼吸急症、过敏反应、危重产科、儿科急症和公共卫生事件。
- 响应时间、覆盖区域、农村/城市差异、互操作通信、医疗指挥、数据反馈和质量改进。
- EMS 与急诊、创伤中心、卒中中心、公共安全、灾害响应和社区急救教育的接口。
- 院前照护对死亡风险、失能时间、恢复窗口、家庭稳定和系统信任的影响。

## Human Infra 价值

很多主体持续性风险不是慢慢发生，而是在几分钟到几小时内决定终局。急救医疗服务域把“急性事件是否能在可逆窗口内进入医疗系统”纳入主体持续性模型，补上医疗可及性中最时间敏感的一层。

```text
急性事件被及时发现、调度、稳定和转运
  -> 可逆损伤窗口被保住
  -> 死亡、失能和长期功能损失下降
  -> 主体恢复机会和家庭连续性提高
```

## 边界

本域只整理公开 EMS、院前照护系统、急救响应、质量改进、覆盖和政策资料。

不提供：

- 急救操作、医疗处置、用药、复苏步骤、创伤处理、分诊或现场指挥建议。
- 个体病情判断、是否呼叫急救、医院选择、转运路线、医疗法律或保险建议。
- 规避急救系统、滥用 911、伪造呼叫、干扰 EMS、跟踪救护车辆或危险现场进入方法。
- 灾害实时指挥、暴力现场应对、危险物处置或公共安全战术。

## 上游与下游

- 上游：`emergency-alerts-communications/`、`geospatial-navigation-location-infrastructure/`、`transportation-access-mobility/`、`health-workforce-capacity/`。
- 下游：`healthcare-access-continuity/`、`patient-safety-organizational-learning/`、`road-traffic-injury-prevention-safe-mobility/`、`risk-engineering/`。

## 初始资料线索

- NHTSA Office of EMS resources。
- EMS.gov resources。
- WHO emergency care system resources。
- CDC emergency medical services and public health resources。
