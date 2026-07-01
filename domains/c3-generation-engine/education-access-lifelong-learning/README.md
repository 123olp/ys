# Education Access Lifelong Learning

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/education-access-lifelong-learning` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 主要放大主体学习、认知、工具使用和生成新路径的能力。 |
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


`education-access-lifelong-learning/` 研究教育可及、成人学习、再培训、基础技能、数字学习和终身学习系统如何把延长的时间窗口转化为可增长的能力。

> 核心问题：有效永生不是只让主体活得更久；如果教育、再训练和学习机会不可达，更长时间也可能停留在低能力、低选择权和低技术采用状态。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须持续学习、更新技能并适应新工具
  -> 学习能力依赖教育入口、基础技能、成人学习、再训练和可负担学习资源
  -> 教育排除、技能过时和学习机会断裂会让长寿无法转化为能力复利
  -> 因此教育可及与终身学习是主体能力持续升级的外部基础设施域
```

## 关注对象

- 学前、基础、中等、高等、职业、成人、继续教育和终身学习系统。
- 基础读写算、数字技能、AI 协作技能、再培训、技能迁移和工作转换学习路径。
- 教育成本、地理可达、残障可达、语言可达、在线学习、学习认证和学习结果。
- 与 `learning-skill-acquisition/` 的边界：本域关注社会教育系统和机会结构；学习技能域关注主体内部学习机制、反馈和技能形成过程。
- 与 `workforce-employment-services/` 的边界：本域关注学习机会；就业服务域关注工作入口、再就业服务和劳动力市场连接。

## Human Infra 模型链路

```text
教育可及与终身学习 T
  -> 改变学习机会、基础技能、再培训、认证、数字能力和技能迁移变量 X
  -> 改变主体能力增长、技术采用、职业转换和问题求解状态 S
  -> 改变技能过时、收入断裂、技术排除和未来选择权损失风险 λ(t)
  -> 影响有效时间、能力复利、任务解决范围和主体持续性
```

## 非目标

- 不提供个人升学、择校、留学、考试、职业培训、证书选择或教育投资建议。
- 不把教育指标写成个体智力、价值或未来成就判断。
- 不支持用学习系统压榨休息、照护、健康、关系或主体自主性。

## Source Signals

- UNESCO Lifelong Learning: https://www.unesco.org/en/lifelong-learning
- UNESCO Institute for Lifelong Learning: https://www.uil.unesco.org/
- World Bank Education: https://www.worldbank.org/en/topic/education
- OECD Skills: https://www.oecd.org/skills/
- ILO Skills and Lifelong Learning: https://www.ilo.org/skills

## 下一步

- 建立教育可及变量表：可负担性、可达性、基础技能、成人学习、认证、数字学习、技能迁移和学习结果。
- 与 `learning-skill-acquisition/`、`digital-inclusion-connectivity/`、`workforce-employment-services/` 和 `media-information-literacy-public-libraries/` 建立接口。
