# Execution Checklist

[x] TP-04 | P0 | 三件套骨架与索引：目录结构、相互引用约定、与项目资产衔接 | Verify: 结构/引用/衔接三要素齐全 | Gate: validate_task_docs 通过 | Parallelizable: No
[x] TP-01 | P1 | 永生史（过去）：六类事件线（神话宗教/古代实践/近代转折/现代技术/思想文学/失败教训） | Verify: 六类全覆盖且每事件含来源分级 | Gate: 时间维度=过去；与 TP-03 交叉引用 | Parallelizable: No
[x] TP-02 | P1 | 健康手册（现在）：七维度实证方法（营养/补剂/运动/睡眠/代谢筛查/环境） | Verify: 每方法含机制/证据等级/剂量/监测/风险 | Gate: 补剂分实证区与证据不足区 | Parallelizable: No
[x] TP-03 | P1 | 永生指南（未来）：七路径族全景（维护/重建/暂停/数字/认知/社会/哲学） | Verify: 每路径含机制/证据等级/阻塞点/时间窗口 | Gate: 哲学判据为标尺；与 TP-02 重叠区衔接 | Parallelizable: No
[ ] WS-01 | P0 | 永生史作品子集：从 2592 条事件选出 400 条，建立可复核作品范围 | Verify: works-subset.v1.json 覆盖全部时期/路径族/证据等级 | Gate: make history-timeline-gate 通过 | Parallelizable: No
[ ] WS-02 | P1 | 首批 31 条本地复核：来源可达性、DOI/标题匹配、日期与主张核对 | Verify: works-review-register.v1.json + verification_status=locally_reviewed | Gate: make history-timeline-gate 通过 | Parallelizable: No
[ ] WS-03 | P1 | 继续本地复核子集内剩余事件（369/400） | Verify: 本地复核登记与事件状态同步推进 | Gate: 每批通过 make history-timeline-gate | Parallelizable: Yes
[ ] WS-04 | P2 | 独立 fresh review 已本地复核事件 | Verify: 独立审阅登记；fresh_reviewed_event_count 上升 | Gate: 非编辑自审 | Parallelizable: No
