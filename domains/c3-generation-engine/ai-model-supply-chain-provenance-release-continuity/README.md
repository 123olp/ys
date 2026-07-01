# AI Model Supply Chain Provenance Release Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-model-supply-chain-provenance-release-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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


`ai-model-supply-chain-provenance-release-continuity/` 研究 AI 模型来源、权重、依赖、数据/代码谱系、签名、发布说明、版本变更、许可证和撤回机制，如何影响 AI 工具作为 Human Infra 的长期可信性。

> 核心问题：AI 模型不是孤立文件，而是数据、代码、依赖、训练流程、权重、许可证和发布治理的供应链产物。供应链不可信，模型能力就不可托付。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要长期复用 AI 模型和工具链作为认知与行动放大器
  -> AI 模型依赖训练数据、代码、权重、依赖包、推理服务和发布流程
  -> 来源不明、依赖污染、版本漂移和许可证不清会破坏长期可用性
  -> 因此 AI 模型供应链、来源证明与发布治理是 AI 工具可信消费域
```

## 关注对象

- 模型来源、权重哈希、签名、依赖、训练/微调流程、数据引用、license、model card、release notes 和 deprecation。
- 模型 registry、artifact provenance、SBOM/ML-BOM、SLSA、Sigstore、可复现构建和撤回通知。
- 发布前审查、版本差异、能力变更、安全变更、已知限制和回滚路径。
- 与 `software-supply-chain-dependency-provenance/` 的关系：软件供应链域关注通用软件依赖；本域关注模型 artifact 与 AI 发布链路。
- 与 `model-cards-ai-audit-documentation/` 的边界：模型卡域关注说明文档；本域关注可验证来源、发布和供应链完整性。

## Human Infra 模型链路

```text
AI 模型供应链来源与发布治理 T
  -> 改变来源证明、版本、依赖、许可证、发布说明和撤回信号变量 X
  -> 改变模型可追溯、可回滚、可替换和可信消费状态 S
  -> 改变供应链污染、不可复现、错误升级、合规不确定和长期不可用风险 λ(t)
  -> 影响主体 AI 工具稳定性、知识资产延续和协作基础设施可信度
```

## 非目标

- 不提供模型盗取、权重绕权、许可证规避、私有模型抓取、供应链投毒或签名伪造方法。
- 不保存未授权模型权重、私有构建日志、密钥、token 或受限 artifact。
- 不把“开源”“公开下载”写成可无限制使用。

## Source Signals

- OpenSSF SLSA: https://slsa.dev/
- Sigstore: https://www.sigstore.dev/
- CISA Secure by Design: https://www.cisa.gov/securebydesign
- NIST Secure Software Development Framework: https://csrc.nist.gov/Projects/ssdf
- Model Cards for Model Reporting: https://arxiv.org/abs/1810.03993

## 下一步

- 建立 Model Release Source Card 字段：artifact id, version, hash, license, provenance, dependency boundary, release note, deprecation status。
- 与 `software-supply-chain-dependency-provenance/`、`model-cards-ai-audit-documentation/` 和 `ai-data-provenance-contamination-drift-continuity/` 建立供应链索引。
