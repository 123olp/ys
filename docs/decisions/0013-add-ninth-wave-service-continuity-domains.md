# 0013 Add Ninth Wave Service Continuity Domains

## Status

Accepted

## Context

Research Domain Atlas 已把 Human Infra 的域生成规则定义为先验条件追溯：凡是主体持续性成立所需的必要条件、支撑条件、风险条件或反馈条件，都可以被抽象为研究域。

前八波已经覆盖分子维护、生理稳态、身体结构、主体代理、任务资源、外部风险和基础社会资源。但“资源存在”不等于“主体能够使用资源”。主体要在现实世界中持续存在、恢复、行动和进入未来，还需要一组服务链把风险、失能、生活空间、制度身份和低频危机接住：

- 可修复疾病必须能进入医疗服务、转诊、随访和连续照护。
- 失能、慢病、脆弱和认知退行必须有家庭、社区、机构和专业照护系统承接。
- 睡眠、恢复、照护、卫生、社区连接和服务接入必须发生在稳定且可用的居住空间中。
- 医疗、工作、食物、关系、照护和应急资源必须通过交通系统变成真实可达。
- 主体必须被法律身份和民事登记系统承认为权利和服务对象。
- 灾害、事故、公共卫生事件和急性危机必须有预警、通信、医疗、安置和恢复系统响应。

这些方向不能继续只放在 `resource-social-infra/` 中，因为它们各自拥有独立证据来源、失败模式、伦理边界和公共系统接口。

## Decision

新增第九波 6 个服务接入与生活连续性研究域：

- `healthcare-access-continuity/`
- `caregiving-long-term-care/`
- `housing-built-environment-stability/`
- `transportation-access-mobility/`
- `legal-identity-civil-registration/`
- `emergency-preparedness-response/`

每个域先只创建 `README.md` 和 `AGENTS.md`，不创建空数据、脚本或复杂目录。

## Consequences

- Human Infra 可以更准确表达“外部系统如何把主体接入恢复、照护、居住、移动、权利和危机响应”。
- `research-domain-atlas.md`、`research-domain-radar.md`、`domain-map.md` 和伦理边界增加第九波域的先验位置、来源信号和禁止用途。
- 仓库结构检查脚本把第九波目录和文件纳入必需项。

## Non-goals

- 不提供个体医疗诊断、治疗、医生/医院/保险选择、护理计划、机构选择、药物、急救或医学处置建议。
- 不提供租房、买房、维修、住房申请、福利申请、交通路线、驾驶、车辆、撤离路线、法律身份申请、移民、证件办理或资格判断建议。
- 不提供证件欺诈、身份冒用、制度规避、违法获取资源、危险环境进入、武器、暴力、恐慌囤积、生存操作或官方应急指挥替代方案。
- 不把结构性服务缺口改写成个人努力问题。
