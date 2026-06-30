# Human Infra Documentation

This directory is organized as a documentation system, not as a dumping ground for notes.

It follows a Diataxis-style split:

- `tutorials/`: learning-oriented paths.
- `how-to/`: task-oriented procedures.
- `reference/`: factual maps, rules, standards, and stable lookup material.
- `explanations/`: understanding-oriented essays and conceptual models.

## Current Map

```text
docs/
├── README.md
├── AGENTS.md
├── decisions/
│   ├── 0001-adopt-docs-as-code-knowledge-base-structure.md
│   ├── 0002-adopt-local-quality-gates.md
│   ├── 0003-add-future-waiting-domain.md
│   ├── 0004-add-cellular-reprogramming-domain.md
│   ├── 0005-establish-research-domain-atlas.md
│   ├── 0006-add-second-wave-research-domains.md
│   ├── 0007-add-third-wave-research-domains.md
│   ├── 0008-add-fourth-wave-molecular-maintenance-domains.md
│   ├── 0009-add-fifth-wave-external-technology-risk-domains.md
│   ├── 0010-add-sixth-wave-physiological-structural-maintenance-domains.md
│   ├── 0011-add-seventh-wave-homeostasis-choice-domains.md
│   ├── 0012-add-eighth-wave-agency-task-resource-domains.md
│   ├── 0013-add-ninth-wave-service-continuity-domains.md
│   ├── 0014-add-tenth-wave-basic-livelihood-risk-transfer-domains.md
│   ├── 0015-add-eleventh-wave-civic-safety-continuity-domains.md
│   ├── 0016-add-twelfth-wave-treatment-service-rights-domains.md
│   ├── 0017-add-thirteenth-wave-health-data-outcomes-public-health-domains.md
│   ├── 0018-add-fourteenth-wave-public-services-emergency-financial-workforce-domains.md
│   ├── 0019-add-fifteenth-wave-preparedness-literacy-workforce-burden-community-data-domains.md
│   ├── 0020-add-sixteenth-wave-education-research-standards-cyber-compute-clinical-translation-domains.md
│   ├── 0021-add-seventeenth-wave-geospatial-weather-building-manufacturing-procurement-one-health-domains.md
│   ├── 0022-add-eighteenth-wave-lab-blood-waste-radiation-chemical-critical-materials-domains.md
│   └── README.md
├── explanations/
│   ├── README.md
│   ├── effective-immortality-acceleration-flywheel.md
│   ├── human-runtime-infrastructure.md
│   ├── life-path-prediction-model.md
│   ├── noah-ark-genealogy.md
│   └── value-lenses.md
├── how-to/
│   ├── README.md
│   ├── add-domain.md
│   ├── add-source-note.md
│   ├── contribute-docs.md
│   ├── run-quality-checks.md
│   └── share-human-infra.md
├── reference/
│   ├── README.md
│   ├── applications-and-literature.md
│   ├── document-lifecycle.md
│   ├── domain-map.md
│   ├── evidence-policy.md
│   ├── ethics-and-safety-boundaries.md
│   ├── glossary.md
│   ├── life-path-prediction-model-contract.md
│   ├── life-path-prediction-model-governance.md
│   ├── project-boundary-v0.1.md
│   ├── repository-standards.md
│   ├── research-domain-atlas.md
│   ├── research-domain-radar.md
│   ├── research-model-visualization-toolkit.md
│   ├── review-checklists.md
│   ├── source-card-system.md
│   ├── source-management.md
│   └── writing-style-guide.md
├── source-notes/
│   ├── core-literature/
│   ├── 2026-06-28-effective-immortality-flywheel-automated-research-run.md
│   ├── 2026-06-28-effective-immortality-flywheel-derivation-package.md
│   ├── 2026-06-28-effective-immortality-flywheel-evidence-matrix.md
│   └── 2026-06-28-effective-immortality-flywheel-source-cards.md
├── templates/
│   ├── README.md
│   ├── decision-record.md
│   ├── domain-readme.md
│   ├── research-card.md
│   ├── reference-doc.md
│   └── source-note.md
└── tutorials/
    └── README.md
```

## Reading Order

1. Start with `../README.md`.
2. Read `reference/domain-map.md`.
3. Read `reference/ethics-and-safety-boundaries.md`.
4. Read `reference/evidence-policy.md`.
5. Read `reference/project-boundary-v0.1.md`.
6. Read `explanations/life-path-prediction-model.md`.
7. Read `reference/life-path-prediction-model-contract.md`.
8. Read `reference/life-path-prediction-model-governance.md`.
9. Read `reference/source-card-system.md`.
10. Read `explanations/noah-ark-genealogy.md`.
11. Read `explanations/value-lenses.md`.
12. Read `explanations/effective-immortality-acceleration-flywheel.md`.
13. Read `source-notes/2026-06-28-effective-immortality-flywheel-evidence-matrix.md`.
14. Read `source-notes/2026-06-28-effective-immortality-flywheel-derivation-package.md`.
15. Read `reference/applications-and-literature.md`.
16. Read `source-notes/core-literature/README.md`.
17. Read `reference/review-checklists.md`.
18. Read `explanations/human-runtime-infrastructure.md`.
19. Read `source-notes/2026-06-29-controllable-metric-waiting-room-hypothesis-revision-notes.md` if you are working on Future Waiting.
20. Read `reference/research-domain-atlas.md`.
21. Read `reference/research-domain-radar.md` before proposing a new domain.
22. Read `../domains/cellular-reprogramming/README.md` if you are working on cellular rejuvenation or epigenetic reprogramming.
23. Read `../domains/health-data-privacy-governance/README.md` if you are working on sensitive health, genomic, behavioral, neural, or service-use data.
24. Read `../domains/functioning-quality-of-life-outcomes/README.md` if you are defining whether a Human Infra intervention actually improves function or lived experience.
25. Read `../domains/health-economics-value-assessment/README.md` if you are working on disease burden, cost-effectiveness, HTA, or public-value framing.
26. Read `../domains/immunization-public-health-surveillance/README.md` if you are working on immunization, infectious-disease surveillance, infection prevention, AMR, or wastewater signals.
27. Read `../domains/maternal-newborn-child-development/README.md` if you are working on maternal, newborn, child health, growth, or early development.
28. Read `../domains/patient-safety-organizational-learning/README.md` if you are working on patient safety, incident learning, team communication, or care-system harm reduction.
29. Read `../domains/social-determinants-community-vulnerability/README.md` if you are working on social determinants, community vulnerability, environmental justice, local health estimates, or health-related social needs.
30. Read `../domains/public-service-design-accessibility/README.md` if you are working on public digital services, forms, accessibility, customer experience, or service task completion.
31. Read `../domains/emergency-alerts-communications/README.md` if you are working on public alerts, 911/NG911, weather radio, first-responder communications, or crisis communication channels.
32. Read `../domains/disaster-recovery-relief-continuity/README.md` if you are working on disaster recovery, individual assistance, shelters, recovery centers, disaster loans, or relief navigation.
33. Read `../domains/financial-inclusion-payment-systems/README.md` if you are working on accounts, payment systems, remittances, digital financial services, or consumer financial protection.
34. Read `../domains/workforce-employment-services/README.md` if you are working on employment services, workforce development, apprenticeships, occupational information, or job accommodation.
35. Read `../domains/household-emergency-preparedness-resilience/README.md` if you are working on household emergency plans, supplies, medication continuity, backup communication, documents, or special needs.
36. Read `../domains/media-information-literacy-public-libraries/README.md` if you are working on media and information literacy, public libraries, trusted information access, or community learning spaces.
37. Read `../domains/health-workforce-capacity/README.md` if you are working on health workforce supply, distribution, training, retention, workload, or shortage risk.
38. Read `../domains/administrative-burden-procedural-friction/README.md` if you are working on paperwork, proof burden, waiting, renewal, appeal, or procedural friction.
39. Read `../domains/community-health-workers-peer-support/README.md` if you are working on community health workers, peer support, navigators, trusted intermediaries, or referral follow-up.
40. Read `../domains/civic-data-open-government-transparency/README.md` if you are working on open data, public records, FOIA, performance data, metadata, accountability, or public feedback.
41. Read `../domains/education-access-lifelong-learning/README.md` if you are working on education access, adult learning, retraining, basic skills, digital learning, or lifelong learning.
42. Read `../domains/research-infrastructure-open-science-translation/README.md` if you are working on research infrastructure, open science, reproducibility, research data, funding, translational science, or knowledge diffusion.
43. Read `../domains/standards-metrology-quality-infrastructure/README.md` if you are working on standards, metrology, calibration, certification, quality infrastructure, conformity assessment, or interoperability.
44. Read `../domains/cybersecurity-resilience-critical-services/README.md` if you are working on cybersecurity, critical-service resilience, incident response, backup recovery, ransomware risk, or digital continuity.
45. Read `../domains/compute-data-center-ai-infrastructure/README.md` if you are working on compute, data centers, AI infrastructure, chips, energy, water, cloud access, or AI infrastructure governance.
46. Read `../domains/clinical-trials-regulatory-science-translation/README.md` if you are working on clinical trials, regulatory science, real-world evidence, safety monitoring, endpoints, or medical translation.
47. Read `../domains/geospatial-navigation-location-infrastructure/README.md` if you are working on geospatial data, maps, addressing, GPS/GNSS, geocoding, emergency location, or location infrastructure.
48. Read `../domains/weather-climate-observation-forecasting/README.md` if you are working on weather observation, forecasting, climate services, severe weather, or early warning inputs.
49. Read `../domains/building-fire-life-safety-codes/README.md` if you are working on building codes, fire safety, egress, smoke alarms, life safety, or resilient buildings.
50. Read `../domains/manufacturing-repair-capacity/README.md` if you are working on manufacturing, repair, maintenance, spare parts, local production, or critical equipment restoration.
51. Read `../domains/public-procurement-contracting-capacity/README.md` if you are working on public procurement, contracting, supplier management, emergency procurement, transparency, or contract delivery.
52. Read `../domains/animal-health-zoonotic-interface-one-health/README.md` if you are working on animal health, zoonotic risk, veterinary public health, One Health, livestock, wildlife, or animal-health surveillance.
53. Read `../domains/public-health-laboratory-diagnostic-capacity/README.md` if you are working on public health laboratories, diagnostic capacity, laboratory quality, specimen networks, or laboratory surge.
54. Read `../domains/blood-organ-tissue-biovigilance-transplantation/README.md` if you are working on blood supply, organ/tissue donation, transplantation systems, transfusion safety, or biovigilance.
55. Read `../domains/waste-management-hazardous-materials-continuity/README.md` if you are working on solid waste, hazardous waste, medical waste, disposal continuity, or circular material flows.
56. Read `../domains/radiation-nuclear-safety-protection/README.md` if you are working on radiation protection, nuclear safety, radiological monitoring, or radiological emergency governance.
57. Read `../domains/chemical-safety-poison-control-toxicology/README.md` if you are working on chemical safety, toxic exposure, poison centers, toxicology, or chemical risk communication.
58. Read `../domains/critical-minerals-materials-resilience/README.md` if you are working on critical minerals, strategic materials, material substitution, recycling, or upstream technology input resilience.
59. Enter a domain under `../domains/`.
