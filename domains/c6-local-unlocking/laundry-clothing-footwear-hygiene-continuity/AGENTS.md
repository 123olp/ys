# laundry-clothing-footwear-hygiene-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/laundry-clothing-footwear-hygiene-continuity` |
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


本目录承载洗衣、衣物、鞋履、个人卫生和穿着防护连续性研究域，关注低层物品系统如何支撑外出、工作、学习、照护和尊严。

## 目录结构

```text
laundry-clothing-footwear-hygiene-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义洗衣、衣物、鞋履、个人卫生和天气防护如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 CDC、Ready.gov、NIOSH、WASH、住房和公共服务可及性资料。
- 不写购买推荐、穿搭建议、PPE 配置、感染清洗处置、医疗判断或个人卫生评价。
- 涉及衣物和卫生时保持反污名边界，关注可及、维护、尊严、参与和风险。
- 新增指标必须注明口径：换洗可得性、洗衣设施可及、天气防护、穿着要求摩擦、卫生用品可得性或参与影响。
