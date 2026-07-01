# 0021 Add Seventeenth Wave Geospatial Weather Building Manufacturing Procurement One Health Domains

Date: 2026-06-30

## Status

Accepted

## Context

Research Domain Atlas 已经把 Human Infra 从单一长寿项目扩展为主体持续性先验条件图谱。第十六波覆盖教育、科研、标准、网络安全、算力和临床转化后，仍有一组外部基础设施条件没有独立承载：

- 主体和资源能否被定位、导航、配送和救援。
- 天气与气候风险能否被观测、预报并转化为提前行动窗口。
- 建筑和消防生命安全能否防止居住、照护、学习、工作空间成为致命风险源。
- 关键工具、设备、备件和基础设施损坏后能否被制造、维修和替换。
- 公共预算、政策和需求能否通过采购与合同转化为真实交付。
- 动物健康、人兽共患风险和 One Health 界面是否能形成上游公共卫生屏障。

这些对象符合 Research Domain Atlas 的五项域判定条件：独立机制、独立证据体系、独立失败模式、独立伦理边界和独立维护价值。

## Decision

新增第十七波 6 个正式研究域：

- `domains/c4-conversion-channel/geospatial-navigation-location-infrastructure/`
- `domains/c5-ecological-substrate/weather-climate-observation-forecasting/`
- `domains/c6-local-unlocking/building-fire-life-safety-codes/`
- `domains/c6-local-unlocking/manufacturing-repair-capacity/`
- `domains/c4-conversion-channel/public-procurement-contracting-capacity/`
- `domains/c6-local-unlocking/animal-health-zoonotic-interface-one-health/`

每个域只创建 `README.md` 和 `AGENTS.md`，用于定义对象、先验位置、链路、非目标、Source Signals 和维护边界；不创建空数据目录、脚本目录或产品服务目录。

## Consequences

- `docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md`、`docs/reference/domain-map.md` 和根 README 需要同步索引这些域。
- 伦理边界需要新增空间定位、天气气候、建筑消防、制造维修、公共采购和 One Health 的禁止用途。
- 本轮不提供实时地图、天气预报、建筑施工、消防操作、制造维修步骤、采购策略、动物诊疗或疫情操作建议。
- 后续资料进入这些域时，必须先形成 Source Card，不把 AI 总结或营销资料当作事实源。

## Alternatives Considered

- 继续放在既有宽域中：会让交通、应急、住房、供应链、公共服务和公共卫生域承担过多机制，降低边界清晰度。
- 直接建立数据或工具目录：当前只有域骨架和资料索引需求，不存在稳定数据管线或工具契约。
- 等待更多文献后再建域：这些域已经有官方框架和明确失败模式，先建边界文档能减少后续资料散落。

## Verification

- 每个新增域必须有 `README.md` 和 `AGENTS.md`。
- `tools/check_repository.py` 必须纳入新增文件和目录。
- `make check` 必须通过。
