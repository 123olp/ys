# Pelvic Floor Continence Function Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/pelvic-floor-continence-function-continuity` |
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


`pelvic-floor-continence-function-continuity/` 研究盆底功能、尿失禁、便失禁、盆腔器官脱垂、产后/老年功能恢复、羞耻和服务可及如何影响主体持续性。

> 核心问题：盆底和控尿控便功能直接影响行动半径、睡眠、社交、工作、照护负担和尊严，是有效时间与社会参与的隐性基础设施。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要可预测的排泄控制、行动半径、睡眠和尊严维持日常任务
  -> 盆底功能障碍会通过失禁、疼痛、感染、跌倒、社交回避和照护负担消耗有效时间
  -> 结果取决于筛查沟通、治疗转介、康复可及、用品可及和非污名环境
  -> 因此盆底与控尿控便功能是身体行动和社会参与之间的关键域
```

## 关注对象

- Pelvic floor function、urinary incontinence、fecal incontinence、pelvic organ prolapse、postpartum recovery, aging continence, pelvic floor physical therapy access, continence supplies, stigma。
- 与 `urogenital-continuity/` 的边界：该域关注泌尿生殖总机制；本域关注盆底、控尿控便和功能参与连续性。
- 与 `fall-risk-prevention-home-safety-continuity/` 的关系：夜尿、急迫性和浴厕环境可放大跌倒风险。

## Human Infra 模型链路

```text
盆底与控尿控便支持系统 T
  -> 改变症状识别、康复可及、用品可及、浴厕环境、羞耻和转介变量 X
  -> 改变行动半径、睡眠、感染风险、社交参与、照护负担和尊严状态 S
  -> 改变有效时间损失、跌倒、隔离、工作退出和生活质量下降 λ(t)
  -> 影响主体日常行动、关系参与、恢复和长期独立性
```

## 非目标

- 不提供个人失禁诊断、盆底训练步骤、用药、器械、手术、产后恢复计划、用品选择或医疗建议。
- 不生成个人症状评分、康复方案、检查排序、家庭处理、保险申诉或临床分诊。
- 不收集个案排泄、性健康、产后、手术、影像、药物、浴厕环境或身份敏感资料。

## Source Signals

- NIDDK urinary incontinence: https://www.niddk.nih.gov/health-information/urologic-diseases/bladder-control-problems
- NIDDK fecal incontinence: https://www.niddk.nih.gov/health-information/digestive-diseases/fecal-incontinence
- HHS OWH urinary incontinence: https://www.womenshealth.gov/a-z-topics/urinary-incontinence

## 下一步

- 建立 Pelvic Floor Continuity Card：symptoms, referral, rehabilitation access, supplies, bathroom environment, stigma, participation。
- 与 `urogenital-continuity/`、`rehabilitation-functioning/` 和 `fall-risk-prevention-home-safety-continuity/` 建立接口。
