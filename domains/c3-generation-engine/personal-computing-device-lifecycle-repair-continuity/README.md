# Personal Computing Device Lifecycle Repair Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/personal-computing-device-lifecycle-repair-continuity` |
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

`personal-computing-device-lifecycle-repair-continuity` 研究个人手机、电脑、平板、外设和本地存储设备的采购、维修、替换、备件、数据迁移、保修、远程锁定和报废如何影响主体的数字行动连续性。

> 核心问题：主体的大量任务已经通过个人计算设备完成；设备失效、不可维修或无法迁移数据，会把账号、资料、工作流和恢复通道同时切断。

## 关注对象

- 手机、电脑、平板、外设、充电器、本地硬盘、备份盘、安全密钥和关键配件。
- 维修权、备件可得性、保修、维修文档、授权维修、二手设备、设备锁定、MDM 和远程擦除。
- 数据迁移、设备替换、加密磁盘恢复、旧设备交接、报废擦除和电子废弃物。
- 设备不可用、供应中断、维修成本过高、平台停止支持、配件断供和本地资料丢失。

## Human Infra 链路

```text
个人计算设备生命周期可维修
  -> 本地计算、通信、认证、资料访问和任务执行入口保持可用
  -> 设备故障、停产、锁定和迁移失败造成的行动中断下降
  -> 学习、工作、医疗、金融、创作和协作系统可持续接入
  -> 主体数字行动能力和有效时间增强
```

## 非目标

- 不提供绕过设备锁、破解加密、规避 MDM、盗取数据、拆机攻击、保修欺诈或维修操作指导。
- 不替代厂商、授权维修、数据恢复服务、消费者保护机构、IT 管理员或法律建议。
- 不收集序列号、设备指纹、密码、恢复密钥、定位记录、企业管理配置或私人文件。

## Source Signals

- FTC right to repair and repair restriction materials: https://www.ftc.gov/
- iFixit / manufacturer public repair documentation as implementation examples.
- NIST media sanitization and endpoint security references: https://www.nist.gov/
- EPA electronics recycling and e-waste resources: https://www.epa.gov/

## 下一步

- 建立 `device -> repairability -> support window -> data migration -> action continuity` 变量表。
- 区分个人设备、工作设备、学校设备、受管设备和医疗辅助设备的所有权边界。
- 与 `digital-inclusion-connectivity`、`password-manager-secret-vault-continuity`、`cloud-backup-file-sync-data-portability-continuity` 和 `long-term-digital-preservation-format-migration` 建立边界。
