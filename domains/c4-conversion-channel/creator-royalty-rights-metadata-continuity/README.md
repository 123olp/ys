# Creator Royalty Rights Metadata Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/creator-royalty-rights-metadata-continuity` |
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


`creator-royalty-rights-metadata-continuity` 研究创作者版税、rights metadata、作品标识符、collective management、分账、平台收入记录和授权链如何影响创作收入、职业可持续、作品发现和长期资源复利。

> 核心问题：创作者的持续性不是只靠灵感；版税、标识符、元数据、分账和可追踪授权链决定作品能否持续产生资源回流。

## 关注对象

- Rights metadata、work identifiers、ISRC、ISWC、ISBN、DOI、ORCID、creator IDs、publisher/label records 和 collective management signals。
- 音乐、文字、研究、影像、课程、图表、开源项目和平台内容的收益归属记录。
- 平台收入、版税报表、分账延迟、权利孤儿化、元数据错配、署名错误和再授权断点。
- 创作职业、研究传播、知识产品、课程产品和社区项目的资源回流机制。

## Human Infra 链路

```text
作品被发布和再利用
  -> 标识符、权利元数据、分账和授权记录决定收益能否回流
  -> 创作者资源、声誉、再创作能力和职业稳定性受到影响
  -> 长期创作项目更容易维持和复利
  -> 主体创造窗口和社会知识生产能力增强
```

## 非目标

- 不提供 royalty recovery、合同解释、版税计算、平台申诉、收款设置、税务、会计、法律或个案收入建议。
- 不判断具体作品权属、分账比例、平台欠款、collecting society 资格或合同有效性。
- 不提供刷量、流媒体操控、元数据冒名、虚假署名、版权洗白或收益劫持方法。
- 不收集收入报表、合同、作品文件、平台账号、税务资料、付款信息或争议证据。

## Source Signals

- U.S. Copyright Office licensing resources: https://www.copyright.gov/licensing/
- The Mechanical Licensing Collective: https://www.themlc.com/
- ISBN International Agency: https://www.isbn-international.org/
- ORCID: https://orcid.org/
- DOI Foundation: https://www.doi.org/

## 下一步

- 建立 `work -> identifier -> rights metadata -> usage report -> royalty/revenue -> creator continuity` 变量表。
- 区分权利元数据、作品标识符、平台收入、集体管理、合同关系和税务/会计边界。
- 与 `copyright-authorship-registration-licensing-continuity`、`arts-creative-expression-participation-continuity`、`personal-knowledge-management-cognitive-offloading` 和 `platform-account-suspension-appeals-continuity` 建立边界。
