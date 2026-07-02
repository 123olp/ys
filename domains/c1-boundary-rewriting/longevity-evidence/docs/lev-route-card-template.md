# LEV Route Card Template

Last reviewed: 2026-07-02

本文是长寿逃逸速度路线卡模板。后续任何新路线进入 `lev-mainstream-routes.md`、`lev_route_cards.tsv` 或 Web 图表前，都必须先填写这张卡。它的目的不是增加文档仪式，而是强制把“路线叙事”压成可审查的变量、概率门、正负链路和证据边界。

## 最小字段

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `route_id` | 是 | 稳定编号，例如 `R10`。 |
| `route_name` | 是 | 中文路线名，避免营销化命名。 |
| `direct_route_type` | 是 | `direct-biomedical`、`enabling-technology`、`measurement-feedback`、`translation-infrastructure`、`translation-bridge` 之一。 |
| `primary_tags` | 是 | 机制、证据阶段、转化路径、治理边界标签。 |
| `direct_effect` | 是 | 该路线直接改变什么，不允许写“延寿”。 |
| `first_order_effect` | 是 | 直接变量如何改变状态或观测。 |
| `second_order_effect` | 是 | 如何改变采用、理解、支付、恢复、扩散或校准概率。 |
| `multi_order_effect` | 是 | 如何进入技术窗口、资源复利或加速回报飞轮。 |
| `probability_gates` | 是 | 至少填写一个概率门。 |
| `positive_chain` | 是 | 正向链路。 |
| `negative_chain` | 是 | 负向链路。 |
| `bottleneck_domains` | 是 | 已有研究域路径，必须能在 `classification.tsv` 中找到。 |
| `source_refs` | 是 | URL 或 Source Card id。 |
| `boundary` | 是 | 明确不能推出什么。 |

## 概率门

路线卡必须从下列概率门中选择，不够时先补模型文档，不要发明临时字段。

```text
P_notice      主体或系统能否发现有效技术 / 风险信号
P_understand  主体能否理解证据、机制、风险和边界
P_access      主体能否接入服务、工具、试验、资金或数据
P_adopt       主体能否安全采用并执行路线
P_recover     主体能否从疾病、损伤、失败或资源断裂中恢复
P_avoid       主体能否避开伪疗法、过度外推、尾部风险和机会成本
P_diffuse     有效技术能否从早期优势群体扩散到普通主体
P_persist     主体能否长期坚持有效策略，并在失败时修正
P_calibrate   主体能否校准证据、指标和 AI 输出
P_equity      技术路线是否避免收益过度集中
```

## 路线卡骨架

```text
Route:
  id:
  name:
  type:
  tags:

Claim boundary:
  direct claim:
  supported claim:
  forbidden inference:

Effect chain:
  direct effect:
  first-order effect:
  second-order effect:
  multi-order effect:
  positive chain:
  negative chain:

Gates:
  probability gates:
  strongest gate:
  weakest gate:
  abort gate:

Evidence:
  source refs:
  evidence type:
  maturity:
  next check:

Domain routing:
  bottleneck domains:
  upstream domains:
  downstream domains:
```

## 示例

```text
Route:
  id: R7
  name: 生物年龄与功能指标路线
  type: measurement-feedback
  tags: mechanism:measurement-feedback; evidence:biomarker; evidence:human-function

Claim boundary:
  direct claim: 指标缩短反馈周期。
  supported claim: 指标可用于候选干预筛选和风险建模入口。
  forbidden inference: 单个指标不能输出个体死亡日期或替代真实寿命终点。

Effect chain:
  direct effect: 状态观测更快。
  first-order effect: 干预响应和风险估计更快。
  second-order effect: 试验筛选和主体决策反馈提高。
  multi-order effect: 与真实终点持续校准后，成为 LEV 模型的反馈基础设施。
  positive chain: biomarker -> 反馈周期缩短 -> 试验筛选效率提高。
  negative chain: biomarker -> Goodhart 化 -> 伪优化和过度检测。

Gates:
  probability gates: P_calibrate; P_access; P_adopt
  strongest gate: P_calibrate
  weakest gate: P_calibrate
  abort gate: 指标被当作真实寿命终点。

Evidence:
  source refs: DunedinPACE; GrimAge; PROSPR
  evidence type: biomarker / cohort association / program design
  maturity: mixed
  next check: 与真实功能、疾病和死亡风险终点对齐。

Domain routing:
  bottleneck domains: biological-age-clocks-biomarker-validation/; survival-analysis-healthspan-risk-modeling/
  upstream domains: longitudinal-cohort-retention-followup-infrastructure/
  downstream domains: clinical-trials-regulatory-science-translation/
```

## 禁止写法

- 禁止把“进入 Phase 1”“获得资助”“指标改善”“动物寿命信号”“AI 生成候选”写成延寿已成立。
- 禁止只写正向链路，不写负向链路。
- 禁止只填路线名和来源，不填概率门。
- 禁止新增不能映射到现有研究域的路线卡；若确实缺域，先提交存在性论证。
