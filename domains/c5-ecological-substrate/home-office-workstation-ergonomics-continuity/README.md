# Home Office Workstation Ergonomics Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-office-workstation-ergonomics-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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


`home-office-workstation-ergonomics-continuity` 研究居家办公/学习工位中的桌椅、屏幕、键鼠、照明、噪声、坐站切换和长时姿势如何影响疼痛、疲劳、注意力和生产任务连续性。

> 核心问题：远程工作和学习把“办公室的人因系统”搬进家庭，但家庭工位常由餐桌、沙发、床、临时屏幕和共享空间拼成；工位失配会把注意力、身体负荷和长期任务能力慢性消耗。

## 关注对象

- 桌椅高度、屏幕位置、键盘鼠标、笔记本支架、照明、眩光、噪声、温度、坐站变化、休息节律和共享空间冲突。
- 远程工作者、学生、照护者、自由职业者、残障者、慢性疼痛者和多成员家庭的工作/学习场景。
- 工位适配如何影响颈肩腰痛、眼疲劳、注意力、视频会议、输入效率、恢复、睡眠和长期执行。
- 与人因工效总域、家庭室内空气、照明、线缆、电力网络和心理负荷的接口。

## Human Infra 链路

```text
家庭工位与人体任务适配
  -> 姿势负荷、视觉负荷、线缆摩擦、噪声和环境干扰下降
  -> 学习、写作、编码、沟通、远程会议和恢复节律更稳定
  -> 疼痛、疲劳、注意力破碎和任务切换成本减少
  -> 主体单位时间行动质量和长期执行能力提高
```

## 非目标

- 不提供个体工位处方、医疗诊断、工伤法律建议、雇主合规意见、产品推荐、监控方案、绩效评分或采购建议。
- 不替代 OSHA、NIOSH、职业治疗师、医疗人员、雇主 EHS、人因专家或劳动法规。
- 不与 `human-factors-ergonomics-task-system-continuity` 合并；本域聚焦家庭环境中的远程办公/学习工位。

## Source Signals

- OSHA Computer Workstations eTool: https://www.osha.gov/etools/computer-workstations
- CDC NIOSH Ergonomics: https://www.cdc.gov/niosh/ergonomics/
- NIST Human Factors / Human-Centered Design: https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design

## 下一步

- 建立 `workstation fit -> body/visual/cognitive load -> task density -> continuity outcome` 变量表。
- 区分临时工位、长期远程工位、多人共享空间、照护兼容工位和低成本工位改造边界。
- 与 `human-factors-ergonomics-task-system-continuity`、`household-cord-cable-trip-entanglement-continuity` 和 `home-lighting-nighttime-pathway-visibility-continuity` 建立边界。
