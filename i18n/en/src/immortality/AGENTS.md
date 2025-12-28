# AI Agent Repository Guidelines

This document serves as an **Operating Manual** for AI agents contributing to this repository.

**Last Updated**: 2025-12-28  
**Repository**: https://github.com/tukuaiai/immortality

---

## 1. Mission & Scope

### Allowed Actions
- Create/edit Markdown documentation in `i18n/` directories
- Update `README.md`, `AGENTS.md`, `CONTRIBUTING.md`
- Add new documents following naming conventions
- Fix broken links and formatting issues
- Update `Makefile` SRC_FILES when adding/removing documents

### Prohibited Actions
- ❌ Modify `LICENSE` without explicit approval
- ❌ Edit files in `backups/` directory
- ❌ Commit secrets, API keys, or PII
- ❌ Delete `archives/` content without approval
- ❌ Modify `.github/FUNDING.yml`
- ❌ Large-scale refactoring without task requirement

### Sensitive Areas (Do Not Modify)
| Path | Reason |
|:---|:---|
| `backups/` | Backup data, read-only |
| `LICENSE` | Legal document |
| `.github/FUNDING.yml` | Funding configuration |
| `*.gz`, `*.tar.gz` | Compressed archives |

---

## 2. Golden Path (Standard Workflow)

```bash
# 1. Clone & enter project
git clone https://github.com/tukuaiai/immortality.git
cd immortality

# 2. Verify build environment
make clean
make all

# 3. Make changes to documentation

# 4. Rebuild and verify
make clean && make html
# Inspect out/report.html

# 5. Update AGENTS.md & README.md if structure changed

# 6. Commit with clear message
git add .
git commit -m "docs: update [specific change]"
```

---

## 3. Must-Run Commands

| Command | Purpose | Prerequisites |
|:---|:---|:---|
| `make all` | Build HTML + PDF | `pandoc`, `texlive-xetex`, `Noto Sans CJK SC` font |
| `make html` | Build HTML only | `pandoc` |
| `make pdf` | Build PDF only | `pandoc`, `texlive-xetex` |
| `make clean` | Remove `out/` directory | None |

### Build Verification
A change is successful if:
1. `make html` completes without errors
2. `out/report.html` renders correctly

---

## 4. Code Change Rules

### Architecture Principles
- This is a **documentation-as-code** project with i18n support
- All content documents go under `i18n/{lang}/`
- Root-level files are project metadata only

### Document Naming Convention
- Use English with `_` separator: `human_3.0_technical_blueprint.md`
- Academic versions: append `_academic` suffix: `human_3.0_technical_blueprint_academic.md`
- Keep names consistent across language directories

### Adding New Documents
1. Create file in appropriate `i18n/{lang}/docs/{category}/` directory
2. Add to `Makefile` SRC_FILES if it should be included in build
3. Update README.md document navigation table
4. Update this file's Project Map if adding new directories

### Dependency Rules
- No runtime dependencies (pure documentation project)
- Build dependencies: `make`, `pandoc`, `texlive-xetex`

---

## 5. Style & Quality

### Markdown Standards
- Use GitHub Flavored Markdown (GFM)
- ATX headings (`#`) with logical hierarchy
- Code blocks with language annotation
- Tables must be aligned

### File Formats
| Type | Format | Indentation |
|:---|:---|:---|
| Markdown | GFM | N/A |
| YAML | Standard | 2 spaces |
| Makefile | GNU Make | Tabs (required) |

### Naming Conventions
- Files: `snake_case.md`
- Directories: `lowercase`
- No spaces in filenames

---

## 6. Project Map

```
immortality/
├── README.md              # Multi-language entry (root)
├── AGENTS.md              # This file (Agent guidelines)
├── CONTRIBUTING.md        # Human contribution guide
├── CODE_OF_CONDUCT.md     # Community standards
├── LICENSE                # CC BY 4.0
├── Makefile               # Build automation
├── metadata.yaml          # Pandoc metadata
│
├── i18n/
│   ├── en/                # English docs
│   │   ├── README.md
│   │   ├── README_academic.md
│   │   ├── human_3.0_technical_blueprint.md
│   │   ├── human_3.0_technical_blueprint_academic.md
│   │   └── immortality_roadmap.md
│   │
│   └── zh/                # Chinese docs
│       ├── README.md
│       ├── README_academic.md
│       ├── docs/
│       │   ├── core/      # Core theory documents
│       │   ├── guides/    # Accessible guides
│       │   ├── philosophy/# Philosophical discussions
│       │   └── system_architecture.mmd
│       ├── archives/      # Historical documents (read-only)
│       └── data/          # Templates & references
│
└── .github/               # GitHub templates
```

### Key Entry Points
| File | Purpose |
|:---|:---|
| `README.md` | Project overview, navigation |
| `Makefile` | Build commands, source file list |
| `metadata.yaml` | Pandoc build metadata |
| `i18n/zh/docs/core/human_3.0_technical_blueprint.md` | Main technical document |

---

## 7. Common Pitfalls

### Makefile Tab Requirement
**Problem**: Build fails with "missing separator" error.

**Cause**: Makefile recipes use spaces instead of tabs.

**Fix**: All recipe lines must use literal tab characters.

### Chinese Font Missing
**Problem**: PDF build fails with font errors.

**Fix**: Install `Noto Sans CJK SC` font:
```bash
# Ubuntu/Debian
sudo apt install fonts-noto-cjk
```

---

## 8. PR / Commit Rules

### Commit Message Format
```
<type>: <short description>

[optional body]
```

**Types**: `docs`, `fix`, `chore`, `refactor`

**Examples**:
- `docs: add emotion modeling academic version`
- `fix: correct broken link in README`
- `chore: update Makefile source list`

### Branch Strategy
- Work on feature branches: `feature/<name>` or `docs/<name>`
- PR to `main` branch
- Link related issues: `Fixes #123`

### CI Behavior
- TODO: No CI workflow currently configured in `.github/workflows/`

---

## 9. Documentation Sync Rule

**MANDATORY**: Any change to the following must trigger documentation update:

| Change Type | Update Required |
|:---|:---|
| New document added | README.md navigation, Makefile SRC_FILES, AGENTS.md Project Map |
| Document renamed/moved | README.md links, Makefile SRC_FILES |
| Directory structure changed | README.md structure, AGENTS.md Project Map |
| Build command changed | README.md build section, AGENTS.md commands |
| New dependency added | README.md requirements, AGENTS.md prerequisites |

**If uncertain**: Add `TODO` with specific file/path needed for confirmation. Never guess.

---

## 10. Quick Reference

```bash
# Verify build works
make clean && make html

# Check for missing files referenced in Makefile
for f in $(grep -E '\.md' Makefile | grep -v '#'); do [ -f "$f" ] || echo "MISSING: $f"; done

# List all markdown files
find i18n -name "*.md" -type f

# Check document links (manual)
grep -r "\](./" i18n/ | head -20
```
