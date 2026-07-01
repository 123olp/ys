# Emergency Supply Kit Go Bag Rotation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/emergency-supply-kit-go-bag-rotation-continuity` |
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


`emergency-supply-kit-go-bag-rotation-continuity/` 研究应急物资包、随身撤离包、耗材轮换和家庭可取用性如何影响主体在灾害早期维持行动的能力。

> 核心问题：灾害不是从救援抵达时开始，而是从水、电、药品、通信、照明和基本用品无法即时取得时开始消耗主体持续性。

## 先验位置

```text
主体要持续行动
  -> 必须在外部服务中断初期维持最低生存与执行能力
  -> 物资包决定水、食物、药品、照明、通信和卫生用品是否可被迅速取用
  -> 因而应急物资包是灾害早期行动窗口的前置条件
```

## 关注对象

- 家庭应急包、撤离包、轮换周期、可达位置、照明、电池、卫生用品、基础通信用品和特殊人群用品。
- 独居者、儿童家庭、残障者、慢病患者、照护者、宠物家庭和服务中断风险较高地区。

## Human Infra 模型链路

```text
应急物资包与轮换系统 T
  -> 改变水食、照明、卫生、药品、通信、可取用性和过期失效变量 X
  -> 改变主体在服务中断初期的自持状态 S
  -> 改变脱水、低血糖、用药中断、恐慌、无法撤离和求助失败风险 λ(t)
  -> 改变灾害早期有效时间、恢复机会和未来选择权
```

## 非目标

- 不提供个人物资清单、采购建议、储存数量、撤离包配置、品牌推荐或灾害现场行动指导。
- 不收集家庭住址、库存照片、药品清单、身份证件、现金储备、儿童/老人信息或撤离路线。

## Source Signals

- Ready.gov emergency kit materials: https://www.ready.gov/kit
- American Red Cross emergency preparedness kit materials: https://www.redcross.org/get-help/how-to-prepare-for-emergencies/survival-kit-supplies.html
