# Health Literacy Navigation

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/health-literacy-navigation` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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


Health Literacy Navigation 负责整理健康素养、医疗服务导航、可理解信息、共同决策、系统入口和服务使用能力。

核心问题：

> 医学和公共服务只有在主体能够理解、找到、进入、使用和复核时，才会转化为真实的主体持续性收益。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能理解风险、服务、证据和选择
  -> 医疗和社会系统必须可被导航、可被询问、可被复核
  -> 健康素养不足会把可用资源变成不可用资源
  -> 因此可理解性和导航能力是外部基础设施转化为主体收益的接口
```

## 关注对象

- 个人健康素养、组织健康素养、plain language、风险沟通、医疗导航和共同决策。
- 预约、转诊、保险、药品说明、检查结果、患者门户、语言可达和认知可达。
- 信息不对称、行政负担、迷宫式服务入口和错误理解风险。
- 与 `resource-social-infra/` 的关系：资源域关注服务供给；本域关注服务是否能被理解和实际使用。

## Human Infra 模型链路

```text
健康素养 / 导航工具 T
  -> 改变理解能力、系统入口、风险判断、服务使用和复核能力 X
  -> 改变主体决策状态 S
  -> 改变误用、延误、放弃服务、药物错误和资源排除风险
  -> 增强医疗可及性、有效时间和未来选择权
```

## 非目标

- 不提供医学、法律、保险或福利申请建议。
- 不伪装专业判断，不替代医生、律师、社工或危机服务。
- 不提供规避资格审查、欺诈、伪造材料或制度漏洞利用。

## Source Signals

- CDC Health Literacy: https://www.cdc.gov/health-literacy/
- HHS Health Literacy: https://health.gov/our-work/national-health-initiatives/health-literacy
