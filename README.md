<p align="center">
  <img src="https://img.shields.io/badge/🧬-Wetware_Engineering-blue?style=for-the-badge" alt="Wetware Engineering"/>
</p>

<h1 align="center">Wetware Engineering</h1>

<p align="center">
  <strong>Decouple biological capabilities from organisms into reusable modules,<br/>reconstruct living systems with software engineering paradigms.</strong>
</p>

<p align="center">
  <a href="https://creativecommons.org/licenses/by-sa/4.0/"><img src="https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg" alt="License"/></a>
  <a href="https://github.com/tukuaiai/wetware-engineering/actions/workflows/lint.yml"><img src="https://github.com/tukuaiai/wetware-engineering/actions/workflows/lint.yml/badge.svg" alt="Markdown Lint"/></a>
  <img src="https://img.shields.io/badge/Bio--Component%20Spec-v0.1-green" alt="Spec Version"/>
  <img src="https://img.shields.io/badge/Docs-EN%20%7C%20中文-orange" alt="Bilingual"/>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-documentation">Documentation</a> •
  <a href="#-core-concepts">Core Concepts</a> •
  <a href="#-roadmap">Roadmap</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

## 🧬 What is Wetware Engineering?

**Wetware Engineering** is an interdisciplinary framework that applies software engineering paradigms to biological system construction.

> 💡 This is not "running biology as software", but **rebuilding life systems using programming paradigms**.

### The Vision

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   Traditional Biology          →      Wetware Engineering          │
│                                                                     │
│   🔬 Monolithic organisms      →      🧩 Modular bio-components     │
│   📝 Ad-hoc protocols          →      📋 Standardized interfaces    │
│   🔄 Manual integration        →      ⚡ Plug-and-play assembly     │
│   📊 Implicit dependencies     →      📦 Managed dependencies       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Key Innovations

| Component | Description |
|:----------|:------------|
| **Bio-Component** | Organs, tissues, actuators as composable modules |
| **Bio-Interface** | Standardized connections for plug-and-play |
| **Bio-DSL** | Domain-specific language for system composition |
| **Bio-Runtime** | Resource scheduling and monitoring system |

---

## 🚀 Quick Start

### 1. Get the Project

```bash
git clone https://github.com/tukuaiai/wetware-engineering.git
cd wetware-engineering
```

### 2. Explore Documentation

```bash
# English docs
ls i18n/en/

# Chinese docs  
ls i18n/zh/
```

### 3. Try Bio-DSL

```biodsl
// Define components
COMPONENT muscle FROM "muscle-actuator-human-skeletal@^2.3"
COMPONENT sensor FROM "piezo-force-sensor@~1.1"
COMPONENT controller FROM "neural-organoid-spinal@>=0.8"

// Connect components
CONNECT sensor.output TO controller.input
CONNECT controller.output TO muscle.stimulation

// Runtime configuration
RUNTIME {
  perfusion: { temperature: 37°C, flow_rate: 0.5 mL/min },
  control: { mode: "closed_loop" }
}
```

---

## 📚 Documentation

### 📖 Wetware Engineering

| Document | EN | 中文 | Description |
|:---------|:--:|:----:|:------------|
| Quick Start | [📄](i18n/en/wetware_engineering_quick_start.md) | [📄](i18n/zh/湿件工程快速入门指南.md) | 5-minute introduction |
| Plain Language | [📄](i18n/en/dummy_doctor_explanation.md) | [📄](i18n/zh/傻子博士解读版本.md) | Zero-barrier explanation |
| Core Concepts | [📄](i18n/en/wetware_engineering.md) | [📄](i18n/zh/湿件工程.md) | Complete introduction |
| Manifesto | [📄](i18n/en/wetware_engineering_manifesto.md) | [📄](i18n/zh/湿件工程宣言.md) | Vision & principles |
| Technical Spec | [📄](i18n/en/wetware_engineering_technical_spec.md) | [📄](i18n/zh/湿件工程技术规范.md) | Bio-Component Spec & DSL |

### 🧠 Immortality Project

<details>
<summary><b>Core Documents</b></summary>

| Document | EN | 中文 |
|:---------|:--:|:----:|
| Overview | [📄](i18n/en/src/immortality/README.md) | [📄](i18n/zh/src/immortality/README.md) |
| Human 3.0 Architecture | [📄](i18n/en/src/immortality/docs/core/human_3.0_architecture.md) | [📄](i18n/zh/src/immortality/docs/core/human_3.0_architecture.md) |
| Architecture (Academic) | [📄](i18n/en/src/immortality/docs/core/human_3.0_architecture_academic.md) | [📄](i18n/zh/src/immortality/docs/core/human_3.0_architecture_academic.md) |
| 27 Elements | [📄](i18n/en/src/immortality/docs/core/immortality_27_elements.md) | [📄](i18n/zh/src/immortality/docs/core/immortality_27_elements.md) |
| 27 Elements (Academic) | [📄](i18n/en/src/immortality/docs/core/immortality_27_elements_academic.md) | [📄](i18n/zh/src/immortality/docs/core/immortality_27_elements_academic.md) |
| Technical Blueprint | [📄](i18n/en/src/immortality/human_3.0_technical_blueprint.md) | [📄](i18n/zh/src/immortality/docs/core/human_3.0_technical_blueprint.md) |
| Blueprint (Academic) | [📄](i18n/en/src/immortality/docs/core/human_3.0_technical_blueprint_academic.md) | [📄](i18n/zh/src/immortality/docs/core/human_3.0_technical_blueprint_academic.md) |

</details>

<details>
<summary><b>Philosophy</b></summary>

| Document | EN | 中文 |
|:---------|:--:|:----:|
| Emotion Modeling | [📄](i18n/en/src/immortality/docs/philosophy/emotion_modeling.md) | [📄](i18n/zh/src/immortality/docs/philosophy/emotion_modeling.md) |
| Emotion Modeling (Academic) | [📄](i18n/en/src/immortality/docs/philosophy/emotion_modeling_academic.md) | [📄](i18n/zh/src/immortality/docs/philosophy/emotion_modeling_academic.md) |
| Experience Machine | [📄](i18n/en/src/immortality/docs/philosophy/ontology_experience_machine.md) | [📄](i18n/zh/src/immortality/docs/philosophy/ontology_experience_machine.md) |
| Experience Machine (Academic) | [📄](i18n/en/src/immortality/docs/philosophy/ontology_experience_machine_academic.md) | [📄](i18n/zh/src/immortality/docs/philosophy/ontology_experience_machine_academic.md) |

</details>

<details>
<summary><b>Guides</b></summary>

| Document | EN | 中文 |
|:---------|:--:|:----:|
| Human 3.0 Social Media | [📄](i18n/en/src/immortality/docs/guides/human_3.0_social_media.md) | [📄](i18n/zh/src/immortality/docs/guides/human_3.0_social_media.md) |
| Social Media (Academic) | [📄](i18n/en/src/immortality/docs/guides/human_3.0_social_media_academic.md) | [📄](i18n/zh/src/immortality/docs/guides/human_3.0_social_media_academic.md) |

</details>

### 📄 Academic Paper

| Resource | Link |
|:---------|:-----|
| Preprint PDF (13 pages) | [📥 Download](paper/arxiv/wetware_engineering.pdf) |
| LaTeX Source | [📝 View](paper/arxiv/wetware_engineering.tex) |
| Markdown Draft | [📖 Read](paper/wetware_engineering_full_paper.md) |

---

## 🎯 Core Concepts

### Component-Interface-Runtime Triad

```
┌─────────────────────────────────────────────────────────────────┐
│                     WETWARE ENGINEERING                         │
├─────────────────────┬─────────────────────┬─────────────────────┤
│     COMPONENT       │     INTERFACE       │      RUNTIME        │
│    (Bio-Module)     │     (Bio-API)       │   (Orchestrator)    │
├─────────────────────┼─────────────────────┼─────────────────────┤
│                     │                     │                     │
│  ◆ Actuator         │  ◆ Power            │  ◆ Scheduling       │
│  ◆ Sensor           │  ◆ Signal           │  ◆ Resource Mgmt    │
│  ◆ Processor        │  ◆ Isolation        │  ◆ Monitoring       │
│  ◆ Metabolic        │  ◆ Mechanical       │  ◆ Fault Isolation  │
│                     │                     │                     │
└─────────────────────┴─────────────────────┴─────────────────────┘
```

### Software ↔ Wetware Mapping

| Software Engineering | Wetware Engineering | Example |
|:---------------------|:--------------------|:--------|
| Package Manager | Bio-Registry | Component discovery |
| Semantic Versioning | Bio-Versioning | `muscle@2.3.1` |
| API Contract | Bio-Interface | I/O specification |
| Unit Test | Viability Test | Function verification |
| Container | Perfusion System | Life support |

---

## 📁 Project Structure

```
wetware-engineering/
│
├── 📄 README.md              # You are here
├── 📄 AGENTS.md              # AI Agent guide
├── 📄 CONTRIBUTING.md        # Contribution guide
├── 📄 CODE_OF_CONDUCT.md     # Community standards
├── 📄 LICENSE                # CC BY-SA 4.0
│
├── 🌐 i18n/
│   ├── en/                   # English documentation
│   │   ├── wetware_engineering*.md
│   │   └── src/immortality/  # Immortality Project
│   │
│   └── zh/                   # 中文文档
│       ├── 湿件工程*.md
│       └── src/immortality/  # 永生计划
│
├── 📝 paper/
│   └── arxiv/                # Academic paper (13 pages)
│
└── ⚙️ .github/
    └── workflows/            # CI/CD
```

---

## 🗺️ Roadmap

### ✅ Completed

- [x] Core concept definition
- [x] Bio-Component Spec v0.1
- [x] Bio-DSL syntax draft
- [x] Bilingual documentation (EN/中文)
- [x] Immortality Project docs
- [x] Academic paper preprint

### 🚧 In Progress

- [ ] arXiv submission

### 📋 Planned

- [ ] Reference implementation (Python/TypeScript)
- [ ] Bio-DSL parser
- [ ] Component registry prototype
- [ ] Visual editor

---

## 🤝 Contributing

We welcome contributions of all kinds!

```bash
# 1. Fork & Clone
git clone https://github.com/YOUR_USERNAME/wetware-engineering.git

# 2. Create branch
git checkout -b feature/your-feature

# 3. Make changes & commit
git commit -m "feat: add something awesome"

# 4. Push & create PR
git push origin feature/your-feature
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## ❓ FAQ

<details>
<summary><b>What's the difference between Wetware Engineering and Synthetic Biology?</b></summary>

Synthetic biology operates at the **gene/molecular level** (e.g., BioBricks), while Wetware Engineering operates at the **organ/system level**. They are complementary: synthetic biology defines component internals, Wetware Engineering defines how components combine.

</details>

<details>
<summary><b>Can Bio-DSL actually run?</b></summary>

Currently Bio-DSL is a **conceptual specification** with no runtime implementation. Its value lies in providing a standardized system description language, laying the foundation for future toolchains.

</details>

<details>
<summary><b>What are the practical applications?</b></summary>

- **Short-term**: Conceptual framework & standard specifications
- **Mid-term**: Toolchain development
- **Long-term**: Reusable, composable biological systems engineering

</details>

---

## 📄 License

<table>
<tr>
<td>

This project is licensed under **[CC BY-SA 4.0](LICENSE)**

</td>
<td>

✅ Free to share and adapt<br/>
✅ Attribution required<br/>
✅ Share under same license

</td>
</tr>
</table>

---

## 🔗 Links

| Resource | Link |
|:---------|:-----|
| 📦 GitHub | [tukuaiai/wetware-engineering](https://github.com/tukuaiai/wetware-engineering) |
| 🆔 Author ORCID | [0009-0009-6523-1823](https://orcid.org/0009-0009-6523-1823) |
| 🤖 ZRead AI | [AI-powered interpretation](https://zread.ai/tukuaiai/wetware-engineering) |
| 📓 NotebookLM | [AI learning notes](https://notebooklm.google.com/notebook/11e804ff-ae6f-4b27-b2f0-e94c2e98ce3a) |

---

<p align="center">
  <strong>🧬 Wetware Engineering: Programming the Future of Life Systems 💻</strong>
</p>

<p align="center">
  <sub>Built with ❤️ for the future of biological engineering</sub>
</p>
