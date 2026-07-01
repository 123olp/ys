# 0128 Add One-Hundred-Twenty-Third Wave Food Is Medicine Execution Domains

Date: 2026-07-01

Status: Accepted

## Context

Human Infra 已有食物安全、食品零售、SNAP/WIC、食品银行、送餐和儿童营养项目域，但 Food is Medicine 把食物支持接入医疗筛查、慢病照护、医学定制餐、食材福利、蔬果处方、临床 pantry 和医学营养治疗。该层不是普通食物获得，也不是单纯临床建议，而是医疗系统、社区食物系统、福利支付和营养服务之间的执行连续性问题。

如果不拆出独立域，营养不安全筛查可能被混入泛化社会处方，医学定制餐和食材福利可能被混入普通送餐或 grocery，蔬果处方可能被混入普通营养教育，food pharmacy 可能被混入社区 pantry，MNT 也可能被误写成饮食建议内容。

## Decision

新增第一百二十三波 6 个 Food is Medicine / 医疗营养支持执行连续性域：

- `domains/nutrition-insecurity-screening-referral-continuity/`
- `domains/medically-tailored-meals-chronic-care-continuity/`
- `domains/medically-tailored-groceries-food-benefit-continuity/`
- `domains/produce-prescription-fruit-vegetable-benefit-continuity/`
- `domains/food-pharmacy-clinic-pantry-integration-continuity/`
- `domains/medical-nutrition-therapy-dietitian-access-continuity/`

这些域只整理公开政策、研究、项目模型、变量、证据等级、执行断点和安全边界，不提供个体医学、营养、保险、福利、转介、菜单、购物、供应商或 eligibility 建议。

## Consequences

- Human Infra 可以把营养支持从“食物是否存在”推进到“医疗系统如何识别、转介、支付、交付、兑换和专业治疗”。
- Food is Medicine 的每条路径都有独立对象、证据和失败模式，便于后续写 Source Cards、变量卡和可视化模型。
- 项目边界更严格：任何个体饮食、疾病管理、保险覆盖、福利申请、具体资源推荐或个人数据处理都必须留在禁止区。
