# Paratransit NEMT Access Continuity

`paratransit-nemt-access-continuity` 研究 ADA paratransit、非紧急医疗交通 NEMT、预约、资格、等待、上门接送、陪同、报销和取消如何影响残障、慢病、老年和低收入主体能否到达医疗与基本服务。

> 核心问题：医疗和公共服务存在不等于人能到达；如果 paratransit 和 NEMT 断裂，可治疗、可复诊、可康复的问题会被交通失败转成健康损失。

## 关注对象

- ADA paratransit、NEMT、上门接送、轮椅车辆、陪同、预约窗口、等待时间、取消、no-show、报销和资格更新。
- 透析、癌症治疗、康复、产检、精神健康、药房、福利办公室和社区服务场景。
- 与医疗可及、残障独立生活、公共交通、照护、医保/Medicaid 和行政负担的接口。

## Human Infra 链路

```text
辅助交通与医疗交通连续
  -> 行动受限主体能到达医疗、康复、药品和公共服务
  -> 预约失败、延误治疗、照护负担和急诊替代风险下降
  -> 医学可及性从名义覆盖转化为真实到达
  -> 健康寿命、功能恢复和主体自主性增强
```

## 非目标

- 不提供资格规避、虚假医疗交通申请、报销欺诈、调度攻击、个案申诉策略或医疗建议。
- 不替代 Medicaid、FTA、交通运营商、医疗机构、照护协调员、保险、法律或本地服务渠道。
- 不收集病历、残障证明、医保号、预约记录、出行轨迹、接送地址或个人身份资料。

## Source Signals

- FTA ADA Paratransit: https://www.transit.dot.gov/regulations-and-guidance/civil-rights-ada/ada-regulations
- FTA ADA Circular: https://www.transit.dot.gov/regulations-and-guidance/fta-circulars/americans-disabilities-act-guidance
- Medicaid NEMT: https://www.medicaid.gov/medicaid/benefits/non-emergency-medical-transportation/index.html
- ADA.gov Transportation: https://www.ada.gov/topics/transportation/

## 下一步

- 建立 `eligibility -> trip request -> pickup/dropoff -> service reliability -> care outcome` 变量表。
- 区分 ADA paratransit、Medicaid NEMT、老年服务交通、社区志愿交通和医疗机构交通协调。
- 与 `healthcare-access-continuity`、`disability-services-independent-living`、`public-transit-service-operations-continuity` 和 `administrative-burden-procedural-friction` 建立边界。
