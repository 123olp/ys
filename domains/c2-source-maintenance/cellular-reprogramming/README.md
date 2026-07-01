# Cellular Reprogramming

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cellular-reprogramming` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 直接维护身体、脑、器官、衰老、损伤或生命系统这些可能性源体。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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


Cellular Reprogramming 负责整理山中因子、部分重编程、化学重编程、AI 因子设计和表观遗传编辑等“细胞状态可重写”谱系，判断它们如何影响主体持续性。

核心判断：

> 山中因子并没有证明“永生即将到来”，但它打开了一个新的生物学范式：细胞身份与细胞年龄，可能在一定条件下被拆开调控。

本域研究的不是“返老还童宣传”，而是一个更窄、更可审查的问题：

```text
能不能只重置年龄，不重置身份；
只修复功能，不制造癌变；
只恢复组织，不打乱整个生命系统。
```

## 与 Human Infra 的关系

Human Infra 关心主体能否持续存在、行动、学习、恢复和进入未来。细胞重编程进入这个框架的位置是生物状态层：

```text
重编程技术 T
  -> 影响表观遗传状态、细胞身份、组织功能和修复能力 X
  -> 改变主体生理状态 S
  -> 改变疾病风险、失能风险、恢复能力和风险函数 λ(t)
  -> 改变健康寿命、有效时间和未来选择权
  -> 可能反过来增强主体持续性
```

它不是独立的永生路径，而是 Human Infra 中“身体可维护性”和“未来边界扩展”的关键机制候选。

## 总谱系

```text
发育生物学：细胞命运并非绝对不可逆
  -> 2006：山中因子 OSKM 诱导 iPS 细胞
  -> 2012：诺奖确认成熟细胞可被重编程
  -> 2013：体内完全重编程暴露畸胎瘤风险
  -> 2016：部分 / 周期性重编程提出
  -> 2020：短暂 mRNA 重编程与局部器官方向推进
  -> 2022：MPTR 在人类体外细胞中展示多组学年轻化信号
  -> 2023：表观遗传信息丢失理论强化
  -> 2024-2026：化学重编程、AI 因子设计、器官特异性疗法和早期人体安全性试验
  -> 当前前沿：局部、安全、可控、可测量的细胞年轻化
```

真正的概念转折不是“细胞可以变年轻”这一句，而是：

```text
完全重编程：
老体细胞 -> 多能干细胞
年龄重置，身份也被抹掉

部分重编程：
老体细胞 -> 更年轻的同类细胞
年龄部分重置，身份尽量保留
```

## 技术分支

| 路线 | 机制 | 当前位置 | 主要风险 |
| --- | --- | --- | --- |
| OSKM / iPS 完全重编程 | Oct4、Sox2、Klf4、c-Myc 将成熟细胞推回多能状态 | 诺奖级基础事实，不是活体抗衰疗法 | 身份丢失、畸胎瘤、系统失控 |
| OSK / OSKM 部分重编程 | 短暂或周期性表达因子，试图停在年轻化窗口内 | 动物和体外研究较多，局部器官方向进入早期人体安全性验证 | 表达控制、肿瘤风险、组织差异 |
| mRNA / LNP 短暂表达 | 非整合性、短时表达重编程因子 | 适合作为可控扰动路线研究 | 递送、剂量、免疫反应、重复给药 |
| 化学重编程 | 用小分子组合调节细胞状态 | 前沿探索，潜在药物化优势 | 效率、毒性、脱靶、肿瘤风险 |
| AI 设计因子 | 用模型设计更强或更特异的重编程因子 | 平台探索和体外实验阶段 | 泛化失败、解释不足、细胞类型差异 |
| 表观遗传编辑 | 不改 DNA 序列，调节表观遗传标记和表达状态 | 更接近特定位点或特定表达程序调控 | 持久性、脱靶、可逆性、长期安全 |

## 前沿理论

### 衰老是表观遗传信息失序的一部分

这一路线认为，衰老不只是 DNA 序列损坏，也包括细胞读取基因组的表观遗传程序逐渐混乱。

```text
基因组 = 底层数据
表观遗传 = 读取方式和索引系统
衰老 = 读取系统逐渐失序
重编程 = 尝试恢复更年轻的读取状态
```

这个理论有解释力，但不能把衰老缩减成单一表观遗传问题。DNA 突变、端粒、蛋白稳态、线粒体、免疫炎症、干细胞耗竭、细胞外基质和组织结构损伤仍然必须进入模型。

### 细胞身份漂移

衰老细胞不一定完全变成另一种细胞，而可能逐渐偏离原来的稳定身份。部分重编程试图把偏离身份轨道的老细胞推回更年轻、更稳定的身份吸引子。

### 年轻化与去分化的部分解耦

领域最关键的治疗窗口是：

```text
过短：没有足够年轻化效果
刚好：年龄指标、功能和修复能力改善
过长：身份丢失、去分化、癌变和系统性混乱
```

因此，本域所有主张必须同时问两个问题：

```text
年轻化信号是否出现？
细胞身份是否仍被保留？
```

### 组织生态位与系统性衰老

未来路径未必是“让每个细胞都逆龄”，更可能是：

```text
重编程关键细胞
  -> 改善组织生态位
  -> 恢复细胞间通讯
  -> 提升器官修复和功能
```

## 证据等级

| 等级 | 内容 | 当前判断 |
| --- | --- | --- |
| 已确定 | OSKM 可以把成熟细胞重编程为 iPS 细胞 | 可靠，属于基础发现 |
| 已确定 | 完全重编程有身份丢失和畸胎瘤风险 | 可靠，动物实验和机制风险明确 |
| 较强证据 | 短暂 / 部分重编程可改善细胞年龄指标 | 多个人类体外细胞研究支持 |
| 较强临床前 | OSK / OSKM 可在小鼠局部组织中改善衰老或损伤表型 | 动物证据较多，但组织差异大 |
| 早期人体 | 局部眼部 OSK 路线进入一期安全性验证 | 只说明进入安全性测试，不等于人体逆龄疗效成立 |
| 前沿探索 | 化学重编程、AI 设计因子、器官特异性因子组合 | 方向重要，但仍早期 |
| 高风险推论 | 全身逆龄、延寿几十年、永生 | 当前不作为仓库稳定结论 |

## 审查清单

新增任何细胞重编程资料时，必须回答：

| 问题 | 审查意义 |
| --- | --- |
| 它影响的是年龄指标、细胞身份、组织功能，还是临床终点？ | 防止把 biomarker 改善误写成寿命改善 |
| 是否区分了年轻化和去分化？ | 防止把身份丢失误当成返老还童 |
| 是否报告肿瘤、畸胎瘤、增殖失控或癌前风险？ | 安全门槛 |
| 使用的是 OSKM、OSK、mRNA、小分子、表观遗传编辑还是 AI 因子？ | 明确技术路线 |
| 作用对象是体外细胞、动物、局部器官，还是人体试验？ | 明确证据层级 |
| 是否有长期随访和功能终点？ | 防止短期分子信号过度外推 |
| 是否有明确关闭机制、剂量控制和组织特异性？ | 可控性边界 |
| 是否涉及医疗建议或实验协议？ | 必须移除或改写为高层边界说明 |

## 非目标

- 不提供细胞培养、载体构建、递送、剂量、给药或实验操作步骤。
- 不提供任何人体自用、临床替代、处方、治疗或抗衰方案。
- 不把商业公告当作疗效证据。
- 不把表观遗传年龄、转录组年龄或单一 biomarker 等同于真实寿命延长。
- 不把局部器官疾病试验外推为全身逆龄。
- 不把山中因子写成“永生按钮”。

## Source Trail

这些来源是本域的第一批资料线索，进入正式模型前仍需转成 Source Card：

- Takahashi & Yamanaka, 2006, OSKM 诱导小鼠 iPS 细胞: https://pubmed.ncbi.nlm.nih.gov/16904174/
- Abad et al., 2013, 体内重编程产生 iPS 样细胞和畸胎瘤风险: https://pubmed.ncbi.nlm.nih.gov/24025773/
- Ocampo et al., 2016, 周期性部分重编程改善小鼠衰老标志: https://pubmed.ncbi.nlm.nih.gov/27984723/
- Sarkar et al., 2020, 短暂非整合性重编程改善人类细胞衰老特征: https://www.nature.com/articles/s41467-020-15174-3
- Gill et al., 2022, MPTR 多组学年轻化人类细胞: https://pmc.ncbi.nlm.nih.gov/articles/PMC9023058/
- Reprogramming-induced rejuvenation 综述: https://www.nature.com/articles/s41467-024-46020-5
- Chemical reprogramming of human somatic cells: https://www.nature.com/articles/s41586-022-04593-5
- Partial chemical reprogramming multi-omics: https://elifesciences.org/articles/90579
- Loss of epigenetic information as a cause of mammalian aging: https://pubmed.ncbi.nlm.nih.gov/36638792/
- Hallmarks of aging: An expanding universe: https://pubmed.ncbi.nlm.nih.gov/36599349/
- Epigenetic clocks reveal a rejuvenation event during embryogenesis: https://pmc.ncbi.nlm.nih.gov/articles/PMC8232908/
- Life Biosciences ER-100 IND clearance: https://www.lifebiosciences.com/life-biosciences-announces-fda-clearance-of-ind-application-for-er-100-in-optic-neuropathies/
- Life Biosciences ER-100 first patient dosed: https://www.lifebiosciences.com/life-biosciences-announces-first-patient-dosed-in-phase-1-trial-of-er-100-for-optic-neuropathies/
- OpenAI / Retro Biosciences life sciences research note: https://openai.com/index/accelerating-life-sciences-research-with-retro-biosciences/
- Epigenetic editing review: https://www.nature.com/articles/s41573-025-01323-0
- Hit-and-run epigenetic silencing in vivo: https://www.nature.com/articles/s41586-024-07087-8

## 下一步

1. 将 Source Trail 转成 `docs/templates/research-card.md` 格式的 Source Cards。
2. 建立 Claim-Evidence Matrix，区分“细胞指标”“动物功能”“人体安全性”“人体疗效”四类主张。
3. 把本域变量接入生命路径预测模型：表观遗传状态、身份保持、肿瘤风险、组织功能、恢复能力和可采用性。
4. 与 `domains/c1-boundary-rewriting/longevity-evidence/` 建立引用关系：本域负责机制和边界，长寿证据域负责具体干预证据账本。
