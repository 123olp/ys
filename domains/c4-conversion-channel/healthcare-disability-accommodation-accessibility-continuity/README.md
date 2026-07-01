# Healthcare Disability Accommodation Accessibility Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/healthcare-disability-accommodation-accessibility-continuity` |
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


## 定位

本域研究残障主体在医疗系统中的 physical access、auxiliary aids、reasonable modification、accessible medical equipment 和 care accessibility 如何影响服务能否实际发生。

它不是 ADA/Section 504 法律意见、机构投诉、设备处方、便利申请代写或医疗建议工具。

## 先验问题

```text
医疗服务何以对残障主体真实可达？
  -> 医疗空间、设备、沟通和流程必须能被不同能力状态的人使用
  -> 辅助沟通、合理修改和无障碍设备必须可请求、可提供、可记录
  -> 转运、检查、治疗、账单和随访必须不因残障被截断
  -> 否则名义医疗服务会变成实际排除
```

## 研究对象

- Healthcare accessibility、reasonable modification、auxiliary aids、accessible medical diagnostic equipment。
- Physical access、exam tables/scales、communication access、appointment accommodation、service animals。
- Section 504、ADA、Section 1557、HHS OCR 和 disability-inclusive care。

## 关键变量

- 可进入性、可转移性、可检查性、辅助沟通可用性和 accommodation 响应时间。
- 设备、空间、培训、照护者参与、隐私尊严和取消/延误率。
- 投诉路径、机构责任、无障碍计划、质量差异和安全事件。

## 证据入口

- ADA.gov healthcare / effective communication / service animals 资料。
- HHS OCR disability rights、Section 504、Section 1557 和 CMS accessibility 语境。
- Accessible medical diagnostic equipment、disability healthcare access 和 health equity 文献。

## 非目标

- 不提供 ADA、Section 504、Section 1557、无障碍投诉、诉讼、权益或法律建议。
- 不代写 accommodation request、complaint、appeal、medical letter 或机构沟通。
- 不推荐设备、机构、医生、交通、检查方式、治疗或安全转移方法。

## 上下游

- 上游：`disability-services-independent-living/`、`public-accommodation-accessibility-service-continuity/`。
- 下游：`appointment-availability-wait-time-continuity/`、`informed-consent-refusal-shared-decision-continuity/`。
