# Pollen Allergen Asthma Outdoor Activity Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pollen-allergen-asthma-outdoor-activity-continuity` |
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


`pollen-allergen-asthma-outdoor-activity-continuity` 研究花粉、季节性过敏、哮喘触发、户外行动和工作/学习窗口如何影响主体持续性。

> 核心问题：花粉不是单纯不适；当过敏、哮喘、睡眠破坏和户外回避叠加时，它会把季节性环境暴露转化为注意力、体力、出勤和行动半径的长期折扣。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须在季节性环境变化中维持呼吸、睡眠、注意力和行动能力
  -> 花粉和空气过敏原会触发鼻炎、眼部症状、哮喘加重和疲劳
  -> 监测、预警、室内过滤、症状管理连接和户外安排构成行动前提
  -> 若该前提失败，学习、工作、运动、通勤和恢复时间都会被季节性压缩
```

## 关注对象

- 花粉、季节性过敏、过敏性鼻炎、哮喘触发、眼鼻症状、睡眠和户外活动限制。
- 花粉预报、空气质量、室内外暴露、学校/工作场所调整、慢病管理连接和风险沟通。
- 与 `respiratory-oxygenation/` 的边界：上位域关注呼吸系统和氧合；本域关注花粉过敏原如何在季节性环境中压缩行动窗口。

## Human Infra 链路

```text
花粉暴露被识别和管理
  -> 过敏症状、哮喘加重和睡眠破坏减少
  -> 户外行动、学习出勤、工作效率和恢复节律更稳定
  -> 有效时间、注意力和未来选择权被保护
```

## 非目标

- 不提供诊断、药物、剂量、免疫治疗、急性哮喘处理、空气净化器购买或个体户外安全结论。
- 不替代医疗机构、过敏/呼吸专科、学校健康服务、职业健康或公共卫生空气质量提示。
- 不把花粉预报、AQI、气象数据或 AI 输出写成个体发作概率、治疗方案或活动许可。

## Source Signals

- CDC Asthma: https://www.cdc.gov/asthma/
- CDC Allergies and Hay Fever: https://www.cdc.gov/nchs/fastats/allergies.htm
- EPA Asthma Triggers: https://www.epa.gov/asthma

## 下一步

- 建立 `pollen exposure -> allergic inflammation -> sleep/respiration/attention cost -> activity continuity` 变量表。
- 区分儿童学校、户外劳动、运动训练、慢性哮喘、城市绿化和气候变化场景。
