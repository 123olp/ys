# LEV Source Cards

Last reviewed: 2026-07-02

本文保存长寿逃逸速度二阶 / 多阶效应模型的第一批 Source Cards。Source Card 的用途是限定证据能支持什么、不能支持什么，防止把理论传统、综述、监管术语或机构项目材料过度外推成个体延寿结论。

## Source Card Format

```text
id:
source:
type:
use:
supports:
does_not_support:
maps_to:
next_check:
```

## Cards

### SRC-SYSTEMS-WHO

- source: WHO Alliance, systems thinking for health systems strengthening, <https://iris.who.int/handle/10665/44204>
- type: 官方 / 方法论
- use: 支持将健康技术、资源、治理和反馈环作为系统响应问题处理。
- supports: 多阶效应、反馈、延迟、反弹、资源转移和治理边界。
- does_not_support: 不支持任何具体长寿干预有效性。
- maps_to: `risk:rebound`, `effect:bottleneck`, `effect:chain-completeness`
- next_check: 后续可补复杂系统、系统动力学和 public health unintended consequences 文献。

### SRC-FCT-1995

- source: Link & Phelan, Social conditions as fundamental causes of disease, <https://pubmed.ncbi.nlm.nih.gov/7560851/>
- type: 理论 / 综述
- use: 支持 flexible resources 会通过多机制持续影响健康风险。
- supports: 资金、知识、社会连接和权力等资源能跨疾病、跨时代重新部署。
- does_not_support: 不支持资源变量能直接替代生物医学干预。
- maps_to: `effect:flexible-resource`, `effect:cross-mechanism`
- next_check: 补全文阅读摘录和后续 fundamental cause 扩展文献。

### SRC-FCT-INEQUALITY-2010

- source: Link, Phelan & Tehranifar, Social conditions as fundamental causes of health inequalities, <https://pubmed.ncbi.nlm.nih.gov/20943581/>
- type: 理论 / 综述
- use: 支持资源优势会随新机制和新技术窗口持续重现。
- supports: LEV 技术收益可能优先流向高资源主体。
- does_not_support: 不支持对任何单一技术的公平性结论。
- maps_to: `risk:distribution-shift`, `gate:P_equity`
- next_check: 与 intervention-generated inequalities 和 digital divide 文献交叉审查。

### SRC-IGI-LORENC

- source: Lorenc et al., intervention-generated inequalities, <https://pure.york.ac.uk/portal/en/publications/what-types-of-interventions-generate-inequalities-evidence-from-s/>
- type: 系统综述概念
- use: 支持有效公共健康干预也可能扩大不平等。
- supports: 每条 LEV 路线必须审查 `who can notice / understand / access / afford / adopt`。
- does_not_support: 不支持某个具体 LEV 项目已经制造不平等。
- maps_to: `risk:intervention-generated-inequality`, `gate:P_diffuse`
- next_check: 补原文中按干预类型划分的不平等风险模式。

### SRC-DIFFUSION-GREENHALGH

- source: Greenhalgh et al., Diffusion of innovations in service organizations, <https://pmc.ncbi.nlm.nih.gov/articles/PMC2690184/>
- type: 系统综述 / 实施科学
- use: 支持创新扩散按组织、网络、资源和人群结构分层。
- supports: `P_adopt` 应改写为社会扩散与结构门槛，而不是个体意愿。
- does_not_support: 不支持任何单项技术一定能扩散。
- maps_to: `gate:P_adopt`, `gate:P_diffuse`, `risk:distribution-shift`
- next_check: 对照 Rogers diffusion of innovations 原始理论和医疗实施科学更新文献。

### SRC-SOCIAL-MORTALITY-HOLT-LUNSTAD

- source: Holt-Lunstad et al., Social relationships and mortality risk, <https://pubmed.ncbi.nlm.nih.gov/20668659/>
- type: Meta-analysis
- use: 支持社会关系作为健康和死亡风险相关变量。
- supports: 社会支持可作为主体持续性模型中的容错、恢复和坚持变量。
- does_not_support: 不支持单个社交干预能实现 LEV。
- maps_to: `effect:fault-tolerance`, `gate:P_persist`, `gate:P_recover`
- next_check: 补 social isolation、loneliness、caregiving 和 community navigation 文献。

### SRC-LANCET-DEMENTIA-2024

- source: Lancet Commission dementia prevention, intervention, and care 2024, <https://pubmed.ncbi.nlm.nih.gov/39096926/>
- type: 权威综述
- use: 支持教育、认知、社交、生活方式和风险控制与长期脑健康相关。
- supports: 认知资源既是健康结果，也是未来技术可读性和主体连续性资源。
- does_not_support: 不支持认知训练或教育单独实现长寿逃逸速度。
- maps_to: `effect:future-readability`, `gate:P_understand`
- next_check: 补 cognitive reserve、hearing、education 和 dementia risk factor 细分文献。

### SRC-SLEEP-MORTALITY-CAPPUCCIO

- source: Cappuccio et al., Sleep duration and all-cause mortality, <https://pmc.ncbi.nlm.nih.gov/articles/PMC2864873/>
- type: 系统综述 / Meta-analysis
- use: 支持睡眠和恢复作为健康风险与执行能力相关变量。
- supports: 恢复能力应作为资源转化率变量。
- does_not_support: 不支持用睡眠优化替代医学干预或给出个体寿命预测。
- maps_to: `effect:conversion-rate`, `gate:P_recover`, `gate:P_persist`
- next_check: 补 circadian rhythm、sleep quality、fatigue 和 mental health 证据。

### SRC-DIGITAL-HEALTH-EQUITY-2024

- source: Telemedicine, e-Health, and Digital Health Equity scoping review, <https://pmc.ncbi.nlm.nih.gov/articles/PMC11041391/>
- type: Scoping review
- use: 支持数字健康技术同时降低门槛和制造门槛。
- supports: AI、远程医疗和数字健康路线必须审查设备、网络、账号、语言、信任和技能差距。
- does_not_support: 不支持远程医疗天然提高公平性。
- maps_to: `risk:digital-gate`, `gate:P_access`, `gate:P_diffuse`
- next_check: 补 telehealth adoption、broadband access 和 digital literacy 数据源。

### SRC-BEST-BIOMARKERS

- source: FDA-NIH Biomarker Working Group, BEST biomarker and surrogate endpoint resource, <https://www.ncbi.nlm.nih.gov/books/NBK338448/>
- type: 术语 / 监管科学资源
- use: 支持 biomarker、surrogate endpoint 和 clinical endpoint 的术语边界。
- supports: `P_calibrate` 必须审查指标与真实临床获益的关系。
- does_not_support: 不支持任何 biomarker 可单独替代真实终点。
- maps_to: `risk:goodhart`, `gate:P_calibrate`
- next_check: 补具体 surrogate endpoint qualification 和 geroscience biomarker validation 文献。

### SRC-GEROSCIENCE-ENDPOINTS

- source: Endpoints for geroscience clinical trials, <https://pmc.ncbi.nlm.nih.gov/articles/PMC9768060/>
- type: 综述 / 方法论
- use: 支持健康寿命研究需要区分临床终点、生物标志物和生物年龄指标。
- supports: LEV 路线必须把测量反馈与真实功能、疾病和死亡终点对齐。
- does_not_support: 不支持任何具体 geroscience 干预已经延寿。
- maps_to: `mechanism:measurement-feedback`, `gate:P_calibrate`
- next_check: 与 TAME、PROSPR、XPRIZE Healthspan 的终点结构交叉对齐。
