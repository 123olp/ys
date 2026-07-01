# Robotics Embodied Assistance Care Automation

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/robotics-embodied-assistance-care-automation` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 主要放大主体学习、认知、工具使用和生成新路径的能力。 |
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

机器人、具身辅助与照护自动化域研究：主体如何通过机器人、自动化设备、外骨骼、家庭辅助系统和照护机器人获得移动、操作、陪护、监测、康复和日常任务支持。

## 对象

- 具身机器人、服务机器人、照护机器人、外骨骼、假肢、移动辅助、家庭自动化和远程操作。
- 日常生活活动、转移、取物、清洁、用药提醒、跌倒响应、康复训练、陪伴和照护者减负。
- 人机协作、安全标准、性能测量、可靠性、故障模式、可访问性、维护、成本和责任归属。
- 机器人对独立生活、长期照护、残障服务、康复、家庭照护和劳动力短缺的影响。
- 隐私、依赖、歧视、误操作、机械伤害、监控化、情感欺骗和服务中断风险。

## Human Infra 价值

有效永生不只是活得更久，还需要身体和环境能继续执行任务。机器人与具身辅助把外部工具从“信息增强”推进到“物理行动增强”：帮助主体移动、照护自己、与环境交互，并在能力下降时保留更多独立性。

```text
具身辅助和照护自动化可用
  -> 移动、操作、康复、监测和日常照护负担下降
  -> 主体独立生活、行动密度和照护连续性提高
  -> 长期执行能力和可持续创造窗口扩大
```

## 边界

本域只整理公开的机器人、具身辅助、照护自动化、外骨骼、服务机器人、安全标准和性能测量资料。

不提供：

- 设备选购、改装、维修、医疗康复处方、照护替代、临床训练或安全认证建议。
- 绕过机器人安全限制、监控他人、操控受照护者、自动化危险动作或规避责任的方案。
- 对具体机器人、外骨骼、照护平台、公司或投资方向的背书。
- 把机器人陪伴写成真实社会关系替代，或把自动化写成照护责任消失。

## 上游与下游

- 上游：`assistive-technology-access/`、`rehabilitation-functioning/`、`caregiving-long-term-care/`、`manufacturing-repair-capacity/`。
- 下游：`disability-services-independent-living/`、`home-health-hospice-palliative-care-continuity/`、`occupational-work-design/`、`cognitive-augmentation/`。

## 初始资料线索

- NIST robotics and robot performance measurement materials: https://www.nist.gov/el/robotics
- Assistive technology, rehabilitation robotics and service robotics standards literature.
- FDA and medical device public materials for robotic medical systems where applicable.
- Human factors, safety and reliability research for embodied human-robot interaction.

## 下一步

- 建立具身辅助变量表：任务类型、自由度、负载、错误率、故障模式、人工接管、维护周期、成本和隐私风险。
- 整理 Source Cards：NIST robotics、assistive robotics、exoskeletons、rehabilitation robots、service robots 和 safety standards。
- 区分辅助、医疗器械、照护服务、家庭自动化和工业自动化，避免责任边界混乱。
