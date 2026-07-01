# cervical-cancer-hpv-prevention-screening-continuity 目录说明

本目录维护宫颈癌 HPV 预防、筛查、异常追踪、阴道镜入口、生殖/性健康和公平可及资料。它是癌症控制与感染预防、性/生殖健康交叉的器官特异域。

## 目录结构

```text
cervical-cancer-hpv-prevention-screening-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 HPV 预防、宫颈筛查、异常结果闭环和生殖/性健康服务如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案 HPV、宫颈细胞学、阴道镜、病理、性史、生殖史或治疗资料。
- 资料进入本域时必须保留 HPV 预防、筛查对象、异常追踪、隐私污名、生殖健康和禁止用途。

## 上下游关系

- 上游来自 NCI、CDC 和宫颈癌/HPV 公开资料。
- 下游服务 `cancer-control/`、`sexual-health-sti-prevention-continuity/`、生殖健康和幸存者建模。
- 不替代医生、妇科、肿瘤科、病理科、疫苗服务、性健康服务、保险服务或个体医疗建议。

## 维护规则

- 不写个人 HPV/宫颈筛查结果解释、疫苗建议、筛查频率、阴道镜、病理、治疗、用药、手术或个体建议。
- 不把系统级宫颈癌研究写成 HPV 解释器、异常结果处理器、疫苗推荐器或商业检测推广。
- 新增变量必须区分 HPV 预防、筛查覆盖、异常追踪、隐私污名、生殖健康和公平性。
