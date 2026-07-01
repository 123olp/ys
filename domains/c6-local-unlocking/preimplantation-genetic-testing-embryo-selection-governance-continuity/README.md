# Preimplantation Genetic Testing Embryo Selection Governance Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/preimplantation-genetic-testing-embryo-selection-governance-continuity` |
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

胚胎植入前遗传检测与胚胎选择治理连续性，关注 PGT-A、PGT-M、PGT-P、embryo biopsy、结果解释、临床效用、不确定性、选择压力、伦理边界和优生风险如何影响主体未来选择权。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体希望降低严重遗传风险并保留未来家庭路径
  -> 胚胎检测把遗传概率、胚胎选择、医学不确定性和伦理判断压缩到 IVF 决策点
  -> 若检测效用、限制和社会后果不可审查，技术会把风险管理变成选择压力
  -> 因此 PGT 治理是生殖技术进入 Human Infra 时必须独立审查的风险接口
```

## 关注对象

- PGT-A、PGT-M、PGT-P、embryo biopsy、aneuploidy、monogenic disease、polygenic risk 和结果不确定性。
- 临床效用、证据强度、嵌合体/假阳假阴、胚胎选择语言、遗传咨询、歧视、残障正义和商业宣传边界。
- 与 `ai-drug-discovery-protein-design/`、`gene-therapy-genome-editing/` 的边界：本域不是修改胚胎，而是审查胚胎检测与选择治理。

## Human Infra 模型链路

```text
PGT 与胚胎选择 T
  -> 改变遗传风险信息、胚胎可用性、选择压力、临床不确定性和伦理边界变量 X
  -> 改变主体的生殖决策、风险承受、心理负担、社会规范和未来家庭路径状态 S
  -> 改变误判、过度筛选、歧视、机会成本、胚胎处置冲突和技术滥用风险 lambda(t)
  -> 影响主体未来选择权、后代风险治理和生殖技术正当性
```

## 非目标

- 不提供 PGT 是否使用、结果解释、胚胎选择、疾病风险判断、遗传咨询、IVF 决策或法律建议。
- 不把 polygenic embryo screening、成人发病风险筛查或非医学性状选择写成临床推荐。
- 不提供胚胎操作、基因编辑、规避监管或优生宣传内容。

## Source Signals

- ASRM PGT-A committee opinion: https://www.asrm.org/practice-guidance/practice-committee-documents/the-use-of-preimplantation-genetic-testing-for-aneuploidy-a-committee-opinion-2024/
- ASRM PGT for monogenic conditions: https://www.asrm.org/practice-guidance/practice-committee-documents/indications-and-management-of-preimplantation-genetic-testing-for-monogenic-conditions-a-committee-opinion-2023/
- ASRM PGT-P ethics opinion: https://www.asrm.org/practice-guidance/ethics-opinions/use-of-preimplantation-genetic-testing-for-polygenic-disorders-pgt-p-an-ethics-committee-opinion-2026/
- ACOG Preimplantation Genetic Testing: https://www.acog.org/clinical/clinical-guidance/committee-opinion/articles/2020/03/preimplantation-genetic-testing

## 下一步

1. 建立 PGT governance card：test type、claim、evidence、uncertainty、counseling boundary、selection pressure 和 prohibited inference。
2. 与 `rare-disease-diagnostic-odyssey-care-coordination/`、`health-literacy-navigation/` 和 `gene-therapy-genome-editing-delivery-safety/` 建立接口。
