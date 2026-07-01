# Benign Prostatic Hyperplasia and LUTS Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/benign-prostatic-hyperplasia-luts-continuity` |
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


`benign-prostatic-hyperplasia-luts-continuity/` 研究良性前列腺增生、下尿路症状、夜尿、尿潴留、感染和生活质量负担如何影响主体持续性。

> 核心问题：BPH/LUTS 常以慢性摩擦出现，但会通过睡眠破坏、急性尿潴留、感染、工作与社交限制压缩有效时间。

## 先验位置

```text
有效永生
  -> 主体需要低摩擦排尿和稳定睡眠
  -> 前列腺增生可造成下尿路症状和排空失败
  -> 因此 BPH/LUTS 是男性排泄出口和有效时间交叉域
```

## 关注对象

- Benign prostatic hyperplasia, lower urinary tract symptoms, nocturia, weak stream, retention risk, infection, quality of life, sexual side-effect boundary。
- 与 `prostate-cancer-screening-treatment-continuity/` 的边界：该域关注癌症筛查治疗，本域关注非癌性下尿路症状和排泄连续性。

## Human Infra 模型链路

```text
BPH/LUTS 识别与服务可及 T
  -> 改变夜尿、排空、急性尿潴留、感染和生活质量 X
  -> 改变睡眠、行动、工作、关系和排泄安全状态 S
  -> 改变跌倒、感染、急诊、照护依赖和有效时间损失 lambda(t)
  -> 改变健康寿命和未来选择权
```

## 非目标

- 不提供 PSA 判断、BPH 诊断、药物、手术、导尿、补剂、性功能治疗或个体泌尿建议。
- 不输出个人风险、症状评分解释、用药选择、癌症排除或医疗机构选择。

## Source Signals

- NIDDK prostate enlargement / benign prostatic hyperplasia materials.
- MedlinePlus benign prostatic hyperplasia public materials.
- AUA terminology references for LUTS boundary.
