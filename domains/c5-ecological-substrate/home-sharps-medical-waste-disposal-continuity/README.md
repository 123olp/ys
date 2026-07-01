# Home Sharps Medical Waste Disposal Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-sharps-medical-waste-disposal-continuity` |
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


`home-sharps-medical-waste-disposal-continuity` 研究家庭针头、注射器、采血针、自动注射器、锐器容器、drop box、mail-back 和照护场景中的针刺伤、感染暴露、儿童接触和清洁人员风险。

> 核心问题：居家医疗把一部分医疗废物带入家庭；如果锐器没有安全容器和处置路径，治疗连续性会把家庭成员、照护者、清洁人员和收运人员暴露在针刺与感染风险中。

## 关注对象

- 家庭针头、注射器、采血针、胰岛素笔针、自动注射器、输液相关锐器和宠物医疗锐器。
- FDA-cleared sharps disposal containers、临时容器边界、社区 drop box、mail-back、药房/医疗机构回收和地方规则差异。
- 糖尿病、注射药物、过敏自救、激素治疗、居家护理、儿童/认知障碍家庭和清洁/收运人员暴露风险。
- 与药品处置、DME 供应、糖尿病耗材、居家照护、废弃物收运和感染预防的接口。

## Human Infra 链路

```text
家庭锐器与医疗废物处置连续
  -> 居家治疗产生的针头和锐器进入清晰容器与合规处置路径
  -> 针刺伤、感染暴露、儿童接触和收运人员风险下降
  -> 注射治疗、居家照护、糖尿病管理和清洁任务可以持续
  -> 主体治疗连续性、家庭安全和照护韧性提高
```

## 非目标

- 不提供注射、针具重复使用、锐器压缩、容器改造、医疗废物运输、感染暴露处理、职业暴露报告或个案医疗建议。
- 不替代 FDA、地方卫生部门、药房、医疗机构、DME 供应商、感染控制、职业安全、毒物/急救或应急服务。
- 不判断某个针刺伤、暴露、锐器容器、医疗废物袋、宠物针具或地方 drop-off 规则应如何具体处理。

## Source Signals

- FDA Sharps Disposal Containers: https://www.fda.gov/medical-devices/safely-using-sharps-needles-and-syringes-home-work-and-travel/sharps-disposal-containers
- CDC Injection Safety: https://www.cdc.gov/injection-safety/

## 下一步

- 建立 `home sharps stream -> container/pathway state -> exposure risk -> treatment task -> continuity outcome` 变量表。
- 区分糖尿病、过敏自救、激素治疗、宠物医疗、居家护理、儿童家庭和多户住宅场景。
- 与 `diabetes-insulin-glucose-monitoring-supplies-continuity`、`unused-medicine-takeback-disposal-continuity`、`waste-management-hazardous-materials-continuity` 建立边界。
