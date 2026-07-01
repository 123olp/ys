# Invasive Species Human Health Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/invasive-species-human-health-access-continuity` |
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


`invasive-species-human-health-access-continuity` 研究入侵物种、生态系统改变、过敏/毒性/病媒/通行风险和公共空间可达如何影响主体持续性。

> 核心问题：入侵物种不是纯生态话题；它会改变病媒生态、过敏原、火灾燃料、水体状态、户外通行、农业和公共空间维护成本。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖稳定生态系统提供食物、水、空气、通行和恢复空间
  -> 入侵物种会改变生态服务、暴露结构和维护成本
  -> 监测、治理、风险沟通、跨部门协调和恢复计划构成环境前提
  -> 若该前提失败，户外行动、公共空间、农业、水体和病媒控制都会被长期重定价
```

## 关注对象

- 入侵植物/动物/病原、过敏原、毒性接触、病媒宿主、通行受阻、火灾燃料和生态服务损耗。
- 早期发现、快速响应、公众报告、生态恢复、维护预算和健康影响沟通。
- 与 `biodiversity-ecosystem-services-resilience/` 的边界：上位域关注生态服务；本域关注入侵物种对主体行动与健康暴露的执行层。

## Human Infra 链路

```text
入侵物种风险被监测和治理
  -> 病媒、过敏、毒性、通行和生态服务损耗下降
  -> 公共空间、农业、水体和居住环境更稳定
  -> 长期环境支持和主体行动选择权被保护
```

## 非目标

- 不提供物种鉴定、清除操作、农药/除草剂使用、土地管理、捕捉处置、法规合规或生态补偿建议。
- 不替代 USDA、地方自然资源机构、农业推广、公共卫生、物业、市政或生态专家。
- 不把观察记录、地图、AI 识别或个案照片写成处置方案、风险等级或执法判断。

## Source Signals

- USDA National Invasive Species Information Center: https://www.invasivespeciesinfo.gov/
- U.S. Fish and Wildlife Service Invasive Species: https://www.fws.gov/program/invasive-species
- EPA Invasive Species: https://www.epa.gov/watershedacademy/invasive-non-native-species

## 下一步

- 建立 `invasive species -> ecosystem service / exposure shift -> maintenance burden -> continuity cost` 变量表。
- 区分病媒生态、过敏植物、水体入侵、农业损耗、火灾燃料和公共通行场景。
