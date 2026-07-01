# Refractive Error Glasses Contact Lens Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/refractive-error-glasses-contact-lens-continuity` |
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


`refractive-error-glasses-contact-lens-continuity/` 负责整理屈光不正、眼镜、隐形眼镜、验光服务、矫正可及性和低成本视觉输入恢复。

核心问题：

> 屈光不正不是高科技问题，却是最基础的视觉输入带宽问题；一副可获得、可佩戴、可更新的矫正工具，可能直接决定学习、工作和日常行动质量。

## 先验位置

```text
主体持续性最大化
  -> 主体必须清楚读取文字、屏幕、空间线索和危险信号
  -> 屈光不正会以低成本但高频方式压缩视觉输入质量
  -> 眼镜、隐形眼镜、验光和更新服务可及性决定矫正是否持续有效
  -> 因此屈光矫正连续性是视觉输入基础设施中的低摩擦恢复层
```

## 关注对象

- 近视、远视、散光、老花等屈光不正。
- 验光、眼镜、隐形眼镜、处方更新、费用、丢失损坏、学校/工作场景可及性。
- 学习、驾驶、屏幕使用、职业安全、儿童发展和老年独立生活。
- 与 `vision-eye-health-continuity/` 的关系：本域聚焦可矫正视觉输入，而不是所有眼病。

## Human Infra 模型链路

```text
验光 / 眼镜 / 隐形眼镜可及性 T
  -> 改变视觉清晰度、阅读速度、屏幕舒适、工具可用性和更新摩擦变量 X
  -> 改变主体学习、工作、移动、驾驶和日常自理状态 S
  -> 改变任务错误、事故、学习损失、工作效率下降和有效时间损耗风险
  -> 增加行动质量、学习入口和未来选择权
```

## 非目标

- 不提供验光处方、眼镜度数、隐形眼镜选择、儿童近视控制方案或个体眼健康判断。
- 不推荐具体品牌、商家、镜片、隐形眼镜、眼药水或购买渠道。
- 不把在线验光、AI 测视力或消费设备写成完整眼科评估替代品。

## Source Signals

- National Eye Institute Refractive Errors: https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/refractive-errors
- CDC Vision Health: https://www.cdc.gov/vision-health/
- WHO Blindness and visual impairment: https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment

## 下一步

- 建立屈光矫正 Source Card，区分儿童、工作、老年和低收入场景。
- 对接教育参与、工作安全、交通移动和辅助技术可及性域。
