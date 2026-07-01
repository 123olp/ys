# Radon Asbestos Indoor Hazard Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/radon-asbestos-indoor-hazard-continuity` |
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


氡、石棉与室内长期危害连续性域研究：当主体持续性依赖可居住空间和长期肺部风险控制时，氡、石棉及其他建筑遗留危害如何通过住房、学校、工作场所和公共建筑制造慢性风险。

## 对象

- 氡进入住宅、学校、地下空间和工作场所后的长期暴露风险。
- 石棉建筑材料、老旧建筑、维护翻新、拆除、学校/公共建筑和职业暴露。
- 肺癌、间皮瘤、慢性呼吸负担、暴露不平等和长期潜伏期风险。
- 建筑年代、通风、地质、材料、监管、检测、缓解、维护记录和公共沟通。
- 租户、房主、学生、工人、维护人员和低收入家庭的风险差异。

## Human Infra 价值

主体持续性需要一个不会持续积累不可见肺部风险的空间。氡和石棉说明，居住空间本身可能成为长期损耗机器；只有检测、治理、监管和维护记录形成闭环，住房才是真正的基础设施。

```text
室内长期危害被识别、记录和治理
  -> 慢性肺部与癌症相关风险暴露下降
  -> 住房、学校和工作场所的长期安全性提高
  -> 健康寿命、有效时间和居住选择权提高
```

## 边界

本域只整理氡、石棉、室内长期危害、建筑资料、监管和公共治理边界。

不提供：

- 个体检测解读、医疗诊断、癌症风险判断、筛查建议、治疗建议或法律赔偿建议。
- 氡检测设备购买、缓解系统设计、石棉识别、采样、拆除、封装、施工、清理、废弃物处置或承包商选择建议。
- 房屋购买、租赁、改造、学校/单位合规、保险、诉讼、投诉策略或资产价值判断。
- 危险材料操作、监管规避、虚假检测、记录篡改或暴露隐瞒方法。

## 上游与下游

- 上游：`housing-built-environment-stability/`、`building-fire-life-safety-codes/`、`air-quality-ventilation-exposure-control/`、`occupational-exposure-industrial-hygiene/`。
- 下游：`respiratory-oxygenation/`、`cancer-control/`、`healthcare-access-continuity/`、`insurance-risk-transfer/`。

## 初始资料线索

- EPA radon resources。
- EPA asbestos resources。
- CDC/NIOSH occupational exposure materials where applicable。
- State or local public-health building hazard resources where applicable。
