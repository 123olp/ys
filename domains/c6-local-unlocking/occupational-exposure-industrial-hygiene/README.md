# Occupational Exposure Industrial Hygiene

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/occupational-exposure-industrial-hygiene` |
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


职业暴露与工业卫生域研究：当主体通过工作获取资源、身份和技能时，化学、物理、生物、噪声、粉尘、热、辐射和人体工效暴露如何决定工作是否消耗未来身体能力。

## 对象

- 工作场所化学品、粉尘、烟雾、气体、噪声、振动、热应激、辐射、生物危害和皮肤暴露。
- 暴露识别、评估、监测、控制层级、替代、工程控制、行政控制和个人防护边界。
- 工业卫生、职业病预防、职业暴露限值、工伤风险、承包/零工/弱势劳动者暴露。
- 工作设计、生产压力、培训、报告、监管、工会/劳动权利和雇主安全责任接口。
- 职业暴露对健康寿命、有效时间、收入连续性、家庭照护和长期行动能力的影响。

## Human Infra 价值

工作不应以消耗未来身体作为当前收入的隐性代价。职业暴露与工业卫生域把“劳动环境是否持续保存身体、感官、呼吸、神经和恢复能力”纳入主体持续性模型，使工作从资源入口扩展为风险控制对象。

```text
职业暴露被识别、评估和控制
  -> 工作导致的损伤、疾病和长期能力损耗下降
  -> 收入、技能、身体功能和家庭连续性更稳定
  -> 主体可持续劳动与未来选择权提高
```

## 边界

本域只整理工业卫生、职业暴露控制、控制层级、标准、监管和公共资料。

不提供：

- 个体职业病诊断、工伤认定、法律、赔偿、投诉、劳动争议或就业建议。
- 现场检测、采样、PPE 选择、通风设计、危险作业、清理或事故处置步骤。
- 化学品、粉尘、辐射、生物危害或高温高噪环境的具体操作规程。
- 规避 OSHA/监管、篡改监测、隐藏暴露、压制报告或危险生产建议。

## 上游与下游

- 上游：`occupational-work-design/`、`labor-rights-workplace-protection/`、`chemical-safety-poison-control-toxicology/`、`air-quality-ventilation-exposure-control/`。
- 下游：`respiratory-oxygenation/`、`sensory-continuity/`、`skin-barrier-wound-healing/`、`musculoskeletal-integrity/`、`risk-engineering/`。

## 初始资料线索

- NIOSH hierarchy of controls resources。
- OSHA industrial hygiene and worker safety resources。
- ILO occupational safety and health resources。
- ACGIH industrial hygiene and exposure guideline resources。
