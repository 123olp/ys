# Chronic Infectious Disease Care Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/chronic-infectious-disease-care-continuity` |
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


慢性与长疗程传染病照护连续性域研究：当 HIV、结核、病毒性肝炎等疾病需要长期检测、治疗、随访、去污名和公共卫生协同时，个体健康寿命与社区风险屏障如何共同维持。

## 对象

- HIV、结核、病毒性肝炎和其他需要长期随访、治疗、耐药监测或公共卫生协同的传染病。
- 筛查系统、确诊路径、治疗连续性、药物可及、依从支持、实验室监测、耐药和失访。
- 污名、隐私、接触服务、公共卫生报告、社区支持、移民/无家可归/羁押场景中的服务断点。
- 个体器官损伤、免疫状态、机会性感染、传播风险、公共卫生屏障和治疗窗口。
- 慢性传染病对健康寿命、有效时间、关系网络、工作能力和未来选择权的影响。

## Human Infra 价值

慢性传染病不是单次感染事件，而是长期治疗、监测、药物、隐私、去污名和公共卫生协同的连续系统。这个域把个体持续性和群体屏障放在同一模型里，避免只看“是否有药”，忽略失访、耐药、污名和服务断线。

```text
慢性和长疗程传染病被连续检测、治疗和支持
  -> 传播、耐药、器官损伤、污名和照护中断下降
  -> 个体健康寿命与公共卫生屏障同步提高
  -> 主体持续性和社区风险韧性提高
```

## 边界

本域只整理公开 HIV、结核、病毒性肝炎、长期感染照护、公共卫生、治疗连续性和去污名资料。

不提供：

- 个体检测、诊断、治疗、用药、停药、PEP/PrEP、隔离、暴露后处理或医疗决策。
- 传播规避、接触追踪逃避、公共卫生报告规避、检测规避、实验室操作或病原体处理方法。
- 对感染者、接触者、社群、职业、国籍、羁押或无家可归群体的污名化、定位或歧视性筛选。
- 把公共卫生资料写成确定个人风险、关系判断、入境/就业/保险策略或法律建议。

## 上游与下游

- 上游：`immunization-public-health-surveillance/`、`antimicrobial-resilience/`、`medicine-access-treatment-continuity/`、`health-data-privacy-governance/`、`clinical-laboratory-diagnostic-quality/`。
- 下游：`immune-maintenance/`、`renal-hepatic-clearance/`、`social-connection-relational-infra/`、`governance-rights/`。

## 初始资料线索

- WHO HIV, tuberculosis and hepatitis resources。
- CDC HIV, TB and hepatitis resources。
- UNAIDS, Stop TB Partnership and viral hepatitis elimination public materials。
- Public materials on treatment continuity, stigma reduction, contact services and drug resistance。
