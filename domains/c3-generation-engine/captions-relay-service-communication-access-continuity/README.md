# Captions Relay Service Communication Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/captions-relay-service-communication-access-continuity` |
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


`captions-relay-service-communication-access-continuity/` 负责整理字幕、实时转写、电话中继服务、视频会议可访问性和非听觉沟通通道连续性。

核心问题：

> 当声音无法稳定接入时，主体仍需要通过字幕、文字、手语、转写和中继服务进入教育、医疗、工作、法律、公共服务和亲密关系。

## 先验位置

```text
主体持续性最大化
  -> 主体必须持续理解他人、服务、会议和公共信息
  -> 听觉通道受限时，沟通必须转译为视觉、文字或中继服务
  -> 字幕、实时转写和电话/视频中继决定非听觉沟通能否进入关键场景
  -> 因此字幕与中继服务连续性是听觉限制后的沟通访问基础设施
```

## 关注对象

- 字幕、实时转写、CART、电话中继服务、视频中继、会议字幕和平台可访问性。
- 医疗、教育、法院、工作、公共服务、媒体、紧急信息和家庭沟通。
- 准确性、延迟、隐私、语言可达性、费用、平台兼容和服务可靠性。
- 与 `language-access-plain-communication/` 的关系：本域聚焦听觉限制下的沟通通道转译。

## Human Infra 模型链路

```text
字幕 / 实时转写 / 中继服务 T
  -> 改变沟通可达性、准确性、延迟、隐私和平台兼容变量 X
  -> 改变主体医疗、教育、工作、法律和关系参与状态 S
  -> 改变服务排除、误解、权利受损、任务失败和社会孤立风险
  -> 增加沟通访问、行动资格和未来选择权
```

## 非目标

- 不提供法律合规判断、具体平台采购、字幕质量认证、翻译解释、手语服务安排或个人便利资格建议。
- 不把自动字幕、AI 转写或中继服务写成完整替代人工有效沟通的方案。
- 不替代听力学、无障碍合规、法律、教育、医疗沟通或公共服务专业判断。

## Source Signals

- NIDCD Captions for Deaf and Hard-of-Hearing Viewers: https://www.nidcd.nih.gov/health/captions-deaf-and-hard-hearing-viewers
- FCC Telecommunications Relay Service: https://www.fcc.gov/consumers/guides/telecommunications-relay-service-trs
- ADA Effective Communication: https://www.ada.gov/resources/effective-communication/

## 下一步

- 建立字幕/中继 Source Card，区分实时沟通、媒体访问、医疗/法律/教育场景和隐私准确性终点。
- 对接语言可达、公共服务无障碍、会议工作和医疗沟通域。
