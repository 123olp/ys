# Child Care Availability Affordability Continuity

`child-care-availability-affordability-continuity/` 研究儿童照护名额、费用、时段、距离和年龄覆盖是否让家庭真正接上稳定照护，而不是只在名义上存在托育市场。

> 核心问题：托育服务存在不等于家庭可用；如果名额不足、费用过高、时段不匹配或地理距离过远，照护者的工作、学习、恢复和收入连续性会被直接切断。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 儿童需要稳定安全的日常照护
  -> 照护者需要可预测的时间、收入和恢复窗口
  -> 托育名额、费用、时段、距离和年龄覆盖必须可承受
  -> 家庭才不会被照护缺口压缩有效时间和未来选择权
```

## 关注对象

- 托育名额供给、等待名单、年龄段覆盖、营业时段、通勤距离和可负担性。
- 家庭费用负担、市场供需、照护安排稳定性、非正式照护和备用照护缺口。
- 与 `childcare-family-continuity/`、`child-care-subsidy-ccdf-payment-continuity/`、`social-protection-benefits-delivery/`、`workforce-employment-services/` 和 `time-allocation-effective-time/` 的接口。

## Human Infra 模型链路

```text
儿童照护需求
  -> 可用名额、可承受费用、时段覆盖和地理可达性
  -> 照护者工作学习恢复时间得到保留
  -> 家庭压力、收入中断和儿童照护不稳定下降
  -> 两代主体的有效时间和未来选择权增加
```

## 非目标

- 不推荐具体托育机构、价格、地点、排队策略或家庭照护安排。
- 不判断个体资格、费用承受能力、补贴申请、机构质量或儿童适配性。
- 不收集儿童身份、家庭收入、工作排班、住址、托育记录或候补名单资料。

## Source Signals

- ACF Office of Child Care: https://www.acf.hhs.gov/occ
- ChildCare.gov: https://childcare.gov/
- National Survey of Early Care and Education: https://www.acf.hhs.gov/opre/project/national-survey-early-care-and-education-2019-2017-2022
- Census Child Care: https://www.census.gov/topics/families/child-care.html

## 下一步

- 建立变量表：名额、费用、时段、距离、年龄覆盖、等待时间、备用照护和照护稳定性。
- 整理 ACF OCC、ChildCare.gov、NSECE 和 Census child care 的 Source Cards。
- 与 `childcare-family-continuity/` 区分：本域只处理供给可得性和费用可承受性执行层。
