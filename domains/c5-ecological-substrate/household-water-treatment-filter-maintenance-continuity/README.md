# Household Water Treatment Filter Maintenance Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/household-water-treatment-filter-maintenance-continuity` |
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


`household-water-treatment-filter-maintenance-continuity` 研究家庭滤水器、点用/点入处理设备、滤芯更换、认证声明、维护失败和污染物降低边界如何影响饮水、烹饪和信任。

> 核心问题：家庭水处理不是一次性安装物，而是需要认证匹配、滤芯更换和维护纪律的运行系统；维护失败时，安全感可能超过真实保护能力。

## 关注对象

- 家庭滤水器、pitcher、龙头式、台下式、全屋式、反渗透、UV、滤芯更换和认证声明。
- 铅、氯味、微生物、沉积物等不同目标污染物与设备声明的错配。
- 安装维护、滤芯可得、费用、提醒、使用量、旁路、老年/租房/灾后家庭和低收入负担。
- 与私人井、铅铜管线、公共饮水、紧急水处理和消费者产品信任的接口。

## Human Infra 链路

```text
家庭水处理维护连续
  -> 家庭端水质改善能力与目标污染物匹配
  -> 滤芯、认证、维护和使用记录更可靠
  -> 饮水、烹饪、婴幼儿照护和风险沟通摩擦下降
  -> 主体健康风险、时间成本和信任误差下降
```

## 非目标

- 不提供滤水器购买推荐、安装教程、滤芯选择、饮水许可、水质结果判断或污染物处理个案建议。
- 不替代 EPA、CDC、NSF/ANSI 认证体系、州/地方卫生部门、水处理专业人员或水务通知。
- 不把过滤器当成所有污染物的通用解决方案；本域只处理家庭水处理的运行连续性和边界。

## Source Signals

- CDC Home Water Treatment Systems: https://www.cdc.gov/drinking-water/about/about-home-water-treatment-systems.html
- CDC Choosing Home Water Filters: https://www.cdc.gov/drinking-water/prevention/about-choosing-home-water-filters.html
- EPA Certified Filters to Reduce Lead: https://www.epa.gov/water-research/consumer-tool-identifying-point-use-and-pitcher-filters-certified-reduce-lead

## 下一步

- 建立 `filter claim -> contaminant target -> maintenance state -> water task -> continuity outcome` 变量表。
- 区分公共水、私人井、铅风险、灾后、租房和婴幼儿家庭场景。
- 与 `private-well-water-testing-treatment-continuity`、`lead-service-line-lead-copper-drinking-water-continuity` 和 `emergency-food-water-storage-treatment-continuity` 建立边界。
