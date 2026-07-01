# Public Service Design Accessibility

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/public-service-design-accessibility` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 主要提供主体展开未来所需的基础环境、资源、治理或基础设施。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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


`public-service-design-accessibility/` 研究公共数字服务、表单、流程、客户体验、无障碍和任务完成路径如何影响主体获得权利、资源和恢复支持。

> 核心问题：公共服务存在不等于主体能完成它；如果入口、表单、身份、语言、移动端、人工帮助和反馈路径失败，名义权利会变成实际排除。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须持续接入公共服务、权利、福利、医疗、身份和灾后支持
  -> 这些服务越来越通过网页、表单、账号、通知和客服流程实现
  -> 糟糕的服务设计会制造行政负担、申请放弃、延误和制度排除
  -> 因此公共服务设计与可达性是主体持续性的制度接口域
```

## 关注对象

- 公共服务设计、USWDS、Digital.gov、客户体验、表单设计、任务完成率、无障碍和反馈路径。
- 数字入口与人工帮助、移动端、语言可达、身份认证、隐私和申诉之间的关系。
- 行政负担如何消耗有效时间、注意力、恢复能力和未来选择权。
- 与 `digital-inclusion-connectivity/` 的边界：本域关注服务本身如何被设计；数字包容关注连接、设备、技能和可负担性。

## Human Infra 模型链路

```text
公共服务设计 T
  -> 改变可理解性、表单负担、无障碍、人工帮助、状态反馈和申诉变量 X
  -> 改变主体完成公共任务和获得服务的状态 S
  -> 改变申请放弃、服务延误、行政时间损耗、权利断线和恢复失败风险 λ(t)
  -> 影响有效时间、资源可及、制度信任和未来选择权
```

## 非目标

- 不提供个体申请、资格判断、材料准备、申诉策略、法律意见或服务绕过方法。
- 不支持 dark patterns、强制数字化、无人工替代、监控式体验分析或服务排除。
- 不把界面效率置于同意、隐私、无障碍、语言可达和主体尊严之上。

## Source Signals

- Digital.gov: https://digital.gov/
- U.S. Web Design System: https://designsystem.digital.gov/
- Performance.gov Customer Experience: https://www.performance.gov/cx/
- Section508.gov: https://www.section508.gov/
- PlainLanguage.gov: https://www.plainlanguage.gov/

## 下一步

- 建立公共服务设计变量表：任务完成、表单负担、可理解性、无障碍、移动端、人工帮助、状态反馈和申诉路径。
- 与 `social-protection-benefits-delivery/`、`language-access-plain-communication/`、`digital-identity-security/` 和 `digital-inclusion-connectivity/` 建立接口。
