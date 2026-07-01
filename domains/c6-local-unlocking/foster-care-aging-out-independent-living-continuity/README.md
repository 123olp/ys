# Foster Care Aging Out Independent Living Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/foster-care-aging-out-independent-living-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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


寄养出离、独立生活和成年转接连续性，关注青年从寄养、亲属照护、团体安置或儿童福利系统进入成年时，住房、医保、教育、就业、身份证件、财务账户、情感支持、永久关系和生活技能如何不中断。

## 对象

- Foster care aging out
- Chafee independent living services
- Extended foster care
- Education and training voucher
- Housing transition
- Medicaid and health coverage transition
- Identity documents and records
- Permanent supportive relationships

## Human Infra 价值

寄养出离是主体持续性的高风险边界：系统保护结束并不等于成年能力已经形成。该域把成年转接建模为一组可维护的支持接口，防止青年在住房、医疗、教育、收入、身份和关系网络上同时掉线。

## 边界

- 不提供寄养、收养、监护、法院、福利、住房、医保、身份文件、教育资助、个案管理或法律建议。
- 不判断个体资格、安置适配、家庭关系、服务优先级或风险等级。
- 不替代儿童福利机构、法院、学校、医疗、住房、法律援助或危机服务。

## 上游与下游

- 上游：`kinship-foster-adoption-care-continuity/`、`child-protection-family-safety/`、`family-law-custody-child-support-continuity/`。
- 下游：`opportunity-youth-education-employment-pathway-continuity/`、`campus-basic-needs-student-support-continuity/`、`health-insurance-enrollment-renewal-continuity/`。

## 初始资料线索

- ACF Children's Bureau Chafee Foster Care Program for Successful Transition to Adulthood.
- Youth.gov transition-age foster youth resources.
- Medicaid and child welfare transition coverage materials.
