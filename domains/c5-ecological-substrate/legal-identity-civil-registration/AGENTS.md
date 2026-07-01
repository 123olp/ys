# legal-identity-civil-registration 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/legal-identity-civil-registration` |
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


`legal-identity-civil-registration/` 是 Human Infra 的法律身份与民事登记域，负责研究主体如何被制度承认为权利和服务对象。

## 目录结构

```text
legal-identity-civil-registration/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义法律身份与民事登记域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做法律身份、出生登记、民事登记、生命统计、身份覆盖和服务入口的资料整理。
- 个体法律、移民、身份申请、证件办理、资格判断、欺诈或规避方法不属于本域。

## 上下游关系

- 上游：`governance-rights/`、`resource-social-infra/` 和 `digital-identity-security/`。
- 下游：`healthcare-access-continuity/`、`financial-resilience-access/`、`emergency-preparedness-response/` 和公共服务接入。

## 维护规则

- 新增资料必须区分法律身份、民事登记、生命统计、数字身份和服务资格。
- 禁止输出证件办理、法律规避、身份欺诈或个体资格建议。
