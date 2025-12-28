# AGENTS.md

## Project Overview
Wetware Engineering - A paradigm for building biological systems using software engineering principles.

## Key Concepts
- **Bio-Component**: Modular biological units (actuators, sensors, processors, metabolic units)
- **Bio-Interface**: Standardized connections (power, signal, isolation, mechanical)
- **Bio-DSL**: Domain-specific language for describing component compositions
- **Bio-Runtime**: Orchestration system for scheduling, resource management, monitoring

## Documentation Structure

```
wetware-engineering/
├── README.md                        # Project overview
├── i18n/
│   ├── zh/                          # 中文文档
│   │   ├── 湿件工程.md              # Core concept
│   │   ├── 湿件工程宣言.md          # Manifesto
│   │   ├── 湿件工程技术规范.md      # Technical spec
│   │   ├── 湿件工程快速入门指南.md  # Quick start
│   │   └── src/immortality/         # Immortality project (ZH)
│   │       ├── docs/core/           # Core docs
│   │       ├── docs/philosophy/     # Philosophy
│   │       └── docs/guides/         # Guides
│   └── en/                          # English docs
│       └── immortality/             # Immortality project (EN)
└── .github/                         # GitHub config
```

## File Conventions
- Documentation in Markdown
- Specifications use YAML for structured data
- Bio-DSL examples use `.biomodule` extension conceptually

## Current Status
- Core concepts: Defined
- Bio-Component Spec: v0.1 draft
- Bio-DSL: Syntax draft complete
- Chinese documentation: Complete
- English documentation: Partial (Immortality only)
- Reference implementation: Planned
