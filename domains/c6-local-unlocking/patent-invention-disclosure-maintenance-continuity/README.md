# Patent Invention Disclosure Maintenance Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/patent-invention-disclosure-maintenance-continuity` |
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


`patent-invention-disclosure-maintenance-continuity` 研究专利、发明披露、优先权、公开、转让、维护费、技术许可和 prior art 记录如何影响科研成果、工程发明、创业资产、技术转移和未来技术可及性。

> 核心问题：发明如果不能被记录、公开、归属、维护和转化，就会在论文、实验室、公司和供应链之间断裂，无法进入主体可用技术窗口。

## 关注对象

- Patent application、publication、grant、assignment、maintenance fees、priority、inventorship 和 public patent records。
- 发明披露、实验记录、资助来源、技术转移、许可、exclusive/non-exclusive arrangements 和公共资助成果。
- Prior art、patent landscape、freedom-to-operate 作为研究资料边界，而不是个案法律结论。
- Human Infra 中未来技术从发现、披露、保护、公开到可获得服务的制度路径。

## Human Infra 链路

```text
发明和技术原型出现
  -> 披露、专利、公开、转让和维护记录决定技术资产形态
  -> 技术能否被生产、许可、扩散和持续维护发生变化
  -> 未来技术窗口的可采用概率和可及性发生变化
  -> 主体获得新工具、治疗、材料和服务的机会改变
```

## 非目标

- 不提供专利申请、权利要求撰写、prior art 检索意见、侵权分析、FTO、维护费策略、许可谈判或法律意见。
- 不判断具体专利有效性、新颖性、创造性、侵权风险、商业价值或投资价值。
- 不提供规避专利、绕开许可、商业秘密获取、专利抢注、专利布局或诉讼策略。
- 不收集未公开发明披露、实验记录、资助合同、商业秘密、许可合同或法律通信。

## Source Signals

- USPTO Patents: https://www.uspto.gov/patents
- WIPO Patents: https://www.wipo.int/patents/en/
- Google Patents as discovery interface: https://patents.google.com/
- NIST Bayh-Dole resources: https://www.nist.gov/tpo/bayh-dole

## 下一步

- 建立 `invention -> disclosure -> patent/publication -> assignment/license -> access/maintenance -> continuity` 变量表。
- 区分专利作为公开记录、技术转移制度、市场排他权和主体可及性门槛。
- 与 `intellectual-property-technology-transfer-access`、`research-portfolio-prioritization-funding-governance`、`clinical-trials-regulatory-science-translation` 和 `technology-foresight-horizon-scanning` 建立边界。
