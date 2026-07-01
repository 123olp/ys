# Robotics Embodied Assistance Care Automation

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/robotics-embodied-assistance-care-automation` |
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


机器人、具身辅助与照护自动化域研究：主体如何通过机器人、自动化设备、外骨骼、家庭辅助系统和照护机器人获得移动、操作、陪护、监测、康复和日常任务支持。

## 对象

- 具身机器人、服务机器人、照护机器人、外骨骼、假肢、移动辅助、家庭自动化和远程操作。
- 日常生活活动、转移、取物、清洁、用药提醒、跌倒响应、康复训练、陪伴和照护者减负。
- 人机协作、安全标准、性能测量、可靠性、故障模式、可访问性、维护、成本和责任归属。
- 机器人对独立生活、长期照护、残障服务、康复、家庭照护和劳动力短缺的影响。
- 隐私、依赖、歧视、误操作、机械伤害、监控化、情感欺骗和服务中断风险。

## Human Infra 价值

有效永生不只是活得更久，还需要身体和环境能继续执行任务。机器人与具身辅助把外部工具从“信息增强”推进到“物理行动增强”：帮助主体移动、照护自己、与环境交互，并在能力下降时保留更多独立性。

```text
具身辅助和照护自动化可用
  -> 移动、操作、康复、监测和日常照护负担下降
  -> 主体独立生活、行动密度和照护连续性提高
  -> 长期执行能力和可持续创造窗口扩大
```

## 边界

本域只整理公开的机器人、具身辅助、照护自动化、外骨骼、服务机器人、安全标准和性能测量资料。

不提供：

- 设备选购、改装、维修、医疗康复处方、照护替代、临床训练或安全认证建议。
- 绕过机器人安全限制、监控他人、操控受照护者、自动化危险动作或规避责任的方案。
- 对具体机器人、外骨骼、照护平台、公司或投资方向的背书。
- 把机器人陪伴写成真实社会关系替代，或把自动化写成照护责任消失。

## 上游与下游

- 上游：`assistive-technology-access/`、`rehabilitation-functioning/`、`caregiving-long-term-care/`、`manufacturing-repair-capacity/`。
- 下游：`disability-services-independent-living/`、`home-health-hospice-palliative-care-continuity/`、`occupational-work-design/`、`cognitive-augmentation/`。

## 初始资料线索

- NIST robotics and robot performance measurement materials: https://www.nist.gov/el/robotics
- Assistive technology, rehabilitation robotics and service robotics standards literature.
- FDA and medical device public materials for robotic medical systems where applicable.
- Human factors, safety and reliability research for embodied human-robot interaction.

## 下一步

- 建立具身辅助变量表：任务类型、自由度、负载、错误率、故障模式、人工接管、维护周期、成本和隐私风险。
- 整理 Source Cards：NIST robotics、assistive robotics、exoskeletons、rehabilitation robots、service robots 和 safety standards。
- 区分辅助、医疗器械、照护服务、家庭自动化和工业自动化，避免责任边界混乱。
