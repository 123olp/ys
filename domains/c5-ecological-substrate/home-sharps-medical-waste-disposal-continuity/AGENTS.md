# home-sharps-medical-waste-disposal-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-sharps-medical-waste-disposal-continuity` |
| 所属层级 | `C5` - 可能性生态承载层 |
| 父级容器 | `domains/c5-ecological-substrate` |
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


本目录承载家庭锐器与居家医疗废物处置连续性研究域，关注治疗工具残余物如何避免转化为针刺、感染和收运风险。

## 目录结构

```text
home-sharps-medical-waste-disposal-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义居家锐器、锐器容器、处置路径、暴露风险和治疗连续性的关系。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 FDA、CDC、地方卫生部门、药房/医疗机构回收资料和职业安全资料。
- 不写注射教程、针具复用、容器改造、锐器压缩、医疗废物运输、感染暴露处理或个案医疗建议。
- 新增指标必须注明口径：锐器类型、容器状态、处置路径、暴露风险、治疗依赖或照护场景。
- 涉及针刺伤、感染、儿童接触、职业暴露或宠物医疗锐器时，必须保留医疗/职业安全转介边界。
