# Venous Thromboembolism Pulmonary Embolism Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/venous-thromboembolism-pulmonary-embolism-continuity` |
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


`venous-thromboembolism-pulmonary-embolism-continuity/` 研究深静脉血栓、肺栓塞、住院/术后/妊娠/癌症相关风险、诊断路径、抗凝系统和长期功能影响如何改变主体持续性。

> 核心问题：静脉血栓栓塞把血液凝固、移动、住院、手术、癌症和妊娠等条件连接成突发死亡风险。肺栓塞尤其会在短时间内改变氧合、右心负荷和死亡风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖血液在血管内保持可流动且不过度凝固
  -> 静脉血栓可脱落进入肺循环，造成氧合和右心急性失效
  -> 结果取决于风险识别、诊断路径、抗凝连续性和复发预防
  -> 因此 VTE/PE 是血液-循环-呼吸交界的急性死亡风险域
```

## 关注对象

- DVT、pulmonary embolism、hospital-acquired VTE、postoperative risk、cancer-associated thrombosis、pregnancy-associated thrombosis、anticoagulation continuity、post-PE syndrome。
- 与 `blood-oxygen-hemostasis/` 的边界：该域关注凝血/止血生理；本域关注 VTE/PE 事件链和系统连续性。
- 与 `transfusion-blood-management-hemorrhage-continuity/` 的关系：抗凝和出血风险构成双向治理边界。

## Human Infra 模型链路

```text
VTE/PE 预防识别系统 T
  -> 改变风险识别、诊断延迟、抗凝连续性、出血权衡和复发预防变量 X
  -> 改变肺循环负荷、氧合、右心功能、住院和长期运动能力 S
  -> 改变急性死亡、复发、慢性血栓栓塞和有效时间损失 λ(t)
  -> 影响主体存活、行动能力和长期选择权
```

## 非目标

- 不提供血栓诊断、D-dimer/影像解读、抗凝、溶栓、滤器、旅行、术后、妊娠或个体治疗建议。
- 不生成 VTE 风险评分、PE 分层、抗凝选择、出血权衡或停药建议。
- 不收集个案症状、影像、凝血结果、用药、肿瘤史、妊娠状态或住院资料。

## Source Signals

- ESC pulmonary embolism guideline materials: https://www.escardio.org/
- CDC blood clots / VTE materials: https://www.cdc.gov/blood-clots/
- NHLBI pulmonary embolism materials: https://www.nhlbi.nih.gov/health/pulmonary-embolism

## 下一步

- 建立 VTE/PE Continuity Card：risk context, diagnosis path, anticoagulation continuity, bleeding tradeoff, recurrence, long-term function。
- 与 `blood-oxygen-hemostasis/`、`transfusion-blood-management-hemorrhage-continuity/` 和 `pregnancy-parental-work-continuity/` 建立接口。
