# Background Check Record Screening Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/background-check-record-screening-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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


Background Check Record Screening Continuity 关注背景调查、犯罪记录、身份核验、教育/执照记录、制裁名单和记录准确性如何影响主体进入工作、志愿、住房、照护、教育和公共服务。

## 对象

- Background checks、criminal records、identity matching、education/license verification、registry checks 和 adverse action。
- 错误匹配、旧记录、缺失上下文、跨州记录、身份盗用、封存/清除记录和更正。
- 就业、租房、照护岗位、志愿服务、教育项目、金融服务和敏感岗位准入。

## Human Infra 价值

```text
主体持续性需要记录筛查不把过去或错误身份变成永久排除
-> 背景检查把分散记录合并成当前准入判断
-> 错误匹配、过期记录或缺失上下文会切断工作、住房、照护和服务入口
-> 准确性、通知、解释、争议和更正机制降低错误排除和永久惩罚
-> 主体更可能在风险治理和未来机会之间保留可修复路径
```

## 边界

- 本域不提供背景调查规避、记录清除、法律、就业、租房、执照、教育、移民或个案申诉建议。
- 不判断某记录是否应报告、某机构是否合规或某人是否适合某岗位。
- 不替代 FTC、EEOC、法院、执法机构、雇主、学校、许可机构、律师或监管机构。
- 只整理公开资料、记录类型、准确性风险、授权边界、争议流程和禁止用途。

## 上游与下游

- 上游：`legal-identity-civil-registration/`、`access-to-justice-legal-aid/`、`correctional-health-reentry-continuity/`、`credit-consumer-reporting-access-continuity/`。
- 下游：`employment-algorithmic-hiring-screening-continuity/`、`tenant-screening-rental-access-continuity/`、`disability-services-independent-living/`。

## 初始资料线索

- FTC background check and consumer report guidance.
- EEOC arrest and conviction records / employment guidance.
- State court public education on records, sealing and expungement boundaries.
