# Mosquito Bite Arbovirus Prevention Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/mosquito-bite-arbovirus-prevention-continuity` |
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


`mosquito-bite-arbovirus-prevention-continuity` 研究蚊虫叮咬、蚊媒病毒、居住/户外暴露和社区防蚊行动如何影响主体持续性。

> 核心问题：蚊媒风险不是“户外不舒服”的小问题；当登革热、西尼罗病毒、寨卡、基孔肯雅热等风险进入居住、旅行、工作和孕产场景时，主体行动窗口会被环境暴露重新约束。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须在可居住、可移动、可工作和可休息的环境中持续行动
  -> 蚊虫叮咬和蚊媒病毒会把普通空间转化为感染暴露空间
  -> 防蚊、积水治理、屏障、警报和公共卫生控制构成行动前提
  -> 若该前提失败，旅行、户外劳动、睡眠、孕产安全和社区活动都会被压缩
```

## 关注对象

- 蚊虫叮咬暴露、蚊媒病毒、户外活动、旅行、孕产风险、居住环境和积水治理。
- 驱避、防护衣物、门窗屏障、社区灭蚊、监测、风险沟通和公共卫生行动。
- 与 `vector-borne-disease-environmental-control/` 的边界：上位域关注病媒传播环境控制；本域关注蚊虫叮咬到主体行动约束的执行层。

## Human Infra 链路

```text
蚊媒暴露被识别和控制
  -> 叮咬、感染和恐惧性行动回避下降
  -> 居住、睡眠、户外工作、旅行和孕产计划更稳定
  -> 有效时间、健康寿命和行动选择权被保护
```

## 非目标

- 不提供个体诊断、治疗、旅行医学、孕产医学、驱虫产品推荐、农药配方或现场灭蚊操作。
- 不替代 CDC、EPA、地方公共卫生、病媒控制、旅行医学或医疗服务。
- 不把蚊媒地图、病例、气候数据或 AI 输出写成个体感染概率、旅行安全结论或资产价值判断。

## Source Signals

- CDC Mosquitoes: https://www.cdc.gov/mosquitoes/
- CDC Prevent Mosquito Bites: https://www.cdc.gov/mosquitoes/prevention/index.html
- EPA Mosquito Control: https://www.epa.gov/mosquitocontrol

## 下一步

- 建立 `mosquito exposure -> bite prevention -> arbovirus risk -> activity constraint -> continuity cost` 变量表。
- 区分居住、旅行、户外劳动、学校活动、孕产风险和灾后积水场景。
