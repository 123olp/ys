# Skin Barrier Wound Healing

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/skin-barrier-wound-healing` |
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


Skin Barrier Wound Healing 负责整理皮肤屏障、伤口愈合、压力损伤、感染入口、热调节和触觉边界如何影响主体持续性。

核心问题：

> 皮肤是主体与外界接触的最大边界；屏障破裂会把环境、感染、疼痛和失能直接接入身体系统。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须长期维持与外界之间的保护边界
  -> 皮肤负责屏障、伤口闭合、温度调节、感觉和部分免疫防御
  -> 慢性伤口、压力损伤、感染入口或屏障失效会消耗恢复资源并增加死亡/失能风险
  -> 因此皮肤屏障与伤口愈合是外界接口维护域
```

## 关注对象

- 皮肤屏障、表皮/真皮、伤口愈合阶段、瘢痕、慢性伤口和压力损伤。
- 感染入口、疼痛、瘙痒、热调节、感觉反馈、行动限制和照护负担。
- 糖尿病足、血流不足、营养状态、免疫状态、老化皮肤和长期卧床风险。
- 皮肤系统与感染、代谢、血液、循环、肌骨、康复、照护和极端环境的交叉。

## Human Infra 模型链路

```text
皮肤屏障或伤口状态 T
  -> 改变屏障完整性、愈合速度、感染入口、疼痛和热调节 X
  -> 改变主体外界防护、行动舒适度和恢复负担 S
  -> 改变感染、慢性伤口、失能和死亡风险 λ(t)
  -> 影响有效时间、独立性和长期照护需求
```

## 非目标

- 不提供伤口处理、敷料、药物、手术、压力损伤处理或急救建议。
- 不把皮肤图像、伤口大小或症状写成诊断。
- 不替代 `immune-maintenance/`、`cardiovascular-resilience/`、`nutrition-metabolic-health/` 或 `rehabilitation-functioning/`。

## Source Signals

- NCBI wound healing overview: https://www.ncbi.nlm.nih.gov/books/NBK470443/
- NCBI pressure injuries overview: https://www.ncbi.nlm.nih.gov/books/NBK553107/
- PMC skin aging and barrier review: https://pmc.ncbi.nlm.nih.gov/articles/PMC3583892/

## 下一步

1. 建立皮肤屏障变量表：屏障完整性、愈合能力、感染入口、疼痛、热调节和照护负担。
2. 与 `immune-maintenance/`、`blood-oxygen-hemostasis/`、`rehabilitation-functioning/` 和 `resource-social-infra/` 建立边界。
