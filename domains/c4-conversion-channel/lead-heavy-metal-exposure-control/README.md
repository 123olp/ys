# Lead Heavy Metal Exposure Control

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/lead-heavy-metal-exposure-control` |
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


铅与重金属暴露控制域研究：当主体持续性依赖神经发育、认知保存、肾脏/血液/心血管稳定和儿童未来选择权时，铅、汞、镉、砷等重金属如何通过住房、饮水、土壤、工作、消费品和工业污染造成长期损耗。

## 对象

- 铅涂料、铅管、饮水、土壤、粉尘、工业排放、职业暴露、旧住房和儿童暴露风险。
- 汞、镉、砷等重金属的环境、食物链、工作场所和社区暴露。
- 神经发育、学习能力、行为、肾功能、血液系统、心血管风险和生殖健康影响。
- 暴露监测、公共卫生筛查、环境治理、住房修复、饮水系统、职业防护和产品监管。
- 环境不平等：旧住房、工业邻近社区、低收入家庭、儿童、孕产人群和高暴露职业。

## Human Infra 价值

重金属暴露不是个人选择问题，而是会穿透住房、水、土壤、工作和产品系统的慢性基础设施失败。它会提前损伤认知、身体和未来选择权，尤其对儿童主体持续性影响极大。

```text
铅与重金属暴露被识别和降低
  -> 神经发育、认知、肾血液系统和心血管负担下降
  -> 学习、工作、照护和长期健康资本更稳定
  -> 主体能力、有效时间和未来选择权提高
```

## 边界

本域只整理重金属暴露来源、公共卫生资料、环境治理、监测体系和证据边界。

不提供：

- 个体检测解读、诊断、治疗、螯合治疗、营养处方、妊娠/儿童医疗建议或急救建议。
- 房屋、饮水、土壤、职业场所或消费品的个案安全判断、采样方案、修复施工、设备购买或法律索赔建议。
- 危险材料拆除、旧漆处理、管道施工、工业清理、废物处置、监管规避或污染隐藏方法。
- 把单次检测、家庭试剂、地图、AI 输出或公开数据写成个体健康、房产、保险、就业或法律结论。

## 上游与下游

- 上游：`housing-built-environment-stability/`、`water-sanitation-hygiene-continuity/`、`occupational-exposure-industrial-hygiene/`、`chemical-safety-poison-control-toxicology/`。
- 下游：`learning-skill-acquisition/`、`neuro-continuity/`、`renal-hepatic-clearance/`、`blood-oxygen-hemostasis/`、`childcare-family-continuity/`。

## 初始资料线索

- CDC lead prevention resources。
- EPA lead resources。
- ATSDR toxic substances resources。
- NIEHS heavy metals resources。
