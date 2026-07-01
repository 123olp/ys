# Organ Donor Registry Anatomical Gift Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/organ-donor-registry-anatomical-gift-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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


Organ Donor Registry Anatomical Gift Continuity 研究器官捐赠登记、anatomical gift、授权状态、家庭沟通、驾驶证/州登记和医疗系统识别如何影响主体死亡边界后的意愿执行与他人生命连续性。

> 核心问题：主体持续性研究不能只看死亡前；死亡边界后的捐赠意愿、登记识别和家庭沟通，会把一个主体的终局转化为其他主体的生存机会。

## 研究对象

- Organ donor registry、anatomical gift law、驾驶证/州登记、撤销/更新、家庭沟通和医院识别流程。
- 器官、眼、组织捐赠与 transplant system、biovigilance 和隐私边界的关系。
- 意愿记录、身份匹配、错误登记、家庭冲突、宗教文化和公平分配问题。

## 先验链路

```text
死亡边界并不结束身体资源的社会影响
  -> 器官、眼和组织可能成为其他主体的生命维持资源
  -> 捐赠意愿必须在登记、识别、授权和家庭沟通中被保留
  -> 记录缺失、错误、不可见或冲突会导致意愿无法执行或信任受损
  -> 因而器官捐赠登记是主体意愿、身体资源和他人持续性的跨边界接口
```

## 关键变量

- 登记状态、更新/撤销、身份匹配、州系统、驾驶证标记和医院识别。
- 家庭沟通、文化信任、授权边界、分配公平、组织安全和数据隐私。
- 错误登记、身份盗用、强迫、误解、商业化和谣言风险。

## 证据入口

- OrganDonor.gov and state donor registry materials.
- HRSA organ donation and transplantation materials.
- OPTN / transplant system public materials.
- Biovigilance and anatomical gift law overview materials.

## 非目标

- 本域不建议是否登记捐赠、如何登记、如何撤销、捐赠范围、家庭沟通策略或法律选择。
- 不提供医学、法律、宗教、伦理个案判断、移植等待名单建议或死亡判定解释。
- 不收集捐赠登记、身份文件、驾驶证、病历、家庭信息或宗教/文化资料。

## 上下游

- 上游：`blood-organ-tissue-biovigilance-transplantation/`、`vital-records-life-event-continuity/`、`driver-license-vehicle-registration-continuity/`。
- 下游：`trust-estate-affairs-succession-continuity/`、`governance-rights/`、`healthcare-civil-rights-nondiscrimination-continuity/`。
