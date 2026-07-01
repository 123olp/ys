# open-source-software-license-compliance-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/open-source-software-license-compliance-continuity` |
| 所属层级 | `C4` - 可能性转换通道层 |
| 父级容器 | `domains/c4-conversion-channel` |
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
open-source-software-license-compliance-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义开源软件许可证、SPDX 标识、notice 和分发边界如何影响工具链与协作连续性。
- `AGENTS.md`：记录本域维护规则，避免输出法律合规意见或许可证规避策略。

## 维护规则

- 资料优先回到 SPDX、OSI、OpenSSF、GitHub 文档和项目公开许可证文件。
- 新增材料必须区分许可证标识、notice、依赖来源、分发边界、SBOM 和安全来源证明。
- 不保存私有代码、私有 SBOM、商业合同、许可证争议证据或法律通信。
- 不提供许可证选择、合规审计、兼容性判断、copyleft 规避、notice 删除、闭源规避或法律意见。

## 上下游

- 上游：`software-supply-chain-dependency-provenance-continuity/`、`open-source-maintainer-sustainability-continuity/`。
- 下游：`cloud-service-exit-interoperability-continuity/`、`safety-critical-software-formal-methods/`、`long-term-digital-preservation-format-migration/`。
