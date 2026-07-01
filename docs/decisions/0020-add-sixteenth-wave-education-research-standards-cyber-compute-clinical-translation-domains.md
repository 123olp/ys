# 0020 Add Sixteenth Wave Education Research Standards Cyber Compute Clinical Translation Domains

## Status

Accepted

## Context

Human Infra 的前十五波研究域已经覆盖身体维护、主体能力、公共服务、应急、金融、就业、家庭准备、信息素养、健康劳动力、行政摩擦、社区中介和开放数据透明。

继续进行先验追问时，新的缺口出现在“未来技术如何持续生成、验证、扩散并被主体使用”这一层：

- 主体需要持续学习和再训练，否则长寿无法转化为能力复利。
- 技术窗口需要科研基础设施、开放科学和转化机制，否则未来不会自动出现。
- 技术系统需要标准、计量、校准和质量基础设施，否则数据和产品不可比较、不可审查。
- 数字公共服务、医疗、金融、身份和 AI 工具需要网络安全韧性，否则会被攻击截断。
- AI 和科学模拟依赖算力、数据中心、能源、水、芯片和接入治理。
- 医学发现必须经过临床试验、监管科学和安全监测，才能成为可用干预。

## Decision

新增第十六波 6 个正式研究域：

- `domains/c3-generation-engine/education-access-lifelong-learning/`
- `domains/c4-conversion-channel/research-infrastructure-open-science-translation/`
- `domains/c4-conversion-channel/standards-metrology-quality-infrastructure/`
- `domains/c5-ecological-substrate/cybersecurity-resilience-critical-services/`
- `domains/c3-generation-engine/compute-data-center-ai-infrastructure/`
- `domains/c4-conversion-channel/clinical-trials-regulatory-science-translation/`

每个域先只建立 `README.md` 和 `AGENTS.md`，并同步更新根 README、域索引、文档索引、domain map、research-domain-atlas、research-domain-radar、伦理边界和结构检查脚本。

## Consequences

- Human Infra 的域生成逻辑从“主体维护与服务接入”继续上升到“知识、标准、网络安全、算力和医学转化”层。
- 这些域为后续《有效永生》研究中的技术窗口概率、技术采用概率、证据生成速度和系统可用性建模提供独立入口。
- 本轮不创建数据采集脚本、Web 页面、数据库、临床工具、网络安全工具或算力成本模型。

## Boundaries

- 不提供个人教育、升学、职业证书、投资或采购建议。
- 不提供论文代写、学术操控、数据造假或同行评审规避策略。
- 不提供认证规避、检测报告伪造、设备改装或标准绕过策略。
- 不提供攻击、入侵、漏洞利用、钓鱼、恶意软件、权限提升或规避检测步骤。
- 不提供盗用算力、绕过云平台限制、芯片走私、数据中心攻击或监管规避策略。
- 不提供入组、治疗、用药、停药、试验选择、人体试验操作或监管规避建议。
