# Rabies Exposure Bite PEP Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/rabies-exposure-bite-pep-continuity` |
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


`rabies-exposure-bite-pep-continuity` 研究疑似狂犬病暴露、动物咬伤、暴露后预防路径和公共卫生/医疗接口如何影响主体持续性。

> 核心问题：狂犬病暴露是低频但高后果风险；一旦出现动物咬伤或可疑接触，主体需要极短时间内完成清洗、报告、风险评估、医疗连接和疫苗/免疫球蛋白路径。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须能处理低概率高致死暴露
  -> 可疑动物接触会触发时间敏感的医疗和公共卫生链路
  -> 暴露识别、伤口处理、动物信息、医疗可及和 PEP 递送构成生存前提
  -> 若链路断裂，主体持续性可能被一次可预防事件终止
```

## 关注对象

- 犬、猫、蝙蝠、野生动物和未知动物接触后的狂犬病暴露风险。
- 伤口、咬伤、抓伤、黏膜暴露、动物观察/检测、公共卫生咨询和暴露后预防。
- 医疗可及、费用、疫苗/免疫球蛋白供应、旅行场景和延误风险。

## Human Infra 链路

```text
狂犬病暴露链路可识别、可连接、可完成
  -> 高致死低频事件被时间敏感地处理
  -> 恐慌、延误、费用和服务断点下降
  -> 主体持续性免受一次可预防暴露的不可逆破坏
```

## 非目标

- 不提供个体暴露判断、伤口处理步骤、PEP 决策、疫苗安排、动物处置或野生动物处理建议。
- 不替代 CDC、地方公共卫生、急诊、医疗机构、兽医、动物控制或旅行医学服务。
- 不提供规避报告、捕捉动物、处理蝙蝠、延迟就医或自我治疗方案。

## Source Signals

- CDC Rabies: https://www.cdc.gov/rabies/
- CDC Rabies Postexposure Prophylaxis: https://www.cdc.gov/rabies/medical_care/index.html
- CDC Healthy Pets: https://www.cdc.gov/healthy-pets/

## 下一步

- 建立 `animal contact -> exposure suspicion -> public health triage -> PEP access -> continuity outcome` 变量表。
- 区分美国本土、旅行、蝙蝠、犬猫、野生动物、儿童和费用/供应链场景。
