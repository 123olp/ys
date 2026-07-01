# Ubiquitin Proteasome Protein Turnover Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/ubiquitin-proteasome-protein-turnover-continuity` |
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


Ubiquitin Proteasome Protein Turnover Continuity 负责整理泛素-蛋白酶体系统、短寿命蛋白更新、错误蛋白降解、蛋白质量控制和蛋白稳态崩塌风险。

核心问题：

> 长期主体需要细胞不断识别、标记并降解错误或过期蛋白；泛素-蛋白酶体系统失灵会把局部蛋白错误转化为全局蛋白稳态压力。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 细胞功能依赖蛋白质持续更新和错误蛋白及时清除
  -> 泛素化、去泛素化、蛋白酶体活性和底物选择决定蛋白周转质量
  -> 蛋白周转失败会触发聚集、压力反应、神经退行、免疫扰动和细胞衰老
  -> 因此 UPS 是蛋白稳态从“折叠正确”走向“错误可清除”的核心执行层
```

## 关注对象

- ubiquitin-proteasome system、E3 ligases、deubiquitinases、proteasome activity、protein turnover、proteotoxic stress。
- 与 `proteostasis-autophagy/` 的关系：本域是蛋白稳态域的下层执行机制，重点在选择性标记和蛋白酶体降解。
- 与 `ribosome-translation-fidelity-proteome-integrity-continuity/` 的关系：翻译域关注错误蛋白生成，本域关注错误蛋白清除。

## Human Infra 模型链路

```text
UPS 观测 / 调节 T
  -> 改变泛素化、蛋白酶体活性、错误蛋白降解和蛋白周转 X
  -> 改变蛋白稳态压力与细胞质量控制状态 S
  -> 改变神经退行、肌肉衰退、免疫压力和细胞衰老风险
  -> 改变有效时间、恢复能力和长期组织功能
```

## 非目标

- 不提供蛋白酶体激活/抑制、药物、补剂、训练、禁食、检测解释或临床建议。
- 不把蛋白酶体活性或泛素化信号写成个体健康结论。
- 不提供细胞实验、动物实验、药筛或人体干预协议。

## Source Signals

- Hallmarks of Aging: https://pubmed.ncbi.nlm.nih.gov/36599349/
- Protein synthesis and quality control in aging: https://pmc.ncbi.nlm.nih.gov/articles/PMC6326689/
- Ubiquitin-proteasome system in healthy aging review: https://pubmed.ncbi.nlm.nih.gov/41937018/
