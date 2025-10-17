# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

**Project Name**: 永生 (Immortality) / 可能性极大主义 (Possibilistic Maximalism)
**Type**: Philosophical Research Framework + Knowledge Repository
**Primary Language**: Chinese (with English translations)
**Status**: Phase 0 - Foundation Building (Active Research)

This is **NOT a traditional software project**. It is a long-term philosophical and scientific research initiative aimed at systematically eliminating three dimensions of human scarcity: time (longevity), cognition (BCI/memory editing), and energy (entropy efficiency).

### Core Philosophy

The project follows strict engineering principles applied to documentation:
- **KISS** (Keep It Simple): Simplicity over complexity
- **YAGNI** (You Aren't Gonna Need It): Implement only current needs
- **DRY** (Don't Repeat Yourself): Eliminate duplication
- **SOLID**: Applied to documentation structure and organization

### Three Dimensions of Focus

1. **Time Liberation (⏳)**: Longevity Escape Velocity (LEV) - ΔLE ≥ 1 year/year
2. **Cognitive Liberation (🧠)**: Brain-Computer Interface + Memory Editing - P(realization) ≈ 1
3. **Energy Liberation (⚡)**: Entropy Efficiency + Reversible Computing - η → 1, ΔS → 0

---

## Build System

### Documentation Build

```bash
# Build all documentation (HTML + PDF)
make all

# Output directory: out/
# - out/report.html
# - out/report.pdf

# Clean build artifacts
make clean
```

### Requirements

```bash
# Install build dependencies
sudo apt-get install pandoc make texlive-xetex  # Linux
brew install pandoc make                        # macOS
```

### Manual Workflow

This project has **no automated testing or CI/CD**. All processes are manual:
1. Edit Markdown files directly
2. Build with `make all` to generate outputs
3. Commit changes following git workflow (see below)

---

## Project Structure

```
永生/
├── README.md                      # Main project overview (Chinese)
├── README.en.md                   # English translation
├── Makefile                       # Build system (pandoc workflow)
│
├── docs/                          # Core theoretical documentation
│   ├── implementation_roadmap.md  # Detailed 5-phase execution plan (22KB)
│   ├── 实践指南.md                # Implementation guide (12KB)
│   ├── 人类 3.0 架构.md           # Modular neural architecture
│   └── [Other theoretical documents]
│
├── kpi/                           # Key Performance Indicators
│   └── 指标_baseline.yaml         # KPI baseline metrics (YAML format)
│
├── data/                          # Evidence & research database (structure ready, content pending)
│   ├── evidence/                  # Evidence collection
│   └── refs/                      # Reference materials
│
├── governance/                    # Ethics & governance framework
│   ├── 神经权利与合规.md          # Neural rights & compliance
│   └── 行星边界约束.md            # Planetary boundary constraints
│
├── audit/                         # Physical limits validation
│   └── 物理极限审计.md            # Physical limits audit
│
├── prototypes/                    # Proof-of-concept directories (planned)
│   ├── lev_evidence/              # Longevity Escape Velocity
│   ├── bci_sandbox/               # Brain-Computer Interface
│   └── energy_eff/                # Energy efficiency
│
├── reviews/                       # Peer review records
│   └── 评审清单.md                # Review checklist
│
├── lesson/                        # Lessons learned from issues
│   └── 文档体系重构_20251017_1105.md
│
├── archives/                      # Historical documents
│   └── original_docs/             # 40+ iterative development files
│
└── .github/                       # GitHub configuration
    ├── ISSUE_TEMPLATE/            # Issue templates (bug, feature, question, data)
    └── pull_request_template.md   # PR template
```

### Directory Purpose Summary

- **docs/**: Theoretical framework, white papers, roadmaps, guides
- **kpi/**: Quantified success metrics for three dimensions
- **data/**: Structured evidence database (mostly placeholders currently)
- **governance/**: Ethical constraints and compliance frameworks
- **audit/**: Physical law boundary validation
- **prototypes/**: Future proof-of-concept code (empty now)
- **lesson/**: Experience capture from problems encountered
- **archives/**: Historical documentation from project evolution

---

## Git Workflow

### Automated Commit Requirements (CRITICAL)

Per project guidelines in `.claude/CLAUDE.md`, **ALL code changes MUST be automatically committed and pushed** in two scenarios:

1. **After Task Completion**: After any development task is successfully completed
   - Code modifications
   - Feature implementation
   - Bug fixes
   - Documentation updates

2. **Before Major Changes**: Before executing any destructive or high-risk modifications
   - Large-scale refactoring
   - Deleting core functionality
   - Experimental changes that may break stability

### Commit Command Format

Use HEREDOC format for all commit messages:

```bash
git add .
git commit -m "$(cat <<'EOF'
Brief description of changes

Detailed explanation:
- What was changed
- Why it was changed
- Stage/environment context

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
git push origin main
```

### Important Notes

- **Repository**: Private GitHub repository at https://github.com/123olp/ys
- **Branch**: Currently on `main` branch
- **Status**: Clean working directory (as of conversation start)
- **Never skip hooks**: Do not use `--no-verify` or similar flags
- **Never force push**: Especially to main/master branches

---

## File Naming Conventions

### Temporal Tracking

Files include dates for version tracking:
- Format 1: `filename_YYYY-MM-DD.md` (e.g., `项目全面分析与实施路径_2025_10_17.md`)
- Format 2: `filename_YYYYMMDD_HHMM.md` (e.g., `文档体系重构_20251017_1105.md`)

### Language Convention

- **Chinese filenames**: Core documentation written primarily in Chinese
- **English filenames**: When explicitly translated or intended for international audience
- **Bilingual**: Most documents have both Chinese and English versions (e.g., README.md / README.en.md)

---

## Key Performance Indicators (KPI)

### Location

`kpi/指标_baseline.yaml`

### Structure

```yaml
longevity:           # Time dimension
  delta_LE_per_year: null       # Yearly life expectancy gain (years/year)
  HALE_over_LE: null            # Healthy life years / Total life years

cognition:           # Cognitive dimension
  bci_bandwidth_bps: null       # BCI read/write bandwidth (bits/sec)
  write_error_rate: null        # Neural write error rate ε
  experience_consistency_kappa: null  # Experience consistency κ

energy:              # Energy dimension
  system_efficiency_eta: null   # System efficiency η
  eroei: null                   # Energy Return On Energy Invested

governance:          # Ethical compliance
  irb_approval_rate: null       # IRB approval rate
  audit_trace_completeness: null  # Audit trail completeness
```

### Current Status

All KPI values are currently `null` (baseline not yet established). This is expected in Phase 0.

---

## Implementation Roadmap (5 Phases)

From `docs/implementation_roadmap.md`:

| Phase | Timeline | Core Goal | Key Deliverable |
|-------|----------|-----------|-----------------|
| **Phase 0** | 0-6 months | Foundation + Survival Stability | White paper v1.1, stable income |
| **Phase 1** | 6-18 months | Academic Dissemination | Published papers, 1000+ community members |
| **Phase 2** | 18-36 months | Evidence Database Construction | LEV/BCI/Energy databases with 100+ entries each |
| **Phase 3** | 3-5 years | Prototype Validation | At least 1 verifiable prototype |
| **Phase 4** | 5-10 years | Organization Building | Establish "Possibility Lab" |
| **Phase 5** | 10-30 years | Technical Breakthroughs | Substantial progress in at least one dimension |

### Current Phase: Phase 0 (Foundation Building)

Focus: Stabilize survival, refine theory, initial dissemination.

---

## Contribution Guidelines

From `CONTRIBUTING.md`:

### What We Need

1. **Theoretical Contributions**: Philosophical refinement, academic dialogue, ethical framework
2. **Data Contributions**: Research data for LEV/BCI/Energy, KPI baseline data
3. **Technical Contributions**: Database construction, visualization tools, prototype development
4. **Documentation Contributions**: Translation, documentation improvement, learning resources

### Contribution Workflow

```bash
# 1. Fork repository
# 2. Create feature branch
git checkout -b feature/amazing-idea

# 3. Make changes following project conventions

# 4. Commit with detailed message
git commit -m "Brief description

Detailed explanation:
- What changed
- Why changed
- Impact scope"

# 5. Push and create PR
git push origin feature/amazing-idea
```

### Code of Conduct

- Respect different viewpoints
- Accept constructive criticism
- Focus on project's best interest
- Maintain friendliness and inclusivity

---

## Experience Capture System

### Lessons Learned Directory: `lesson/`

**Trigger Condition**: Any error or problem that is identified and fixed MUST trigger experience capture.

**Process**:
1. Identify and fix the error
2. Create new file: `问题描述_YYYYMMDD_HHMM.md`
3. Commit to repository
4. Push to ensure knowledge preservation

**File Format**:

```markdown
# Problem Title, Time, Module Location, Architecture Context

---

### Problem Description
(Clear description of error and symptoms)

### Root Cause Analysis
(Deep analysis of core cause, technical bottleneck, or logic defect)

### Solution & Steps
(Detailed record of final solution, specific commands, code adjustments)
```

**Example**: `lesson/文档体系重构_20251017_1105.md` documents the refactoring experience.

---

## Documentation Standards

### Markdown Format

- Use GitHub Flavored Markdown (GFM)
- Clear heading hierarchy
- Code blocks with language annotation
- Aligned tables for readability
- Valid, accessible links

### Mathematical Notation

Project extensively uses mathematical formalism:

```
Time: Y(t) = ∫₀^∞ W(t)dt, where ΔLE ≥ 1 → lim(t→∞) Y = ∞
Cognition: P(realization) = ∏P(i) → g(E), bandwidth ≥ b bit/s, error ≤ ε
Energy: η → 1, ΔS → 0, approaching Landauer limit
```

### Physical Limits References

Always acknowledge physical boundaries:
- **Bekenstein Bound**: Information capacity upper limit
- **Bremermann Limit**: Computation rate upper limit
- **Landauer Principle**: Thermodynamic cost of information erasure

---

## Important Constraints

### What This Project Is NOT

- ❌ NOT a traditional software codebase
- ❌ NOT a commercial product
- ❌ NOT expecting rapid results (30-year horizon)
- ❌ NOT ignoring physical law constraints

### What This Project IS

- ✅ Philosophical framework with technical grounding
- ✅ Long-term research coordination hub
- ✅ Knowledge repository for cross-disciplinary work
- ✅ Community-driven open-source initiative (CC BY 4.0)

### Ethical Red Lines (From Governance)

- Neural editing must follow strict ethical review
- Privacy protection in all data collection
- Avoid technology privilege solidification
- Maintain auditability and reversibility

---

## References & Learning Resources

### Must-Read Papers (Top 10)

**Philosophy**:
1. Nick Bostrom - "A History of Transhumanist Thought"
2. Derek Parfit - "Personal Identity"

**Longevity**:
3. López-Otín et al. (2023) - "The Hallmarks of Aging" (Cell)
4. Ocampo et al. (2016) - "Partial Reprogramming" (Cell)

**BCI/Cognition**:
5. Willett et al. (2023) - "High-Performance BCI" (Nature)
6. Neuralink - Technical Paper (latest)

**Energy/Thermodynamics**:
7. Landauer (1961) - "Irreversibility and Heat Generation"
8. Bennett (1982) - "Thermodynamics of Computation"

**Boundaries**:
9. Bekenstein (1981) - "Universal Upper Bound"
10. Lloyd (2000) - "Ultimate Physical Limits" (Nature)

### Community Platforms

- **LessWrong**: Rationalist philosophy discussions
- **EA Forum**: Effective altruism community
- **Reddit**: r/Longevity, r/Futurology
- **Academic**: arXiv, PubMed, Nature journals

---

## Working with This Repository

### Reading Files

- Always start with `README.md` for project context
- Consult `docs/implementation_roadmap.md` for detailed execution plan
- Check `docs/实践指南.md` for practical implementation guidance
- Review `kpi/指标_baseline.yaml` for quantified metrics

### Making Changes

1. **Understand context**: Read related documents thoroughly before editing
2. **Follow principles**: Apply KISS, YAGNI, DRY, SOLID to documentation
3. **Maintain structure**: Respect directory separation of concerns
4. **Update related files**: If changing KPIs, update both YAML and related docs
5. **Commit immediately**: Follow automated commit requirements

### Adding New Content

- **New theory**: Add to `docs/` with descriptive filename + date
- **New data**: Place in appropriate `data/` subdirectory with metadata
- **New lessons**: Create in `lesson/` following template format
- **New prototype**: Use `prototypes/` subdirectories

---

## Architecture Patterns

### Separation of Concerns

```
Layer                  Directory          Purpose
────────────────────────────────────────────────────────────────
Philosophical          docs/              Theory, framework, white papers
Practical              prototypes/        Proof-of-concepts, experiments
Metrics                kpi/, audit/       Measurable outcomes, validation
Evidence               data/              Research database, references
Governance             governance/        Rules, ethics, compliance
Meta-learning          lesson/            Knowledge capture
Publishing             style/, figs/      Output formats, visualizations
Community              .github/           Contribution paths, templates
```

### Document Hierarchy

```
Root README (overview)
    ↓
docs/implementation_roadmap.md (detailed plan)
    ↓
docs/实践指南.md (practical guide)
    ↓
Specific technical documents
```

---

## Special Notes for Claude Code

### When Editing Documents

- **Never use emojis** unless explicitly requested by user
- **Maintain bilingual parity**: If editing Chinese, consider updating English version
- **Preserve mathematical notation**: LaTeX-style equations are intentional
- **Keep temporal markers**: Don't remove date stamps from filenames
- **Respect formality**: This is academic research, maintain professional tone

### When Analyzing Structure

- This is **documentation-centric**, not code-centric
- "Build" means generating HTML/PDF, not compiling code
- "Testing" means peer review and checklist-based QA
- Focus on **content quality** over technical implementation

### When Committing

- **Always auto-commit** after task completion (per requirements)
- **Always auto-commit** before major destructive changes
- Use HEREDOC format for commit messages
- Include "🤖 Generated with Claude Code" footer
- Push to private repository at https://github.com/123olp/ys

### Understanding Success

Success for this project is measured in:
- Theoretical coherence and academic rigor
- Community building and knowledge dissemination
- Evidence database growth (entries in `data/`)
- Long-term sustainability (30-year horizon thinking)

**NOT** measured in:
- Lines of code written
- Features shipped
- User adoption metrics (it's not a product)

---

## License

CC BY 4.0 (Creative Commons Attribution 4.0) - All intellectual property is open by default.

---

**Last Updated**: 2025-10-18
**For Questions**: Refer to GitHub Issues or `CONTRIBUTING.md`
