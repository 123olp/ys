# Death Certificate Registration Cause Of Death Record Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/death-certificate-registration-cause-of-death-record-continuity` |
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


Death Certificate Registration Cause Of Death Record Continuity 研究死亡证明、死亡登记、死因记录、认证副本和生命统计如何把死亡事实转化为公共卫生、法律、保险、遗属福利和账户关闭可承认的基础记录。

> 核心问题：死亡事实如果不能被准确登记和证明，遗属福利、保险理赔、遗产交接、公共卫生统计和服务关闭都会卡在第一道行政门槛。

## 研究对象

- Death certificate、death registration、cause of death、certified copy、medical certification 和 vital statistics。
- 医疗机构、法医/验尸官、民事登记、生命统计系统、公共卫生机构和遗属申请链。
- 死亡记录更正、延迟登记、跨州/跨境死亡、非自然死亡、身份不明和死因分类边界。

## 先验链路

```text
主体死亡后仍会触发遗属、制度和公共卫生连续性任务
  -> 这些任务需要一个可被机构承认的死亡事实和死因记录
  -> 死亡证明若缺失、错误、延迟或无法取得，福利、理赔、遗产、账户关闭和统计学习无法启动
  -> 遗属资源、法律交接、风险监测和公共卫生反馈形成阻塞
  -> 幸存者行动能力与社会系统学习能力下降
  -> 因而死亡证明、登记和死因记录是死亡边界后的第一基础记录层
```

## 关键变量

- 登记及时性、死因准确性、认证副本可得性、记录更正路径和跨机构承认。
- 医疗认证者、法医/验尸官、登记机关、公共卫生统计和遗属申请之间的责任边界。
- 身份不明、灾害死亡、跨境死亡、无亲属、暴力死亡、隐私和污名风险。

## 证据入口

- CDC / NCHS mortality、NVSS 和 death certificate materials。
- USA.gov death certificate and death of a loved one materials。
- State vital records and medical examiner / coroner public materials。

## 非目标

- 本域不办理、代写、解释或更正死亡证明。
- 不判断死因、死亡方式、责任归属、保险适用、福利资格或法律效力。
- 不收集死亡证明、身份文件、病历、法医材料、亲属信息或案件资料。

## 上下游

- 上游：`vital-records-life-event-continuity/`、`emergency-contact-next-of-kin-notification-continuity/`、`organ-donor-registry-anatomical-gift-continuity/`。
- 下游：`survivor-benefits-death-notification-continuity/`、`life-insurance-beneficiary-claim-continuity/`、`estate-inventory-asset-liability-handoff-continuity/`、`post-death-account-closure-service-cancellation-continuity/`。
