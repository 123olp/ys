# menstrual-product-access-safety-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/menstrual-product-access-safety-continuity` |
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


本目录承载月经用品可得性、卫生设施、隐私尊严、材料安全和参与连续性研究域，关注周期性耗材如何支撑学习、工作和公共空间进入。

## 目录结构

```text
menstrual-product-access-safety-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义月经用品、设施、费用和隐私如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 OWH、CDC、FDA、学校健康、WASH、公厕和公共福利资料。
- 不写产品推荐、个体使用参数、异常出血判断、感染诊断、妇科治疗或避孕建议。
- 涉及未成年人、学校、工作和羁押场景时必须保留隐私、反污名和非监控边界。
- 新增指标必须注明口径：用品可得性、费用摩擦、设施可达、隐私条件、缺勤影响或安全标签。
