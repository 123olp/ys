# missing-persons-unidentified-remains-resolution-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/missing-persons-unidentified-remains-resolution-continuity` |
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


本目录维护失踪人员、无名遗体与身份恢复连续性域。它关注失踪、无名、无人认领、身份确认和家属通知如何影响主体身份、家庭记录和死亡后连续性。

```text
missing-persons-unidentified-remains-resolution-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义 missing persons、unidentified remains、unclaimed persons、NamUs、法医数据、家属通知和禁止用途。
- `AGENTS.md`：说明本目录职责和隐私边界。

## 维护规则

- 新增资料必须优先来自 NamUs、DOJ/NIJ、FBI、医学检查/法医公开资料或 NCMEC 儿童系统资料。
- 必须区分公共系统说明、个案搜索、线索扩散、身份确认、家属通知和法律建议。
- 不保存可识别失踪者、家属、儿童、证人、嫌疑人、地址、实时位置、DNA/医疗/法医资料或案件编号。
- 不输出私自调查、定位、人肉搜索、公开指认、未经核实线索扩散、骚扰或干扰执法/法医工作内容。
