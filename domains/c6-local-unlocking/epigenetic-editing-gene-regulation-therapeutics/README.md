# Epigenetic Editing Gene Regulation Therapeutics

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/epigenetic-editing-gene-regulation-therapeutics` |
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

`epigenetic-editing-gene-regulation-therapeutics/` 研究表观遗传编辑、可编程基因调控、转录沉默/激活、表观标记改写和非序列改变型疗法，如何影响 Human Infra 的疾病控制、年轻化叙事和长期安全边界。

> 核心问题：若基因表达状态可以在不改变 DNA 序列的情况下被可控改写，医学可能从“改基因”扩展到“改读取方式”。但这种能力也会引入持久表达异常、脱靶调控和身份状态扰动风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 细胞功能和疾病状态不仅由 DNA 序列决定，也由基因表达和表观遗传状态决定
  -> 若表达状态可被可控、可逆或可持久地改写，疾病和衰老相关状态可能获得新干预入口
  -> 若调控范围、持久性和脱靶未知，表达修复会变成系统性扰动
  -> 因此表观遗传编辑是基因表达层面的状态改写域
```

## 关注对象

- dCas9/转录调控器、表观遗传编辑器、DNA 甲基化/去甲基化、组蛋白修饰、染色质状态和 hit-and-run 调控。
- 疾病基因沉默、转录激活、可逆调控、长期表达状态、细胞身份和组织特异性。
- 与细胞重编程的关系：本域关注特定位点或程序的表达状态调控；`cellular-reprogramming/` 关注整体细胞身份和年龄状态重置。
- 与基因编辑的关系：本域不改变 DNA 序列本身；`gene-therapy-genome-editing-delivery-safety/` 关注序列编辑、递送和长期遗传风险。

## Human Infra 模型链路

```text
表观遗传编辑 T
  -> 改变基因表达、染色质状态、组织特异调控、持久性、可逆性和脱靶调控变量 X
  -> 改变细胞功能、疾病通路、身份稳定性和长期安全状态 S
  -> 改变疾病进展、异常表达、肿瘤风险、免疫风险和不可逆状态漂移 λ(t)
  -> 影响可治疗疾病范围、细胞状态维护和主体持续性
```

## 非目标

- 不把表观遗传编辑写成已经成熟的抗衰、逆龄或永生技术。
- 不提供人体实验、非临床递送、编辑器构建、靶点设计或监管规避方案。
- 不把单基因沉默案例外推为全身年轻化。

## Source Signals

- Nature Reviews Drug Discovery: Epigenetic editing from concept to clinic: https://www.nature.com/articles/s41573-025-01323-0
- Nature: Durable and efficient gene silencing in vivo by hit-and-run epigenetic editing: https://www.nature.com/articles/s41586-024-07087-8
- NIH Common Fund Epigenomics: https://commonfund.nih.gov/epigenomics
- FDA Human Gene Therapy Guidance: https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/human-gene-therapy-guidances

## 下一步

- 建立表观编辑变量表：编辑器类型、靶位点、组织、表达变化、持久性、可逆性、脱靶、递送、免疫和长期随访。
- 与 `cellular-reprogramming/`、`gene-therapy-genome-editing-delivery-safety/`、`biological-age-clocks-biomarker-validation/` 和 `cancer-control/` 建立接口。
