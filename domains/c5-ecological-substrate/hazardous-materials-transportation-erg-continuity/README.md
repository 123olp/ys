# Hazardous Materials Transportation ERG Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/hazardous-materials-transportation-erg-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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


`hazardous-materials-transportation-erg-continuity/` 研究危险材料运输、标识、应急响应指南、铁路/公路/管道/港口接口和社区交通中断如何影响主体持续性。

> 核心问题：危险材料不只存在于固定设施；运输路径把风险带到道路、铁路、港口、社区和供应链节点，事故会同时冲击通勤、物流、医疗和居住。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖危险材料被安全运输且事故可被快速识别
  -> 运输事故把化学风险、交通中断、供应链断点和社区暴露叠加
  -> ERG 与运输应急连续性把移动风险转化为可识别、可沟通、可转运恢复的系统
```

## 关注对象

- PHMSA ERG、危险品运输、标识、铁路/公路/管道/港口事故、交通绕行、物流中断和公共沟通。
- 与 `freight-logistics-port-cold-chain-continuity/` 的关系：物流域关注供应连续；本域关注危险材料运输事故风险和响应接口。

## Human Infra 模型链路

```text
危险材料运输应急连续性
  -> 改变事故识别、公共沟通、交通中断、供应链断点和暴露控制
  -> 改变通勤、医疗可达、物流恢复和社区环境安全
  -> 支撑主体移动、照护、工作和恢复能力
```

## 非目标

- 不提供运输路线、包装、装卸、隔离距离、处置步骤、标识规避或违法运输建议。
- 不提供实时道路/铁路/港口行动、企业合规、事故责任、保险或法律判断。
- 不把 ERG 或运输资料转化为危险品操作、规避检查或事故制造信息。

## Source Signals

- PHMSA Emergency Response Guidebook: https://www.phmsa.dot.gov/hazmat/erg/emergency-response-guidebook-erg
- PHMSA hazardous materials safety: https://www.phmsa.dot.gov/hazmat
- DOT Pipeline and Hazardous Materials Safety Administration: https://www.phmsa.dot.gov/
- National Response Center: https://nrc.uscg.mil/

## 下一步

- 建立 HazMat Transport Card：transport mode, identification interface, community exposure, traffic disruption, supply impact, public communication。
- 与 `transportation-access-mobility/`、`freight-logistics-port-cold-chain-continuity/` 和 `emergency-alerts-communications/` 建立接口。
