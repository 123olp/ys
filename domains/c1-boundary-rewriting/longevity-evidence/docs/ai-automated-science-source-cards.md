# AI Automated Science Source Cards

本文为 `ai-automated-science-technology-window-compression.md` 建立首批 Source Cards。目标不是证明“奇点已经到来”，而是把传播稿里提到的论文、数据库、自动实验室和思想来源，拆成可审查的证据边界。

## Admission Rule

进入 Human Infra C1 `longevity-evidence` 的主张必须通过三层分流：

| 层级 | 可进入内容 | 禁止用途 |
| --- | --- | --- |
| Fact layer | 论文、数据库、自动实验平台、更正声明、官方元数据。 | 不把单点任务表现写成通用科研自治。 |
| Model layer | `DiscoveryRate`、`ValidationLag`、`ExperimentThroughput`、`TranslationProbability`、`SafetyAttrition`、`AccessProbability`。 | 不把发现速度直接替代健康寿命或死亡率终点。 |
| Narrative layer | 范式转移、奇点、长寿逃逸速度、AI 风险、超人类主义背景。 | 不作为事实证据、临床证据或模型校准输入。 |

## Local Pull Record

| 项目 | 记录 |
| --- | --- |
| 本地缓存目录 | `build/reports/ai-automated-science-literature/` |
| 仓库状态 | `build/` 已被 `.gitignore` 忽略；缓存只作本地阅读证据，不提交论文全文。 |
| 主要拉取方式 | Nature / NAR / PubMed / PMC / NCBI E-utilities / 官方页面。 |
| 访问限制 | Science 页面触发 Cloudflare challenge；部分 PubMed 普通页面触发 reCAPTCHA；采用 NCBI E-utilities XML 作为可复核元数据源。 |
| 可提交内容 | Source Card、链接、hash、主张边界、禁止外推。 |
| 不提交内容 | 版权全文、受限页面、个人账号页面、非公开数据、临床或个体预测材料。 |

### Pulled Hashes

| 来源 | 本地缓存 | SHA-256 |
| --- | --- | --- |
| AlphaFold 2021 PubMed XML | `build/reports/ai-automated-science-literature/eutils/alphafold-nature-2021.xml` | `87fa9161895917709873d34af969a4ee8e45ba8518e96c633b1138286e3ac828` |
| AlphaFold 2021 PDF | `build/reports/ai-automated-science-literature/alphafold-nature-2021.pdf` | `6eae057a9faf4f671c3101e0745ed704460c6d3dec77243dfd3a9f2d2ab68970` |
| AlphaFold DB 2024 PubMed XML | `build/reports/ai-automated-science-literature/eutils/alphafold-db-pubmed-2024.xml` | `a883914cc7a88a3fd067c1067a4a468e1ea9151fd8bf300d82475d860ef980bc` |
| AlphaMissense 2023 PubMed XML | `build/reports/ai-automated-science-literature/eutils/alphamissense-pubmed-2023.xml` | `e5d6bda503e513b9f12492622425768cde19b53dfa0bb9d0f689c4832033b3a7` |
| GNoME 2023 PubMed XML | `build/reports/ai-automated-science-literature/eutils/gnome-pubmed-2023.xml` | `31cccc3a7eed567890158ce527a9398df8a5c2b40017180d5630822ba83bfbe4` |
| A-Lab 2023 PubMed XML | `build/reports/ai-automated-science-literature/eutils/alab-nature-2023.xml` | `16a2f23ea7162ad6d80ee1fe743a112694c020ff5d69318b5f3a072c46007256` |
| A-Lab 2026 correction PubMed XML | `build/reports/ai-automated-science-literature/eutils/alab-correction-pubmed-2026.xml` | `79dc2e7a1adeded892238247c0ceed6f9a6e3e19d839c881a29770e11f811fe5` |
| RoboChem 2024 PubMed XML | `build/reports/ai-automated-science-literature/eutils/robochem-pubmed-2024.xml` | `0786b155535128c7f9dc0b661be5d38d298317323e7badc95932866c5c9139b2` |

## Source Cards

### SRC-AI-SCIENCE-ALPHAFOLD-2021

| 字段 | 内容 |
| --- | --- |
| Source | Jumper et al., 2021, *Highly accurate protein structure prediction with AlphaFold*, Nature. |
| DOI / PMID | `10.1038/s41586-021-03819-2` / `34265844` |
| Link | https://www.nature.com/articles/s41586-021-03819-2 |
| Evidence type | Peer-reviewed research article; CASP14 benchmark and method paper. |
| Supports | AI can substantially improve protein structure prediction and reduce the structure-biology bottleneck for many sequence-to-structure tasks. |
| Does not support | Protein function, drug efficacy, clinical therapy, wet-lab validation, or biological aging problems being automatically solved. |
| Human Infra variable | `DiscoveryRate`, `ToolCapability`, `BiologicalModelingCoverage`. |
| C1 use | Serves as a technology-window compression signal for biomedical toolchain speed, not a direct longevity intervention endpoint. |
| Boundary | Prediction accuracy is task-scoped; it must not be converted into “AI has solved biology.” |
| Next action | Map downstream dependency into `ai-drug-discovery-protein-design` when route cards discuss candidate generation. |

### SRC-AI-SCIENCE-ALPHAFOLD-DB-2024

| 字段 | 内容 |
| --- | --- |
| Source | Varadi et al., 2024, *AlphaFold Protein Structure Database in 2024*, Nucleic Acids Research. |
| DOI / PMID | `10.1093/nar/gkad1011` / `37933859` |
| Link | https://academic.oup.com/nar/article/52/D1/D368/7337620 |
| Evidence type | Peer-reviewed database update. |
| Supports | AlphaFold DB provides structure coverage for over 214 million predicted protein sequences and became a large open infrastructure resource. |
| Does not support | The claim that 214 million structures were completed by the 2021 Nature paper or that predictions equal experimental structures. |
| Human Infra variable | `DiscoveryRate`, `OpenScienceInfrastructure`, `SearchableKnowledgeBase`. |
| C1 use | Corrects the article timeline and supports “open predicted-structure infrastructure expanded the search space.” |
| Boundary | Use 2024 database/update wording, not “2021 finished 2.14e8 structures in 12 months.” |
| Next action | Keep as source-of-truth for scale claims in web pages and future C1 narrative. |

### SRC-AI-SCIENCE-ALPHAMISSENSE-2023

| 字段 | 内容 |
| --- | --- |
| Source | Cheng et al., 2023, *Accurate proteome-wide missense variant effect prediction with AlphaMissense*, Science. |
| DOI / PMID | `10.1126/science.adg7492` / `37733863` |
| Link | https://www.science.org/doi/10.1126/science.adg7492 |
| Evidence type | Peer-reviewed computational biology paper and prediction resource. |
| Supports | AI can predict pathogenicity tendencies for large-scale human missense variants and classify many possible single amino-acid substitutions. |
| Does not support | Clinical variant interpretation being complete, patient diagnosis being automated, or the human pathogenic-gene map being “filled.” |
| Human Infra variable | `BiologicalRiskInterpretation`, `DiscoveryRate`, `EvidenceQuality`. |
| C1 use | Supports the claim that AI expands interpretation capacity for genetic risk signals relevant to future medicine. |
| Boundary | Must retain “prediction / tendency / aid to interpretation” language and require clinical, functional, and genetic evidence for decisions. |
| Next action | Cross-link to future genetics, cancer risk, and personalized risk-model cards only after domain-specific review. |

### SRC-AI-SCIENCE-GNOME-2023

| 字段 | 内容 |
| --- | --- |
| Source | Merchant et al., 2023, *Scaling deep learning for materials discovery*, Nature. |
| DOI / PMID | `10.1038/s41586-023-06735-9` / `38030720` |
| Link | https://www.nature.com/articles/s41586-023-06735-9 |
| Evidence type | Peer-reviewed computational materials paper. |
| Supports | Graph networks and active-learning-style scale-up can expand computational search over stable inorganic material candidates. |
| Does not support | Candidate stability being equivalent to synthesis, manufacturing, cost, safety, deployment, or longevity-relevant device availability. |
| Human Infra variable | `DiscoveryRate`, `MaterialsCandidateSpace`, `TranslationProbability`. |
| C1 use | Shows AI can widen the future materials window that may support medical devices, energy storage, sensors, and automation infrastructure. |
| Boundary | Treat as candidate generation and screening, not experimental realization. |
| Next action | Pair with A-Lab / correction cards before making claims about lab realization. |

### SRC-AI-SCIENCE-ALAB-2023

| 字段 | 内容 |
| --- | --- |
| Source | Szymanski et al., 2023, *An autonomous laboratory for the accelerated synthesis of novel materials*, Nature. |
| DOI / PMID | `10.1038/s41586-023-06734-w` / `38030721` |
| Link | https://www.nature.com/articles/s41586-023-06734-w |
| Evidence type | Peer-reviewed autonomous laboratory / materials synthesis paper. |
| Supports | Autonomous lab workflows can combine computation, literature-derived recipes, robotics, ML, active learning, and experimental feedback to explore inorganic materials synthesis. |
| Does not support | Fully autonomous general science, universal experimental success, or unrestricted “Earth has never had these materials” framing. |
| Human Infra variable | `ExperimentThroughput`, `ValidationLag`, `ClosedLoopAutomation`. |
| C1 use | Supports the mechanism that candidate generation can be connected to automated experimental feedback, narrowing the gap between computational search and lab work. |
| Boundary | Must always be read with SRC-AI-SCIENCE-ALAB-CORRECTION-2026. |
| Next action | Use only corrected / conservative wording in public-facing material. |

### SRC-AI-SCIENCE-ALAB-CORRECTION-2026

| 字段 | 内容 |
| --- | --- |
| Source | Szymanski et al., 2026, Author Correction: *An autonomous laboratory for the accelerated synthesis of inorganic materials*, Nature. |
| DOI / PMID | `10.1038/s41586-025-09992-y` / `41554984` |
| Link | https://www.nature.com/articles/s41586-025-09992-y |
| Evidence type | Author correction / amendment. |
| Supports | The A-Lab paper needs constrained citation and title/claim correction; downstream summaries must not preserve unqualified “novel materials” claims. |
| Does not support | A stronger A-Lab result than the corrected paper allows. |
| Human Infra variable | `EvidenceQuality`, `ClaimScope`, `CorrectionRisk`. |
| C1 use | This is a governance card: it prevents the AI automated science route from importing exaggerated A-Lab claims. |
| Boundary | Any A-Lab claim without this correction should be marked stale or overclaimed. |
| Next action | Add a future gate: if a source has an erratum/correction, narrative pages must cite the correction next to the original. |

### SRC-AI-SCIENCE-ROBOCHEM-2024

| 字段 | 内容 |
| --- | --- |
| Source | Slattery et al., 2024, *Automated self-optimization, intensification, and scale-up of photocatalysis in flow*, Science. |
| DOI / PMID | `10.1126/science.adj1817` / `38271529` |
| Link | https://www.science.org/doi/10.1126/science.adj1817 |
| Evidence type | Peer-reviewed chemistry automation paper. |
| Supports | Robotic flow-chemistry platforms can integrate hardware, inline measurement, software, and Bayesian optimization to improve selected photocatalytic reaction workflows. |
| Does not support | General automated drug synthesis, autonomous pharmaceutical discovery, or chemistry as a whole surpassing human scientists. |
| Human Infra variable | `ExperimentThroughput`, `ValidationLag`, `HumanToolSymbiosis`. |
| C1 use | Supports the broader route that automated wet-lab loops can compress experimental feedback for some chemical processes. |
| Boundary | Keep wording at “photocatalysis in flow / selected reactions,” not “new drugs generally.” |
| Next action | Route to drug discovery only after a specific medicinal chemistry or clinical translation source is added. |

### SRC-AI-SINGULARITY-VINGE-1993

| 字段 | 内容 |
| --- | --- |
| Source | Vernor Vinge, 1993, *The Coming Technological Singularity*. |
| Link | https://ntrs.nasa.gov/citations/19940022856 |
| Evidence type | Future studies / conceptual essay. |
| Supports | “Technological singularity” as a historical concept in future studies and AI-intelligence acceleration discourse. |
| Does not support | Any current empirical claim that AI has escaped control, that human science has ended, or that LEV is inevitable. |
| Human Infra variable | `NarrativeFrame`, `TailRiskFrame`, `AccelerationHypothesis`. |
| C1 use | Useful as a narrative and hypothesis-space reference only. |
| Boundary | Never use as evidence for scientific, clinical, or engineering feasibility. |
| Next action | Keep in context layer with Kuhn, Kurzweil, de Grey, Bostrom, Russell, and related books. |

## Context Sources Not Admitted As Fact Cards

| 来源 | Human Infra 用途 | 当前状态 |
| --- | --- | --- |
| Thomas Kuhn, *The Structure of Scientific Revolutions* | 范式转移语言背景。 | 不作为 AI 自动科研事实来源。 |
| Yuval Noah Harari, *Sapiens* | 人类协作、虚构秩序、历史叙事背景。 | 不作为科研自动化或 LEV 证据。 |
| Ray Kurzweil, *The Singularity Is Near* / *The Singularity Is Nearer* | 奇点和长寿逃逸速度的未来学框架。 | 只进入 narrative layer；时间表不作事实结论。 |
| Ray Kurzweil and Terry Grossman, *Fantastic Voyage* | “live long enough to live forever” 传播谱系。 | 只作思想史来源。 |
| Jose Cordeiro and David Wood, *The Death of Death* | 2045 与死亡终结论述背景。 | 不作实验或临床证据。 |
| Aubrey de Grey and Michael Rae, *Ending Aging* / SENS materials | 损伤修复与 LEV 思想背景。 | 需要单独进入 mainstream route source cards 后才能用作路线材料。 |
| Nick Bostrom, *Superintelligence* | AI 风险和失控叙事背景。 | 不作自动科研事实。 |
| Stuart Russell, *Human Compatible* | AI alignment / control problem 背景。 | 不作自动科研事实。 |

## Claim-Evidence Matrix

| Claim ID | 主张 | Evidence | Verdict |
| --- | --- | --- | --- |
| AI-SCI-CL1 | AI 已经压缩部分科学任务中的候选生成和预测周期。 | AlphaFold 2021, AlphaFold DB 2024, AlphaMissense 2023, GNoME 2023. | Supported, task-scoped. |
| AI-SCI-CL2 | AI 自动实验系统已经能在部分材料/化学任务中形成闭环反馈。 | A-Lab 2023 with correction 2026; RoboChem 2024. | Supported, narrow-domain. |
| AI-SCI-CL3 | AI 已经接管科研并让人类失去解释权。 | Vinge / singularity narrative only; no empirical source here. | Not supported. |
| AI-SCI-CL4 | AI 自动科研可作为 LEV 的间接变量。 | Fact cards plus Human Infra technology-window model. | Hypothesis, model-layer only. |
| AI-SCI-CL5 | AI 自动科研已经证明永生或长寿逃逸速度。 | None. | Rejected. |

## Model Admission

本批资料只允许进入以下中间变量，不允许直接进入寿命终点：

```text
AlphaFold / AlphaFold DB
  -> BiologicalModelingCoverage
  -> DiscoveryRate
  -> candidate biomedical window

AlphaMissense
  -> VariantInterpretationCapacity
  -> biological risk stratification hypothesis

GNoME
  -> MaterialsCandidateSpace
  -> future device / energy / sensing window

A-Lab / RoboChem
  -> ExperimentThroughput
  -> ValidationLag pressure
  -> closed-loop lab automation hypothesis

All cards
  -> technology-window compression hypothesis
  -> no direct healthspan, lifespan, LEV or mortality claim
```

## Open Tasks

1. 为 GNoME、A-Lab correction 和 RoboChem 补更细的 full-text claim review，尤其是 correction 后的 A-Lab 数字边界。
2. 把 `DiscoveryRate`、`ValidationLag`、`ExperimentThroughput` 和 `TranslationProbability` 写入下一版 route-card schema。
3. 为自动科研路线新增至少一个 negative case：高候选生成速度但低验证质量导致 `TranslationProbability` 下降。
4. 与 `domains/c3-generation-engine/ai-drug-discovery-protein-design/` 对齐蛋白设计和药物发现边界。
5. 与 `domains/c4-conversion-channel/research-infrastructure-open-science-translation/` 对齐开放科学、复现、预注册、数据仓库和更正机制。
