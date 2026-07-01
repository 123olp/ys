# ai-training-data-rights-opt-out-provenance-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-training-data-rights-opt-out-provenance-continuity` |
| 所属层级 | `C3` - 可能性生成引擎层 |
| 父级容器 | `domains/c3-generation-engine` |
| 路径真相源 | `domains/_possibility-space-control/classification.tsv` |
| 复核状态 | `heuristic-v0.1` |

### 文件职责

- `README.md` 面向读者，说明研究对象、Human Infra 价值链路、证据边界、非目标和下一步资料入口。
- `AGENTS.md` 面向维护者和代理，说明目录结构、上下游依赖、禁止事项、更新规则和验证要求。

### 更新规则

- 修改本域对象、边界或上下游关系时，必须同步检查 README、AGENTS 和分类表中的 `physical_path`。
- 新增资料优先沉淀为 Source Signals、Source Cards、Claim-Evidence Matrix 或明确的证据段落，不把未经核验的摘要写成稳定结论。
- 若发现当前层级不符合“可能性空间控制力”标尺，先修改 `_possibility-space-control/rubric.md` 或 `classification.tsv`，再移动目录。

### 禁止事项

- 不把研究域写成个体行动处方、临床建议、法律建议、投资建议、工程操作手册或规避规则指南。
- 不在本目录保存无来源、无边界、无证据等级的断言。
- 不绕过父级 C1-C6 物理目录直接在 `domains/` 根目录新增正式研究域。
<!-- domain-agent-contract:end -->


## 目录结构

```text
ai-training-data-rights-opt-out-provenance-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义 AI 训练数据权利、来源、许可、opt-out 和 provenance 如何影响创作者、研究者、用户和知识生态连续性。
- `AGENTS.md`：记录本域维护规则，避免输出抓取、规避、模型训练或法律策略。

## 维护规则

- 资料优先回到 Copyright Office、WIPO、Creative Commons、C2PA、模型卡/数据卡和平台公开 AI 数据政策。
- 新增材料必须区分版权制度、平台条款、开放许可、技术排除信号、内容凭据、数据集文档和模型使用披露。
- 不保存未公开数据集、训练数据、作品文件、合同、平台账号、争议证据或法律通信。
- 不提供数据抓取、robots/paywall 绕过、训练数据规避、版权清洗、模型训练操作、授权谈判、takedown、法律或个案策略建议。

## 上下游

- 上游：`copyright-authorship-registration-licensing-continuity/`、`creative-commons-open-content-license-continuity/`、`content-provenance-authenticity-credential-continuity/`。
- 下游：`model-cards-ai-audit-documentation/`、`information-integrity-trust/`、`platform-content-moderation-notice-appeal-continuity/`。
