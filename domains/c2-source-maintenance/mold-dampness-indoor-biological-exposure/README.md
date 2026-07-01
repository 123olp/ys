# Mold Dampness Indoor Biological Exposure

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/mold-dampness-indoor-biological-exposure` |
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


霉菌、潮湿与室内生物暴露域研究：当主体持续性依赖稳定住房、呼吸恢复、免疫负担控制和可学习工作空间时，建筑潮湿、霉菌、室内过敏原和生物气溶胶如何成为慢性环境压力。

## 对象

- 建筑潮湿、漏水、霉菌、室内过敏原、尘螨、潮湿材料和通风不足。
- 呼吸症状、哮喘负担、过敏、感染风险、睡眠破坏、学习/工作环境质量和心理压力。
- 住房质量、维修责任、学校/托育/养老机构、灾后水损、低收入住房和租户暴露。
- 观察、记录、公共卫生沟通、住房治理、建筑维护和风险分层。
- 霉菌问题与空气质量、能源贫困、洪水恢复、建筑材料和社会不平等的交叉。

## Human Infra 价值

潮湿和霉菌把住房从保护层变成持续暴露源。它们通过呼吸、免疫、睡眠、注意力和家庭压力影响主体的有效时间。本域把室内生物暴露纳入住房和恢复基础设施，而不是把它缩小成清洁习惯问题。

```text
潮湿、霉菌和室内生物暴露被治理
  -> 呼吸、过敏、睡眠和心理压力负担下降
  -> 居住、学习、照护和恢复空间更稳定
  -> 有效时间、健康寿命和未来选择权提高
```

## 边界

本域只整理霉菌、潮湿、室内过敏原、住房质量、公共健康和建筑维护治理资料。

不提供：

- 个体医疗诊断、哮喘/过敏治疗、用药、检测解读、感染判断或急救建议。
- 霉菌采样、清理、消毒剂配方、除湿设备购买、施工、维修、租房纠纷、保险、赔偿或法律建议。
- 灾后进入水损建筑、危险环境清理、污染材料处理、隐藏问题、规避监管或虚假检测方法。
- 把霉菌照片、气味、传感器、家庭试剂或 AI 输出写成个人健康、住房安全或法律结论。

## 上游与下游

- 上游：`housing-built-environment-stability/`、`water-resources-hydrology-flood-drought-management/`、`air-quality-ventilation-exposure-control/`、`disaster-recovery-relief-continuity/`。
- 下游：`respiratory-oxygenation/`、`immune-maintenance/`、`sleep-circadian-recovery/`、`mental-health-affective-stability/`、`healthcare-access-continuity/`。

## 初始资料线索

- CDC mold health resources。
- EPA mold resources。
- WHO indoor air quality dampness and mould guidance。
- Housing and public-health resources on dampness, leaks and indoor biological exposure。
