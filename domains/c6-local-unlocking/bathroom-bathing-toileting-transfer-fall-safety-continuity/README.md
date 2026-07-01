# Bathroom Bathing Toileting Transfer Fall Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/bathroom-bathing-toileting-transfer-fall-safety-continuity` |
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


`bathroom-bathing-toileting-transfer-fall-safety-continuity/` 研究浴室、洗澡、如厕、转移、湿滑表面、扶手、照明和照护辅助如何影响主体在家庭中完成高风险日常动作的连续性。

> 核心问题：浴室不是生活细节，而是跌倒、烫伤、隐私、尊严、照护负担和独立生活交汇的高风险节点。

## 先验位置

```text
主体要持续行动
  -> 必须能安全完成洗澡、如厕、站起、坐下、转身和转移
  -> 浴室通常同时存在水、硬表面、狭小空间、裸露身体和隐私约束
  -> 因而浴室安全是家庭行动连续性的高风险执行层
```

## 关注对象

- 浴缸、淋浴、马桶、洗手池、地面湿滑、浴垫、扶手、座椅、门槛、照明、照护辅助空间。
- 老年人、残障者、术后恢复者、孕产者、儿童、照护者和夜间如厕场景。

## Human Infra 模型链路

```text
浴室转移与洗浴环境 T
  -> 改变湿滑、扶手、照明、空间、照护辅助和隐私变量 X
  -> 改变洗澡、如厕、转移和夜间行动状态 S
  -> 改变跌倒、烫伤、照护依赖、活动回避和住院风险 λ(t)
  -> 改变独立生活、有效时间、尊严和未来选择权
```

## 非目标

- 不提供浴室改造方案、产品推荐、扶手安装、护理动作、跌倒风险评分、康复训练、施工、保险、法律或个体安全建议。
- 不收集个人浴室照片、户型、残障状态、跌倒史、如厕记录、护理记录或其他敏感资料。

## Source Signals

- CDC / STEADI fall prevention and home safety materials.
- NIA falls and home safety materials.
- CPSC home safety and bathtub/shower risk materials.
