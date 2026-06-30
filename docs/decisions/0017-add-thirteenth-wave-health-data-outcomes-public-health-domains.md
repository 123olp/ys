# 0017 Add Thirteenth Wave Health Data Outcomes Public Health Domains

Date: 2026-06-30

## Status

Accepted

## Context

The Research Domain Atlas now treats Human Infra as a map of subject-continuity conditions. Recent source signals show another set of conditions that cannot be safely collapsed into existing domains:

- health, genomic, behavioral, neural, and service-use data require privacy, consent, security, sharing, withdrawal, and use-boundary governance;
- interventions must be judged against functioning, quality of life, symptom burden, patient-reported outcomes, and subject-centered results;
- scarce medical and public resources require disease-burden, cost-effectiveness, HTA, budget-impact, equity, and value assessment language;
- individual immune resilience depends on immunization systems, infectious-disease surveillance, infection prevention, AMR governance, One Health, and wastewater signals;
- long-term subject capacity is shaped by maternal health, newborn health, child health, growth, nurturing care, and early development;
- medical systems need patient safety, team communication, incident learning, root-cause analysis, and organizational learning to prevent repeat harm.

These are not simply subtopics of `patient-data-interoperability/`, `measurement-feedback/`, `financial-resilience-access/`, `immune-maintenance/`, `reproductive-fertility-continuity/`, or `risk-engineering/`. Each has independent mechanisms, evidence systems, failure modes, and safety boundaries.

## Decision

Add six new domain skeletons:

- `domains/health-data-privacy-governance/`
- `domains/functioning-quality-of-life-outcomes/`
- `domains/health-economics-value-assessment/`
- `domains/immunization-public-health-surveillance/`
- `domains/maternal-newborn-child-development/`
- `domains/patient-safety-organizational-learning/`

Each domain starts with only `README.md` and `AGENTS.md`.

## Rationale

- Health data privacy governance determines whether Human Infra measurement remains a consented trust system rather than a surveillance or discrimination system.
- Functioning and quality-of-life outcomes determine whether the project optimizes real subject capability and lived burden rather than surrogate metrics alone.
- Health economics and value assessment determine how scarce resources, disease burden, cost, fairness, and rights enter anti-scarcity engineering.
- Immunization and public health surveillance determine whether infection, AMR, and outbreak risks are handled as system conditions rather than individual hygiene problems.
- Maternal, newborn, and child development determines how early-life conditions shape future subject capacity before adult self-optimization begins.
- Patient safety and organizational learning determine whether care systems learn from errors instead of repeatedly harming subjects.

## Boundaries

- No legal advice, compliance certification, PHI handling architecture, de-identification guarantee, privacy bypass, or sensitive data-sharing permission.
- No individual score interpretation, diagnosis, disability/benefit judgment, insurance judgment, or reduction of a person to a single outcome score.
- No investment, reimbursement, coverage, individual treatment, or resource-denial advice based on economic metrics.
- No vaccine medical advice, contraindication judgment, outbreak prediction guarantee, public-health evasion, pathogen handling, or surveillance misuse.
- No pregnancy, newborn, child medical advice, parenting prescription, family ranking, insurance screening, or family surveillance.
- No malpractice legal advice, blame assignment, institutional endorsement, punitive monitoring, or clinical operations guidance.

## Consequences

- Update root README, root AGENTS, `domains/README.md`, `domains/AGENTS.md`, domain map, atlas, radar, ethics boundaries, docs indexes, changelog, and repository structure checks.
- Keep the domains as documentation skeletons until source cards, variable contracts, or structured datasets justify additional files.
- Do not create data, scripts, apps, or empty pipeline folders for these domains in this slice.
