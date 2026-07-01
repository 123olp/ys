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
│   ├── 0023-add-nineteenth-wave-air-food-occupational-device-sterilization-accessibility-domains.md
│   ├── 0024-add-twentieth-wave-clinical-drug-ems-surgical-road-safety-domains.md
│   ├── 0025-add-twenty-first-wave-rural-homelessness-correctional-disability-dementia-infectious-continuity-domains.md
│   ├── 0026-add-twenty-second-wave-crisis-exploitation-recovery-domains.md
│   ├── 0027-add-twenty-third-wave-complex-care-navigation-transition-decision-domains.md
│   ├── 0028-add-twenty-fourth-wave-externalized-subject-continuity-domains.md
│   ├── 0029-add-twenty-fifth-wave-civilizational-continuity-collective-security-domains.md
│   ├── 0030-add-twenty-sixth-wave-primary-production-natural-systems-logistics-domains.md
│   ├── 0031-add-twenty-seventh-wave-coastal-civil-urban-infrastructure-domains.md
│   ├── 0032-add-twenty-eighth-wave-utility-lifeline-continuity-domains.md
│   ├── 0033-add-twenty-ninth-wave-biomedical-platform-domains.md
│   ├── 0034-add-thirtieth-wave-quantitative-methodology-domains.md
│   ├── 0035-add-thirty-first-wave-knowledge-governance-technology-diffusion-domains.md
│   ├── 0036-add-thirty-second-wave-research-evidence-infrastructure-domains.md
│   ├── 0037-add-thirty-third-wave-future-technology-continuity-domains.md
│   ├── 0038-add-thirty-fourth-wave-acute-neuro-continuity-domains.md
│   ├── 0039-add-thirty-fifth-wave-sensory-communication-continuity-domains.md
│   ├── 0040-add-thirty-sixth-wave-planetary-geophysical-heat-risk-domains.md
│   ├── 0041-add-thirty-seventh-wave-chronic-environmental-exposure-domains.md
│   ├── 0042-add-thirty-eighth-wave-decision-authority-fiduciary-continuity-domains.md
│   ├── 0043-add-thirty-ninth-wave-algorithmic-access-screening-domains.md
│   ├── 0044-add-fortieth-wave-credential-licensure-continuity-domains.md
│   ├── 0045-add-forty-first-wave-income-entitlement-record-continuity-domains.md
│   ├── 0046-add-forty-second-wave-work-interruption-care-continuity-domains.md
│   ├── 0047-add-forty-third-wave-life-event-household-record-continuity-domains.md
│   ├── 0048-add-forty-fourth-wave-asset-account-transaction-continuity-domains.md
│   ├── 0049-add-forty-fifth-wave-legal-status-coercive-process-continuity-domains.md
│   ├── 0050-add-forty-sixth-wave-school-service-continuity-domains.md
│   ├── 0051-add-forty-seventh-wave-postsecondary-student-continuity-domains.md
│   ├── 0052-add-forty-eighth-wave-digital-account-continuity-domains.md
│   ├── 0053-add-forty-ninth-wave-software-device-trust-continuity-domains.md
│   ├── 0054-add-fiftieth-wave-personal-operations-continuity-domains.md
│   ├── 0055-add-fifty-first-wave-household-operations-continuity-domains.md
│   ├── 0056-add-fifty-second-wave-personal-mobility-execution-continuity-domains.md
│   ├── 0057-add-fifty-third-wave-public-realm-survival-access-continuity-domains.md
│   ├── 0058-add-fifty-fourth-wave-food-acquisition-execution-continuity-domains.md
│   ├── 0059-add-fifty-fifth-wave-treatment-execution-medical-supply-continuity-domains.md
│   ├── 0060-add-fifty-sixth-wave-outpatient-access-clinical-service-execution-domains.md
│   ├── 0061-add-fifty-seventh-wave-medical-payment-billing-cost-protection-domains.md
│   ├── 0062-add-fifty-eighth-wave-patient-rights-records-communication-domains.md
│   ├── 0063-add-fifty-ninth-wave-emergency-health-handoff-domains.md
│   ├── 0064-add-sixtieth-wave-post-death-survivor-continuity-domains.md
│   ├── 0065-add-sixty-first-wave-relational-social-capital-continuity-domains.md
│   ├── 0066-add-sixty-second-wave-meaning-culture-identity-continuity-domains.md
│   ├── 0067-add-sixty-third-wave-human-factors-operational-reliability-domains.md
│   ├── 0068-add-sixty-fourth-wave-mental-health-neurodevelopment-functioning-domains.md
│   ├── 0069-add-sixty-fifth-wave-companion-service-animal-continuity-domains.md
│   ├── 0070-add-sixty-sixth-wave-travel-lodging-border-continuity-domains.md
│   ├── 0071-add-sixty-seventh-wave-consumer-transaction-continuity-domains.md
│   ├── 0072-add-sixty-eighth-wave-consumer-credit-lending-continuity-domains.md
│   ├── 0073-add-sixty-ninth-wave-personal-insurance-claims-continuity-domains.md
│   ├── 0074-add-seventieth-wave-victim-safety-recovery-continuity-domains.md
│   ├── 0075-add-seventy-first-wave-housing-tenure-stability-continuity-domains.md
│   ├── 0076-add-seventy-second-wave-court-access-procedure-continuity-domains.md
│   ├── 0077-add-seventy-third-wave-personal-data-privacy-continuity-domains.md
│   ├── 0078-add-seventy-fourth-wave-digital-content-trust-continuity-domains.md
│   ├── 0079-add-seventy-fifth-wave-intellectual-property-digital-rights-continuity-domains.md
│   ├── 0080-add-seventy-sixth-wave-research-identity-reproducibility-infrastructure-domains.md
│   ├── 0081-add-seventy-seventh-wave-evidence-synthesis-guideline-translation-domains.md
│   ├── 0082-add-seventy-eighth-wave-research-correction-scientific-integrity-domains.md
│   ├── 0083-add-seventy-ninth-wave-ai-evaluation-operations-governance-domains.md
│   ├── 0084-add-eightieth-wave-compute-energy-connectivity-substrate-domains.md
│   ├── 0085-add-eighty-first-wave-acute-rescue-organ-support-domains.md
│   ├── 0086-add-eighty-second-wave-acute-internal-medicine-emergency-domains.md
│   ├── 0087-add-eighty-third-wave-preventive-risk-factor-control-domains.md
│   ├── 0088-add-eighty-fourth-wave-life-course-preventive-continuity-domains.md
│   ├── 0089-add-eighty-fifth-wave-chronic-specialty-burden-continuity-domains.md
│   ├── 0090-add-eighty-sixth-wave-chronic-neuro-neuromuscular-post-infectious-continuity-domains.md
│   ├── 0091-add-eighty-seventh-wave-organ-specific-cancer-continuity-domains.md
│   ├── 0092-add-eighty-eighth-wave-oral-dental-jaw-function-continuity-domains.md
│   ├── 0093-add-eighty-ninth-wave-eye-disease-visual-function-continuity-domains.md
│   ├── 0094-add-ninetieth-wave-auditory-communication-execution-continuity-domains.md
│   ├── 0095-add-ninety-first-wave-vestibular-balance-execution-continuity-domains.md
│   ├── 0096-add-ninety-second-wave-speech-language-communication-execution-domains.md
│   ├── 0097-add-ninety-third-wave-swallowing-feeding-execution-domains.md
│   ├── 0098-add-ninety-fourth-wave-urinary-renal-replacement-continuity-domains.md
│   ├── 0099-add-ninety-fifth-wave-skin-wound-barrier-continuity-domains.md
│   ├── 0100-add-ninety-sixth-wave-home-injury-domestic-safety-continuity-domains.md
│   ├── 0101-add-ninety-seventh-wave-child-recreation-injury-prevention-domains.md
│   ├── 0102-add-ninety-eighth-wave-household-personal-emergency-preparedness-domains.md
│   ├── 0103-add-ninety-ninth-wave-disaster-recovery-execution-continuity-domains.md
│   ├── 0104-add-one-hundredth-wave-infectious-disease-outbreak-response-execution-domains.md
│   ├── 0105-add-one-hundred-first-wave-hazardous-materials-industrial-incident-execution-domains.md
│   ├── 0106-establish-transcendental-domain-index.md
│   ├── 0107-add-one-hundred-second-wave-severe-weather-hazard-execution-domains.md
│   ├── 0108-add-one-hundred-third-wave-vector-animal-pest-exposure-execution-domains.md
│   ├── 0109-add-one-hundred-fourth-wave-plant-algae-fungi-outdoor-biological-exposure-domains.md
│   ├── 0110-add-one-hundred-fifth-wave-personal-device-consumable-continuity-domains.md
│   ├── 0111-add-one-hundred-sixth-wave-assistive-device-operational-continuity-domains.md
│   ├── 0112-add-one-hundred-seventh-wave-household-water-wastewater-execution-domains.md
│   ├── 0113-add-one-hundred-eighth-wave-household-energy-thermal-safety-domains.md
│   ├── 0114-add-one-hundred-ninth-wave-household-waste-disposal-execution-domains.md
│   ├── 0115-add-one-hundred-tenth-wave-household-indoor-air-ventilation-execution-domains.md
│   ├── 0116-add-one-hundred-eleventh-wave-household-physical-order-object-access-domains.md
│   ├── 0117-add-one-hundred-twelfth-wave-household-operating-metadata-handoff-domains.md
│   ├── 0118-add-one-hundred-thirteenth-wave-neighborhood-public-space-maintenance-service-request-domains.md
│   ├── 0119-add-one-hundred-fourteenth-wave-early-child-care-execution-domains.md
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
│   ├── transcendental-domain-index.md
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
1. Read `reference/domain-map.md`.
2. Read `reference/ethics-and-safety-boundaries.md`.
3. Read `reference/evidence-policy.md`.
4. Read `reference/project-boundary-v0.1.md`.
5. Read `explanations/life-path-prediction-model.md`.
6. Read `reference/life-path-prediction-model-contract.md`.
7. Read `reference/life-path-prediction-model-governance.md`.
8. Read `reference/source-card-system.md`.
9. Read `explanations/noah-ark-genealogy.md`.
10. Read `explanations/value-lenses.md`.
11. Read `explanations/effective-immortality-acceleration-flywheel.md`.
12. Read `source-notes/2026-06-28-effective-immortality-flywheel-evidence-matrix.md`.
13. Read `source-notes/2026-06-28-effective-immortality-flywheel-derivation-package.md`.
14. Read `reference/applications-and-literature.md`.
15. Read `source-notes/core-literature/README.md`.
16. Read `reference/review-checklists.md`.
17. Read `explanations/human-runtime-infrastructure.md`.
18. Read `source-notes/2026-06-29-controllable-metric-waiting-room-hypothesis-revision-notes.md` if you are working on Future Waiting.
19. Read `reference/transcendental-domain-index.md` before turning effective-immortality ideas into domain work.
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
53. Read `../domains/human-animal-bond-companion-care-continuity/README.md` if you are working on companion animals, human-animal bond, pet care routines, family rhythms, or relationship support.
54. Read `../domains/veterinary-care-access-cost-continuity/README.md` if you are working on veterinary access, veterinary cost, emergency veterinary care, low-cost clinics, or animal-care service continuity.
55. Read `../domains/service-animal-disability-access-continuity/README.md` if you are working on service animals, disability access, task assistance, handler rights, or public participation.
56. Read `../domains/pet-identification-microchip-reunification-continuity/README.md` if you are working on pet identification, microchips, tags, registration, lost pets, or reunification systems.
57. Read `../domains/pet-food-medication-supply-safety-continuity/README.md` if you are working on pet food, animal drugs, veterinary prescriptions, recalls, labeling, or supply interruptions.
58. Read `../domains/pet-disaster-evacuation-sheltering-continuity/README.md` if you are working on pets in disasters, evacuation, sheltering, pet supplies, service animals, or post-disaster reunification.
59. Read `../domains/animal-shelter-rescue-rehoming-continuity/README.md` if you are working on animal shelters, rescue, foster care, adoption, rehoming, or owner reunification.
60. Read `../domains/animal-welfare-cruelty-reporting-continuity/README.md` if you are working on animal welfare, cruelty, neglect, hoarding, abandonment, reporting pathways, or humane-law interfaces.
61. Read `../domains/public-health-laboratory-diagnostic-capacity/README.md` if you are working on public health laboratories, diagnostic capacity, laboratory quality, specimen networks, or laboratory surge.
62. Read `../domains/blood-organ-tissue-biovigilance-transplantation/README.md` if you are working on blood supply, organ/tissue donation, transplantation systems, transfusion safety, or biovigilance.
63. Read `../domains/waste-management-hazardous-materials-continuity/README.md` if you are working on solid waste, hazardous waste, medical waste, disposal continuity, or circular material flows.
64. Read `../domains/radiation-nuclear-safety-protection/README.md` if you are working on radiation protection, nuclear safety, radiological monitoring, or radiological emergency governance.
65. Read `../domains/chemical-safety-poison-control-toxicology/README.md` if you are working on chemical safety, toxic exposure, poison centers, toxicology, or chemical risk communication.
66. Read `../domains/critical-minerals-materials-resilience/README.md` if you are working on critical minerals, strategic materials, material substitution, recycling, or upstream technology input resilience.
67. Read `../domains/air-quality-ventilation-exposure-control/README.md` if you are working on air quality, ventilation, filtration, aerosols, smoke, or inhaled exposure control.
68. Read `../domains/food-safety-contamination-control/README.md` if you are working on foodborne hazards, contamination, inspection, traceability, recalls, or outbreak governance.
69. Read `../domains/occupational-exposure-industrial-hygiene/README.md` if you are working on industrial hygiene, workplace exposure, hierarchy of controls, dust, noise, heat, chemicals, or biological hazards.
70. Read `../domains/medical-device-equipment-safety-maintenance/README.md` if you are working on medical device safety, equipment lifecycle, UDI, adverse events, recalls, maintenance, or device cybersecurity.
71. Read `../domains/sterilization-disinfection-infection-control/README.md` if you are working on sterilization, disinfection, reprocessing, environmental infection control, or healthcare-associated infection prevention.
72. Read `../domains/built-environment-accessibility-universal-design/README.md` if you are working on built-environment accessibility, universal design, ADA/ABA standards, public-space access, or physical-path continuity.
73. Read `../domains/clinical-laboratory-diagnostic-quality/README.md` if you are working on clinical laboratory quality, diagnostic testing, CLIA, test reliability, diagnostic stewardship, or lab result quality.
74. Read `../domains/pharmacovigilance-drug-safety-monitoring/README.md` if you are working on pharmacovigilance, adverse event reports, FAERS, postmarket drug safety, labels, REMS, or medication safety signals.
75. Read `../domains/pharmaceutical-quality-supply-integrity/README.md` if you are working on pharmaceutical quality, GMP, substandard/falsified medicines, drug shortages, cold chain, traceability, or supply integrity.
76. Read `../domains/emergency-medical-services-prehospital-care/README.md` if you are working on EMS, prehospital care, dispatch, response time, ambulance systems, or time-critical acute response.
77. Read `../domains/surgical-anesthesia-perioperative-safety/README.md` if you are working on surgical safety, anesthesia safety, perioperative quality, surgical checklist, or preventable surgical complications.
78. Read `../domains/road-traffic-injury-prevention-safe-mobility/README.md` if you are working on road traffic injury prevention, safe system, speed management, vehicle safety, or safe mobility.
79. Read `../domains/rural-health-access-geographic-equity/README.md` if you are working on rural health, geographic access, rural workforce, hospital/pharmacy closure, telehealth, EMS distance, or rural equity.
80. Read `../domains/homelessness-unsheltered-health-continuity/README.md` if you are working on homelessness, unsheltered health, shelters, street outreach, housing continuity, hygiene, safety, or service access.
81. Read `../domains/correctional-health-reentry-continuity/README.md` if you are working on correctional health, incarceration, jail/prison healthcare, reentry, medication continuity, Medicaid transition, or release planning systems.
82. Read `../domains/disability-services-independent-living/README.md` if you are working on disability services, independent living, HCBS, personal assistance, reasonable accommodation, assistive technology, or community integration.
83. Read `../domains/dementia-cognitive-decline-care-continuity/README.md` if you are working on dementia, cognitive decline, Alzheimer’s, caregiver burden, dementia care continuity, safety, dignity, or service navigation.
84. Read `../domains/chronic-infectious-disease-care-continuity/README.md` if you are working on HIV, TB, viral hepatitis, long-course infectious disease care, treatment continuity, stigma, drug resistance, or public-health follow-up.
85. Read `../domains/suicide-crisis-response-continuity/README.md` if you are working on suicide prevention, 988, crisis response, mobile crisis teams, crisis stabilization, follow-up care, or suicide-risk service systems.
86. Read `../domains/substance-use-treatment-recovery-continuity/README.md` if you are working on substance use disorder treatment, recovery support, overdose prevention, harm reduction governance, peer support, or treatment continuity.
87. Read `../domains/elder-justice-adult-protective-services/README.md` if you are working on elder abuse, Adult Protective Services, elder justice, financial exploitation, neglect, or long-term-care ombudsman systems.
88. Read `../domains/child-protection-family-safety/README.md` if you are working on child protection, child welfare, child abuse and neglect prevention, ACEs, family safety, or trauma-informed child services.
89. Read `../domains/fraud-scams-consumer-protection/README.md` if you are working on scams, fraud, phishing, identity theft recovery, consumer complaints, consumer protection, or fraud risk communication.
90. Read `../domains/online-safety-digital-harm-prevention/README.md` if you are working on online safety, cyberbullying, online harassment, digital abuse, child online protection, platform reporting, or digital harm recovery.
91. Read `../domains/rare-disease-diagnostic-odyssey-care-coordination/README.md` if you are working on rare diseases, undiagnosed disease, diagnostic odyssey, genetic testing pathways, expert referral, patient registries, or orphan products.
92. Read `../domains/multimorbidity-polypharmacy-care-coordination/README.md` if you are working on multimorbidity, multiple chronic conditions, polypharmacy, medication reconciliation, treatment burden, or complex care plans.
93. Read `../domains/care-transitions-discharge-continuity/README.md` if you are working on discharge planning, care transitions, handoffs, medication reconciliation, follow-up, readmissions, or cross-setting care continuity.
94. Read `../domains/home-health-hospice-palliative-care-continuity/README.md` if you are working on home health, serious illness care, palliative care, hospice, symptom burden, caregiver support, or goals-of-care systems.
95. Read `../domains/medical-interpreter-cultural-mediation/README.md` if you are working on medical interpreting, language assistance, CLAS, LEP, culturally appropriate care, informed-consent understanding, or clinical communication access.
96. Read `../domains/patient-advocacy-shared-decision-making/README.md` if you are working on patient advocacy, shared decision-making, decision aids, informed consent, patient participation, treatment burden, or preference-sensitive care.
97. Read `../domains/life-logging-personal-archives-continuity/README.md` if you are working on life logging, personal digital archives, metadata, backup, migration, long-term readability, or personal history continuity.
98. Read `../domains/digital-legacy-data-succession/README.md` if you are working on digital legacy, account succession, fiduciary access, disabled-agent access, data handoff, or digital asset continuity.
99. Read `../domains/wearables-continuous-sensing-personal-informatics/README.md` if you are working on wearables, continuous sensing, self-tracking, remote data acquisition, personal informatics, or feedback loops.
100. Read `../domains/personal-knowledge-management-cognitive-offloading/README.md` if you are working on personal knowledge management, cognitive offloading, external memory, notes, retrieval, knowledge bases, or AI-assisted context recovery.
101. Read `../domains/brain-computer-interface-neurotechnology-governance/README.md` if you are working on brain-computer interfaces, neural recording, neural stimulation, neural data, neuroethics, or BCI governance.
102. Read `../domains/robotics-embodied-assistance-care-automation/README.md` if you are working on robotics, embodied assistance, exoskeletons, care automation, service robots, or rehabilitation robots.
103. Read `../domains/armed-conflict-civilian-protection-ihl/README.md` if you are working on armed conflict, IHL, civilian protection, humanitarian access, or conflict service continuity.
104. Read `../domains/peacebuilding-conflict-prevention-social-cohesion/README.md` if you are working on peacebuilding, conflict prevention, social cohesion, mediation, or fragility.
105. Read `../domains/continuity-of-government-public-administration-resilience/README.md` if you are working on continuity of government, public administration resilience, essential functions, or public service recovery.
106. Read `../domains/telecommunications-network-resilience-continuity/README.md` if you are working on telecommunications networks, emergency communications, broadband resilience, backup power, or outage recovery.
107. Read `../domains/macroeconomic-monetary-fiscal-stability/README.md` if you are working on inflation, employment, fiscal space, public debt, financial stability, or macro resource constraints.
108. Read `../domains/anti-corruption-public-integrity-accountability/README.md` if you are working on anti-corruption, public integrity, transparency, audit, accountability, or public resource capture.
109. Read `../domains/agricultural-production-food-system-resilience/README.md` if you are working on agricultural production, crop/livestock systems, irrigation, seeds, fertilizer, farm labor, or climate adaptation.
110. Read `../domains/soil-health-land-degradation-drought-resilience/README.md` if you are working on soil health, land degradation, erosion, salinization, desertification, drought, or land restoration.
111. Read `../domains/water-resources-hydrology-flood-drought-management/README.md` if you are working on water resources, hydrology, river basins, groundwater, reservoirs, floods, droughts, or water security.
112. Read `../domains/biodiversity-ecosystem-services-resilience/README.md` if you are working on biodiversity, ecosystem services, pollination, filtration, cooling, habitat, or ecosystem restoration.
113. Read `../domains/wildfire-landscape-fire-resilience/README.md` if you are working on wildfire, landscape fire risk, WUI, smoke exposure, evacuation interfaces, or community fire resilience.
114. Read `../domains/freight-logistics-port-cold-chain-continuity/README.md` if you are working on freight logistics, ports, warehousing, cold chain, key material delivery, or last-mile continuity.
115. Read `../domains/coastal-marine-resilience-blue-economy-continuity/README.md` if you are working on coastal resilience, sea level rise, storm surge, coastal economies, marine ecosystem buffers, or blue economy continuity.
116. Read `../domains/fisheries-aquatic-food-systems-continuity/README.md` if you are working on fisheries, aquaculture, aquatic foods, seafood nutrition, small-scale fisheries, or aquatic food supply continuity.
117. Read `../domains/dams-levees-flood-control-infrastructure-safety/README.md` if you are working on dam safety, levee safety, flood-control assets, drainage infrastructure, or flood-infrastructure failure risk.
118. Read `../domains/public-works-civil-infrastructure-asset-management/README.md` if you are working on roads, bridges, tunnels, drainage, public works maintenance, civil infrastructure asset management, or maintenance backlog.
119. Read `../domains/urban-planning-land-use-zoning-resilience/README.md` if you are working on urban planning, land use, zoning, service layout, spatial equity, or resilience planning.
120. Read `../domains/green-blue-infrastructure-urban-nature-cooling/README.md` if you are working on urban green spaces, tree canopy, stormwater green infrastructure, blue-green corridors, heat island mitigation, or nature-based urban cooling.
121. Read `../domains/electric-grid-reliability-resilience-continuity/README.md` if you are working on electric grid reliability, distribution resilience, outages, restoration, critical loads, or grid lifeline continuity.
122. Read `../domains/water-wastewater-utility-service-continuity/README.md` if you are working on drinking-water utilities, wastewater systems, water quality, sewer service, pump stations, or water utility resilience.
123. Read `../domains/fuel-thermal-energy-service-continuity/README.md` if you are working on heating fuel, cooling energy, gas, propane, district energy, backup fuel, or thermal service continuity.
124. Read `../domains/public-transit-service-operations-continuity/README.md` if you are working on bus, rail, ferry, paratransit, service reliability, transit assets, operations workforce, or service restoration.
125. Read `../domains/critical-infrastructure-lifeline-interdependency-resilience/README.md` if you are working on community lifelines, national critical functions, cascading failures, infrastructure dependencies, or cross-sector resilience.
126. Read `../domains/utility-affordability-shutoff-protection-continuity/README.md` if you are working on utility bills, arrears, shutoff protection, LIHEAP, Lifeline, energy burden, water affordability, or utility consumer protection.
127. Read `../domains/gene-therapy-genome-editing-delivery-safety/README.md` if you are working on gene therapy, genome editing, delivery vectors, off-target risk, expression control, or long-term follow-up.
128. Read `../domains/biological-age-clocks-biomarker-validation/README.md` if you are working on epigenetic clocks, biological age, biomarker validation, surrogate endpoints, or aging feedback metrics.
129. Read `../domains/multiomics-personal-baseline-systems-biology/README.md` if you are working on genomics, epigenomics, transcriptomics, proteomics, metabolomics, microbiomics, longitudinal personal baselines, or systems biology.
130. Read `../domains/engineered-cell-therapy-regenerative-platforms/README.md` if you are working on CAR-T, TCR-T, TIL, NK, iPSC-derived cells, programmable cells, or engineered cell therapy safety.
131. Read `../domains/organoids-organ-on-chip-disease-models/README.md` if you are working on organoids, organ-on-chip, tissue chips, patient-derived models, alternative methods, or disease-model validation.
132. Read `../domains/xenotransplantation-bioengineered-organ-replacement/README.md` if you are working on xenotransplantation, genetically engineered animal organs, bioengineered organ replacement, organ perfusion, or transplant platform risks.
133. Read `../domains/causal-inference-target-trial-emulation/README.md` if you are working on causality, target trial emulation, intervention effects, confounding, selection bias, or counterfactual evaluation.
134. Read `../domains/survival-analysis-healthspan-risk-modeling/README.md` if you are working on survival curves, hazard functions, healthspan, competing risks, disability time, or effective-time endpoints.
135. Read `../domains/human-digital-twin-life-course-simulation/README.md` if you are working on human digital twins, life-course simulation, state vectors, scenario modeling, or dynamic subject models.
136. Read `../domains/implementation-science-adherence-behavior-change/README.md` if you are working on implementation science, adherence, adoption, behavior change, RE-AIM, COM-B, or real-world effectiveness.
137. Read `../domains/uncertainty-quantification-model-calibration/README.md` if you are working on model calibration, validation, uncertainty intervals, prediction reporting, drift, or overconfidence controls.
138. Read `../domains/data-quality-missingness-representativeness/README.md` if you are working on data quality, missingness, representativeness, measurement error, cohort bias, or data source suitability.
139. Read `../domains/privacy-preserving-computation-federated-learning/README.md` if you are working on differential privacy, federated learning, privacy-enhancing technologies, collaborative analytics, synthetic data, or privacy-utility tradeoffs.
140. Read `../domains/knowledge-graph-ontology-semantic-interoperability/README.md` if you are working on ontology, knowledge graph, RDF/OWL, FAIR data, semantic interoperability, controlled vocabulary, or domain relation modeling.
141. Read `../domains/model-cards-ai-audit-documentation/README.md` if you are working on model cards, datasheets, AI audit documentation, system cards, model limitations, or visualization governance.
142. Read `../domains/technology-foresight-horizon-scanning/README.md` if you are working on horizon scanning, technology foresight, weak signals, scenario planning, emerging technology watch, or future technology windows.
143. Read `../domains/research-portfolio-prioritization-funding-governance/README.md` if you are working on research prioritization, portfolio governance, funding allocation, value of information, stage gates, or stop conditions.
144. Read `../domains/intellectual-property-technology-transfer-access/README.md` if you are working on patents, licensing, technology transfer, public-funded inventions, Bayh-Dole, march-in rights, or technology access.
145. Read `../domains/trustworthy-scientific-communication-peer-review/README.md` if you are working on peer review, preprints, publication ethics, retractions, corrections, citation context, or scientific communication.
146. Read `../domains/research-participant-consent-community-engagement/README.md` if you are working on informed consent, participant withdrawal, recontact, research return of results, patient engagement, or community engagement.
147. Read `../domains/biobanking-biospecimen-quality-chain-of-custody/README.md` if you are working on biobanks, biospecimen quality, preanalytical variables, cold chain, sample tracking, or chain of custody.
148. Read `../domains/longitudinal-cohort-retention-followup-infrastructure/README.md` if you are working on longitudinal cohorts, follow-up, retention, attrition, event ascertainment, or life-course data linkage.
149. Read `../domains/registries-real-world-data-governance/README.md` if you are working on patient registries, disease registries, product registries, real-world data, real-world evidence, or registry data quality.
150. Read `../domains/scientific-instrumentation-sensor-calibration-maintenance/README.md` if you are working on scientific instrumentation, sensor calibration, drift, maintenance, reference materials, or measurement uncertainty.
151. Read `../domains/nanomedicine-targeted-delivery-molecular-repair/README.md` if you are working on nanomedicine, targeted delivery, nanoparticles, release control, molecular diagnostics, or future molecular repair claims.
152. Read `../domains/ai-drug-discovery-protein-design/README.md` if you are working on AI drug discovery, protein design, molecular generation, lead optimization, or predictive medicinal chemistry.
153. Read `../domains/epigenetic-editing-gene-regulation-therapeutics/README.md` if you are working on epigenetic editing, gene regulation therapeutics, chromatin state, gene silencing, or expression reprogramming.
154. Read `../domains/brain-preservation-connectomics-emulation/README.md` if you are working on brain preservation, connectomics, whole-brain emulation, neural identity records, or mind-uploading claims.
155. Read `../domains/post-quantum-cryptography-long-term-data-security/README.md` if you are working on post-quantum cryptography, long-term confidentiality, cryptographic migration, or future decryption risk.
156. Read `../domains/safety-critical-software-formal-methods/README.md` if you are working on safety-critical software, formal methods, assurance cases, verification, or high-risk system failures.
157. Read `../domains/long-term-digital-preservation-format-migration/README.md` if you are working on long-term digital preservation, file formats, metadata, fixity, backups, migration, or future readability.
158. Read `../domains/cerebrovascular-stroke-brain-perfusion-resilience/README.md` if you are working on stroke, brain perfusion, TIA, reperfusion windows, secondary prevention, or brain vascular resilience.
159. Read `../domains/traumatic-brain-injury-neurotrauma-recovery/README.md` if you are working on traumatic brain injury, concussion, repeated head impacts, neurotrauma recovery, or long-term cognitive/emotional/sleep sequelae.
160. Read `../domains/delirium-acute-cognitive-failure-prevention/README.md` if you are working on delirium, acute cognitive failure, ICU/hospital cognitive risk, or prevention of acute subject disconnection.
161. Read `../domains/disorders-of-consciousness-coma-recovery/README.md` if you are working on coma, vegetative/unresponsive wakefulness syndrome, minimally conscious state, recovery windows, or surrogate decision boundaries.
162. Read `../domains/epilepsy-seizure-network-stability/README.md` if you are working on seizures, epilepsy, brain network stability, treatment continuity, injury risk, or participation limits.
163. Read `../domains/autonomic-nervous-system-homeostasis/README.md` if you are working on autonomic regulation, orthostatic intolerance, heart-rate/blood-pressure control, sweating, digestion, bladder function, or stress recovery.
164. Read `../domains/migraine-headache-effective-time-burden/README.md` if you are working on migraine, headache disorders, sensory sensitivity, cognitive fog, disability days, or effective-time burden.
165. Read `../domains/vision-eye-health-continuity/README.md` if you are working on vision, eye health, visual impairment, low vision support, reading, mobility, or visual task participation.
166. Read `../domains/hearing-auditory-communication-continuity/README.md` if you are working on hearing loss, auditory communication, tinnitus, hearing support, sound alerts, or communication fatigue.
167. Read `../domains/vestibular-balance-spatial-orientation/README.md` if you are working on vestibular disorders, dizziness, balance, spatial orientation, falls, or mobility confidence.
168. Read `../domains/speech-language-communication-continuity/README.md` if you are working on aphasia, dysarthria, apraxia of speech, communication participation, consent expression, or augmentative communication.
169. Read `../domains/swallowing-dysphagia-aspiration-nutrition/README.md` if you are working on dysphagia, aspiration, swallowing safety, nutrition/hydration entry, feeding dignity, or aspiration pneumonia risk.
170. Read `../domains/smell-taste-chemosensory-continuity/README.md` if you are working on smell, taste, chemosensory loss, hazard detection, appetite, nutrition, or quality of life.
171. Read `../domains/peripheral-neuropathy-somatosensory-continuity/README.md` if you are working on peripheral neuropathy, touch, pain, proprioception, foot risk, somatosensory feedback, or fine motor feedback.
172. Read `../domains/space-weather-geomagnetic-storm-resilience/README.md` if you are working on space weather, geomagnetic storms, solar activity, electric grids, satellites, communications, navigation, or timing-system resilience.
173. Read `../domains/planetary-defense-near-earth-object-risk/README.md` if you are working on near-Earth objects, asteroid/comet impact risk, planetary defense, detection, tracking, warning, or deflection governance.
174. Read `../domains/volcanic-ashfall-geohazard-continuity/README.md` if you are working on volcano hazards, volcanic ash, air quality, aviation disruption, water, agriculture, buildings, or geohazard recovery.
175. Read `../domains/earthquake-seismic-risk-built-environment-continuity/README.md` if you are working on earthquakes, seismic risk, built environment safety, hospitals, roads, utilities, ShakeAlert, or post-earthquake recovery.
176. Read `../domains/tsunami-warning-coastal-evacuation-continuity/README.md` if you are working on tsunami warning, coastal evacuation, vertical refuge, alerting, coastal recovery, or short-window evacuation systems.
177. Read `../domains/extreme-heat-cooling-public-health-continuity/README.md` if you are working on extreme heat, heat health, cooling access, energy burden, housing quality, occupational heat exposure, or urban heat islands.
178. Read `../domains/noise-exposure-acoustic-environment-continuity/README.md` if you are working on noise exposure, acoustic environments, hearing preservation, sleep disruption, community noise, transportation noise, or occupational noise.
179. Read `../domains/light-exposure-circadian-environment-continuity/README.md` if you are working on light exposure, circadian environment, daylight, night-time light, shift work, lighting, sleep timing, or light pollution.
180. Read `../domains/lead-heavy-metal-exposure-control/README.md` if you are working on lead, mercury, cadmium, arsenic, heavy-metal exposure, old housing, drinking water, soil, dust, occupational exposure, or children's environmental health.
181. Read `../domains/radon-asbestos-indoor-hazard-continuity/README.md` if you are working on radon, asbestos, indoor long-latency hazards, old buildings, schools, workplaces, lung cancer risk, or building legacy exposures.
182. Read `../domains/mold-dampness-indoor-biological-exposure/README.md` if you are working on mold, dampness, indoor biological exposure, leaks, water damage, indoor allergens, housing quality, or post-flood indoor environments.
183. Read `../domains/vector-borne-disease-environmental-control/README.md` if you are working on vector-borne disease, mosquitoes, ticks, fleas, vector control, climate-water ecology, One Health, or environmental infection risk.
    - Then read `../domains/mosquito-bite-arbovirus-prevention-continuity/README.md` for mosquito bites, arboviruses, standing water, travel, outdoor activity, or pregnancy-related exposure boundaries.
    - Then read `../domains/tick-bite-lyme-rickettsial-prevention-continuity/README.md` for tick bites, Lyme disease, rickettsial disease, wooded yards, pets, outdoor labor, or delayed recognition.
    - Then read `../domains/rabies-exposure-bite-pep-continuity/README.md` for suspected rabies exposure, animal bites, public-health consultation, PEP access, or bat/wildlife contact boundaries.
    - Then read `../domains/dog-bite-community-injury-prevention-continuity/README.md` for dog bites, child safety, community animal interaction, infection risk, or neighborhood co-existence.
    - Then read `../domains/rodent-infestation-hantavirus-plague-continuity/README.md` for rodent infestation, droppings/urine contamination, hantavirus, plague, storage spaces, or post-disaster return.
    - Then read `../domains/bed-bug-infestation-sleep-housing-continuity/README.md` for bed bugs, sleep disruption, housing stability, stigma, treatment cost, or pesticide misuse.
    - Then read `../domains/venomous-bites-stings-envenomation-continuity/README.md` for venomous bites/stings, snakes, spiders, scorpions, bees, poison-center connection, or outdoor task interruption.
    - Then read `../domains/reptile-amphibian-backyard-poultry-salmonella-continuity/README.md` for reptiles, amphibians, backyard poultry, salmonella, children, schools, or kitchen hygiene boundaries.
    - Then read `../domains/lice-scabies-school-shelter-infestation-continuity/README.md` for lice, scabies, schools, shelters, long-term care, stigma, sleep disruption, or participation policy.
    - Then read `../domains/pesticide-label-exposure-poison-control-continuity/README.md` for pesticide labels, exposure events, children/pets, poison control, NPIC, or safe pest-control boundaries.
    - Then read `../domains/pollen-allergen-asthma-outdoor-activity-continuity/README.md` for pollen, seasonal allergy, asthma triggers, outdoor activity, school/work attendance, or sleep disruption.
    - Then read `../domains/poison-ivy-oak-sumac-urushiol-exposure-continuity/README.md` for poison ivy/oak/sumac, urushiol contact, dermatitis, outdoor labor, gardening, or disaster cleanup boundaries.
    - Then read `../domains/harmful-algal-bloom-cyanotoxin-water-recreation-continuity/README.md` for harmful algal blooms, cyanotoxins, lake/coastal advisories, pets, water recreation, or drinking-water trust.
    - Then read `../domains/toxic-mushroom-foraging-poisoning-continuity/README.md` for wild mushroom foraging, misidentification, ingestion, poison-center connection, or food-safety risk communication.
    - Then read `../domains/poisonous-plant-childcare-household-exposure-continuity/README.md` for poisonous plants, children, pets, childcare, schools, household plants, or poison-center connection.
    - Then read `../domains/invasive-species-human-health-access-continuity/README.md` for invasive species, ecosystem-service loss, allergenic/toxic species, vector ecology, public-space access, or maintenance burden.
    - Then read `../domains/mycotoxin-food-crop-storage-safety-continuity/README.md` for mycotoxins, crop storage, grains/nuts, feed safety, chronic exposure, or food-supply inspection boundaries.
    - Then read `../domains/recreational-water-illness-beach-lake-access-continuity/README.md` for pools, lakes, beaches, recreational water illness, water-quality advisories, closures, or cooling/recovery access.
    - Then read `../domains/shellfish-biotoxin-harmful-algal-bloom-food-continuity/README.md` for shellfish biotoxins, HAB-related closures, seafood safety, harvest advisories, recalls, or coastal food continuity.
    - Then read `../domains/landscaping-horticulture-worker-equipment-injury-continuity/README.md` for landscaping, horticulture, lawn/tree maintenance, outdoor worker injury, heat, equipment, pesticide, or plant exposure.
    - Then read `../domains/contact-lens-hygiene-eye-infection-continuity/README.md` for contact lenses, lens solution/cases, hygiene failure, eye infection risk, or vision task continuity.
    - Then read `../domains/hearing-aid-maintenance-battery-access-continuity/README.md` for hearing aids, batteries/charging, maintenance, consumables, OTC boundaries, or communication participation.
    - Then read `../domains/menstrual-product-access-safety-continuity/README.md` for menstrual products, hygiene access, school/work participation, replacement access, or product-safety boundaries.
    - Then read `../domains/incontinence-absorbent-product-supply-dignity-continuity/README.md` for absorbent products, incontinence supply, dignity, privacy, skin risk, or caregiver burden.
    - Then read `../domains/diabetic-therapeutic-footwear-offloading-continuity/README.md` for diabetic therapeutic footwear, inserts, offloading, foot protection, replacement supply, or walking continuity.
    - Then read `../domains/compression-garment-lymphedema-venous-continuity/README.md` for compression garments, lymphedema, venous swelling, wearing burden, replacement supply, or functional participation.
    - Then read `../domains/eyeglasses-prescription-repair-replacement-continuity/README.md` for eyeglasses, prescription renewal, repair/replacement, backup glasses, pickup delay, or visual task continuity.
    - Then read `../domains/wheelchair-scooter-battery-repair-access-continuity/README.md` for wheelchairs, scooters, batteries, chargers, repair access, spare parts, supplier response, or transport compatibility.
    - Then read `../domains/walker-cane-crutch-fit-maintenance-continuity/README.md` for canes, crutches, walkers, rubber tips, brakes, fit, maintenance, replacement, or fall/participation consequences.
    - Then read `../domains/prosthetic-limb-orthotic-fit-repair-continuity/README.md` for prosthetic limbs, orthotics, sockets, braces, liners, skin interface, repair, replacement, or mobility participation.
    - Then read `../domains/cpap-pap-device-mask-supply-power-continuity/README.md` for CPAP/BiPAP/PAP devices, masks, tubing, filters, power, recalls, supplier friction, or sleep-recovery continuity.
    - Then read `../domains/fall-detection-emergency-response-device-continuity/README.md` for fall-detection devices, personal emergency response buttons, sensors, charging, connectivity, notification routing, or response chains.
    - Then read `../domains/private-well-water-testing-treatment-continuity/README.md` for private wells, groundwater testing, water treatment, wellhead protection, alternate water, or household water-task continuity.
    - Then read `../domains/household-water-treatment-filter-maintenance-continuity/README.md` for home water filters, point-of-use treatment, filter replacement, certification claims, maintenance, or contaminant-target mismatch.
    - Then read `../domains/lead-service-line-lead-copper-drinking-water-continuity/README.md` for lead service lines, lead/copper sampling, corrosion control, public notices, replacement plans, or household mitigation boundaries.
    - Then read `../domains/premise-plumbing-backflow-cross-connection-continuity/README.md` for premise plumbing, cross-connections, backflow, pressure events, testing/maintenance records, or use-point water safety.
    - Then read `../domains/septic-system-maintenance-sewage-backup-continuity/README.md` for septic tanks, drainfields, pumping/inspection, overload, sewage backup, or decentralized wastewater continuity.
    - Then read `../domains/basement-flooding-sump-pump-moisture-recovery-continuity/README.md` for basement flooding, sump pumps, drainage, outages, moisture recovery, mold risk, or housing recovery tasks.
    - Then read `../domains/residential-electrical-wiring-outlet-safety-continuity/README.md` for residential wiring, outlets, extension cords, GFCI/AFCI, overload, electrical fire, or household device power safety.
    - Then read `../domains/home-heating-equipment-chimney-vent-maintenance-continuity/README.md` for heating equipment, chimney, venting, furnace/boiler/fireplace maintenance, winter indoor heat, or combustion safety boundaries.
    - Then read `../domains/home-cooling-heat-pump-air-conditioning-maintenance-continuity/README.md` for AC, heat pumps, cooling maintenance, filters, indoor heat exposure, heat waves, or cooling-task continuity.
    - Then read `../domains/natural-gas-propane-leak-shutoff-continuity/README.md` for natural gas, propane, fuel-gas leaks, shutoff boundaries, evacuation, or professional restoration after fuel risk.
    - Then read `../domains/thermostat-temperature-control-thermal-comfort-continuity/README.md` for thermostats, setpoints, sensors, remote control, thermal comfort, or temperature-control task continuity.
    - Then read `../domains/weatherization-insulation-air-sealing-thermal-envelope-continuity/README.md` for weatherization, insulation, air sealing, thermal envelope, moisture/ventilation balance, or energy-burden continuity.
    - Then read `../domains/residential-solid-waste-collection-bin-sanitation-continuity/README.md` for residential trash, recycling, yard waste, bins, missed collection, bulky pickup, or household waste sanitation continuity.
    - Then read `../domains/household-hazardous-waste-chemical-disposal-continuity/README.md` for household hazardous waste, paints, solvents, pesticides, cleaners, auto chemicals, HHW drop-off, or chemical-disposal continuity.
    - Then read `../domains/home-sharps-medical-waste-disposal-continuity/README.md` for home needles, syringes, lancets, auto-injectors, sharps containers, drop boxes, mail-back, or medical-waste disposal continuity.
    - Then read `../domains/e-waste-battery-recycling-disposal-continuity/README.md` for e-waste, lithium-ion batteries, button batteries, household batteries, device retirement, take-back, recycling, or battery-disposal continuity.
    - Then read `../domains/food-scrap-composting-pest-odor-continuity/README.md` for food scraps, composting, countertop bins, curbside organics, pests, odor, leakage, or food-waste diversion continuity.
    - Then read `../domains/illegal-dumping-litter-neighborhood-sanitation-continuity/README.md` for illegal dumping, litter, abandoned furniture, tires, mattresses, alley/lot dumping, reporting, cleanup delays, or neighborhood sanitation continuity.
    - Then read `../domains/home-hvac-filter-maintenance-indoor-air-continuity/README.md` for HVAC filters, filter fit, MERV semantics, replacement reminders, return-air filter access, or indoor-air maintenance continuity.
    - Then read `../domains/portable-air-cleaner-room-filtration-continuity/README.md` for portable air cleaners, room filtration, filter replacement, clean-air rooms, noise/power constraints, or room-level filtration continuity.
    - Then read `../domains/cooking-ventilation-range-hood-indoor-air-continuity/README.md` for range hoods, kitchen ventilation, cooking particles, NO2, cooking odors, or meal-preparation indoor-air continuity.
    - Then read `../domains/home-humidity-dehumidifier-moisture-control-continuity/README.md` for household humidity, dehumidifiers, humidifiers, condensation, basement moisture, or moisture-control continuity.
    - Then read `../domains/household-dust-allergen-source-control-continuity/README.md` for household dust, dust mites, pet dander, bedding/fabrics, allergen source control, or allergy-burden task continuity.
    - Then read `../domains/household-voc-fragrance-product-emission-continuity/README.md` for VOCs, fragrances, air fresheners, cleaning-product emissions, furniture/off-gassing, odor sensitivity, or product-emission continuity.
    - Then read `../domains/home-clutter-pathway-trip-fall-continuity/README.md` for home clutter, pathway obstruction, temporary piles, throw rugs, toys, laundry, packages, trip/fall exposure, or household pathway continuity.
    - Then read `../domains/household-cord-cable-trip-entanglement-continuity/README.md` for charging cables, extension cords, power strips, device cords, cable routing, trip/entanglement exposure, or household connection continuity.
    - Then read `../domains/home-shelving-cabinet-storage-stability-continuity/README.md` for shelves, cabinets, closets, garage storage, falling objects, overloaded storage, or household object-access continuity.
    - Then read `../domains/household-ladder-step-stool-reach-task-continuity/README.md` for ladders, step stools, high-reach tasks, bulb/smoke-alarm battery changes, seasonal storage, or reach-task continuity.
    - Then read `../domains/home-office-workstation-ergonomics-continuity/README.md` for home-office workstations, desk/chair/screen/keyboard/mouse fit, remote work, posture load, visual load, or workstation continuity.
    - Then read `../domains/toy-small-parts-choking-ingestion-continuity/README.md` for toy small parts, magnets, button batteries, age separation, toy storage, recalls, choking, ingestion, or child play-space continuity.
    - Then read `../domains/home-utility-shutoff-location-labeling-continuity/README.md` for household utility shutoff locations, labels, maps, responsibility boundaries, or emergency/repair handoff metadata.
    - Then read `../domains/household-circuit-breaker-panel-labeling-continuity/README.md` for circuit breaker panel directories, circuit labels, critical loads, electrical handoff metadata, or professional-service readability.
    - Then read `../domains/home-water-valve-plumbing-labeling-continuity/README.md` for water valves, plumbing labels, leak history, water-system maps, or plumbing repair handoff metadata.
    - Then read `../domains/household-equipment-serial-model-recall-record-continuity/README.md` for household equipment model/serial records, recall matching, product identity, repair history, or safety-notice continuity.
    - Then read `../domains/home-service-provider-emergency-contact-directory-continuity/README.md` for household service contacts, utilities, property managers, repair providers, poison help, or emergency/non-emergency contact directories.
    - Then read `../domains/household-operating-map-handoff-continuity/README.md` for household operating maps, implicit household knowledge, caregiver/house-sitter handoff, supply locations, routines, or household proxy execution.
    - Then read `../domains/municipal-311-service-request-continuity/README.md` for 311, non-emergency service requests, Open311, service request status, routing, or local public works request continuity.
    - Then read `../domains/streetlight-outage-nighttime-visibility-continuity/README.md` for streetlight outages, nighttime visibility, pedestrian lighting, dark corridors, or lighting repair request continuity.
    - Then read `../domains/sidewalk-curb-ramp-maintenance-access-continuity/README.md` for sidewalk defects, curb ramps, PROWAG/ADA public right-of-way, trip hazards, or pedestrian facility maintenance continuity.
    - Then read `../domains/snow-ice-sidewalk-winter-access-continuity/README.md` for snow, ice, winter sidewalk access, curb ramp blockage, transit stop snow, or seasonal pedestrian access continuity.
    - Then read `../domains/street-tree-branch-hazard-shade-maintenance-continuity/README.md` for street trees, branch hazards, root sidewalk conflict, shade access, urban forestry, or street tree maintenance continuity.
    - Then read `../domains/storm-drain-catch-basin-local-flooding-continuity/README.md` for storm drains, catch basins, street flooding, local flooding, stormwater maintenance, or neighborhood drainage continuity.
184. Read `../domains/advance-care-planning-medical-decision-continuity/README.md` if you are working on advance care planning, advance directives, health care proxy, medical decision continuity, goals of care, or incapacity communication.
185. Read `../domains/supported-decision-making-guardianship-rights/README.md` if you are working on supported decision-making, guardianship, conservatorship, decision capacity, disability rights, or least restrictive alternatives.
186. Read `../domains/healthcare-personal-representative-hipaa-access-continuity/README.md` if you are working on HIPAA personal representatives, caregiver access, proxy access, medical records, privacy boundaries, or authorized care coordination.
187. Read `../domains/financial-fiduciary-power-of-attorney-continuity/README.md` if you are working on financial power of attorney, fiduciary duty, bill payment, asset management, incapacity finance, or elder financial exploitation prevention.
188. Read `../domains/representative-payee-benefits-management-continuity/README.md` if you are working on representative payees, VA fiduciaries, benefits management, public income continuity, payee oversight, or protected benefit use.
189. Read `../domains/trust-estate-affairs-succession-continuity/README.md` if you are working on getting affairs in order, trustees, executors, estate affairs, beneficiary records, succession, or long-term project handoff.
190. Read `../domains/credit-consumer-reporting-access-continuity/README.md` if you are working on credit reports, consumer reports, specialty reporting agencies, report disputes, identity errors, or access impacts.
191. Read `../domains/tenant-screening-rental-access-continuity/README.md` if you are working on tenant screening, rental applications, eviction records, rental history, housing access, or rental-platform screening.
192. Read `../domains/background-check-record-screening-continuity/README.md` if you are working on background checks, criminal records, identity matching, license/education verification, adverse action, or record correction.
193. Read `../domains/employment-algorithmic-hiring-screening-continuity/README.md` if you are working on AI hiring, algorithmic resume screening, employment tests, video interview scoring, job matching, or employment decision systems.
194. Read `../domains/insurance-underwriting-algorithmic-risk-scoring-continuity/README.md` if you are working on insurance underwriting, algorithmic risk scoring, premium rating, claims automation, external data, or insurance AI governance.
195. Read `../domains/public-benefits-eligibility-automated-decision-continuity/README.md` if you are working on public benefits eligibility, automated eligibility screening, data matching, renewals, terminations, appeals, or human review.
196. Read `../domains/education-record-transcript-verification-continuity/README.md` if you are working on education records, transcripts, diplomas, enrollment verification, student records, FERPA, or degree verification.
197. Read `../domains/professional-licensure-certification-continuity/README.md` if you are working on occupational licensing, professional certification, registration, boards, scope of practice, license renewal, discipline, or portability.
198. Read `../domains/skills-competency-credentialing-continuity/README.md` if you are working on skills taxonomies, competency frameworks, micro-credentials, digital badges, portfolios, or skills-based hiring.
199. Read `../domains/continuing-education-recertification-continuity/README.md` if you are working on continuing education, CPD, CEU, CME, maintenance of certification, recertification, renewal, or continuing competence.
200. Read `../domains/apprenticeship-work-based-learning-continuity/README.md` if you are working on apprenticeships, work-based learning, on-the-job training, mentorship, journeyworker status, or competency progression.
201. Read `../domains/verifiable-credential-wallet-interoperability/README.md` if you are working on verifiable credentials, digital credential wallets, issuers, holders, verifiers, DIDs, trust registries, selective disclosure, or credential revocation.
202. Read `../domains/income-payroll-employment-record-continuity/README.md` if you are working on payroll records, wage records, employment verification, pay stubs, income proof, or payroll record correction.
203. Read `../domains/tax-administration-filing-record-continuity/README.md` if you are working on tax records, IRS transcripts, filing records, taxpayer identity, refund/credit records, tax notices, or tax account correction.
204. Read `../domains/social-security-earnings-benefit-record-continuity/README.md` if you are working on Social Security earnings records, work credits, benefit statements, retirement/disability/survivor records, or earnings corrections.
205. Read `../domains/retirement-pension-savings-plan-continuity/README.md` if you are working on pensions, 401(k), IRA, retirement plan records, vesting, rollovers, beneficiaries, lost accounts, or pension guarantees.
206. Read `../domains/unemployment-insurance-wage-record-continuity/README.md` if you are working on unemployment insurance wage records, UI claims, base periods, eligibility determinations, appeals, overpayments, or fraud controls.
207. Read `../domains/workers-compensation-occupational-injury-benefit-continuity/README.md` if you are working on workers compensation, occupational injury records, occupational disease, wage replacement, return-to-work, vocational rehabilitation, or OSHA injury logs.
208. Read `../domains/family-medical-leave-job-protection-continuity/README.md` if you are working on family or medical leave, job-protected leave, serious health conditions, caregiving leave, military caregiver leave, anti-retaliation, insurance continuity, or return-to-role after leave.
209. Read `../domains/paid-sick-family-leave-wage-replacement-continuity/README.md` if you are working on paid sick leave, paid family leave, paid medical leave, wage replacement, waiting periods, replacement rates, or leave-related payroll continuity.
210. Read `../domains/pregnancy-parental-work-continuity/README.md` if you are working on pregnancy accommodation, childbirth recovery, parental leave, bonding leave, lactation or pumping at work, parental work continuity, or pregnancy discrimination.
211. Read `../domains/workplace-accommodation-return-to-work-continuity/README.md` if you are working on reasonable accommodation, interactive process, stay-at-work, return-to-work, modified duty, phased return, work capacity, or assistive technology in employment.
212. Read `../domains/disability-income-work-capacity-benefit-continuity/README.md` if you are working on SSDI, SSI, disability income, work credits, work capacity, return-to-work incentives, benefit cliffs, or disability benefit continuity.
213. Read `../domains/family-caregiver-respite-work-continuity/README.md` if you are working on family caregiver support, respite care, caregiver training, caregiver employment continuity, eldercare, disability caregiving, or caregiver burden.
    - Then read `../domains/adult-day-services-supervision-transport-continuity/README.md` if you are working on adult day services, daytime supervision, meals/activities, transport handoff, caregiver work windows, or service continuity.
    - Then read `../domains/home-care-aide-personal-care-workforce-continuity/README.md` if you are working on home care aides, personal care attendants, ADL/IADL support, scheduling, supervision, workforce stability, or paid in-home support.
    - Then read `../domains/respite-care-provider-capacity-scheduling-continuity/README.md` if you are working on respite provider capacity, short-term substitute care, scheduling, waiting lists, service gaps, or caregiver recovery windows.
    - Then read `../domains/caregiver-training-skills-safety-continuity/README.md` if you are working on caregiver training, safe transfers, medication communication, fall prevention, infection control, behavioral support, or emergency recognition.
    - Then read `../domains/caregiver-health-burnout-screening-support-continuity/README.md` if you are working on caregiver strain, sleep loss, burnout, depression/anxiety signals, peer support, counseling connection, or caregiver health monitoring.
    - Then read `../domains/home-care-task-coordination-care-plan-continuity/README.md` if you are working on home-care task lists, care-plan handoffs, role assignment, reminders, supplies, family communication, or escalation paths.
214. Read `../domains/vital-records-life-event-continuity/README.md` if you are working on vital records, birth/death/marriage/divorce records, certified copies, record corrections, civil registration, or life-event record continuity.
215. Read `../domains/name-change-identity-record-synchronization-continuity/README.md` if you are working on legal name changes, identity record synchronization, SSA/passport/state ID updates, tax/employment/school/medical record matching, or name mismatch risks.
216. Read `../domains/address-residency-mail-service-continuity/README.md` if you are working on address changes, residency, mailing address, USPS forwarding, service notices, jurisdiction, homelessness address alternatives, or address-based service routing.
217. Read `../domains/household-composition-dependent-eligibility-continuity/README.md` if you are working on household composition, dependents, coverage household, benefit household, tax/insurance/welfare household rules, or family eligibility units.
218. Read `../domains/family-law-custody-child-support-continuity/README.md` if you are working on custody, parenting time, child support, parentage, family court orders, child support services, or family-law record continuity.
219. Read `../domains/kinship-foster-adoption-care-continuity/README.md` if you are working on kinship care, foster care, adoption, guardianship-like placements, permanency planning, child welfare records, or child placement continuity.
220. Read `../domains/banking-deposit-account-access-continuity/README.md` if you are working on bank accounts, credit union accounts, deposit insurance, account access, account recovery, payment errors, or bank-account continuity.
221. Read `../domains/debt-obligation-collection-relief-continuity/README.md` if you are working on consumer debt, medical debt, collections, garnishment, bankruptcy, debt relief, debt records, or debt-related continuity risks.
222. Read `../domains/real-property-title-deed-record-continuity/README.md` if you are working on property title, deeds, land records, tax assessor records, title insurance, liens, mortgages, or real-property record continuity.
223. Read `../domains/driver-license-vehicle-registration-continuity/README.md` if you are working on driver's licenses, state IDs, REAL ID, vehicle title, registration, plates, DMV records, or personal mobility credential continuity.
224. Read `../domains/passport-travel-document-mobility-continuity/README.md` if you are working on passports, travel documents, consular services, emergency documents, travel advisories, or cross-border mobility continuity.
225. Read `../domains/long-distance-travel-booking-itinerary-continuity/README.md` if you are working on long-distance travel booking, itinerary records, confirmations, cancellations, changes, notifications, or travel-service handoffs.
226. Read `../domains/air-passenger-rights-disruption-refund-continuity/README.md` if you are working on flight delays, cancellations, refunds, denied boarding, tarmac delays, air-travel disability access, or aviation consumer protection.
227. Read `../domains/aviation-security-screening-identity-continuity/README.md` if you are working on TSA screening, REAL ID, passenger support, identity verification, accessible screening, or airport security-screening continuity.
228. Read `../domains/baggage-personal-property-travel-continuity/README.md` if you are working on checked baggage, carry-on property, delayed/lost/damaged baggage, critical medicines/documents, or travel personal-property continuity.
229. Read `../domains/lodging-temporary-accommodation-access-continuity/README.md` if you are working on hotels, temporary lodging, check-in requirements, accessibility rooms, disaster lodging, vacation-rental scams, or accommodation access.
230. Read `../domains/travel-advisory-consular-assistance-continuity/README.md` if you are working on travel advisories, STEP, embassies, consular assistance, emergency passports, overseas crisis communication, or citizen services abroad.
231. Read `../domains/travel-health-preparedness-continuity/README.md` if you are working on travelers' health, destination health risks, travel vaccines, chronic-condition travel preparation, medicines, travel clinics, or overseas medical access.
232. Read `../domains/customs-border-entry-declaration-continuity/README.md` if you are working on customs declarations, border entry, I-94 records, prohibited/restricted items, agriculture inspection, duties, or trusted traveler systems.
233. Read `../domains/online-retail-order-shipping-fulfillment-continuity/README.md` if you are working on online retail orders, mail/telephone orders, order confirmation, shipping promises, delivery delays, non-delivery, cancellation, or fulfillment disputes.
234. Read `../domains/consumer-return-refund-dispute-resolution-continuity/README.md` if you are working on returns, refunds, exchanges, store credit, cancellation, merchant disputes, consumer complaints, or transaction-failure recovery.
235. Read `../domains/consumer-warranty-service-contract-repair-continuity/README.md` if you are working on consumer warranties, service contracts, repair/replacement promises, warranty registration, warranty documentation, or product-failure recovery.
236. Read `../domains/right-to-repair-parts-manuals-access-continuity/README.md` if you are working on right to repair, repair manuals, parts, diagnostic tools, software locks, independent repair, or product repairability.
237. Read `../domains/payment-card-dispute-unauthorized-charge-continuity/README.md` if you are working on credit-card disputes, debit-card errors, EFT errors, unauthorized charges, billing errors, provisional credits, or payment error resolution.
238. Read `../domains/gift-card-prepaid-stored-value-continuity/README.md` if you are working on gift cards, prepaid cards, store credit, platform balances, loyalty balances, expiration, fees, or stored-value scams.
239. Read `../domains/price-fee-disclosure-junk-fee-continuity/README.md` if you are working on price disclosure, total price, drip pricing, junk fees, mandatory fees, hidden fees, or bill transparency.
240. Read `../domains/consumer-reviews-endorsements-marketplace-trust-continuity/README.md` if you are working on consumer reviews, fake reviews, endorsements, influencer disclosures, testimonials, review suppression, or marketplace trust.
241. Read `../domains/credit-card-revolving-credit-cost-continuity/README.md` if you are working on credit cards, revolving balances, APR, fees, grace periods, minimum payments, delinquency, or account closure.
242. Read `../domains/consumer-loan-origination-apr-disclosure-continuity/README.md` if you are working on consumer loans, personal loans, installment loans, origination, underwriting, APR disclosure, fees, repayment schedules, or servicing handoffs.
243. Read `../domains/mortgage-origination-servicing-foreclosure-continuity/README.md` if you are working on mortgage origination, Loan Estimates, Closing Disclosures, escrow, servicing transfers, loss mitigation, forbearance, or foreclosure continuity.
244. Read `../domains/auto-loan-lease-servicing-repossession-continuity/README.md` if you are working on auto loans, vehicle leases, dealer financing, add-ons, servicing, delinquency, repossession, title liens, or deficiency balances.
245. Read `../domains/student-loan-servicing-repayment-forgiveness-continuity/README.md` if you are working on student loan servicing, repayment plans, deferment, forbearance, PSLF, forgiveness, discharge, default, or payment-count records.
246. Read `../domains/payday-small-dollar-title-loan-continuity/README.md` if you are working on payday loans, small-dollar high-cost loans, title loans, rollovers, account access, vehicle collateral, or debt cycles.
247. Read `../domains/buy-now-pay-later-installment-financing-continuity/README.md` if you are working on BNPL, installment financing, merchant checkout credit, autopay, refunds, late fees, credit reporting, or platform overextension.
248. Read `../domains/remittance-money-transfer-disclosure-continuity/README.md` if you are working on remittance transfers, cross-border money transfers, exchange-rate disclosure, fees, cancellation, refunds, error resolution, or recipient availability.
249. Read `../domains/auto-insurance-liability-collision-claims-continuity/README.md` if you are working on auto insurance, liability, collision, comprehensive coverage, uninsured/underinsured motorists, deductibles, accident claims, repair estimates, total loss, or subrogation.
250. Read `../domains/homeowners-renters-property-insurance-claims-continuity/README.md` if you are working on homeowners insurance, renters insurance, personal property, loss of use, additional living expense, property inventories, proof of loss, or housing recovery claims.
251. Read `../domains/flood-insurance-nfip-claims-continuity/README.md` if you are working on flood insurance, NFIP, private flood insurance, flood maps, waiting periods, proof of loss, flood claims, appeals, or disaster recovery cash-flow continuity.
252. Read `../domains/catastrophe-wind-wildfire-earthquake-insurance-continuity/README.md` if you are working on windstorm, wildfire, earthquake, hail, catastrophe deductibles, FAIR Plans, insurer nonrenewal, insurance withdrawal, or catastrophe coverage gaps.
253. Read `../domains/disability-income-insurance-claim-continuity/README.md` if you are working on short-term disability insurance, long-term disability insurance, own-occupation standards, any-occupation standards, elimination periods, medical evidence, claims, or appeals.
254. Read `../domains/long-term-care-insurance-benefit-activation-continuity/README.md` if you are working on long-term care insurance, ADL triggers, cognitive impairment triggers, elimination periods, care plans, invoices, benefit activation, or premium increases.
255. Read `../domains/travel-insurance-trip-protection-claims-continuity/README.md` if you are working on travel insurance, trip cancellation, trip interruption, travel medical, emergency evacuation, baggage, travel delay, covered reasons, documentation, or claims.
256. Read `../domains/personal-liability-umbrella-insurance-defense-continuity/README.md` if you are working on personal liability insurance, umbrella insurance, excess liability, defense costs, claim notice, coverage disputes, settlements, exclusions, or asset exposure.
257. Read `../domains/contract-subscription-billing-consent-continuity/README.md` if you are working on contracts, subscriptions, automatic renewal, billing, cancellation, negative options, ongoing consent, or transaction-friction continuity.
258. Read `../domains/notary-document-authentication-signature-continuity/README.md` if you are working on notarization, electronic signatures, digital signatures, document authentication, apostilles, or institutional recognition of signed records.
259. Read `../domains/citizenship-nationality-statelessness-continuity/README.md` if you are working on citizenship, nationality, naturalization, consular protection, statelessness, nationality proof, or national-membership continuity.
260. Read `../domains/immigration-status-residency-work-authorization-continuity/README.md` if you are working on immigration status, residency, work authorization, status renewal, employment eligibility, or local-status continuity.
261. Read `../domains/asylum-refugee-protection-status-continuity/README.md` if you are working on asylum, refugee status, temporary protection, humanitarian protection, resettlement, or protection-status continuity.
262. Read `../domains/detention-custody-confinement-status-continuity/README.md` if you are working on arrest, detention, custody, confinement, immigration detention, release transition, or custody-status continuity.
263. Read `../domains/civil-commitment-involuntary-treatment-rights-continuity/README.md` if you are working on civil commitment, involuntary treatment, crisis evaluation, least-restrictive alternatives, review, or rights continuity.
264. Read `../domains/court-notice-service-process-default-judgment-continuity/README.md` if you are working on court notice, service of process, hearing notices, response deadlines, default judgments, or procedural-notice continuity.
265. Read `../domains/criminal-record-relief-collateral-consequences-continuity/README.md` if you are working on criminal records, record relief, expungement, sealing, collateral consequences, reentry eligibility, or record-recovery continuity.
266. Read `../domains/school-enrollment-attendance-continuity/README.md` if you are working on school enrollment, transfer, attendance, chronic absenteeism, school stability, homelessness protections, or student attendance continuity.
267. Read `../domains/special-education-iep-504-accommodation-continuity/README.md` if you are working on IDEA, IEP, Section 504, accommodations, related services, assistive supports, transition, or disability participation continuity in schools.
268. Read `../domains/school-meals-nutrition-access-continuity/README.md` if you are working on school meals, school breakfast/lunch, free/reduced-price access, CEP, summer meals, dietary accommodations, or student nutrition continuity.
269. Read `../domains/school-health-services-chronic-condition-continuity/README.md` if you are working on school health services, school nursing, chronic condition support, medication, immunization records, emergency action plans, or return-to-school continuity.
270. Read `../domains/school-transportation-safe-routes-continuity/README.md` if you are working on school buses, safe routes to school, walking/biking safety, disability transportation, distance barriers, or attendance-related transportation continuity.
271. Read `../domains/school-discipline-exclusion-restraint-continuity/README.md` if you are working on suspensions, expulsions, classroom removals, restraint/seclusion, re-entry, discipline data, or exclusion-risk continuity.
272. Read `../domains/school-mental-health-counseling-support-continuity/README.md` if you are working on school counseling, school-based mental health, social workers, crisis referral, community care linkage, or student recovery continuity.
273. Read `../domains/school-climate-bullying-violence-prevention-continuity/README.md` if you are working on school climate, belonging, bullying, harassment, violence prevention, reporting channels, or school safety continuity.
274. Read `../domains/postsecondary-admissions-transfer-articulation-continuity/README.md` if you are working on higher education admissions, enrollment, transfer, articulation, credit conversion, readmission, or postsecondary pathway continuity.
275. Read `../domains/student-financial-aid-grant-scholarship-continuity/README.md` if you are working on FAFSA, Title IV aid, grants, scholarships, work-study, aid disbursement, SAP, or student financial-aid continuity.
276. Read `../domains/academic-advising-degree-progress-continuity/README.md` if you are working on academic advising, degree audit, course sequencing, credit accumulation, early alerts, retention, or degree-progress continuity.
277. Read `../domains/campus-basic-needs-student-support-continuity/README.md` if you are working on campus food, housing, transportation, childcare, emergency aid, benefits navigation, or basic-needs student support continuity.
278. Read `../domains/campus-disability-accommodations-accessibility-continuity/README.md` if you are working on campus disability services, Section 504, ADA, accommodations, accessible materials, auxiliary aids, or higher-ed accessibility continuity.
279. Read `../domains/campus-mental-health-crisis-student-support-continuity/README.md` if you are working on campus counseling, student mental health, crisis response, leave/re-entry, peer support, or student recovery continuity.
280. Read `../domains/campus-safety-title-ix-clery-continuity/README.md` if you are working on campus safety, Title IX, sexual misconduct response, Clery Act, campus crime reporting, emergency notification, or supportive-measure continuity.
281. Read `../domains/international-student-sevis-status-continuity/README.md` if you are working on SEVIS, F/M student status, I-20, DSO reporting, CPT/OPT, travel signature, or international-student status continuity.
282. Read `../domains/email-account-recovery-continuity/README.md` if you are working on email account access, recovery email, password reset, service notifications, account takeover, or email-based recovery continuity.
283. Read `../domains/phone-number-sim-portability-account-security-continuity/README.md` if you are working on phone number control, SIM/eSIM, port-out, SIM swap, SMS verification, carrier accounts, or phone-based recovery continuity.
284. Read `../domains/mfa-passkey-credential-recovery-continuity/README.md` if you are working on MFA, passkeys, security keys, authenticator apps, recovery codes, trusted devices, or credential recovery continuity.
285. Read `../domains/password-manager-secret-vault-continuity/README.md` if you are working on password managers, secret vaults, recovery keys, emergency access, shared vaults, or credential portfolio continuity.
286. Read `../domains/cloud-backup-file-sync-data-portability-continuity/README.md` if you are working on cloud storage, file sync, backup, version history, data export, format migration, or data portability continuity.
287. Read `../domains/messaging-contact-graph-portability-continuity/README.md` if you are working on messaging accounts, contacts, groups, chat history, backup/export, interoperability, or social graph continuity.
288. Read `../domains/domain-dns-web-presence-continuity/README.md` if you are working on domain names, DNS, registrar accounts, TLS certificates, hosting, custom email domains, or web presence continuity.
289. Read `../domains/platform-account-suspension-appeals-continuity/README.md` if you are working on platform account suspension, content removal, moderation appeals, transparency, creator/merchant accounts, or platform exit continuity.
290. Read `../domains/personal-computing-device-lifecycle-repair-continuity/README.md` if you are working on personal computing devices, repairability, device replacement, support windows, data migration, device lock-in, or repair continuity.
291. Read `../domains/home-network-router-iot-security-continuity/README.md` if you are working on home routers, Wi-Fi, broadband gateways, IoT security, firmware updates, default credentials, or home-network continuity.
292. Read `../domains/software-supply-chain-dependency-provenance-continuity/README.md` if you are working on software dependencies, SBOM, package managers, build provenance, artifact signing, or software supply-chain continuity.
293. Read `../domains/software-update-vulnerability-patch-continuity/README.md` if you are working on vulnerability disclosure, patch deployment, rollback, known exploited vulnerabilities, support windows, or software-update continuity.
294. Read `../domains/open-source-maintainer-sustainability-continuity/README.md` if you are working on maintainer capacity, open-source funding, bus factor, project health, security response, or open-source sustainability continuity.
295. Read `../domains/pki-certificate-cryptographic-trust-continuity/README.md` if you are working on PKI, TLS certificates, certificate authorities, key management, revocation, root trust, certificate transparency, or cryptographic trust continuity.
296. Read `../domains/cloud-service-exit-interoperability-continuity/README.md` if you are working on SaaS/cloud export, data migration, interoperability, vendor lock-in, service exit, or cloud-switching continuity.
297. Read `../domains/api-platform-dependency-runtime-continuity/README.md` if you are working on third-party APIs, SDKs, rate limits, deprecation, SLA, runtime fallback, platform dependency, or API continuity.
298. Read `../domains/calendar-scheduling-appointment-continuity/README.md` if you are working on calendars, scheduling, appointments, time zones, reminders, rescheduling, invitations, or calendar continuity.
299. Read `../domains/notification-alert-routing-attention-continuity/README.md` if you are working on notifications, push alerts, delivery channels, quiet hours, escalation, acknowledgement, notification fatigue, or alert routing continuity.
300. Read `../domains/reminder-alarm-routine-task-continuity/README.md` if you are working on reminders, alarms, recurring tasks, routines, missed-task recovery, habit systems, or routine task continuity.
301. Read `../domains/meeting-video-conferencing-remote-collaboration-continuity/README.md` if you are working on video meetings, remote collaboration, WebRTC, captions, recordings, meeting notes, or action-item continuity.
302. Read `../domains/document-capture-ocr-pdf-record-workflow-continuity/README.md` if you are working on document capture, OCR, scanning, PDF/PDF-A, forms, metadata, submissions, or record workflow continuity.
303. Read `../domains/search-index-discovery-retrieval-continuity/README.md` if you are working on search, indexing, metadata, sitemap, schema, discovery, retrieval, broken links, or findability continuity.
304. Read `../domains/personal-automation-integration-workflow-continuity/README.md` if you are working on personal automation, low-code workflows, webhooks, OAuth, scripts, triggers, idempotency, or workflow continuity.
305. Read `../domains/collaborative-document-permission-version-continuity/README.md` if you are working on shared documents, permissions, version history, comments, ownership transfer, export, or collaborative document continuity.
306. Read `../domains/public-restroom-sanitation-hygiene-access-continuity/README.md` if you are working on public restrooms, sanitation, handwashing, menstrual hygiene, family restrooms, accessible toilets, or public hygiene access continuity.
307. Read `../domains/public-drinking-water-hydration-access-continuity/README.md` if you are working on public drinking water, hydration stations, fountains, water quality notices, emergency water distribution, or heat-related hydration access.
308. Read `../domains/public-seating-shade-rest-cooling-access-continuity/README.md` if you are working on public seating, shade, transit shelters, cooling centers, rest opportunities, urban heat exposure, or public-space recovery.
309. Read `../domains/community-resilience-hub-shelter-center-continuity/README.md` if you are working on resilience hubs, shelters, cooling/warming/clean-air centers, public charging, disaster service centers, or community lifelines.
310. Read `../domains/public-library-community-anchor-access-continuity/README.md` if you are working on public libraries, community anchors, public computers, Wi-Fi, printing/scanning, digital skills, or service navigation.
311. Read `../domains/parks-recreation-green-space-access-continuity/README.md` if you are working on parks, recreation, green space, trails, playgrounds, public exercise, nature access, or restorative public space.
312. Read `../domains/public-wifi-device-charging-connectivity-continuity/README.md` if you are working on public Wi-Fi, public computers, device charging, outage connectivity, emergency communications, or digital task continuity outside home.
313. Read `../domains/public-accommodation-accessibility-service-continuity/README.md` if you are working on public accommodations, ADA Title II/III, effective communication, service animals, reasonable accommodations, or accessible service continuity.
314. Read `../domains/municipal-311-service-request-continuity/README.md` if you are working on 311, Open311, service requests, local government service status, non-emergency reporting, or public works request continuity.
315. Read `../domains/streetlight-outage-nighttime-visibility-continuity/README.md` if you are working on streetlight outages, nighttime visibility, pedestrian lighting, dark corridors, or lighting repair request continuity.
316. Read `../domains/sidewalk-curb-ramp-maintenance-access-continuity/README.md` if you are working on sidewalk defects, curb ramps, PROWAG, ADA public right-of-way access, trip hazards, or pedestrian facility maintenance continuity.
317. Read `../domains/snow-ice-sidewalk-winter-access-continuity/README.md` if you are working on snow, ice, winter sidewalk access, curb ramp blockage, transit stop snow, or seasonal pedestrian access continuity.
318. Read `../domains/street-tree-branch-hazard-shade-maintenance-continuity/README.md` if you are working on street trees, branch hazards, shade, root-sidewalk conflicts, urban forestry, or street tree maintenance continuity.
319. Read `../domains/storm-drain-catch-basin-local-flooding-continuity/README.md` if you are working on storm drains, catch basins, street flooding, stormwater maintenance, local flooding, or neighborhood drainage continuity.
320. Read `../domains/grocery-retail-food-store-access-continuity/README.md` if you are working on grocery stores, food retail, supermarkets, farmers markets, online pickup/delivery, food prices, or retail food access continuity.
321. Read `../domains/snap-ebt-redemption-retailer-payment-continuity/README.md` if you are working on SNAP EBT, authorized retailers, EBT cards, online SNAP purchasing, benefit redemption, transaction failures, or food-benefit payment continuity.
322. Read `../domains/wic-benefit-redemption-infant-maternal-nutrition-continuity/README.md` if you are working on WIC, eWIC, food packages, infant formula through WIC, maternal/infant nutrition, or WIC redemption continuity.
323. Read `../domains/food-bank-pantry-community-food-distribution-continuity/README.md` if you are working on food banks, pantries, TEFAP, community food distribution, donated food logistics, or emergency household food buffers.
324. Read `../domains/emergency-food-disaster-feeding-continuity/README.md` if you are working on disaster feeding, emergency food distribution, D-SNAP, shelter meals, emergency food packages, or disaster nutrition assistance.
325. Read `../domains/home-delivered-meals-congregate-nutrition-services-continuity/README.md` if you are working on home-delivered meals, congregate meals, Older Americans Act nutrition services, Meals on Wheels, senior meals, or disability-related meal delivery.
326. Read `../domains/infant-formula-baby-food-supply-safety-continuity/README.md` if you are working on infant formula, baby food, specialty formula, formula recalls, shortages, WIC substitutions, or early-life food supply safety.
327. Read `../domains/prepared-food-restaurant-cafeteria-safety-access-continuity/README.md` if you are working on prepared food, restaurants, cafeterias, workplace/school/hospital meals, takeout, food allergens, menu information, or restaurant food safety access.
328. Read `../domains/retail-pharmacy-prescription-dispensing-continuity/README.md` if you are working on retail pharmacies, mail-order pharmacies, specialty pharmacies, prescription dispensing, refill continuity, pharmacy deserts, pharmacy delivery, or prescription transfer.
329. Read `../domains/pharmacy-benefit-formulary-prior-authorization-continuity/README.md` if you are working on pharmacy benefits, formularies, prior authorization, step therapy, coverage determination, exceptions, Part D, PBMs, or prescription benefit friction.
330. Read `../domains/medication-reconciliation-regimen-adherence-continuity/README.md` if you are working on medication reconciliation, medication lists, care transitions, adherence, regimen burden, pill organization, or household medication execution.
331. Read `../domains/patient-medication-labeling-counseling-continuity/README.md` if you are working on medication labels, Medication Guides, Patient Medication Information, pharmacist counseling, prescription instructions, plain-language drug information, or medication communication.
332. Read `../domains/unused-medicine-takeback-disposal-continuity/README.md` if you are working on unused medicines, expired medicines, medicine take-back, disposal sites, mail-back envelopes, drug drop boxes, or household medication storage risk.
333. Read `../domains/durable-medical-equipment-supplier-repair-continuity/README.md` if you are working on DME, DMEPOS suppliers, wheelchair/walker/hospital-bed access, equipment repair, replacement, consumables, coverage, or home medical equipment continuity.
334. Read `../domains/home-oxygen-respiratory-equipment-supply-continuity/README.md` if you are working on home oxygen, oxygen concentrators, portable oxygen, CPAP/BiPAP, respiratory equipment, oxygen accessories, electricity dependency, or respiratory supply continuity.
335. Read `../domains/diabetes-insulin-glucose-monitoring-supplies-continuity/README.md` if you are working on insulin, diabetes supplies, CGM, glucose meters, test strips, pump supplies, diabetes device access, refrigeration, or diabetes treatment supply continuity.
336. Read `../domains/provider-directory-network-adequacy-continuity/README.md` if you are working on provider directories, network adequacy, provider networks, in-network access, accepting-new-patient status, Care Compare, provider directory accuracy, or ghost networks.
337. Read `../domains/primary-care-panel-appointment-access-continuity/README.md` if you are working on primary care, PCP panel, new patient intake, same-day access, annual wellness, chronic follow-up, FQHC, or routine care continuity.
338. Read `../domains/specialist-referral-authorization-navigation-continuity/README.md` if you are working on specialist referrals, referral orders, prior authorization, e-consults, network routing, referral management, referral leakage, or specialist feedback loops.
339. Read `../domains/appointment-availability-wait-time-continuity/README.md` if you are working on appointment availability, wait times, scheduling capacity, cancellation lists, no-show, rescheduling, same-day access, or healthcare wait-time measurement.
340. Read `../domains/outpatient-laboratory-specimen-result-routing-continuity/README.md` if you are working on outpatient lab orders, specimen collection, draw stations, result routing, patient portals, abnormal result follow-up, or diagnostic signal continuity.
341. Read `../domains/diagnostic-imaging-order-scheduling-report-continuity/README.md` if you are working on diagnostic imaging orders, radiology scheduling, CT/MRI/ultrasound/X-ray access, imaging reports, DICOM/PACS, critical result routing, or image sharing.
342. Read `../domains/ambulatory-procedure-surgery-center-continuity/README.md` if you are working on ambulatory surgery centers, outpatient procedures, endoscopy, infusion centers, pre-op workflows, escorts, recovery observation, or post-procedure follow-up.
343. Read `../domains/after-hours-urgent-care-triage-continuity/README.md` if you are working on after-hours care, urgent care, nurse advice lines, retail clinics, tele-triage, same-day advice, ED diversion, or non-emergency time-window failures.
344. Read `../domains/health-insurance-enrollment-renewal-continuity/README.md` if you are working on health insurance enrollment, renewal, open enrollment, special enrollment periods, Medicaid/Marketplace transitions, premium payment, or coverage gaps.
345. Read `../domains/insurance-eligibility-benefits-verification-continuity/README.md` if you are working on eligibility checks, benefits verification, active coverage, deductible/copay/coinsurance, out-of-pocket maximum, network status, or coverage limits.
346. Read `../domains/medical-service-prior-authorization-utilization-management-continuity/README.md` if you are working on medical-service prior authorization, utilization management, medical necessity review, coverage criteria, peer review, or authorization delays.
347. Read `../domains/claims-adjudication-eob-denial-continuity/README.md` if you are working on claims adjudication, EOBs, claim denials, coordination of benefits, resubmission, appeal windows, or payer payment loops.
348. Read `../domains/patient-billing-payment-plan-continuity/README.md` if you are working on patient billing, statements, patient responsibility, payment plans, billing inquiries, collections handoff, or billing readability.
349. Read `../domains/price-transparency-good-faith-estimate-continuity/README.md` if you are working on hospital price transparency, payer transparency, good faith estimates, shoppable services, machine-readable files, or bill-estimate mismatch.
350. Read `../domains/surprise-billing-balance-bill-protection-continuity/README.md` if you are working on No Surprises Act, balance billing, out-of-network emergency care, air ambulance, notice/consent, or surprise-bill complaints.
351. Read `../domains/charity-care-financial-assistance-medical-debt-continuity/README.md` if you are working on hospital financial assistance, charity care, limitation on charges, billing and collections, payment plans, medical debt, or extraordinary collection actions.
352. Read `../domains/patient-portal-account-message-continuity/README.md` if you are working on patient portals, secure messaging, notification routing, proxy access, patient-facing APIs, or healthcare account/message continuity.
353. Read `../domains/medical-record-access-amendment-release-continuity/README.md` if you are working on HIPAA record access, amendment, release of information, information blocking, USCDI/FHIR patient access, or record portability.
354. Read `../domains/clinical-results-notification-followup-continuity/README.md` if you are working on clinical results notification, abnormal results, critical values, incidental findings, diagnostic safety, or follow-up tracking.
355. Read `../domains/informed-consent-refusal-shared-decision-continuity/README.md` if you are working on informed consent, informed refusal, shared decision-making, decision aids, risk communication, or medical choice documentation.
356. Read `../domains/healthcare-language-interpreter-effective-communication-continuity/README.md` if you are working on healthcare interpreter services, LEP, translated materials, CLAS, auxiliary communication, or effective communication.
357. Read `../domains/healthcare-disability-accommodation-accessibility-continuity/README.md` if you are working on healthcare disability accommodation, auxiliary aids, accessible medical diagnostic equipment, ADA/Section 504 healthcare access, or reasonable modification.
358. Read `../domains/patient-grievance-complaint-ombuds-continuity/README.md` if you are working on patient grievance, hospital complaint, state survey agency, ombudsman, quality complaint, or healthcare complaint routing.
359. Read `../domains/healthcare-civil-rights-nondiscrimination-continuity/README.md` if you are working on Section 1557, healthcare nondiscrimination, HHS OCR civil rights, healthcare bias, or protected-characteristic access barriers.
360. Read `../domains/emergency-contact-next-of-kin-notification-continuity/README.md` if you are working on emergency contacts, next of kin, authorized contacts, caregiver notification, or urgent support-network handoff.
361. Read `../domains/personal-health-record-emergency-summary-continuity/README.md` if you are working on personal health records, emergency summaries, wallet cards, patient-maintained records, Blue Button exports, or minimum emergency health data.
362. Read `../domains/medical-id-allergy-critical-alert-continuity/README.md` if you are working on medical ID, allergy alerts, critical condition alerts, emergency phone/wearable health profiles, or visible urgent health warnings.
363. Read `../domains/medication-list-implant-device-emergency-continuity/README.md` if you are working on medication lists, high-risk medications, implant/device cards, UDI, device constraints, or emergency medication/device transfer.
364. Read `../domains/chronic-condition-emergency-action-plan-continuity/README.md` if you are working on chronic-condition emergency action plans, symptom zones, escalation paths, school/work action plans, or disaster interruption of chronic care.
365. Read `../domains/immunization-record-proof-continuity/README.md` if you are working on vaccination records, immunization registries, vaccine proof, school/work/travel immunization documentation, or record portability.
366. Read `../domains/organ-donor-registry-anatomical-gift-continuity/README.md` if you are working on organ donor registry, anatomical gift, donor designation, state registry, transplant-system identity handoff, or post-death donation intent.
367. Read `../domains/access-functional-needs-emergency-registry-continuity/README.md` if you are working on access and functional needs, special needs registries, medical needs registries, evacuation support, power-dependent devices, or disaster accessibility planning.
368. Read `../domains/death-certificate-registration-cause-of-death-record-continuity/README.md` if you are working on death certificates, death registration, cause-of-death records, certified copies, medical certification, or vital statistics.
369. Read `../domains/funeral-cremation-burial-disposition-continuity/README.md` if you are working on funeral services, cremation, burial, body disposition, price disclosure, funeral permits, or remains transport.
370. Read `../domains/cemetery-memorial-remains-location-continuity/README.md` if you are working on cemetery plots, grave markers, columbarium, ashes/remains location, memorial records, or cemetery maintenance.
371. Read `../domains/bereavement-leave-grief-support-continuity/README.md` if you are working on bereavement leave, grief support, EAP, peer support, school/work adjustment, or survivor recovery after death.
372. Read `../domains/survivor-benefits-death-notification-continuity/README.md` if you are working on death reporting, survivor benefits, Social Security survivor benefits, VA survivor benefits, employer benefits, or pension notifications.
373. Read `../domains/life-insurance-beneficiary-claim-continuity/README.md` if you are working on life insurance policies, beneficiary designations, death claims, policy locator systems, group life insurance, or unclaimed benefits.
374. Read `../domains/estate-inventory-asset-liability-handoff-continuity/README.md` if you are working on estate inventory, asset lists, liability lists, executor/personal representative task queues, probate handoff, or creditor notices.
375. Read `../domains/post-death-account-closure-service-cancellation-continuity/README.md` if you are working on post-death account closure, service cancellation, automatic payment stops, deceased-account handling, data export, or identity theft prevention.
376. Read `../domains/loneliness-social-isolation-risk-continuity/README.md` if you are working on loneliness, social isolation, connection quality, relationship risk, help-seeking capacity, or social disconnection as a health and continuity variable.
377. Read `../domains/social-prescribing-community-referral-continuity/README.md` if you are working on social prescribing, link workers, community referrals, closed-loop social support, activity referral, or non-clinical support pathways.
378. Read `../domains/mutual-aid-neighbor-support-network-continuity/README.md` if you are working on mutual aid, neighbor support, informal care, disaster neighbor checks, low-friction help, or community support networks.
379. Read `../domains/volunteering-civic-service-participation-continuity/README.md` if you are working on volunteering, civic service, service participation, social capital, skill-building, or community contribution pathways.
380. Read `../domains/community-mediation-neighbor-conflict-resolution-continuity/README.md` if you are working on community mediation, neighbor conflict, low-level disputes, dialogue, agreement follow-up, or conflict de-escalation infrastructure.
381. Read `../domains/restorative-justice-repair-accountability-continuity/README.md` if you are working on restorative justice, repair, accountability, victim needs, reintegration, or post-harm community continuity.
382. Read `../domains/reputation-defamation-public-trust-repair-continuity/README.md` if you are working on reputation harm, defamation, public trust, correction, complaint pathways, or trust repair.
383. Read `../domains/references-vouching-recommendation-social-capital-continuity/README.md` if you are working on references, vouching, recommendation letters, introductions, social proof, opportunity access, or social-capital conversion.
384. Read `../domains/third-place-belonging-social-participation-continuity/README.md` if you are working on third places, belonging, public libraries, parks, community anchors, social participation, or weak-tie spaces.
385. Read `../domains/purpose-meaning-existential-continuity/README.md` if you are working on purpose, meaning in life, existential well-being, hope, despair, long-term goals, or value orientation as a continuity variable.
386. Read `../domains/spiritual-care-religious-practice-continuity/README.md` if you are working on spiritual care, chaplaincy, religious practice, faith communities, spiritual distress, or conscience/religion continuity.
387. Read `../domains/cultural-heritage-identity-continuity/README.md` if you are working on cultural heritage, language, community memory, minority identity, migration culture, or intergenerational cultural transmission.
388. Read `../domains/arts-creative-expression-participation-continuity/README.md` if you are working on arts participation, creative expression, community arts, creative aging, cultural production, or expressive continuity.
389. Read `../domains/leisure-recreation-restorative-activity-continuity/README.md` if you are working on leisure, recreation, play, hobbies, parks use, restorative activity, non-work time, or recreation access.
390. Read `../domains/narrative-identity-life-review-continuity/README.md` if you are working on narrative identity, life review, reminiscence, autobiography, memory work, life story, or identity reconstruction.
391. Read `../domains/ritual-ceremony-life-transition-continuity/README.md` if you are working on rituals, ceremonies, rites of passage, memorials, life transitions, public recognition, or community recognition.
392. Read `../domains/dignity-personhood-respect-continuity/README.md` if you are working on dignity, personhood, respect, autonomy, non-humiliation, person-centered care, or dehumanization risk.
393. Read `../domains/human-factors-ergonomics-task-system-continuity/README.md` if you are working on human factors, ergonomics, human systems integration, usability engineering, task-system fit, or human-centered design.
394. Read `../domains/cognitive-load-workload-measurement-continuity/README.md` if you are working on cognitive load, NASA-TLX, mental workload, working memory, task complexity, or workload measurement.
395. Read `../domains/fatigue-risk-alertness-continuity/README.md` if you are working on fatigue risk, shift work, long hours, alertness, sleep debt, recovery windows, or fatigue safety.
396. Read `../domains/situational-awareness-decision-environment-continuity/README.md` if you are working on situation awareness, sensemaking, shared mental models, decision support, risk picture, or state dashboards.
397. Read `../domains/handoff-checklist-procedure-reliability-continuity/README.md` if you are working on handoffs, checklists, SOPs, standard work, read-back, briefing, debriefing, or process reliability.
398. Read `../domains/incident-reporting-just-culture-learning-continuity/README.md` if you are working on incident reporting, near misses, just culture, safety culture, RCA/RCA2, corrective actions, or learning systems.
399. Read `../domains/automation-bias-mode-confusion-oversight-continuity/README.md` if you are working on automation bias, mode confusion, overreliance, human override, supervisory control, or meaningful human oversight.
400. Read `../domains/alert-fatigue-interruption-signal-management-continuity/README.md` if you are working on alert fatigue, alarm fatigue, notification fatigue, interruptions, signal prioritization, quiet hours, or escalation routing.
401. Read `../domains/depression-mood-disorder-functioning-continuity/README.md` if you are working on depression, mood disorder, anhedonia, motivation loss, functional impairment, or depression-related service continuity.
402. Read `../domains/anxiety-stress-threat-regulation-continuity/README.md` if you are working on anxiety, chronic stress, threat regulation, avoidance, panic, social anxiety, or stress-related functioning.
403. Read `../domains/trauma-ptsd-adversity-recovery-continuity/README.md` if you are working on trauma, PTSD, adverse childhood experiences, disaster trauma, violence exposure, trauma-informed support, or recovery continuity.
404. Read `../domains/psychosis-reality-testing-community-continuity/README.md` if you are working on psychosis, schizophrenia spectrum, hallucinations, delusions, reality testing, community mental health, or rights-protecting support.
405. Read `../domains/bipolar-mood-episode-stability-continuity/README.md` if you are working on bipolar disorder, mania, hypomania, mood episodes, sleep rhythm instability, impulsive risk, or cyclical functioning.
406. Read `../domains/adhd-executive-function-neurodevelopment-continuity/README.md` if you are working on ADHD, executive function, task initiation, time sense, impulse control, school/work supports, or neurodevelopmental task continuity.
407. Read `../domains/autism-neurodiversity-support-continuity/README.md` if you are working on autism, neurodiversity, sensory differences, communication access, routines, support needs, or inclusive participation.
408. Read `../domains/eating-disorders-nutrition-body-continuity/README.md` if you are working on eating disorders, body image, restrictive eating, binge/purge behavior, nutrition risk, or eating-disorder service continuity.
409. Read `../domains/domestic-violence-coercive-control-safety-continuity/README.md` if you are working on domestic violence, intimate partner violence, coercive control, confidential contact, safe exit, advocacy, or survivor recovery continuity.
410. Read `../domains/sexual-assault-forensic-exam-advocacy-continuity/README.md` if you are working on sexual assault forensic examinations, medical advocacy, evidence boundaries, trauma-informed support, confidential options, or survivor service continuity.
411. Read `../domains/stalking-harassment-protection-order-continuity/README.md` if you are working on stalking, harassment, protection orders, pattern documentation boundaries, notification, enforcement pathways, or safety communication continuity.
412. Read `../domains/victim-witness-rights-notification-continuity/README.md` if you are working on victim-witness rights, case notification, participation rights, protection arrangements, service referral, or justice-process continuity.
413. Read `../domains/crime-victim-compensation-restitution-continuity/README.md` if you are working on crime victim compensation, restitution, medical or counseling costs, funeral costs, lost income, or financial recovery continuity.
414. Read `../domains/survivor-safe-housing-emergency-transfer-continuity/README.md` if you are working on survivor shelter, safe housing, VAWA housing protections, emergency transfer, confidentiality, or housing-stability recovery.
415. Read `../domains/human-trafficking-victim-identification-services-continuity/README.md` if you are working on trafficking victim identification, service referral, protection, labor/sex trafficking support, benefits navigation, or anti-retraumatization boundaries.
416. Read `../domains/missing-persons-unidentified-remains-resolution-continuity/README.md` if you are working on missing persons, unidentified remains, NamUs, family notification, identity resolution, or long-term ambiguous loss continuity.
417. Read `../domains/rental-lease-tenancy-rights-continuity/README.md` if you are working on rental leases, tenancy rights, rent, deposits, notices, renewal, termination, repair responsibility, or lease communication continuity.
418. Read `../domains/eviction-prevention-court-diversion-continuity/README.md` if you are working on eviction prevention, court diversion, mediation, legal-aid referral, rental assistance linkage, eviction records, or housing-loss buffering.
419. Read `../domains/emergency-rental-assistance-arrears-continuity/README.md` if you are working on rent arrears, emergency rental assistance, utility arrears, payment timing, documentation burden, or housing-cost shock continuity.
420. Read `../domains/housing-choice-voucher-public-housing-continuity/README.md` if you are working on Housing Choice Vouchers, public housing, waitlists, inspections, recertification, portability, or subsidized housing continuity.
421. Read `../domains/fair-housing-discrimination-reasonable-accommodation-continuity/README.md` if you are working on fair housing, protected classes, reasonable accommodations, reasonable modifications, service animals, retaliation, or housing discrimination boundaries.
422. Read `../domains/housing-habitability-inspection-code-enforcement-continuity/README.md` if you are working on habitability, NSPIRE, housing inspections, code enforcement, heating, mold, lead, pests, structural safety, or housing-quality continuity.
423. Read `../domains/hud-approved-housing-counseling-navigation-continuity/README.md` if you are working on HUD-approved housing counseling, rental counseling, default or foreclosure counseling, disaster housing counseling, HECM counseling, or anti-scam housing navigation.
424. Read `../domains/manufactured-housing-park-tenure-safety-continuity/README.md` if you are working on manufactured housing, mobile-home parks, lot rent, park rules, park closure, relocation, infrastructure, or manufactured-home tenure safety.
425. Read `../domains/self-represented-litigant-court-self-help-continuity/README.md` if you are working on self-represented litigants, court self-help centers, legal information/advice boundaries, court forms navigation, or procedural literacy.
426. Read `../domains/court-efiling-document-submission-continuity/README.md` if you are working on court e-filing, document submission, paper alternatives, format rejection, timestamps, filing notifications, or fee-waiver interfaces.
427. Read `../domains/remote-hybrid-court-hearing-access-continuity/README.md` if you are working on remote hearings, hybrid court participation, telephonic appearances, connectivity, privacy, interpretation, or hearing accessibility.
428. Read `../domains/court-language-access-interpreter-continuity/README.md` if you are working on court language access, LEP participants, court interpreters, translated notices, language access plans, or interpreter continuity.
429. Read `../domains/court-disability-accommodation-accessibility-continuity/README.md` if you are working on court disability accommodations, ADA court access, auxiliary aids, effective communication, digital access, or accessible jury service.
430. Read `../domains/court-fees-fines-ability-to-pay-continuity/README.md` if you are working on court fees, fines, surcharges, fee waivers, ability-to-pay review, payment plans, collections, or nonpayment consequences.
431. Read `../domains/jury-service-summons-hardship-continuity/README.md` if you are working on jury summons, juror qualification, exemption, deferral, hardship, employer constraints, childcare, transportation, or juror accessibility.
432. Read `../domains/small-claims-civil-dispute-resolution-continuity/README.md` if you are working on small claims, low-value civil disputes, online dispute resolution, mediation, simplified civil procedure, or judgment recovery boundaries.
433. Read `../domains/data-broker-registry-opt-out-deletion-continuity/README.md` if you are working on data brokers, data broker registries, opt-out, deletion requests, authorized agents, or broker enforcement boundaries.
434. Read `../domains/privacy-rights-access-correction-deletion-continuity/README.md` if you are working on privacy rights, data access, correction, deletion, appeal, verification, or data-subject request boundaries.
435. Read `../domains/opt-out-preference-signal-consent-revocation-continuity/README.md` if you are working on opt-out preference signals, Global Privacy Control, consent revocation, privacy preferences, notices, or dark patterns.
436. Read `../domains/commercial-surveillance-adtech-profile-continuity/README.md` if you are working on commercial surveillance, adtech, tracking, profiling, audience segments, or real-time bidding risk.
437. Read `../domains/sensitive-location-data-exposure-continuity/README.md` if you are working on precise location data, sensitive places, geofencing, mobile ad IDs, movement histories, or location broker risk.
438. Read `../domains/biometric-identifier-template-governance-continuity/README.md` if you are working on biometric identifiers, biometric templates, facial recognition, voiceprints, fingerprints, iris scans, liveness, or biometric matching risk.
439. Read `../domains/children-teen-data-privacy-consent-continuity/README.md` if you are working on COPPA, parental consent, age assurance, edtech data, teen privacy, child-directed advertising, or youth data retention.
440. Read `../domains/data-breach-notification-identity-recovery-continuity/README.md` if you are working on breach notification, identity theft recovery, exposed personal information, credit freezes, fraud alerts, or account recovery after data exposure.
441. Read `../domains/content-provenance-authenticity-credential-continuity/README.md` if you are working on content provenance, content credentials, publisher identity, metadata, cryptographic signature, or authenticity verification UX.
442. Read `../domains/synthetic-media-watermarking-disclosure-continuity/README.md` if you are working on synthetic media, AI-generated content, watermarking, disclosure, labeling, detector limitations, or provenance preservation.
443. Read `../domains/ai-impersonation-deepfake-fraud-continuity/README.md` if you are working on AI impersonation, deepfake scams, voice cloning, video impersonation, government/business impersonation, or verification workflows.
444. Read `../domains/voice-call-caller-id-authentication-continuity/README.md` if you are working on caller ID authentication, STIR/SHAKEN, spoofed calls, robocalls, vishing, call blocking, or verified calling.
445. Read `../domains/email-domain-authentication-spoofing-continuity/README.md` if you are working on SPF, DKIM, DMARC, BIMI, phishing, domain spoofing, email authentication, or notification deliverability.
446. Read `../domains/official-web-domain-brand-impersonation-continuity/README.md` if you are working on official domains, brand impersonation, lookalike domains, typosquatting, search-result trust, or fake service entrances.
447. Read `../domains/digital-evidence-preservation-chain-of-custody-continuity/README.md` if you are working on digital evidence, screenshots, metadata, chain of custody, record retention, audit trails, or evidence-handling boundaries.
448. Read `../domains/platform-content-moderation-notice-appeal-continuity/README.md` if you are working on content moderation, notices, statements of reasons, appeals, human review, account restrictions, or transparency reports.
449. Read `../domains/copyright-authorship-registration-licensing-continuity/README.md` if you are working on copyright authorship, registration, licensing, assignments, copyright management information, or AI-assisted authorship boundaries.
450. Read `../domains/dmca-notice-counter-notice-platform-removal-continuity/README.md` if you are working on DMCA notices, counter-notices, designated agents, platform removals, restoration windows, repeat-infringer policies, or copyright strikes.
451. Read `../domains/creative-commons-open-content-license-continuity/README.md` if you are working on Creative Commons licenses, public-domain tools, attribution, share-alike, noncommercial, no-derivatives, or open content reuse.
452. Read `../domains/open-source-software-license-compliance-continuity/README.md` if you are working on SPDX, OSI-approved licenses, open-source license notices, copyleft/permissive licenses, dependency license records, or software distribution boundaries.
453. Read `../domains/trademark-brand-identity-rights-continuity/README.md` if you are working on trademarks, brand identifiers, source identity, confusion risk, registration records, or brand impersonation.
454. Read `../domains/patent-invention-disclosure-maintenance-continuity/README.md` if you are working on patents, invention disclosure, publication, assignment, maintenance fees, prior art records, or technology access.
455. Read `../domains/creator-royalty-rights-metadata-continuity/README.md` if you are working on creator royalties, rights metadata, work identifiers, collective management, usage reports, platform revenue, or attribution-linked income.
456. Read `../domains/ai-training-data-rights-opt-out-provenance-continuity/README.md` if you are working on AI training data rights, dataset provenance, opt-out signals, robots/noai markers, content credentials, or model data-use disclosure.
457. Read `../domains/scholarly-identity-orcid-affiliation-continuity/README.md` if you are working on ORCID, ROR, researcher identity, affiliation continuity, name ambiguity, or durable scholarly attribution.
458. Read `../domains/persistent-identifier-doi-citation-metadata-continuity/README.md` if you are working on DOI, Crossref, DataCite, citation metadata, persistent scholarly objects, or reference stability.
459. Read `../domains/research-data-repository-fair-sharing-continuity/README.md` if you are working on FAIR data, data repositories, NIH DMS, repository selection, metadata, access levels, or reuse boundaries.
460. Read `../domains/research-software-capsule-reproducibility-continuity/README.md` if you are working on research software, CITATION.cff, Software Heritage, Zenodo, executable environments, or computational reproducibility.
461. Read `../domains/preregistration-registered-report-study-plan-continuity/README.md` if you are working on preregistration, registered reports, analysis plans, protocol transparency, deviations, or confirmatory/exploratory claim boundaries.
462. Read `../domains/lab-notebook-protocol-versioning-continuity/README.md` if you are working on lab notebooks, protocols, method versioning, procedural provenance, timestamps, or deviation disclosure.
463. Read `../domains/contributor-role-authorship-attribution-continuity/README.md` if you are working on CRediT, authorship, contributor roles, acknowledgements, responsibility statements, or attribution metadata.
464. Read `../domains/conflict-of-interest-funding-disclosure-continuity/README.md` if you are working on conflicts of interest, funding disclosures, sponsor roles, competing interests, or disclosure updates.
465. Read `../domains/research-artifact-archive-retention-preservation-continuity/README.md` if you are working on research artifact archives, retention, preservation, link rot, format drift, Zenodo, LOCKSS, CLOCKSS, or Software Heritage.
466. Read `../domains/systematic-review-protocol-search-screening-continuity/README.md` if you are working on PRISMA, PROSPERO, systematic review protocols, search strategies, eligibility criteria, screening records, or PRISMA flow diagrams.
467. Read `../domains/risk-of-bias-critical-appraisal-continuity/README.md` if you are working on RoB 2, ROBINS-I, QUADAS-2, PROBAST, CASP, study appraisal, applicability, or bias-domain judgments.
468. Read `../domains/meta-analysis-effect-size-heterogeneity-continuity/README.md` if you are working on effect sizes, fixed/random effects, heterogeneity, prediction intervals, subgroup analysis, or sensitivity analysis.
469. Read `../domains/publication-reporting-bias-detection-continuity/README.md` if you are working on publication bias, selective outcome reporting, trial registry mismatch, outcome switching, small-study effects, or missing studies.
470. Read `../domains/evidence-certainty-grade-summary-findings-continuity/README.md` if you are working on GRADE, evidence certainty, summary-of-findings tables, downgrade reasons, outcome importance, or recommendation prerequisites.
471. Read `../domains/evidence-to-decision-guideline-panel-continuity/README.md` if you are working on GRADE EtD, guideline panels, recommendation strength, benefits/harms, resources, equity, acceptability, or feasibility.
472. Read `../domains/guideline-appraisal-adaptation-localization-continuity/README.md` if you are working on AGREE II, guideline appraisal, adaptation, localization, update status, conflicts, or context fit.
473. Read `../domains/living-evidence-surveillance-update-continuity/README.md` if you are working on living systematic reviews, surveillance searches, evidence update triggers, versioned conclusions, retractions, or stale-claim retirement.
474. Read `../domains/rapid-review-emergency-evidence-triage-continuity/README.md` if you are working on rapid reviews, evidence maps, crisis evidence triage, shortcut disclosure, provisional claims, or expiry dates.
475. Read `../domains/research-misconduct-investigation-correction-continuity/README.md` if you are working on research misconduct definitions, investigation status, institutional findings, integrity correction, or publication action linkage.
476. Read `../domains/retraction-expression-concern-correction-continuity/README.md` if you are working on retractions, expressions of concern, corrections, Crossmark status, withdrawal, updated versions, or reuse decisions after correction.
477. Read `../domains/preprint-versioning-public-review-continuity/README.md` if you are working on preprints, version history, public review, PubPeer, PREreview, medRxiv, bioRxiv, or journal-version linkage.
478. Read `../domains/journal-editorial-policy-peer-review-integrity-continuity/README.md` if you are working on editorial policy, peer review model, open review, registered reports, data availability policy, or correction policy.
479. Read `../domains/predatory-publishing-paper-mill-detection-continuity/README.md` if you are working on predatory journals, paper mills, fake peer review, systematic manipulation, anomalous citation networks, or publication transparency.
480. Read `../domains/citation-network-claim-propagation-continuity/README.md` if you are working on citation context, claim support, reference lineage, citation cascades, misquotation, or citations to retracted work.
481. Read `../domains/research-metrics-incentives-assessment-continuity/README.md` if you are working on DORA, Leiden Manifesto, impact factor, H-index, Altmetrics, Goodhart risk, or responsible research assessment.
482. Read `../domains/replication-reproducibility-many-labs-continuity/README.md` if you are working on replication, reproducibility, Many Labs, registered replication reports, reanalysis, robustness, or failed-replication context.
483. Read `../domains/science-communication-evidence-translation-continuity/README.md` if you are working on science communication, risk communication, public understanding, press releases, uncertainty framing, or evidence translation.
484. Read `../domains/ai-evaluation-benchmark-validity-continuity/README.md` if you are working on AI benchmarks, evaluation validity, contamination risk, task coverage, or metric interpretation.
485. Read `../domains/ai-red-teaming-adversarial-testing-continuity/README.md` if you are working on AI red teaming, adversarial testing, threat modeling, mitigation validation, or residual risk.
486. Read `../domains/ai-incident-reporting-post-deployment-monitoring-continuity/README.md` if you are working on AI incident reporting, post-deployment monitoring, drift alerts, correction actions, or recurrence checks.
487. Read `../domains/ai-data-provenance-contamination-drift-continuity/README.md` if you are working on AI data provenance, contamination, distribution drift, representativeness, or data lineage.
488. Read `../domains/synthetic-data-generation-validation-continuity/README.md` if you are working on synthetic data, privacy validation, utility testing, distribution fidelity, or downstream synthetic-to-real gaps.
489. Read `../domains/ai-model-supply-chain-provenance-release-continuity/README.md` if you are working on model artifact provenance, weights, dependencies, release notes, signing, licensing, or deprecation.
490. Read `../domains/ai-agent-tool-permission-sandbox-continuity/README.md` if you are working on AI agent tools, permission boundaries, sandboxing, human approval, audit logs, rollback, or abort gates.
491. Read `../domains/human-ai-oversight-handoff-accountability-continuity/README.md` if you are working on human-AI oversight, handoff, escalation, override, accountability, appeal, or contestability.
492. Read `../domains/ai-resource-cost-latency-budget-continuity/README.md` if you are working on AI token budgets, compute budgets, latency, rate limits, cost ceilings, caching, fallback, or resource governance.
493. Read `../domains/semiconductor-manufacturing-metrology-continuity/README.md` if you are working on semiconductor manufacturing, metrology, process control, yield, inspection, or fabrication continuity.
494. Read `../domains/semiconductor-advanced-packaging-continuity/README.md` if you are working on advanced packaging, chiplets, HBM, interposers, 2.5D/3D integration, packaging test, or thermal reliability.
495. Read `../domains/chip-design-eda-verification-ip-continuity/README.md` if you are working on chip design, EDA tools, hardware verification, IP reuse, open ISA, or hardware design provenance.
496. Read `../domains/ai-hardware-accelerator-performance-continuity/README.md` if you are working on GPU/TPU/NPU accelerators, MLPerf, hardware benchmark validity, memory bandwidth, interconnect, driver/runtime stacks, or AI hardware availability.
497. Read `../domains/data-center-cooling-water-thermal-continuity/README.md` if you are working on data center cooling, liquid cooling, water usage, PUE/WUE, thermal density, heat reuse, or climate exposure.
498. Read `../domains/large-load-grid-interconnection-transmission-continuity/README.md` if you are working on data center or industrial large loads, interconnection queues, transmission planning, grid upgrades, or load-growth constraints.
499. Read `../domains/grid-scale-energy-storage-flexibility-continuity/README.md` if you are working on grid-scale storage, long-duration storage, demand response, virtual power plants, reserve margins, or grid flexibility.
500. Read `../domains/advanced-nuclear-energy-safety-generation-continuity/README.md` if you are working on advanced nuclear energy, SMRs, licensing, nuclear fuel, waste management, safety oversight, or reliable low-carbon generation.
501. Read `../domains/undersea-cable-internet-backbone-continuity/README.md` if you are working on submarine cables, landing stations, cross-border data flows, route diversity, repair time, or internet backbone resilience.
502. Read `../domains/satellite-communications-spectrum-orbit-continuity/README.md` if you are working on satellite broadband, spectrum, orbital resources, ground stations, space weather exposure, or disaster/remote connectivity.
503. Read `../domains/cardiac-arrest-cpr-defibrillation-continuity/README.md` if you are working on cardiac arrest systems, CPR, AED availability, defibrillation time, EMS resuscitation, ROSC, or post-arrest continuity.
504. Read `../domains/sepsis-shock-early-recognition-resuscitation-continuity/README.md` if you are working on sepsis, septic shock, early recognition, resuscitation, source control, ICU transfer, or post-sepsis continuity.
505. Read `../domains/trauma-system-hemorrhage-control-continuity/README.md` if you are working on trauma systems, hemorrhage control, trauma center access, prehospital triage, massive transfusion, or injury recovery handoff.
506. Read `../domains/intensive-care-organ-support-delirium-continuity/README.md` if you are working on ICU organ support, PADIS/ABCDEF bundles, sedation, delirium, early mobility, family engagement, or post-ICU syndrome.
507. Read `../domains/mechanical-ventilation-respiratory-failure-continuity/README.md` if you are working on acute respiratory failure, oxygenation, ventilation support, ARDS, ventilator-associated harm, weaning, or respiratory recovery.
508. Read `../domains/ecmo-extracorporeal-life-support-continuity/README.md` if you are working on ECMO/ECLS, extracorporeal cardiopulmonary support, bridge-to-recovery, center capacity, transport, complications, or exit paths.
509. Read `../domains/acute-kidney-injury-renal-replacement-continuity/README.md` if you are working on AKI, kidney replacement therapy, CRRT, dialysis access, fluid/electrolyte failure, kidney recovery, or CKD transition.
510. Read `../domains/transfusion-blood-management-hemorrhage-continuity/README.md` if you are working on transfusion, blood availability, patient blood management, massive hemorrhage, coagulation support, or hemovigilance.
511. Read `../domains/overdose-poisoning-reversal-toxicology-continuity/README.md` if you are working on overdose, poisoning, poison centers, toxic exposure reversal, naloxone access, respiratory depression, or recovery linkage.
512. Read `../domains/burn-injury-critical-care-rehabilitation-continuity/README.md` if you are working on burn injury, burn centers, fluid loss, infection risk, reconstruction, scar, rehabilitation, or social reintegration.
513. Read `../domains/acute-coronary-syndrome-reperfusion-continuity/README.md` if you are working on acute coronary syndrome, chest pain systems, ECG/troponin pathways, reperfusion windows, PCI access, or post-MI recovery.
514. Read `../domains/acute-heart-failure-decompensation-continuity/README.md` if you are working on acute decompensated heart failure, pulmonary edema, congestion, perfusion, hospitalization, discharge handoff, or readmission.
515. Read `../domains/cardiac-arrhythmia-syncope-decompensation-continuity/README.md` if you are working on arrhythmia, syncope, atrial fibrillation, rhythm monitoring, sudden decompensation, stroke/fall risk, or pre-arrest rhythm instability.
516. Read `../domains/venous-thromboembolism-pulmonary-embolism-continuity/README.md` if you are working on DVT, pulmonary embolism, anticoagulation continuity, hospital-acquired VTE, cancer-associated thrombosis, pregnancy-associated thrombosis, or recurrence.
517. Read `../domains/hypertensive-crisis-end-organ-risk-continuity/README.md` if you are working on hypertensive crisis, acute end-organ risk, stroke, heart failure, AKI, aortic syndromes, or blood-pressure follow-up continuity.
518. Read `../domains/diabetic-hyperglycemic-hypoglycemic-crisis-continuity/README.md` if you are working on DKA, HHS, severe hypoglycemia, glucose monitoring breaks, insulin access, emergency metabolic care, or recurrence prevention.
519. Read `../domains/anaphylaxis-allergic-emergency-continuity/README.md` if you are working on anaphylaxis, severe allergy, epinephrine access, allergen exposure contexts, school/workplace plans, EMS handoff, or allergy follow-up.
520. Read `../domains/asthma-copd-exacerbation-airway-continuity/README.md` if you are working on asthma exacerbations, COPD exacerbations, inhaler access, airway emergencies, hospitalization, respiratory support, or pulmonary recovery.
521. Read `../domains/acute-gastrointestinal-bleeding-endoscopy-continuity/README.md` if you are working on upper/lower GI bleeding, transfusion interface, endoscopy access, anticoagulant context, rebleeding, or discharge follow-up.
522. Read `../domains/obstetric-emergency-hemorrhage-hypertension-continuity/README.md` if you are working on obstetric hemorrhage, postpartum hemorrhage, preeclampsia/eclampsia, severe maternal morbidity, transport, blood access, or postpartum follow-up.
523. Read `../domains/hypertension-detection-control-continuity/README.md` if you are working on hypertension screening, BP measurement quality, confirmation, long-term control, follow-up, or end-organ prevention.
524. Read `../domains/lipid-atherosclerosis-risk-management-continuity/README.md` if you are working on lipid testing, ASCVD risk, atherosclerosis prevention, preventive medication evidence, or secondary prevention continuity.
525. Read `../domains/prediabetes-diabetes-prevention-continuity/README.md` if you are working on prediabetes screening, Diabetes Prevention Program referral, retention, behavior support, or transition into chronic diabetes care.
526. Read `../domains/obesity-adiposity-metabolic-risk-continuity/README.md` if you are working on obesity, adiposity, metabolic risk, structural food/activity environments, weight-stigma boundaries, or service access.
527. Read `../domains/tobacco-nicotine-cessation-continuity/README.md` if you are working on tobacco use, nicotine dependence, cessation support, quitlines, policy environments, relapse prevention, or smoke-free infrastructure.
528. Read `../domains/alcohol-use-risk-reduction-continuity/README.md` if you are working on unhealthy alcohol use screening, brief intervention, referral, treatment continuity, relapse prevention, or alcohol-attributable harm reduction.
529. Read `../domains/chronic-kidney-disease-screening-progression-continuity/README.md` if you are working on CKD screening, eGFR, albuminuria, progression risk, cardiorenal-metabolic interaction, or kidney replacement preparation.
530. Read `../domains/cancer-screening-early-detection-continuity/README.md` if you are working on cancer screening, early detection, abnormal result tracking, false positives/negatives, overdiagnosis, or equitable screening access.
531. Read `../domains/osteoporosis-fracture-prevention-bone-health-continuity/README.md` if you are working on osteoporosis screening, fracture risk, bone health services, treatment persistence, post-fracture recovery, or independent living.
532. Read `../domains/fall-risk-prevention-home-safety-continuity/README.md` if you are working on fall-risk screening, home safety, medication/vision/balance/strength interfaces, post-fall review, fear of falling, or independent living.
533. Read `../domains/sleep-disordered-breathing-screening-treatment-continuity/README.md` if you are working on sleep-disordered breathing, obstructive sleep apnea, nocturnal hypoxemia, sleep study access, treatment adherence, or daytime sleepiness.
534. Read `../domains/chronic-insomnia-cbti-access-continuity/README.md` if you are working on chronic insomnia, CBT-I access, behavioral sleep treatment, hypnotic medication risk, daytime impairment, or relapse prevention.
535. Read `../domains/sexual-health-sti-prevention-continuity/README.md` if you are working on sexual health, STI prevention, testing access, treatment referral, partner services, confidentiality, or stigma.
536. Read `../domains/hiv-testing-prep-prevention-continuity/README.md` if you are working on HIV testing, PrEP/PEP referral, ART linkage, retention in care, viral suppression, confidentiality, or HIV stigma.
537. Read `../domains/chronic-viral-hepatitis-screening-liver-protection-continuity/README.md` if you are working on hepatitis B/C screening, confirmatory testing, linkage to care, liver fibrosis, cirrhosis, or liver cancer surveillance.
538. Read `../domains/contraception-family-planning-access-continuity/README.md` if you are working on contraception access, family planning, informed choice, medical eligibility, cost coverage, pharmacy access, or reproductive coercion safeguards.
539. Read `../domains/menstrual-health-cycle-literacy-continuity/README.md` if you are working on menstrual health literacy, period poverty, dysmenorrhea, heavy menstrual bleeding, school/work participation, or referral pathways.
540. Read `../domains/perimenopause-menopause-midlife-health-continuity/README.md` if you are working on perimenopause, menopause symptoms, vasomotor symptoms, sleep disruption, mood, bone health, cardiovascular risk, or workplace participation.
541. Read `../domains/pelvic-floor-continence-function-continuity/README.md` if you are working on pelvic floor function, urinary incontinence, fecal incontinence, pelvic organ prolapse, rehabilitation access, continence supplies, or participation.
542. Read `../domains/skin-cancer-uv-protection-early-detection-continuity/README.md` if you are working on UV exposure, sun protection, skin cancer prevention, early recognition, referral access, occupational outdoor exposure, or skin tone equity.
543. Read `../domains/chronic-pain-functional-restoration-continuity/README.md` if you are working on chronic pain, functional restoration, opioid risk, sleep disruption, work participation, or effective-time loss.
544. Read `../domains/low-back-pain-spine-function-continuity/README.md` if you are working on low back pain, spine function, red-flag routing boundaries, rehabilitation access, work modification, imaging pathway, or recurrence prevention.
545. Read `../domains/osteoarthritis-joint-function-continuity/README.md` if you are working on osteoarthritis, joint pain, stiffness, mobility limitation, assistive devices, rehabilitation, or joint replacement pathway boundaries.
546. Read `../domains/autoimmune-rheumatic-disease-inflammatory-burden-continuity/README.md` if you are working on rheumatoid arthritis, lupus, autoimmune rheumatic disease, chronic inflammation, immunosuppression, organ involvement, or flare burden.
547. Read `../domains/inflammatory-bowel-disease-digestive-continuity/README.md` if you are working on Crohn's disease, ulcerative colitis, flare burden, nutrition, anemia, medication monitoring, surgery pathway, or participation support.
548. Read `../domains/chronic-liver-disease-masld-mash-continuity/README.md` if you are working on MASLD, MASH, fatty liver disease, fibrosis, cirrhosis, liver cancer risk, metabolic comorbidity, or medication safety.
549. Read `../domains/thyroid-disease-endocrine-function-continuity/README.md` if you are working on hypothyroidism, hyperthyroidism, thyroid nodules, thyroid cancer pathway, monitoring continuity, pregnancy overlap, or midlife symptom attribution.
550. Read `../domains/iron-deficiency-anemia-oxygen-carrying-continuity/README.md` if you are working on iron deficiency, anemia, hemoglobin, oxygen carrying capacity, fatigue, menstruation/GI/nutrition overlap, or recovery access.
551. Read `../domains/asthma-copd-maintenance-control-continuity/README.md` if you are working on asthma/COPD long-term control, inhaler access, trigger exposure, pulmonary rehabilitation, activity limitation, or exacerbation prevention.
552. Read `../domains/allergic-atopic-disease-immunologic-burden-continuity/README.md` if you are working on allergic rhinitis, atopic dermatitis, food allergy, allergen exposure, itch/sleep disruption, anaphylaxis boundary, or participation support.
553. Read `../domains/parkinsons-disease-movement-control-continuity/README.md` if you are working on Parkinson's disease, movement control, tremor, rigidity, gait, non-motor symptoms, care burden, or long-term participation.
554. Read `../domains/multiple-sclerosis-demyelination-function-continuity/README.md` if you are working on multiple sclerosis, demyelination, relapse/progression, fatigue, sensory-motor change, cognition, or service continuity.
555. Read `../domains/amyotrophic-lateral-sclerosis-motor-neuron-continuity/README.md` if you are working on ALS, motor neuron degeneration, weakness, swallowing, breathing, communication, dignity, or care continuity.
556. Read `../domains/huntington-disease-genetic-neurodegeneration-continuity/README.md` if you are working on Huntington disease, genetic neurodegeneration, movement disorder, cognitive/psychiatric change, family risk, or decision capacity.
557. Read `../domains/spinal-muscular-atrophy-motor-neuron-continuity/README.md` if you are working on spinal muscular atrophy, inherited motor neuron disease, respiration, swallowing, mobility support, child development, or long-term care.
558. Read `../domains/muscular-dystrophy-progressive-weakness-continuity/README.md` if you are working on muscular dystrophy, progressive weakness, cardiopulmonary risk, mobility support, school/work participation, or assistive technology.
559. Read `../domains/myasthenia-gravis-neuromuscular-junction-continuity/README.md` if you are working on myasthenia gravis, neuromuscular junction transmission, fluctuating weakness, swallowing/breathing risk, or crisis boundaries.
560. Read `../domains/spinal-cord-injury-paralysis-secondary-complications-continuity/README.md` if you are working on spinal cord injury, paralysis, sensory-motor pathways, secondary complications, accessibility, or independent living.
561. Read `../domains/me-cfs-post-exertional-energy-limitation-continuity/README.md` if you are working on ME/CFS, post-exertional malaise, energy limitation, cognitive difficulty, sleep recovery failure, pacing, or participation.
562. Read `../domains/long-covid-post-acute-infection-continuity/README.md` if you are working on Long COVID, post-acute infection, fatigue, brain fog, respiratory/autonomic symptoms, multi-system burden, or service navigation.
563. Read `../domains/breast-cancer-screening-treatment-survivorship-continuity/README.md` if you are working on breast cancer screening, abnormal imaging follow-up, treatment burden, recurrence monitoring, body image, work/family support, or survivorship.
564. Read `../domains/colorectal-cancer-screening-treatment-continuity/README.md` if you are working on colorectal cancer screening, colonoscopy access, abnormal follow-up, treatment burden, ostomy/bowel function, or survivorship support.
565. Read `../domains/lung-cancer-screening-treatment-continuity/README.md` if you are working on lung cancer screening, low-dose CT, smoking exposure, abnormal imaging follow-up, diagnostic delay, treatment burden, or respiratory function.
566. Read `../domains/prostate-cancer-screening-treatment-continuity/README.md` if you are working on prostate cancer screening, PSA controversy, risk stratification, active surveillance, treatment side effects, urinary/sexual function, or quality of life.
567. Read `../domains/cervical-cancer-hpv-prevention-screening-continuity/README.md` if you are working on cervical cancer, HPV prevention, vaccination access, screening, abnormal result tracking, colposcopy access, stigma, or reproductive/sexual health.
568. Read `../domains/ovarian-cancer-symptom-detection-treatment-continuity/README.md` if you are working on ovarian cancer symptoms, diagnostic delay, hereditary risk pathways, treatment burden, recurrence, caregiver load, or quality of life.
569. Read `../domains/pancreatic-cancer-high-risk-detection-treatment-continuity/README.md` if you are working on pancreatic cancer, high-risk detection, diagnostic delay, treatment access, nutrition, pain, caregiver burden, or supportive continuity.
570. Read `../domains/liver-cancer-cirrhosis-surveillance-treatment-continuity/README.md` if you are working on liver cancer, cirrhosis surveillance, viral/metabolic liver disease upstream risk, liver reserve, treatment access, or transplant/supportive pathway boundaries.
571. Read `../domains/childhood-cancer-treatment-survivorship-continuity/README.md` if you are working on childhood cancer treatment burden, family caregiving, school disruption, development, psychosocial support, late effects, or transition to adult survivorship care.
572. Read `../domains/cancer-survivorship-late-effects-continuity/README.md` if you are working on cancer survivorship, late effects, recurrence fear, secondary cancers, organ toxicity, fatigue, work/insurance, or care transition.
573. Read `../domains/dental-caries-prevention-restoration-continuity/README.md` if you are working on dental caries, tooth decay, fluoride/sealants, restorative access, dental pain, school/work absence, or caries prevention.
574. Read `../domains/periodontal-disease-systemic-inflammation-continuity/README.md` if you are working on gum disease, periodontitis, tooth support, tooth loss risk, chronic inflammation, diabetes/smoking overlap, or periodontal maintenance.
575. Read `../domains/tooth-loss-prosthodontic-chewing-continuity/README.md` if you are working on tooth loss, dentures, implants/prosthodontics, chewing efficiency, nutrition, speech, social dignity, or repair access.
576. Read `../domains/dental-pain-emergency-infection-continuity/README.md` if you are working on dental pain, odontogenic infection, abscess, emergency dental access, sleep disruption, work absence, or urgent-care friction.
577. Read `../domains/oral-cancer-mucosal-lesion-early-detection-continuity/README.md` if you are working on oral cancer, oropharyngeal cancer, mucosal lesions, early detection, referral delay, swallowing/speech function, or survivorship.
578. Read `../domains/pediatric-oral-health-development-continuity/README.md` if you are working on pediatric oral health, early childhood caries, school dental programs, family caregiving, nutrition, school attendance, or development.
579. Read `../domains/geriatric-long-term-care-oral-health-continuity/README.md` if you are working on older adult oral health, dentures, xerostomia, swallowing, long-term care oral hygiene, nutrition, or dignity.
580. Read `../domains/dental-care-access-insurance-workforce-continuity/README.md` if you are working on dental insurance, oral health workforce, dental deserts, cost barriers, appointment access, Medicaid/public programs, or language access.
581. Read `../domains/xerostomia-salivary-function-oral-medication-continuity/README.md` if you are working on dry mouth, salivary function, medication oral side effects, radiation oral risk, Sjogren overlap, swallowing, speech, or caries risk.
582. Read `../domains/temporomandibular-orofacial-pain-jaw-function-continuity/README.md` if you are working on TMD, orofacial pain, jaw function, chewing, speech, sleep, stress, chronic pain, or service pathways.
583. Read `../domains/cataract-vision-restoration-continuity/README.md` if you are working on cataracts, lens opacity, glare, visual restoration, cataract surgery access, postoperative follow-up, or reversible vision loss.
584. Read `../domains/glaucoma-visual-field-protection-continuity/README.md` if you are working on glaucoma, eye pressure, optic nerve damage, visual field loss, long-term eye follow-up, or irreversible peripheral vision loss.
585. Read `../domains/diabetic-retinopathy-screening-treatment-continuity/README.md` if you are working on diabetic retinopathy, retinal screening, diabetic macular edema, eye referral, treatment linkage, or diabetes-related vision loss.
586. Read `../domains/age-related-macular-degeneration-central-vision-continuity/README.md` if you are working on age-related macular degeneration, central vision, reading loss, face recognition, retina follow-up, or low-vision transition.
587. Read `../domains/refractive-error-glasses-contact-lens-continuity/README.md` if you are working on refractive error, myopia, hyperopia, astigmatism, presbyopia, glasses, contact lenses, eye exams, or vision correction access.
588. Read `../domains/low-vision-rehabilitation-assistive-technology-continuity/README.md` if you are working on low vision, vision rehabilitation, magnification, orientation and mobility, assistive technology, visual task compensation, or environment adaptation.
589. Read `../domains/dry-eye-ocular-surface-comfort-continuity/README.md` if you are working on dry eye, ocular surface discomfort, screen tolerance, visual fatigue, indoor environment, light sensitivity, or eye-related effective-time burden.
590. Read `../domains/eye-injury-urgent-vision-protection-continuity/README.md` if you are working on eye injury, chemical exposure, foreign body, eye protection, occupational eye safety, sports eye injury, emergency referral, or acute visual loss prevention.
591. Read `../domains/pediatric-vision-screening-amblyopia-continuity/README.md` if you are working on pediatric vision screening, amblyopia, strabismus, childhood refractive risk, family follow-up, school participation, or visual development windows.
592. Read `../domains/retinal-detachment-urgent-referral-continuity/README.md` if you are working on retinal detachment, flashes, floaters, visual curtain symptoms, urgent eye referral, retinal surgery window, or acute retina continuity.
593. Read `../domains/age-related-hearing-loss-hearing-aid-continuity/README.md` if you are working on age-related hearing loss, speech audibility, hearing aids, hearing rehabilitation, listening fatigue, or older-adult communication continuity.
594. Read `../domains/noise-induced-hearing-loss-prevention-continuity/README.md` if you are working on occupational or recreational noise exposure, hearing conservation, ear protection, sound-level monitoring, or preventable hearing loss.
595. Read `../domains/tinnitus-sound-tolerance-sleep-continuity/README.md` if you are working on tinnitus, sound tolerance, sleep disruption, attention burden, distress, or effective-time loss from intrusive sound perception.
596. Read `../domains/otitis-media-child-hearing-development-continuity/README.md` if you are working on childhood ear infections, temporary conductive hearing loss, language development, school participation, or family follow-up.
597. Read `../domains/sudden-hearing-loss-urgent-referral-continuity/README.md` if you are working on sudden sensorineural hearing loss, acute hearing change, urgent referral, treatment window awareness, or unilateral hearing collapse.
598. Read `../domains/cochlear-implant-communication-continuity/README.md` if you are working on cochlear implants, severe-to-profound hearing loss, auditory rehabilitation, device maintenance, mapping, or communication restoration.
599. Read `../domains/newborn-hearing-screening-language-development-continuity/README.md` if you are working on newborn hearing screening, diagnostic follow-up, early intervention, language development, or family navigation.
600. Read `../domains/auditory-processing-listening-effort-continuity/README.md` if you are working on auditory processing, listening effort, speech-in-noise, classroom/workplace listening load, or central auditory function.
601. Read `../domains/hearing-assistive-devices-alerting-access-continuity/README.md` if you are working on assistive listening devices, alerting devices, hearing loops, amplified phones, captions, or acoustic accessibility.
602. Read `../domains/captions-relay-service-communication-access-continuity/README.md` if you are working on captions, real-time transcription, telecommunications relay, video relay, meeting accessibility, or non-auditory communication access.
603. Read `../domains/bppv-positional-vertigo-continuity/README.md` if you are working on benign paroxysmal positional vertigo, positional dizziness, head-movement triggers, recurrence, or task disruption from brief vertigo spells.
604. Read `../domains/menieres-disease-episodic-vertigo-continuity/README.md` if you are working on Meniere's disease, episodic vertigo, fluctuating hearing, tinnitus, aural fullness, attack planning, or unpredictable mobility loss.
605. Read `../domains/vestibular-neuritis-labyrinthitis-acute-vertigo-continuity/README.md` if you are working on acute vestibular neuritis, labyrinthitis, sudden prolonged vertigo, gait instability, nausea burden, or acute recovery continuity.
606. Read `../domains/persistent-postural-perceptual-dizziness-continuity/README.md` if you are working on PPPD, chronic dizziness, visual motion sensitivity, postural threat, avoidance loops, or persistent balance-related participation loss.
607. Read `../domains/vestibular-migraine-dizziness-sensory-load-continuity/README.md` if you are working on vestibular migraine, dizziness with migraine features, sensory load, visual motion intolerance, episodic vertigo, or effective-time loss.
608. Read `../domains/bilateral-vestibular-hypofunction-gaze-gait-stability-continuity/README.md` if you are working on bilateral vestibular hypofunction, oscillopsia, gaze stability, gait instability, dark-surface mobility, or spatial confidence loss.
609. Read `../domains/vestibular-rehabilitation-balance-compensation-continuity/README.md` if you are working on vestibular rehabilitation as a research domain, balance compensation, gaze adaptation, habituation, substitution, or functional recovery pathways.
610. Read `../domains/gait-balance-assessment-fall-screening-continuity/README.md` if you are working on gait and balance assessment, fall screening, mobility confidence, assistive referral boundaries, or balance-related task risk.
611. Read `../domains/motion-sickness-transport-virtual-environment-tolerance-continuity/README.md` if you are working on motion sickness, travel tolerance, simulator sickness, VR/AR vestibular conflict, transport productivity, or virtual-environment access.
612. Read `../domains/vestibular-ototoxicity-medication-chemical-risk-continuity/README.md` if you are working on vestibular ototoxicity, medication or chemical exposure, aminoglycoside-like risk, occupational exposure, or balance loss from toxic injury.
613. Read `../domains/aphasia-language-access-recovery-continuity/README.md` if you are working on aphasia, acquired language loss, language access, reading/writing communication, supported conversation, or recovery participation.
614. Read `../domains/dysarthria-speech-intelligibility-continuity/README.md` if you are working on dysarthria, motor speech intelligibility, speaking fatigue, listener burden, or verbal output reliability.
615. Read `../domains/apraxia-of-speech-motor-planning-continuity/README.md` if you are working on apraxia of speech, speech motor planning, inconsistent errors, childhood apraxia, or verbal output planning reliability.
616. Read `../domains/voice-disorders-phonation-communication-continuity/README.md` if you are working on voice disorders, dysphonia, vocal fatigue, occupational voice, pitch/loudness limits, or phonation continuity.
617. Read `../domains/stuttering-fluency-participation-continuity/README.md` if you are working on stuttering, fluency disorders, anticipation, avoidance, stigma, classroom/work participation, or speaking opportunity loss.
618. Read `../domains/developmental-language-disorder-child-communication-continuity/README.md` if you are working on developmental language disorder, child language delay, vocabulary/grammar, narrative, literacy readiness, or school participation.
619. Read `../domains/speech-sound-disorder-articulation-phonology-continuity/README.md` if you are working on speech sound disorders, articulation, phonology, intelligibility, literacy links, or child speech participation.
620. Read `../domains/augmentative-alternative-communication-aac-continuity/README.md` if you are working on AAC, communication boards, symbols, speech-generating devices, eye-gaze/switch access, or expression-channel redundancy.
621. Read `../domains/social-communication-pragmatic-language-continuity/README.md` if you are working on social communication, pragmatic language, conversational repair, inference, context, or relationship participation.
622. Read `../domains/cognitive-communication-disorder-executive-language-continuity/README.md` if you are working on cognitive-communication disorder, executive language, attention/memory in conversation, organization, topic maintenance, or complex communication support.
623. Read `../domains/oropharyngeal-dysphagia-swallow-safety-continuity/README.md` if you are working on oropharyngeal dysphagia, swallow safety, airway protection, residue, cough response, eating efficiency, or swallow fatigue.
624. Read `../domains/esophageal-dysphagia-motility-obstruction-continuity/README.md` if you are working on esophageal dysphagia, food sticking, motility, obstruction, reflux burden, eating avoidance, or weight-risk continuity.
625. Read `../domains/aspiration-pneumonia-airway-protection-continuity/README.md` if you are working on aspiration, oral load, airway protection, aspiration pneumonia, lung-risk pathways, or care process risk.
626. Read `../domains/choking-foreign-body-airway-risk-continuity/README.md` if you are working on choking, food or foreign-body airway obstruction, public mealtime risk, child/older-adult choking risk, or time-sensitive airway boundary.
627. Read `../domains/texture-modified-diet-thickened-liquid-continuity/README.md` if you are working on texture-modified diets, thickened liquids, IDDSI, kitchen execution, labeling, hydration burden, or dysphagia food-interface continuity.
628. Read `../domains/enteral-feeding-tube-nutrition-continuity/README.md` if you are working on feeding tubes, enteral nutrition, formula supply, tube/device dependence, pump access, caregiver burden, or non-oral nutrition pathways.
629. Read `../domains/pediatric-feeding-swallowing-development-continuity/README.md` if you are working on pediatric feeding, child swallowing, oral-motor development, sensory feeding burden, growth, caregiver stress, or school/daycare eating participation.
630. Read `../domains/post-stroke-dysphagia-screening-recovery-continuity/README.md` if you are working on post-stroke dysphagia, swallow screening, aspiration risk, stroke recovery nutrition, rehabilitation referral, or dysphagia recovery trajectory.
631. Read `../domains/neurodegenerative-dysphagia-nutrition-continuity/README.md` if you are working on dysphagia in Parkinson's, ALS, dementia, Huntington disease, MS, progressive neurological disease, nutrition decline, or advance decision boundaries.
632. Read `../domains/feeding-assistance-mealtime-dignity-continuity/README.md` if you are working on feeding assistance, mealtime dignity, long-term care meals, adaptive utensils, caregiver timing, social meals, or assisted eating participation.
633. Read `../domains/urinary-tract-infection-pyelonephritis-urosepsis-continuity/README.md` if you are working on urinary tract infection, recurrent UTI, pyelonephritis, urosepsis, antimicrobial exposure, or infection-to-systemic-risk continuity.
634. Read `../domains/catheter-associated-uti-device-infection-continuity/README.md` if you are working on urinary catheters, CAUTI, device-associated infection, dwell time, infection control, or catheter-related participation burden.
635. Read `../domains/urinary-retention-bladder-emptying-continuity/README.md` if you are working on urinary retention, bladder emptying, obstruction, neurogenic bladder signals, catheter dependence, or renal-backpressure risk.
636. Read `../domains/overactive-bladder-nocturia-sleep-continuity/README.md` if you are working on urgency, frequency, nocturia, sleep fragmentation, fall risk, restroom planning, or effective-time loss from bladder symptoms.
637. Read `../domains/kidney-stone-obstruction-renal-colic-continuity/README.md` if you are working on kidney stones, renal colic, urinary obstruction, infection overlap, recurrence, acute-care access, or renal function disruption.
638. Read `../domains/benign-prostatic-hyperplasia-luts-continuity/README.md` if you are working on BPH, lower urinary tract symptoms, nocturia, retention risk, urinary infections, or quality-of-life burden.
639. Read `../domains/urinary-diversion-urostomy-supplies-continuity/README.md` if you are working on urinary diversion, urostomy supplies, pouch systems, skin barriers, leakage risk, or continence-related dignity infrastructure.
640. Read `../domains/dialysis-access-vascular-peritoneal-continuity/README.md` if you are working on dialysis access, fistula/graft/catheter pathways, peritoneal access, maturation failure, infection, thrombosis, or treatment interruption.
641. Read `../domains/home-dialysis-supply-self-management-continuity/README.md` if you are working on home hemodialysis, peritoneal dialysis, supplies, water/power dependence, training, caregiver burden, or emergency backup continuity.
642. Read `../domains/kidney-transplant-immunosuppression-graft-continuity/README.md` if you are working on kidney transplant, graft function, immunosuppression, rejection, infection risk, medication supply, or long-term transplant governance.
643. Read `../domains/pressure-injury-prevention-repositioning-support-surface-continuity/README.md` if you are working on pressure injuries, immobility, repositioning, support surfaces, moisture, shear, sensory loss, or long-term-care skin integrity.
644. Read `../domains/chronic-wound-venous-diabetic-pressure-ulcer-continuity/README.md` if you are working on chronic wounds, venous ulcers, diabetic ulcers, pressure ulcers, wound chronicity, pain, recurrence, or wound-care burden.
645. Read `../domains/wound-infection-cellulitis-sepsis-continuity/README.md` if you are working on wound infection, cellulitis, skin/soft-tissue infection, spreading infection, sepsis risk, or infection escalation from a skin boundary.
646. Read `../domains/diabetic-foot-ulcer-amputation-prevention-continuity/README.md` if you are working on diabetic foot, neuropathy, foot ulcers, peripheral artery disease, infection, footwear barriers, or amputation-prevention continuity.
647. Read `../domains/burn-wound-aftercare-scar-function-continuity/README.md` if you are working on burn aftercare, burn wounds, scar, contracture, pain, thermoregulation, rehabilitation, or post-burn function.
648. Read `../domains/surgical-wound-dehiscence-ssi-continuity/README.md` if you are working on surgical wounds, incision closure, dehiscence, surgical site infection, discharge handoff, follow-up, or readmission risk.
649. Read `../domains/incontinence-associated-dermatitis-moisture-skin-continuity/README.md` if you are working on incontinence-associated dermatitis, moisture-associated skin damage, urine/stool exposure, cleansing, barrier products, or skin dignity.
650. Read `../domains/eczema-atopic-dermatitis-itch-sleep-continuity/README.md` if you are working on eczema, atopic dermatitis, itch, barrier dysfunction, sleep disruption, allergy burden, or effective-time loss from skin inflammation.
651. Read `../domains/psoriasis-inflammatory-skin-systemic-burden-continuity/README.md` if you are working on psoriasis, systemic inflammatory skin burden, itch/pain, comorbidities, stigma, treatment continuity, or participation loss.
652. Read `../domains/skin-care-supplies-dressings-barrier-products-continuity/README.md` if you are working on wound dressings, skin barriers, cleansers, incontinence supplies, DME supply, coverage, inventory, or skin-care material continuity.
653. Read `../domains/bathroom-bathing-toileting-transfer-fall-safety-continuity/README.md` if you are working on bathroom bathing, toileting transfers, wet-floor fall risk, grab-bar/shower-seat evidence, or home-care dignity boundaries.
654. Read `../domains/stairs-steps-handrail-threshold-fall-safety-continuity/README.md` if you are working on stairs, steps, handrails, thresholds, uneven surfaces, entry transitions, or trip/fall execution risks.
655. Read `../domains/home-lighting-nighttime-pathway-visibility-continuity/README.md` if you are working on home lighting, nighttime pathways, visibility, contrast, power outage lighting, or low-light navigation risk.
656. Read `../domains/bedroom-bed-transfer-entrapment-safety-continuity/README.md` if you are working on bed transfer, bed height, entrapment, nighttime toileting, caregiver handoff, or bedroom fall risk.
657. Read `../domains/smoke-alarm-home-fire-escape-readiness-continuity/README.md` if you are working on smoke alarms, home fire escape readiness, warning audibility, evacuation planning, or household fire drills.
658. Read `../domains/carbon-monoxide-alarm-combustion-appliance-safety-continuity/README.md` if you are working on carbon monoxide alarms, combustion appliances, generator misuse, ventilation failure, or invisible toxic exposure.
659. Read `../domains/furniture-tv-tip-over-anchoring-child-safety-continuity/README.md` if you are working on furniture and TV tip-over risk, anchoring, child injury prevention, product stability, or household layout hazards.
660. Read `../domains/household-poison-storage-child-resistant-packaging-continuity/README.md` if you are working on household poison storage, child-resistant packaging, medicine/chemical access, or poison-control evidence boundaries.
661. Read `../domains/window-covering-cord-strangulation-child-safety-continuity/README.md` if you are working on window-covering cords, strangulation risk, nursery safety, product standards, or child home injury prevention.
662. Read `../domains/hot-water-scald-burn-prevention-continuity/README.md` if you are working on hot-water scalds, burn prevention, water temperature governance, bathing/kitchen burn risk, or household thermal injury.
663. Read `../domains/drowning-water-safety-supervision-continuity/README.md` if you are working on drowning prevention, water safety, supervision systems, open water, pool exposure, or non-fatal drowning risk.
664. Read `../domains/pool-spa-barrier-drain-entrapment-safety-continuity/README.md` if you are working on pool or spa barriers, gates, drain entrapment, suction hazards, or aquatic facility safety.
665. Read `../domains/boating-life-jacket-watercraft-safety-continuity/README.md` if you are working on boating safety, life jackets, personal watercraft, watercraft incidents, weather exposure, or recreational water mobility.
666. Read `../domains/child-passenger-safety-car-seat-restraint-continuity/README.md` if you are working on child passenger safety, car seats, booster seats, seat belts, restraint systems, or child traffic injury prevention.
667. Read `../domains/bicycle-helmet-wheeled-sports-head-injury-prevention-continuity/README.md` if you are working on bicycle helmets, wheeled sports, skating, scooters, micromobility head injury, or recreational TBI prevention.
668. Read `../domains/playground-surface-equipment-fall-injury-prevention-continuity/README.md` if you are working on playground equipment, surfacing, fall heights, child play safety, public playgrounds, or equipment maintenance evidence boundaries.
669. Read `../domains/sports-concussion-return-to-play-protocol-continuity/README.md` if you are working on sports concussion, return-to-play, return-to-learn, school sports, coach protocols, or youth head injury governance.
670. Read `../domains/infant-safe-sleep-suid-risk-reduction-continuity/README.md` if you are working on infant safe sleep, SUID/SIDS risk reduction, sleep environment, caregiver education, or early-life sleep safety.
671. Read `../domains/firearm-safe-storage-injury-prevention-continuity/README.md` if you are working on firearm injury prevention, safe storage as public-health evidence, child access prevention, suicide-risk interfaces, or violence-risk boundaries.
672. Read `../domains/atv-off-highway-vehicle-injury-prevention-continuity/README.md` if you are working on ATV/OHV injury prevention, off-highway vehicles, rollover risk, youth riding, recreational vehicle injuries, or product-safety boundaries.
673. Read `../domains/emergency-supply-kit-go-bag-rotation-continuity/README.md` if you are working on emergency kits, go bags, disaster supply rotation, household readiness, basic supplies, or service interruption self-sustainment.
674. Read `../domains/family-emergency-communication-reunification-continuity/README.md` if you are working on family emergency communication, reunification, out-of-area contacts, school pickup, caregiver handoff, or household disaster coordination.
675. Read `../domains/evacuation-route-transportation-shelter-plan-continuity/README.md` if you are working on evacuation planning, transportation, shelter access, route redundancy, mobility barriers, or disaster displacement logistics.
676. Read `../domains/shelter-in-place-clean-air-room-indoor-protection-continuity/README.md` if you are working on shelter-in-place, clean air rooms, indoor air protection, wildfire smoke, chemical release boundaries, or indoor waiting safety.
677. Read `../domains/backup-power-battery-generator-safety-continuity/README.md` if you are working on backup power, batteries, generator safety, power outages, charging, carbon monoxide risk, or electricity-dependent continuity.
678. Read `../domains/emergency-food-water-storage-treatment-continuity/README.md` if you are working on emergency food, water storage, water treatment, food safety during disasters, refrigeration failure, or disaster nutrition inputs.
679. Read `../domains/refrigerated-medication-medical-device-power-outage-continuity/README.md` if you are working on refrigerated medicines, medical devices during outages, electricity-dependent medical equipment, prescription continuity, or power-dependent treatment.
680. Read `../domains/emergency-financial-document-cash-readiness-continuity/README.md` if you are working on emergency documents, disaster financial readiness, cash access, insurance records, identity papers, or recovery paperwork.
681. Read `../domains/disability-access-functional-needs-personal-preparedness-continuity/README.md` if you are working on disability preparedness, access and functional needs, assistive technology, service animals, accessible alerts, or support networks.
682. Read `../domains/older-adult-caregiver-disaster-preparedness-continuity/README.md` if you are working on older adults in disasters, caregiver preparedness, medication continuity, mobility limits, social isolation, or late-life disaster risk.
683. Read `../domains/disaster-individual-assistance-benefits-navigation-continuity/README.md` if you are working on disaster individual assistance, DisasterAssistance.gov, FEMA IA, applications, appeals, benefits navigation, or post-disaster resource recovery.
684. Read `../domains/disaster-temporary-housing-displacement-recovery-continuity/README.md` if you are working on disaster temporary housing, displacement, rental assistance, direct housing, shelter-to-housing transitions, or long-term housing recovery.
685. Read `../domains/disaster-recovery-center-service-access-continuity/README.md` if you are working on disaster recovery centers, mobile DRCs, service access, multi-agency windows, document correction, or recovery referral interfaces.
686. Read `../domains/disaster-case-management-long-term-recovery-continuity/README.md` if you are working on disaster case management, long-term recovery groups, unmet needs, service referrals, recovery plans, or VOAD-style coordination.
687. Read `../domains/disaster-unemployment-income-disruption-continuity/README.md` if you are working on disaster unemployment assistance, job interruption, self-employment disruption, income loss, or recovery-period cash flow.
688. Read `../domains/disaster-legal-aid-rights-claims-continuity/README.md` if you are working on disaster legal services, tenant rights, insurance claims boundaries, document replacement, consumer fraud, or legal aid referrals.
689. Read `../domains/disaster-debris-waste-sanitation-cleanup-continuity/README.md` if you are working on disaster debris, waste, sanitation cleanup, hazardous materials, post-disaster public health, or debris removal governance.
690. Read `../domains/post-flood-mold-moisture-indoor-recovery-continuity/README.md` if you are working on post-flood mold, moisture, indoor air, housing returnability, dampness, respiratory burden, or cleanup evidence boundaries.
691. Read `../domains/disaster-behavioral-health-distress-recovery-continuity/README.md` if you are working on disaster behavioral health, distress, trauma stress, crisis counseling, disaster hotlines, or recovery-period sleep and coping.
692. Read `../domains/disaster-volunteer-donations-management-continuity/README.md` if you are working on disaster volunteers, donation management, unsolicited donations, VOAD, resource matching, or disaster social-support logistics.
693. Read `../domains/outbreak-case-investigation-contact-tracing-continuity/README.md` if you are working on outbreak case investigation, contact tracing, exposure notification, privacy, or public-health service referral.
694. Read `../domains/isolation-quarantine-work-school-continuity/README.md` if you are working on isolation, quarantine, sick leave, return-to-work, return-to-school, remote alternatives, or caregiving continuity during outbreaks.
695. Read `../domains/community-testing-screening-access-continuity/README.md` if you are working on community testing, screening access, at-home tests, result reporting, testing sites, or outbreak observation interfaces.
696. Read `../domains/vaccination-campaign-booster-delivery-continuity/README.md` if you are working on vaccination campaigns, booster delivery, appointment systems, cold chain, outreach, high-risk coverage, or immunization access equity.
697. Read `../domains/mask-respirator-source-control-fit-access-continuity/README.md` if you are working on masks, respirators, source control, fit/access, respiratory protection, or public-place airborne risk control.
698. Read `../domains/indoor-ventilation-filtration-outbreak-control-continuity/README.md` if you are working on ventilation, filtration, air cleaning, CO2 proxy metrics, indoor airborne exposure, or outbreak building operations.
699. Read `../domains/school-workplace-outbreak-operations-continuity/README.md` if you are working on school operations, workplace operations, sick leave, absence, remote substitution, layered controls, or outbreak organizational continuity.
700. Read `../domains/healthcare-surge-triage-capacity-continuity/README.md` if you are working on healthcare surge, bed capacity, staffing, triage frameworks, crisis standards, transfer networks, or delayed-care risk during outbreaks.
701. Read `../domains/medical-countermeasure-stockpile-distribution-continuity/README.md` if you are working on medical countermeasures, Strategic National Stockpile, points of dispensing, antivirals, PPE, cold chain, or outbreak distribution equity.
702. Read `../domains/wastewater-pathogen-surveillance-early-warning-continuity/README.md` if you are working on wastewater pathogen surveillance, NWSS, community trend signals, early warning, aggregation, or public-health trigger interfaces.
703. Read `../domains/chemical-release-shelter-evacuation-continuity/README.md` if you are working on chemical-release protective actions, shelter-in-place, evacuation, warning comprehension, transport disruption, or recovery referral.
704. Read `../domains/community-right-to-know-chemical-risk-disclosure-continuity/README.md` if you are working on EPCRA, TRI, Tier II, RMP, chemical-facility disclosure, community right-to-know, or environmental justice.
705. Read `../domains/hazmat-incident-command-emergency-response-continuity/README.md` if you are working on HazMat incident command, NIMS/ICS, unified command, multi-agency coordination, public information, or recovery handoff.
706. Read `../domains/industrial-process-safety-management-continuity/README.md` if you are working on OSHA PSM, EPA RMP, mechanical integrity, management of change, process accident prevention, or incident learning.
707. Read `../domains/toxic-plume-air-monitoring-risk-communication-continuity/README.md` if you are working on toxic plumes, air monitoring, CAMEO/ALOHA, weather interfaces, uncertainty, or public risk communication.
708. Read `../domains/hazwoper-responder-ppe-safety-continuity/README.md` if you are working on HAZWOPER, responder PPE, respiratory protection, heat stress, contamination transfer, or responder staffing continuity.
709. Read `../domains/decontamination-exposure-triage-continuity/README.md` if you are working on exposure decontamination interfaces, medical triage, hospital preparedness, dignity/privacy, or family reunification after hazardous exposure.
710. Read `../domains/hazardous-materials-transportation-erg-continuity/README.md` if you are working on hazardous materials transportation, ERG, identification interfaces, road/rail/pipeline/port incidents, traffic disruption, or community communication.
711. Read `../domains/oil-spill-hazardous-release-response-recovery-continuity/README.md` if you are working on oil spills, hazardous releases, coastal/waterway response, worker safety, fisheries/tourism income disruption, or long-term monitoring.
712. Read `../domains/battery-thermal-runaway-fire-hazard-continuity/README.md` if you are working on lithium-ion batteries, thermal runaway, micro-mobility fires, energy storage incidents, recalls, smoke exposure, or housing/fire interfaces.
713. Read `../domains/severe-weather-watch-warning-risk-communication-continuity/README.md` if you are working on weather watches/warnings/advisories, alert comprehension, warning channels, protective-action translation, or false-alarm trust.
714. Read `../domains/river-flash-flood-warning-evacuation-continuity/README.md` if you are working on river flooding, flash flooding, flood warnings, evacuation triggers, road closure, shelter routing, or flood-return boundaries.
715. Read `../domains/hurricane-storm-surge-evacuation-shelter-continuity/README.md` if you are working on hurricanes, storm surge, evacuation zones, shelter continuity, coastal transport, or post-landfall service disruption.
716. Read `../domains/tornado-warning-safe-room-shelter-continuity/README.md` if you are working on tornado warnings, safe rooms, interior refuge, mobile-home vulnerability, school/workplace sheltering, or short-fuse protective action.
717. Read `../domains/winter-storm-cold-exposure-power-continuity/README.md` if you are working on winter storms, extreme cold, heating failure, power outages, hypothermia risk, generator safety, or road isolation.
718. Read `../domains/drought-water-restriction-household-health-continuity/README.md` if you are working on drought, water restrictions, household water continuity, heat and agricultural stress, or public-health drought impacts.
719. Read `../domains/landslide-mudslide-debris-flow-warning-continuity/README.md` if you are working on landslides, mudslides, debris flows, burn-scar rainfall, slope instability, evacuation warning, or road/lifeline blockage.
720. Read `../domains/wildfire-smoke-clean-air-respiratory-continuity/README.md` if you are working on wildfire smoke, clean-air rooms, AQI/PM2.5, respiratory protection, indoor filtration, or smoke-sensitive populations.
721. Read `../domains/thunderstorm-lightning-outdoor-safety-continuity/README.md` if you are working on thunderstorms, lightning safety, outdoor activity interruption, shelter timing, sports/event operations, or electrical storm exposure.
722. Read `../domains/coastal-flooding-erosion-inundation-continuity/README.md` if you are working on coastal flooding, high-tide flooding, erosion, inundation, road access, property exposure, or coastal service continuity.
723. Read `../domains/child-care-availability-affordability-continuity/README.md` if you are working on child care slots, cost, hours, distance, waitlists, age coverage, or affordability.
724. Read `../domains/child-care-licensing-health-safety-continuity/README.md` if you are working on child care licensing, inspections, health and safety standards, ratios, background checks, or incident transparency.
725. Read `../domains/child-care-subsidy-ccdf-payment-continuity/README.md` if you are working on CCDF, child care subsidies, eligibility, authorization, redetermination, copayments, provider payments, or administrative burden.
726. Read `../domains/head-start-early-head-start-family-support-continuity/README.md` if you are working on Head Start, Early Head Start, early learning, health, nutrition, family engagement, or family support services.
727. Read `../domains/early-intervention-idea-part-c-developmental-services-continuity/README.md` if you are working on IDEA Part C, early intervention, developmental referrals, IFSP, service coordination, or transition.
728. Read `../domains/out-of-school-time-afterschool-summer-learning-continuity/README.md` if you are working on afterschool programs, out-of-school time, summer learning, supervision, meals, transportation, or caregiver schedule continuity.
729. Read `../domains/tribal-health-sovereignty-service-access-continuity/README.md` if you are working on tribal health, IHS, tribal sovereignty, referral care, cultural safety, tribal data sovereignty, or tribal public-health service access.
730. Read `../domains/veterans-health-benefits-navigation-continuity/README.md` if you are working on veterans health care, VA benefits, military-to-civilian transition, service records, veteran housing, employment, family support, or community care navigation.
731. Read `../domains/migrant-seasonal-farmworker-health-housing-continuity/README.md` if you are working on migrant or seasonal farmworker health, agricultural labor, temporary housing, transportation dependence, language access, occupational exposure, or migrant health centers.
732. Read `../domains/territorial-island-health-infrastructure-access-continuity/README.md` if you are working on U.S. territories, island health infrastructure, Medicaid/CHIP territories, medical referral off-island, supply chains, disaster recovery, or public-health infrastructure.
733. Read `../domains/border-community-cross-border-care-continuity/README.md` if you are working on border communities, cross-border families, binational public health, U.S.-Mexico health, care continuity, records, language, or border-service access.
734. Read `../domains/lgbtq-health-identity-affirming-service-continuity/README.md` if you are working on LGBTQ health, identity recognition, nondiscrimination, affirming services, privacy, family/community support, or service access.
735. Read `../domains/runaway-homeless-youth-outreach-shelter-continuity/README.md` if you are working on runaway or homeless youth, street outreach, basic center shelter, transitional living, family mediation, youth service linkage, or youth confidentiality.
736. Read `../domains/foster-care-aging-out-independent-living-continuity/README.md` if you are working on foster-care aging out, Chafee, independent living, extended foster care, education/training vouchers, youth housing transition, Medicaid transition, or identity documents.
737. Read `../domains/juvenile-justice-reentry-aftercare-continuity/README.md` if you are working on juvenile justice reentry, aftercare, community supervision, school re-enrollment, behavioral health linkage, family support, or youth record confidentiality.
738. Read `../domains/transition-age-youth-mental-health-service-continuity/README.md` if you are working on transition-age youth mental health, child-to-adult behavioral-health handoff, school-to-community care, crisis entry points, peer support, consent, confidentiality, or insurance transition.
739. Read `../domains/opportunity-youth-education-employment-pathway-continuity/README.md` if you are working on opportunity youth, disconnected youth, GED/high-school equivalency, alternative education, Job Corps, YouthBuild, workforce pathways, or youth basic-needs support.
740. Read `../domains/pregnant-parenting-youth-family-support-continuity/README.md` if you are working on pregnant or parenting youth, school continuity, Title IX pregnancy boundaries, prenatal/postpartum service linkage, childcare, housing, nutrition benefits, or parenting support.
741. Read `../domains/prenatal-care-access-risk-screening-continuity/README.md` if you are working on prenatal care access, pregnancy entry timing, risk screening, lab or ultrasound follow-up, high-risk referral, transportation, language, insurance, or prenatal privacy.
742. Read `../domains/postpartum-care-recovery-follow-up-continuity/README.md` if you are working on postpartum visits, recovery follow-up, warning signs, pregnancy complication follow-up, coverage, family/work load, or primary-care transition.
743. Read `../domains/lactation-breastfeeding-support-continuity/README.md` if you are working on lactation support, breastfeeding counseling, pumping space/time, WIC breastfeeding support, feeding referral, or work/school breastfeeding boundaries.
744. Read `../domains/preterm-birth-nicu-discharge-transition-continuity/README.md` if you are working on preterm birth, NICU discharge, family education, follow-up, feeding/device boundaries, developmental follow-up, early intervention, or caregiver workload.
745. Read `../domains/pregnancy-loss-stillbirth-bereavement-continuity/README.md` if you are working on miscarriage, stillbirth, pregnancy loss follow-up, bereavement support, work/school adjustment, vital-record interfaces, family communication, or subsequent pregnancy counseling boundaries.
746. Read `../domains/perinatal-mental-health-screening-referral-continuity/README.md` if you are working on perinatal depression/anxiety screening, referral pathways, crisis boundaries, IPV/substance-use interfaces, peer support, language/cultural safety, or warm handoff.
747. Read `../domains/newborn-screening-result-followup-continuity/README.md` if you are working on newborn screening, specimen collection, result routing, abnormal notification, confirmatory referral, state program interfaces, or genetic/privacy boundaries.
748. Read `../domains/well-child-visit-preventive-care-continuity/README.md` if you are working on well-child visits, pediatric medical home, preventive care, growth/development monitoring, anticipatory guidance boundaries, or pediatric referral follow-up.
749. Read `../domains/childhood-immunization-schedule-record-continuity/README.md` if you are working on childhood immunization records, official schedule interfaces, school/childcare proof, reminder/recall systems, IIS records, consent, or vaccine advice boundaries.
750. Read `../domains/developmental-behavioral-screening-referral-continuity/README.md` if you are working on developmental monitoring, behavioral screening, family observations, early intervention referral, language/cultural access, or child data boundaries.
751. Read `../domains/pediatric-lead-screening-environmental-followup-continuity/README.md` if you are working on pediatric blood lead screening, public-health follow-up, housing/water exposure, environmental investigation, remediation handoff, or lead-result interpretation boundaries.
752. Read `../domains/children-youth-special-health-care-needs-care-coordination-continuity/README.md` if you are working on CYSHCN, pediatric medical home, care coordination, specialty referral, school interface, insurance/DME/medication access, or transition to adult care.
684. Enter a domain under `../domains/`.
