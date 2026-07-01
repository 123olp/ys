# Research Infrastructure Open Science Translation

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/research-infrastructure-open-science-translation` |
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


`research-infrastructure-open-science-translation/` 研究科研基础设施、开放科学、数据共享、可复现性、研究资助、转化科学和知识扩散如何把发现转化为可审查、可复用、可应用的主体持续性收益。

> 核心问题：未来技术不会自动出现；它依赖实验平台、研究人员、数据、标准、开放知识、转化机制和持续资助。没有科研基础设施，长寿医学、AI、生物技术和公共健康都只会停在孤立论文或不可复现叙事中。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要未来技术窗口持续出现
  -> 技术窗口依赖科研基础设施、开放科学、可复现研究和转化机制
  -> 研究不可复现、数据不可得、资助断裂和转化失败会降低技术到达概率
  -> 因此科研基础设施与开放转化是未来技术生成和采用的上游域
```

## 关注对象

- 科研资助、实验平台、研究数据、开放科学、开放获取、代码与数据复现、研究诚信和知识保存。
- 转化科学、临床前到临床桥接、跨学科协作、研究基础设施共享和发现扩散。
- 研究质量、可复现性、发表偏倚、负结果、数据治理和利益冲突。
- 与 `clinical-trials-regulatory-science-translation/` 的边界：本域关注更宽的科研生态和开放转化；临床试验监管科学域关注人体研究、监管证据和批准路径。
- 与 `measurement-feedback/` 的边界：本域关注知识生产系统；测量反馈域关注主体状态测量、预测和反馈闭环。

## Human Infra 模型链路

```text
科研基础设施与开放转化 T
  -> 改变研究质量、数据可得性、复现性、共享平台、资助和转化协作变量 X
  -> 改变未来技术窗口出现、被验证、被扩散和被采用的系统状态 S
  -> 改变无效研究、证据错配、转化失败和技术窗口延迟风险 λ(t)
  -> 影响未来选择权、技术采用概率和主体持续性上限
```

## 非目标

- 不提供论文代写、署名操控、同行评审规避、数据造假、刷引用或学术不端策略。
- 不把单篇预印本、新闻稿或公司叙事写成已验证技术窗口。
- 不替代研究伦理、机构审查、数据治理或临床监管判断。

## Source Signals

- UNESCO Recommendation on Open Science: https://www.unesco.org/en/open-science
- NIH National Center for Advancing Translational Sciences: https://ncats.nih.gov/
- ClinicalTrials.gov: https://clinicaltrials.gov/
- National Academies Reproducibility and Replicability in Science: https://nap.nationalacademies.org/catalog/25303/reproducibility-and-replicability-in-science
- OECD Science, Technology and Innovation: https://www.oecd.org/sti/

## 下一步

- 建立科研转化变量表：开放数据、复现性、资助、研究诚信、共享平台、转化路径和扩散速度。
- 与 `clinical-trials-regulatory-science-translation/`、`longevity-evidence/`、`cellular-reprogramming/` 和 `measurement-feedback/` 建立接口。
