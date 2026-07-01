# Lipid Atherosclerosis Risk Management Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/lipid-atherosclerosis-risk-management-continuity` |
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

`lipid-atherosclerosis-risk-management-continuity/` 研究血脂检测、动脉粥样硬化风险管理、预防性药物证据、生活环境、坚持和二级预防交接如何影响主体持续性。

> 核心问题：动脉粥样硬化风险长期沉积，直到 ACS、卒中或外周血管事件才显性化。有效永生需要把血脂和 ASCVD 风险管理建模为急性血管事件之前的长期概率分布调整器。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖长期通畅血管网络维持脑、心、肾和肌肉灌注
  -> 血脂和炎症环境会推动动脉粥样硬化负荷累积
  -> 结果取决于检测、风险分层、可及治疗、坚持和二级预防交接
  -> 因此血脂与动脉粥样硬化风险管理是血管事件上游预防域
```

## 关注对象

- Lipid testing、ASCVD risk estimation、statin preventive medication evidence、familial hypercholesterolemia signal、secondary prevention handoff、adherence、access barriers。
- 与 `cardiovascular-resilience/` 的边界：该域关注心血管系统韧性；本域关注血脂/ASCVD 风险管理的执行和证据边界。
- 与 `acute-coronary-syndrome-reperfusion-continuity/` 的关系：本域处理 ACS 之前的长期斑块风险，后者处理急性事件窗口。

## Human Infra 模型链路

```text
血脂与 ASCVD 风险管理 T
  -> 改变检测、风险识别、治疗可及、坚持和二级预防变量 X
  -> 改变斑块负荷、血管事件概率和功能储备 S
  -> 改变 ACS、卒中、外周血管事件和有效时间损失 λ(t)
  -> 影响主体行动能力、认知稳定和未来选择权
```

## 非目标

- 不提供个人血脂解读、ASCVD 计算、他汀/降脂药、剂量、补剂、饮食、运动、检查或个体治疗建议。
- 不生成个人药物适应证、二级预防方案、风险排序、保险申诉或商业产品推荐。
- 不收集个案血脂、家族史、用药、不良反应、影像或诊疗资料。

## Source Signals

- USPSTF statin preventive medication: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/statin-use-in-adults-preventive-medication
- CDC cholesterol: https://www.cdc.gov/cholesterol/
- NHLBI atherosclerosis materials: https://www.nhlbi.nih.gov/

## 下一步

- 建立 ASCVD Risk Management Card：lipid test, risk model boundary, access, adherence, event prevention, secondary handoff。
- 与 `cardiovascular-resilience/`、`acute-coronary-syndrome-reperfusion-continuity/` 和 `cerebrovascular-stroke-brain-perfusion-resilience/` 建立接口。
