# domains 目录说明

`domains/` 保存 Human Infra 的独立子域。每个子域都是一个有边界的研究或产品方向，必须说明对象、非目标、证据要求和上游/下游关系。

## 目录结构

```text
domains/
├── AGENTS.md
├── README.md
├── antimicrobial-resilience/
│   ├── AGENTS.md
│   └── README.md
├── assistive-technology-access/
│   ├── AGENTS.md
│   └── README.md
├── biostasis-cryopreservation/
│   ├── AGENTS.md
│   └── README.md
├── cancer-control/
│   ├── AGENTS.md
│   └── README.md
├── cellular-reprogramming/
│   ├── AGENTS.md
│   └── README.md
├── cognitive-augmentation/
│   ├── AGENTS.md
│   └── README.md
├── disembodied-cns/
│   ├── AGENTS.md
│   └── README.md
├── future-waiting/
│   ├── AGENTS.md
│   ├── README.md
│   └── paths/
├── governance-rights/
│   ├── AGENTS.md
│   └── README.md
├── immune-maintenance/
│   ├── AGENTS.md
│   └── README.md
├── longevity-evidence/
│   ├── AGENTS.md
│   ├── README.md
│   ├── data/
│   ├── docs/
│   └── scripts/
├── nutrition-metabolic-health/
│   ├── AGENTS.md
│   └── README.md
├── physical-activity-mobility/
│   ├── AGENTS.md
│   └── README.md
├── cardiovascular-resilience/
│   ├── AGENTS.md
│   └── README.md
├── musculoskeletal-integrity/
│   ├── AGENTS.md
│   └── README.md
├── measurement-feedback/
│   ├── AGENTS.md
│   └── README.md
├── mental-health-affective-stability/
│   ├── AGENTS.md
│   └── README.md
├── memory-editing/
│   ├── AGENTS.md
│   └── README.md
├── neuro-continuity/
│   ├── AGENTS.md
│   └── README.md
├── pain-suffering-control/
│   ├── AGENTS.md
│   └── README.md
├── planetary-health-environment/
│   ├── AGENTS.md
│   └── README.md
├── regenerative-medicine/
│   ├── AGENTS.md
│   └── README.md
├── rehabilitation-functioning/
│   ├── AGENTS.md
│   └── README.md
├── resource-social-infra/
│   ├── AGENTS.md
│   └── README.md
├── risk-engineering/
│   ├── AGENTS.md
│   └── README.md
├── sensory-continuity/
│   ├── AGENTS.md
│   └── README.md
├── sleep-circadian-recovery/
│   ├── AGENTS.md
│   └── README.md
├── social-connection-relational-infra/
│   ├── AGENTS.md
│   └── README.md
├── substance-exposure-control/
│   ├── AGENTS.md
│   └── README.md
├── health-literacy-navigation/
│   ├── AGENTS.md
│   └── README.md
└── oral-health-continuity/
    ├── AGENTS.md
    └── README.md
```

## 职责边界

- `longevity-evidence/` 是当前唯一含数据和采集脚本的产品化子域。
- `nutrition-metabolic-health/`、`physical-activity-mobility/`、`cardiovascular-resilience/` 和 `musculoskeletal-integrity/` 负责营养、行动、循环和承载结构这些身体运行条件。
- `cellular-reprogramming/` 负责山中因子、部分重编程、化学重编程、AI 因子设计和表观遗传编辑等“细胞状态可重写”谱系，不提供实验协议或人体应用建议。
- `regenerative-medicine/`、`cancer-control/` 和 `immune-maintenance/` 负责身体基底维护相关的机制、风险和证据边界。
- `rehabilitation-functioning/`、`assistive-technology-access/` 和 `sensory-continuity/` 负责功能恢复、能力补偿和感官反馈连续性。
- `antimicrobial-resilience/` 负责抗微生物耐药、感染控制和现代医学抗感染底座。
- `neuro-continuity/`、`memory-editing/`、`cognitive-augmentation/` 和 `disembodied-cns/` 负责神经、身份、认知和去具身连续性相关边界。
- `mental-health-affective-stability/`、`sleep-circadian-recovery/` 和 `pain-suffering-control/` 负责心理稳定、恢复调度和持续存在的可承受性。
- `social-connection-relational-infra/` 负责社会连接、孤独、照护网络、信任和社区关系。
- `substance-exposure-control/` 负责烟草、酒精、成瘾性物质、有害暴露和主体自主性风险。
- `health-literacy-navigation/` 负责健康素养、服务导航、可理解信息、风险沟通和共同决策。
- `oral-health-continuity/` 负责口腔健康、咀嚼、疼痛、感染、营养和沟通连续性。
- `future-waiting/` 和 `biostasis-cryopreservation/` 负责等待未来的时间成本和损耗成本路径。
- `risk-engineering/`、`planetary-health-environment/`、`resource-social-infra/` 和 `governance-rights/` 负责外部风险、环境底座、资源底座和主体权利保护。
- `measurement-feedback/` 负责所有研究域进入定量模型前的测量、预测和反馈接口。
- 子域之间共享 Human Infra 的伦理和证据原则，但不能共享模糊数据目录或脚本目录。

## 维护规则

- 新子域必须先在 `docs/reference/domain-map.md` 中说明存在理由、边界和非目标。
- 子域内新增文件或目录时，同步更新该子域 `AGENTS.md`。
- 跨子域概念进入 `docs/`；子域专属材料留在对应子域。
- 不为了“未来可能需要”创建空数据、空脚本或空框架目录。
