# Eye Injury Urgent Vision Protection Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/eye-injury-urgent-vision-protection-continuity` |
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


`eye-injury-urgent-vision-protection-continuity/` 负责整理眼外伤、化学/机械/异物损伤、紧急转诊、防护装备和急性视觉保护连续性。

核心问题：

> 眼外伤是分钟到小时级的视觉连续性断点；它把工作场所、家庭、运动、化学暴露和急诊通道连接成一条高后果风险链。

## 先验位置

```text
主体持续性最大化
  -> 主体必须避免可预防的急性视觉输入崩溃
  -> 机械、化学、热、辐射或异物伤害可快速造成不可逆视损
  -> 防护、识别、急诊通道和转诊延迟决定视觉损害是否被放大
  -> 因此眼外伤紧急保护连续性是视觉输入的急性风险防线
```

## 关注对象

- 眼外伤、化学暴露、异物、穿通伤、烧伤、运动和工作场所眼伤。
- 护目镜、防护标准、急诊转诊、职业安全、儿童/家庭风险和恢复随访。
- 视觉丢失、工作能力、学习运动、疼痛、心理影响和照护成本。
- 与 `occupational-exposure-industrial-hygiene/` 的关系：本域聚焦眼部急性伤害；职业暴露域负责更广泛的作业风险。

## Human Infra 模型链路

```text
眼部防护 / 暴露控制 / 急诊转诊 T
  -> 改变外伤暴露、防护装备、处理延迟、损伤严重度和随访变量 X
  -> 改变主体视觉功能、疼痛、工作学习参与和恢复状态 S
  -> 改变不可逆视损、感染、失能、工作退出和长期照护风险
  -> 保护急性视觉连续性、行动能力和未来选择权
```

## 非目标

- 不提供眼外伤急救步骤、冲洗时长、取异物、药物、包扎、复工返赛许可或个体处置建议。
- 不根据症状或图片判断是否需要急诊、损伤程度、感染风险或法律责任。
- 不替代急诊、眼科、职业安全、学校/运动医疗或毒物控制服务。

## Source Signals

- National Eye Institute Eye Injuries: https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/eye-injuries
- CDC/NIOSH Eye Safety: https://www.cdc.gov/niosh/topics/eye/
- American Academy of Ophthalmology Eye Injuries: https://www.aao.org/eye-health/tips-prevention/injuries

## 下一步

- 建立眼外伤 Source Card，区分防护、暴露、急诊通道、复工和长期功能终点。
- 对接职业安全、儿童保护、运动安全、急诊转诊和创伤系统域。
