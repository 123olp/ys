# social-protection-benefits-delivery 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/social-protection-benefits-delivery` |
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


`social-protection-benefits-delivery/` 是 Human Infra 的社会保护与福利递送域，负责研究公共福利和社会保护系统如何在风险冲击中接住主体。

## 目录结构

```text
social-protection-benefits-delivery/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义社会保护与福利递送域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做社会保护、福利服务、资格流程、行政负担、支付连续性和申诉路径资料整理。
- 个体福利申请、资格判断、材料准备、税务、法律、移民和规避制度不属于本域。

## 上下游关系

- 上游：`legal-identity-civil-registration/`、`health-literacy-navigation/`、`digital-identity-security/`。
- 下游：`food-security-nutrition-access/`、`housing-built-environment-stability/`、`energy-access-resilience/` 和 `financial-resilience-access/`。

## 维护规则

- 新增资料必须说明它影响资格、申请、续期、支付、申诉、等待、人工帮助还是行政负担。
- 禁止输出个体申请、规避制度、虚假材料或资格判断建议。
