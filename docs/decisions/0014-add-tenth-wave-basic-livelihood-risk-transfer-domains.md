# 0014 Add Tenth Wave Basic Livelihood Risk Transfer Domains

## Status

Accepted

## Context

Research Domain Atlas 已把 Human Infra 的域生成规则定义为先验条件追溯：凡是主体持续性成立所需的必要条件、支撑条件、风险条件或反馈条件，都可以被抽象为研究域。

前九波已经覆盖身体维护、主体代理、服务接入、外部风险和生活连续性。但仍有一组更基础的“生计输入和风险分摊”条件没有独立所有权：

- 主体需要稳定、安全、可负担且营养充分的食物输入。
- 主体需要安全饮用水、卫生设施和个人卫生条件。
- 主体需要电力、清洁烹饪、温控、通信供能和医疗设备供电。
- 疾病、失业、残障、贫困、灾害和照护冲击需要公共福利和社会保护承接。
- 高成本风险需要保险、担保、赔付和风险池分摊。
- 儿童发展和照护者工作连续性需要托育和家庭支持基础设施。

这些方向不能继续只放在 `resource-social-infra/`、`financial-resilience-access/` 或 `caregiving-long-term-care/` 中，因为它们有独立证据来源、失败模式、伦理边界和公共政策接口。

## Decision

新增第十波 6 个基础生计与风险分摊研究域：

- `food-security-nutrition-access/`
- `water-sanitation-hygiene-continuity/`
- `energy-access-resilience/`
- `social-protection-benefits-delivery/`
- `insurance-risk-transfer/`
- `childcare-family-continuity/`

每个域先只创建 `README.md` 和 `AGENTS.md`，不创建空数据、脚本或复杂目录。

## Consequences

- Human Infra 可以更准确表达“反稀缺工程”：食物、水卫生、能源、福利、保险和托育把抽象资源转化为主体可持续运行的底层条件。
- `research-domain-atlas.md`、`research-domain-radar.md`、`domain-map.md` 和伦理边界增加第十波域的先验位置、来源信号和禁止用途。
- 仓库结构检查脚本把第十波目录和文件纳入必需项。

## Non-goals

- 不提供个体饮食、食品处置、补水、水质检测、净水购买、电气施工、发电设备、燃料储存或危险应急操作建议。
- 不提供个体福利申请、资格判断、材料准备、保险选择、投保、理赔、税务、法律、移民、投资或财务规划建议。
- 不提供托育机构选择、育儿处方、教育处方、儿童危机处置、家庭纠纷或补贴申请建议。
- 不提供囤积恐慌、黑市采购、非法获取、虚假材料、制度规避、身份冒用或保险欺诈方法。
