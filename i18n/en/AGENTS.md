# AGENTS.md

> AI Agent Operating Manual - Wetware Engineering Project

## 1. Mission & Scope

### Allowed Operations
- Edit/create documentation files (`.md`) under `i18n/` directory
- Edit/create paper-related files under `paper/` directory
- Update README.md, AGENTS.md, CONTRIBUTING.md
- Add new Bio-DSL examples
- Fix broken links and formatting issues in documentation

### Prohibited Operations
- Delete any existing documentation (unless explicitly requested)
- Modify LICENSE file
- Modify CI configuration in `.github/workflows/` (unless explicitly requested)
- Fabricate technical details or citations in documentation

### Sensitive Areas (Modify with Caution)
- `i18n/zh/湿件工程技术规范.md` - Bio-Component Spec core definitions
- `i18n/*/src/immortality/` - Immortality Project subproject
- `paper/arxiv/wetware_engineering.tex` - Academic paper LaTeX source

## 2. Golden Path (Recommended Workflow)

```bash
# 1. Clone repository
git clone https://github.com/tukuaiai/wetware-engineering.git
cd wetware-engineering

# 2. View documentation structure
ls -la i18n/zh/
ls -la i18n/en/

# 3. Edit documentation
# ... make changes ...

# 4. Check Markdown format (optional locally)
# npx markdownlint-cli2 "**/*.md"

# 5. Commit changes
git add .
git commit -m "docs: <describe changes>"
git push
```

## 3. Must-Run Commands

This is a pure documentation project with no build/test commands.

| Scenario | Command | Description |
|----------|---------|-------------|
| View structure | `find i18n -name "*.md" \| head -20` | List documentation files |
| Format check | `npx markdownlint-cli2 "**/*.md"` | Optional, CI runs automatically |
| Compile paper | `cd paper/arxiv && xelatex wetware_engineering.tex` | Requires texlive-full |

## 4. Code Change Rules

### Documentation Writing Principles
- Chinese docs go in `i18n/zh/`, English docs go in `i18n/en/`
- Immortality Project docs go in `i18n/*/src/immortality/`
- Academic papers go in `paper/`
- Filenames use Chinese (for Chinese docs) or lowercase_underscore (for English docs)

### Link Rules
- Use relative path links
- Ensure correct paths when linking to other documents (note `src/` hierarchy)

### Prohibited Behaviors
- Do not arbitrarily restructure directory layout
- Do not delete `_academic.md` suffixed academic version documents
- Do not modify Bio-DSL syntax definitions (unless explicitly requested)

## 5. Style & Quality

### Markdown Standards
- CI uses markdownlint-cli2 for checking
- Disabled rules: MD013 (line length), MD033 (HTML), MD041 (first line heading)

### Naming Conventions
- Chinese docs: `湿件工程*.md`
- English docs: `snake_case.md`
- Academic version suffix: `*_academic.md`

### Document Structure
- Every document must have a level-1 heading
- Use appropriate heading hierarchy (no skipping levels)
- Annotate code blocks with language type

### LaTeX Paper Standards
- Use arXiv standard template (`arxiv.sty`)
- Use `\textit{}` for journal/book names in references
- Use `\,` to separate numbers and units

## 6. Project Map

```
wetware-engineering/
├── README.md                    # Project homepage (bilingual)
├── AGENTS.md                    # This file - AI Agent guide
├── CONTRIBUTING.md              # Contribution guide
├── CODE_OF_CONDUCT.md           # Code of conduct
├── LICENSE                      # CC BY-SA 4.0
│
├── i18n/zh/                     # Chinese docs
│   ├── README.md                # Chinese index
│   ├── 湿件工程.md              # Core concepts
│   ├── 湿件工程宣言.md          # Manifesto
│   ├── 湿件工程技术规范.md      # Technical spec (Bio-Component Spec + Bio-DSL)
│   ├── 湿件工程快速入门指南.md  # Quick start
│   ├── 傻子博士解读版本.md      # Plain language version
│   └── src/immortality/         # Immortality Project (Chinese)
│       ├── README.md            # Project overview
│       ├── AGENTS.md            # Subproject Agent guide
│       ├── docs/core/           # Core documents
│       │   ├── human_3.0_architecture.md
│       │   ├── human_3.0_architecture_academic.md
│       │   ├── human_3.0_technical_blueprint.md
│       │   ├── human_3.0_technical_blueprint_academic.md
│       │   ├── immortality_27_elements.md
│       │   └── immortality_27_elements_academic.md
│       ├── docs/philosophy/     # Philosophy
│       │   ├── emotion_modeling.md
│       │   ├── emotion_modeling_academic.md
│       │   ├── ontology_experience_machine.md
│       │   └── ontology_experience_machine_academic.md
│       ├── docs/guides/         # Guides
│       │   ├── human_3.0_social_media.md
│       │   └── human_3.0_social_media_academic.md
│       └── data/                # Data templates
│
├── i18n/en/                     # English docs
│   ├── README.md                # English index
│   ├── wetware_engineering.md
│   ├── wetware_engineering_manifesto.md
│   ├── wetware_engineering_technical_spec.md
│   ├── wetware_engineering_quick_start.md
│   ├── dummy_doctor_explanation.md
│   └── src/immortality/         # Immortality Project (EN)
│       ├── README.md
│       ├── AGENTS.md
│       ├── docs/core/           # Core documents
│       │   ├── human_3.0_architecture.md
│       │   ├── human_3.0_architecture_academic.md
│       │   ├── human_3.0_technical_blueprint_academic.md
│       │   ├── immortality_27_elements.md
│       │   └── immortality_27_elements_academic.md
│       ├── docs/philosophy/     # Philosophy
│       │   ├── emotion_modeling.md
│       │   ├── emotion_modeling_academic.md
│       │   ├── ontology_experience_machine.md
│       │   └── ontology_experience_machine_academic.md
│       └── docs/guides/         # Guides
│           ├── human_3.0_social_media.md
│           └── human_3.0_social_media_academic.md
│
├── paper/                       # Academic paper
│   ├── arxiv/                   # arXiv submission version
│   │   ├── wetware_engineering.tex   # LaTeX source
│   │   ├── wetware_engineering.pdf   # Compiled PDF (13 pages)
│   │   ├── arxiv.sty            # arXiv style
│   │   └── orcid.pdf            # ORCID icon
│   ├── sections/                # Paper sections (Markdown)
│   └── wetware_engineering_full_paper.md  # Complete draft
│
├── backups/                     # Backup tools
│   ├── gz/                      # Compressed backup storage
│   ├── 快速备份.py
│   └── 一键备份.sh
│
└── .github/
    ├── workflows/lint.yml       # Markdown lint CI
    ├── ISSUE_TEMPLATE/          # Issue templates
    └── PULL_REQUEST_TEMPLATE.md # PR template
```

## 7. Common Pitfalls

| Problem | Cause | Solution |
|---------|-------|----------|
| Link 404 | Path missing `src/` | Check actual file location |
| CI lint failure | Markdown format issues | Run `npx markdownlint-cli2` locally |
| Chinese filename garbled | Git config issue | Ensure `git config core.quotepath false` |
| LaTeX compile failure | Missing dependencies | Install `texlive-full` |
| PDF font issues | Using pdflatex | Use `xelatex` instead |

## 8. PR / Commit Rules

### Commit Message Format
```
<type>: <description>

type: docs / fix / chore / refactor
```

Examples:
- `docs: add Bio-DSL example for neural controller`
- `docs: update paper formatting for arXiv submission`
- `fix: correct link to immortality roadmap`
- `chore: update .gitignore`

### Branch Strategy
- Main branch: `main`
- Feature branches: `feature/<topic>` or `docs/<topic>`

### CI Triggers
- Push to any branch with `.md` file changes triggers Markdown lint

## 9. Documentation Sync Rule

### Mandatory Sync Requirements
Any of the following changes must sync updates to README.md and AGENTS.md:
- Directory structure changes
- Adding/removing documentation files
- Link path changes
- Workflow/CI configuration changes

### When Uncertain
- Use `TODO: <content needing confirmation>` annotation
- Do not guess or fabricate

---

## Key Concepts (Quick Reference)

- **Bio-Component**: Independently functional biological module unit (actuator/sensor/processor/metabolic unit)
- **Bio-Interface**: Standardized connections (power/signal/isolation/mechanical)
- **Bio-DSL**: Domain-specific language for describing component composition
- **Bio-Runtime**: Orchestration system responsible for scheduling, resource management, monitoring

## Current Status

| Module | Status |
|--------|--------|
| Core Concepts | ✅ Defined |
| Bio-Component Spec | ✅ v0.1 Draft |
| Bio-DSL Syntax | ✅ Draft Complete |
| Chinese Docs | ✅ Complete |
| English Docs | ✅ Complete |
| Academic Paper | ✅ Preprint Complete (13 pages) |
| arXiv Submission | 📋 Pending |
| Reference Implementation | 📋 Planned |
