# Disembodied CNS 架构说明

`disembodied-cns/` 是去具身外部维持型中枢生命系统研究域。它只做高层系统建模、证据问题、风险分类和伦理边界，不提供实验操作协议。

## 目录结构

```text
disembodied-cns/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义具身半自主开放生命系统与去具身外部维持型中枢生命系统的对照、接口架构、研究对象和非目标。

## 上下游关系

- 上游依赖 `docs/explanations/human-runtime-infrastructure.md` 的 Human Infra 总模型和 `docs/reference/ethics-and-safety-boundaries.md` 的安全边界。
- 与 `memory-editing/` 共享主体连续性、可表达性、可退出性和尊严原则。
- 不依赖 `longevity-evidence/` 的数据采集脚本；两者只共享证据追溯和风险表达原则。

## 维护规则

- 新增内容必须保持非操作性、非实验步骤、非人体改造指南。
- 技术讨论必须围绕系统边界、接口、控制、反馈、故障、验证和伦理。
- 不宣称当前技术已经实现脱离身体的长期人格保存。
