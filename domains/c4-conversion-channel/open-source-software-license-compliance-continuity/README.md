# Open Source Software License Compliance Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/open-source-software-license-compliance-continuity` |
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


`open-source-software-license-compliance-continuity` 研究开源软件许可证、SPDX 标识、OSI 批准许可证、license notices、copyright notices、copyleft、permissive license 和依赖授权记录如何影响软件工具、产品、研究代码和组织协作连续性。

> 核心问题：代码不是只有能运行才有价值；如果许可证、通知和依赖授权不可追溯，工具会在分发、商业化、复现和长期维护时突然变成不可用资产。

## 关注对象

- SPDX License List、OSI-approved licenses、permissive/copyleft licenses、license identifiers、notices 和 attribution。
- 开源依赖、研究代码、模型代码、数据处理脚本、软件供应链和 SBOM 中的许可证记录。
- 许可证兼容性、分发边界、源码提供义务、notice 保留、商业使用风险和组织治理。
- Human Infra 工具链、知识库、Web 展示、模型代码和自动化脚本的长期可复用性。

## Human Infra 链路

```text
软件依赖和代码资产进入主体工具链
  -> 许可证、notice 和授权记录必须可追溯
  -> 分发、复现、商业化、协作和归档边界更清楚
  -> 软件工具持续可维护、可替换、可审计
  -> 数字行动底座和长期项目连续性增强
```

## 非目标

- 不提供开源许可证选择、兼容性法律判断、合规审计、商业发布判断、侵权分析或法律意见。
- 不提供规避 copyleft、移除 notice、闭源规避、许可证清洗、依赖隐藏或违规分发方法。
- 不收集私有代码库、私有 SBOM、许可证争议、商业合同、发布计划或法律通信。

## Source Signals

- SPDX License List: https://spdx.org/licenses/
- Open Source Initiative licenses: https://opensource.org/license
- GitHub license documentation: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
- OpenSSF resources: https://openssf.org/

## 下一步

- 建立 `dependency -> license id -> notice -> distribution boundary -> tool continuity` 变量表。
- 区分许可证元数据、供应链来源证明、维护者可持续和组织合规。
- 与 `software-supply-chain-dependency-provenance-continuity`、`open-source-maintainer-sustainability-continuity`、`long-term-digital-preservation-format-migration` 和 `model-cards-ai-audit-documentation` 建立边界。
