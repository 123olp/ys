# trauma-ptsd-adversity-recovery-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/trauma-ptsd-adversity-recovery-continuity` |
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


本目录承载创伤、PTSD、逆境暴露和恢复连续性资料。它关注创伤如何改变主体安全感、记忆、关系和未来进入能力，而不是治疗或个案处置。

## 结构

```text
trauma-ptsd-adversity-recovery-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须使用创伤知情语言，避免诱导披露、猎奇叙事、责任归因和可识别个案细节。
- 必须区分公共资料、服务系统、功能结局、隐私边界、儿童/弱势群体保护和再创伤风险。
- 不保存创伤细节、报案材料、法律材料、心理记录、家庭冲突、位置或身份可识别资料。
