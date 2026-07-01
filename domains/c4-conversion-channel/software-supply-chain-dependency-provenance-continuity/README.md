# Software Supply Chain Dependency Provenance Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/software-supply-chain-dependency-provenance-continuity` |
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


`software-supply-chain-dependency-provenance-continuity` 研究软件依赖、包管理器、构建系统、SBOM、签名、来源证明、构件仓库和供应链完整性如何影响主体依赖的服务、工具和医疗/金融/教育系统能否持续可信运行。

> 核心问题：主体行动越来越依赖软件；软件供应链污染会把工具、平台、数据和服务同时变成不可信基础设施。

## 关注对象

- 开源/商业依赖、包管理器、构建流水线、容器镜像、制品仓库、SBOM、签名、来源证明和依赖更新策略。
- 供应链攻击、依赖混淆、恶意包、构建环境污染、制品替换、许可证风险和不可复现构建。
- 医疗、金融、教育、工作、政府和个人工具软件中的第三方依赖风险。
- 依赖可追溯性、制品完整性、可复现性、审计证据和恢复能力。

## Human Infra 链路

```text
软件供应链来源可追溯
  -> 工具和服务的依赖、构建和制品可信度可审查
  -> 恶意依赖、构建污染和不可追溯更新造成的系统失效下降
  -> 主体依赖的软件环境更稳定、更可恢复、更可验证
  -> 数字任务执行和关键服务连续性增强
```

## 非目标

- 不提供供应链攻击、恶意包投递、依赖混淆、构建系统入侵、签名绕过或漏洞利用步骤。
- 不替代安全审计、软件采购、法律、合规、应急响应或组织 DevSecOps 流程。
- 不收集私有仓库、token、构建日志、私有 SBOM、许可证争议或未公开漏洞细节。

## Source Signals

- NIST Secure Software Development Framework SP 800-218: https://csrc.nist.gov/
- CISA SBOM and Secure by Design resources: https://www.cisa.gov/
- SLSA supply-chain levels: https://slsa.dev/
- OpenSSF Scorecard and Sigstore resources: https://openssf.org/

## 下一步

- 建立 `dependency -> build -> artifact -> provenance -> service continuity` 变量表。
- 区分依赖治理、构建可复现、SBOM 可审计、签名信任和运行时恢复。
- 与 `cybersecurity-resilience-critical-services`、`safety-critical-software-formal-methods`、`model-cards-ai-audit-documentation` 和 `api-platform-dependency-runtime-continuity` 建立边界。
