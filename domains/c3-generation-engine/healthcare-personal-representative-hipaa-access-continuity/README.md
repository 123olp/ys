# Healthcare Personal Representative HIPAA Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/healthcare-personal-representative-hipaa-access-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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


Healthcare Personal Representative HIPAA Access Continuity 关注 HIPAA personal representative、授权照护者、医疗记录访问、隐私边界和代理访问如何在主体失能、转诊、照护协调或长期照护中保持医疗信息连续性。

## 对象

- HIPAA personal representative、授权照护者、医疗代理人、家属访问和患者门户代理访问。
- 医疗记录、检验结果、用药、转诊、出院文件、保险信息和远程照护数据的授权共享。
- 隐私保护、越权访问、家庭冲突、照护者任务负担和跨机构数据断点。

## Human Infra 价值

```text
主体持续性需要医疗信息在授权边界内可传递
-> 失能、慢病和照护转移会让主体无法亲自汇总和解释资料
-> 若照护者无合法访问路径，药物、结果、预约和风险信息会断裂
-> 若访问边界过宽，主体隐私和安全又会被侵蚀
-> 个人代表和授权访问机制把信息连续性与隐私控制放在同一框架
-> 医疗照护更可能被复核、协调和持续执行
```

## 边界

- 本域不提供 HIPAA 法律意见、授权表填写、病历索取策略、门户设置、隐私投诉或家庭纠纷建议。
- 不判断某人是否有权访问特定病历或机构是否违反隐私规则。
- 不替代 HHS OCR、医疗机构隐私官、律师、患者代表或监管机构。
- 只整理公开资料、角色边界、信息流断点、授权模型和禁止用途。

## 上游与下游

- 上游：`patient-data-interoperability/`、`health-data-privacy-governance/`、`caregiving-long-term-care/`、`care-transitions-discharge-continuity/`。
- 下游：`advance-care-planning-medical-decision-continuity/`、`patient-advocacy-shared-decision-making/`、`telehealth-remote-monitoring-access/`。

## 初始资料线索

- HHS HIPAA guidance on personal representatives.
- HHS OCR patient access and privacy guidance.
- ONC patient access, portal, and interoperability resources.
