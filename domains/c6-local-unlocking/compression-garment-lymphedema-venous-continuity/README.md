# Compression Garment Lymphedema Venous Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/compression-garment-lymphedema-venous-continuity` |
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


`compression-garment-lymphedema-venous-continuity` 研究淋巴水肿、静脉回流问题、压迫衣物/绷带、尺寸测量、替换、覆盖、穿脱能力和皮肤监测如何影响肢体功能、疼痛、感染风险、工作和自理连续性。

> 核心问题：压迫用品不是普通衣物；它把体液回流、皮肤屏障、肢体体积、穿脱能力、费用覆盖和日常坚持连成一个长期维护系统。

## 关注对象

- 压迫袖套、袜、手套、绷带、夜间用品、测量适配、替换周期、洗护、穿脱辅助和备用件。
- 淋巴水肿、癌症治疗后水肿、慢性静脉问题、皮肤破损、蜂窝织炎风险和疼痛/沉重感。
- 工作穿着、热环境、残障手功能、肥胖、照护者协助、费用覆盖和供应延迟。
- 与淋巴清除、慢性伤口、蜂窝织炎、DME、皮肤耗材、职业设计和热稳态的接口。

## Human Infra 链路

```text
压迫用品连续
  -> 主体能在体液回流受限时维持肢体体积、皮肤边界和可用功能
  -> 测量、适配、替换、穿脱、费用和洗护断点造成的肿胀/感染/疼痛风险下降
  -> 工作、自理、移动、睡眠和照护安排更稳定
  -> 有效时间、肢体功能和未来选择权增强
```

## 非目标

- 不提供淋巴水肿诊断、压迫等级、尺寸测量、绷带技术、治疗方案、产品推荐或覆盖个案建议。
- 不替代肿瘤团队、淋巴水肿治疗师、血管/伤口团队、Medicare、DME 供应商或临床指南。
- 不把压迫用品写成所有肿胀、疼痛、感染或血栓风险的自我处理方案。

## Source Signals

- NCI Lymphedema: https://www.cancer.gov/about-cancer/treatment/side-effects/lymphedema
- Medicare Lymphedema Compression Treatment Items: https://www.medicare.gov/coverage/lymphedema-compression-treatment-items
- MedlinePlus Lymphedema: https://medlineplus.gov/lymphedema.html

## 下一步

- 建立 `swelling/venous/lymphedema state -> compression item -> fit/replacement -> function/infection impact` 变量表。
- 区分癌症治疗后、慢性静脉、工作热暴露、手功能受限、照护依赖和低收入覆盖场景。
- 与 `lymphatic-glymphatic-clearance`、`wound-infection-cellulitis-sepsis-continuity` 和 `durable-medical-equipment-supplier-repair-continuity` 建立边界。
