# Clinical Laboratory Diagnostic Quality

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/clinical-laboratory-diagnostic-quality` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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


临床检验、诊断质量与检测可靠性域研究：当个体诊断、筛查、治疗监测和风险分层依赖检验结果时，实验室质量、检测准确性、解释边界和诊断管理如何成为主体持续性的前提。

## 对象

- 临床实验室、检验项目、样本流程、质量控制、能力验证、CLIA/实验室监管和检验报告。
- 诊断准确性、假阳性/假阴性、参考区间、检测适用对象、临床效用和诊断延误。
- 诊断管理、重复检测、过度检测、检测短缺、实验室信息系统和检验结果互操作。
- 居家/即时检测、筛查项目、慢病监测、药物监测和风险预测模型中的检测输入。
- 检验质量对医疗决策、治疗连续性、早筛、误诊风险、成本和主体未来选择权的影响。

## Human Infra 价值

主体持续性模型依赖可靠观测。如果检验结果不准确、不可比、不可解释或无法进入临床流程，后续治疗、预防、预测和风险管理都会被污染。临床检验诊断质量域把“观测是否可信”从公共卫生实验室中拆出，作为个体医疗路径的基础设施。

```text
临床检测质量可验证
  -> 诊断、筛查和监测信号更可靠
  -> 医疗决策、风险分层和治疗调整更少误差
  -> 主体修复窗口、有效时间和未来选择权提高
```

## 边界

本域只整理公开实验室质量、检测可靠性、监管、诊断管理和临床效用资料。

不提供：

- 个体检验解读、诊断、治疗、筛查选择、复查建议或医学决策。
- 样本采集、运输、处理、检测操作、试剂配方、实验室 SOP 或质量控制操作步骤。
- 实验室认证规避、报告伪造、检测规避、样本替换、数据篡改或监管绕过方法。
- 商业实验室选择、检测购买、保险索赔、医疗纠纷或法律建议。

## 上游与下游

- 上游：`public-health-laboratory-diagnostic-capacity/`、`standards-metrology-quality-infrastructure/`、`medical-device-equipment-safety-maintenance/`、`patient-data-interoperability/`。
- 下游：`measurement-feedback/`、`healthcare-access-continuity/`、`clinical-trials-regulatory-science-translation/`、`cancer-control/`。

## 初始资料线索

- CMS Clinical Laboratory Improvement Amendments resources。
- CDC laboratory quality resources。
- FDA diagnostic tests and laboratory developed test resources。
- CLSI and laboratory medicine quality resources。
