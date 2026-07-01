# Nutrition Insecurity Screening Referral Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/nutrition-insecurity-screening-referral-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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


该域研究营养不安全、食物不安全和健康相关社会需求如何在医疗、公共卫生、福利和社区食物系统之间被识别、记录、转介、闭环跟踪。它把“患者缺食物”从背景变量转成主体持续性问题中的观测、导航和转接接口。

## 核心问题

- 医疗系统如何识别 nutrition insecurity / food insecurity，而不把它停留在问卷勾选。
- 筛查信号如何进入 closed-loop referral、care management、社区资源、食物药房、医学定制餐或营养治疗。
- 哪些断点会让主体从“被识别有需求”滑回“无人转接、无人跟踪、无人确认是否获得食物”。
- 筛查、转介和跟踪如何处理隐私、污名、语言、交通、数字访问和资格边界。

## 对象

- HRSN screening、food insecurity screening、nutrition insecurity screening。
- 电子健康记录、社区资源目录、closed-loop referral、社会处方和 care navigation。
- 食品银行、food pharmacy、produce prescription、medically tailored meals / groceries 和 dietitian referral。
- 隐私、同意、数据共享、污名和 follow-up 状态。

## Human Infra 价值

营养不安全会削弱恢复、注意力、慢病控制、用药执行、儿童发展、照护能力和工作学习稳定性。该域关注医疗系统是否能把“缺食物”转成可行动的支持链路，防止主体在已经被系统看见后仍然因为转介失败继续失能。

## 边界

- 只整理公开政策、项目模型、变量、证据、风险和执行断点。
- 不提供个人筛查、资格判断、转介选择、福利申请、饮食处方、医疗诊断或保险建议。
- 不收集、复制、处理或要求个人健康信息、收入、住址、食品不安全问卷答案、保险号或医疗记录。

## 上游与下游

- 上游：`food-security-nutrition-access`、`healthcare-access-continuity`、`social-prescribing-community-referral-continuity`、`patient-data-interoperability`。
- 下游：`medically-tailored-meals-chronic-care-continuity`、`medically-tailored-groceries-food-benefit-continuity`、`produce-prescription-fruit-vegetable-benefit-continuity`、`food-pharmacy-clinic-pantry-integration-continuity`、`medical-nutrition-therapy-dietitian-access-continuity`。

## 初始资料线索

- HHS Office of Disease Prevention and Health Promotion: Food Is Medicine.
- HHS ASPE: Food Is Medicine current activities.
- CMS: Medicaid Section 1115 health-related social needs guidance and demonstrations.
- USDA ERS: food security and food access resources.
- NIH Common Fund: Food is Medicine research opportunities.
