# Early Intervention IDEA Part C Developmental Services Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/early-intervention-idea-part-c-developmental-services-continuity` |
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


`early-intervention-idea-part-c-developmental-services-continuity/` 研究 IDEA Part C 早期干预如何把发育担忧、评估、IFSP、服务协调和转衔转化为婴幼儿发展支持连续性。

> 核心问题：儿童发育支持不能等到学校失败后才介入；早期识别、服务协调和家庭中心服务决定发展差异是否被及时接住。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 婴幼儿发展差异会影响沟通、行动、学习和家庭压力
  -> 早期发现、评估、服务协调和家庭支持必须及时接上
  -> IDEA Part C 将发育服务嵌入生命早期
  -> 儿童能力形成和家庭恢复窗口才不会被延迟耗尽
```

## 关注对象

- IDEA Part C、早期干预、发育筛查入口、评估、IFSP、service coordination 和转衔。
- 家庭中心服务、特殊需要、服务可及、等待、跨系统转介和从 Part C 到学前/学校支持的过渡。
- 与 `maternal-newborn-child-development/`、`special-education-iep-504-accommodation-continuity/`、`speech-language-execution-continuity/`、`hearing-auditory-communication-continuity/` 和 `autism-neurodiversity-support-continuity/` 的接口。

## Human Infra 模型链路

```text
婴幼儿发育担忧
  -> 早期识别、评估、IFSP、服务协调和转衔
  -> 沟通、行动、学习、家庭支持和照护能力改善
  -> 儿童发展损失和家庭压力下降
  -> 长期能力形成与未来选择权增加
```

## 非目标

- 不诊断儿童发育、残障、自闭症、语言、听力、运动或行为问题。
- 不提供治疗计划、训练动作、服务申请、IFSP 策略、学校安置、法律或保险建议。
- 不收集儿童发育记录、评估报告、IFSP、医疗记录、教育记录、视频、照片或家庭身份资料。

## Source Signals

- IDEA Topic Areas - Early Childhood: https://sites.ed.gov/idea/topic-areas/#Early-Childhood
- IDEA Statute and Regulations: https://sites.ed.gov/idea/statuteregulations/
- CDC Child Development: https://www.cdc.gov/child-development/
- Head Start: https://headstart.gov/

## 下一步

- 建立变量表：识别入口、评估、IFSP、服务协调、等待、转介、转衔和家庭支持。
- 整理 IDEA Part C、CDC Child Development 和早期儿童服务 Source Cards。
- 与 `special-education-iep-504-accommodation-continuity/` 区分：本域聚焦 0-3 岁早期干预执行链。
