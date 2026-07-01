# private-well-water-testing-treatment-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/private-well-water-testing-treatment-continuity` |
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


本目录承载私人井水检测、处理和维护连续性研究域，关注家庭自有水源如何持续支撑饮水、烹饪、清洁和照护任务。

## 目录结构

```text
private-well-water-testing-treatment-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义私人井水检测、处理、维护和家庭水任务断点如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 EPA、CDC、州/地方卫生部门、认证实验室和公共卫生材料。
- 不写水质结果判断、井施工、消毒步骤、药剂配比、设备推荐、检测频率个案或房屋交易建议。
- 新增指标必须注明口径：检测可得性、污染物类别、处理维护状态、替代水源、记录连续性或家庭任务后果。
- 涉及婴幼儿、免疫脆弱、灾后和租赁住房时，必须保留医疗、卫生、法律和住房边界。
