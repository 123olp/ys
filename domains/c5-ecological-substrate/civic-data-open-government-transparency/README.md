# Civic Data Open Government Transparency

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/civic-data-open-government-transparency` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 主要提供主体展开未来所需的基础环境、资源、治理或基础设施。 |
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


`civic-data-open-government-transparency/` 研究开放数据、政府透明、公共记录、绩效数据、FOIA、数据目录和可复用公共信息如何支撑问责、服务改进和公共决策参与。

> 核心问题：公共系统不可见时，主体无法判断资源如何分配、服务是否有效、风险是否被治理；开放数据和透明机制把制度运行变成可审查、可复用、可反馈的公共基础设施。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖公共资源、政策、服务和风险治理
  -> 这些系统必须可被观察、比较、审查和反馈
  -> 开放数据、公共记录和透明机制降低制度不可见性
  -> 缺乏透明会放大腐败、低效、排除、服务失败和信任崩塌
  -> 因此公民数据与开放政府是主体持续性的治理可观测域
```

## 关注对象

- 开放政府数据、Data.gov、元数据、公共记录、FOIA、绩效仪表板、服务数据和公共参与数据。
- 透明、问责、可复用、机器可读、隐私保护、数据质量、更新频率和访问门槛。
- 公民社会、研究者、记者、社区组织和公共部门如何用数据发现缺口、改进服务和监督风险。
- 与 `civic-participation-election-access/` 的边界：本域关注公共数据和透明度；公民参与域关注投票和公共参与入口。
- 与 `health-data-privacy-governance/` 的边界：本域处理公共开放数据；健康数据隐私域处理敏感个体健康数据治理。

## Human Infra 模型链路

```text
开放政府与公民数据 T
  -> 改变数据可得性、透明度、元数据质量、公共记录、绩效反馈和隐私保护变量 X
  -> 改变主体、社区和研究者审查制度、发现缺口和推动改进的状态 S
  -> 改变服务失败不可见、资源错配、腐败、歧视、信任崩塌和风险治理失灵风险 λ(t)
  -> 影响公共资源质量、制度反馈、权利保护和未来选择权
```

## 非目标

- 不提供人肉搜索、隐私攻击、规避访问控制、监控目标定位、商业抓取滥用或执法情报分析。
- 不把开放数据写成可以发布敏感个体数据、健康数据、儿童数据、位置数据或可再识别数据的理由。
- 不提供 FOIA 个案法律建议、诉讼策略、政府合规判断或政治操控方案。

## Source Signals

- Data.gov: https://data.gov/
- Resources.data.gov: https://resources.data.gov/
- FOIA.gov: https://www.foia.gov/
- U.S. Open Government: https://open.usa.gov/
- Federal Data Strategy: https://strategy.data.gov/

## 下一步

- 建立开放数据变量表：可得性、机器可读、元数据、更新、许可、隐私、再识别风险、绩效反馈和公共参与接口。
- 与 `governance-rights/`、`public-service-design-accessibility/`、`civic-participation-election-access/` 和 `health-data-privacy-governance/` 建立接口。
