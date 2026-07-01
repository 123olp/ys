# Osteoarthritis Joint Function Continuity

`osteoarthritis-joint-function-continuity/` 研究骨关节炎、关节疼痛、移动能力、体重与负荷、保守治疗、关节置换路径和长期参与如何影响主体持续性。

> 核心问题：骨关节炎把慢性关节退变转化为移动半径、工作能力、照护负担和独立生活能力的长期压缩。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要稳定步行、站立、抓握和日常活动能力
  -> 骨关节炎会通过疼痛、僵硬和活动受限降低行动密度
  -> 结果取决于体重负荷、运动支持、疼痛管理、辅助技术和手术/康复路径
  -> 因此骨关节炎是移动寿命、独立生活和长期参与的关键维护域
```

## 关注对象

- Osteoarthritis、joint pain、stiffness、mobility limitation、exercise access、weight/load factors、assistive devices、joint replacement pathway、rehabilitation。
- 与 `musculoskeletal-integrity/` 的边界：该域关注肌骨完整性总机制；本域聚焦退行性关节病对移动和独立生活的影响。
- 与 `assistive-technology-access/` 的关系：辅助器具、环境改造和康复服务会改变关节病程对主体行动的实际损耗。

## Human Infra 模型链路

```text
骨关节炎关节功能维护系统 T
  -> 改变疼痛、僵硬、移动能力、体重负荷、辅助器具、康复和手术路径变量 X
  -> 改变步行半径、跌倒风险、工作参与、照护需求和生活自理状态 S
  -> 改变失能时间、有效时间损耗、独立生活概率和未来选择权 λ(t)
  -> 影响主体长期行动能力、恢复成本和资源消耗
```

## 非目标

- 不提供个人关节炎诊断、影像判读、运动处方、止痛药、注射、补充剂、手术、假体、康复或体重建议。
- 不生成个人治疗计划、设备购买、手术时机、残障、保险或工伤判断。
- 不收集个案疼痛、影像、药物、活动追踪、体重或手术资料。

## Source Signals

- NIAMS osteoarthritis: https://www.niams.nih.gov/health-topics/osteoarthritis
- CDC arthritis information: https://www.cdc.gov/arthritis/
- WHO musculoskeletal conditions: https://www.who.int/news-room/fact-sheets/detail/musculoskeletal-conditions

## 下一步

- 建立 Joint Function Card：joint site, pain interference, mobility limitation, assistive technology, rehabilitation access, surgery pathway。
- 与 `musculoskeletal-integrity/`、`assistive-technology-access/` 和 `fall-risk-prevention-home-safety-continuity/` 建立接口。
