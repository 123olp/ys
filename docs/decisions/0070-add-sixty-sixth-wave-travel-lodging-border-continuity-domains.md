# ADR 0070: Add Sixty-Sixth-Wave Travel Lodging Border Continuity Domains

## Status

Accepted.

## Context

Human Infra 已经覆盖日常交通、个人移动执行、护照旅行证件、移民身份、公共住宿无障碍和灾害安置等域。但主体离开本地生活圈之后，还存在一组独立的短期移动执行链：行程预订、航空中断、安检身份核验、行李物品、临时住宿、旅行警示/领事协助、旅行健康准备和海关边境申报。

这些对象不能只归入 `transportation-access-mobility`、`passport-travel-document-mobility-continuity` 或 `immigration-status-residency-work-authorization-continuity`。日常交通关注本地可达性；护照域关注跨境移动资格；移民域关注居留和工作授权。本波关注的是主体离家后如何把交通、住所、证件、物品、健康、领事求助和边境规则组织成一条可恢复的临时行动链。

## Decision

新增第 66 波 8 个旅行、临时住宿与跨境移动连续性域：

- `long-distance-travel-booking-itinerary-continuity`
- `air-passenger-rights-disruption-refund-continuity`
- `aviation-security-screening-identity-continuity`
- `baggage-personal-property-travel-continuity`
- `lodging-temporary-accommodation-access-continuity`
- `travel-advisory-consular-assistance-continuity`
- `travel-health-preparedness-continuity`
- `customs-border-entry-declaration-continuity`

## Consequences

- Human Infra 能把离家后的临时操作系统拆成可审查域：计划、交通中断、安全筛查、物品、住宿、海外求助、健康暴露和边境通过。
- 这些域只做公开资料整理、机制建模、证据边界和禁止用途声明；不提供路线推荐、票务套利、安检规避、住宿选择、旅行安全、医疗、签证、移民、海关申报、法律、保险或个案策略建议。
- 后续若新增 U.S. DOT、TSA、State Department、CDC、CBP、FTC、ADA.gov、FEMA 或旅行消费者保护资料，应优先进入对应细分域；只有基础跨境移动资格才回到 `passport-travel-document-mobility-continuity`，只有居留/工作授权才回到 `immigration-status-residency-work-authorization-continuity`。
