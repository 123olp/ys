# Surgical Anesthesia Perioperative Safety

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/surgical-anesthesia-perioperative-safety` |
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

手术、麻醉与围手术期安全域研究：当主体需要通过侵入性干预修复疾病、创伤或器官功能时，手术系统、麻醉安全、围手术期管理、团队检查和并发症预防如何决定修复是否变成新的风险。

## 对象

- 手术安全、麻醉安全、围手术期风险、术前评估、术中监测、术后恢复和并发症预防。
- WHO Surgical Safety Checklist、团队沟通、time-out、手术部位感染、出血、血栓、气道、用药错误和设备准备。
- 手术容量、麻醉人力、无菌流程、血液供应、ICU/恢复室、低资源环境手术安全。
- 选择性手术、急诊手术、创伤手术、产科手术、儿童/老年/多病共存人群手术风险。
- 手术与麻醉对死亡风险、功能恢复、疼痛、失能时间、医疗信任和未来选择权的影响。

## Human Infra 价值

很多医学修复必须穿过手术和麻醉这条高风险通道。围手术期安全域把“高强度修复工具是否被安全组织和执行”纳入主体持续性模型，避免只把手术看成治疗，而忽视它自身的系统风险。

```text
手术和麻醉过程被标准化、监测和团队化
  -> 可预防并发症、错误和围手术期死亡下降
  -> 修复性干预更能转化为功能恢复
  -> 主体行动能力和未来治疗窗口提高
```

## 边界

本域只整理公开手术安全、麻醉安全、围手术期质量、团队检查和系统治理资料。

不提供：

- 个体手术选择、麻醉选择、术前准备、术后护理、用药、禁食、康复或医疗建议。
- 手术操作、麻醉操作、插管、止血、缝合、器械使用、无菌操作或并发症处理步骤。
- 医院/医生选择、风险承诺、法律责任、纠纷、保险、费用或第二意见建议。
- 绕过手术安全流程、虚假记录、规避检查、无证操作或危险训练材料。

## 上游与下游

- 上游：`healthcare-access-continuity/`、`patient-safety-organizational-learning/`、`sterilization-disinfection-infection-control/`、`blood-organ-tissue-biovigilance-transplantation/`。
- 下游：`rehabilitation-functioning/`、`pain-suffering-control/`、`medical-device-equipment-safety-maintenance/`、`clinical-laboratory-diagnostic-quality/`。

## 初始资料线索

- WHO Surgical Safety Checklist resources。
- WHO safe surgery and patient safety resources。
- World Federation of Societies of Anaesthesiologists patient safety resources。
- AHRQ surgical safety and perioperative resources。
