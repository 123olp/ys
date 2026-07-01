# Temporomandibular Orofacial Pain Jaw Function Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/temporomandibular-orofacial-pain-jaw-function-continuity` |
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


`temporomandibular-orofacial-pain-jaw-function-continuity/` 负责整理颞下颌关节障碍、口颌面痛、颌功能、咀嚼言语和睡眠连续性。

核心问题：

> 颌面功能是进食、说话、表情和疼痛承受的运动接口；慢性口颌面痛会把任务执行变成持续的注意力税。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能开口、咀嚼、说话、休息并承受可管理的疼痛负担
  -> 颞下颌关节、咀嚼肌、牙列和神经疼痛系统共同决定颌面功能
  -> TMD 和口颌面痛会影响饮食、语言、睡眠、情绪和工作能力
  -> 因此颌功能连续性是口腔系统、疼痛系统和沟通系统的交叉条件
```

## 关注对象

- 颞下颌关节障碍、咀嚼肌痛、口颌面痛、开口受限、咀嚼困难和睡眠/压力交叉。
- 慢性疼痛、焦虑压力、睡眠、工作参与、社会沟通和服务路径。
- 牙科、疼痛医学、物理治疗、心理支持和多学科照护边界。
- 与 `pain-suffering-control/` 的关系：本域聚焦颌面机制；痛苦域关注整体痛苦和可承受性。

## Human Infra 模型链路

```text
颌面疼痛 / 颌功能支持 T
  -> 改变开口、咀嚼、言语、睡眠、疼痛、压力和服务可及性变量 X
  -> 改变主体口颌运动和痛苦负担状态 S
  -> 改变饮食受限、沟通退缩、注意力损耗和工作能力下降风险
  -> 增加有效时间、表达能力和任务执行稳定性
```

## 非目标

- 不提供 TMD 诊断、咬合判断、护牙套、练习、用药、影像、手术或个体治疗建议。
- 不根据弹响、疼痛位置、照片或影像判断病因。
- 不替代牙医、口腔颌面外科、疼痛医学、物理治疗或心理健康专业评估。

## Source Signals

- NIDCR TMD: https://www.nidcr.nih.gov/health-info/tmd
- NIDCR Facial Pain: https://www.nidcr.nih.gov/health-info/facial-pain
- WHO Oral Health: https://www.who.int/news-room/fact-sheets/detail/oral-health

## 下一步

- 建立 TMD 与口颌面痛 Source Card，覆盖颌功能、慢性痛、睡眠、压力和服务路径。
- 对接疼痛、睡眠、语言沟通、营养和牙科可及性域。
