# Wearables Continuous Sensing Personal Informatics

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/wearables-continuous-sensing-personal-informatics` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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

- 界定被放大的通用能力资源：智力、注意力、记忆、学习、判断、执行、反馈或工具使用。
- 说明任务链路：能力变化如何改变问题求解、行动质量、创造密度或学习轮次。
- 识别复利结构：能力增强、工具采用、协作网络、经验积累和自我升级如何互相强化。
- 记录依赖条件：AI、数据、界面、训练、外部工具、社会支持或反馈系统。
- 列出误用、过载、依赖、幻觉、注意力破坏、人格边界和安全风险。

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

可穿戴、连续感知与个人信息学域研究：主体如何通过可穿戴设备、家庭传感器、移动设备和自我追踪系统连续观察状态，并把信号转化为反馈、预警、行为调整和照护协作。

## 对象

- 可穿戴设备、连续监测、移动健康、远程数据采集、个人信息学和自我追踪。
- 心率、睡眠、活动、血糖、血压、体温、呼吸、位置、跌倒、症状、用药和环境暴露信号。
- 传感器准确性、校准、缺失数据、误报漏报、算法偏差、临床效用和用户负担。
- 反馈闭环、风险预警、远程照护、个人实验、行为改变和长期状态建模。
- 数据隐私、过度量化、焦虑、误读、医疗化、平台依赖和证据等级边界。

## Human Infra 价值

没有观测，主体只能在风险已经显性化后被动反应。连续感知域把“身体和环境状态”变成可反馈的时间序列：更早发现偏移，更快修正行为，更稳定连接医疗、AI 和自我管理系统。

```text
主体状态被连续感知
  -> 风险偏移、恢复不足和行为反馈更早可见
  -> 主体更容易调整睡眠、活动、用药、照护和环境暴露
  -> 风险函数、有效寿命和长期行动能力获得更细粒度输入
```

## 边界

本域只整理公开的可穿戴、连续监测、个人信息学、远程数据采集、传感器质量和反馈系统资料。

不提供：

- 个体诊断、治疗、用药调整、急诊判断、设备选购、算法解释或个人健康预测建议。
- 将消费级传感器数据直接写成临床结论、死亡风险、寿命预测或保险/雇佣资格判断。
- 规避设备安全、隐私、安全认证、数据授权或平台条款的操作。
- 对具体设备、App、平台、算法或服务的背书。

## 上游与下游

- 上游：`measurement-feedback/`、`telehealth-remote-monitoring-access/`、`health-data-privacy-governance/`、`digital-inclusion-connectivity/`。
- 下游：`longevity-evidence/`、`sleep-circadian-recovery/`、`physical-activity-mobility/`、`cognitive-augmentation/`。

## 初始资料线索

- FDA Digital Health Technologies for Remote Data Acquisition in Clinical Investigations guidance.
- Personal informatics and lived informatics research literature.
- NIST and standards materials related to sensor measurement, calibration and data quality.
- Remote patient monitoring and digital health public materials.

## 下一步

- 建立连续感知变量表：测量对象、频率、准确性、校准、缺失、用户负担、反馈延迟、临床效用和隐私等级。
- 整理 Source Cards：FDA DHT、personal informatics、sensor validation、RPM 和数字健康证据边界。
- 区分“个人反馈信号”“研究数据”“临床监测”和“监管级证据”，避免证据等级混用。
