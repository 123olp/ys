# missing-persons-unidentified-remains-resolution-continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/missing-persons-unidentified-remains-resolution-continuity` |
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


`missing-persons-unidentified-remains-resolution-continuity` 研究 missing persons、unidentified persons、unclaimed persons、family reporting、law enforcement interface、forensic data、NamUs、death investigation 和 family notification 如何影响主体身份恢复、家庭持续性、哀悼、法律记录和遗属资源。

## Scope

- Missing persons、unidentified remains、unclaimed persons、NamUs、law enforcement reporting、medical examiner / coroner interface、DNA/dental/fingerprint data 和 family assistance。
- 成年人、儿童、失踪原住民、灾害、迁移、无家可归、认知障碍、拘押和死亡记录交叉风险。
- 资料质量、隐私、错误身份、家属通知、未成年人、媒体传播和二次伤害边界。

## Continuity Logic

```text
人员失踪或身份未确认
-> 主体身份、家庭关系、死亡事实、法律记录和遗属资源悬置
-> 报告、搜索系统、法医数据、身份确认和家属通知成为恢复接口
-> 记录断裂会延长不确定性、阻断福利/遗产/哀悼，并增加误认和二次伤害
```

## Source Spine

- NamUs missing, unidentified, and unclaimed persons public materials.
- DOJ / NIJ missing persons and forensic identification materials.
- FBI missing persons public resources where relevant.
- NCMEC public materials for children, when used only as system context.

## Evidence Boundary

本域只整理公开失踪人员、无名遗体、无人认领遗体、身份确认和家属通知资料。

Do not include:

- 个案搜索建议、定位、私自调查、线索扩散、公开指认、尸体识别判断、媒体动员或法律建议。
- 可识别失踪者、家属、儿童、证人、嫌疑人、地址、实时位置、DNA/医疗/法医资料或案件编号。
- 骚扰家属、嫌疑人、证人、机构人员，传播未经核实线索，或干扰执法/法医工作的内容。

## Upstream / Downstream

- Upstream: `personal-safety-violence-prevention/`, `disaster-mortality-missing-person-accounting-continuity` if added later, `cognitive-decline` and `migration` related domains.
- Downstream: `death-certificate-registration-cause-of-death-record-continuity/`, `survivor-benefits-death-notification-continuity/`, `cemetery-memorial-remains-location-continuity/`, `bereavement-leave-grief-support-continuity/`.
