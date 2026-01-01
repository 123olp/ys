<!-- Banner -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,100:764ba2&height=200&section=header&text=🧬%20Wetware%20Engineering&fontSize=42&fontColor=fff&animation=fadeIn&fontAlignY=35&desc=Programming%20the%20Future%20of%20Life%20Systems&descSize=18&descAlignY=55"/>
    <img src="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,100:764ba2&height=200&section=header&text=🧬%20Wetware%20Engineering&fontSize=42&fontColor=fff&animation=fadeIn&fontAlignY=35&desc=Programming%20the%20Future%20of%20Life%20Systems&descSize=18&descAlignY=55" width="100%" alt="Wetware Engineering Banner"/>
  </picture>
</p>

<!-- Badges -->
<p align="center">
  <a href="https://creativecommons.org/licenses/by-sa/4.0/"><img src="https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg?style=flat-square" alt="License"/></a>
  <a href="https://github.com/tukuaiai/wetware-engineering/actions/workflows/lint.yml"><img src="https://img.shields.io/github/actions/workflow/status/tukuaiai/wetware-engineering/lint.yml?style=flat-square&label=Lint" alt="Lint Status"/></a>
  <img src="https://img.shields.io/badge/Bio--Component%20Spec-v0.1-success?style=flat-square" alt="Spec Version"/>
  <img src="https://img.shields.io/badge/Docs-EN%20%7C%20中文-blue?style=flat-square" alt="Bilingual"/>
  <a href="https://github.com/tukuaiai/wetware-engineering/stargazers"><img src="https://img.shields.io/github/stars/tukuaiai/wetware-engineering?style=flat-square&color=yellow" alt="Stars"/></a>
</p>

<!-- Tagline -->
<p align="center">
  <strong>Decouple biological capabilities from organisms into reusable modules,<br/>reconstruct living systems with software engineering paradigms.</strong>
</p>

<!-- Navigation -->
<p align="center">
  <a href="#-what-is-wetware-engineering">About</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-documentation">Docs</a> •
  <a href="#-core-concepts">Concepts</a> •
  <a href="#-roadmap">Roadmap</a> •
  <a href="#-contributing">Contribute</a>
</p>

<br/>

<!-- Intro Section -->
## 🧬 What is Wetware Engineering?

<table>
<tr>
<td width="60%">

**Wetware Engineering** is an interdisciplinary framework that applies software engineering paradigms to biological system construction.

> 💡 This is not "running biology as software", but **rebuilding life systems using programming paradigms**.

**Key Innovations:**

| 🧩 | **Bio-Component** | Organs, tissues, actuators as composable modules |
|:--:|:------------------|:-------------------------------------------------|
| 🔌 | **Bio-Interface** | Standardized connections for plug-and-play |
| 📝 | **Bio-DSL** | Domain-specific language for system composition |
| ⚙️ | **Bio-Runtime** | Resource scheduling and monitoring system |

</td>
<td width="40%">

```
┌────────────────────────────┐
│   Traditional Biology      │
│   ────────────────────     │
│   🔬 Monolithic organisms  │
│   📝 Ad-hoc protocols      │
│   🔄 Manual integration    │
│   📊 Implicit dependencies │
└────────────────────────────┘
            ⬇️
┌────────────────────────────┐
│   Wetware Engineering      │
│   ────────────────────     │
│   🧩 Modular components    │
│   📋 Standard interfaces   │
│   ⚡ Plug-and-play         │
│   📦 Managed dependencies  │
└────────────────────────────┘
```

</td>
</tr>
</table>

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/tukuaiai/wetware-engineering.git
cd wetware-engineering

# Explore documentation
ls i18n/en/    # English docs
ls i18n/zh/    # 中文文档
```

<details>
<summary>💻 <b>Try Bio-DSL Example</b></summary>

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

</details>

---

## 📚 Documentation

### 📖 Wetware Engineering Core

| Document | EN | 中文 | Description |
|:---------|:--:|:----:|:------------|
| Quick Start | [📄](i18n/en/wetware_engineering_quick_start.md) | [📄](i18n/zh/湿件工程快速入门指南.md) | 5-minute introduction |
| Plain Language | [📄](i18n/en/dummy_doctor_explanation.md) | [📄](i18n/zh/傻子博士解读版本.md) | Zero-barrier explanation |
| Core Concepts | [📄](i18n/en/wetware_engineering.md) | [📄](i18n/zh/湿件工程.md) | Complete introduction |
| Manifesto | [📄](i18n/en/wetware_engineering_manifesto.md) | [📄](i18n/zh/湿件工程宣言.md) | Vision & principles |
| Technical Spec | [📄](i18n/en/wetware_engineering_technical_spec.md) | [📄](i18n/zh/湿件工程技术规范.md) | Bio-Component Spec & DSL |

### 🧠 Immortality Project

<details>
<summary><b>📁 Core Documents</b> — Architecture, 27 Elements, Technical Blueprint</summary>

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
<summary><b>🎭 Philosophy</b> — Emotion Modeling, Experience Machine</summary>

| Document | EN | 中文 |
|:---------|:--:|:----:|
| Emotion Modeling | [📄](i18n/en/src/immortality/docs/philosophy/emotion_modeling.md) | [📄](i18n/zh/src/immortality/docs/philosophy/emotion_modeling.md) |
| Emotion Modeling (Academic) | [📄](i18n/en/src/immortality/docs/philosophy/emotion_modeling_academic.md) | [📄](i18n/zh/src/immortality/docs/philosophy/emotion_modeling_academic.md) |
| Experience Machine | [📄](i18n/en/src/immortality/docs/philosophy/ontology_experience_machine.md) | [📄](i18n/zh/src/immortality/docs/philosophy/ontology_experience_machine.md) |
| Experience Machine (Academic) | [📄](i18n/en/src/immortality/docs/philosophy/ontology_experience_machine_academic.md) | [📄](i18n/zh/src/immortality/docs/philosophy/ontology_experience_machine_academic.md) |

</details>

<details>
<summary><b>📢 Guides</b> — Social Media, Outreach</summary>

| Document | EN | 中文 |
|:---------|:--:|:----:|
| Human 3.0 Social Media | [📄](i18n/en/src/immortality/docs/guides/human_3.0_social_media.md) | [📄](i18n/zh/src/immortality/docs/guides/human_3.0_social_media.md) |
| Social Media (Academic) | [📄](i18n/en/src/immortality/docs/guides/human_3.0_social_media_academic.md) | [📄](i18n/zh/src/immortality/docs/guides/human_3.0_social_media_academic.md) |

</details>

### 📄 Academic Paper

| Resource | Link |
|:---------|:-----|
| 📥 Preprint PDF (13 pages) | [Download](paper/arxiv/wetware_engineering.pdf) |
| 📝 LaTeX Source | [View](paper/arxiv/wetware_engineering.tex) |
| 📖 Markdown Draft | [Read](paper/wetware_engineering_full_paper.md) |

---

## 🎯 Core Concepts

<table>
<tr>
<td width="50%">

### Component-Interface-Runtime

```
┌─────────────────────────────────┐
│      WETWARE ENGINEERING        │
├──────────┬──────────┬───────────┤
│COMPONENT │INTERFACE │  RUNTIME  │
│(Module)  │  (API)   │(Orchestr.)│
├──────────┼──────────┼───────────┤
│◆ Actuator│◆ Power   │◆ Schedule │
│◆ Sensor  │◆ Signal  │◆ Resource │
│◆ Process │◆ Isolate │◆ Monitor  │
│◆ Metabol │◆ Mechani │◆ Fault    │
└──────────┴──────────┴───────────┘
```

</td>
<td width="50%">

### Software ↔ Wetware Mapping

| Software | Wetware | Example |
|:---------|:--------|:--------|
| Package Manager | Bio-Registry | Discovery |
| Semver | Bio-Versioning | `muscle@2.3.1` |
| API Contract | Bio-Interface | I/O spec |
| Unit Test | Viability Test | Verification |
| Container | Perfusion | Life support |

</td>
</tr>
</table>

---

## 📁 Project Structure

```
wetware-engineering/
├── 📄 README.md              # You are here
├── 📄 AGENTS.md              # AI Agent guide
├── 📄 CONTRIBUTING.md        # Contribution guide
├── 📄 LICENSE                # CC BY-SA 4.0
│
├── 🌐 i18n/
│   ├── en/                   # English documentation
│   └── zh/                   # 中文文档
│
├── 📝 paper/arxiv/           # Academic paper (13 pages)
│
└── ⚙️ .github/workflows/     # CI/CD
```

---

## 🗺️ Roadmap

| Status | Milestone |
|:------:|:----------|
| ✅ | Core concept definition |
| ✅ | Bio-Component Spec v0.1 |
| ✅ | Bio-DSL syntax draft |
| ✅ | Bilingual documentation (EN/中文) |
| ✅ | Academic paper preprint |
| 🚧 | arXiv submission |
| 📋 | Reference implementation (Python/TypeScript) |
| 📋 | Bio-DSL parser |
| 📋 | Component registry prototype |

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

```bash
git clone https://github.com/YOUR_USERNAME/wetware-engineering.git
git checkout -b feature/your-feature
git commit -m "feat: add something awesome"
git push origin feature/your-feature
```

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

**Short-term**: Conceptual framework & standard specifications  
**Mid-term**: Toolchain development  
**Long-term**: Reusable, composable biological systems engineering

</details>

---

## 🔗 Links & Resources

<p align="center">
  <a href="https://github.com/tukuaiai/wetware-engineering"><img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub"/></a>
  <a href="https://orcid.org/0009-0009-6523-1823"><img src="https://img.shields.io/badge/ORCID-Author-A6CE39?style=for-the-badge&logo=orcid" alt="ORCID"/></a>
  <a href="https://zread.ai/tukuaiai/wetware-engineering"><img src="https://img.shields.io/badge/ZRead-AI%20Interpretation-FF6B6B?style=for-the-badge" alt="ZRead"/></a>
</p>

---

## 📄 License

This project is licensed under **[CC BY-SA 4.0](LICENSE)** — Free to share and adapt with attribution.

---

<!-- Footer -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,100:764ba2&height=100&section=footer" width="100%"/>
</p>

<p align="center">
  <sub>Built with ❤️ for the future of biological engineering</sub>
</p>
