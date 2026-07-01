# Utility Affordability Shutoff Protection Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/utility-affordability-shutoff-protection-continuity` |
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


`utility-affordability-shutoff-protection-continuity/` 研究电、水、燃气、热能和通信等公共事业服务在账单压力、欠费、断供、援助、分期、消费者保护和危机豁免下如何保持主体持续性。

> 核心问题：服务系统存在不等于主体能持续使用。公用事业可负担性失败会让电、水、热、通信和医疗设备供能在家庭层面被切断，形成“基础设施存在但不可用”的断点。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要持续使用电、水、热、燃气、通信和关键家庭服务
  -> 即使基础设施存在，账单压力、欠费、资格摩擦和断供规则也可能切断服务
  -> 服务被切断会造成温控失败、饮水卫生失败、通信断线、医疗设备失效和家庭压力升级
  -> 公用事业可负担性和断供保护决定基础设施能否真实到达主体
```

## 关注对象

- 能源负担、水费负担、燃气/热能账单、通信账单、欠费、断供保护、低收入援助、分期安排、危机援助、医疗必要服务保护、消费者申诉和程序摩擦。
- 与 `energy-access-resilience/`、`water-wastewater-utility-service-continuity/` 的边界：能源/水务域关注服务生产和可及；本域关注服务存在后是否因费用、资格、欠费和断供规则被家庭实际失去。
- 与 `social-protection-benefits-delivery/` 的边界：社会保护域关注福利整体递送；本域聚焦 utility services 的 affordability、arrears、shutoff 和 lifeline protection。

## Human Infra 模型链路

```text
公用事业可负担性与断供保护
  -> 账单压力、欠费、援助入口、分期、保护规则和申诉机制可被观察
  -> 家庭电、水、热、燃气、通信和医疗设备供能被切断的概率下降
  -> 温控、卫生、通信、照护、学习、工作和数字服务连续性提升
  -> 主体获得不因支付摩擦被基础设施排除的最低生命线保障
```

## 非目标

- 不提供个体账单、断供、资格、申请、法律、债务、信用、争议、逃费、绕表或服务规避建议。
- 不承诺任何援助项目资格、金额、时效或停止断供结果。
- 不替代公用事业公司、监管机构、社会服务机构、法律援助、消费者保护和官方项目入口。

## Source Signals

- ACF LIHEAP: https://www.acf.hhs.gov/ocs/programs/liheap
- DOE Low-Income Energy Affordability Data Tool: https://www.energy.gov/scep/slsc/lead-tool
- EPA Water Infrastructure and Resiliency Finance Center: https://www.epa.gov/waterfinancecenter
- FCC Lifeline: https://www.fcc.gov/lifeline-consumers

## 下一步

- 建立公用事业负担变量表：账单负担、欠费、断供率、援助可达、资格摩擦、保护规则、申诉入口和脆弱家庭。
- 整理 LIHEAP、DOE LEAD、EPA Water Finance Center、FCC Lifeline、州监管和消费者保护公开资料卡片。
- 与能源、水务、通信、社会保护、行政负担、住房、医疗设备、热稳态和家庭应急准备域建立接口。
