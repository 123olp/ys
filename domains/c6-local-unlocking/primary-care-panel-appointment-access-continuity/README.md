# Primary Care Panel Appointment Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/primary-care-panel-appointment-access-continuity` |
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

本域研究初级照护、panel、new patient intake、年度体检、慢病随访、同日预约、远程/线下入口和连续关系如何把医疗系统转化为主体的常规维护界面。

它不是个体诊断、医生选择、预约抢号或健康管理建议入口。

## 先验问题

```text
医疗系统何以维护主体而不是只处理危机？
  -> 主体必须有可进入的初级照护入口
  -> 初诊、随访、预防、慢病和转诊关系必须连续
  -> panel 和预约容量必须能吸收真实需求
  -> 否则问题会累积到急诊、住院或不可逆损伤
```

## 研究对象

- Primary care、family medicine、internal medicine、pediatrics 和 community health centers。
- Panel size、new patient access、same-day access、annual wellness、follow-up 和 chronic care visits。
- FQHC、HRSA health center、patient-centered medical home 和 team-based care。
- 远程初级照护、语言服务、交通、数字入口和预约改期。

## 关键变量

- 初诊等待时间、新患者接收率、随访间隔和 missed appointment。
- Panel capacity、PCP-to-population ratio、连续性指数和常规来源照护比例。
- 预防服务完成、慢病监测间隔、转诊启动率和患者门户可用性。

## 证据入口

- HRSA health centers、AHRQ primary care、CMS preventive services 和 Medicare wellness visit 资料。
- CDC / Healthy People primary care access 指标。
- NCQA patient-centered medical home 和卫生服务研究。

## 非目标

- 不推荐医生、诊断、检查、药物、慢病方案、预约技巧或抢号方法。
- 不提供保险选择、资格判断、FQHC 申请、病历整理或个案转诊建议。
- 不收集病历、保险、预约、地址、症状、用药或健康门户信息。

## 上下游

- 上游：`provider-directory-network-adequacy-continuity/`、`healthcare-access-continuity/`、`community-resource-navigation/`。
- 下游：`specialist-referral-authorization-navigation-continuity/`、`appointment-availability-wait-time-continuity/`、`medication-reconciliation-regimen-adherence-continuity/`。
