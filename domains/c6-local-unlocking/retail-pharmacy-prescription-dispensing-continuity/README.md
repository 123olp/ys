# Retail Pharmacy Prescription Dispensing Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/retail-pharmacy-prescription-dispensing-continuity` |
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


## 定位

本域研究零售药房、邮寄药房、处方传递、库存、营业覆盖、药师服务、支付结算和取药/配送路径如何把临床处方转化为主体真实获得的治疗物质。

它不是处方建议、药品推荐、药房营销或个案医保申诉入口。

## 先验问题

```text
治疗何以成为主体持续性收益？
  -> 临床处方必须离开病历系统
  -> 药房必须能接收、核验、配发和交付
  -> 主体必须能支付、取到、理解并持续补充
  -> 否则“有药可治”不会转化为实际治疗连续性
```

## 研究对象

- 零售药房、邮寄药房、专科药房和长期照护药房。
- e-prescribing、处方转移、refill、库存和短缺替代路径。
- 药师咨询、取药窗口、配送、营业时间和地理可达。
- 支付、copay、保险结算、现金价格和药房网络。
- 紧急补药、灾害闭店、药房关闭和药房荒漠。

## 关键变量

- 处方到配药的时间、首次取药率和 refill gap。
- 药房距离、营业覆盖、网络内药房覆盖和配送可用性。
- 缺货率、转药房失败率、处方转移摩擦和拒付率。
- 药师可用性、咨询可达性、语言/无障碍支持。

## 证据入口

- FDA 药品短缺、药品标签和安全沟通资料。
- CMS / Medicare Part D、药房网络和处方药计划资料。
- 州 pharmacy board、NABP、公共卫生和药房可达性研究。

## 非目标

- 不提供处方、换药、剂量、停药、替代药或个体治疗建议。
- 不指导绕过处方、药房规则、保险规则、药品管制或身份核验。
- 不收集处方号、药房账号、保险卡、病历、药品照片或个人用药记录。

## 上下游

- 上游：`medicine-access-treatment-continuity/`、`healthcare-access-continuity/`、`pharmaceutical-quality-supply-integrity/`。
- 下游：`medication-reconciliation-regimen-adherence-continuity/`、`pharmacy-benefit-formulary-prior-authorization-continuity/`、`patient-medication-labeling-counseling-continuity/`。
