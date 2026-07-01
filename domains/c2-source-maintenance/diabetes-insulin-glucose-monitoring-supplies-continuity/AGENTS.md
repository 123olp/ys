# diabetes-insulin-glucose-monitoring-supplies-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/diabetes-insulin-glucose-monitoring-supplies-continuity` |
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


## 职责

本目录承载胰岛素、糖尿病耗材、CGM、血糖监测设备、泵 supplies、冷藏、支付和供应连续性资料。

## 边界

- 只整理公开制度、供应、支付、设备和风险变量。
- 不提供血糖管理、胰岛素剂量、饮食、运动、泵/CGM 设置或急救建议。
- 不保存血糖、CGM、剂量、处方、保险、设备序列号或诊断资料。

## 结构

```text
diabetes-insulin-glucose-monitoring-supplies-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分药品、DME、耗材、监测设备、支付和冷藏/灾害连续性。
- 个案糖尿病管理必须转回医生、糖尿病教育者、药师、供应商、保险方或急救渠道。
