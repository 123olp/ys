# Parks Recreation Green Space Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/parks-recreation-green-space-access-continuity` |
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


`parks-recreation-green-space-access-continuity` 研究公园、绿地、步道、运动场、游乐场、社区娱乐设施和自然接触如何影响身体活动、心理恢复、社交连接、热环境缓冲和公共生活参与。

> 核心问题：公园不是装饰性绿化，而是低成本恢复和行动空间；当绿地不可达、不安全或不可用，身体、心理、社交和热暴露都会失去缓冲层。

## 关注对象

- 公园、绿地、步道、球场、游乐场、社区运动设施、自然区域、开放空间和公共娱乐项目。
- 步行可达性、维护、安全感、照明、无障碍、树冠、水源、厕所、活动项目、费用、开放时段和环境质量。
- 与身体活动、心理健康、儿童发展、老年友好城市、热岛缓解、社区安全、城市规划和生态系统服务的接口。

## Human Infra 链路

```text
公园、娱乐和绿地接入稳定
  -> 身体活动、恢复、社交、自然接触和热环境缓冲更可持续
  -> 久坐、孤立、压力、儿童活动不足和高温暴露风险下降
  -> 主体可以低成本维护身体、情绪、关系和社区参与
  -> 主体健康寿命、恢复能力和公共生活选择权增强
```

## 非目标

- 不提供违规进入、逃避公园管理、破坏设施、骚扰游客、跟踪儿童或弱势群体、露宿规避、野外风险操作或个案执法建议。
- 不替代公园部门、公共卫生、城市规划、学校、生态管理、治安机构、医疗或心理健康专业服务。
- 不收集儿童位置、个人活动轨迹、敏感生态点位、设施安防细节或实时拥挤数据。

## Source Signals

- CDC Physical Activity and Built Environment: https://www.cdc.gov/physical-activity/php/toolkit/index.html
- CDC Parks, Trails, and Health: https://www.cdc.gov/physical-activity/php/toolkit/parks-trails-health.html
- EPA Green Infrastructure: https://www.epa.gov/green-infrastructure
- National Recreation and Park Association: https://www.nrpa.org/

## 下一步

- 建立 `green space -> access quality -> activity/recovery/social exposure -> healthspan impact -> subject continuity` 变量表。
- 区分邻里公园、区域公园、步道、运动设施、游乐场、自然区域和公共娱乐项目。
- 与 `physical-activity-mobility`、`mental-health-stress-resilience`、`green-blue-infrastructure-urban-nature-cooling`、`public-seating-shade-rest-cooling-access-continuity` 和 `urban-planning-land-use-zoning-resilience` 建立边界。
