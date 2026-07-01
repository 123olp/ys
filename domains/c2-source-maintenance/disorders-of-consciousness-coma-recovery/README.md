# Disorders Of Consciousness Coma Recovery

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/disorders-of-consciousness-coma-recovery` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 直接维护身体、脑、器官、衰老、损伤或生命系统这些可能性源体。 |
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


`disorders-of-consciousness-coma-recovery/` 研究昏迷、植物状态/无反应觉醒综合征、最低意识状态、意识评估、预后、康复和照护伦理，如何影响 Human Infra 的主体连续性判定。

> 核心问题：有效永生不能只问“身体是否还活着”。当意识、反应、沟通和主观体验无法确认时，主体持续性进入最困难的边界：存在状态、恢复机会、代理决策和尊严保护必须同时审查。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续性要求存在、感知、沟通、恢复机会和代理决策边界
  -> 意识障碍使“活着”“清醒”“有体验”“可恢复”“仍是主体”之间的关系变得不确定
  -> 若评估不足、误诊、预后过度确定或照护伦理失衡，主体可能被过早放弃或被无意义维持
  -> 因此意识障碍和昏迷恢复是主体连续性最硬的边界域
```

## 关注对象

- 昏迷、无反应觉醒综合征、最低意识状态、locked-in 综合征鉴别、意识评估和长期康复。
- CRS-R、神经影像、脑电、预后不确定性、替代决策、长期照护、沟通技术和伦理边界。
- 与 `disembodied-cns/` 的边界：去具身中枢域关注中枢生命系统维持架构；本域关注现有医学中的意识状态评估和恢复边界。
- 与 `governance-rights/` 的边界：治理权利域关注同意和代理；本域关注意识不确定状态下的主体连续性判定。

## Human Infra 模型链路

```text
意识障碍评估与恢复 T
  -> 改变意识评估、误诊率、神经恢复机会、沟通接口、照护质量和代理决策变量 X
  -> 改变主体是否可感知、可沟通、可恢复和可被尊严照护的状态 S
  -> 改变误放弃、无意义维持、痛苦、照护崩溃和身份连续性误判风险 λ(t)
  -> 影响主体连续性定义、有效永生边界和医疗伦理治理
```

## 非目标

- 不提供昏迷评估、预后判断、撤治建议、生命支持决策或个案伦理判断。
- 不替代神经科、康复医学、ICU、伦理委员会、法律代理或照护团队。
- 不把单次反应、影像、脑电或 AI 预测写成意识存在或恢复概率结论。

## Source Signals

- NINDS Coma: https://www.ninds.nih.gov/health-information/disorders/coma
- AAN Disorders of Consciousness guideline summary: https://www.aan.com/Guidelines/home/GuidelineDetail/930
- Model Systems Knowledge Translation Center Disorders of Consciousness: https://msktc.org/tbi/factsheets/disorders-consciousness
- Royal College of Physicians prolonged disorders of consciousness guideline: https://www.rcp.ac.uk/improving-care/resources/prolonged-disorders-of-consciousness-guidelines/

## 下一步

- 建立意识连续性变量表：状态分类、评估工具、误诊风险、沟通能力、恢复窗口、代理决策、痛苦和长期照护。
- 与 `neuro-continuity/`、`disembodied-cns/`、`governance-rights/`、`brain-preservation-connectomics-emulation/` 和 `home-health-hospice-palliative-care-continuity/` 建立接口。
