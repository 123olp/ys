# Memory Editing 架构说明

`memory-editing/` 是记忆编辑与人格连续性研究域。它处理记忆痕迹读写、删除、写入、重构、验证和治理的高层模型，不提供可执行神经操控步骤。

## 目录结构

```text
memory-editing/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义记忆编辑的核心对象、研究问题、安全边界和与 Human Infra 的关系。

## 上下游关系

- 上游依赖 `docs/reference/ethics-and-safety-boundaries.md` 的神经安全、同意、退出和审计原则。
- 与 `disembodied-cns/` 共享主体连续性和尊严原则。
- 不与 `longevity-evidence/` 共享数据模型；记忆编辑不是普通健康干预证据页。

## 维护规则

- 新增内容必须明确区分治疗性干预、增强性干预和控制性操控。
- 禁止写入可执行的记忆读取、删除、写入、重构或人体实验步骤。
- 技术路线只能作为公开证据的高层整理，并必须保留不确定性、失败模式和滥用风险。
