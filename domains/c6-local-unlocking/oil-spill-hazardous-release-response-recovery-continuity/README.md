# Oil Spill Hazardous Release Response Recovery Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/oil-spill-hazardous-release-response-recovery-continuity` |
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


`oil-spill-hazardous-release-response-recovery-continuity/` 研究油类和危险物质释放对水域、海岸、渔业、饮用水、旅游、工人安全和社区恢复的影响，以及响应恢复系统如何维持主体持续性。

> 核心问题：油污和危险物质释放不是单纯环境事件；它会切断食物、收入、住房、交通、水源、文化生活和长期信任。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体长期行动依赖水域、海岸、食物和收入系统不被污染长期锁死
  -> 油污与危险释放会把生态损害转化为健康、收入、迁移和恢复负担
  -> 响应与恢复连续性把污染事件转化为可补救、可监测、可赔付、可恢复的公共过程
```

## 关注对象

- 油污、危险物质释放、水域污染、海岸恢复、工人安全、渔业旅游、饮用水、社区经济和长期监测。
- 与 `water-resources-hydrology-flood-drought-management/` 的关系：水资源域关注水文管理；本域关注事故性污染释放后的响应恢复链。

## Human Infra 模型链路

```text
油污与危险释放响应恢复
  -> 改变环境暴露、收入断点、食物水源风险、清理工人风险和社区恢复速度
  -> 改变健康寿命、有效时间、经济安全和地方信任
  -> 支撑污染后主体继续居住、工作、恢复和选择
```

## 非目标

- 不提供清理技术、围控、分散剂、采样、现场进入、工人防护、索赔策略或法律建议。
- 不提供事故责任判断、企业合规、生态修复设计、投资或保险建议。
- 不把公开资料转化为污染制造、责任规避或现场行动指令。

## Source Signals

- NOAA Office of Response and Restoration: https://response.restoration.noaa.gov/
- EPA oil spills prevention and preparedness: https://www.epa.gov/oil-spills-prevention-and-preparedness-regulations
- National Response Center: https://nrc.uscg.mil/
- CDC/NIOSH oil spill response worker safety context: https://www.cdc.gov/niosh/

## 下一步

- 建立 Spill Recovery Card：release type, water/coast interface, worker risk, food/income impact, monitoring, claims/referral boundary。
- 与 `water-wastewater-utility-service-continuity/`、`food-security-nutrition-access/`、`workforce-employment-services/` 和 `environmental-justice-exposure-equity-continuity/` 建立接口。
