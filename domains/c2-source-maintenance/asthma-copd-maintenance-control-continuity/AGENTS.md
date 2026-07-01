# asthma-copd-maintenance-control-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/asthma-copd-maintenance-control-continuity` |
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

<!-- domain-agent-workflow:start -->
## 代理执行流程

1. 先读本目录 `README.md`，确认研究对象、分级理由、Human Infra 追问和使用边界。
2. 再读父级层目录的 `README.md` 与 `AGENTS.md`，确认 `C2` 层的根本性标尺和同层相邻域。
3. 需要移动、拆分、合并或重命名本域时，先更新 `domains/_possibility-space-control/classification.tsv`，再运行 `python3 tools/update_domain_doc_contracts.py`。
4. 新增资料时先落到 Source Signals 或 Source Cards；只有完成证据边界复核后，才沉淀为稳定叙述。
5. 输出结论时必须同时写清：它影响什么变量、通过什么机制、证据等级是什么、不能推出什么。

## 补齐优先级

- P1 Source trail：补来源、日期、版本、作者、原始链接和本地路径。
- P2 Variable map：补输入变量、中间机制、状态变量、风险变量和输出指标。
- P3 Claim-Evidence Matrix：补主张、证据、适用范围、不确定性、反例和禁用外推。
- P4 Relation links：补上游依赖、下游输出、同层相邻域和可能的迁移路径。
- P5 Reader path：补新手入口、术语、最小阅读顺序和下一步研究任务。

## 验证要求

- 批量更新域文档后，必须运行 `python3 tools/update_domain_doc_contracts.py` 并确认第二次运行更新数为 0。
- 结构或链接变化后，必须运行 `make check`。
- 提交前必须运行 `git diff --check`，避免 Markdown 空白和格式错误。
- 不得把 `web/`、临时下载、个人资料或未核验论文缓存混入域文档提交。
<!-- domain-agent-workflow:end -->

本目录维护哮喘、COPD、长期气道控制、吸入药可及、触发因素、肺康复和急性加重预防资料。它关注慢性气道疾病如何持续压缩行动能力。

## 目录结构

```text
asthma-copd-maintenance-control-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义哮喘/COPD 长期控制如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案肺功能、用药、氧饱和度、急诊、吸烟、职业暴露或设备资料。
- 资料进入本域时必须保留疾病类型、控制状态、药物可及、触发因素、急性加重边界和禁止用途。

## 上下游关系

- 上游来自 NHLBI、CDC、呼吸医学、环境健康和康复资料。
- 下游服务 `respiratory-oxygenation/`、`asthma-copd-exacerbation-airway-continuity/` 和空气质量暴露模型。
- 不替代呼吸科、急诊、药学、氧疗、康复、职业医学、保险或个体医疗建议。

## 维护规则

- 不写个人诊断、肺功能判读、吸入药、剂量、氧疗、急性发作处理、康复动作或设备建议。
- 不把长期控制证据写成个人行动计划或药物调整流程。
- 新增资料必须区分哮喘、COPD、控制状态、触发暴露、急性加重和活动结果。
