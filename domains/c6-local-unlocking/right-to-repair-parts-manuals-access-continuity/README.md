# 维修权、零件、手册与诊断接入连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/right-to-repair-parts-manuals-access-continuity` |
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


本域研究维修权、零件、维修手册、诊断工具、软件锁、独立维修和产品可修复性如何影响设备寿命、资源消耗和主体任务连续性。它关注维修接入作为反浪费和资源恢复基础设施，而不是拆机教程、绕过安全机制或个案维修建议。

## 研究对象

- 维修手册、零件供应、诊断工具、软件配对、固件限制、维修授权和独立维修市场。
- 手机、电脑、家电、车辆、医疗设备、农业设备和其他关键工具的可修复性边界。
- 产品寿命、维修成本、停机时间、备件可得性、废弃物和所有权控制。
- 与保修服务合同、制造维修能力、个人设备生命周期维修、家用电器维修和产品安全召回的边界。

## 价值链路

```text
主体依赖产品完成任务
  -> 零件、手册和诊断接入决定产品故障后能否被恢复
  -> 可修复性延长设备寿命并降低替换、等待和废弃成本
  -> 软件锁、配件封闭和资料缺失会把故障转化为强制替换
  -> 维修权连续性把产品所有权从消费许可转化为可维护的行动资产
```

## 关键问题

- 维修资料、零件和诊断工具的可得性如何影响产品寿命和主体任务中断？
- 保修限制、软件配对和授权维修网络如何改变维修市场与消费者控制权？
- 维修权如何与安全、隐私、网络安全、知识产权和产品责任边界冲突？
- 哪些设备属于主体持续性关键工具，故障会放大到医疗、工作、通信或照护风险？

## 上游与下游

- 上游：`manufacturing-repair-capacity/`、`consumer-warranty-service-contract-repair-continuity/`、`personal-computing-device-lifecycle-repair-continuity/`、`household-appliance-maintenance-repair-continuity/`。
- 下游：`waste-management-hazardous-materials-continuity/`、`critical-minerals-materials-resilience/`、`software-update-vulnerability-patch-continuity/`、`product-safety-recall-systems/`。

## 非目标

- 不提供拆机、绕锁、破解、固件修改、DRM 规避、危险电气/燃气/医疗设备维修或个案维修操作。
- 不判断某个产品是否应维修、某个厂商是否合法、某个维修行为是否安全或某个法律是否适用。
- 不协助绕过安全锁、访问受保护诊断系统、规避产品安全控制、侵犯知识产权或处理个人设备隐私数据。

## 初始资料入口

- FTC: Nixing the Fix report
- FTC: Right to repair policy and consumer protection materials
- U.S. PIRG / iFixit public right-to-repair materials as secondary context
- State right-to-repair official statutes and agency materials
