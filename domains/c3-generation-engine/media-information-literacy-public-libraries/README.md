# Media Information Literacy Public Libraries

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/media-information-literacy-public-libraries` |
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

`media-information-literacy-public-libraries/` 研究媒体与信息素养、公共图书馆、可信知识入口和社区学习空间如何支撑主体判断、学习、公共服务使用和社会参与。

> 核心问题：信息存在不等于主体能够判断、理解和使用；如果缺少信息素养、可信入口、馆员支持和公共知识空间，主体会在 AI 内容、谣言、复杂服务和证据噪声中失去行动能力。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须持续学习、判断和使用公共信息
  -> 现代任务依赖数字内容、媒体环境、公共服务材料和证据链
  -> 信息素养与公共图书馆降低寻找、理解、验证和使用信息的成本
  -> 判断环境失败会放大误导、服务排除、学习断点和公共参与失败
  -> 因此媒体信息素养与公共图书馆是主体认知基础设施域
```

## 关注对象

- 媒体与信息素养、事实核验、来源判断、信息搜索、公共信息获取和 AI 生成内容识别。
- 公共图书馆作为免费知识入口、数字技能支持、公共电脑、社区学习、服务转介和可信空间。
- 图书馆数据、馆藏、项目、访问、数字资源、数字鸿沟和社区信息服务。
- 与 `information-integrity-trust/` 的边界：本域关注主体如何获得判断能力和公共知识入口；信息完整性域关注信息环境和信任链本身。
- 与 `digital-inclusion-connectivity/` 的边界：本域关注知识与信息能力；数字包容关注连接、设备和可负担性。

## Human Infra 模型链路

```text
信息素养与公共图书馆 T
  -> 改变来源判断、搜索能力、数字技能、馆员支持、可信材料和公共知识入口变量 X
  -> 改变主体理解风险、完成任务、学习新技能和参与公共生活的状态 S
  -> 改变误导暴露、服务误解、学习失败、公共参与断线和技术采用错误风险 λ(t)
  -> 影响认知质量、行动正确率、有效时间和未来选择权
```

## 非目标

- 不提供宣传、舆论操控、微定向影响、平台规避、内容伪造或信息战策略。
- 不把图书馆写成医疗、法律、福利或危机服务的替代机构。
- 不把信息素养简化为个人责任，忽视平台、制度、教育、语言和可访问性条件。

## Source Signals

- UNESCO Media and Information Literacy: https://www.unesco.org/en/media-information-literacy
- IMLS Public Libraries Survey: https://www.imls.gov/research-evaluation/data-collection/public-libraries-survey
- IMLS Data Catalog: https://www.imls.gov/research-evaluation/data-collection
- ALA Libraries Transform: https://www.ala.org/advocacy/libraries-transform
- Digital.gov: https://digital.gov/

## 下一步

- 建立信息判断变量表：来源识别、证据链、事实核验、搜索、数字技能、馆员支持和公共知识入口。
- 与 `information-integrity-trust/`、`learning-skill-acquisition/`、`digital-inclusion-connectivity/` 和 `public-service-design-accessibility/` 建立接口。
