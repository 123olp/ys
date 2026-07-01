# Acute Gastrointestinal Bleeding Endoscopy Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/acute-gastrointestinal-bleeding-endoscopy-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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


`acute-gastrointestinal-bleeding-endoscopy-continuity/` 研究急性上/下消化道出血、休克风险、输血/凝血支持、内镜可及、住院路径和复发预防如何影响主体持续性。

> 核心问题：消化道出血把隐蔽失血、贫血、休克、抗凝药物、内镜能力和血液系统连接成急性死亡边界。它需要被建模为“出血识别-稳定-内镜-恢复”的服务链。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖血容量和血红蛋白维持灌注与供氧
  -> 消化道出血可隐蔽或急性地造成贫血、休克和器官灌注失败
  -> 结果取决于识别、稳定、输血/凝血支持、内镜可及和复发预防
  -> 因此急性消化道出血是血液-消化-急诊交界的时间关键域
```

## 关注对象

- Upper GI bleeding, lower GI bleeding, hemodynamic instability, transfusion interface, anticoagulant context, endoscopy access, rebleeding, discharge follow-up。
- 与 `transfusion-blood-management-hemorrhage-continuity/` 的边界：该域关注血液供应和输血治理；本域关注消化道出血的诊断、内镜和复发链。
- 与 `surgical-anesthesia-perioperative-safety/` 的关系：严重出血可能进入操作/手术路径，但本域关注出血服务链。

## Human Infra 模型链路

```text
消化道出血服务链 T
  -> 改变识别延迟、血流动力学稳定、输血/凝血支持、内镜可及和复发预防变量 X
  -> 改变血容量、贫血、休克、住院、再出血和功能恢复状态 S
  -> 改变急性死亡、再住院、长期虚弱和有效时间损失 λ(t)
  -> 影响主体存活、恢复能力和未来选择权
```

## 非目标

- 不提供便血/呕血判断、急诊分诊、停药、抗凝处理、输血、内镜、饮食、药物或个体治疗建议。
- 不生成 GI bleeding 风险评分、内镜时机、药物路径、家庭处理或预后工具。
- 不收集个案症状、血压、血红蛋白、粪便/呕吐物图片、用药、内镜或病历资料。

## Source Signals

- American College of Gastroenterology guideline materials: https://gi.org/
- NIDDK digestive diseases materials: https://www.niddk.nih.gov/health-information/digestive-diseases
- AABB transfusion guideline materials: https://www.aabb.org/news-resources/resources/clinical-practice-guidelines

## 下一步

- 建立 GI Bleeding Card：recognition, instability, transfusion interface, endoscopy access, anticoagulant context, rebleeding。
- 与 `transfusion-blood-management-hemorrhage-continuity/`、`surgical-anesthesia-perioperative-safety/` 和 `acute-coronary-syndrome-reperfusion-continuity/` 建立抗凝/出血权衡接口。
