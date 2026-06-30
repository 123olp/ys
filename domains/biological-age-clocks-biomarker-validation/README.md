# Biological Age Clocks Biomarker Validation

`biological-age-clocks-biomarker-validation/` 研究表观遗传年龄钟、蛋白组/代谢组年龄、功能年龄、综合生物标志物和验证框架如何进入寿命与健康寿命模型。

> 核心问题：年龄钟不是寿命本身。它们的价值在于能否可靠反映风险、功能、干预反应和未来状态，而不是生成一个看起来精确的“生物年龄数字”。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要知道自身状态是否正在改善或恶化
  -> 寿命终点反馈极慢，必须寻找可验证中间指标
  -> 生物年龄钟和 biomarker 可能压缩反馈时间
  -> 若指标与真实终点错配，会制造伪优化和错误干预
  -> 因此年龄钟验证是定量模型的观测层研究域
```

## 关注对象

- DNA methylation clocks、GrimAge、PhenoAge、DunedinPACE、蛋白组年龄、代谢组年龄和复合 biomarker。
- 预测死亡率、疾病发生、功能衰退、健康寿命、恢复能力和干预反应的证据。
- 量表漂移、组织差异、人群偏差、可重复性、批次效应、替代终点错配和个体解释风险。
- 与 `measurement-feedback/` 的边界：测量反馈域关注通用测量控制；本域关注生物年龄与衰老 biomarker。
- 与 `longevity-evidence/` 的边界：长寿证据域关注干预证据；本域关注指标是否能作为证据接口。

## Human Infra 模型链路

```text
生物年龄 / biomarker B
  -> 观测身体损伤、炎症、代谢、表观遗传、功能和恢复状态 X
  -> 改变模型对主体状态 S 的估计
  -> 改变风险函数 λ(t) 的预测和干预选择
  -> 影响健康寿命管理、反馈速度和未来选择权
```

## 非目标

- 不输出个体死亡日期、寿命承诺、医学诊断、治疗建议或单次检测解释。
- 不把 biomarker 改善等同于真实寿命延长。
- 不把商业检测、营销年龄、单一时钟或未验证指标写成决策真相。
- 不提供检测购买、样本采集、实验操作、保险、就业或歧视性使用建议。

## Source Signals

- Horvath DNA methylation age: https://genomebiology.biomedcentral.com/articles/10.1186/gb-2013-14-10-r115
- GrimAge and lifespan / healthspan prediction: https://pmc.ncbi.nlm.nih.gov/articles/PMC6366976/
- DunedinPACE: https://elifesciences.org/articles/73420
- Hallmarks of aging: https://pubmed.ncbi.nlm.nih.gov/36599349/
- NIA biology of aging: https://www.nia.nih.gov/research/dab/biology-aging

## 下一步

1. 建立年龄钟证据分层：相关性、预测性、干预响应、真实终点和个体可解释性。
2. 与 `measurement-feedback/`、`multiomics-personal-baseline-systems-biology/`、`longevity-evidence/` 建立变量接口。
3. 增加反误用清单：替代终点、个体解释、保险就业和商业营销边界。
