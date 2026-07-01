# catheter-associated-uti-device-infection-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/catheter-associated-uti-device-infection-continuity` |
| 所属层级 | `C2` - 可能性源体维护层 |
| 父级容器 | `domains/c2-source-maintenance` |
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


`domains/c2-source-maintenance/catheter-associated-uti-device-infection-continuity/` 保存导尿设备、CAUTI 和设备相关感染连续性研究资料。

## 职责

- 维护导尿设备、留置时间、感染控制、长期照护和行动/隐私负担的证据边界。
- 将设备化排尿出口的感染、照护、尊严和抗菌药压力纳入 Human Infra 模型。
- 记录公开来源、机构流程边界和禁止用途。

## 非目标

- 不提供导尿、拔管、消毒、冲洗、护理操作、设备购买、感染处理或个体医疗建议。
- 不输出机构责任判断、护理质量评分或法律结论。

## 上游

- `urogenital-continuity/`
- `urinary-retention-bladder-emptying-continuity/`
- `sterilization-disinfection-infection-control/`

## 下游

- `urinary-tract-infection-pyelonephritis-urosepsis-continuity/`
- `health-workforce-capacity/`
- `caregiving-long-term-care/`
