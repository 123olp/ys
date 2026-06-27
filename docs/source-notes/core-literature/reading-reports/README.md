# Paper Reading Reports

本目录保存 Human Infra 谱系论文的 Markdown 解读报告。分类依据不是原压缩包编号，而是论文进入 Human Infra 的模型位置：观测、生命状态、定量方法、数字孪生、主体连续性、神经边界、可视化和风险治理。

## 分类总览

| 分类 | 作用 | 报告数 | 迁移方向 |
| --- | --- | ---: | --- |
| `01-observation-personal-informatics/` | 主体数据如何被收集、整合、反思并转化为行动 | 2 | 观测层、反馈闭环、个人信息学 |
| `02-aging-healthspan-biology/` | 衰老机制、生物年龄和死亡风险标志物 | 3 | 状态变量、健康寿命、风险变量 |
| `03-survival-causal-models/` | 生存曲线、风险函数、因果推断和目标试验模拟 | 4 | 定量预测模型、干预评估契约 |
| `04-digital-twin-life-path/` | 人体数字孪生、生命历程模拟和个性化医学 | 3 | 生命路径模拟、动态状态转移 |
| `05-cognition-identity-augmentation/` | 扩展心智、智能增强、人格连续性和上传边界 | 5 | 主体连续性、工具增强、身份边界 |
| `06-neuroethics-bci/` | BCI 伦理、同意、隐私、自主性和责任 | 1 | 神经科技治理、主体边界 |
| `07-visualization-research-ui/` | D3 数据驱动文档和交互式研究表达 | 1 | HTML paper、模型可视化 |
| `08-ai-risk-governance/` | AI 风险分类、灾难性风险、恶意使用和治理 | 3 | Tail risk、治理边界、反滥用 |
| `_original/` | 原始阅读报告包索引 | 1 | 仅用于回溯 |

## 文件索引

### 01. Observation / Personal Informatics

- [`01_li_2010_stage_based_personal_informatics.md`](01-observation-personal-informatics/01_li_2010_stage_based_personal_informatics.md)：个人信息学五阶段模型，支撑 Human Infra 的“准备-收集-整合-反思-行动”观测闭环。
- [`02_epstein_2015_lived_informatics.md`](01-observation-personal-informatics/02_epstein_2015_lived_informatics.md)：生活化自我追踪模型，提醒观测系统必须处理日常中断、负担、动机和修复。

### 02. Aging / Healthspan Biology

- [`03_lopez_otin_2013_hallmarks_of_aging.md`](02-aging-healthspan-biology/03_lopez_otin_2013_hallmarks_of_aging.md)：衰老 hallmarks，提供生物状态变量地图。
- [`04_horvath_2013_dna_methylation_age.md`](02-aging-healthspan-biology/04_horvath_2013_dna_methylation_age.md)：DNA 甲基化年龄，提供生物年龄观测代理。
- [`05_lu_2019_grimage.md`](02-aging-healthspan-biology/05_lu_2019_grimage.md)：GrimAge，连接表观遗传指标、寿命、健康寿命和死亡风险预测。

### 03. Survival / Causal Models

- [`06_kaplan_meier_1958_nonparametric_estimation.md`](03-survival-causal-models/06_kaplan_meier_1958_nonparametric_estimation.md)：Kaplan-Meier 生存曲线，支撑 `S(t)` 和删失数据处理。
- [`07_cox_1972_regression_models_life_tables.md`](03-survival-causal-models/07_cox_1972_regression_models_life_tables.md)：Cox 比例风险模型，支撑风险函数 `lambda(t)`。
- [`08a_hernan_2022_framework_causal_inference.md`](03-survival-causal-models/08a_hernan_2022_framework_causal_inference.md)：观察数据因果推断框架，支撑从相关性到干预问题的转换。
- [`08b_jafarzadeh_neogi_2022_target_trial_emulation.md`](03-survival-causal-models/08b_jafarzadeh_neogi_2022_target_trial_emulation.md)：目标试验模拟入门，支撑 Human Infra 的干预评估门禁。

### 04. Digital Twin / Life Path

- [`09_mulder_2022_dynamic_digital_twin.md`](04-digital-twin-life-path/09_mulder_2022_dynamic_digital_twin.md)：动态数字孪生，连接诊断、治疗、预测和预防。
- [`18_genome_medicine_2025_digital_twins.md`](04-digital-twin-life-path/18_genome_medicine_2025_digital_twins.md)：全球学习型健康与疾病数字孪生，扩展个体和群体模型的连接方式。
- [`19_pascual_2023_human_digital_twin_review.md`](04-digital-twin-life-path/19_pascual_2023_human_digital_twin_review.md)：人体数字孪生实现综述，提供实现类型和工具边界。

### 05. Cognition / Identity / Augmentation

- [`10_clark_chalmers_1998_extended_mind.md`](05-cognition-identity-augmentation/10_clark_chalmers_1998_extended_mind.md)：扩展心智，支撑 AI、笔记、记忆外化和工具增强进入主体模型。
- [`14_zahedi_kambhampati_2021_human_ai_symbiosis.md`](05-cognition-identity-augmentation/14_zahedi_kambhampati_2021_human_ai_symbiosis.md)：人机共生综述，支撑协作式智能增强。
- [`17_engelbart_1962_augmenting_human_intellect.md`](05-cognition-identity-augmentation/17_engelbart_1962_augmenting_human_intellect.md)：增强人类智能，提供工具系统作为认知基础设施的早期谱系。
- [`20_persson_2016_parfit_personal_identity.md`](05-cognition-identity-augmentation/20_persson_2016_parfit_personal_identity.md)：Parfit 人格同一性讨论，支撑主体连续性的哲学边界。
- [`21_wiley_koene_2015_mind_uploading_replacement.md`](05-cognition-identity-augmentation/21_wiley_koene_2015_mind_uploading_replacement.md)：mind uploading 的渐进替换与扫描复制争议，支撑数字连续性边界。

### 06. Neuroethics / BCI

- [`11_burwell_2017_bci_ethics.md`](06-neuroethics-bci/11_burwell_2017_bci_ethics.md)：BCI 伦理综述，提供神经接口中的隐私、同意、身份、自主性和责任边界。

### 07. Visualization / Research UI

- [`12_bostock_2011_d3_data_driven_documents.md`](07-visualization-research-ui/12_bostock_2011_d3_data_driven_documents.md)：D3 数据驱动文档，支撑 Human Infra 的交互式论文页和模型图表。

### 08. AI Risk / Governance

- [`13_slattery_2026_ai_risk_repository.md`](08-ai-risk-governance/13_slattery_2026_ai_risk_repository.md)：AI Risk Repository，提供 AI 风险 taxonomy 和治理词表。
- [`15_hendrycks_2023_catastrophic_ai_risks.md`](08-ai-risk-governance/15_hendrycks_2023_catastrophic_ai_risks.md)：灾难性 AI 风险综述，支撑尾部风险边界。
- [`16_brundage_2018_malicious_use_ai.md`](08-ai-risk-governance/16_brundage_2018_malicious_use_ai.md)：AI 恶意使用，支撑双重用途和反滥用治理。

## 材料状态修正

这些报告生成时，部分条目还是 URL-only。当前论文缓存已经补齐了一部分 PDF，阅读时以 [`../2026-06-28-human-infra-genealogy-download-manifest.md`](../2026-06-28-human-infra-genealogy-download-manifest.md) 为准：

- `06` Kaplan-Meier：已补 Stanford public course PDF。
- `07` Cox：已补 McGill public course PDF。
- `08a` Hernan：已补 public mirror PDF，并保留 PubMed/JAMA metadata。
- `18` Genome Medicine 2025：已补 Springer PDF。
- `20` Persson：仍为 metadata-only，但已补 Parfit 1971 public course copy 作为人格同一性根文献。

## 使用规则

- 本目录是解读工作台，不是项目最终结论。
- 迁移到稳定文档前，必须回看论文原文、缓存状态和 evidence boundary。
- 引用时优先引用论文 canonical URL；本地 PDF/HTML 只作为离线阅读副本。
