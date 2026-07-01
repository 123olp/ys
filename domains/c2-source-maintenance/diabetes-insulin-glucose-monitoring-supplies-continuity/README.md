# Diabetes Insulin Glucose Monitoring Supplies Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/diabetes-insulin-glucose-monitoring-supplies-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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


## 定位

本域研究胰岛素、注射器/笔针、泵耗材、血糖试纸、CGM、传感器、校准、冷藏、支付和供应中断如何影响糖尿病主体的日常风险控制和长期持续性。

它不是血糖管理、胰岛素剂量、饮食或设备设置建议入口。

## 先验问题

```text
慢病治疗何以日常可执行？
  -> 药物、耗材、监测设备和冷藏必须连续
  -> 支付、处方、供应商和设备生态必须同步
  -> 任何一个断点都会把可管理风险转成急性和长期损伤
```

## 研究对象

- 胰岛素、注射用品、泵 supplies、CGM、血糖仪、试纸、lancets 和传感器。
- Medicare diabetes supplies、DME / pharmacy benefit、copay、prior authorization 和供应商。
- 冷藏、旅行、灾害、短缺、设备失效和 refill 中断。
- 糖尿病教育、药房、内分泌照护和居家监测基础设施。

## 关键变量

- 胰岛素可得性、耗材连续天数、监测中断、传感器替换失败。
- 自付费用、coverage denial、处方续期、药房/DME 供应路径。
- 冷链中断、旅行限制、灾害断供和设备生态锁定。

## 证据入口

- Medicare diabetes equipment and supplies 资料。
- FDA insulin、glucose monitoring devices、recalls 和 safety communications。
- CDC diabetes、NIDDK 和糖尿病公共卫生资料。

## 非目标

- 不提供血糖目标、胰岛素剂量、饮食、运动、泵设置、CGM 解释或急救建议。
- 不判断某个设备、耗材、保险、处方或供应商个案。
- 不收集血糖数据、CGM 数据、胰岛素剂量、处方、设备序列号、保险或诊断资料。

## 上下游

- 上游：`endocrine-hormonal-regulation/`、`medicine-access-treatment-continuity/`、`durable-medical-equipment-supplier-repair-continuity/`。
- 下游：`home-refrigeration-food-storage-continuity/`、`healthcare-access-continuity/`、`measurement-feedback/`。
