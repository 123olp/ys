# lead-heavy-metal-exposure-control 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/lead-heavy-metal-exposure-control` |
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


本目录维护铅与重金属暴露控制域。它是 Human Infra 的“慢性神经毒性与环境不平等层”，负责重金属如何影响认知、儿童发展、肾血液系统、心血管风险和未来选择权。

## 目录结构

```text
lead-heavy-metal-exposure-control/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明铅、汞、镉、砷等重金属暴露如何经住房、饮水、土壤、工作和产品系统影响主体持续性。
- 本域只做公开公共卫生、环境暴露、监管资料和证据边界整理。
- 不提供检测解释、治疗建议、采样方案、除铅施工、危险废物处理、法律索赔或房产判断。

## 维护规则

- 新增材料必须区分儿童铅暴露、饮水管线、旧住房、职业暴露、土壤/粉尘、食品链和工业污染。
- 不把地图、检测数值、家庭试剂或 AI 结果写成个体医疗、房屋安全、法律责任或资产价值结论。
- 涉及危险材料和污染修复时，只写公共系统和官方边界，不写操作步骤。
