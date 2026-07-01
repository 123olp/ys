# biobanking-biospecimen-quality-chain-of-custody 目录说明

本目录维护生物样本库、样本质量和保管链。它是生命科学证据从人体材料进入数据系统之前的物质可信层。

## 目录结构

```text
biobanking-biospecimen-quality-chain-of-custody/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义样本采集、预分析变量、冷链、追踪和保管链如何影响 Human Infra 证据质量。
- 本目录不保存样本数据、个人身份、实验 SOP 或可执行采样协议。
- 资料必须区分研究样本库、临床样本、公共资源标准和企业服务声明。

## 上下游关系

- 上游来自研究伦理、同意治理、样本库标准和生物安全资料。
- 下游服务多组学、生物年龄钟、癌症控制、细胞重编程和临床转化证据。
- 不替代 `blood-organ-tissue-biovigilance-transplantation/` 的临床供体安全和生物警戒职责。

## 维护规则

- 不提供非法采样、规避同意、样本匿名化绕行或生物安全规避策略。
- 不把样本质量指标写成个人诊断或治疗建议。
- 若新增样本相关结论，必须写明样本来源、处理条件、质量边界和适用对象。
