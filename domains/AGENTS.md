# domains 目录说明

`domains/` 保存 Human Infra 的独立子域。每个子域都是一个有边界的研究或产品方向，必须说明对象、非目标、证据要求和上游/下游关系。

## 目录结构

```text
domains/
├── AGENTS.md
├── README.md
├── disembodied-cns/
│   ├── AGENTS.md
│   └── README.md
├── future-waiting/
│   ├── AGENTS.md
│   ├── README.md
│   └── paths/
├── longevity-evidence/
│   ├── AGENTS.md
│   ├── README.md
│   ├── data/
│   ├── docs/
│   └── scripts/
└── memory-editing/
    ├── AGENTS.md
    └── README.md
```

## 职责边界

- `longevity-evidence/` 是当前唯一含数据和采集脚本的产品化子域。
- `future-waiting/`、`disembodied-cns/` 和 `memory-editing/` 是高风险远期研究域，当前只做高层建模、证据框架和伦理边界。
- 子域之间共享 Human Infra 的伦理和证据原则，但不能共享模糊数据目录或脚本目录。

## 维护规则

- 新子域必须先在 `docs/reference/domain-map.md` 中说明存在理由、边界和非目标。
- 子域内新增文件或目录时，同步更新该子域 `AGENTS.md`。
- 跨子域概念进入 `docs/`；子域专属材料留在对应子域。
- 不为了“未来可能需要”创建空数据、空脚本或空框架目录。
