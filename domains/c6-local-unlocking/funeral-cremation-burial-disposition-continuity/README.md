# Funeral Cremation Burial Disposition Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/funeral-cremation-burial-disposition-continuity` |
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


Funeral Cremation Burial Disposition Continuity 研究遗体处置、葬礼、火化、土葬、价格披露、许可、运输和消费者保护如何在死亡后保护尊严、家庭决策能力和资源不被一次性击穿。

> 核心问题：死亡后遗体处置是高压力、低时间窗口、高信息不对称任务；若价格、权限、运输和选择不透明，遗属的资源、时间和判断力会被快速消耗。

## 研究对象

- Funeral services、cremation、burial、body disposition、funeral home、price list、permit 和遗体运输。
- 葬礼消费者保护、价格透明、宗教文化需求、低收入丧葬援助、灾害/大规模死亡处置。
- 遗体认领、授权处置人、火化授权、骨灰/遗体交接和处置记录。

## 先验链路

```text
死亡事实发生后遗体必须被处置
  -> 处置过程需要授权、费用、运输、选择、文化尊严和记录链
  -> 信息不透明、价格不清、授权不明或服务不可达会制造遗属决策与资源冲击
  -> 家庭恢复、福利申请、纪念安排和后续行政任务被拖延
  -> 幸存者有效时间、财务韧性和心理恢复能力下降
  -> 因而葬礼、火化、土葬和遗体处置是死亡后主体网络恢复的执行层
```

## 关键变量

- 价格透明、授权处置人、服务可达性、文化/宗教适配、费用负担和消费者保护入口。
- 遗体运输、火化/土葬许可、处置记录、死亡证明依赖和灾害容量。
- 家庭冲突、无亲属、低收入、跨州/跨境、诈骗、强制销售和情绪脆弱窗口。

## 证据入口

- FTC Funeral Rule and funeral consumer guidance。
- USA.gov death of a loved one and funeral-related materials。
- State funeral board, consumer protection and vital records materials。

## 非目标

- 本域不推荐殡仪馆、墓地、火化服务、仪式、价格、宗教方案或具体安排。
- 不提供法律、税务、保险、遗体运输、尸检、火化授权或家庭争议建议。
- 不收集死亡证明、遗体位置、付款记录、家庭关系、宗教偏好或服务合同。

## 上下游

- 上游：`death-certificate-registration-cause-of-death-record-continuity/`、`emergency-contact-next-of-kin-notification-continuity/`。
- 下游：`cemetery-memorial-remains-location-continuity/`、`bereavement-leave-grief-support-continuity/`、`estate-inventory-asset-liability-handoff-continuity/`。
