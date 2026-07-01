# Estate Inventory Asset Liability Handoff Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/estate-inventory-asset-liability-handoff-continuity` |
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


Estate Inventory Asset Liability Handoff Continuity 研究遗产清单、资产负债盘点、executor / personal representative、债权通知、文件交接和 probate 前后任务如何把死亡后的事务从混乱转为可执行队列。

> 核心问题：死亡后真正困难的往往不是“有没有遗产”，而是资产、债务、文件、受益人和责任人能否被看见、排序、交接和关闭。

## 研究对象

- Estate inventory、asset list、liability list、executor、personal representative、probate task queue 和 creditor notice。
- 银行、房产、车辆、税务、债务、订阅、数字资产、保险、养老金和家庭文件的死亡后盘点。
- 无遗嘱、小额遗产、共同账户、联名资产、家庭冲突、债务催收和记录缺失。

## 先验链路

```text
死亡后主体留下资产、债务、合同、文件和未完成责任
  -> 执行人或遗属需要先盘点事实，再决定通知、支付、转移、关闭或争议
  -> 清单缺失、记录碎片化或责任人不清会导致资产流失、债务误处理和账户遗留
  -> 遗属时间、注意力、财务韧性和家庭关系被持续消耗
  -> 死亡后的资源交接无法稳定支持幸存者未来
  -> 因而遗产资产负债清单是死亡后事务执行的任务编排层
```

## 关键变量

- 资产可发现性、负债可确认性、文件位置、执行人权限、债权通知、清单更新和账户关闭状态。
- Probate、小额遗产、信托、联名账户、受益人资产、税务、债务、数字资产和家庭文件边界。
- 欺诈、家庭冲突、过度催收、身份盗用、遗失资产、无亲属和隐私风险。

## 证据入口

- USA.gov wills, estates and death of a loved one materials。
- State probate court, small-estate and consumer protection materials。
- CFPB / FTC debt collection, identity theft and consumer protection materials。

## 非目标

- 本域不提供 probate、遗产规划、税务、债务、执行人、资产分配或法律建议。
- 不代写遗产清单、通知、遗嘱、法院文件、债权人信或家庭协议。
- 不收集资产、负债、账户、遗嘱、家庭关系、税务、房产或法院材料。

## 上下游

- 上游：`trust-estate-affairs-succession-continuity/`、`death-certificate-registration-cause-of-death-record-continuity/`、`life-insurance-beneficiary-claim-continuity/`。
- 下游：`post-death-account-closure-service-cancellation-continuity/`、`debt-obligation-collection-relief-continuity/`、`real-property-title-deed-record-continuity/`、`digital-legacy-data-succession/`。
