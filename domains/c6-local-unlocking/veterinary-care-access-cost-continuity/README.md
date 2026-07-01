# Veterinary Care Access Cost Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/veterinary-care-access-cost-continuity` |
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


Veterinary Care Access Cost Continuity 研究兽医照护、费用、地理可达、急诊能力和预防服务如何影响伴侣动物健康、家庭压力和主体持续性。

> 核心问题：宠物照护能否持续，不只取决于“有爱”，还取决于兽医服务、费用、交通、时间和信息是否可达。

## 研究对象

- 兽医服务可及性、预防照护、急诊兽医、费用负担、地理距离、预约容量和支付摩擦。
- 兽医照护断点如何影响家庭预算、情绪压力、灾害恢复、儿童关系和宠物福利。
- 公共卫生、动物福利、低收入家庭支持和反兽医建议边界。

## 先验链路

```text
伴侣动物连续性需要基本健康维护
  -> 健康维护依赖兽医服务、费用可承受、交通可达和信息理解
  -> 兽医照护断点会扩大动物痛苦、家庭压力、债务风险和遗弃风险
  -> 宠物健康压力反过来影响主体情绪、时间、经济和关系系统
  -> 因而兽医照护可及和费用连续性是宠物支持系统的基础域
```

## 关键变量

- 兽医 workforce、诊所距离、预约等待、急诊覆盖、费用负担、支付方式和低成本服务。
- 疫苗、寄生虫预防、慢病管理、疼痛、老年动物照护、安宁/临终边界和动物福利。
- 把兽医资料写成动物诊断、处方、治疗选择、急救或购买建议的风险。

## 证据入口

- AVMA pet owner and veterinary care resources。
- CDC Healthy Pets, Healthy People。
- FDA animal drugs and pet medication materials。
- USDA APHIS Animal Care materials。

## 非目标

- 本域不提供动物诊断、治疗、疫苗、药物、剂量、急救、手术、安乐死、繁育、购买或保险建议。
- 不判断某个动物是否需要就医、不替代兽医、不解释化验影像或处方。
- 不收集宠物病历、兽医账单、家庭收入、支付信息、地址、照片或个案动物伤情。

## 上下游

- 上游：`human-animal-bond-companion-care-continuity/`、`animal-health-zoonotic-interface-one-health/`、`financial-resilience-access/`。
- 下游：`pet-food-medication-supply-safety-continuity/`、`animal-welfare-cruelty-reporting-continuity/`、`pet-disaster-evacuation-sheltering-continuity/`。
