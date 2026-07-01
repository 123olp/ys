# Venomous Bites Stings Envenomation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/venomous-bites-stings-envenomation-continuity` |
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


`venomous-bites-stings-envenomation-continuity` 研究蛇、蜘蛛、蝎、蜂等咬蜇伤和毒液暴露如何影响户外劳动、旅行、儿童活动和急救连接。

> 核心问题：有毒咬蜇伤是短窗口高后果事件；真正的持续性问题是风险识别、避免接触、及时医疗连接和毒物中心/急诊网络是否可用。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要进入户外、农林、仓储、旅行和灾后清理环境
  -> 有毒动物接触会在短时间内造成疼痛、过敏、组织损伤或生命威胁
  -> 暴露避免、识别、医疗连接和毒物中心路径构成行动前提
  -> 若该前提失败，局部户外风险可能转化为功能损失或死亡边界
```

## 关注对象

- 毒蛇、蜘蛛、蝎、蜂/黄蜂、火蚁、水母等咬蜇伤风险。
- 户外劳动、农林、旅行、儿童活动、灾后清理、过敏反应和急诊连接。
- 毒物中心、抗毒素可及、误处置、延误和地区差异。

## Human Infra 链路

```text
咬蜇伤风险被避免、识别并连接医疗
  -> 延误、误处置、过敏和组织损伤风险下降
  -> 户外劳动、旅行、儿童活动和灾后清理更可控
  -> 身体完整性、有效时间和行动自由被保护
```

## 非目标

- 不提供咬蜇伤急救步骤、抗毒素建议、动物识别诊断、捕捉处理、个体风险判断或旅行许可。
- 不替代毒物中心、急诊、EMS、医疗服务、职业安全、野生动物或地方公共卫生机构。
- 不鼓励接近、捕捉、杀伤或保存危险动物。

## Source Signals

- Poison Help: https://www.poisonhelp.org/
- CDC/NIOSH Venomous Spiders: https://www.cdc.gov/niosh/topics/spiders/
- CDC/NIOSH Venomous Snakes: https://www.cdc.gov/niosh/topics/snakes/

## 下一步

- 建立 `habitat/task -> animal contact -> bite/sting -> poison/medical connection -> function outcome` 变量表。
- 区分儿童、户外工作者、旅行者、灾后清理、过敏体质和偏远地区场景。
