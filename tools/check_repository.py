#!/usr/bin/env python3
"""检查 Human Infra 知识仓库的基础结构。"""

from __future__ import annotations

import sys
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
    "AGENTS.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "LICENSE.md",
    "Makefile",
    "README.md",
    "SECURITY.md",
    "SUPPORT.md",
    "tools/AGENTS.md",
    ".github/AGENTS.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/check.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/documentation.yml",
    ".github/ISSUE_TEMPLATE/research-note.yml",
    ".github/ISSUE_TEMPLATE/data-pipeline.yml",
    "tools/README.md",
    "tools/arxiv_html_paper_tool.py",
    "tools/arxiv-html-paper/AGENTS.md",
    "tools/arxiv-html-paper/README.md",
    "tools/arxiv-html-paper/assets/static/browse/0.3.4/images/icons/apple-touch-icon.png",
    "tools/arxiv-html-paper/assets/static/browse/0.3.4/images/icons/safari-pinned-tab.svg",
    "tools/arxiv-html-paper/templates/PaperReaderLayout.astro",
    "tools/arxiv-html-paper/templates/paper.astro",
    "web/AGENTS.md",
    "web/README.md",
    "web/package.json",
    "web/astro.config.mjs",
    "web/src/layouts/PaperReaderLayout.astro",
    "web/src/layouts/ResearchLayout.astro",
    "web/src/pages/paper.astro",
    "web/src/pages/index.astro",
    "web/src/pages/book.astro",
    "web/src/pages/model.astro",
    "web/src/pages/research-standards.astro",
    "web/src/styles/global.css",
    "web/src/scripts/model-charts.js",
    "web/src/data/book-signals.json",
    "docs/README.md",
    "docs/AGENTS.md",
    "docs/decisions/README.md",
    "docs/decisions/0001-adopt-docs-as-code-knowledge-base-structure.md",
    "docs/decisions/0002-adopt-local-quality-gates.md",
    "docs/decisions/0003-add-future-waiting-domain.md",
    "docs/decisions/0004-add-cellular-reprogramming-domain.md",
    "docs/decisions/0005-establish-research-domain-atlas.md",
    "docs/decisions/0006-add-second-wave-research-domains.md",
    "docs/decisions/0007-add-third-wave-research-domains.md",
    "docs/decisions/0008-add-fourth-wave-molecular-maintenance-domains.md",
    "docs/decisions/0009-add-fifth-wave-external-technology-risk-domains.md",
    "docs/decisions/0010-add-sixth-wave-physiological-structural-maintenance-domains.md",
    "docs/decisions/0011-add-seventh-wave-homeostasis-choice-domains.md",
    "docs/decisions/0012-add-eighth-wave-agency-task-resource-domains.md",
    "docs/decisions/0013-add-ninth-wave-service-continuity-domains.md",
    "docs/decisions/0014-add-tenth-wave-basic-livelihood-risk-transfer-domains.md",
    "docs/decisions/0015-add-eleventh-wave-civic-safety-continuity-domains.md",
    "docs/explanations/README.md",
    "docs/how-to/README.md",
    "docs/how-to/add-domain.md",
    "docs/how-to/add-source-note.md",
    "docs/how-to/contribute-docs.md",
    "docs/how-to/run-quality-checks.md",
    "docs/how-to/share-human-infra.md",
    "docs/reference/README.md",
    "docs/reference/applications-and-literature.md",
    "docs/reference/arxiv-html-papers-toolchain.md",
    "docs/source-notes/README.md",
    "docs/templates/README.md",
    "docs/tutorials/README.md",
    "docs/reference/document-lifecycle.md",
    "docs/reference/domain-map.md",
    "docs/reference/evidence-policy.md",
    "docs/reference/ethics-and-safety-boundaries.md",
    "docs/reference/glossary.md",
    "docs/reference/project-boundary-v0.1.md",
    "docs/reference/repository-standards.md",
    "docs/reference/research-domain-atlas.md",
    "docs/reference/research-domain-radar.md",
    "docs/reference/review-checklists.md",
    "docs/reference/source-card-system.md",
    "docs/reference/source-management.md",
    "docs/reference/writing-style-guide.md",
    "docs/explanations/human-runtime-infrastructure.md",
    "docs/templates/decision-record.md",
    "docs/templates/domain-readme.md",
    "docs/templates/research-card.md",
    "docs/templates/reference-doc.md",
    "docs/templates/source-note.md",
    "domains/README.md",
    "domains/AGENTS.md",
    "domains/antimicrobial-resilience/README.md",
    "domains/antimicrobial-resilience/AGENTS.md",
    "domains/assistive-technology-access/README.md",
    "domains/assistive-technology-access/AGENTS.md",
    "domains/biostasis-cryopreservation/README.md",
    "domains/biostasis-cryopreservation/AGENTS.md",
    "domains/attention-executive-control/README.md",
    "domains/attention-executive-control/AGENTS.md",
    "domains/cancer-control/README.md",
    "domains/cancer-control/AGENTS.md",
    "domains/cardiovascular-resilience/README.md",
    "domains/cardiovascular-resilience/AGENTS.md",
    "domains/cellular-senescence-clearance/README.md",
    "domains/cellular-senescence-clearance/AGENTS.md",
    "domains/cellular-reprogramming/README.md",
    "domains/cellular-reprogramming/AGENTS.md",
    "domains/extracellular-matrix-glycation/README.md",
    "domains/extracellular-matrix-glycation/AGENTS.md",
    "domains/financial-resilience-access/README.md",
    "domains/financial-resilience-access/AGENTS.md",
    "domains/food-security-nutrition-access/README.md",
    "domains/food-security-nutrition-access/AGENTS.md",
    "domains/water-sanitation-hygiene-continuity/README.md",
    "domains/water-sanitation-hygiene-continuity/AGENTS.md",
    "domains/energy-access-resilience/README.md",
    "domains/energy-access-resilience/AGENTS.md",
    "domains/healthcare-access-continuity/README.md",
    "domains/healthcare-access-continuity/AGENTS.md",
    "domains/caregiving-long-term-care/README.md",
    "domains/caregiving-long-term-care/AGENTS.md",
    "domains/housing-built-environment-stability/README.md",
    "domains/housing-built-environment-stability/AGENTS.md",
    "domains/transportation-access-mobility/README.md",
    "domains/transportation-access-mobility/AGENTS.md",
    "domains/legal-identity-civil-registration/README.md",
    "domains/legal-identity-civil-registration/AGENTS.md",
    "domains/access-to-justice-legal-aid/README.md",
    "domains/access-to-justice-legal-aid/AGENTS.md",
    "domains/civic-participation-election-access/README.md",
    "domains/civic-participation-election-access/AGENTS.md",
    "domains/migration-displacement-humanitarian-continuity/README.md",
    "domains/migration-displacement-humanitarian-continuity/AGENTS.md",
    "domains/digital-inclusion-connectivity/README.md",
    "domains/digital-inclusion-connectivity/AGENTS.md",
    "domains/social-protection-benefits-delivery/README.md",
    "domains/social-protection-benefits-delivery/AGENTS.md",
    "domains/insurance-risk-transfer/README.md",
    "domains/insurance-risk-transfer/AGENTS.md",
    "domains/childcare-family-continuity/README.md",
    "domains/childcare-family-continuity/AGENTS.md",
    "domains/emergency-preparedness-response/README.md",
    "domains/emergency-preparedness-response/AGENTS.md",
    "domains/personal-safety-violence-prevention/README.md",
    "domains/personal-safety-violence-prevention/AGENTS.md",
    "domains/product-safety-recall-systems/README.md",
    "domains/product-safety-recall-systems/AGENTS.md",
    "domains/cognitive-augmentation/README.md",
    "domains/cognitive-augmentation/AGENTS.md",
    "domains/ai-agency-safety/README.md",
    "domains/ai-agency-safety/AGENTS.md",
    "domains/digital-identity-security/README.md",
    "domains/digital-identity-security/AGENTS.md",
    "domains/future-waiting/README.md",
    "domains/future-waiting/AGENTS.md",
    "domains/future-waiting/paths/black-hole-waiting-room.md",
    "domains/genomic-stability-dna-repair/README.md",
    "domains/genomic-stability-dna-repair/AGENTS.md",
    "domains/gastrointestinal-barrier-absorption/README.md",
    "domains/gastrointestinal-barrier-absorption/AGENTS.md",
    "domains/governance-rights/README.md",
    "domains/governance-rights/AGENTS.md",
    "domains/health-literacy-navigation/README.md",
    "domains/health-literacy-navigation/AGENTS.md",
    "domains/information-integrity-trust/README.md",
    "domains/information-integrity-trust/AGENTS.md",
    "domains/learning-skill-acquisition/README.md",
    "domains/learning-skill-acquisition/AGENTS.md",
    "domains/immune-maintenance/README.md",
    "domains/immune-maintenance/AGENTS.md",
    "domains/endocrine-hormonal-regulation/README.md",
    "domains/endocrine-hormonal-regulation/AGENTS.md",
    "domains/blood-oxygen-hemostasis/README.md",
    "domains/blood-oxygen-hemostasis/AGENTS.md",
    "domains/longevity-evidence/README.md",
    "domains/longevity-evidence/AGENTS.md",
    "domains/longevity-evidence/docs/README.md",
    "domains/fluid-electrolyte-acid-base-homeostasis/README.md",
    "domains/fluid-electrolyte-acid-base-homeostasis/AGENTS.md",
    "domains/measurement-feedback/README.md",
    "domains/measurement-feedback/AGENTS.md",
    "domains/lymphatic-glymphatic-clearance/README.md",
    "domains/lymphatic-glymphatic-clearance/AGENTS.md",
    "domains/mental-health-affective-stability/README.md",
    "domains/mental-health-affective-stability/AGENTS.md",
    "domains/disembodied-cns/README.md",
    "domains/disembodied-cns/AGENTS.md",
    "domains/memory-editing/README.md",
    "domains/memory-editing/AGENTS.md",
    "domains/microbiome-ecology/README.md",
    "domains/microbiome-ecology/AGENTS.md",
    "domains/mitochondrial-bioenergetics/README.md",
    "domains/mitochondrial-bioenergetics/AGENTS.md",
    "domains/musculoskeletal-integrity/README.md",
    "domains/musculoskeletal-integrity/AGENTS.md",
    "domains/neuro-continuity/README.md",
    "domains/neuro-continuity/AGENTS.md",
    "domains/nutrition-metabolic-health/README.md",
    "domains/nutrition-metabolic-health/AGENTS.md",
    "domains/oral-health-continuity/README.md",
    "domains/oral-health-continuity/AGENTS.md",
    "domains/occupational-work-design/README.md",
    "domains/occupational-work-design/AGENTS.md",
    "domains/pain-suffering-control/README.md",
    "domains/pain-suffering-control/AGENTS.md",
    "domains/physical-activity-mobility/README.md",
    "domains/physical-activity-mobility/AGENTS.md",
    "domains/planetary-health-environment/README.md",
    "domains/planetary-health-environment/AGENTS.md",
    "domains/proteostasis-autophagy/README.md",
    "domains/proteostasis-autophagy/AGENTS.md",
    "domains/regenerative-medicine/README.md",
    "domains/regenerative-medicine/AGENTS.md",
    "domains/rehabilitation-functioning/README.md",
    "domains/rehabilitation-functioning/AGENTS.md",
    "domains/reproductive-fertility-continuity/README.md",
    "domains/reproductive-fertility-continuity/AGENTS.md",
    "domains/renal-hepatic-clearance/README.md",
    "domains/renal-hepatic-clearance/AGENTS.md",
    "domains/respiratory-oxygenation/README.md",
    "domains/respiratory-oxygenation/AGENTS.md",
    "domains/resource-social-infra/README.md",
    "domains/resource-social-infra/AGENTS.md",
    "domains/risk-engineering/README.md",
    "domains/risk-engineering/AGENTS.md",
    "domains/sensory-continuity/README.md",
    "domains/sensory-continuity/AGENTS.md",
    "domains/sleep-circadian-recovery/README.md",
    "domains/sleep-circadian-recovery/AGENTS.md",
    "domains/skin-barrier-wound-healing/README.md",
    "domains/skin-barrier-wound-healing/AGENTS.md",
    "domains/social-connection-relational-infra/README.md",
    "domains/social-connection-relational-infra/AGENTS.md",
    "domains/stem-cell-reserve-renewal/README.md",
    "domains/stem-cell-reserve-renewal/AGENTS.md",
    "domains/substance-exposure-control/README.md",
    "domains/substance-exposure-control/AGENTS.md",
    "domains/supply-chain-continuity/README.md",
    "domains/supply-chain-continuity/AGENTS.md",
    "domains/synthetic-biology-biosecurity/README.md",
    "domains/synthetic-biology-biosecurity/AGENTS.md",
    "domains/space-extreme-habitation/README.md",
    "domains/space-extreme-habitation/AGENTS.md",
    "domains/thermal-homeostasis-resilience/README.md",
    "domains/thermal-homeostasis-resilience/AGENTS.md",
    "domains/time-allocation-effective-time/README.md",
    "domains/time-allocation-effective-time/AGENTS.md",
    "domains/urogenital-continuity/README.md",
    "domains/urogenital-continuity/AGENTS.md",
    "domains/telomere-maintenance/README.md",
    "domains/telomere-maintenance/AGENTS.md",
]

REQUIRED_DIRS = [
    ".github/ISSUE_TEMPLATE",
    ".github/workflows",
    "docs/decisions",
    "docs/explanations",
    "docs/how-to",
    "docs/reference",
    "docs/source-notes",
    "docs/templates",
    "docs/tutorials",
    "domains/antimicrobial-resilience",
    "domains/assistive-technology-access",
    "domains/biostasis-cryopreservation",
    "domains/cancer-control",
    "domains/cardiovascular-resilience",
    "domains/cellular-senescence-clearance",
    "domains/cellular-reprogramming",
    "domains/extracellular-matrix-glycation",
    "domains/cognitive-augmentation",
    "domains/ai-agency-safety",
    "domains/digital-identity-security",
    "domains/future-waiting",
    "domains/future-waiting/paths",
    "domains/fluid-electrolyte-acid-base-homeostasis",
    "domains/food-security-nutrition-access",
    "domains/water-sanitation-hygiene-continuity",
    "domains/energy-access-resilience",
    "domains/healthcare-access-continuity",
    "domains/caregiving-long-term-care",
    "domains/housing-built-environment-stability",
    "domains/transportation-access-mobility",
    "domains/legal-identity-civil-registration",
    "domains/access-to-justice-legal-aid",
    "domains/civic-participation-election-access",
    "domains/migration-displacement-humanitarian-continuity",
    "domains/digital-inclusion-connectivity",
    "domains/social-protection-benefits-delivery",
    "domains/insurance-risk-transfer",
    "domains/childcare-family-continuity",
    "domains/emergency-preparedness-response",
    "domains/personal-safety-violence-prevention",
    "domains/product-safety-recall-systems",
    "domains/genomic-stability-dna-repair",
    "domains/gastrointestinal-barrier-absorption",
    "domains/governance-rights",
    "domains/health-literacy-navigation",
    "domains/immune-maintenance",
    "domains/endocrine-hormonal-regulation",
    "domains/blood-oxygen-hemostasis",
    "domains/measurement-feedback",
    "domains/lymphatic-glymphatic-clearance",
    "domains/mental-health-affective-stability",
    "domains/microbiome-ecology",
    "domains/mitochondrial-bioenergetics",
    "domains/musculoskeletal-integrity",
    "domains/neuro-continuity",
    "domains/nutrition-metabolic-health",
    "domains/oral-health-continuity",
    "domains/pain-suffering-control",
    "domains/physical-activity-mobility",
    "domains/planetary-health-environment",
    "domains/proteostasis-autophagy",
    "domains/regenerative-medicine",
    "domains/rehabilitation-functioning",
    "domains/reproductive-fertility-continuity",
    "domains/renal-hepatic-clearance",
    "domains/respiratory-oxygenation",
    "domains/resource-social-infra",
    "domains/risk-engineering",
    "domains/sensory-continuity",
    "domains/sleep-circadian-recovery",
    "domains/social-connection-relational-infra",
    "domains/skin-barrier-wound-healing",
    "domains/stem-cell-reserve-renewal",
    "domains/substance-exposure-control",
    "domains/supply-chain-continuity",
    "domains/synthetic-biology-biosecurity",
    "domains/space-extreme-habitation",
    "domains/thermal-homeostasis-resilience",
    "domains/urogenital-continuity",
    "domains/telomere-maintenance",
    "domains",
    "tools",
    "tools/arxiv-html-paper",
    "tools/arxiv-html-paper/assets",
    "tools/arxiv-html-paper/assets/static/browse/0.3.4/images/icons",
    "tools/arxiv-html-paper/templates",
    "web",
    "web/public",
    "web/src",
    "web/src/components",
    "web/src/data",
    "web/src/layouts",
    "web/src/pages",
    "web/src/scripts",
    "web/src/styles",
]

FORBIDDEN_NAME_PARTS = [
    "新建 文本文档",
]

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
IGNORED_LINK_PREFIXES = (
    "#",
    "http://",
    "https://",
    "mailto:",
)


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def iter_markdown_without_code(path: Path) -> list[tuple[int, str]]:
    lines: list[tuple[int, str]] = []
    in_fence = False
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            lines.append((lineno, line))
    return lines


def check_local_markdown_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        rel = relative(path)
        if rel.startswith((".history/", "node_modules/", "web/node_modules/", "web/dist/", "web/.observablehq/", "web/src/.observablehq/")):
            continue
        for lineno, line in iter_markdown_without_code(path):
            for match in MARKDOWN_LINK_RE.finditer(line):
                target = match.group(1).strip()
                if target.startswith("<") and target.endswith(">"):
                    target = target[1:-1]
                if target.startswith(IGNORED_LINK_PREFIXES):
                    continue
                target_path = target.split("#", 1)[0]
                if not target_path:
                    continue
                resolved = (path.parent / target_path).resolve()
                try:
                    resolved.relative_to(ROOT)
                except ValueError:
                    errors.append(f"markdown link escapes repository: {rel}:{lineno}: {target}")
                    continue
                if not resolved.exists():
                    errors.append(f"broken markdown link: {rel}:{lineno}: {target}")


def main() -> int:
    errors: list[str] = []

    for name in REQUIRED_FILES:
        path = ROOT / name
        if not path.is_file():
            errors.append(f"missing file: {name}")

    for name in REQUIRED_DIRS:
        path = ROOT / name
        if not path.is_dir():
            errors.append(f"missing directory: {name}")

    for path in ROOT.rglob("*"):
        rel = relative(path)
        if rel.startswith(("node_modules/", "web/node_modules/", "web/dist/", "web/.observablehq/", "web/src/.observablehq/")):
            continue
        if any(part in rel for part in FORBIDDEN_NAME_PARTS):
            if ".history/" not in rel:
                errors.append(f"temporary filename still active: {rel}")
        if path.is_dir() and path.name == "__pycache__":
            errors.append(f"python cache directory present: {rel}")

    check_local_markdown_links(errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("repository structure ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
