# refractive-error-glasses-contact-lens-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/refractive-error-glasses-contact-lens-continuity` |
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


## 职责

- 维护屈光矫正连续性的研究边界、变量表、证据入口和禁止用途。
- 将近视、远视、散光、老花、验光、眼镜、隐形眼镜、费用和更新摩擦整理为 Source Card、机制链和模型变量。
- 与 `vision-eye-health-continuity/`、`education-access-lifelong-learning/`、`workforce-employment-services/`、`transportation-access-mobility/` 保持边界清晰。

## 非目标

- 不提供验光处方、度数建议、隐形眼镜适配、儿童近视控制、品牌推荐、购买建议或个人医疗判断。
- 不替代验光、眼科、学校筛查、职业安全或交通资格评估。

## 上游

- `vision-eye-health-continuity/`：视觉输入总框架。
- `healthcare-access-continuity/`：验光和眼科服务可及性。
- `public-health-screening-prevention/`：筛查和早期发现框架。

## 下游

- `education-access-lifelong-learning/`：儿童与成人学习入口。
- `transportation-access-mobility/`：驾驶和空间行动。
- `time-allocation-effective-time/`：低清晰度造成的任务摩擦。
