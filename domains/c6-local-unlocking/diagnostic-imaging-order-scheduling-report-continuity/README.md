# Diagnostic Imaging Order Scheduling Report Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/diagnostic-imaging-order-scheduling-report-continuity` |
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

## 定位

本域研究影像医嘱、prior authorization、预约、设备容量、造影/准备、报告生成、影像资料可携带和结果回传如何把影像能力转化为主体可用的诊断信号。

它不是影像解读、检查推荐、放射风险评估或个案加急入口。

## 先验问题

```text
影像能力何以成为诊断进展？
  -> 医嘱和授权必须能转化为预约
  -> 检查必须在合适窗口内完成
  -> 图像和报告必须回到患者和照护团队
  -> 关键发现必须触发下一步
  -> 否则昂贵设备不会自动减少诊断延误
```

## 研究对象

- X-ray、CT、MRI、ultrasound、mammography 和 nuclear medicine 的门诊执行链。
- 医嘱、预约、prior authorization、site of care、准备要求和造影资料。
- DICOM、PACS、radiology report、critical result、incidental finding 和 image sharing。
- 设备容量、等待时间、重复影像、报告延迟和跨机构可携带性。

## 关键变量

- order-to-schedule、schedule-to-scan、scan-to-report 和 report-viewed 时间。
- 授权失败率、重复影像率、影像资料共享成功率和 critical result 通知闭环率。
- 设备容量、地理距离、语言/无障碍、辐射/造影准备信息和费用透明。

## 证据入口

- Medicare diagnostic non-laboratory tests、CMS imaging quality 和 prior authorization 资料。
- ACR appropriateness / radiology reporting / DICOM / image sharing 相关资料。
- ONC interoperability、diagnostic safety 和 radiology follow-up 研究。

## 非目标

- 不解释影像、推荐检查、判断发现、评估辐射/造影风险或给出诊断治疗建议。
- 不代写 prior authorization、medical necessity、加急申请或影像报告摘要。
- 不收集影像文件、报告、病历、保险、授权号、预约、设备参数或个案健康资料。

## 上下游

- 上游：`specialist-referral-authorization-navigation-continuity/`、`appointment-availability-wait-time-continuity/`、`patient-data-interoperability/`。
- 下游：`rare-disease-diagnostic-odyssey-care-coordination/`、`cancer-control/`、`surgical-anesthesia-perioperative-safety/`。
