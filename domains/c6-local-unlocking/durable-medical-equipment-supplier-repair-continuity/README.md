# Durable Medical Equipment Supplier Repair Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/durable-medical-equipment-supplier-repair-continuity` |
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


## 定位

本域研究 durable medical equipment、prosthetics、orthotics、supplies、供应商、维修、替换、coverage、配送和服务中断如何影响主体在家中维持行动、呼吸、监测、照护和安全。

它不是设备维修教程、医保索赔策略或个案采购建议入口。

## 先验问题

```text
居家治疗和独立生活何以可执行？
  -> 设备和耗材必须按需供应、维护、维修和替换
  -> 供应商、支付方和临床处方必须协同
  -> 设备故障不能把慢病管理和独立生活变成单点失败
```

## 研究对象

- Medicare DMEPOS、供应商、coverage、订单、配送、维修和替换。
- 轮椅、助行器、病床、CPAP、泵、伤口护理 supplies、尿控/造口 supplies 等。
- 设备召回、可用性、维修延迟、供应商退出和灾害中断。
- 居家照护、残障服务和医疗设备安全交叉边界。

## 关键变量

- 供应商覆盖、交付时间、维修等待、替换审批和停用天数。
- 设备故障率、耗材短缺、召回响应和备用路径。
- coverage denial、out-of-pocket cost、供应商投诉和用户训练。

## 证据入口

- CMS / Medicare durable medical equipment 资料。
- FDA medical device safety / recalls、DMEPOS 供应商资料。
- ACL、残障独立生活、居家医疗和设备可用性研究。

## 非目标

- 不提供设备维修、改装、绕过安全机制、医保报销、供应商谈判或采购建议。
- 不判断某个设备、供应商、coverage、维修、替换或索赔个案。
- 不收集设备序列号、保险号、订单、处方、诊断、住址或供应商合同。

## 上下游

- 上游：`medical-device-equipment-safety-maintenance/`、`disability-services-independent-living/`、`home-health-hospice-palliative-care-continuity/`。
- 下游：`home-oxygen-respiratory-equipment-supply-continuity/`、`diabetes-insulin-glucose-monitoring-supplies-continuity/`、`assistive-technology-access/`。
