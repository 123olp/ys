# Mask Respirator Source Control Fit Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/mask-respirator-source-control-fit-access-continuity` |
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


`mask-respirator-source-control-fit-access-continuity/` 研究口罩、呼吸防护、源头控制、适配、可得性和使用治理如何降低暴发期间的空气传播风险。

> 核心问题：呼吸防护不是单个用品选择；它是公共空间能否继续学习、工作、照护和服务的低摩擦风险控制层。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 暴发期间呼吸暴露会压缩公共空间行动能力
  -> 口罩、呼吸防护和源头控制改变单位接触风险
  -> 防护可得性和适配决定主体能否在必要场景中继续行动
```

## 关注对象

- 口罩、呼吸器、源头控制、适配、可得性、工作场所呼吸防护、学校/公共场所政策和风险沟通。
- 与 `air-quality-ventilation-exposure-control/` 的关系：空气质量域关注空间暴露环境；本域关注个人/人群层的呼吸源头控制与防护接口。

## Human Infra 模型链路

```text
口罩与呼吸防护可达性
  -> 改变空气传播暴露、源头控制、工作学校开放风险和高风险主体保护
  -> 改变感染概率、停工停课概率和公共空间信任
  -> 降低暴发期间行动中断和医疗系统负担
  -> 增强有效行动、关系参与和主体持续性
```

## 非目标

- 不提供个人产品推荐、佩戴教程、fit testing 指令、职业合规、医疗建议或法律建议。
- 不提供防护规避、假冒认证、PPE 抢占、场所对抗或风险补偿策略。
- 不替代 OSHA/NIOSH、雇主 respiratory protection program 或医疗判断。

## Source Signals

- CDC masks and respirators: https://www.cdc.gov/respiratory-viruses/prevention/masks.html
- CDC NIOSH respirators: https://www.cdc.gov/niosh/npptl/topics/respirators/
- OSHA respiratory protection: https://www.osha.gov/respiratory-protection
- WHO mask guidance portal: https://www.who.int/

## 下一步

- 建立变量表：源头控制、过滤效率、适配、可得性、成本、接受度、工作场所要求、高风险主体保护和沟通误差。
- 与 `indoor-ventilation-filtration-outbreak-control-continuity/`、`occupational-exposure-industrial-hygiene/` 和 `school-workplace-outbreak-operations-continuity/` 建立接口。
