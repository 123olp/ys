# Telehealth Remote Monitoring Access

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/telehealth-remote-monitoring-access` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 主要把科学、医疗、数据、制度或技术从潜在能力转成真实可用路径。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

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

`telehealth-remote-monitoring-access/` 研究远程医疗、虚拟照护、远程患者监测、居家设备、覆盖规则和数字照护连续性。

> 核心问题：医疗并不必然发生在固定诊室；主体能否跨越距离、行动限制、慢病随访和居家照护断点，取决于远程照护是否可达、可信、可升级并有临床责任边界。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 风险发现、随访和照护不能只依赖线下到院能力
  -> 远程问诊、远程监测、居家设备和升级路径必须可用且可治理
  -> 医疗服务才能跨越距离、行动限制和慢病连续性断点
```

## 关注对象

- 远程问诊、远程患者监测、虚拟随访、居家设备、数据回传和服务升级路径。
- 农村可及、行动受限、慢病管理、覆盖规则、隐私、安全、数字能力和设备可靠性。
- 与 `healthcare-access-continuity/`、`patient-data-interoperability/`、`digital-inclusion-connectivity/` 和 `measurement-feedback/` 的交叉。

## Human Infra 模型链路

```text
远程医疗与居家监测基础设施
  -> 改变距离成本、随访频率、监测可见性、服务升级和居家照护能力
  -> 改变疾病管理、风险识别、恢复反馈和医疗接入状态
  -> 降低失访、延误、慢病失控、交通摩擦和居家风险不可见
  -> 增强健康寿命、有效时间和照护连续性
```

## 非目标

- 不提供远程诊断、分诊、治疗方案、设备选择、保险报销或具体服务推荐。
- 不把远程监测数据写成自动诊断或急诊替代。
- 不背书任何数字健康产品、设备、应用、平台或服务可用性。

## Source Signals

- Telehealth.HHS.gov: https://telehealth.hhs.gov/
- HHS Telehealth and Remote Patient Monitoring: https://telehealth.hhs.gov/providers/best-practice-guides/telehealth-and-remote-patient-monitoring
- HRSA Telehealth: https://www.hrsa.gov/telehealth
- CMS Telehealth: https://www.cms.gov/medicare/coverage/telehealth
- FDA Digital Health Center of Excellence: https://www.fda.gov/medical-devices/digital-health-center-excellence

## 下一步

- 建立远程照护变量表：服务可达、设备可达、数据质量、升级路径、覆盖、隐私、数字能力和临床责任。
- 与 `healthcare-access-continuity/` 拆分线下服务连续性边界，与 `digital-inclusion-connectivity/` 拆分宽带/设备通用接入边界。
- 整理 telehealth、RPM、数字健康监管和支付覆盖资料的 Source Cards。
