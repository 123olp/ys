# digital-inclusion-connectivity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/digital-inclusion-connectivity` |
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


`digital-inclusion-connectivity/` 是 Human Infra 的数字包容与连接域，负责研究连接、设备、技能和可访问服务如何成为主体进入现代资源系统的基础接入层。

## 目录结构

```text
digital-inclusion-connectivity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义数字包容与连接域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做互联网接入、设备可及、可负担性、数字技能、无障碍、人工帮助和数字公共服务资料整理。
- 黑客攻击、账号绕过、盗版破解、电信账户操控、个体补贴申请和设备购买建议不属于本域。

## 上下游关系

- 上游：`resource-social-infra/`、`energy-access-resilience/`、`assistive-technology-access/`。
- 下游：`digital-identity-security/`、`social-protection-benefits-delivery/`、`health-literacy-navigation/`、`civic-participation-election-access/`。

## 维护规则

- 新增资料必须说明它影响覆盖、速度、设备、费用、技能、无障碍、语言、人工帮助还是数字服务成功率。
- 禁止输出攻击、绕过、盗版、账户操控、平台规避或个体补贴/设备选择建议。
