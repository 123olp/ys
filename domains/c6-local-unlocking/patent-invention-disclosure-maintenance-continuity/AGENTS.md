# patent-invention-disclosure-maintenance-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/patent-invention-disclosure-maintenance-continuity` |
| 所属层级 | `C6` - 局部可能性解锁层 |
| 父级容器 | `domains/c6-local-unlocking` |
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
patent-invention-disclosure-maintenance-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义专利、发明披露、公开记录、转让、维护和技术扩散如何影响未来技术可及性。
- `AGENTS.md`：记录本域维护边界，避免输出专利法律、商业或诉讼策略。

## 维护规则

- 资料优先回到 USPTO、WIPO、NIST、公共专利数据库和技术转移机构公开资料。
- 新增材料必须区分发明披露、专利公开、授权状态、转让/许可、维护记录和可及性影响。
- 不保存未公开发明、实验记录、商业秘密、许可合同、资助合同或法律通信。
- 不提供专利申请、权利要求、prior art/FTO 法律意见、侵权判断、维护费策略、许可谈判或专利规避方法。

## 上下游

- 上游：`intellectual-property-technology-transfer-access/`、`research-portfolio-prioritization-funding-governance/`。
- 下游：`technology-foresight-horizon-scanning/`、`clinical-trials-regulatory-science-translation/`、`medicine-access-treatment-continuity/`。
