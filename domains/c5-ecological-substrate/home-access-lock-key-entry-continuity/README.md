# Home Access Lock Key Entry Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-access-lock-key-entry-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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


`home-access-lock-key-entry-continuity` 研究住所进入权、钥匙、门锁、智能锁、门禁码、备用入口、访客授权和紧急出入如何影响主体能否持续进入自己的恢复空间与资料空间。

> 核心问题：住房存在不等于主体能进入；如果钥匙丢失、锁具失效、门禁权限断裂或紧急出入被误设计，睡眠、药品、证件、设备、照护和工作都会被本地访问失败截断。

## 关注对象

- 物理钥匙、备用钥匙、门锁、门禁、智能锁、门铃、访客授权、临时密码和权限撤销。
- 紧急逃生、消防疏散、无障碍出入、照护者进入、维修人员进入和租住场景下的授权边界。
- 锁具失效、停电、网络中断、电池耗尽、账号失效、权限误删、住址变更和家庭成员变化。
- 与住房稳定、建筑消防、家庭网络 IoT 安全、数字身份、失能代理和家庭应急准备的接口。

## Human Infra 链路

```text
住所进入连续
  -> 主体能稳定进入睡眠、恢复、药品、文件、设备和照护空间
  -> 锁具、钥匙、门禁、权限和紧急出入失效成本下降
  -> 住房从名义资产转化为可用恢复环境与本地任务基地
  -> 日常行动、照护交接、应急恢复和主体安全连续性增强
```

## 非目标

- 不提供开锁、绕过门禁、破解智能锁、入侵住宅、跟踪定位或非法进入方法。
- 不替代本地消防、建筑、租赁、物业、执法或 locksmith 专业服务。
- 不收集个人住址、钥匙位置、门禁码、锁具型号、摄像头信息或家庭成员权限。

## Source Signals

- NFPA Home Fire Escape Planning: https://www.nfpa.org/education-and-research/home-fire-safety/escape-planning
- CPSC Consumer Product Safety Recalls: https://www.cpsc.gov/Recalls
- NIST Digital Identity Guidelines: https://pages.nist.gov/800-63-3/
- FTC Smart Home and IoT consumer guidance: https://consumer.ftc.gov/

## 下一步

- 建立 `access credential -> authorized person -> entry event -> failure mode -> recovery path` 变量表。
- 区分所有权、租住、合住、照护者进入、维修进入和应急进入的授权边界。
- 与 `housing-built-environment-stability`、`building-fire-life-safety-codes`、`home-network-router-iot-security-continuity` 和 `household-emergency-preparedness-resilience` 建立边界。
