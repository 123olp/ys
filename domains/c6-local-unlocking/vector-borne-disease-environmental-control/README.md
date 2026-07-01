# Vector Borne Disease Environmental Control

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/vector-borne-disease-environmental-control` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

病媒传播疾病与环境控制域研究：当主体持续性依赖稳定的居住、工作、旅行、农业和公共卫生环境时，蚊、蜱、蚤等病媒、气候变化、土地使用、水环境和控制系统如何改变感染风险。

## 对象

- 蚊媒、蜱媒、蚤媒和其他病媒传播疾病风险。
- 气候、降水、温度、水体、土地使用、城市化、住房质量、动物宿主和迁移旅行。
- 监测、预警、公共卫生响应、环境管理、病媒控制、疫苗/诊断/治疗可及性和社区沟通。
- 病媒控制中的农药使用、生态影响、抗药性、职业暴露和公平性问题。
- 慢性感染、急性感染、暴发、地方性传播、输入性病例和跨境治理。

## Human Infra 价值

病媒传播疾病说明，主体持续性不只取决于免疫系统，还取决于环境、动物、气候、住房和公共卫生网络。病媒控制做得不好，居住空间、工作空间和移动自由都会被感染风险重新定价。

```text
病媒与环境传播风险被监测和控制
  -> 感染、暴发、慢性后遗症和行动限制下降
  -> 居住、工作、旅行和农业活动更可持续
  -> 健康寿命、有效时间和未来选择权提高
```

## 边界

本域只整理病媒传播疾病、环境控制、公共卫生监测、生态治理和风险沟通资料。

不提供：

- 个体诊断、检测、治疗、疫苗选择、药物、旅行医学、暴露后处理或急救建议。
- 驱虫产品选择、农药配方、喷洒方法、害虫灭杀、现场采样、动物处理、居住/旅行路线或户外活动许可建议。
- 公共卫生报告规避、检疫规避、病媒释放、生态破坏、违规用药、危险化学品操作或监管规避方法。
- 把地图、病例数据、气候模型、虫媒监测或 AI 输出写成个体感染风险、旅行安全或资产价值结论。

## 上游与下游

- 上游：`animal-health-zoonotic-interface-one-health/`、`weather-climate-observation-forecasting/`、`water-resources-hydrology-flood-drought-management/`、`housing-built-environment-stability/`、`biodiversity-ecosystem-services-resilience/`。
- 下游：`immunization-public-health-surveillance/`、`chronic-infectious-disease-care-continuity/`、`healthcare-access-continuity/`、`occupational-exposure-industrial-hygiene/`、`migration-displacement-humanitarian-continuity/`。

## 初始资料线索

- CDC vector-borne disease resources。
- WHO vector-borne diseases resources。
- EPA mosquito control and pesticide resources。
- One Health, climate and public-health surveillance resources。
