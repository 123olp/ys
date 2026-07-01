# Municipal 311 Service Request Continuity

`municipal-311-service-request-continuity/` 研究 311、非紧急服务请求、地方公共工程派单、状态回传和服务请求数据如何影响主体在邻里环境中的问题报告、跟踪和恢复能力。

## 先验链路

```text
主体要在社区中持续行动
  -> 邻里问题必须能从个人观察转成公共机构可处理的请求
  -> 请求需要渠道、分类、位置、编号、责任部门和状态回传
  -> 311 / Open311 / 地方服务请求系统把问题转成可派单的公共服务对象
  -> 请求失败会让路灯、坑洞、垃圾、积水、标志、噪声和通行障碍长期滞留
  -> 日常出行、照护、工作、学习、公共安全和邻里信任被持续消耗
```

## 研究对象

- 311、non-emergency service request、Open311 / GeoReport、service category、request status、department routing、SLA、closure code、公开服务请求数据和回传机制。

## 不能做

- 不提供紧急报警替代、执法规避、骚扰举报、虚假投诉、个人跟踪、位置监控、投诉代写、法律策略、政治动员或个案市政服务申诉建议。
- 不收集、复制或要求家庭地址、精确位置、照片、车牌、邻居身份、联系方式、执法记录、账号、投诉记录或其他敏感资料。

## Source Signals

- Open311 GeoReport v2: https://wiki.open311.org/GeoReport_v2/
- NYC Open Data 311 service requests: https://opendata.cityofnewyork.us/
- Code for America 311 and civic service context: https://www.codeforamerica.org/
- USA.gov local governments: https://www.usa.gov/local-governments

## 上下游关系

- 上游：`public-service-design-accessibility/`、`civic-data-open-government-transparency/`、`public-works-civil-infrastructure-asset-management/`。
- 下游：`streetlight-outage-nighttime-visibility-continuity/`、`sidewalk-curb-ramp-maintenance-access-continuity/`、`storm-drain-catch-basin-local-flooding-continuity/`。
