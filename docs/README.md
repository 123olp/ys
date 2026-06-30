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
19. Read `reference/research-domain-atlas.md`.
20. Read `reference/research-domain-radar.md` before proposing a new domain.
21. Read `../domains/cellular-reprogramming/README.md` if you are working on cellular rejuvenation or epigenetic reprogramming.
22. Read `../domains/health-data-privacy-governance/README.md` if you are working on sensitive health, genomic, behavioral, neural, or service-use data.
23. Read `../domains/functioning-quality-of-life-outcomes/README.md` if you are defining whether a Human Infra intervention actually improves function or lived experience.
24. Read `../domains/health-economics-value-assessment/README.md` if you are working on disease burden, cost-effectiveness, HTA, or public-value framing.
25. Read `../domains/immunization-public-health-surveillance/README.md` if you are working on immunization, infectious-disease surveillance, infection prevention, AMR, or wastewater signals.
26. Read `../domains/maternal-newborn-child-development/README.md` if you are working on maternal, newborn, child health, growth, or early development.
27. Read `../domains/patient-safety-organizational-learning/README.md` if you are working on patient safety, incident learning, team communication, or care-system harm reduction.
28. Read `../domains/social-determinants-community-vulnerability/README.md` if you are working on social determinants, community vulnerability, environmental justice, local health estimates, or health-related social needs.
29. Read `../domains/public-service-design-accessibility/README.md` if you are working on public digital services, forms, accessibility, customer experience, or service task completion.
30. Read `../domains/emergency-alerts-communications/README.md` if you are working on public alerts, 911/NG911, weather radio, first-responder communications, or crisis communication channels.
31. Read `../domains/disaster-recovery-relief-continuity/README.md` if you are working on disaster recovery, individual assistance, shelters, recovery centers, disaster loans, or relief navigation.
32. Read `../domains/financial-inclusion-payment-systems/README.md` if you are working on accounts, payment systems, remittances, digital financial services, or consumer financial protection.
33. Read `../domains/workforce-employment-services/README.md` if you are working on employment services, workforce development, apprenticeships, occupational information, or job accommodation.
34. Read `../domains/household-emergency-preparedness-resilience/README.md` if you are working on household emergency plans, supplies, medication continuity, backup communication, documents, or special needs.
35. Read `../domains/media-information-literacy-public-libraries/README.md` if you are working on media and information literacy, public libraries, trusted information access, or community learning spaces.
36. Read `../domains/health-workforce-capacity/README.md` if you are working on health workforce supply, distribution, training, retention, workload, or shortage risk.
37. Read `../domains/administrative-burden-procedural-friction/README.md` if you are working on paperwork, proof burden, waiting, renewal, appeal, or procedural friction.
38. Read `../domains/community-health-workers-peer-support/README.md` if you are working on community health workers, peer support, navigators, trusted intermediaries, or referral follow-up.
39. Read `../domains/civic-data-open-government-transparency/README.md` if you are working on open data, public records, FOIA, performance data, metadata, accountability, or public feedback.
40. Read `../domains/education-access-lifelong-learning/README.md` if you are working on education access, adult learning, retraining, basic skills, digital learning, or lifelong learning.
41. Read `../domains/research-infrastructure-open-science-translation/README.md` if you are working on research infrastructure, open science, reproducibility, research data, funding, translational science, or knowledge diffusion.
42. Read `../domains/standards-metrology-quality-infrastructure/README.md` if you are working on standards, metrology, calibration, certification, quality infrastructure, conformity assessment, or interoperability.
43. Read `../domains/cybersecurity-resilience-critical-services/README.md` if you are working on cybersecurity, critical-service resilience, incident response, backup recovery, ransomware risk, or digital continuity.
44. Read `../domains/compute-data-center-ai-infrastructure/README.md` if you are working on compute, data centers, AI infrastructure, chips, energy, water, cloud access, or AI infrastructure governance.
45. Read `../domains/clinical-trials-regulatory-science-translation/README.md` if you are working on clinical trials, regulatory science, real-world evidence, safety monitoring, endpoints, or medical translation.
46. Read `../domains/geospatial-navigation-location-infrastructure/README.md` if you are working on geospatial data, maps, addressing, GPS/GNSS, geocoding, emergency location, or location infrastructure.
47. Read `../domains/weather-climate-observation-forecasting/README.md` if you are working on weather observation, forecasting, climate services, severe weather, or early warning inputs.
48. Read `../domains/building-fire-life-safety-codes/README.md` if you are working on building codes, fire safety, egress, smoke alarms, life safety, or resilient buildings.
49. Read `../domains/manufacturing-repair-capacity/README.md` if you are working on manufacturing, repair, maintenance, spare parts, local production, or critical equipment restoration.
50. Read `../domains/public-procurement-contracting-capacity/README.md` if you are working on public procurement, contracting, supplier management, emergency procurement, transparency, or contract delivery.
51. Read `../domains/animal-health-zoonotic-interface-one-health/README.md` if you are working on animal health, zoonotic risk, veterinary public health, One Health, livestock, wildlife, or animal-health surveillance.
52. Read `../domains/human-animal-bond-companion-care-continuity/README.md` if you are working on companion animals, human-animal bond, pet care routines, family rhythms, or relationship support.
53. Read `../domains/veterinary-care-access-cost-continuity/README.md` if you are working on veterinary access, veterinary cost, emergency veterinary care, low-cost clinics, or animal-care service continuity.
54. Read `../domains/service-animal-disability-access-continuity/README.md` if you are working on service animals, disability access, task assistance, handler rights, or public participation.
55. Read `../domains/pet-identification-microchip-reunification-continuity/README.md` if you are working on pet identification, microchips, tags, registration, lost pets, or reunification systems.
56. Read `../domains/pet-food-medication-supply-safety-continuity/README.md` if you are working on pet food, animal drugs, veterinary prescriptions, recalls, labeling, or supply interruptions.
57. Read `../domains/pet-disaster-evacuation-sheltering-continuity/README.md` if you are working on pets in disasters, evacuation, sheltering, pet supplies, service animals, or post-disaster reunification.
58. Read `../domains/animal-shelter-rescue-rehoming-continuity/README.md` if you are working on animal shelters, rescue, foster care, adoption, rehoming, or owner reunification.
59. Read `../domains/animal-welfare-cruelty-reporting-continuity/README.md` if you are working on animal welfare, cruelty, neglect, hoarding, abandonment, reporting pathways, or humane-law interfaces.
60. Read `../domains/public-health-laboratory-diagnostic-capacity/README.md` if you are working on public health laboratories, diagnostic capacity, laboratory quality, specimen networks, or laboratory surge.
61. Read `../domains/blood-organ-tissue-biovigilance-transplantation/README.md` if you are working on blood supply, organ/tissue donation, transplantation systems, transfusion safety, or biovigilance.
62. Read `../domains/waste-management-hazardous-materials-continuity/README.md` if you are working on solid waste, hazardous waste, medical waste, disposal continuity, or circular material flows.
63. Read `../domains/radiation-nuclear-safety-protection/README.md` if you are working on radiation protection, nuclear safety, radiological monitoring, or radiological emergency governance.
64. Read `../domains/chemical-safety-poison-control-toxicology/README.md` if you are working on chemical safety, toxic exposure, poison centers, toxicology, or chemical risk communication.
65. Read `../domains/critical-minerals-materials-resilience/README.md` if you are working on critical minerals, strategic materials, material substitution, recycling, or upstream technology input resilience.
66. Read `../domains/air-quality-ventilation-exposure-control/README.md` if you are working on air quality, ventilation, filtration, aerosols, smoke, or inhaled exposure control.
67. Read `../domains/food-safety-contamination-control/README.md` if you are working on foodborne hazards, contamination, inspection, traceability, recalls, or outbreak governance.
68. Read `../domains/occupational-exposure-industrial-hygiene/README.md` if you are working on industrial hygiene, workplace exposure, hierarchy of controls, dust, noise, heat, chemicals, or biological hazards.
69. Read `../domains/medical-device-equipment-safety-maintenance/README.md` if you are working on medical device safety, equipment lifecycle, UDI, adverse events, recalls, maintenance, or device cybersecurity.
70. Read `../domains/sterilization-disinfection-infection-control/README.md` if you are working on sterilization, disinfection, reprocessing, environmental infection control, or healthcare-associated infection prevention.
71. Read `../domains/built-environment-accessibility-universal-design/README.md` if you are working on built-environment accessibility, universal design, ADA/ABA standards, public-space access, or physical-path continuity.
72. Read `../domains/clinical-laboratory-diagnostic-quality/README.md` if you are working on clinical laboratory quality, diagnostic testing, CLIA, test reliability, diagnostic stewardship, or lab result quality.
73. Read `../domains/pharmacovigilance-drug-safety-monitoring/README.md` if you are working on pharmacovigilance, adverse event reports, FAERS, postmarket drug safety, labels, REMS, or medication safety signals.
74. Read `../domains/pharmaceutical-quality-supply-integrity/README.md` if you are working on pharmaceutical quality, GMP, substandard/falsified medicines, drug shortages, cold chain, traceability, or supply integrity.
75. Read `../domains/emergency-medical-services-prehospital-care/README.md` if you are working on EMS, prehospital care, dispatch, response time, ambulance systems, or time-critical acute response.
76. Read `../domains/surgical-anesthesia-perioperative-safety/README.md` if you are working on surgical safety, anesthesia safety, perioperative quality, surgical checklist, or preventable surgical complications.
77. Read `../domains/road-traffic-injury-prevention-safe-mobility/README.md` if you are working on road traffic injury prevention, safe system, speed management, vehicle safety, or safe mobility.
78. Read `../domains/rural-health-access-geographic-equity/README.md` if you are working on rural health, geographic access, rural workforce, hospital/pharmacy closure, telehealth, EMS distance, or rural equity.
79. Read `../domains/homelessness-unsheltered-health-continuity/README.md` if you are working on homelessness, unsheltered health, shelters, street outreach, housing continuity, hygiene, safety, or service access.
80. Read `../domains/correctional-health-reentry-continuity/README.md` if you are working on correctional health, incarceration, jail/prison healthcare, reentry, medication continuity, Medicaid transition, or release planning systems.
81. Read `../domains/disability-services-independent-living/README.md` if you are working on disability services, independent living, HCBS, personal assistance, reasonable accommodation, assistive technology, or community integration.
82. Read `../domains/dementia-cognitive-decline-care-continuity/README.md` if you are working on dementia, cognitive decline, Alzheimer’s, caregiver burden, dementia care continuity, safety, dignity, or service navigation.
83. Read `../domains/chronic-infectious-disease-care-continuity/README.md` if you are working on HIV, TB, viral hepatitis, long-course infectious disease care, treatment continuity, stigma, drug resistance, or public-health follow-up.
84. Read `../domains/suicide-crisis-response-continuity/README.md` if you are working on suicide prevention, 988, crisis response, mobile crisis teams, crisis stabilization, follow-up care, or suicide-risk service systems.
85. Read `../domains/substance-use-treatment-recovery-continuity/README.md` if you are working on substance use disorder treatment, recovery support, overdose prevention, harm reduction governance, peer support, or treatment continuity.
86. Read `../domains/elder-justice-adult-protective-services/README.md` if you are working on elder abuse, Adult Protective Services, elder justice, financial exploitation, neglect, or long-term-care ombudsman systems.
87. Read `../domains/child-protection-family-safety/README.md` if you are working on child protection, child welfare, child abuse and neglect prevention, ACEs, family safety, or trauma-informed child services.
88. Read `../domains/fraud-scams-consumer-protection/README.md` if you are working on scams, fraud, phishing, identity theft recovery, consumer complaints, consumer protection, or fraud risk communication.
89. Read `../domains/online-safety-digital-harm-prevention/README.md` if you are working on online safety, cyberbullying, online harassment, digital abuse, child online protection, platform reporting, or digital harm recovery.
90. Read `../domains/rare-disease-diagnostic-odyssey-care-coordination/README.md` if you are working on rare diseases, undiagnosed disease, diagnostic odyssey, genetic testing pathways, expert referral, patient registries, or orphan products.
91. Read `../domains/multimorbidity-polypharmacy-care-coordination/README.md` if you are working on multimorbidity, multiple chronic conditions, polypharmacy, medication reconciliation, treatment burden, or complex care plans.
92. Read `../domains/care-transitions-discharge-continuity/README.md` if you are working on discharge planning, care transitions, handoffs, medication reconciliation, follow-up, readmissions, or cross-setting care continuity.
93. Read `../domains/home-health-hospice-palliative-care-continuity/README.md` if you are working on home health, serious illness care, palliative care, hospice, symptom burden, caregiver support, or goals-of-care systems.
94. Read `../domains/medical-interpreter-cultural-mediation/README.md` if you are working on medical interpreting, language assistance, CLAS, LEP, culturally appropriate care, informed-consent understanding, or clinical communication access.
95. Read `../domains/patient-advocacy-shared-decision-making/README.md` if you are working on patient advocacy, shared decision-making, decision aids, informed consent, patient participation, treatment burden, or preference-sensitive care.
96. Read `../domains/life-logging-personal-archives-continuity/README.md` if you are working on life logging, personal digital archives, metadata, backup, migration, long-term readability, or personal history continuity.
97. Read `../domains/digital-legacy-data-succession/README.md` if you are working on digital legacy, account succession, fiduciary access, disabled-agent access, data handoff, or digital asset continuity.
98. Read `../domains/wearables-continuous-sensing-personal-informatics/README.md` if you are working on wearables, continuous sensing, self-tracking, remote data acquisition, personal informatics, or feedback loops.
99. Read `../domains/personal-knowledge-management-cognitive-offloading/README.md` if you are working on personal knowledge management, cognitive offloading, external memory, notes, retrieval, knowledge bases, or AI-assisted context recovery.
100. Read `../domains/brain-computer-interface-neurotechnology-governance/README.md` if you are working on brain-computer interfaces, neural recording, neural stimulation, neural data, neuroethics, or BCI governance.
101. Read `../domains/robotics-embodied-assistance-care-automation/README.md` if you are working on robotics, embodied assistance, exoskeletons, care automation, service robots, or rehabilitation robots.
102. Read `../domains/armed-conflict-civilian-protection-ihl/README.md` if you are working on armed conflict, IHL, civilian protection, humanitarian access, or conflict service continuity.
103. Read `../domains/peacebuilding-conflict-prevention-social-cohesion/README.md` if you are working on peacebuilding, conflict prevention, social cohesion, mediation, or fragility.
104. Read `../domains/continuity-of-government-public-administration-resilience/README.md` if you are working on continuity of government, public administration resilience, essential functions, or public service recovery.
105. Read `../domains/telecommunications-network-resilience-continuity/README.md` if you are working on telecommunications networks, emergency communications, broadband resilience, backup power, or outage recovery.
106. Read `../domains/macroeconomic-monetary-fiscal-stability/README.md` if you are working on inflation, employment, fiscal space, public debt, financial stability, or macro resource constraints.
107. Read `../domains/anti-corruption-public-integrity-accountability/README.md` if you are working on anti-corruption, public integrity, transparency, audit, accountability, or public resource capture.
108. Read `../domains/agricultural-production-food-system-resilience/README.md` if you are working on agricultural production, crop/livestock systems, irrigation, seeds, fertilizer, farm labor, or climate adaptation.
109. Read `../domains/soil-health-land-degradation-drought-resilience/README.md` if you are working on soil health, land degradation, erosion, salinization, desertification, drought, or land restoration.
110. Read `../domains/water-resources-hydrology-flood-drought-management/README.md` if you are working on water resources, hydrology, river basins, groundwater, reservoirs, floods, droughts, or water security.
111. Read `../domains/biodiversity-ecosystem-services-resilience/README.md` if you are working on biodiversity, ecosystem services, pollination, filtration, cooling, habitat, or ecosystem restoration.
112. Read `../domains/wildfire-landscape-fire-resilience/README.md` if you are working on wildfire, landscape fire risk, WUI, smoke exposure, evacuation interfaces, or community fire resilience.
113. Read `../domains/freight-logistics-port-cold-chain-continuity/README.md` if you are working on freight logistics, ports, warehousing, cold chain, key material delivery, or last-mile continuity.
114. Read `../domains/coastal-marine-resilience-blue-economy-continuity/README.md` if you are working on coastal resilience, sea level rise, storm surge, coastal economies, marine ecosystem buffers, or blue economy continuity.
115. Read `../domains/fisheries-aquatic-food-systems-continuity/README.md` if you are working on fisheries, aquaculture, aquatic foods, seafood nutrition, small-scale fisheries, or aquatic food supply continuity.
116. Read `../domains/dams-levees-flood-control-infrastructure-safety/README.md` if you are working on dam safety, levee safety, flood-control assets, drainage infrastructure, or flood-infrastructure failure risk.
117. Read `../domains/public-works-civil-infrastructure-asset-management/README.md` if you are working on roads, bridges, tunnels, drainage, public works maintenance, civil infrastructure asset management, or maintenance backlog.
118. Read `../domains/urban-planning-land-use-zoning-resilience/README.md` if you are working on urban planning, land use, zoning, service layout, spatial equity, or resilience planning.
119. Read `../domains/green-blue-infrastructure-urban-nature-cooling/README.md` if you are working on urban green spaces, tree canopy, stormwater green infrastructure, blue-green corridors, heat island mitigation, or nature-based urban cooling.
120. Read `../domains/electric-grid-reliability-resilience-continuity/README.md` if you are working on electric grid reliability, distribution resilience, outages, restoration, critical loads, or grid lifeline continuity.
121. Read `../domains/water-wastewater-utility-service-continuity/README.md` if you are working on drinking-water utilities, wastewater systems, water quality, sewer service, pump stations, or water utility resilience.
122. Read `../domains/fuel-thermal-energy-service-continuity/README.md` if you are working on heating fuel, cooling energy, gas, propane, district energy, backup fuel, or thermal service continuity.
123. Read `../domains/public-transit-service-operations-continuity/README.md` if you are working on bus, rail, ferry, paratransit, service reliability, transit assets, operations workforce, or service restoration.
124. Read `../domains/critical-infrastructure-lifeline-interdependency-resilience/README.md` if you are working on community lifelines, national critical functions, cascading failures, infrastructure dependencies, or cross-sector resilience.
125. Read `../domains/utility-affordability-shutoff-protection-continuity/README.md` if you are working on utility bills, arrears, shutoff protection, LIHEAP, Lifeline, energy burden, water affordability, or utility consumer protection.
126. Read `../domains/gene-therapy-genome-editing-delivery-safety/README.md` if you are working on gene therapy, genome editing, delivery vectors, off-target risk, expression control, or long-term follow-up.
127. Read `../domains/biological-age-clocks-biomarker-validation/README.md` if you are working on epigenetic clocks, biological age, biomarker validation, surrogate endpoints, or aging feedback metrics.
128. Read `../domains/multiomics-personal-baseline-systems-biology/README.md` if you are working on genomics, epigenomics, transcriptomics, proteomics, metabolomics, microbiomics, longitudinal personal baselines, or systems biology.
129. Read `../domains/engineered-cell-therapy-regenerative-platforms/README.md` if you are working on CAR-T, TCR-T, TIL, NK, iPSC-derived cells, programmable cells, or engineered cell therapy safety.
130. Read `../domains/organoids-organ-on-chip-disease-models/README.md` if you are working on organoids, organ-on-chip, tissue chips, patient-derived models, alternative methods, or disease-model validation.
131. Read `../domains/xenotransplantation-bioengineered-organ-replacement/README.md` if you are working on xenotransplantation, genetically engineered animal organs, bioengineered organ replacement, organ perfusion, or transplant platform risks.
132. Read `../domains/causal-inference-target-trial-emulation/README.md` if you are working on causality, target trial emulation, intervention effects, confounding, selection bias, or counterfactual evaluation.
133. Read `../domains/survival-analysis-healthspan-risk-modeling/README.md` if you are working on survival curves, hazard functions, healthspan, competing risks, disability time, or effective-time endpoints.
134. Read `../domains/human-digital-twin-life-course-simulation/README.md` if you are working on human digital twins, life-course simulation, state vectors, scenario modeling, or dynamic subject models.
135. Read `../domains/implementation-science-adherence-behavior-change/README.md` if you are working on implementation science, adherence, adoption, behavior change, RE-AIM, COM-B, or real-world effectiveness.
136. Read `../domains/uncertainty-quantification-model-calibration/README.md` if you are working on model calibration, validation, uncertainty intervals, prediction reporting, drift, or overconfidence controls.
137. Read `../domains/data-quality-missingness-representativeness/README.md` if you are working on data quality, missingness, representativeness, measurement error, cohort bias, or data source suitability.
138. Read `../domains/privacy-preserving-computation-federated-learning/README.md` if you are working on differential privacy, federated learning, privacy-enhancing technologies, collaborative analytics, synthetic data, or privacy-utility tradeoffs.
139. Read `../domains/knowledge-graph-ontology-semantic-interoperability/README.md` if you are working on ontology, knowledge graph, RDF/OWL, FAIR data, semantic interoperability, controlled vocabulary, or domain relation modeling.
140. Read `../domains/model-cards-ai-audit-documentation/README.md` if you are working on model cards, datasheets, AI audit documentation, system cards, model limitations, or visualization governance.
141. Read `../domains/technology-foresight-horizon-scanning/README.md` if you are working on horizon scanning, technology foresight, weak signals, scenario planning, emerging technology watch, or future technology windows.
142. Read `../domains/research-portfolio-prioritization-funding-governance/README.md` if you are working on research prioritization, portfolio governance, funding allocation, value of information, stage gates, or stop conditions.
143. Read `../domains/intellectual-property-technology-transfer-access/README.md` if you are working on patents, licensing, technology transfer, public-funded inventions, Bayh-Dole, march-in rights, or technology access.
144. Read `../domains/trustworthy-scientific-communication-peer-review/README.md` if you are working on peer review, preprints, publication ethics, retractions, corrections, citation context, or scientific communication.
145. Read `../domains/research-participant-consent-community-engagement/README.md` if you are working on informed consent, participant withdrawal, recontact, research return of results, patient engagement, or community engagement.
146. Read `../domains/biobanking-biospecimen-quality-chain-of-custody/README.md` if you are working on biobanks, biospecimen quality, preanalytical variables, cold chain, sample tracking, or chain of custody.
147. Read `../domains/longitudinal-cohort-retention-followup-infrastructure/README.md` if you are working on longitudinal cohorts, follow-up, retention, attrition, event ascertainment, or life-course data linkage.
148. Read `../domains/registries-real-world-data-governance/README.md` if you are working on patient registries, disease registries, product registries, real-world data, real-world evidence, or registry data quality.
149. Read `../domains/scientific-instrumentation-sensor-calibration-maintenance/README.md` if you are working on scientific instrumentation, sensor calibration, drift, maintenance, reference materials, or measurement uncertainty.
150. Read `../domains/nanomedicine-targeted-delivery-molecular-repair/README.md` if you are working on nanomedicine, targeted delivery, nanoparticles, release control, molecular diagnostics, or future molecular repair claims.
151. Read `../domains/ai-drug-discovery-protein-design/README.md` if you are working on AI drug discovery, protein design, molecular generation, lead optimization, or predictive medicinal chemistry.
152. Read `../domains/epigenetic-editing-gene-regulation-therapeutics/README.md` if you are working on epigenetic editing, gene regulation therapeutics, chromatin state, gene silencing, or expression reprogramming.
153. Read `../domains/brain-preservation-connectomics-emulation/README.md` if you are working on brain preservation, connectomics, whole-brain emulation, neural identity records, or mind-uploading claims.
154. Read `../domains/post-quantum-cryptography-long-term-data-security/README.md` if you are working on post-quantum cryptography, long-term confidentiality, cryptographic migration, or future decryption risk.
155. Read `../domains/safety-critical-software-formal-methods/README.md` if you are working on safety-critical software, formal methods, assurance cases, verification, or high-risk system failures.
156. Read `../domains/long-term-digital-preservation-format-migration/README.md` if you are working on long-term digital preservation, file formats, metadata, fixity, backups, migration, or future readability.
157. Read `../domains/cerebrovascular-stroke-brain-perfusion-resilience/README.md` if you are working on stroke, brain perfusion, TIA, reperfusion windows, secondary prevention, or brain vascular resilience.
158. Read `../domains/traumatic-brain-injury-neurotrauma-recovery/README.md` if you are working on traumatic brain injury, concussion, repeated head impacts, neurotrauma recovery, or long-term cognitive/emotional/sleep sequelae.
159. Read `../domains/delirium-acute-cognitive-failure-prevention/README.md` if you are working on delirium, acute cognitive failure, ICU/hospital cognitive risk, or prevention of acute subject disconnection.
160. Read `../domains/disorders-of-consciousness-coma-recovery/README.md` if you are working on coma, vegetative/unresponsive wakefulness syndrome, minimally conscious state, recovery windows, or surrogate decision boundaries.
161. Read `../domains/epilepsy-seizure-network-stability/README.md` if you are working on seizures, epilepsy, brain network stability, treatment continuity, injury risk, or participation limits.
162. Read `../domains/autonomic-nervous-system-homeostasis/README.md` if you are working on autonomic regulation, orthostatic intolerance, heart-rate/blood-pressure control, sweating, digestion, bladder function, or stress recovery.
163. Read `../domains/migraine-headache-effective-time-burden/README.md` if you are working on migraine, headache disorders, sensory sensitivity, cognitive fog, disability days, or effective-time burden.
164. Read `../domains/vision-eye-health-continuity/README.md` if you are working on vision, eye health, visual impairment, low vision support, reading, mobility, or visual task participation.
165. Read `../domains/hearing-auditory-communication-continuity/README.md` if you are working on hearing loss, auditory communication, tinnitus, hearing support, sound alerts, or communication fatigue.
166. Read `../domains/vestibular-balance-spatial-orientation/README.md` if you are working on vestibular disorders, dizziness, balance, spatial orientation, falls, or mobility confidence.
167. Read `../domains/speech-language-communication-continuity/README.md` if you are working on aphasia, dysarthria, apraxia of speech, communication participation, consent expression, or augmentative communication.
168. Read `../domains/swallowing-dysphagia-aspiration-nutrition/README.md` if you are working on dysphagia, aspiration, swallowing safety, nutrition/hydration entry, feeding dignity, or aspiration pneumonia risk.
169. Read `../domains/smell-taste-chemosensory-continuity/README.md` if you are working on smell, taste, chemosensory loss, hazard detection, appetite, nutrition, or quality of life.
170. Read `../domains/peripheral-neuropathy-somatosensory-continuity/README.md` if you are working on peripheral neuropathy, touch, pain, proprioception, foot risk, somatosensory feedback, or fine motor feedback.
171. Read `../domains/space-weather-geomagnetic-storm-resilience/README.md` if you are working on space weather, geomagnetic storms, solar activity, electric grids, satellites, communications, navigation, or timing-system resilience.
172. Read `../domains/planetary-defense-near-earth-object-risk/README.md` if you are working on near-Earth objects, asteroid/comet impact risk, planetary defense, detection, tracking, warning, or deflection governance.
173. Read `../domains/volcanic-ashfall-geohazard-continuity/README.md` if you are working on volcano hazards, volcanic ash, air quality, aviation disruption, water, agriculture, buildings, or geohazard recovery.
174. Read `../domains/earthquake-seismic-risk-built-environment-continuity/README.md` if you are working on earthquakes, seismic risk, built environment safety, hospitals, roads, utilities, ShakeAlert, or post-earthquake recovery.
175. Read `../domains/tsunami-warning-coastal-evacuation-continuity/README.md` if you are working on tsunami warning, coastal evacuation, vertical refuge, alerting, coastal recovery, or short-window evacuation systems.
176. Read `../domains/extreme-heat-cooling-public-health-continuity/README.md` if you are working on extreme heat, heat health, cooling access, energy burden, housing quality, occupational heat exposure, or urban heat islands.
177. Read `../domains/noise-exposure-acoustic-environment-continuity/README.md` if you are working on noise exposure, acoustic environments, hearing preservation, sleep disruption, community noise, transportation noise, or occupational noise.
178. Read `../domains/light-exposure-circadian-environment-continuity/README.md` if you are working on light exposure, circadian environment, daylight, night-time light, shift work, lighting, sleep timing, or light pollution.
179. Read `../domains/lead-heavy-metal-exposure-control/README.md` if you are working on lead, mercury, cadmium, arsenic, heavy-metal exposure, old housing, drinking water, soil, dust, occupational exposure, or children's environmental health.
180. Read `../domains/radon-asbestos-indoor-hazard-continuity/README.md` if you are working on radon, asbestos, indoor long-latency hazards, old buildings, schools, workplaces, lung cancer risk, or building legacy exposures.
181. Read `../domains/mold-dampness-indoor-biological-exposure/README.md` if you are working on mold, dampness, indoor biological exposure, leaks, water damage, indoor allergens, housing quality, or post-flood indoor environments.
182. Read `../domains/vector-borne-disease-environmental-control/README.md` if you are working on vector-borne disease, mosquitoes, ticks, fleas, vector control, climate-water ecology, One Health, or environmental infection risk.
183. Read `../domains/advance-care-planning-medical-decision-continuity/README.md` if you are working on advance care planning, advance directives, health care proxy, medical decision continuity, goals of care, or incapacity communication.
184. Read `../domains/supported-decision-making-guardianship-rights/README.md` if you are working on supported decision-making, guardianship, conservatorship, decision capacity, disability rights, or least restrictive alternatives.
185. Read `../domains/healthcare-personal-representative-hipaa-access-continuity/README.md` if you are working on HIPAA personal representatives, caregiver access, proxy access, medical records, privacy boundaries, or authorized care coordination.
186. Read `../domains/financial-fiduciary-power-of-attorney-continuity/README.md` if you are working on financial power of attorney, fiduciary duty, bill payment, asset management, incapacity finance, or elder financial exploitation prevention.
187. Read `../domains/representative-payee-benefits-management-continuity/README.md` if you are working on representative payees, VA fiduciaries, benefits management, public income continuity, payee oversight, or protected benefit use.
188. Read `../domains/trust-estate-affairs-succession-continuity/README.md` if you are working on getting affairs in order, trustees, executors, estate affairs, beneficiary records, succession, or long-term project handoff.
189. Read `../domains/credit-consumer-reporting-access-continuity/README.md` if you are working on credit reports, consumer reports, specialty reporting agencies, report disputes, identity errors, or access impacts.
190. Read `../domains/tenant-screening-rental-access-continuity/README.md` if you are working on tenant screening, rental applications, eviction records, rental history, housing access, or rental-platform screening.
191. Read `../domains/background-check-record-screening-continuity/README.md` if you are working on background checks, criminal records, identity matching, license/education verification, adverse action, or record correction.
192. Read `../domains/employment-algorithmic-hiring-screening-continuity/README.md` if you are working on AI hiring, algorithmic resume screening, employment tests, video interview scoring, job matching, or employment decision systems.
193. Read `../domains/insurance-underwriting-algorithmic-risk-scoring-continuity/README.md` if you are working on insurance underwriting, algorithmic risk scoring, premium rating, claims automation, external data, or insurance AI governance.
194. Read `../domains/public-benefits-eligibility-automated-decision-continuity/README.md` if you are working on public benefits eligibility, automated eligibility screening, data matching, renewals, terminations, appeals, or human review.
195. Read `../domains/education-record-transcript-verification-continuity/README.md` if you are working on education records, transcripts, diplomas, enrollment verification, student records, FERPA, or degree verification.
196. Read `../domains/professional-licensure-certification-continuity/README.md` if you are working on occupational licensing, professional certification, registration, boards, scope of practice, license renewal, discipline, or portability.
197. Read `../domains/skills-competency-credentialing-continuity/README.md` if you are working on skills taxonomies, competency frameworks, micro-credentials, digital badges, portfolios, or skills-based hiring.
198. Read `../domains/continuing-education-recertification-continuity/README.md` if you are working on continuing education, CPD, CEU, CME, maintenance of certification, recertification, renewal, or continuing competence.
199. Read `../domains/apprenticeship-work-based-learning-continuity/README.md` if you are working on apprenticeships, work-based learning, on-the-job training, mentorship, journeyworker status, or competency progression.
200. Read `../domains/verifiable-credential-wallet-interoperability/README.md` if you are working on verifiable credentials, digital credential wallets, issuers, holders, verifiers, DIDs, trust registries, selective disclosure, or credential revocation.
201. Read `../domains/income-payroll-employment-record-continuity/README.md` if you are working on payroll records, wage records, employment verification, pay stubs, income proof, or payroll record correction.
202. Read `../domains/tax-administration-filing-record-continuity/README.md` if you are working on tax records, IRS transcripts, filing records, taxpayer identity, refund/credit records, tax notices, or tax account correction.
203. Read `../domains/social-security-earnings-benefit-record-continuity/README.md` if you are working on Social Security earnings records, work credits, benefit statements, retirement/disability/survivor records, or earnings corrections.
204. Read `../domains/retirement-pension-savings-plan-continuity/README.md` if you are working on pensions, 401(k), IRA, retirement plan records, vesting, rollovers, beneficiaries, lost accounts, or pension guarantees.
205. Read `../domains/unemployment-insurance-wage-record-continuity/README.md` if you are working on unemployment insurance wage records, UI claims, base periods, eligibility determinations, appeals, overpayments, or fraud controls.
206. Read `../domains/workers-compensation-occupational-injury-benefit-continuity/README.md` if you are working on workers compensation, occupational injury records, occupational disease, wage replacement, return-to-work, vocational rehabilitation, or OSHA injury logs.
207. Read `../domains/family-medical-leave-job-protection-continuity/README.md` if you are working on family or medical leave, job-protected leave, serious health conditions, caregiving leave, military caregiver leave, anti-retaliation, insurance continuity, or return-to-role after leave.
208. Read `../domains/paid-sick-family-leave-wage-replacement-continuity/README.md` if you are working on paid sick leave, paid family leave, paid medical leave, wage replacement, waiting periods, replacement rates, or leave-related payroll continuity.
209. Read `../domains/pregnancy-parental-work-continuity/README.md` if you are working on pregnancy accommodation, childbirth recovery, parental leave, bonding leave, lactation or pumping at work, parental work continuity, or pregnancy discrimination.
210. Read `../domains/workplace-accommodation-return-to-work-continuity/README.md` if you are working on reasonable accommodation, interactive process, stay-at-work, return-to-work, modified duty, phased return, work capacity, or assistive technology in employment.
211. Read `../domains/disability-income-work-capacity-benefit-continuity/README.md` if you are working on SSDI, SSI, disability income, work credits, work capacity, return-to-work incentives, benefit cliffs, or disability benefit continuity.
212. Read `../domains/family-caregiver-respite-work-continuity/README.md` if you are working on family caregiver support, respite care, caregiver training, caregiver employment continuity, eldercare, disability caregiving, or caregiver burden.
213. Read `../domains/vital-records-life-event-continuity/README.md` if you are working on vital records, birth/death/marriage/divorce records, certified copies, record corrections, civil registration, or life-event record continuity.
214. Read `../domains/name-change-identity-record-synchronization-continuity/README.md` if you are working on legal name changes, identity record synchronization, SSA/passport/state ID updates, tax/employment/school/medical record matching, or name mismatch risks.
215. Read `../domains/address-residency-mail-service-continuity/README.md` if you are working on address changes, residency, mailing address, USPS forwarding, service notices, jurisdiction, homelessness address alternatives, or address-based service routing.
216. Read `../domains/household-composition-dependent-eligibility-continuity/README.md` if you are working on household composition, dependents, coverage household, benefit household, tax/insurance/welfare household rules, or family eligibility units.
217. Read `../domains/family-law-custody-child-support-continuity/README.md` if you are working on custody, parenting time, child support, parentage, family court orders, child support services, or family-law record continuity.
218. Read `../domains/kinship-foster-adoption-care-continuity/README.md` if you are working on kinship care, foster care, adoption, guardianship-like placements, permanency planning, child welfare records, or child placement continuity.
219. Read `../domains/banking-deposit-account-access-continuity/README.md` if you are working on bank accounts, credit union accounts, deposit insurance, account access, account recovery, payment errors, or bank-account continuity.
220. Read `../domains/debt-obligation-collection-relief-continuity/README.md` if you are working on consumer debt, medical debt, collections, garnishment, bankruptcy, debt relief, debt records, or debt-related continuity risks.
221. Read `../domains/real-property-title-deed-record-continuity/README.md` if you are working on property title, deeds, land records, tax assessor records, title insurance, liens, mortgages, or real-property record continuity.
222. Read `../domains/driver-license-vehicle-registration-continuity/README.md` if you are working on driver's licenses, state IDs, REAL ID, vehicle title, registration, plates, DMV records, or personal mobility credential continuity.
223. Read `../domains/passport-travel-document-mobility-continuity/README.md` if you are working on passports, travel documents, consular services, emergency documents, travel advisories, or cross-border mobility continuity.
224. Read `../domains/long-distance-travel-booking-itinerary-continuity/README.md` if you are working on long-distance travel booking, itinerary records, confirmations, cancellations, changes, notifications, or travel-service handoffs.
225. Read `../domains/air-passenger-rights-disruption-refund-continuity/README.md` if you are working on flight delays, cancellations, refunds, denied boarding, tarmac delays, air-travel disability access, or aviation consumer protection.
226. Read `../domains/aviation-security-screening-identity-continuity/README.md` if you are working on TSA screening, REAL ID, passenger support, identity verification, accessible screening, or airport security-screening continuity.
227. Read `../domains/baggage-personal-property-travel-continuity/README.md` if you are working on checked baggage, carry-on property, delayed/lost/damaged baggage, critical medicines/documents, or travel personal-property continuity.
228. Read `../domains/lodging-temporary-accommodation-access-continuity/README.md` if you are working on hotels, temporary lodging, check-in requirements, accessibility rooms, disaster lodging, vacation-rental scams, or accommodation access.
229. Read `../domains/travel-advisory-consular-assistance-continuity/README.md` if you are working on travel advisories, STEP, embassies, consular assistance, emergency passports, overseas crisis communication, or citizen services abroad.
230. Read `../domains/travel-health-preparedness-continuity/README.md` if you are working on travelers' health, destination health risks, travel vaccines, chronic-condition travel preparation, medicines, travel clinics, or overseas medical access.
231. Read `../domains/customs-border-entry-declaration-continuity/README.md` if you are working on customs declarations, border entry, I-94 records, prohibited/restricted items, agriculture inspection, duties, or trusted traveler systems.
224. Read `../domains/contract-subscription-billing-consent-continuity/README.md` if you are working on contracts, subscriptions, automatic renewal, billing, cancellation, negative options, ongoing consent, or transaction-friction continuity.
225. Read `../domains/notary-document-authentication-signature-continuity/README.md` if you are working on notarization, electronic signatures, digital signatures, document authentication, apostilles, or institutional recognition of signed records.
226. Read `../domains/citizenship-nationality-statelessness-continuity/README.md` if you are working on citizenship, nationality, naturalization, consular protection, statelessness, nationality proof, or national-membership continuity.
227. Read `../domains/immigration-status-residency-work-authorization-continuity/README.md` if you are working on immigration status, residency, work authorization, status renewal, employment eligibility, or local-status continuity.
228. Read `../domains/asylum-refugee-protection-status-continuity/README.md` if you are working on asylum, refugee status, temporary protection, humanitarian protection, resettlement, or protection-status continuity.
229. Read `../domains/detention-custody-confinement-status-continuity/README.md` if you are working on arrest, detention, custody, confinement, immigration detention, release transition, or custody-status continuity.
230. Read `../domains/civil-commitment-involuntary-treatment-rights-continuity/README.md` if you are working on civil commitment, involuntary treatment, crisis evaluation, least-restrictive alternatives, review, or rights continuity.
231. Read `../domains/court-notice-service-process-default-judgment-continuity/README.md` if you are working on court notice, service of process, hearing notices, response deadlines, default judgments, or procedural-notice continuity.
232. Read `../domains/criminal-record-relief-collateral-consequences-continuity/README.md` if you are working on criminal records, record relief, expungement, sealing, collateral consequences, reentry eligibility, or record-recovery continuity.
233. Read `../domains/school-enrollment-attendance-continuity/README.md` if you are working on school enrollment, transfer, attendance, chronic absenteeism, school stability, homelessness protections, or student attendance continuity.
234. Read `../domains/special-education-iep-504-accommodation-continuity/README.md` if you are working on IDEA, IEP, Section 504, accommodations, related services, assistive supports, transition, or disability participation continuity in schools.
235. Read `../domains/school-meals-nutrition-access-continuity/README.md` if you are working on school meals, school breakfast/lunch, free/reduced-price access, CEP, summer meals, dietary accommodations, or student nutrition continuity.
236. Read `../domains/school-health-services-chronic-condition-continuity/README.md` if you are working on school health services, school nursing, chronic condition support, medication, immunization records, emergency action plans, or return-to-school continuity.
237. Read `../domains/school-transportation-safe-routes-continuity/README.md` if you are working on school buses, safe routes to school, walking/biking safety, disability transportation, distance barriers, or attendance-related transportation continuity.
238. Read `../domains/school-discipline-exclusion-restraint-continuity/README.md` if you are working on suspensions, expulsions, classroom removals, restraint/seclusion, re-entry, discipline data, or exclusion-risk continuity.
239. Read `../domains/school-mental-health-counseling-support-continuity/README.md` if you are working on school counseling, school-based mental health, social workers, crisis referral, community care linkage, or student recovery continuity.
240. Read `../domains/school-climate-bullying-violence-prevention-continuity/README.md` if you are working on school climate, belonging, bullying, harassment, violence prevention, reporting channels, or school safety continuity.
241. Read `../domains/postsecondary-admissions-transfer-articulation-continuity/README.md` if you are working on higher education admissions, enrollment, transfer, articulation, credit conversion, readmission, or postsecondary pathway continuity.
242. Read `../domains/student-financial-aid-grant-scholarship-continuity/README.md` if you are working on FAFSA, Title IV aid, grants, scholarships, work-study, aid disbursement, SAP, or student financial-aid continuity.
243. Read `../domains/academic-advising-degree-progress-continuity/README.md` if you are working on academic advising, degree audit, course sequencing, credit accumulation, early alerts, retention, or degree-progress continuity.
244. Read `../domains/campus-basic-needs-student-support-continuity/README.md` if you are working on campus food, housing, transportation, childcare, emergency aid, benefits navigation, or basic-needs student support continuity.
245. Read `../domains/campus-disability-accommodations-accessibility-continuity/README.md` if you are working on campus disability services, Section 504, ADA, accommodations, accessible materials, auxiliary aids, or higher-ed accessibility continuity.
246. Read `../domains/campus-mental-health-crisis-student-support-continuity/README.md` if you are working on campus counseling, student mental health, crisis response, leave/re-entry, peer support, or student recovery continuity.
247. Read `../domains/campus-safety-title-ix-clery-continuity/README.md` if you are working on campus safety, Title IX, sexual misconduct response, Clery Act, campus crime reporting, emergency notification, or supportive-measure continuity.
248. Read `../domains/international-student-sevis-status-continuity/README.md` if you are working on SEVIS, F/M student status, I-20, DSO reporting, CPT/OPT, travel signature, or international-student status continuity.
249. Read `../domains/email-account-recovery-continuity/README.md` if you are working on email account access, recovery email, password reset, service notifications, account takeover, or email-based recovery continuity.
250. Read `../domains/phone-number-sim-portability-account-security-continuity/README.md` if you are working on phone number control, SIM/eSIM, port-out, SIM swap, SMS verification, carrier accounts, or phone-based recovery continuity.
251. Read `../domains/mfa-passkey-credential-recovery-continuity/README.md` if you are working on MFA, passkeys, security keys, authenticator apps, recovery codes, trusted devices, or credential recovery continuity.
252. Read `../domains/password-manager-secret-vault-continuity/README.md` if you are working on password managers, secret vaults, recovery keys, emergency access, shared vaults, or credential portfolio continuity.
253. Read `../domains/cloud-backup-file-sync-data-portability-continuity/README.md` if you are working on cloud storage, file sync, backup, version history, data export, format migration, or data portability continuity.
254. Read `../domains/messaging-contact-graph-portability-continuity/README.md` if you are working on messaging accounts, contacts, groups, chat history, backup/export, interoperability, or social graph continuity.
255. Read `../domains/domain-dns-web-presence-continuity/README.md` if you are working on domain names, DNS, registrar accounts, TLS certificates, hosting, custom email domains, or web presence continuity.
256. Read `../domains/platform-account-suspension-appeals-continuity/README.md` if you are working on platform account suspension, content removal, moderation appeals, transparency, creator/merchant accounts, or platform exit continuity.
257. Read `../domains/personal-computing-device-lifecycle-repair-continuity/README.md` if you are working on personal computing devices, repairability, device replacement, support windows, data migration, device lock-in, or repair continuity.
258. Read `../domains/home-network-router-iot-security-continuity/README.md` if you are working on home routers, Wi-Fi, broadband gateways, IoT security, firmware updates, default credentials, or home-network continuity.
259. Read `../domains/software-supply-chain-dependency-provenance-continuity/README.md` if you are working on software dependencies, SBOM, package managers, build provenance, artifact signing, or software supply-chain continuity.
260. Read `../domains/software-update-vulnerability-patch-continuity/README.md` if you are working on vulnerability disclosure, patch deployment, rollback, known exploited vulnerabilities, support windows, or software-update continuity.
261. Read `../domains/open-source-maintainer-sustainability-continuity/README.md` if you are working on maintainer capacity, open-source funding, bus factor, project health, security response, or open-source sustainability continuity.
262. Read `../domains/pki-certificate-cryptographic-trust-continuity/README.md` if you are working on PKI, TLS certificates, certificate authorities, key management, revocation, root trust, certificate transparency, or cryptographic trust continuity.
263. Read `../domains/cloud-service-exit-interoperability-continuity/README.md` if you are working on SaaS/cloud export, data migration, interoperability, vendor lock-in, service exit, or cloud-switching continuity.
264. Read `../domains/api-platform-dependency-runtime-continuity/README.md` if you are working on third-party APIs, SDKs, rate limits, deprecation, SLA, runtime fallback, platform dependency, or API continuity.
265. Read `../domains/calendar-scheduling-appointment-continuity/README.md` if you are working on calendars, scheduling, appointments, time zones, reminders, rescheduling, invitations, or calendar continuity.
266. Read `../domains/notification-alert-routing-attention-continuity/README.md` if you are working on notifications, push alerts, delivery channels, quiet hours, escalation, acknowledgement, notification fatigue, or alert routing continuity.
267. Read `../domains/reminder-alarm-routine-task-continuity/README.md` if you are working on reminders, alarms, recurring tasks, routines, missed-task recovery, habit systems, or routine task continuity.
268. Read `../domains/meeting-video-conferencing-remote-collaboration-continuity/README.md` if you are working on video meetings, remote collaboration, WebRTC, captions, recordings, meeting notes, or action-item continuity.
269. Read `../domains/document-capture-ocr-pdf-record-workflow-continuity/README.md` if you are working on document capture, OCR, scanning, PDF/PDF-A, forms, metadata, submissions, or record workflow continuity.
270. Read `../domains/search-index-discovery-retrieval-continuity/README.md` if you are working on search, indexing, metadata, sitemap, schema, discovery, retrieval, broken links, or findability continuity.
271. Read `../domains/personal-automation-integration-workflow-continuity/README.md` if you are working on personal automation, low-code workflows, webhooks, OAuth, scripts, triggers, idempotency, or workflow continuity.
272. Read `../domains/collaborative-document-permission-version-continuity/README.md` if you are working on shared documents, permissions, version history, comments, ownership transfer, export, or collaborative document continuity.
273. Read `../domains/public-restroom-sanitation-hygiene-access-continuity/README.md` if you are working on public restrooms, sanitation, handwashing, menstrual hygiene, family restrooms, accessible toilets, or public hygiene access continuity.
274. Read `../domains/public-drinking-water-hydration-access-continuity/README.md` if you are working on public drinking water, hydration stations, fountains, water quality notices, emergency water distribution, or heat-related hydration access.
275. Read `../domains/public-seating-shade-rest-cooling-access-continuity/README.md` if you are working on public seating, shade, transit shelters, cooling centers, rest opportunities, urban heat exposure, or public-space recovery.
276. Read `../domains/community-resilience-hub-shelter-center-continuity/README.md` if you are working on resilience hubs, shelters, cooling/warming/clean-air centers, public charging, disaster service centers, or community lifelines.
277. Read `../domains/public-library-community-anchor-access-continuity/README.md` if you are working on public libraries, community anchors, public computers, Wi-Fi, printing/scanning, digital skills, or service navigation.
278. Read `../domains/parks-recreation-green-space-access-continuity/README.md` if you are working on parks, recreation, green space, trails, playgrounds, public exercise, nature access, or restorative public space.
279. Read `../domains/public-wifi-device-charging-connectivity-continuity/README.md` if you are working on public Wi-Fi, public computers, device charging, outage connectivity, emergency communications, or digital task continuity outside home.
280. Read `../domains/public-accommodation-accessibility-service-continuity/README.md` if you are working on public accommodations, ADA Title II/III, effective communication, service animals, reasonable accommodations, or accessible service continuity.
281. Read `../domains/grocery-retail-food-store-access-continuity/README.md` if you are working on grocery stores, food retail, supermarkets, farmers markets, online pickup/delivery, food prices, or retail food access continuity.
282. Read `../domains/snap-ebt-redemption-retailer-payment-continuity/README.md` if you are working on SNAP EBT, authorized retailers, EBT cards, online SNAP purchasing, benefit redemption, transaction failures, or food-benefit payment continuity.
283. Read `../domains/wic-benefit-redemption-infant-maternal-nutrition-continuity/README.md` if you are working on WIC, eWIC, food packages, infant formula through WIC, maternal/infant nutrition, or WIC redemption continuity.
284. Read `../domains/food-bank-pantry-community-food-distribution-continuity/README.md` if you are working on food banks, pantries, TEFAP, community food distribution, donated food logistics, or emergency household food buffers.
285. Read `../domains/emergency-food-disaster-feeding-continuity/README.md` if you are working on disaster feeding, emergency food distribution, D-SNAP, shelter meals, emergency food packages, or disaster nutrition assistance.
286. Read `../domains/home-delivered-meals-congregate-nutrition-services-continuity/README.md` if you are working on home-delivered meals, congregate meals, Older Americans Act nutrition services, Meals on Wheels, senior meals, or disability-related meal delivery.
287. Read `../domains/infant-formula-baby-food-supply-safety-continuity/README.md` if you are working on infant formula, baby food, specialty formula, formula recalls, shortages, WIC substitutions, or early-life food supply safety.
288. Read `../domains/prepared-food-restaurant-cafeteria-safety-access-continuity/README.md` if you are working on prepared food, restaurants, cafeterias, workplace/school/hospital meals, takeout, food allergens, menu information, or restaurant food safety access.
289. Read `../domains/retail-pharmacy-prescription-dispensing-continuity/README.md` if you are working on retail pharmacies, mail-order pharmacies, specialty pharmacies, prescription dispensing, refill continuity, pharmacy deserts, pharmacy delivery, or prescription transfer.
290. Read `../domains/pharmacy-benefit-formulary-prior-authorization-continuity/README.md` if you are working on pharmacy benefits, formularies, prior authorization, step therapy, coverage determination, exceptions, Part D, PBMs, or prescription benefit friction.
291. Read `../domains/medication-reconciliation-regimen-adherence-continuity/README.md` if you are working on medication reconciliation, medication lists, care transitions, adherence, regimen burden, pill organization, or household medication execution.
292. Read `../domains/patient-medication-labeling-counseling-continuity/README.md` if you are working on medication labels, Medication Guides, Patient Medication Information, pharmacist counseling, prescription instructions, plain-language drug information, or medication communication.
293. Read `../domains/unused-medicine-takeback-disposal-continuity/README.md` if you are working on unused medicines, expired medicines, medicine take-back, disposal sites, mail-back envelopes, drug drop boxes, or household medication storage risk.
294. Read `../domains/durable-medical-equipment-supplier-repair-continuity/README.md` if you are working on DME, DMEPOS suppliers, wheelchair/walker/hospital-bed access, equipment repair, replacement, consumables, coverage, or home medical equipment continuity.
295. Read `../domains/home-oxygen-respiratory-equipment-supply-continuity/README.md` if you are working on home oxygen, oxygen concentrators, portable oxygen, CPAP/BiPAP, respiratory equipment, oxygen accessories, electricity dependency, or respiratory supply continuity.
296. Read `../domains/diabetes-insulin-glucose-monitoring-supplies-continuity/README.md` if you are working on insulin, diabetes supplies, CGM, glucose meters, test strips, pump supplies, diabetes device access, refrigeration, or diabetes treatment supply continuity.
297. Read `../domains/provider-directory-network-adequacy-continuity/README.md` if you are working on provider directories, network adequacy, provider networks, in-network access, accepting-new-patient status, Care Compare, provider directory accuracy, or ghost networks.
298. Read `../domains/primary-care-panel-appointment-access-continuity/README.md` if you are working on primary care, PCP panel, new patient intake, same-day access, annual wellness, chronic follow-up, FQHC, or routine care continuity.
299. Read `../domains/specialist-referral-authorization-navigation-continuity/README.md` if you are working on specialist referrals, referral orders, prior authorization, e-consults, network routing, referral management, referral leakage, or specialist feedback loops.
300. Read `../domains/appointment-availability-wait-time-continuity/README.md` if you are working on appointment availability, wait times, scheduling capacity, cancellation lists, no-show, rescheduling, same-day access, or healthcare wait-time measurement.
301. Read `../domains/outpatient-laboratory-specimen-result-routing-continuity/README.md` if you are working on outpatient lab orders, specimen collection, draw stations, result routing, patient portals, abnormal result follow-up, or diagnostic signal continuity.
302. Read `../domains/diagnostic-imaging-order-scheduling-report-continuity/README.md` if you are working on diagnostic imaging orders, radiology scheduling, CT/MRI/ultrasound/X-ray access, imaging reports, DICOM/PACS, critical result routing, or image sharing.
303. Read `../domains/ambulatory-procedure-surgery-center-continuity/README.md` if you are working on ambulatory surgery centers, outpatient procedures, endoscopy, infusion centers, pre-op workflows, escorts, recovery observation, or post-procedure follow-up.
304. Read `../domains/after-hours-urgent-care-triage-continuity/README.md` if you are working on after-hours care, urgent care, nurse advice lines, retail clinics, tele-triage, same-day advice, ED diversion, or non-emergency time-window failures.
305. Read `../domains/health-insurance-enrollment-renewal-continuity/README.md` if you are working on health insurance enrollment, renewal, open enrollment, special enrollment periods, Medicaid/Marketplace transitions, premium payment, or coverage gaps.
306. Read `../domains/insurance-eligibility-benefits-verification-continuity/README.md` if you are working on eligibility checks, benefits verification, active coverage, deductible/copay/coinsurance, out-of-pocket maximum, network status, or coverage limits.
307. Read `../domains/medical-service-prior-authorization-utilization-management-continuity/README.md` if you are working on medical-service prior authorization, utilization management, medical necessity review, coverage criteria, peer review, or authorization delays.
308. Read `../domains/claims-adjudication-eob-denial-continuity/README.md` if you are working on claims adjudication, EOBs, claim denials, coordination of benefits, resubmission, appeal windows, or payer payment loops.
309. Read `../domains/patient-billing-payment-plan-continuity/README.md` if you are working on patient billing, statements, patient responsibility, payment plans, billing inquiries, collections handoff, or billing readability.
310. Read `../domains/price-transparency-good-faith-estimate-continuity/README.md` if you are working on hospital price transparency, payer transparency, good faith estimates, shoppable services, machine-readable files, or bill-estimate mismatch.
311. Read `../domains/surprise-billing-balance-bill-protection-continuity/README.md` if you are working on No Surprises Act, balance billing, out-of-network emergency care, air ambulance, notice/consent, or surprise-bill complaints.
312. Read `../domains/charity-care-financial-assistance-medical-debt-continuity/README.md` if you are working on hospital financial assistance, charity care, limitation on charges, billing and collections, payment plans, medical debt, or extraordinary collection actions.
313. Read `../domains/patient-portal-account-message-continuity/README.md` if you are working on patient portals, secure messaging, notification routing, proxy access, patient-facing APIs, or healthcare account/message continuity.
314. Read `../domains/medical-record-access-amendment-release-continuity/README.md` if you are working on HIPAA record access, amendment, release of information, information blocking, USCDI/FHIR patient access, or record portability.
315. Read `../domains/clinical-results-notification-followup-continuity/README.md` if you are working on clinical results notification, abnormal results, critical values, incidental findings, diagnostic safety, or follow-up tracking.
316. Read `../domains/informed-consent-refusal-shared-decision-continuity/README.md` if you are working on informed consent, informed refusal, shared decision-making, decision aids, risk communication, or medical choice documentation.
317. Read `../domains/healthcare-language-interpreter-effective-communication-continuity/README.md` if you are working on healthcare interpreter services, LEP, translated materials, CLAS, auxiliary communication, or effective communication.
318. Read `../domains/healthcare-disability-accommodation-accessibility-continuity/README.md` if you are working on healthcare disability accommodation, auxiliary aids, accessible medical diagnostic equipment, ADA/Section 504 healthcare access, or reasonable modification.
319. Read `../domains/patient-grievance-complaint-ombuds-continuity/README.md` if you are working on patient grievance, hospital complaint, state survey agency, ombudsman, quality complaint, or healthcare complaint routing.
320. Read `../domains/healthcare-civil-rights-nondiscrimination-continuity/README.md` if you are working on Section 1557, healthcare nondiscrimination, HHS OCR civil rights, healthcare bias, or protected-characteristic access barriers.
321. Read `../domains/emergency-contact-next-of-kin-notification-continuity/README.md` if you are working on emergency contacts, next of kin, authorized contacts, caregiver notification, or urgent support-network handoff.
322. Read `../domains/personal-health-record-emergency-summary-continuity/README.md` if you are working on personal health records, emergency summaries, wallet cards, patient-maintained records, Blue Button exports, or minimum emergency health data.
323. Read `../domains/medical-id-allergy-critical-alert-continuity/README.md` if you are working on medical ID, allergy alerts, critical condition alerts, emergency phone/wearable health profiles, or visible urgent health warnings.
324. Read `../domains/medication-list-implant-device-emergency-continuity/README.md` if you are working on medication lists, high-risk medications, implant/device cards, UDI, device constraints, or emergency medication/device transfer.
325. Read `../domains/chronic-condition-emergency-action-plan-continuity/README.md` if you are working on chronic-condition emergency action plans, symptom zones, escalation paths, school/work action plans, or disaster interruption of chronic care.
326. Read `../domains/immunization-record-proof-continuity/README.md` if you are working on vaccination records, immunization registries, vaccine proof, school/work/travel immunization documentation, or record portability.
327. Read `../domains/organ-donor-registry-anatomical-gift-continuity/README.md` if you are working on organ donor registry, anatomical gift, donor designation, state registry, transplant-system identity handoff, or post-death donation intent.
328. Read `../domains/access-functional-needs-emergency-registry-continuity/README.md` if you are working on access and functional needs, special needs registries, medical needs registries, evacuation support, power-dependent devices, or disaster accessibility planning.
329. Read `../domains/death-certificate-registration-cause-of-death-record-continuity/README.md` if you are working on death certificates, death registration, cause-of-death records, certified copies, medical certification, or vital statistics.
330. Read `../domains/funeral-cremation-burial-disposition-continuity/README.md` if you are working on funeral services, cremation, burial, body disposition, price disclosure, funeral permits, or remains transport.
331. Read `../domains/cemetery-memorial-remains-location-continuity/README.md` if you are working on cemetery plots, grave markers, columbarium, ashes/remains location, memorial records, or cemetery maintenance.
332. Read `../domains/bereavement-leave-grief-support-continuity/README.md` if you are working on bereavement leave, grief support, EAP, peer support, school/work adjustment, or survivor recovery after death.
333. Read `../domains/survivor-benefits-death-notification-continuity/README.md` if you are working on death reporting, survivor benefits, Social Security survivor benefits, VA survivor benefits, employer benefits, or pension notifications.
334. Read `../domains/life-insurance-beneficiary-claim-continuity/README.md` if you are working on life insurance policies, beneficiary designations, death claims, policy locator systems, group life insurance, or unclaimed benefits.
335. Read `../domains/estate-inventory-asset-liability-handoff-continuity/README.md` if you are working on estate inventory, asset lists, liability lists, executor/personal representative task queues, probate handoff, or creditor notices.
336. Read `../domains/post-death-account-closure-service-cancellation-continuity/README.md` if you are working on post-death account closure, service cancellation, automatic payment stops, deceased-account handling, data export, or identity theft prevention.
337. Read `../domains/loneliness-social-isolation-risk-continuity/README.md` if you are working on loneliness, social isolation, connection quality, relationship risk, help-seeking capacity, or social disconnection as a health and continuity variable.
338. Read `../domains/social-prescribing-community-referral-continuity/README.md` if you are working on social prescribing, link workers, community referrals, closed-loop social support, activity referral, or non-clinical support pathways.
339. Read `../domains/mutual-aid-neighbor-support-network-continuity/README.md` if you are working on mutual aid, neighbor support, informal care, disaster neighbor checks, low-friction help, or community support networks.
340. Read `../domains/volunteering-civic-service-participation-continuity/README.md` if you are working on volunteering, civic service, service participation, social capital, skill-building, or community contribution pathways.
341. Read `../domains/community-mediation-neighbor-conflict-resolution-continuity/README.md` if you are working on community mediation, neighbor conflict, low-level disputes, dialogue, agreement follow-up, or conflict de-escalation infrastructure.
342. Read `../domains/restorative-justice-repair-accountability-continuity/README.md` if you are working on restorative justice, repair, accountability, victim needs, reintegration, or post-harm community continuity.
343. Read `../domains/reputation-defamation-public-trust-repair-continuity/README.md` if you are working on reputation harm, defamation, public trust, correction, complaint pathways, or trust repair.
344. Read `../domains/references-vouching-recommendation-social-capital-continuity/README.md` if you are working on references, vouching, recommendation letters, introductions, social proof, opportunity access, or social-capital conversion.
345. Read `../domains/third-place-belonging-social-participation-continuity/README.md` if you are working on third places, belonging, public libraries, parks, community anchors, social participation, or weak-tie spaces.
346. Read `../domains/purpose-meaning-existential-continuity/README.md` if you are working on purpose, meaning in life, existential well-being, hope, despair, long-term goals, or value orientation as a continuity variable.
347. Read `../domains/spiritual-care-religious-practice-continuity/README.md` if you are working on spiritual care, chaplaincy, religious practice, faith communities, spiritual distress, or conscience/religion continuity.
348. Read `../domains/cultural-heritage-identity-continuity/README.md` if you are working on cultural heritage, language, community memory, minority identity, migration culture, or intergenerational cultural transmission.
349. Read `../domains/arts-creative-expression-participation-continuity/README.md` if you are working on arts participation, creative expression, community arts, creative aging, cultural production, or expressive continuity.
350. Read `../domains/leisure-recreation-restorative-activity-continuity/README.md` if you are working on leisure, recreation, play, hobbies, parks use, restorative activity, non-work time, or recreation access.
351. Read `../domains/narrative-identity-life-review-continuity/README.md` if you are working on narrative identity, life review, reminiscence, autobiography, memory work, life story, or identity reconstruction.
352. Read `../domains/ritual-ceremony-life-transition-continuity/README.md` if you are working on rituals, ceremonies, rites of passage, memorials, life transitions, public recognition, or community recognition.
353. Read `../domains/dignity-personhood-respect-continuity/README.md` if you are working on dignity, personhood, respect, autonomy, non-humiliation, person-centered care, or dehumanization risk.
354. Read `../domains/human-factors-ergonomics-task-system-continuity/README.md` if you are working on human factors, ergonomics, human systems integration, usability engineering, task-system fit, or human-centered design.
355. Read `../domains/cognitive-load-workload-measurement-continuity/README.md` if you are working on cognitive load, NASA-TLX, mental workload, working memory, task complexity, or workload measurement.
356. Read `../domains/fatigue-risk-alertness-continuity/README.md` if you are working on fatigue risk, shift work, long hours, alertness, sleep debt, recovery windows, or fatigue safety.
357. Read `../domains/situational-awareness-decision-environment-continuity/README.md` if you are working on situation awareness, sensemaking, shared mental models, decision support, risk picture, or state dashboards.
358. Read `../domains/handoff-checklist-procedure-reliability-continuity/README.md` if you are working on handoffs, checklists, SOPs, standard work, read-back, briefing, debriefing, or process reliability.
359. Read `../domains/incident-reporting-just-culture-learning-continuity/README.md` if you are working on incident reporting, near misses, just culture, safety culture, RCA/RCA2, corrective actions, or learning systems.
360. Read `../domains/automation-bias-mode-confusion-oversight-continuity/README.md` if you are working on automation bias, mode confusion, overreliance, human override, supervisory control, or meaningful human oversight.
361. Read `../domains/alert-fatigue-interruption-signal-management-continuity/README.md` if you are working on alert fatigue, alarm fatigue, notification fatigue, interruptions, signal prioritization, quiet hours, or escalation routing.
362. Read `../domains/depression-mood-disorder-functioning-continuity/README.md` if you are working on depression, mood disorder, anhedonia, motivation loss, functional impairment, or depression-related service continuity.
363. Read `../domains/anxiety-stress-threat-regulation-continuity/README.md` if you are working on anxiety, chronic stress, threat regulation, avoidance, panic, social anxiety, or stress-related functioning.
364. Read `../domains/trauma-ptsd-adversity-recovery-continuity/README.md` if you are working on trauma, PTSD, adverse childhood experiences, disaster trauma, violence exposure, trauma-informed support, or recovery continuity.
365. Read `../domains/psychosis-reality-testing-community-continuity/README.md` if you are working on psychosis, schizophrenia spectrum, hallucinations, delusions, reality testing, community mental health, or rights-protecting support.
366. Read `../domains/bipolar-mood-episode-stability-continuity/README.md` if you are working on bipolar disorder, mania, hypomania, mood episodes, sleep rhythm instability, impulsive risk, or cyclical functioning.
367. Read `../domains/adhd-executive-function-neurodevelopment-continuity/README.md` if you are working on ADHD, executive function, task initiation, time sense, impulse control, school/work supports, or neurodevelopmental task continuity.
368. Read `../domains/autism-neurodiversity-support-continuity/README.md` if you are working on autism, neurodiversity, sensory differences, communication access, routines, support needs, or inclusive participation.
369. Read `../domains/eating-disorders-nutrition-body-continuity/README.md` if you are working on eating disorders, body image, restrictive eating, binge/purge behavior, nutrition risk, or eating-disorder service continuity.
370. Enter a domain under `../domains/`.
