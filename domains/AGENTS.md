# domains 目录说明

`domains/` 保存 Human Infra 的独立子域。每个子域都是一个有边界的研究或产品方向，必须说明对象、非目标、证据要求和上游/下游关系。

## 目录结构

```text
domains/
├── AGENTS.md
├── README.md
├── antimicrobial-resilience/
│   ├── AGENTS.md
│   └── README.md
├── assistive-technology-access/
│   ├── AGENTS.md
│   └── README.md
├── biostasis-cryopreservation/
│   ├── AGENTS.md
│   └── README.md
├── ai-agency-safety/
│   ├── AGENTS.md
│   └── README.md
├── attention-executive-control/
│   ├── AGENTS.md
│   └── README.md
├── cancer-control/
│   ├── AGENTS.md
│   └── README.md
├── cellular-reprogramming/
│   ├── AGENTS.md
│   └── README.md
├── gene-therapy-genome-editing-delivery-safety/
│   ├── AGENTS.md
│   └── README.md
├── biological-age-clocks-biomarker-validation/
│   ├── AGENTS.md
│   └── README.md
├── multiomics-personal-baseline-systems-biology/
│   ├── AGENTS.md
│   └── README.md
├── engineered-cell-therapy-regenerative-platforms/
│   ├── AGENTS.md
│   └── README.md
├── organoids-organ-on-chip-disease-models/
│   ├── AGENTS.md
│   └── README.md
├── xenotransplantation-bioengineered-organ-replacement/
│   ├── AGENTS.md
│   └── README.md
├── causal-inference-target-trial-emulation/
│   ├── AGENTS.md
│   └── README.md
├── survival-analysis-healthspan-risk-modeling/
│   ├── AGENTS.md
│   └── README.md
├── human-digital-twin-life-course-simulation/
│   ├── AGENTS.md
│   └── README.md
├── implementation-science-adherence-behavior-change/
│   ├── AGENTS.md
│   └── README.md
├── uncertainty-quantification-model-calibration/
│   ├── AGENTS.md
│   └── README.md
├── data-quality-missingness-representativeness/
│   ├── AGENTS.md
│   └── README.md
├── privacy-preserving-computation-federated-learning/
│   ├── AGENTS.md
│   └── README.md
├── knowledge-graph-ontology-semantic-interoperability/
│   ├── AGENTS.md
│   └── README.md
├── model-cards-ai-audit-documentation/
│   ├── AGENTS.md
│   └── README.md
├── technology-foresight-horizon-scanning/
│   ├── AGENTS.md
│   └── README.md
├── research-portfolio-prioritization-funding-governance/
│   ├── AGENTS.md
│   └── README.md
├── intellectual-property-technology-transfer-access/
│   ├── AGENTS.md
│   └── README.md
├── trustworthy-scientific-communication-peer-review/
│   ├── AGENTS.md
│   └── README.md
├── research-participant-consent-community-engagement/
│   ├── AGENTS.md
│   └── README.md
├── biobanking-biospecimen-quality-chain-of-custody/
│   ├── AGENTS.md
│   └── README.md
├── longitudinal-cohort-retention-followup-infrastructure/
│   ├── AGENTS.md
│   └── README.md
├── registries-real-world-data-governance/
│   ├── AGENTS.md
│   └── README.md
├── scientific-instrumentation-sensor-calibration-maintenance/
│   ├── AGENTS.md
│   └── README.md
├── nanomedicine-targeted-delivery-molecular-repair/
│   ├── AGENTS.md
│   └── README.md
├── ai-drug-discovery-protein-design/
│   ├── AGENTS.md
│   └── README.md
├── epigenetic-editing-gene-regulation-therapeutics/
│   ├── AGENTS.md
│   └── README.md
├── brain-preservation-connectomics-emulation/
│   ├── AGENTS.md
│   └── README.md
├── post-quantum-cryptography-long-term-data-security/
│   ├── AGENTS.md
│   └── README.md
├── safety-critical-software-formal-methods/
│   ├── AGENTS.md
│   └── README.md
├── long-term-digital-preservation-format-migration/
│   ├── AGENTS.md
│   └── README.md
├── cerebrovascular-stroke-brain-perfusion-resilience/
│   ├── AGENTS.md
│   └── README.md
├── traumatic-brain-injury-neurotrauma-recovery/
│   ├── AGENTS.md
│   └── README.md
├── delirium-acute-cognitive-failure-prevention/
│   ├── AGENTS.md
│   └── README.md
├── disorders-of-consciousness-coma-recovery/
│   ├── AGENTS.md
│   └── README.md
├── epilepsy-seizure-network-stability/
│   ├── AGENTS.md
│   └── README.md
├── autonomic-nervous-system-homeostasis/
│   ├── AGENTS.md
│   └── README.md
├── migraine-headache-effective-time-burden/
│   ├── AGENTS.md
│   └── README.md
├── vision-eye-health-continuity/
│   ├── AGENTS.md
│   └── README.md
├── hearing-auditory-communication-continuity/
│   ├── AGENTS.md
│   └── README.md
├── vestibular-balance-spatial-orientation/
│   ├── AGENTS.md
│   └── README.md
├── speech-language-communication-continuity/
│   ├── AGENTS.md
│   └── README.md
├── swallowing-dysphagia-aspiration-nutrition/
│   ├── AGENTS.md
│   └── README.md
├── smell-taste-chemosensory-continuity/
│   ├── AGENTS.md
│   └── README.md
├── peripheral-neuropathy-somatosensory-continuity/
│   ├── AGENTS.md
│   └── README.md
├── space-weather-geomagnetic-storm-resilience/
│   ├── AGENTS.md
│   └── README.md
├── planetary-defense-near-earth-object-risk/
│   ├── AGENTS.md
│   └── README.md
├── volcanic-ashfall-geohazard-continuity/
│   ├── AGENTS.md
│   └── README.md
├── earthquake-seismic-risk-built-environment-continuity/
│   ├── AGENTS.md
│   └── README.md
├── tsunami-warning-coastal-evacuation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── extreme-heat-cooling-public-health-continuity/
│   ├── AGENTS.md
│   └── README.md
├── noise-exposure-acoustic-environment-continuity/
│   ├── AGENTS.md
│   └── README.md
├── light-exposure-circadian-environment-continuity/
│   ├── AGENTS.md
│   └── README.md
├── lead-heavy-metal-exposure-control/
│   ├── AGENTS.md
│   └── README.md
├── radon-asbestos-indoor-hazard-continuity/
│   ├── AGENTS.md
│   └── README.md
├── mold-dampness-indoor-biological-exposure/
│   ├── AGENTS.md
│   └── README.md
├── vector-borne-disease-environmental-control/
│   ├── AGENTS.md
│   └── README.md
├── advance-care-planning-medical-decision-continuity/
│   ├── AGENTS.md
│   └── README.md
├── supported-decision-making-guardianship-rights/
│   ├── AGENTS.md
│   └── README.md
├── healthcare-personal-representative-hipaa-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── financial-fiduciary-power-of-attorney-continuity/
│   ├── AGENTS.md
│   └── README.md
├── representative-payee-benefits-management-continuity/
│   ├── AGENTS.md
│   └── README.md
├── trust-estate-affairs-succession-continuity/
│   ├── AGENTS.md
│   └── README.md
├── credit-consumer-reporting-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── tenant-screening-rental-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── background-check-record-screening-continuity/
│   ├── AGENTS.md
│   └── README.md
├── employment-algorithmic-hiring-screening-continuity/
│   ├── AGENTS.md
│   └── README.md
├── insurance-underwriting-algorithmic-risk-scoring-continuity/
│   ├── AGENTS.md
│   └── README.md
├── public-benefits-eligibility-automated-decision-continuity/
│   ├── AGENTS.md
│   └── README.md
├── education-record-transcript-verification-continuity/
│   ├── AGENTS.md
│   └── README.md
├── professional-licensure-certification-continuity/
│   ├── AGENTS.md
│   └── README.md
├── skills-competency-credentialing-continuity/
│   ├── AGENTS.md
│   └── README.md
├── continuing-education-recertification-continuity/
│   ├── AGENTS.md
│   └── README.md
├── apprenticeship-work-based-learning-continuity/
│   ├── AGENTS.md
│   └── README.md
├── verifiable-credential-wallet-interoperability/
│   ├── AGENTS.md
│   └── README.md
├── income-payroll-employment-record-continuity/
│   ├── AGENTS.md
│   └── README.md
├── tax-administration-filing-record-continuity/
│   ├── AGENTS.md
│   └── README.md
├── social-security-earnings-benefit-record-continuity/
│   ├── AGENTS.md
│   └── README.md
├── retirement-pension-savings-plan-continuity/
│   ├── AGENTS.md
│   └── README.md
├── unemployment-insurance-wage-record-continuity/
│   ├── AGENTS.md
│   └── README.md
├── workers-compensation-occupational-injury-benefit-continuity/
│   ├── AGENTS.md
│   └── README.md
├── family-medical-leave-job-protection-continuity/
│   ├── AGENTS.md
│   └── README.md
├── paid-sick-family-leave-wage-replacement-continuity/
│   ├── AGENTS.md
│   └── README.md
├── pregnancy-parental-work-continuity/
│   ├── AGENTS.md
│   └── README.md
├── workplace-accommodation-return-to-work-continuity/
│   ├── AGENTS.md
│   └── README.md
├── disability-income-work-capacity-benefit-continuity/
│   ├── AGENTS.md
│   └── README.md
├── family-caregiver-respite-work-continuity/
│   ├── AGENTS.md
│   └── README.md
├── vital-records-life-event-continuity/
│   ├── AGENTS.md
│   └── README.md
├── name-change-identity-record-synchronization-continuity/
│   ├── AGENTS.md
│   └── README.md
├── address-residency-mail-service-continuity/
│   ├── AGENTS.md
│   └── README.md
├── household-composition-dependent-eligibility-continuity/
│   ├── AGENTS.md
│   └── README.md
├── family-law-custody-child-support-continuity/
│   ├── AGENTS.md
│   └── README.md
├── kinship-foster-adoption-care-continuity/
│   ├── AGENTS.md
│   └── README.md
├── banking-deposit-account-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── debt-obligation-collection-relief-continuity/
│   ├── AGENTS.md
│   └── README.md
├── real-property-title-deed-record-continuity/
│   ├── AGENTS.md
│   └── README.md
├── driver-license-vehicle-registration-continuity/
│   ├── AGENTS.md
│   └── README.md
├── passport-travel-document-mobility-continuity/
│   ├── AGENTS.md
│   └── README.md
├── contract-subscription-billing-consent-continuity/
│   ├── AGENTS.md
│   └── README.md
├── notary-document-authentication-signature-continuity/
│   ├── AGENTS.md
│   └── README.md
├── citizenship-nationality-statelessness-continuity/
│   ├── AGENTS.md
│   └── README.md
├── immigration-status-residency-work-authorization-continuity/
│   ├── AGENTS.md
│   └── README.md
├── asylum-refugee-protection-status-continuity/
│   ├── AGENTS.md
│   └── README.md
├── detention-custody-confinement-status-continuity/
│   ├── AGENTS.md
│   └── README.md
├── civil-commitment-involuntary-treatment-rights-continuity/
│   ├── AGENTS.md
│   └── README.md
├── court-notice-service-process-default-judgment-continuity/
│   ├── AGENTS.md
│   └── README.md
├── criminal-record-relief-collateral-consequences-continuity/
│   ├── AGENTS.md
│   └── README.md
├── school-enrollment-attendance-continuity/
│   ├── AGENTS.md
│   └── README.md
├── special-education-iep-504-accommodation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── school-meals-nutrition-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── school-health-services-chronic-condition-continuity/
│   ├── AGENTS.md
│   └── README.md
├── school-transportation-safe-routes-continuity/
│   ├── AGENTS.md
│   └── README.md
├── school-discipline-exclusion-restraint-continuity/
│   ├── AGENTS.md
│   └── README.md
├── school-mental-health-counseling-support-continuity/
│   ├── AGENTS.md
│   └── README.md
├── school-climate-bullying-violence-prevention-continuity/
│   ├── AGENTS.md
│   └── README.md
├── postsecondary-admissions-transfer-articulation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── student-financial-aid-grant-scholarship-continuity/
│   ├── AGENTS.md
│   └── README.md
├── academic-advising-degree-progress-continuity/
│   ├── AGENTS.md
│   └── README.md
├── campus-basic-needs-student-support-continuity/
│   ├── AGENTS.md
│   └── README.md
├── campus-disability-accommodations-accessibility-continuity/
│   ├── AGENTS.md
│   └── README.md
├── campus-mental-health-crisis-student-support-continuity/
│   ├── AGENTS.md
│   └── README.md
├── campus-safety-title-ix-clery-continuity/
│   ├── AGENTS.md
│   └── README.md
├── international-student-sevis-status-continuity/
│   ├── AGENTS.md
│   └── README.md
├── email-account-recovery-continuity/
│   ├── AGENTS.md
│   └── README.md
├── phone-number-sim-portability-account-security-continuity/
│   ├── AGENTS.md
│   └── README.md
├── mfa-passkey-credential-recovery-continuity/
│   ├── AGENTS.md
│   └── README.md
├── password-manager-secret-vault-continuity/
│   ├── AGENTS.md
│   └── README.md
├── cloud-backup-file-sync-data-portability-continuity/
│   ├── AGENTS.md
│   └── README.md
├── messaging-contact-graph-portability-continuity/
│   ├── AGENTS.md
│   └── README.md
├── domain-dns-web-presence-continuity/
│   ├── AGENTS.md
│   └── README.md
├── platform-account-suspension-appeals-continuity/
│   ├── AGENTS.md
│   └── README.md
├── personal-computing-device-lifecycle-repair-continuity/
│   ├── AGENTS.md
│   └── README.md
├── home-network-router-iot-security-continuity/
│   ├── AGENTS.md
│   └── README.md
├── software-supply-chain-dependency-provenance-continuity/
│   ├── AGENTS.md
│   └── README.md
├── software-update-vulnerability-patch-continuity/
│   ├── AGENTS.md
│   └── README.md
├── open-source-maintainer-sustainability-continuity/
│   ├── AGENTS.md
│   └── README.md
├── pki-certificate-cryptographic-trust-continuity/
│   ├── AGENTS.md
│   └── README.md
├── cloud-service-exit-interoperability-continuity/
│   ├── AGENTS.md
│   └── README.md
├── api-platform-dependency-runtime-continuity/
│   ├── AGENTS.md
│   └── README.md
├── cognitive-augmentation/
│   ├── AGENTS.md
│   └── README.md
├── digital-identity-security/
│   ├── AGENTS.md
│   └── README.md
├── disembodied-cns/
│   ├── AGENTS.md
│   └── README.md
├── future-waiting/
│   ├── AGENTS.md
│   ├── README.md
│   └── paths/
├── governance-rights/
│   ├── AGENTS.md
│   └── README.md
├── immune-maintenance/
│   ├── AGENTS.md
│   └── README.md
├── longevity-evidence/
│   ├── AGENTS.md
│   ├── README.md
│   ├── data/
│   ├── docs/
│   └── scripts/
├── genomic-stability-dna-repair/
│   ├── AGENTS.md
│   └── README.md
├── telomere-maintenance/
│   ├── AGENTS.md
│   └── README.md
├── proteostasis-autophagy/
│   ├── AGENTS.md
│   └── README.md
├── mitochondrial-bioenergetics/
│   ├── AGENTS.md
│   └── README.md
├── cellular-senescence-clearance/
│   ├── AGENTS.md
│   └── README.md
├── extracellular-matrix-glycation/
│   ├── AGENTS.md
│   └── README.md
├── financial-resilience-access/
│   ├── AGENTS.md
│   └── README.md
├── food-security-nutrition-access/
│   ├── AGENTS.md
│   └── README.md
├── water-sanitation-hygiene-continuity/
│   ├── AGENTS.md
│   └── README.md
├── energy-access-resilience/
│   ├── AGENTS.md
│   └── README.md
├── healthcare-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── medicine-access-treatment-continuity/
│   ├── AGENTS.md
│   └── README.md
├── patient-data-interoperability/
│   ├── AGENTS.md
│   └── README.md
├── telehealth-remote-monitoring-access/
│   ├── AGENTS.md
│   └── README.md
├── health-data-privacy-governance/
│   ├── AGENTS.md
│   └── README.md
├── functioning-quality-of-life-outcomes/
│   ├── AGENTS.md
│   └── README.md
├── health-economics-value-assessment/
│   ├── AGENTS.md
│   └── README.md
├── immunization-public-health-surveillance/
│   ├── AGENTS.md
│   └── README.md
├── maternal-newborn-child-development/
│   ├── AGENTS.md
│   └── README.md
├── patient-safety-organizational-learning/
│   ├── AGENTS.md
│   └── README.md
├── caregiving-long-term-care/
│   ├── AGENTS.md
│   └── README.md
├── housing-built-environment-stability/
│   ├── AGENTS.md
│   └── README.md
├── transportation-access-mobility/
│   ├── AGENTS.md
│   └── README.md
├── legal-identity-civil-registration/
│   ├── AGENTS.md
│   └── README.md
├── access-to-justice-legal-aid/
│   ├── AGENTS.md
│   └── README.md
├── civic-participation-election-access/
│   ├── AGENTS.md
│   └── README.md
├── migration-displacement-humanitarian-continuity/
│   ├── AGENTS.md
│   └── README.md
├── digital-inclusion-connectivity/
│   ├── AGENTS.md
│   └── README.md
├── social-protection-benefits-delivery/
│   ├── AGENTS.md
│   └── README.md
├── community-resource-navigation/
│   ├── AGENTS.md
│   └── README.md
├── social-determinants-community-vulnerability/
│   ├── AGENTS.md
│   └── README.md
├── public-service-design-accessibility/
│   ├── AGENTS.md
│   └── README.md
├── emergency-alerts-communications/
│   ├── AGENTS.md
│   └── README.md
├── disaster-recovery-relief-continuity/
│   ├── AGENTS.md
│   └── README.md
├── financial-inclusion-payment-systems/
│   ├── AGENTS.md
│   └── README.md
├── workforce-employment-services/
│   ├── AGENTS.md
│   └── README.md
├── household-emergency-preparedness-resilience/
│   ├── AGENTS.md
│   └── README.md
├── media-information-literacy-public-libraries/
│   ├── AGENTS.md
│   └── README.md
├── health-workforce-capacity/
│   ├── AGENTS.md
│   └── README.md
├── administrative-burden-procedural-friction/
│   ├── AGENTS.md
│   └── README.md
├── community-health-workers-peer-support/
│   ├── AGENTS.md
│   └── README.md
├── civic-data-open-government-transparency/
│   ├── AGENTS.md
│   └── README.md
├── education-access-lifelong-learning/
│   ├── AGENTS.md
│   └── README.md
├── research-infrastructure-open-science-translation/
│   ├── AGENTS.md
│   └── README.md
├── standards-metrology-quality-infrastructure/
│   ├── AGENTS.md
│   └── README.md
├── cybersecurity-resilience-critical-services/
│   ├── AGENTS.md
│   └── README.md
├── compute-data-center-ai-infrastructure/
│   ├── AGENTS.md
│   └── README.md
├── clinical-trials-regulatory-science-translation/
│   ├── AGENTS.md
│   └── README.md
├── geospatial-navigation-location-infrastructure/
│   ├── AGENTS.md
│   └── README.md
├── weather-climate-observation-forecasting/
│   ├── AGENTS.md
│   └── README.md
├── building-fire-life-safety-codes/
│   ├── AGENTS.md
│   └── README.md
├── manufacturing-repair-capacity/
│   ├── AGENTS.md
│   └── README.md
├── public-procurement-contracting-capacity/
│   ├── AGENTS.md
│   └── README.md
├── animal-health-zoonotic-interface-one-health/
│   ├── AGENTS.md
│   └── README.md
├── public-health-laboratory-diagnostic-capacity/
│   ├── AGENTS.md
│   └── README.md
├── blood-organ-tissue-biovigilance-transplantation/
│   ├── AGENTS.md
│   └── README.md
├── waste-management-hazardous-materials-continuity/
│   ├── AGENTS.md
│   └── README.md
├── radiation-nuclear-safety-protection/
│   ├── AGENTS.md
│   └── README.md
├── chemical-safety-poison-control-toxicology/
│   ├── AGENTS.md
│   └── README.md
├── critical-minerals-materials-resilience/
│   ├── AGENTS.md
│   └── README.md
├── air-quality-ventilation-exposure-control/
│   ├── AGENTS.md
│   └── README.md
├── food-safety-contamination-control/
│   ├── AGENTS.md
│   └── README.md
├── occupational-exposure-industrial-hygiene/
│   ├── AGENTS.md
│   └── README.md
├── medical-device-equipment-safety-maintenance/
│   ├── AGENTS.md
│   └── README.md
├── sterilization-disinfection-infection-control/
│   ├── AGENTS.md
│   └── README.md
├── built-environment-accessibility-universal-design/
│   ├── AGENTS.md
│   └── README.md
├── clinical-laboratory-diagnostic-quality/
│   ├── AGENTS.md
│   └── README.md
├── pharmacovigilance-drug-safety-monitoring/
│   ├── AGENTS.md
│   └── README.md
├── pharmaceutical-quality-supply-integrity/
│   ├── AGENTS.md
│   └── README.md
├── emergency-medical-services-prehospital-care/
│   ├── AGENTS.md
│   └── README.md
├── surgical-anesthesia-perioperative-safety/
│   ├── AGENTS.md
│   └── README.md
├── road-traffic-injury-prevention-safe-mobility/
│   ├── AGENTS.md
│   └── README.md
├── rural-health-access-geographic-equity/
│   ├── AGENTS.md
│   └── README.md
├── homelessness-unsheltered-health-continuity/
│   ├── AGENTS.md
│   └── README.md
├── correctional-health-reentry-continuity/
│   ├── AGENTS.md
│   └── README.md
├── disability-services-independent-living/
│   ├── AGENTS.md
│   └── README.md
├── dementia-cognitive-decline-care-continuity/
│   ├── AGENTS.md
│   └── README.md
├── chronic-infectious-disease-care-continuity/
│   ├── AGENTS.md
│   └── README.md
├── suicide-crisis-response-continuity/
│   ├── AGENTS.md
│   └── README.md
├── substance-use-treatment-recovery-continuity/
│   ├── AGENTS.md
│   └── README.md
├── elder-justice-adult-protective-services/
│   ├── AGENTS.md
│   └── README.md
├── child-protection-family-safety/
│   ├── AGENTS.md
│   └── README.md
├── fraud-scams-consumer-protection/
│   ├── AGENTS.md
│   └── README.md
├── online-safety-digital-harm-prevention/
│   ├── AGENTS.md
│   └── README.md
├── rare-disease-diagnostic-odyssey-care-coordination/
│   ├── AGENTS.md
│   └── README.md
├── multimorbidity-polypharmacy-care-coordination/
│   ├── AGENTS.md
│   └── README.md
├── care-transitions-discharge-continuity/
│   ├── AGENTS.md
│   └── README.md
├── home-health-hospice-palliative-care-continuity/
│   ├── AGENTS.md
│   └── README.md
├── medical-interpreter-cultural-mediation/
│   ├── AGENTS.md
│   └── README.md
├── patient-advocacy-shared-decision-making/
│   ├── AGENTS.md
│   └── README.md
├── life-logging-personal-archives-continuity/
│   ├── AGENTS.md
│   └── README.md
├── digital-legacy-data-succession/
│   ├── AGENTS.md
│   └── README.md
├── wearables-continuous-sensing-personal-informatics/
│   ├── AGENTS.md
│   └── README.md
├── personal-knowledge-management-cognitive-offloading/
│   ├── AGENTS.md
│   └── README.md
├── brain-computer-interface-neurotechnology-governance/
│   ├── AGENTS.md
│   └── README.md
├── robotics-embodied-assistance-care-automation/
│   ├── AGENTS.md
│   └── README.md
├── armed-conflict-civilian-protection-ihl/
│   ├── AGENTS.md
│   └── README.md
├── peacebuilding-conflict-prevention-social-cohesion/
│   ├── AGENTS.md
│   └── README.md
├── continuity-of-government-public-administration-resilience/
│   ├── AGENTS.md
│   └── README.md
├── telecommunications-network-resilience-continuity/
│   ├── AGENTS.md
│   └── README.md
├── macroeconomic-monetary-fiscal-stability/
│   ├── AGENTS.md
│   └── README.md
├── anti-corruption-public-integrity-accountability/
│   ├── AGENTS.md
│   └── README.md
├── agricultural-production-food-system-resilience/
│   ├── AGENTS.md
│   └── README.md
├── soil-health-land-degradation-drought-resilience/
│   ├── AGENTS.md
│   └── README.md
├── water-resources-hydrology-flood-drought-management/
│   ├── AGENTS.md
│   └── README.md
├── biodiversity-ecosystem-services-resilience/
│   ├── AGENTS.md
│   └── README.md
├── wildfire-landscape-fire-resilience/
│   ├── AGENTS.md
│   └── README.md
├── freight-logistics-port-cold-chain-continuity/
│   ├── AGENTS.md
│   └── README.md
├── coastal-marine-resilience-blue-economy-continuity/
│   ├── AGENTS.md
│   └── README.md
├── fisheries-aquatic-food-systems-continuity/
│   ├── AGENTS.md
│   └── README.md
├── dams-levees-flood-control-infrastructure-safety/
│   ├── AGENTS.md
│   └── README.md
├── public-works-civil-infrastructure-asset-management/
│   ├── AGENTS.md
│   └── README.md
├── urban-planning-land-use-zoning-resilience/
│   ├── AGENTS.md
│   └── README.md
├── green-blue-infrastructure-urban-nature-cooling/
│   ├── AGENTS.md
│   └── README.md
├── electric-grid-reliability-resilience-continuity/
│   ├── AGENTS.md
│   └── README.md
├── water-wastewater-utility-service-continuity/
│   ├── AGENTS.md
│   └── README.md
├── fuel-thermal-energy-service-continuity/
│   ├── AGENTS.md
│   └── README.md
├── public-transit-service-operations-continuity/
│   ├── AGENTS.md
│   └── README.md
├── critical-infrastructure-lifeline-interdependency-resilience/
│   ├── AGENTS.md
│   └── README.md
├── utility-affordability-shutoff-protection-continuity/
│   ├── AGENTS.md
│   └── README.md
├── insurance-risk-transfer/
│   ├── AGENTS.md
│   └── README.md
├── childcare-family-continuity/
│   ├── AGENTS.md
│   └── README.md
├── emergency-preparedness-response/
│   ├── AGENTS.md
│   └── README.md
├── personal-safety-violence-prevention/
│   ├── AGENTS.md
│   └── README.md
├── product-safety-recall-systems/
│   ├── AGENTS.md
│   └── README.md
├── microbiome-ecology/
│   ├── AGENTS.md
│   └── README.md
├── stem-cell-reserve-renewal/
│   ├── AGENTS.md
│   └── README.md
├── renal-hepatic-clearance/
│   ├── AGENTS.md
│   └── README.md
├── gastrointestinal-barrier-absorption/
│   ├── AGENTS.md
│   └── README.md
├── respiratory-oxygenation/
│   ├── AGENTS.md
│   └── README.md
├── blood-oxygen-hemostasis/
│   ├── AGENTS.md
│   └── README.md
├── endocrine-hormonal-regulation/
│   ├── AGENTS.md
│   └── README.md
├── lymphatic-glymphatic-clearance/
│   ├── AGENTS.md
│   └── README.md
├── fluid-electrolyte-acid-base-homeostasis/
│   ├── AGENTS.md
│   └── README.md
├── thermal-homeostasis-resilience/
│   ├── AGENTS.md
│   └── README.md
├── nutrition-metabolic-health/
│   ├── AGENTS.md
│   └── README.md
├── physical-activity-mobility/
│   ├── AGENTS.md
│   └── README.md
├── cardiovascular-resilience/
│   ├── AGENTS.md
│   └── README.md
├── musculoskeletal-integrity/
│   ├── AGENTS.md
│   └── README.md
├── skin-barrier-wound-healing/
│   ├── AGENTS.md
│   └── README.md
├── urogenital-continuity/
│   ├── AGENTS.md
│   └── README.md
├── reproductive-fertility-continuity/
│   ├── AGENTS.md
│   └── README.md
├── measurement-feedback/
│   ├── AGENTS.md
│   └── README.md
├── mental-health-affective-stability/
│   ├── AGENTS.md
│   └── README.md
├── memory-editing/
│   ├── AGENTS.md
│   └── README.md
├── neuro-continuity/
│   ├── AGENTS.md
│   └── README.md
├── pain-suffering-control/
│   ├── AGENTS.md
│   └── README.md
├── planetary-health-environment/
│   ├── AGENTS.md
│   └── README.md
├── regenerative-medicine/
│   ├── AGENTS.md
│   └── README.md
├── rehabilitation-functioning/
│   ├── AGENTS.md
│   └── README.md
├── resource-social-infra/
│   ├── AGENTS.md
│   └── README.md
├── risk-engineering/
│   ├── AGENTS.md
│   └── README.md
├── sensory-continuity/
│   ├── AGENTS.md
│   └── README.md
├── sleep-circadian-recovery/
│   ├── AGENTS.md
│   └── README.md
├── social-connection-relational-infra/
│   ├── AGENTS.md
│   └── README.md
├── space-extreme-habitation/
│   ├── AGENTS.md
│   └── README.md
├── substance-exposure-control/
│   ├── AGENTS.md
│   └── README.md
├── supply-chain-continuity/
│   ├── AGENTS.md
│   └── README.md
├── synthetic-biology-biosecurity/
│   ├── AGENTS.md
│   └── README.md
├── health-literacy-navigation/
│   ├── AGENTS.md
│   └── README.md
├── language-access-plain-communication/
│   ├── AGENTS.md
│   └── README.md
├── labor-rights-workplace-protection/
│   ├── AGENTS.md
│   └── README.md
├── information-integrity-trust/
│   ├── AGENTS.md
│   └── README.md
├── learning-skill-acquisition/
│   ├── AGENTS.md
│   └── README.md
├── occupational-work-design/
│   ├── AGENTS.md
│   └── README.md
├── oral-health-continuity/
│   ├── AGENTS.md
│   └── README.md
└── time-allocation-effective-time/
    ├── AGENTS.md
    └── README.md
```

## 职责边界

- `longevity-evidence/` 是当前唯一含数据和采集脚本的产品化子域。
- `genomic-stability-dna-repair/`、`telomere-maintenance/`、`proteostasis-autophagy/`、`mitochondrial-bioenergetics/`、`cellular-senescence-clearance/`、`extracellular-matrix-glycation/`、`microbiome-ecology/`、`stem-cell-reserve-renewal/` 和 `renal-hepatic-clearance/` 负责分子维护、结构材料、宿主生态、内源性修复和肝肾清除底座。
- `respiratory-oxygenation/`、`blood-oxygen-hemostasis/`、`endocrine-hormonal-regulation/` 和 `lymphatic-glymphatic-clearance/` 负责氧合、血液运输、激素协调和清除网络这些跨器官稳态条件。
- `gastrointestinal-barrier-absorption/`、`fluid-electrolyte-acid-base-homeostasis/` 和 `thermal-homeostasis-resilience/` 负责营养进入、内环境化学和体温边界这些基础稳态条件。
- `nutrition-metabolic-health/`、`physical-activity-mobility/`、`cardiovascular-resilience/` 和 `musculoskeletal-integrity/` 负责营养、行动、循环和承载结构这些身体运行条件。
- `urogenital-continuity/` 和 `reproductive-fertility-continuity/` 负责尿控、泌尿感染、性功能、生育力、生殖衰老和未来选择权。
- `attention-executive-control/`、`learning-skill-acquisition/` 和 `time-allocation-effective-time/` 负责注意力、学习能力和有效时间这些主体代理与任务资源条件。
- `financial-resilience-access/`、`financial-inclusion-payment-systems/`、`workforce-employment-services/`、`education-access-lifelong-learning/`、`occupational-work-design/`、`labor-rights-workplace-protection/`、`language-access-plain-communication/`、`media-information-literacy-public-libraries/` 和 `information-integrity-trust/` 负责财务韧性、金融支付入口、就业服务、教育与终身学习、工作环境、劳动权利、语言理解入口、公共知识入口和信息可信度这些资源入口与认知环境条件。
- `food-security-nutrition-access/`、`water-sanitation-hygiene-continuity/`、`energy-access-resilience/`、`social-protection-benefits-delivery/`、`community-resource-navigation/`、`social-determinants-community-vulnerability/`、`public-service-design-accessibility/`、`administrative-burden-procedural-friction/`、`civic-data-open-government-transparency/`、`insurance-risk-transfer/` 和 `childcare-family-continuity/` 负责食物、水卫生、能源、公共福利、社区资源导航、社区脆弱性、公共服务可达、行政负担、开放数据透明、保险风险池和托育家庭连续性这些基础生计、公共服务与风险分摊条件。
- `research-infrastructure-open-science-translation/`、`standards-metrology-quality-infrastructure/`、`compute-data-center-ai-infrastructure/`、`cybersecurity-resilience-critical-services/`、`geospatial-navigation-location-infrastructure/`、`manufacturing-repair-capacity/`、`supply-chain-continuity/` 和 `ai-agency-safety/` 负责科研转化、标准计量质量、算力 AI 基础设施、网络安全韧性、空间定位导航、制造维修能力、供应链连续和 AI 代理安全这些技术窗口生成、可信化和可用性的外部底座。
- `healthcare-access-continuity/`、`medicine-access-treatment-continuity/`、`patient-data-interoperability/`、`telehealth-remote-monitoring-access/`、`health-data-privacy-governance/`、`functioning-quality-of-life-outcomes/`、`health-economics-value-assessment/`、`clinical-trials-regulatory-science-translation/`、`immunization-public-health-surveillance/`、`animal-health-zoonotic-interface-one-health/`、`maternal-newborn-child-development/`、`patient-safety-organizational-learning/`、`health-workforce-capacity/`、`community-health-workers-peer-support/`、`caregiving-long-term-care/`、`housing-built-environment-stability/`、`building-fire-life-safety-codes/`、`transportation-access-mobility/`、`legal-identity-civil-registration/`、`emergency-preparedness-response/`、`weather-climate-observation-forecasting/`、`emergency-alerts-communications/`、`household-emergency-preparedness-resilience/` 和 `disaster-recovery-relief-continuity/` 负责医疗接入、药品治疗连续性、患者数据互操作、远程照护、健康数据治理、结局评估、价值评估、临床监管转化、公共卫生监测、动物健康界面、早期生命发展、患者安全、健康劳动力、社区中介支持、长期照护、居住空间、建筑消防生命安全、交通可达、法律身份、应急响应、天气气候观测、预警通信、家庭准备和灾后恢复这些服务接入与生活连续性条件。
- `public-procurement-contracting-capacity/` 负责公共采购、合同、供应商管理、应急采购、透明度和交付验收这些公共能力落地条件。
- `public-health-laboratory-diagnostic-capacity/`、`blood-organ-tissue-biovigilance-transplantation/`、`waste-management-hazardous-materials-continuity/`、`radiation-nuclear-safety-protection/`、`chemical-safety-poison-control-toxicology/` 和 `critical-minerals-materials-resilience/` 负责风险确认、外部生物材料安全、残余物治理、不可见高能暴露、化学毒理和未来技术物质输入这些外部安全与材料支撑条件。
- `air-quality-ventilation-exposure-control/`、`food-safety-contamination-control/`、`occupational-exposure-industrial-hygiene/`、`medical-device-equipment-safety-maintenance/`、`sterilization-disinfection-infection-control/` 和 `built-environment-accessibility-universal-design/` 负责可呼吸环境、食物污染控制、工作暴露控制、医疗设备可靠性、感染控制屏障和物理空间可达性这些日常环境与工具可靠性条件。
- `clinical-laboratory-diagnostic-quality/`、`pharmacovigilance-drug-safety-monitoring/`、`pharmaceutical-quality-supply-integrity/`、`emergency-medical-services-prehospital-care/`、`surgical-anesthesia-perioperative-safety/` 和 `road-traffic-injury-prevention-safe-mobility/` 负责临床检验质量、真实世界药品安全、药品质量完整性、院前急救窗口、围手术期安全和道路交通伤害预防这些临床可靠性与急性风险窗口条件。
- `rural-health-access-geographic-equity/`、`homelessness-unsheltered-health-continuity/`、`correctional-health-reentry-continuity/`、`disability-services-independent-living/`、`dementia-cognitive-decline-care-continuity/` 和 `chronic-infectious-disease-care-continuity/` 负责农村地理可及、无家可归健康连续性、羁押重返服务连续性、残障独立生活、认知衰退照护和慢性传染病长期照护这些结构性脆弱与连续照护断点。
- `suicide-crisis-response-continuity/`、`substance-use-treatment-recovery-continuity/`、`elder-justice-adult-protective-services/`、`child-protection-family-safety/`、`fraud-scams-consumer-protection/` 和 `online-safety-digital-harm-prevention/` 负责自杀危机响应、物质使用障碍治疗恢复、老年正义成人保护、儿童保护家庭安全、诈骗消费者保护和在线数字伤害预防这些危机、剥削与恢复连续性条件。
- `rare-disease-diagnostic-odyssey-care-coordination/`、`multimorbidity-polypharmacy-care-coordination/`、`care-transitions-discharge-continuity/`、`home-health-hospice-palliative-care-continuity/`、`medical-interpreter-cultural-mediation/` 和 `patient-advocacy-shared-decision-making/` 负责罕见病诊断漫游、多病共存多重用药、照护转移、居家/缓和/安宁疗护、医疗解释文化中介和患者共同决策这些复杂照护导航、交接与决策连续性条件。
- `life-logging-personal-archives-continuity/`、`digital-legacy-data-succession/`、`wearables-continuous-sensing-personal-informatics/`、`personal-knowledge-management-cognitive-offloading/`、`brain-computer-interface-neurotechnology-governance/` 和 `robotics-embodied-assistance-care-automation/` 负责生命日志个人档案、数字遗产继承、连续感知、个人知识管理、神经接口治理和具身辅助这些外部化主体连续性条件。
- `armed-conflict-civilian-protection-ihl/`、`peacebuilding-conflict-prevention-social-cohesion/`、`continuity-of-government-public-administration-resilience/`、`telecommunications-network-resilience-continuity/`、`macroeconomic-monetary-fiscal-stability/` 和 `anti-corruption-public-integrity-accountability/` 负责武装冲突平民保护、和平建设、政府连续性、通信网络韧性、宏观稳定和公共廉洁这些文明连续性与集体安全条件。
- `agricultural-production-food-system-resilience/`、`soil-health-land-degradation-drought-resilience/`、`water-resources-hydrology-flood-drought-management/`、`biodiversity-ecosystem-services-resilience/`、`wildfire-landscape-fire-resilience/` 和 `freight-logistics-port-cold-chain-continuity/` 负责农业生产、土壤土地、水资源、生态系统服务、野火韧性和物流冷链这些初级生产、自然系统与物理流通条件。
- `coastal-marine-resilience-blue-economy-continuity/`、`fisheries-aquatic-food-systems-continuity/`、`dams-levees-flood-control-infrastructure-safety/`、`public-works-civil-infrastructure-asset-management/`、`urban-planning-land-use-zoning-resilience/` 和 `green-blue-infrastructure-urban-nature-cooling/` 负责海岸海洋、水生食物、防洪工程、公共工程资产、城市空间治理和绿蓝基础设施这些自然-工程-城市交界条件。
- `electric-grid-reliability-resilience-continuity/`、`water-wastewater-utility-service-continuity/`、`fuel-thermal-energy-service-continuity/`、`public-transit-service-operations-continuity/`、`critical-infrastructure-lifeline-interdependency-resilience/` 和 `utility-affordability-shutoff-protection-continuity/` 负责电网、水务污水、燃料热能、公共交通、关键基础设施生命线互依赖和公用事业可负担性这些日常运行生命线条件。
- `gene-therapy-genome-editing-delivery-safety/`、`biological-age-clocks-biomarker-validation/`、`multiomics-personal-baseline-systems-biology/`、`engineered-cell-therapy-regenerative-platforms/`、`organoids-organ-on-chip-disease-models/` 和 `xenotransplantation-bioengineered-organ-replacement/` 负责基因治疗与编辑递送安全、生物年龄钟验证、多组学个人基线、工程细胞疗法、人体相关疾病模型和器官替换平台这些生物医学平台条件。
- `causal-inference-target-trial-emulation/`、`survival-analysis-healthspan-risk-modeling/`、`human-digital-twin-life-course-simulation/`、`implementation-science-adherence-behavior-change/`、`uncertainty-quantification-model-calibration/` 和 `data-quality-missingness-representativeness/` 负责因果识别、寿命/健康寿命风险、生命历程仿真、实施落地、模型校准和数据质量这些定量方法学条件。
- `privacy-preserving-computation-federated-learning/`、`knowledge-graph-ontology-semantic-interoperability/`、`model-cards-ai-audit-documentation/`、`technology-foresight-horizon-scanning/`、`research-portfolio-prioritization-funding-governance/` 和 `intellectual-property-technology-transfer-access/` 负责隐私保护计算、语义知识组织、模型审计、未来技术信号、研究组合排序和技术转移可及这些知识治理与技术扩散条件。
- `trustworthy-scientific-communication-peer-review/`、`research-participant-consent-community-engagement/`、`biobanking-biospecimen-quality-chain-of-custody/`、`longitudinal-cohort-retention-followup-infrastructure/`、`registries-real-world-data-governance/` 和 `scientific-instrumentation-sensor-calibration-maintenance/` 负责可信科研传播、研究参与者同意、样本质量保管链、纵向队列随访、真实世界登记和仪器传感器校准这些科研证据基础设施条件。
- `nanomedicine-targeted-delivery-molecular-repair/`、`ai-drug-discovery-protein-design/`、`epigenetic-editing-gene-regulation-therapeutics/`、`brain-preservation-connectomics-emulation/`、`post-quantum-cryptography-long-term-data-security/`、`safety-critical-software-formal-methods/` 和 `long-term-digital-preservation-format-migration/` 负责未来技术窗口生成、递送、调控、信息保存、长期数字安全、软件可信和外部记忆可读性这些未来技术连续性条件。
- `cerebrovascular-stroke-brain-perfusion-resilience/`、`traumatic-brain-injury-neurotrauma-recovery/`、`delirium-acute-cognitive-failure-prevention/`、`disorders-of-consciousness-coma-recovery/`、`epilepsy-seizure-network-stability/`、`autonomic-nervous-system-homeostasis/` 和 `migraine-headache-effective-time-burden/` 负责卒中脑灌注、神经创伤、谵妄、意识障碍、癫痫、自主神经和偏头痛这些急性神经连续性与意识韧性条件。
- `vision-eye-health-continuity/`、`hearing-auditory-communication-continuity/`、`vestibular-balance-spatial-orientation/`、`speech-language-communication-continuity/`、`swallowing-dysphagia-aspiration-nutrition/`、`smell-taste-chemosensory-continuity/` 和 `peripheral-neuropathy-somatosensory-continuity/` 负责视觉输入、听觉沟通、空间平衡、语言表达、吞咽摄食、化学感知和身体边界反馈这些感官、沟通与具身反馈连续性条件。
- `space-weather-geomagnetic-storm-resilience/`、`planetary-defense-near-earth-object-risk/`、`volcanic-ashfall-geohazard-continuity/`、`earthquake-seismic-risk-built-environment-continuity/`、`tsunami-warning-coastal-evacuation-continuity/` 和 `extreme-heat-cooling-public-health-continuity/` 负责空间天气、近地天体、火山灰、地震、海啸和极端高温这些行星、地球物理与极端热风险连续性条件。
- `noise-exposure-acoustic-environment-continuity/`、`light-exposure-circadian-environment-continuity/`、`lead-heavy-metal-exposure-control/`、`radon-asbestos-indoor-hazard-continuity/`、`mold-dampness-indoor-biological-exposure/` 和 `vector-borne-disease-environmental-control/` 负责噪声、光照节律、铅与重金属、氡与石棉、霉菌潮湿和病媒传播这些慢性环境暴露与日常损耗条件。
- `advance-care-planning-medical-decision-continuity/`、`supported-decision-making-guardianship-rights/`、`healthcare-personal-representative-hipaa-access-continuity/`、`financial-fiduciary-power-of-attorney-continuity/`、`representative-payee-benefits-management-continuity/` 和 `trust-estate-affairs-succession-continuity/` 负责预先医疗照护计划、支持性决策、医疗个人代表、财务受托、代表收款人和事务继承这些决策权、代理权与受托连续性条件。
- `credit-consumer-reporting-access-continuity/`、`tenant-screening-rental-access-continuity/`、`background-check-record-screening-continuity/`、`employment-algorithmic-hiring-screening-continuity/`、`insurance-underwriting-algorithmic-risk-scoring-continuity/` 和 `public-benefits-eligibility-automated-decision-continuity/` 负责信用与消费者报告、租房筛查、背景记录筛查、算法招聘、保险算法评分和公共福利自动资格系统这些算法化准入、筛查与资格连续性条件。
- `education-record-transcript-verification-continuity/`、`professional-licensure-certification-continuity/`、`skills-competency-credentialing-continuity/`、`continuing-education-recertification-continuity/`、`apprenticeship-work-based-learning-continuity/` 和 `verifiable-credential-wallet-interoperability/` 负责教育记录核验、职业证照认证、技能胜任力凭证、继续教育再认证、学徒制工作中学习和可验证凭证钱包互操作这些资格证明、授权与能力可携带连续性条件。
- `income-payroll-employment-record-continuity/`、`tax-administration-filing-record-continuity/`、`social-security-earnings-benefit-record-continuity/`、`retirement-pension-savings-plan-continuity/`、`unemployment-insurance-wage-record-continuity/` 和 `workers-compensation-occupational-injury-benefit-continuity/` 负责工资雇佣记录、税务申报记录、社会保险收入与福利记录、退休养老金计划、失业保险工资记录和工伤职业伤害权益这些劳动成果到未来保障的记录连续性条件。
- `family-medical-leave-job-protection-continuity/`、`paid-sick-family-leave-wage-replacement-continuity/`、`pregnancy-parental-work-continuity/`、`workplace-accommodation-return-to-work-continuity/`、`disability-income-work-capacity-benefit-continuity/` 和 `family-caregiver-respite-work-continuity/` 负责家庭医疗假岗位保护、带薪病假/家庭假工资替代、孕产育儿工作连续性、合理便利复工、残障收入与工作能力福利、家庭照护者喘息与工作连续性这些工作中断与照护事件连续性条件。
- `vital-records-life-event-continuity/`、`name-change-identity-record-synchronization-continuity/`、`address-residency-mail-service-continuity/`、`household-composition-dependent-eligibility-continuity/`、`family-law-custody-child-support-continuity/` 和 `kinship-foster-adoption-care-continuity/` 负责生命事件记录、姓名变更同步、地址居住地邮件路由、家庭组成资格关系、家庭法监护抚养、亲属照护寄养收养这些家庭事实与制度记录连续性条件。
- `banking-deposit-account-access-continuity/`、`debt-obligation-collection-relief-continuity/`、`real-property-title-deed-record-continuity/`、`driver-license-vehicle-registration-continuity/`、`passport-travel-document-mobility-continuity/`、`contract-subscription-billing-consent-continuity/` 和 `notary-document-authentication-signature-continuity/` 负责银行账户存款访问、债务义务催收救济、不动产权属地契、驾照车辆登记、护照旅行证件、合同订阅账单、公证文件认证签名这些资源控制、移动资格与交易执行连续性条件。
- `citizenship-nationality-statelessness-continuity/`、`immigration-status-residency-work-authorization-continuity/`、`asylum-refugee-protection-status-continuity/`、`detention-custody-confinement-status-continuity/`、`civil-commitment-involuntary-treatment-rights-continuity/`、`court-notice-service-process-default-judgment-continuity/` 和 `criminal-record-relief-collateral-consequences-continuity/` 负责公民国籍无国籍、移民居留工作授权、庇护难民保护、拘押羁押监管状态、非自愿治疗权利、法院通知缺席判决和犯罪记录附带后果这些法律状态与强制程序连续性条件。
- `school-enrollment-attendance-continuity/`、`special-education-iep-504-accommodation-continuity/`、`school-meals-nutrition-access-continuity/`、`school-health-services-chronic-condition-continuity/`、`school-transportation-safe-routes-continuity/`、`school-discipline-exclusion-restraint-continuity/`、`school-mental-health-counseling-support-continuity/` 和 `school-climate-bullying-violence-prevention-continuity/` 负责入学出勤、特殊教育 IEP/504、校餐营养、学校健康服务、通学安全、纪律排除约束、学校心理健康和学校气候欺凌暴力预防这些学校服务连续性条件。
- `postsecondary-admissions-transfer-articulation-continuity/`、`student-financial-aid-grant-scholarship-continuity/`、`academic-advising-degree-progress-continuity/`、`campus-basic-needs-student-support-continuity/`、`campus-disability-accommodations-accessibility-continuity/`、`campus-mental-health-crisis-student-support-continuity/`、`campus-safety-title-ix-clery-continuity/` 和 `international-student-sevis-status-continuity/` 负责高等教育入学转学衔接、学生资助奖助学金、学业指导学位进度、校园基本需求、校园残障便利、校园心理危机支持、校园安全 Title IX/Clery 和国际学生 SEVIS 身份这些高等教育学生生命周期连续性条件。
- `email-account-recovery-continuity/`、`phone-number-sim-portability-account-security-continuity/`、`mfa-passkey-credential-recovery-continuity/`、`password-manager-secret-vault-continuity/`、`cloud-backup-file-sync-data-portability-continuity/`、`messaging-contact-graph-portability-continuity/`、`domain-dns-web-presence-continuity/` 和 `platform-account-suspension-appeals-continuity/` 负责邮箱账号恢复、手机号 SIM 携转安全、MFA/passkey 凭证恢复、密码管理器密钥库、云备份文件同步数据可携带、消息联系人图谱可携带、域名 DNS Web 存在和平台账号停权申诉这些数字账户与通信可达连续性条件。
- `personal-computing-device-lifecycle-repair-continuity/`、`home-network-router-iot-security-continuity/`、`software-supply-chain-dependency-provenance-continuity/`、`software-update-vulnerability-patch-continuity/`、`open-source-maintainer-sustainability-continuity/`、`pki-certificate-cryptographic-trust-continuity/`、`cloud-service-exit-interoperability-continuity/` 和 `api-platform-dependency-runtime-continuity/` 负责个人计算设备生命周期维修、家庭网络路由器 IoT 安全、软件供应链来源证明、软件更新漏洞补丁、开源维护者可持续、PKI 证书密码信任、云服务退出互操作和 API 平台运行时依赖这些软件、设备与信任连续性条件。
- `access-to-justice-legal-aid/`、`civic-participation-election-access/`、`migration-displacement-humanitarian-continuity/` 和 `digital-inclusion-connectivity/` 负责司法可及、公民参与、迁移流离失所人道连续性和数字连接这些制度参与与公共服务接入条件。
- `personal-safety-violence-prevention/` 和 `product-safety-recall-systems/` 负责暴力预防、受害者支持、产品缺陷报告、召回和纠正这些公共安全连续性条件。
- `cellular-reprogramming/` 负责山中因子、部分重编程、化学重编程、AI 因子设计和表观遗传编辑等“细胞状态可重写”谱系，不提供实验协议或人体应用建议。
- `gene-therapy-genome-editing-delivery-safety/`、`biological-age-clocks-biomarker-validation/`、`multiomics-personal-baseline-systems-biology/`、`engineered-cell-therapy-regenerative-platforms/`、`organoids-organ-on-chip-disease-models/` 和 `xenotransplantation-bioengineered-organ-replacement/` 负责高杠杆生物医学平台从状态观测、机制扰动、模型验证到器官替换的证据和风险边界，不提供实验协议、制造步骤、个体检测解释、治疗选择或人体应用建议。
- `causal-inference-target-trial-emulation/`、`survival-analysis-healthspan-risk-modeling/`、`human-digital-twin-life-course-simulation/`、`implementation-science-adherence-behavior-change/`、`uncertainty-quantification-model-calibration/` 和 `data-quality-missingness-representativeness/` 负责各研究域进入定量预测前的因果、风险、仿真、实施、校准和数据入口门禁，不输出个体死亡日期、临床决策、自动化评分或未经验证的寿命承诺。
- `privacy-preserving-computation-federated-learning/`、`knowledge-graph-ontology-semantic-interoperability/`、`model-cards-ai-audit-documentation/`、`technology-foresight-horizon-scanning/`、`research-portfolio-prioritization-funding-governance/` 和 `intellectual-property-technology-transfer-access/` 负责研究系统可信、可组合、可审计、可预警、可排序和可扩散的治理边界，不提供隐私攻击、临床编码服务、模型认证、投资建议、资助操控、专利法律意见或商业估值。
- `trustworthy-scientific-communication-peer-review/`、`research-participant-consent-community-engagement/`、`biobanking-biospecimen-quality-chain-of-custody/`、`longitudinal-cohort-retention-followup-infrastructure/`、`registries-real-world-data-governance/` 和 `scientific-instrumentation-sensor-calibration-maintenance/` 负责科研证据进入模型前的基础设施边界，不提供学术操控、IRB 规避、非法采样、重新识别、真实世界数据越权访问、伪造校准、设备改装、个体诊断或寿命预测。
- `nanomedicine-targeted-delivery-molecular-repair/`、`ai-drug-discovery-protein-design/`、`epigenetic-editing-gene-regulation-therapeutics/`、`brain-preservation-connectomics-emulation/`、`post-quantum-cryptography-long-term-data-security/`、`safety-critical-software-formal-methods/` 和 `long-term-digital-preservation-format-migration/` 负责远期技术连续性的证据边界，不提供自制纳米材料、双重用途生物设计、表观编辑操作、脑保存操作、密码攻击、安全关键系统规避、档案窃取或数字永生承诺。
- `cerebrovascular-stroke-brain-perfusion-resilience/`、`traumatic-brain-injury-neurotrauma-recovery/`、`delirium-acute-cognitive-failure-prevention/`、`disorders-of-consciousness-coma-recovery/`、`epilepsy-seizure-network-stability/`、`autonomic-nervous-system-homeostasis/` 和 `migraine-headache-effective-time-burden/` 负责急性神经连续性与意识韧性的证据边界，不提供个体诊断、治疗方案、急救指令、用药调整、预后判断、返工返赛许可、影像/EEG/可穿戴解释或 AI 个人医疗结论。
- `vision-eye-health-continuity/`、`hearing-auditory-communication-continuity/`、`vestibular-balance-spatial-orientation/`、`speech-language-communication-continuity/`、`swallowing-dysphagia-aspiration-nutrition/`、`smell-taste-chemosensory-continuity/` 和 `peripheral-neuropathy-somatosensory-continuity/` 负责感官、沟通与具身反馈连续性的证据边界，不提供个体诊断、治疗、设备处方、检查解释、康复训练、饮食质地调整、误吸处置、跌倒训练、驾驶/工作/活动许可或 AI 个人医疗结论。
- `space-weather-geomagnetic-storm-resilience/`、`planetary-defense-near-earth-object-risk/`、`volcanic-ashfall-geohazard-continuity/`、`earthquake-seismic-risk-built-environment-continuity/`、`tsunami-warning-coastal-evacuation-continuity/` 和 `extreme-heat-cooling-public-health-continuity/` 负责行星、地球物理与极端热风险的证据边界，不提供实时预警、地震预测、撤离路线、避难命令、太阳风暴操作建议、撞击预测、个人急救、工程设计、保险或投资建议。
- `noise-exposure-acoustic-environment-continuity/`、`light-exposure-circadian-environment-continuity/`、`lead-heavy-metal-exposure-control/`、`radon-asbestos-indoor-hazard-continuity/`、`mold-dampness-indoor-biological-exposure/` 和 `vector-borne-disease-environmental-control/` 负责慢性环境暴露与日常损耗条件的证据边界，不提供个体诊断、检测解释、设备购买、施工改造、农药操作、房产判断、旅行安全、工作许可、法律索赔或现场处置建议。
- `advance-care-planning-medical-decision-continuity/`、`supported-decision-making-guardianship-rights/`、`healthcare-personal-representative-hipaa-access-continuity/`、`financial-fiduciary-power-of-attorney-continuity/`、`representative-payee-benefits-management-continuity/` 和 `trust-estate-affairs-succession-continuity/` 负责决策权、代理权与受托连续性的证据边界，不提供医疗、法律、财务、税务、投资、福利、遗产、授权表填写、法院策略、隐私投诉、资格判断、资产分配或家庭纠纷建议。
- `credit-consumer-reporting-access-continuity/`、`tenant-screening-rental-access-continuity/`、`background-check-record-screening-continuity/`、`employment-algorithmic-hiring-screening-continuity/`、`insurance-underwriting-algorithmic-risk-scoring-continuity/` 和 `public-benefits-eligibility-automated-decision-continuity/` 负责算法化准入、筛查与资格连续性的证据边界，不提供信用修复、租房申请、背景调查规避、求职作弊、保险购买理赔、福利申请申诉、资格判断、法律、税务、投资或个案行动建议。
- `education-record-transcript-verification-continuity/`、`professional-licensure-certification-continuity/`、`skills-competency-credentialing-continuity/`、`continuing-education-recertification-continuity/`、`apprenticeship-work-based-learning-continuity/` 和 `verifiable-credential-wallet-interoperability/` 负责资格证明、证照与能力可携带连续性的证据边界，不提供升学、求职、考试、执照申请、续证、培训选择、学历认证、法律、移民、金融、KYC、证书购买、伪造、作弊或规避核验建议。
- `income-payroll-employment-record-continuity/`、`tax-administration-filing-record-continuity/`、`social-security-earnings-benefit-record-continuity/`、`retirement-pension-savings-plan-continuity/`、`unemployment-insurance-wage-record-continuity/` 和 `workers-compensation-occupational-injury-benefit-continuity/` 负责权益记录连续性的证据边界，不提供工资索赔、税务申报、福利申请、退休规划、投资、失业保险申领、工伤索赔、医疗诊断、法律、财务、移民、保险、记录伪造或个人案件建议。
- `family-medical-leave-job-protection-continuity/`、`paid-sick-family-leave-wage-replacement-continuity/`、`pregnancy-parental-work-continuity/`、`workplace-accommodation-return-to-work-continuity/`、`disability-income-work-capacity-benefit-continuity/` 和 `family-caregiver-respite-work-continuity/` 负责工作中断与照护事件连续性的证据边界，不提供个人请假、带薪假、孕产育儿、合理便利、残障福利、照护服务、医疗、法律、HR、税务、保险、福利申请、申诉或雇主合规建议。
- `vital-records-life-event-continuity/`、`name-change-identity-record-synchronization-continuity/`、`address-residency-mail-service-continuity/`、`household-composition-dependent-eligibility-continuity/`、`family-law-custody-child-support-continuity/` 和 `kinship-foster-adoption-care-continuity/` 负责家庭事实与制度记录连续性的证据边界，不提供个人证件办理、改名、地址变更、税务/福利 household 判断、监护权、子女抚养、寄养、收养、法律、移民、福利、保险、学校、法院或个案策略建议。
- `banking-deposit-account-access-continuity/`、`debt-obligation-collection-relief-continuity/`、`real-property-title-deed-record-continuity/`、`driver-license-vehicle-registration-continuity/`、`passport-travel-document-mobility-continuity/`、`contract-subscription-billing-consent-continuity/` 和 `notary-document-authentication-signature-continuity/` 负责资源控制、移动资格与交易执行连续性的证据边界，不提供个人银行、债务、破产、房产、车辆、驾驶、护照、签证、移民、订阅取消、合同审查、公证、apostille、电子签名、法律、金融或个案策略建议。
- `citizenship-nationality-statelessness-continuity/`、`immigration-status-residency-work-authorization-continuity/`、`asylum-refugee-protection-status-continuity/`、`detention-custody-confinement-status-continuity/`、`civil-commitment-involuntary-treatment-rights-continuity/`、`court-notice-service-process-default-judgment-continuity/` 和 `criminal-record-relief-collateral-consequences-continuity/` 负责法律状态、保护身份、强制程序与记录救济连续性的证据边界，不提供公民身份、国籍、移民、庇护、拘押、非自愿治疗、法院程序、犯罪记录救济、刑事、税务、医疗或法律建议。
- `school-enrollment-attendance-continuity/`、`special-education-iep-504-accommodation-continuity/`、`school-meals-nutrition-access-continuity/`、`school-health-services-chronic-condition-continuity/`、`school-transportation-safe-routes-continuity/`、`school-discipline-exclusion-restraint-continuity/`、`school-mental-health-counseling-support-continuity/` 和 `school-climate-bullying-violence-prevention-continuity/` 负责学校服务连续性的证据边界，不提供个人入学、出勤、IEP/504、校餐、校医、通学路线、纪律申诉、心理危机、欺凌投诉、教育、医疗、法律或个案建议。
- `postsecondary-admissions-transfer-articulation-continuity/`、`student-financial-aid-grant-scholarship-continuity/`、`academic-advising-degree-progress-continuity/`、`campus-basic-needs-student-support-continuity/`、`campus-disability-accommodations-accessibility-continuity/`、`campus-mental-health-crisis-student-support-continuity/`、`campus-safety-title-ix-clery-continuity/` 和 `international-student-sevis-status-continuity/` 负责高等教育学生生命周期连续性的证据边界，不提供个人申请、转学、资助、选课、住宿、残障便利、心理危机、Title IX、校园安全、SEVIS、移民、税务、医疗、法律或个案建议。
- `email-account-recovery-continuity/`、`phone-number-sim-portability-account-security-continuity/`、`mfa-passkey-credential-recovery-continuity/`、`password-manager-secret-vault-continuity/`、`cloud-backup-file-sync-data-portability-continuity/`、`messaging-contact-graph-portability-continuity/`、`domain-dns-web-presence-continuity/` 和 `platform-account-suspension-appeals-continuity/` 负责数字账户与通信可达连续性的证据边界，不提供个人账号恢复、绕过验证、短信拦截、MFA 绕过、密码破解、密钥导出、云盘取证、聊天恢复、联系人抓取、DNS 操作、平台封禁规避、申诉文案、法律或安全事件处置建议。
- `personal-computing-device-lifecycle-repair-continuity/`、`home-network-router-iot-security-continuity/`、`software-supply-chain-dependency-provenance-continuity/`、`software-update-vulnerability-patch-continuity/`、`open-source-maintainer-sustainability-continuity/`、`pki-certificate-cryptographic-trust-continuity/`、`cloud-service-exit-interoperability-continuity/` 和 `api-platform-dependency-runtime-continuity/` 负责软件、设备与信任连续性的证据边界，不提供绕过设备锁、破解加密、网络入侵、IoT 漏洞利用、供应链攻击、恶意包、漏洞利用、证书滥用、云入侵、API 限制规避、计费规避、账号规避或安全事件处置建议。
- `regenerative-medicine/`、`cancer-control/` 和 `immune-maintenance/` 负责身体基底维护相关的机制、风险和证据边界。
- `rehabilitation-functioning/`、`assistive-technology-access/`、`skin-barrier-wound-healing/` 和 `sensory-continuity/` 负责功能恢复、能力补偿、外界屏障和感官反馈连续性。
- `antimicrobial-resilience/` 负责抗微生物耐药、感染控制和现代医学抗感染底座。
- `neuro-continuity/`、`memory-editing/`、`cognitive-augmentation/`、`ai-agency-safety/`、`digital-identity-security/` 和 `disembodied-cns/` 负责神经、身份、认知、AI 代理、数字入口和去具身连续性相关边界。
- `mental-health-affective-stability/`、`sleep-circadian-recovery/` 和 `pain-suffering-control/` 负责心理稳定、恢复调度和持续存在的可承受性。
- `social-connection-relational-infra/` 负责社会连接、孤独、照护网络、信任和社区关系。
- `substance-exposure-control/` 负责烟草、酒精、成瘾性物质、有害暴露和主体自主性风险。
- `health-literacy-navigation/` 和 `language-access-plain-communication/` 负责健康素养、服务导航、清晰语言、语言服务、可理解信息、风险沟通和共同决策。
- `oral-health-continuity/` 负责口腔健康、咀嚼、疼痛、感染、营养和沟通连续性。
- `future-waiting/` 和 `biostasis-cryopreservation/` 负责等待未来的时间成本和损耗成本路径。
- `risk-engineering/`、`planetary-health-environment/`、`resource-social-infra/`、`supply-chain-continuity/`、`synthetic-biology-biosecurity/`、`space-extreme-habitation/` 和 `governance-rights/` 负责外部风险、环境底座、资源底座、关键供应链、生物安全、极端栖居和主体权利保护。
- `measurement-feedback/` 负责所有研究域进入定量模型前的测量、预测和反馈接口。
- 子域之间共享 Human Infra 的伦理和证据原则，但不能共享模糊数据目录或脚本目录。

## 维护规则

- 新子域必须先在 `docs/reference/domain-map.md` 中说明存在理由、边界和非目标。
- 子域内新增文件或目录时，同步更新该子域 `AGENTS.md`。
- 跨子域概念进入 `docs/`；子域专属材料留在对应子域。
- 不为了“未来可能需要”创建空数据、空脚本或空框架目录。
