# Burn Injury Critical Care Rehabilitation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/burn-injury-critical-care-rehabilitation-continuity` |
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


`burn-injury-critical-care-rehabilitation-continuity/` 研究烧伤预防、烧伤中心、液体/感染/疼痛/手术照护、皮肤屏障修复、瘢痕和长期康复如何影响主体身体连续性。

> 核心问题：严重烧伤同时破坏皮肤屏障、体液稳态、感染防线、疼痛控制、运动功能和身份体验。它是身体边界被急性摧毁后的长期重建域。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖皮肤屏障、体温、液体平衡、感染防线和行动功能
  -> 严重烧伤可同时造成休克、感染、疼痛、瘢痕、功能损失和心理创伤
  -> 生存和恢复依赖烧伤中心、重症照护、手术修复、康复和长期支持
  -> 因此烧伤损伤是身体边界毁损后的急性救援与长期重建域
```

## 关注对象

- Burn center access、burn severity、fluid loss、infection risk、pain, grafting/reconstruction, scar, rehabilitation, return to function。
- 与 `skin-barrier-wound-healing/` 的边界：皮肤屏障域关注屏障和伤口机制；本域关注严重烧伤的系统性重症和康复链。
- 与 `trauma-system-hemorrhage-control-continuity/` 的关系：烧伤也可作为特殊创伤系统的一部分。

## Human Infra 模型链路

```text
烧伤重症与康复基础设施 T
  -> 改变烧伤中心可达、液体管理、感染控制、手术修复、疼痛和康复变量 X
  -> 改变休克、感染、皮肤屏障、运动功能、瘢痕和心理恢复状态 S
  -> 改变死亡、感染、长期残障、疼痛和社会参与损失风险 λ(t)
  -> 影响主体身体连续性、有效时间和行动能力
```

## 非目标

- 不提供烧伤急救、伤口处理、敷料、液体、止痛、抗感染、手术、瘢痕处理或个体医疗建议。
- 不生成烧伤中心选择、转运策略、工伤/保险/法律建议或事故处置方案。
- 不收集伤口照片、身份、定位、病历、烧伤机制、暴力/工伤证据或敏感康复资料。

## Source Signals

- WHO Burns Fact Sheet: https://www.who.int/news-room/fact-sheets/detail/burns
- American Burn Association: https://ameriburn.org/
- CDC Fire Safety: https://www.cdc.gov/fire-safety/

## 下一步

- 建立 Burn Continuity Card：severity, center access, infection, reconstruction, pain, scar, rehab, social reintegration。
- 与 `skin-barrier-wound-healing/`、`trauma-system-hemorrhage-control-continuity/` 和 `rehabilitation-functioning/` 建立接口。
