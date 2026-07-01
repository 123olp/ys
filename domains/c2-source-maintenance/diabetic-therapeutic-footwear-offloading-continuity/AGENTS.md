# diabetic-therapeutic-footwear-offloading-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/diabetic-therapeutic-footwear-offloading-continuity` |
| 所属层级 | `C2` - 可能性源体维护层 |
| 父级容器 | `domains/c2-source-maintenance` |
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


本目录承载糖尿病治疗鞋、鞋垫、卸载、适配、覆盖和日常穿着连续性研究域，关注足部保护如何阻断移动能力崩塌和截肢风险链条。

## 目录结构

```text
diabetic-therapeutic-footwear-offloading-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义糖尿病治疗鞋和卸载用品如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 NIDDK、CDC、CMS/Medicare、糖尿病足、DME、伤口和截肢预防资料。
- 不写足部诊断、伤口处理、鞋履处方、卸载设备操作、覆盖资格判断或产品推荐。
- 涉及感染、开放伤口、疼痛、红肿、发热或急性恶化时，只能写转诊边界，不写处理步骤。
- 新增指标必须注明口径：足风险分层、压力再分配、适配/替换、供应可达、穿着依从或移动影响。
