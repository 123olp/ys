# Newborn Screening Result Followup Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/newborn-screening-result-followup-continuity` |
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


本目录承载新生儿筛查、结果路由、异常通知、诊断确认转介、家庭沟通和州级项目接口资料。它处理筛查到随访的系统连续性，不处理个体筛查结果或治疗决策。

## 目录结构

```text
newborn-screening-result-followup-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 记录 newborn screening program、specimen collection、result routing、abnormal notification、confirmatory referral、family communication 和 privacy boundary。
- 关注筛查信号是否能进入儿科、专科、公共卫生和家庭支持闭环。
- 不提供筛查结果解释、遗传判断、诊断、治疗、喂养、药物或急诊建议。

## 维护规则

- 新增资料优先引用 CDC、HRSA、州级 newborn screening program、AAP 或公开公共卫生资料。
- 涉及婴儿、遗传、家庭成员、实验室结果和罕见病时必须保留高敏感边界。
- 不把公共卫生筛查资料转化为个体诊断、风险分层、治疗或家庭检测建议。
