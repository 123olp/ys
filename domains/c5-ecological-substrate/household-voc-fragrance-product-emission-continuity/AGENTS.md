# household-voc-fragrance-product-emission-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/household-voc-fragrance-product-emission-continuity` |
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


本目录承载家庭 VOC、香氛与产品释放源控制连续性研究域，关注室内产品/材料释放如何消耗注意力、呼吸舒适和居住恢复。

## 目录结构

```text
household-voc-fragrance-product-emission-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义 VOC、香氛、清洁产品、材料释放、气味敏感和家庭任务连续性的关系。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 EPA、CDC/NIOSH、毒物控制、住房和公共卫生资料。
- 不写化学品混合、装修施工、检测判读、产品推荐、气味纠纷、职业合规、医学诊断或法律建议。
- 新增指标必须注明口径：源类型、释放/气味状态、通风状态、暴露空间、敏感人群、任务负担或恢复结果。
- 涉及化学安全、头痛刺激、哮喘/过敏、装修材料或租房冲突时，必须保留专业检测、医疗和法律边界。
