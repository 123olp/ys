# Eyeglasses Prescription Repair Replacement Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/eyeglasses-prescription-repair-replacement-continuity` |
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


`eyeglasses-prescription-repair-replacement-continuity` 研究眼镜、处方更新、镜片/镜架损坏、备用眼镜、费用、取件等待和远程/旅行断点如何影响阅读、工作、驾驶、导航、屏幕任务和公共服务使用。

> 核心问题：屈光矫正工具不是一次性购买物，而是视觉带宽的日常运行接口；当眼镜丢失、损坏、过期或无法替换时，低成本视觉能力会立刻变成任务摩擦。

## 关注对象

- 眼镜、镜片、镜架、处方有效性、备用眼镜、修理、替换、取件等待和费用摩擦。
- 阅读、学习、屏幕工作、驾驶、步行导航、药品标签、公共表格和灾害转移中的视觉任务断点。
- 儿童、低收入者、老年人、流动人口、灾后失物和长期照护场景中的眼镜可得性。
- 与屈光不正、低视力康复、视觉健康、身份文件、驾驶和学校/工作参与的接口。

## Human Infra 链路

```text
眼镜运行连续
  -> 主体保持低成本、低负担的基础视觉带宽
  -> 阅读、导航、屏幕任务、标签识别和安全判断更可靠
  -> 学习、工作、医疗理解、交通和公共服务使用摩擦下降
  -> 有效时间、行动能力和未来选择权增强
```

## 非目标

- 不提供验光、处方判断、镜片参数、品牌推荐、购买建议、驾驶资格判断或保险个案建议。
- 不替代眼科医生、验光师、NEI、MedlinePlus、学校视觉项目、低视力服务或交通监管要求。
- 不把眼镜运行问题合并进眼病诊疗；本域只处理矫正工具的可得、可用和断点。

## Source Signals

- MedlinePlus Refractive Errors: https://medlineplus.gov/refractiveerrors.html
- NEI Contact Lenses and Eyeglasses context: https://www.nei.nih.gov/eye-health-information/healthy-vision/contact-lenses

## 下一步

- 建立 `glasses state -> replacement/repair delay -> visual task -> execution loss` 变量表。
- 区分学生、驾驶、工作屏幕、老年照护、灾后失物和流动人口场景。
- 与 `refractive-error-glasses-contact-lens-continuity`、`low-vision-rehabilitation-assistive-technology-continuity` 和 `contact-lens-hygiene-eye-infection-continuity` 建立边界。
