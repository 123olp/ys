# Chemical Release Shelter Evacuation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/chemical-release-shelter-evacuation-continuity` |
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


`chemical-release-shelter-evacuation-continuity/` 研究化学释放事故中就地避险、撤离、警报理解、交通转移、家庭/学校/工作场所接续和恢复入口如何保护主体持续性。

> 核心问题：化学释放不是单点暴露事件；如果人不知道何时避险、何时撤离、如何接上医疗、交通、照护和住宿，事故会把可控暴露变成大范围生活断裂。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体长期行动依赖可呼吸、可居住、可撤离的环境
  -> 化学释放使空气、水、道路、学校、工作和家庭照护同时进入不确定状态
  -> 就地避险与撤离连续性把危险信号转化为可执行、可恢复、可转介的行动链
```

## 关注对象

- 化学事故警报、就地避险、撤离、公共沟通、交通断点、临时安置和恢复入口。
- 家庭、学校、工作场所、长期照护机构和残障功能需求人群在化学释放中的连续性。
- 与 `chemical-safety-poison-control-toxicology/` 的关系：化学安全域关注毒理和暴露治理；本域关注事故发生后的避险/撤离执行链。

## Human Infra 模型链路

```text
化学释放避险与撤离连续性
  -> 改变暴露时长、错误行动、交通断点、照护断点和恢复入口
  -> 改变急性伤害、长期健康损害、居住中断和工作学习中断风险
  -> 增强主体生存、恢复、行动和未来选择权
```

## 非目标

- 不提供具体化学品处置、防护搭建、去污、撤离路线、现场判断或实时指挥。
- 不提供中毒处理、解毒、医疗分诊、法律索赔、保险、企业合规或责任判断。
- 不提供规避警报、规避监管、隐藏释放源、制造恐慌或破坏设施的信息。

## Source Signals

- Ready.gov chemical emergencies: https://www.ready.gov/chemical
- CDC chemical emergencies: https://www.cdc.gov/chemical-emergencies/
- FEMA protective actions and emergency management resources: https://www.fema.gov/emergency-managers
- EPA chemical emergency preparedness and prevention: https://www.epa.gov/chemical-emergency-preparedness-and-prevention

## 下一步

- 建立 Chemical Release Continuity Card：release signal, protective action, evacuation/shelter, transport, care dependency, re-entry, recovery referral。
- 与 `emergency-alerts-communications/`、`household-emergency-preparedness-resilience/`、`transportation-access-mobility/` 和 `disaster-recovery-relief-continuity/` 建立接口。
