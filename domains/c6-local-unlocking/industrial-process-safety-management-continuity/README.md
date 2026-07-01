# Industrial Process Safety Management Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/industrial-process-safety-management-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->


`industrial-process-safety-management-continuity/` 研究高危化学工艺、过程安全管理、风险管理计划、机械完整性、变更管理和事故预防如何防止工作与社区环境被重大事故切断。

> 核心问题：工业系统的价值不只在产出；一旦过程安全失败，工厂、工人、社区、交通、空气、水和公共信任都会同时受损。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体长期行动依赖生产系统不把风险外溢给工人和社区
  -> 高危工艺把能量、压力、易燃性和毒性集中在组织边界内
  -> 过程安全管理把事故预防、维护、变更和学习转化为主体环境稳定条件
```

## 关注对象

- OSHA PSM、EPA RMP、机械完整性、操作程序、变更管理、事故调查、承包商和组织学习。
- 近失误、维护延迟、自动化报警、生产压力、外包边界、监管报告和社区风险。
- 与 `occupational-exposure-industrial-hygiene/` 的关系：工业卫生关注日常暴露；本域关注重大过程事故和组织控制。

## Human Infra 模型链路

```text
过程安全管理
  -> 改变重大事故概率、工人伤亡、社区暴露、设施停摆和供应中断
  -> 改变有效时间、收入连续性、环境安全和社会信任
  -> 支撑主体持续存在、工作、恢复和长期居住
```

## 非目标

- 不提供工艺参数、设备调试、危险化学品操作、漏洞利用、绕过联锁或企业合规建议。
- 不提供事故调查结论、责任认定、诉讼、保险、投资或监管规避策略。
- 不把过程安全资料写成制造事故、隐藏风险或优化危险工艺的工具。

## Source Signals

- OSHA Process Safety Management: https://www.osha.gov/process-safety-management
- EPA Risk Management Program: https://www.epa.gov/rmp
- U.S. Chemical Safety and Hazard Investigation Board: https://www.csb.gov/
- NIOSH chemical safety and engineering controls: https://www.cdc.gov/niosh/

## 下一步

- 建立 Process Safety Continuity Card：hazard class, safeguards, maintenance, change management, incident learning, worker/community interface。
- 与 `manufacturing-repair-capacity/`、`occupational-exposure-industrial-hygiene/` 和 `patient-safety-organizational-learning/` 建立组织学习接口。
