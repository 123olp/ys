# digital-legacy-data-succession 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/digital-legacy-data-succession` |
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


本目录维护数字遗产、数据继承与账号连续性域。它是 Human Infra 的“失能和死亡边界下资料与权限不断线”层，负责数字资产、账号、授权和数据交接如何影响主体意愿与长期项目连续性。

## 目录结构

```text
digital-legacy-data-succession/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明数字遗产、数据继承、账号恢复、受托访问和身份生命周期如何进入主体持续性模型。
- 本域只做公开资料整理和证据边界维护。
- 不提供法律、税务、遗嘱、继承、账号访问、密钥恢复、平台规避或争议处理建议。

## 维护规则

- 新增资料必须区分法律授权、平台规则、技术访问、密钥控制和主体意愿表达。
- 涉及死亡、失能、家庭争议和数字人格时，必须保留隐私、同意、撤回、证明和滥用风险边界。
- 不把数字资产交接写成人格延续，不把平台工具写成法律或伦理充分授权。
