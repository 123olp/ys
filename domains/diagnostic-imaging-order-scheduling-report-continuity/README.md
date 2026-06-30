# Diagnostic Imaging Order Scheduling Report Continuity

## 定位

本域研究影像医嘱、prior authorization、预约、设备容量、造影/准备、报告生成、影像资料可携带和结果回传如何把影像能力转化为主体可用的诊断信号。

它不是影像解读、检查推荐、放射风险评估或个案加急入口。

## 先验问题

```text
影像能力何以成为诊断进展？
  -> 医嘱和授权必须能转化为预约
  -> 检查必须在合适窗口内完成
  -> 图像和报告必须回到患者和照护团队
  -> 关键发现必须触发下一步
  -> 否则昂贵设备不会自动减少诊断延误
```

## 研究对象

- X-ray、CT、MRI、ultrasound、mammography 和 nuclear medicine 的门诊执行链。
- 医嘱、预约、prior authorization、site of care、准备要求和造影资料。
- DICOM、PACS、radiology report、critical result、incidental finding 和 image sharing。
- 设备容量、等待时间、重复影像、报告延迟和跨机构可携带性。

## 关键变量

- order-to-schedule、schedule-to-scan、scan-to-report 和 report-viewed 时间。
- 授权失败率、重复影像率、影像资料共享成功率和 critical result 通知闭环率。
- 设备容量、地理距离、语言/无障碍、辐射/造影准备信息和费用透明。

## 证据入口

- Medicare diagnostic non-laboratory tests、CMS imaging quality 和 prior authorization 资料。
- ACR appropriateness / radiology reporting / DICOM / image sharing 相关资料。
- ONC interoperability、diagnostic safety 和 radiology follow-up 研究。

## 非目标

- 不解释影像、推荐检查、判断发现、评估辐射/造影风险或给出诊断治疗建议。
- 不代写 prior authorization、medical necessity、加急申请或影像报告摘要。
- 不收集影像文件、报告、病历、保险、授权号、预约、设备参数或个案健康资料。

## 上下游

- 上游：`specialist-referral-authorization-navigation-continuity/`、`appointment-availability-wait-time-continuity/`、`patient-data-interoperability/`。
- 下游：`rare-disease-diagnostic-odyssey-care-coordination/`、`cancer-control/`、`surgical-anesthesia-perioperative-safety/`。
