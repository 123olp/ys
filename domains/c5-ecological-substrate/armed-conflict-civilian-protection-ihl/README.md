# Armed Conflict Civilian Protection IHL

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/armed-conflict-civilian-protection-ihl` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 主要提供主体展开未来所需的基础环境、资源、治理或基础设施。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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


武装冲突、平民保护与国际人道法域研究：当社会进入战争、占领、内战或武装暴力状态时，主体的生命、医疗、水、食物、身份、住所、通信和家庭连续性如何仍被最低限度保护。

## 对象

- 国际人道法、平民保护、受保护人员、医疗中立、人道准入、战俘与被拘押者保护。
- 武装冲突对医疗系统、水电、粮食、住房、学校、身份文件、通信、家庭分离和流离失所的影响。
- 人道组织、保护监测、失踪人员、家属联系、伤病员救护和基本服务恢复。
- 冲突中“主体持续性”被一次性击穿的路径：死亡、伤残、饥饿、感染、创伤、失踪、身份断裂和制度排除。
- 国际法、公共人道资料和非操作性风险建模之间的边界。

## Human Infra 价值

有效永生和主体持续性不能只建立在和平、稳定和个人资源充足的默认世界上。武装冲突会把生命风险、医疗断裂、资源断供、身份丢失和家庭分离同时推高，因此平民保护是 Human Infra 的集体底线域。

```text
武装冲突发生
  -> 生命、医疗、水、食物、住所、通信和身份同时暴露
  -> 平民保护、人道准入和医疗中立成为最低连续性条件
  -> 主体才有机会存活、获得救助、保持身份和进入恢复路径
```

## 边界

本域只整理公开国际人道法、人道保护、平民风险和服务连续性资料。

不提供：

- 作战、武器、目标选择、战术规避、情报、破坏、战场移动或准军事组织建议。
- 帮助任何一方规避国际法、监测、制裁、审计、调查或问责的内容。
- 针对具体冲突、军队、组织、地点或人员的行动指导。
- 把人道资料写成政治动员、宣传、仇恨、报复或暴力正当化材料。

## 上游与下游

- 上游：`risk-engineering/`、`governance-rights/`、`personal-safety-violence-prevention/`、`migration-displacement-humanitarian-continuity/`。
- 下游：`healthcare-access-continuity/`、`water-sanitation-hygiene-continuity/`、`food-security-nutrition-access/`、`legal-identity-civil-registration/`、`peacebuilding-conflict-prevention-social-cohesion/`。

## 初始资料线索

- ICRC protected persons and civilians: https://www.icrc.org/en/law-and-policy/protected-persons-civilians
- ICRC Geneva Conventions and commentaries: https://www.icrc.org/en/law-and-policy/geneva-conventions-and-their-commentaries
- OCHA humanitarian principles: https://www.unocha.org/publications/report/world/ocha-message-humanitarian-principles
- UN Security Council protection of civilians materials.

## 下一步

- 建立冲突场景变量表：平民伤亡、医疗可及、水电服务、粮食安全、身份文件、通信可达、家庭分离、人道准入和恢复时间。
- 整理 Source Cards：ICRC、OCHA、UN、WHO、UNHCR 等公开资料。
- 将冲突风险与 `migration-displacement-humanitarian-continuity/`、`emergency-preparedness-response/` 和 `peacebuilding-conflict-prevention-social-cohesion/` 建立上下游映射。
