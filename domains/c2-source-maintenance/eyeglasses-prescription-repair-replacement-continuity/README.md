# Eyeglasses Prescription Repair Replacement Continuity

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
