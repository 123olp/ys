# Longevity Escape Velocity Mainstream Routes

Last reviewed: 2026-07-02

本文整理当前全球围绕长寿逃逸速度的九条主流探索路线，并把每条路线落回 Human Infra 现有研究域。它是 `longevity-evidence/` 的主流路线索引，不是医学建议、投资建议、个体用药建议或“长寿逃逸速度已经实现”的证明。

## 核心判断

长寿逃逸速度不是单一技术路线，而是一个动态阈值问题：

```text
每一轮医学、AI、测量、监管和资金基础设施进步
  -> 争取更多健康寿命与有效时间
  -> 使主体更可能活到下一轮技术窗口
  -> 下一轮技术继续降低衰老、疾病、失能和验证成本
  -> 当每年新增可行动时间持续超过每年消耗时间
  -> 长寿逃逸速度才具有模型意义
```

因此，主流路线需要同时覆盖直接生物干预、人体功能终点、监管范式、AI 设计、指标反馈、动物转化和资金基础设施。

## 与现有研究域的存在性核查

这些路线已经能被现有域承接，当前不需要新增研究域。正确动作是把它们作为 `longevity-evidence/` 的跨域路线索引维护。

| 路线 | 是否已有承接域 | 主要承接域 | 备注 |
| --- | --- | --- | --- |
| 组合疗法 | 是 | `longevity-evidence/`, `cellular-senescence-clearance/`, `telomere-maintenance/`, `stem-cell-reserve-renewal/`, `proteostasis-autophagy/`, `nutrition-metabolic-health/` | 组合干预需要跨机制矩阵，而不是单药条目。 |
| 健康寿命竞赛 | 是 | `longevity-evidence/`, `survival-analysis-healthspan-risk-modeling/`, `biological-age-clocks-biomarker-validation/`, `clinical-trials-regulatory-science-translation/` | 把抗衰叙事压成可测量人体功能终点。 |
| Geroscience 临床转化 | 是 | `geroprotective-drug-repurposing-trial-governance-continuity/`, `clinical-trials-regulatory-science-translation/`, `causal-inference-target-trial-emulation/` | 重点是监管和试验范式，不只是二甲双胍。 |
| 细胞重编程 | 是 | `cellular-reprogramming/`, `regenerative-medicine/`, `cancer-control/`, `biological-age-clocks-biomarker-validation/` | 触及年龄状态重写，但必须受身份、肿瘤和局部安全边界约束。 |
| AI 加速生物设计 | 是 | `ai-drug-discovery-protein-design/`, `cellular-reprogramming/`, `research-infrastructure-open-science-translation/`, `synthetic-biology-biosecurity/` | AI 从阅读资料进入蛋白、因子和实验设计。 |
| 衰老标志靶向 | 是 | `longevity-evidence/` 与 C2 衰老标志相关域 | 应作为机制地图，不应把机制合理性写成寿命收益。 |
| 生物年龄与功能指标 | 是 | `biological-age-clocks-biomarker-validation/`, `survival-analysis-healthspan-risk-modeling/`, `longitudinal-cohort-retention-followup-infrastructure/` | 作用是缩短反馈周期，不是输出个体死亡日期。 |
| 动物临床捷径 | 部分已有 | `veterinary-care-access-cost-continuity/`, `animal-health-zoonotic-interface-one-health/`, `clinical-trials-regulatory-science-translation/` | 仓库已有动物/兽医域，但缺少“伴侣动物长寿转化”专门视角，可作为后续复核候选。 |
| 资金与基础设施 | 是 | `research-portfolio-prioritization-funding-governance/`, `clinical-trials-regulatory-science-translation/`, `research-infrastructure-open-science-translation/` | 决定哪些路线能从论文进入试验、监管和产业化。 |

## 标签体系

标签只用于分类、检索和可视化，不代表疗效已成立。

| 标签族 | 标签 | 含义 |
| --- | --- | --- |
| 机制 | `mechanism:damage-repair` | 直接处理损伤、修复、细胞状态或组织功能。 |
| 机制 | `mechanism:systems-combination` | 通过多干预组合或系统协同寻找收益。 |
| 机制 | `mechanism:measurement-feedback` | 通过 biomarker、功能终点或居家数据缩短反馈周期。 |
| 机制 | `mechanism:ai-design` | 用 AI 生成、筛选或优化生物工具。 |
| 机制 | `mechanism:translation-infra` | 主要改变试验、监管、资金、数据和转化基础设施。 |
| 证据阶段 | `evidence:animal` | 主要证据或主战场仍在动物系统。 |
| 证据阶段 | `evidence:human-function` | 关注人体功能终点、健康寿命终点或临床转化。 |
| 证据阶段 | `evidence:early-human-safety` | 已进入人体早期安全性研究，但疗效未成立。 |
| 证据阶段 | `evidence:biomarker` | 主要处理替代指标、年龄钟或观测代理指标。 |
| 证据阶段 | `evidence:institutional` | 主要来源是竞赛、资助、项目方或监管基础设施材料。 |
| 转化路径 | `translation:clinical-trial` | 通过人体临床试验或试验范式推进。 |
| 转化路径 | `translation:animal-bridge` | 通过伴侣动物或动物临床作为转化桥。 |
| 转化路径 | `translation:regulatory-pathway` | 重点是监管可接受终点、适应症或审批路径。 |
| 治理边界 | `boundary:no-personal-advice` | 不得转成个体用药、检测、治疗或购买建议。 |
| 治理边界 | `boundary:no-lev-proof` | 不得写成长寿逃逸速度已经实现。 |
| 治理边界 | `risk:overclaim` | 高风险在于把早期信号、动物数据或指标改善过度外推。 |

## 路线标签总览

| 路线 | 标签 |
| --- | --- |
| R1 组合疗法 | `mechanism:systems-combination`, `mechanism:damage-repair`, `evidence:animal`, `translation:clinical-trial`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof` |
| R2 健康寿命竞赛 | `mechanism:measurement-feedback`, `evidence:human-function`, `evidence:institutional`, `translation:clinical-trial`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof` |
| R3 Geroscience 临床转化 | `mechanism:translation-infra`, `evidence:human-function`, `translation:clinical-trial`, `translation:regulatory-pathway`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof` |
| R4 细胞重编程 | `mechanism:damage-repair`, `evidence:early-human-safety`, `translation:clinical-trial`, `translation:regulatory-pathway`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof` |
| R5 AI 加速生物设计 | `mechanism:ai-design`, `mechanism:translation-infra`, `evidence:institutional`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof` |
| R6 衰老标志靶向 | `mechanism:damage-repair`, `mechanism:systems-combination`, `evidence:biomarker`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof` |
| R7 生物年龄与功能指标 | `mechanism:measurement-feedback`, `evidence:biomarker`, `evidence:human-function`, `translation:clinical-trial`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof` |
| R8 动物临床捷径 | `translation:animal-bridge`, `evidence:animal`, `translation:regulatory-pathway`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof` |
| R9 资金与基础设施 | `mechanism:translation-infra`, `evidence:institutional`, `translation:regulatory-pathway`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof` |

## 路线卡

### R1. 组合疗法路线

代表项目：LEV Foundation Robust Mouse Rejuvenation。

Tags: `mechanism:systems-combination`, `mechanism:damage-repair`, `evidence:animal`, `translation:clinical-trial`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof`.

核心问题不是“哪个单药能延寿”，而是：

```text
多个已存在延寿信号
  -> 能否在同一老年动物系统中组合
  -> 是否产生叠加、协同、抵消或毒性
  -> 是否同时改善寿命曲线和健康寿命指标
```

Human Infra 映射：

- 直接输入：雷帕霉素、端粒酶、senolytics、干细胞 / 骨髓相关干预等组合信号。
- 中间变量：细胞衰老负担、营养感知、组织修复、端粒维护、免疫 / 炎症状态。
- 输出位置：`lambda(t)`、健康寿命、动物寿命曲线、组合风险。
- 不能推出：小鼠组合结果不能直接推出人体延寿或个人干预策略。

来源信号：LEV Foundation 将 RMR 描述为测试多种已有健康寿命延展潜力干预组合是否存在协同收益；其更新页也持续发布生存曲线和健康寿命数据整理进度。

### R2. 健康寿命竞赛路线

代表项目：XPRIZE Healthspan。

Tags: `mechanism:measurement-feedback`, `evidence:human-function`, `evidence:institutional`, `translation:clinical-trial`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof`.

它的真正价值是把“抗衰”从宣传词压进可审查终点：

```text
候选干预
  -> 恢复肌肉、认知、免疫功能
  -> 用统一竞赛规则比较
  -> 形成可审查的人体健康寿命终点
```

Human Infra 映射：

- 直接输入：功能恢复型干预组合。
- 中间变量：肌肉功能、认知表现、免疫功能。
- 输出位置：健康寿命、有效时间、行动能力。
- 不能推出：竞赛获胜或功能改善不自动等于死亡风险下降。

来源信号：XPRIZE Healthspan 页面显示该竞赛处于 active 状态，时间线为 2023-2030，奖金池为 1.01 亿美元，并要求团队创造能至少恢复 10 年、目标 20 年肌肉、认知和免疫功能的疗法。

### R3. Geroscience 临床转化路线

代表项目：TAME。

Tags: `mechanism:translation-infra`, `evidence:human-function`, `translation:clinical-trial`, `translation:regulatory-pathway`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof`.

核心不是“二甲双胍是否神奇”，而是监管范式：

```text
把衰老作为共同生物靶点
  -> 测试是否延迟多种年龄相关疾病
  -> 推动 aging indication / geroscience trial 语言
  -> 让后续 geroprotective drugs 有临床试验模板
```

Human Infra 映射：

- 直接输入：再利用药物、老年多病种终点、目标试验设计。
- 中间变量：代谢、炎症、慢病发生时间、复合疾病终点。
- 输出位置：疾病发生 / 进展延迟、监管可接受终点。
- 不能推出：TAME 的成败不能代表整个 geroscience 是否成立。

来源信号：AFAR 的 TAME 页面称该试验计划在 14 个机构、6 年、3000 多名 65-79 岁个体中测试 metformin 是否延迟年龄相关慢病发生或进展，并强调目标是证明 aging 可以被作为治疗对象。

### R4. 细胞重编程路线

代表项目：Life Biosciences ER-100。

Tags: `mechanism:damage-repair`, `evidence:early-human-safety`, `translation:clinical-trial`, `translation:regulatory-pathway`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof`.

该路线最接近“年龄状态重写”，但当前现实路径是局部疾病治疗：

```text
受控 OSK 表达
  -> 眼部局部细胞功能恢复假设
  -> Phase 1 安全性 / 耐受性 / 视觉功能终点
  -> 远期才可能讨论多器官平台
```

Human Infra 映射：

- 直接输入：部分表观遗传重编程、OSK、局部递送。
- 中间变量：表观遗传模式、细胞身份、组织功能、肿瘤风险、免疫反应。
- 输出位置：器官功能、年龄相关疾病进展、未来重编程平台证据。
- 不能推出：Phase 1 入组或首例给药不等于人体逆龄成功。

来源信号：Life Biosciences 2026-01-28 宣布 FDA 清除 ER-100 的 IND，允许其启动 Phase 1 first-in-human 研究；2026-06-09 宣布首位受试者给药。官方材料称 ER-100 使用 OCT4、SOX2、KLF4 的受控表达，当前研究对象是 OAG 和 NAION 等视神经病变。

### R5. AI 加速生物设计路线

代表项目：OpenAI / Retro Biosciences 的 Yamanaka 因子工程；OpenAI GPT-Rosalind 生命科学研究模型。

Tags: `mechanism:ai-design`, `mechanism:translation-infra`, `evidence:institutional`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof`.

核心转折是 AI 不只是整理文献，而是进入生物工具设计：

```text
蛋白工程模型
  -> 设计 SOX2 / KLF4 变体
  -> 提升体外重编程 marker 表达和候选命中率
  -> 降低未来细胞重编程工具搜索成本
```

Human Infra 映射：

- 直接输入：领域模型、蛋白序列、结构 / 文本 / wet-lab feedback。
- 中间变量：候选生成速度、命中率、验证成本、实验迭代周期。
- 输出位置：未来技术窗口概率、工具设计能力、科研速度。
- 不能推出：体外 marker 提升不等于人体疗法、寿命延长或安全性成立。

来源信号：OpenAI 与 Retro Biosciences 的研究说明称其创建 GPT-4b micro，设计增强版 Yamanaka 因子，并在体外实现 reprogramming marker 表达大幅提升；OpenAI 2026 年发布 GPT-Rosalind，定位为支持 biology、drug discovery 和 translational medicine 的生命科学研究模型。两者都只支持“AI 生物设计路线正在形成”，不能支持疗效或延寿结论。

### R6. 衰老标志靶向路线

代表框架：Hallmarks of Aging。

Tags: `mechanism:damage-repair`, `mechanism:systems-combination`, `evidence:biomarker`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof`.

这条路线是全域机制地图：

```text
衰老被拆成多个 hallmark
  -> 每个 hallmark 对应可观测变量和干预候选
  -> 项目可被映射到机制模块
  -> 但机制模块必须再回到功能、疾病和死亡终点
```

Human Infra 映射：

- 直接输入：基因组稳定、端粒、表观遗传、蛋白稳态、营养感知、线粒体、细胞衰老、炎症等机制域。
- 中间变量：损伤、修复、代谢、细胞通信和组织稳态。
- 输出位置：候选靶点地图、干预组合设计、证据分层。
- 不能推出：命中 hallmark 不等于人类寿命延长。

来源信号：2023 年 Cell 综述 `Hallmarks of aging: An expanding universe` 将衰老框架扩展为十二个标志；AFAR 的 Hallmarks 页面也将这些标志作为健康寿命疗法开发的领域入口。

### R7. 生物年龄与功能指标路线

代表指标：DunedinPACE、GrimAge、PROSPR 指标体系。

Tags: `mechanism:measurement-feedback`, `evidence:biomarker`, `evidence:human-function`, `translation:clinical-trial`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof`.

核心功能是缩短反馈周期：

```text
寿命终点反馈太慢
  -> 需要 biomarker / functional endpoint
  -> 更快筛选候选干预
  -> 但指标必须与真实功能、疾病、死亡风险对齐
```

Human Infra 映射：

- 直接输入：DNA methylation clocks、功能年龄、体内 / 居家数据采集、临床终点。
- 中间变量：状态观测、风险估计、干预响应、试验周期。
- 输出位置：模型反馈速度、证据质量、临床试验可行性。
- 不能推出：单个年龄钟数值不能输出个体死亡日期或替代真实终点。

来源信号：DunedinPACE 论文将其定位为 pace-of-aging biomarker，并报告与 morbidity、disability、mortality 相关；GrimAge 论文题名即强调其预测 lifespan 和 healthspan。ARPA-H PROSPR 则明确希望用 biochemical / physiological markers、in-home data collection 和三年内可评估 age-associated health outcomes 的临床试验协议，加速疗法可用性。

### R8. 动物临床捷径路线

代表项目：Loyal 犬类长寿药物。

Tags: `translation:animal-bridge`, `evidence:animal`, `translation:regulatory-pathway`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof`.

犬类路线的价值是转化桥梁：

```text
狗寿命短、共享人类环境、年龄病相似
  -> 可在兽医监管和真实世界动物临床中测试
  -> 获得寿命 / 健康寿命 / 安全性转化信号
  -> 反哺人类 geroscience 设计
```

Human Infra 映射：

- 直接输入：犬类长寿药物、兽医临床、真实世界伴侣动物数据。
- 中间变量：代谢健康、品种寿命差异、生活质量、年龄病发生。
- 输出位置：转化模型、监管路径、老龄动物安全性要求。
- 不能推出：犬类寿命药物进展不等于人类可用长寿药物。

来源信号：Loyal 官方材料显示 LOY-001、LOY-002、LOY-003 均处于开发中；Loyal 称 LOY-001 已收到 FDA Center for Veterinary Medicine 的 Reasonable Expectation of Effectiveness 技术节完成信，LOY-002 已完成三项条件批准关键要求中的两项。

缺口：仓库已有兽医、动物健康和临床转化域，但还没有一个专门承接“伴侣动物长寿转化模型”的域。当前先在本路线卡记录，后续可复核是否需要新增或重分级。

### R9. 资金与基础设施路线

代表：Hevolution、ARPA-H PROSPR、Academy for Health & Lifespan Research。

Tags: `mechanism:translation-infra`, `evidence:institutional`, `translation:regulatory-pathway`, `risk:overclaim`, `boundary:no-personal-advice`, `boundary:no-lev-proof`.

这条路线常被低估，但它决定前八条能否持续运转：

```text
资金、试验网络、指标共识、监管接口、开放科研和产业化
  -> 决定项目是否能从机制走到人体证据
  -> 决定失败是否被记录、复现和纠错
  -> 决定长寿技术是否有真实可及性
```

Human Infra 映射：

- 直接输入：资助机构、竞赛、临床试验网络、监管讨论、开放科研基础设施。
- 中间变量：研究组合、试验成本、数据标准、重复验证、转化速度。
- 输出位置：技术窗口概率、证据生产速度、可及性和公平性。
- 不能推出：资金规模不等于技术成功。

来源信号：Hevolution 自称以 aging as a treatable process 为方向推动科学和商业人才进入健康寿命领域；XPRIZE 页面也披露 Hevolution 作为 co-title sponsor 支撑 Healthspan 竞赛。ARPA-H PROSPR 明确以 biomarkers、assessment tools、in-home data 和三年期健康寿命试验协议为核心。

## 主流路线总链路

```text
组合疗法、重编程、衰老标志靶向
  -> 改变身体损伤、修复、炎症、功能和疾病风险
  -> 健康寿命竞赛、TAME、PROSPR 把干预压入人体功能和监管终点
  -> 生物年龄 / 功能指标缩短反馈周期
  -> AI 生物设计提高候选工具生成速度
  -> 动物临床提供中间转化桥梁
  -> 资金、试验网络、数据标准和监管接口降低转化成本
  -> 主体更可能获得下一轮健康寿命增量
  -> 长寿逃逸速度从单点技术叙事变成复合系统阈值问题
```

## 证据边界

- `official / registry`：机构官网、ClinicalTrials.gov、监管相关页面，只能证明项目定位、试验状态、公开目标和自述边界。
- `peer-reviewed framework`：Hallmarks、DunedinPACE、GrimAge 等文献，可支撑机制地图或指标预测性，但不能直接推出干预效果。
- `company announcement`：Life Biosciences、Loyal、OpenAI / Retro 等材料必须标注为项目方材料，不能当作独立疗效证明。
- `competition / funder`：XPRIZE、Hevolution、ARPA-H 说明资金和试验基础设施，不证明具体疗法有效。
- `prohibited inference`：不得把动物实验、早期安全试验、biomarker 改善、体外 marker、竞赛规则或公司公告写成有效永生、人体逆龄或长寿逃逸速度已实现。

## Source signal register

| 来源 | 类型 | 路线 | 本文使用边界 |
| --- | --- | --- | --- |
| https://www.levf.org/projects/robust-mouse-rejuvenation-study-1/study-updates | 项目更新 | R1 | 支持“组合疗法 / 小鼠复兴研究”作为路线存在，不直接支持人体结论。 |
| https://www.xprize.org/competitions/healthspan | 竞赛官网 | R2 / R9 | 支持奖金、时间线和肌肉 / 认知 / 免疫功能终点定位。 |
| https://www.afar.org/tame-trial | 机构官网 | R3 | 支持 TAME 的设计目标、年龄段、机构数量和 aging indication 叙事。 |
| https://www.lifebiosciences.com/life-biosciences-announces-fda-clearance-of-ind-application-for-er-100-in-optic-neuropathies/ | 公司公告 | R4 | 支持 ER-100 IND clearance 和 Phase 1 启动边界。 |
| https://www.lifebiosciences.com/life-biosciences-announces-first-patient-dosed-in-phase-1-trial-of-er-100-for-optic-neuropathies/ | 公司公告 | R4 | 支持首例给药和当前终点边界，不支持疗效结论。 |
| https://clinicaltrials.gov/study/NCT07290244 | 试验登记 | R4 | 支持 ER-100 试验登记核验。 |
| https://openai.com/index/accelerating-life-sciences-research-with-retro-biosciences/ | 研究说明 | R5 | 支持 GPT-4b micro / Yamanaka 因子工程作为 AI 生物设计路线信号。 |
| https://openai.com/index/introducing-gpt-rosalind/ | 研究说明 | R5 | 支持 GPT-Rosalind 作为生命科学研究工作流和药物发现加速路线信号。 |
| https://www.cell.com/cell/fulltext/S0092-8674(22)01377-0 | 综述论文 | R6 | 支持 Hallmarks of Aging 扩展框架，不支持单一干预有效性。 |
| https://elifesciences.org/articles/73420 | 论文 | R7 | 支持 DunedinPACE 作为 pace-of-aging biomarker。 |
| https://pubmed.ncbi.nlm.nih.gov/30669119/ | 论文索引 | R7 | 支持 GrimAge 与 lifespan / healthspan 预测相关的来源入口。 |
| https://loyal.com/products | 公司产品页 | R8 | 支持 Loyal 犬类长寿药物管线状态和目标定位。 |
| https://loyal.com/posts/loyal-announces-historic-fda-milestone-for-large-dog-lifespan-extension-drug | 公司公告 | R8 | 支持 LOY-001 RXE 里程碑作为公司披露；需避免写成最终 FDA 批准。 |
| https://arpa-h.gov/explore-funding/programs/prospr | 官方项目页 | R7 / R9 | 支持 PROSPR 的 marker、home data 和三年健康寿命试验协议目标。 |
| https://www.hevolution.com/ | 机构官网 | R9 | 支持 Hevolution 的健康寿命资金和产业基础设施定位。 |

## 下一步研究任务

1. 给 R1-R9 各建一张 Source Card，字段包括 `claim`, `variable`, `mechanism`, `evidence_type`, `domain_path`, `boundary`, `next_check`。
2. 为每条路线建立 `route -> tag -> variable -> endpoint -> domain` 结构化 TSV，后续供 Web 图表和筛选器使用。
3. 对 R8 做分级复核：判断是否需要新增 `companion-animal-longevity-translation/`，或纳入现有兽医 / 临床转化域。
4. 把 R7 的指标路线与 `survival-analysis-healthspan-risk-modeling/`、`causal-inference-target-trial-emulation/` 和 `longitudinal-cohort-retention-followup-infrastructure/` 建立显式接口。
5. 所有传播材料必须保留非主张边界：当前没有任何路线证明长寿逃逸速度已经实现。
