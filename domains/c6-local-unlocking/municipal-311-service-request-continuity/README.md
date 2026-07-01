# Municipal 311 Service Request Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/municipal-311-service-request-continuity` |
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


`municipal-311-service-request-continuity/` 研究 311、非紧急服务请求、地方公共工程派单、状态回传和服务请求数据如何影响主体在邻里环境中的问题报告、跟踪和恢复能力。

## 先验链路

```text
主体要在社区中持续行动
  -> 邻里问题必须能从个人观察转成公共机构可处理的请求
  -> 请求需要渠道、分类、位置、编号、责任部门和状态回传
  -> 311 / Open311 / 地方服务请求系统把问题转成可派单的公共服务对象
  -> 请求失败会让路灯、坑洞、垃圾、积水、标志、噪声和通行障碍长期滞留
  -> 日常出行、照护、工作、学习、公共安全和邻里信任被持续消耗
```

## 研究对象

- 311、non-emergency service request、Open311 / GeoReport、service category、request status、department routing、SLA、closure code、公开服务请求数据和回传机制。

## 不能做

- 不提供紧急报警替代、执法规避、骚扰举报、虚假投诉、个人跟踪、位置监控、投诉代写、法律策略、政治动员或个案市政服务申诉建议。
- 不收集、复制或要求家庭地址、精确位置、照片、车牌、邻居身份、联系方式、执法记录、账号、投诉记录或其他敏感资料。

## Source Signals

- Open311 GeoReport v2: https://wiki.open311.org/GeoReport_v2/
- NYC Open Data 311 service requests: https://opendata.cityofnewyork.us/
- Code for America 311 and civic service context: https://www.codeforamerica.org/
- USA.gov local governments: https://www.usa.gov/local-governments

## 上下游关系

- 上游：`public-service-design-accessibility/`、`civic-data-open-government-transparency/`、`public-works-civil-infrastructure-asset-management/`。
- 下游：`streetlight-outage-nighttime-visibility-continuity/`、`sidewalk-curb-ramp-maintenance-access-continuity/`、`storm-drain-catch-basin-local-flooding-continuity/`。
