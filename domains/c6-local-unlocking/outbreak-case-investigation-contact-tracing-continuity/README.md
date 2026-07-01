# Outbreak Case Investigation Contact Tracing Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/outbreak-case-investigation-contact-tracing-continuity` |
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


`outbreak-case-investigation-contact-tracing-continuity/` 研究暴发中的病例调查、接触者追踪、暴露通知、隐私保护和服务转介如何维持主体持续性。

> 核心问题：传染病暴发不是单个病例事件；如果暴露关系不能被及时、可信、隐私保护地转化为行动信号，学习、工作、照护和医疗系统会被连锁中断。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体长期行动依赖可持续的群体接触环境
  -> 暴发使日常接触网络变成传播网络
  -> 病例调查和接触追踪把不可见传播链转化为可通知、可转介、可隔离、可恢复的执行信号
```

## 关注对象

- 病例调查、接触者追踪、暴露通知、数字工具、公共卫生访谈、服务转介和隐私保护。
- 传播链识别、延迟、覆盖率、信任、语言可达、弱势群体保护和污名风险。
- 与 `immunization-public-health-surveillance/` 的关系：上位域关注监测系统；本域关注暴发后从病例到接触者的执行链。

## Human Infra 模型链路

```text
病例调查与接触追踪
  -> 改变暴露关系发现、通知、隔离支持和服务转介能力
  -> 改变传播链继续扩展的概率和被暴露主体的行动选择
  -> 降低暴发扩散、工作学校关闭、照护中断和医疗挤兑风险
  -> 增强健康寿命、有效时间、社会信任和主体持续性
```

## 非目标

- 不提供个体诊断、检测解释、隔离命令、法律建议或接触者名单识别。
- 不提供追踪规避、隐私侵害、定位、人肉搜索、污名化或暴露信息公开策略。
- 不把公共卫生调查工具写成监控、惩罚或社会控制方案。

## Source Signals

- CDC case investigation and contact tracing: https://www.cdc.gov/covid/php/contact-tracing/index.html
- CDC contact tracing resources: https://www.cdc.gov/contact-tracing/
- WHO contact tracing: https://www.who.int/news-room/questions-and-answers/item/contact-tracing
- WHO outbreak response and risk communication: https://www.who.int/emergencies

## 下一步

- 建立变量表：病例发现延迟、接触者覆盖率、通知时滞、隔离支持、隐私保护、污名风险和服务转介。
- 与 `isolation-quarantine-work-school-continuity/`、`community-testing-screening-access-continuity/` 和 `health-data-privacy-governance/` 建立接口。
