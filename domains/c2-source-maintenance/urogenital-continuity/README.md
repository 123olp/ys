# Urogenital Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/urogenital-continuity` |
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


Urogenital Continuity 负责整理膀胱、尿路、盆底、尿控、泌尿感染、性功能和日常尊严如何支撑主体持续性。

核心问题：

> 主体持续性不只是避免死亡，也包括保持可行动、可参与、可自理和有尊严的生活；泌尿生殖功能失稳会通过感染、疼痛、睡眠破坏、社会退缩和照护负担侵蚀有效时间。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须维持排泄控制、泌尿安全和身体自主性
  -> 尿控、感染、盆底功能和性/生殖相关功能影响睡眠、行动、关系、尊严和照护负担
  -> 泌尿生殖功能失败会把长期存在转化为痛苦、隔离和依赖
  -> 因此泌尿生殖连续性是主体持续性的功能与尊严域
```

## 关注对象

- 膀胱、尿路、尿控、尿频、夜尿、盆底、泌尿感染、性功能和相关生活质量。
- 尿失禁、尿路感染、慢性盆腔/泌尿疼痛、夜间睡眠中断、照护负担和社会参与。
- 泌尿生殖功能如何进入睡眠、心理稳定、疼痛、康复、照护、感染和身份尊严模型。
- 与生殖生育域的边界：本域关注主体当下功能、尿路安全和生活质量；生殖生育域关注生育窗口和未来选择权。

## Human Infra 模型链路

```text
泌尿生殖因素 T
  -> 改变尿控、感染风险、疼痛、睡眠中断、性功能和盆底支持 X
  -> 改变主体自理、行动、关系、尊严和有效时间状态 S
  -> 改变感染、跌倒、失眠、抑郁、失能和照护依赖风险 λ(t)
  -> 影响健康寿命、有效时间和未来选择权
```

## 非目标

- 不提供泌尿、生殖、性功能、盆底训练、感染、药物、器械、手术或检查解释建议。
- 不把尿频、尿控、性功能或感染症状写成个体诊断。
- 不替代 `renal-hepatic-clearance/`、`pain-suffering-control/` 或 `reproductive-fertility-continuity/`，而是承载泌尿生殖功能与尊严主接口。

## Source Signals

- NIDDK urologic diseases: https://www.niddk.nih.gov/health-information/urologic-diseases
- NIDDK bladder control problems: https://www.niddk.nih.gov/health-information/urologic-diseases/bladder-control-problems
- CDC urinary tract infection basics: https://www.cdc.gov/uti/about/index.html

## 下一步

1. 建立泌尿生殖连续性变量表：尿控、感染、夜尿、疼痛、盆底、性功能、照护负担和尊严。
2. 与 `sleep-circadian-recovery/`、`pain-suffering-control/`、`immune-maintenance/` 和 `reproductive-fertility-continuity/` 建立交叉边界。
