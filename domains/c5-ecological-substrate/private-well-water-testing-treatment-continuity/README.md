# Private Well Water Testing Treatment Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/private-well-water-testing-treatment-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定外部承载条件：能源、水、食物、住房、通信、交通、治理、经济或公共基础设施。
- 说明它如何改变主体展开未来所需的稳定性、冗余、可获得性和安全边界。
- 记录基础设施依赖：供应链、地理环境、制度、资金、维护能力和公共服务。
- 识别冲击场景：灾害、战争、断供、污染、气候、系统失灵或社会支持崩溃。
- 建立韧性指标：可用率、恢复时间、冗余、成本、覆盖范围、可负担性和风险暴露。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

`private-well-water-testing-treatment-continuity` 研究私人井水的检测、污染识别、处理、维护、记录和替代水源如何影响家庭饮水、烹饪、清洁、婴幼儿照护和灾害恢复。

> 核心问题：私人井不是公共水务系统的自然延伸；当检测、处理或维护失败时，饮水安全从公共基础设施问题转成家庭端的持续执行负担。

## 关注对象

- 私人井、地下水、水质检测、细菌/硝酸盐/砷等污染物、井口保护、处理设备和检测记录。
- 饮水、烹饪、婴幼儿配方、刷牙、清洁、慢病脆弱人群和灾后水源恢复。
- 井水责任主体、检测频率、实验室可达、结果理解、处理维护、备用水和搬迁/租房信息不对称。
- 与公共饮水、家庭水处理、食品安全、灾害应急水和住房可持续性的接口。

## Human Infra 链路

```text
私人井水检测与处理连续
  -> 家庭端饮水风险更早可见并可治理
  -> 饮水、烹饪、清洁和婴幼儿照护更可靠
  -> 感染、毒性暴露、灾后断水和信息不对称风险下降
  -> 健康寿命、有效时间和居住稳定性增强
```

## 非目标

- 不提供水质结果判断、饮水许可、井施工、消毒步骤、药剂配比、设备选购或检测频率个案建议。
- 不替代 EPA、CDC、州/地方卫生部门、认证实验室、持证井承包商、水处理专业人员或房屋检查。
- 不把私人井问题合并进公共水务系统；本域只处理家庭自有水源的检测、处理、维护和风险转交。

## Source Signals

- EPA Private Drinking Water Wells: https://www.epa.gov/privatewells
- CDC Guidelines for Testing Well Water: https://www.cdc.gov/drinking-water/safety/guidelines-for-testing-well-water.html
- EPA Protect Your Home's Water: https://www.epa.gov/privatewells/protect-your-homes-water

## 下一步

- 建立 `well state -> test/treatment status -> household water task -> continuity outcome` 变量表。
- 区分常规检测、灾后检测、婴幼儿家庭、租赁住房、低收入维护负担和农村医疗脆弱性场景。
- 与 `water-sanitation-hygiene-continuity`、`public-drinking-water-hydration-access-continuity` 和 `emergency-food-water-storage-treatment-continuity` 建立边界。
