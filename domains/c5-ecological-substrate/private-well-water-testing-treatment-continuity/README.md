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
