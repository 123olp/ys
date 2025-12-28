# Wetware Engineering

> Decouple biological capabilities from organisms into reusable modules, reconstruct living systems with software engineering paradigms.

把生命能力从个体中解耦为可复用模块，用软件工程范式重构生命系统。

## 🧬 What is Wetware Engineering?

Wetware Engineering proposes treating organs, tissues, actuators, and sensors as modular "bio-components" that can be combined like software libraries — with standardized interfaces, dependency management, versioning, and testing.

**Core Idea**: Not "running biology as software", but **rebuilding life systems using programming paradigms**.

## 📚 Documentation

### 湿件工程 (Wetware Engineering)

| 中文 | English | 说明 |
|-----|---------|------|
| [快速入门指南](i18n/zh/湿件工程快速入门指南.md) | [Quick Start](i18n/en/wetware_engineering_quick_start.md) | 5分钟理解核心概念 |
| [湿件工程](i18n/zh/湿件工程.md) | [Wetware Engineering](i18n/en/wetware_engineering.md) | 完整概念介绍 |
| [湿件工程宣言](i18n/zh/湿件工程宣言.md) | [Manifesto](i18n/en/wetware_engineering_manifesto.md) | 愿景与原则 |
| [湿件工程技术规范](i18n/zh/湿件工程技术规范.md) | [Technical Spec](i18n/en/wetware_engineering_technical_spec.md) | Bio-Component Spec & Bio-DSL |

### 永生计划 (Immortality Project)

| 中文 | English | 说明 |
|-----|---------|------|
| [项目概述](i18n/zh/src/immortality/README.md) | [Overview](i18n/en/src/immortality/README.md) | 项目介绍 |
| [Human 3.0 架构](i18n/zh/src/immortality/docs/core/human_3.0_architecture.md) | [Architecture](i18n/en/src/immortality/docs/core/human_3.0_architecture.md) | 技术架构 |
| [27要素](i18n/zh/src/immortality/docs/core/immortality_27_elements.md) | [27 Elements](i18n/en/src/immortality/docs/core/immortality_27_elements.md) | 永生27要素 |
| [技术蓝图](i18n/zh/src/immortality/docs/core/human_3.0_technical_blueprint.md) | [Blueprint](i18n/en/src/immortality/human_3.0_technical_blueprint.md) | 实施路线 |

## 🎯 Core Concepts

```
┌─────────────────────────────────────────────────────────┐
│                   Wetware Engineering                    │
├─────────────────────────────────────────────────────────┤
│  Component    │  Interface    │  Runtime                │
│  (Bio-Module) │  (Bio-API)    │  (Orchestrator)         │
├───────────────┼───────────────┼─────────────────────────┤
│  • Actuator   │  • Power      │  • Scheduling           │
│  • Sensor     │  • Signal     │  • Resource Management  │
│  • Processor  │  • Isolation  │  • Monitoring           │
│  • Metabolic  │  • Mechanical │  • Fault Isolation      │
└───────────────┴───────────────┴─────────────────────────┘
```

## 🔧 Bio-DSL Example

```biomodule
COMPONENT muscle FROM human-skeletal-v2.3 AS flexor
COMPONENT sensor FROM synthetic-piezo-v1.1 AS force_sensor

CONNECT muscle.output TO sensor.input

RUNTIME {
  perfusion: { temperature: 37°C, flow_rate: 0.5 mL/min },
  control: { mode: "closed_loop" }
}
```

## 📁 Repository Structure

```
wetware-engineering/
├── README.md
├── AGENTS.md
├── LICENSE                          # CC BY-SA 4.0
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── i18n/
│   ├── zh/                          # 中文文档
│   │   ├── 湿件工程.md
│   │   ├── 湿件工程宣言.md
│   │   ├── 湿件工程技术规范.md
│   │   ├── 湿件工程快速入门指南.md
│   │   └── src/immortality/         # 永生计划 (中文)
│   └── en/                          # English docs
│       ├── wetware_engineering.md
│       ├── wetware_engineering_manifesto.md
│       ├── wetware_engineering_technical_spec.md
│       ├── wetware_engineering_quick_start.md
│       └── src/immortality/         # Immortality Project (EN)
└── .github/
    └── workflows/lint.yml
```

## 🗺️ Roadmap

- [x] Core concept definition
- [x] Bio-Component Spec v0.1
- [x] Bio-DSL syntax draft
- [x] Chinese documentation
- [x] English documentation
- [x] Immortality Project (ZH/EN)
- [ ] Reference implementation
- [ ] Tool chain development

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under [CC BY-SA 4.0](LICENSE).

---

*Wetware Engineering: Programming the future of life systems* 🧬💻
