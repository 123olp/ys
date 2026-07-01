# natural-gas-propane-leak-shutoff-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/natural-gas-propane-leak-shutoff-continuity` |
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


本目录承载天然气、丙烷泄漏识别与关断恢复连续性研究域，关注高能量燃料接口如何支撑供暖和烹饪并避免泄漏、爆炸、火灾和中毒风险。

## 目录结构

```text
natural-gas-propane-leak-shutoff-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义燃气/丙烷接口、泄漏信号、撤离、专业恢复和家庭任务连续性如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 PHMSA、USFA/FEMA、CDC、燃气公司公共安全资料、消防部门和地方建筑/燃气规范。
- 不写关阀操作、泄漏判断、维修步骤、恢复通气、管线施工、设备调试或现场许可。
- 新增指标必须注明口径：燃料类型、泄漏信号、撤离入口、专业恢复、供暖/烹饪依赖或灾后返家后果。
- 涉及泄漏、火灾、爆炸、CO 或灾后返家时，必须保留 911、消防和燃气专业人员边界。
