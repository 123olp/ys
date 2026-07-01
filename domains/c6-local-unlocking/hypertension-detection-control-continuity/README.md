# Hypertension Detection Control Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/hypertension-detection-control-continuity` |
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


`hypertension-detection-control-continuity/` 研究高血压筛查、确认、家庭/门诊测量质量、长期控制、随访坚持和靶器官风险预防如何影响主体持续性。

> 核心问题：高血压常在无症状阶段持续改变卒中、心衰、肾衰和血管事件风险。有效永生需要把“发现、确认、控制和长期坚持”建模为急性危象之前的上游风险治理层。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖稳定血管压力环境维持脑、心、肾和眼底功能
  -> 高血压可长期无症状地提高多器官风险函数
  -> 结果取决于筛查、确认、随访、治疗可及、行为环境和坚持系统
  -> 因此高血压检测与控制是急性靶器官损害之前的预防执行域
```

## 关注对象

- Hypertension screening、office / out-of-office BP measurement、confirmation、control rate、treatment adherence、follow-up interval、team-based care、home BP device access。
- 与 `cardiovascular-resilience/` 的边界：该域关注心血管韧性总机制；本域关注血压风险被发现、确认、控制和长期坚持的执行链。
- 与 `hypertensive-crisis-end-organ-risk-continuity/` 的关系：本域处理危象之前的长期风险控制，后者处理急性靶器官损害窗口。

## Human Infra 模型链路

```text
高血压检测与控制系统 T
  -> 改变测量准确性、确认率、控制率、随访坚持和药物/生活环境可及变量 X
  -> 改变血管负荷、心脑肾眼底状态和长期器官储备 S
  -> 改变卒中、心衰、肾衰、急性危象和有效时间损失 λ(t)
  -> 影响主体行动能力、认知稳定和未来选择权
```

## 非目标

- 不提供个人血压读数判断、降压药、剂量、家庭处理、设备购买、检查排序、急诊分诊或个体医疗建议。
- 不生成个人风险评分、治疗目标、生活方式处方、用药调整、远程监测策略或保险申诉。
- 不收集个案血压、病史、用药、实验室、位置、设备或诊疗资料。

## Source Signals

- USPSTF hypertension screening: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/hypertension-in-adults-screening
- CDC high blood pressure: https://www.cdc.gov/high-blood-pressure/
- NHLBI high blood pressure: https://www.nhlbi.nih.gov/health/high-blood-pressure

## 下一步

- 建立 Hypertension Control Card：screening, confirmation, measurement quality, access, adherence, follow-up, end-organ prevention。
- 与 `cardiovascular-resilience/`、`hypertensive-crisis-end-organ-risk-continuity/` 和 `chronic-kidney-disease-screening-progression-continuity/` 建立接口。
