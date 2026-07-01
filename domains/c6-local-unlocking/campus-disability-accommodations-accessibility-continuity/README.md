# Campus Disability Accommodations Accessibility Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/campus-disability-accommodations-accessibility-continuity` |
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

`campus-disability-accommodations-accessibility-continuity` 研究高校残障服务、Section 504/ADA 合理便利、可访问教学材料、辅助技术、考试住宿、住宿环境、实习临床安排和数字无障碍如何影响学生参与、学习进度和主体权利。

> 核心问题：进入高校以后，功能限制若不能转化为可执行便利和可访问环境，教育机会会被课程形式、考试制度、平台、空间和实习要求重新关闭。

## 关注对象

- Disability services registration、documentation、reasonable accommodations、interactive process 和 grievance routes。
- 可访问课件、captioning、interpreting、assistive technology、考试住宿、实验室/临床/实习便利和 housing accommodations。
- ADA、Section 504、Title II/III、数字无障碍、LMS/平台可访问性和公开课程材料。
- 便利延迟、不可执行、教师落实差异、隐私、污名、课程替代、停学和毕业进度。

## Human Infra 链路

```text
校园残障便利与无障碍连续
  -> 功能限制被转化为可执行支持、可访问材料和可进入空间
  -> 课程排除、考试不公平、实习断裂和身份暴露风险下降
  -> 学习进度、校园参与和自主行动能力保持
  -> 主体长期能力资本、职业入口和权利连续性增强
```

## 非目标

- 不提供个人残障认定、住宿申请、documentation、申诉、法律策略、医疗证明、课程替代或个案建议。
- 不替代 campus disability services、OCR、ADA coordinator、health provider、academic advisor 或法律援助。
- 不收集或处理残障诊断、医疗资料、心理资料、住宿信、课程记录或身份资料。

## Source Signals

- U.S. Department of Education OCR disability discrimination and Section 504 resources: https://www.ed.gov/about/ed-offices/ocr
- ADA.gov higher education and effective communication resources: https://www.ada.gov/
- Section508.gov and W3C WCAG accessibility standards for digital materials.
- Institutional disability services, accessibility and grievance policy materials.

## 下一步

- 建立 `functional limitation -> accommodation process -> implementation -> participation -> progress` 变量表。
- 区分教室、考试、数字平台、住宿、实验室、临床、实习、交通和沟通便利。
- 与 `disability-services-independent-living`、`built-environment-accessibility-universal-design`、`assistive-technology-access`、`education-access-lifelong-learning` 和本轮高教域建立边界。
