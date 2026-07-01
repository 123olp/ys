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
├── long-distance-travel-booking-itinerary-continuity/
│   ├── AGENTS.md
│   └── README.md
├── air-passenger-rights-disruption-refund-continuity/
│   ├── AGENTS.md
│   └── README.md
├── aviation-security-screening-identity-continuity/
│   ├── AGENTS.md
│   └── README.md
├── baggage-personal-property-travel-continuity/
│   ├── AGENTS.md
│   └── README.md
├── lodging-temporary-accommodation-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── travel-advisory-consular-assistance-continuity/
│   ├── AGENTS.md
│   └── README.md
├── travel-health-preparedness-continuity/
│   ├── AGENTS.md
│   └── README.md
├── customs-border-entry-declaration-continuity/
│   ├── AGENTS.md
│   └── README.md
├── online-retail-order-shipping-fulfillment-continuity/
│   ├── AGENTS.md
│   └── README.md
├── consumer-return-refund-dispute-resolution-continuity/
│   ├── AGENTS.md
│   └── README.md
├── consumer-warranty-service-contract-repair-continuity/
│   ├── AGENTS.md
│   └── README.md
├── right-to-repair-parts-manuals-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── payment-card-dispute-unauthorized-charge-continuity/
│   ├── AGENTS.md
│   └── README.md
├── gift-card-prepaid-stored-value-continuity/
│   ├── AGENTS.md
│   └── README.md
├── price-fee-disclosure-junk-fee-continuity/
│   ├── AGENTS.md
│   └── README.md
├── consumer-reviews-endorsements-marketplace-trust-continuity/
│   ├── AGENTS.md
│   └── README.md
├── credit-card-revolving-credit-cost-continuity/
│   ├── AGENTS.md
│   └── README.md
├── consumer-loan-origination-apr-disclosure-continuity/
│   ├── AGENTS.md
│   └── README.md
├── mortgage-origination-servicing-foreclosure-continuity/
│   ├── AGENTS.md
│   └── README.md
├── auto-loan-lease-servicing-repossession-continuity/
│   ├── AGENTS.md
│   └── README.md
├── student-loan-servicing-repayment-forgiveness-continuity/
│   ├── AGENTS.md
│   └── README.md
├── payday-small-dollar-title-loan-continuity/
│   ├── AGENTS.md
│   └── README.md
├── buy-now-pay-later-installment-financing-continuity/
│   ├── AGENTS.md
│   └── README.md
├── remittance-money-transfer-disclosure-continuity/
│   ├── AGENTS.md
│   └── README.md
├── auto-insurance-liability-collision-claims-continuity/
│   ├── AGENTS.md
│   └── README.md
├── homeowners-renters-property-insurance-claims-continuity/
│   ├── AGENTS.md
│   └── README.md
├── flood-insurance-nfip-claims-continuity/
│   ├── AGENTS.md
│   └── README.md
├── catastrophe-wind-wildfire-earthquake-insurance-continuity/
│   ├── AGENTS.md
│   └── README.md
├── disability-income-insurance-claim-continuity/
│   ├── AGENTS.md
│   └── README.md
├── long-term-care-insurance-benefit-activation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── travel-insurance-trip-protection-claims-continuity/
│   ├── AGENTS.md
│   └── README.md
├── personal-liability-umbrella-insurance-defense-continuity/
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
├── calendar-scheduling-appointment-continuity/
│   ├── AGENTS.md
│   └── README.md
├── notification-alert-routing-attention-continuity/
│   ├── AGENTS.md
│   └── README.md
├── reminder-alarm-routine-task-continuity/
│   ├── AGENTS.md
│   └── README.md
├── meeting-video-conferencing-remote-collaboration-continuity/
│   ├── AGENTS.md
│   └── README.md
├── document-capture-ocr-pdf-record-workflow-continuity/
│   ├── AGENTS.md
│   └── README.md
├── search-index-discovery-retrieval-continuity/
│   ├── AGENTS.md
│   └── README.md
├── personal-automation-integration-workflow-continuity/
│   ├── AGENTS.md
│   └── README.md
├── collaborative-document-permission-version-continuity/
│   ├── AGENTS.md
│   └── README.md
├── personal-vehicle-maintenance-recall-repair-continuity/
│   ├── AGENTS.md
│   └── README.md
├── fuel-ev-charging-refueling-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── parking-curb-access-towing-impound-continuity/
│   ├── AGENTS.md
│   └── README.md
├── walking-bicycling-micromobility-continuity/
│   ├── AGENTS.md
│   └── README.md
├── paratransit-nemt-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── taxi-rideshare-demand-response-mobility-continuity/
│   ├── AGENTS.md
│   └── README.md
├── transit-fare-payment-toll-account-continuity/
│   ├── AGENTS.md
│   └── README.md
├── multimodal-trip-planning-real-time-wayfinding-continuity/
│   ├── AGENTS.md
│   └── README.md
├── public-restroom-sanitation-hygiene-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── public-drinking-water-hydration-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── public-seating-shade-rest-cooling-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── community-resilience-hub-shelter-center-continuity/
│   ├── AGENTS.md
│   └── README.md
├── public-library-community-anchor-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── parks-recreation-green-space-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── public-wifi-device-charging-connectivity-continuity/
│   ├── AGENTS.md
│   └── README.md
├── public-accommodation-accessibility-service-continuity/
│   ├── AGENTS.md
│   └── README.md
├── grocery-retail-food-store-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── snap-ebt-redemption-retailer-payment-continuity/
│   ├── AGENTS.md
│   └── README.md
├── wic-benefit-redemption-infant-maternal-nutrition-continuity/
│   ├── AGENTS.md
│   └── README.md
├── food-bank-pantry-community-food-distribution-continuity/
│   ├── AGENTS.md
│   └── README.md
├── emergency-food-disaster-feeding-continuity/
│   ├── AGENTS.md
│   └── README.md
├── home-delivered-meals-congregate-nutrition-services-continuity/
│   ├── AGENTS.md
│   └── README.md
├── infant-formula-baby-food-supply-safety-continuity/
│   ├── AGENTS.md
│   └── README.md
├── prepared-food-restaurant-cafeteria-safety-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── retail-pharmacy-prescription-dispensing-continuity/
│   ├── AGENTS.md
│   └── README.md
├── pharmacy-benefit-formulary-prior-authorization-continuity/
│   ├── AGENTS.md
│   └── README.md
├── medication-reconciliation-regimen-adherence-continuity/
│   ├── AGENTS.md
│   └── README.md
├── patient-medication-labeling-counseling-continuity/
│   ├── AGENTS.md
│   └── README.md
├── unused-medicine-takeback-disposal-continuity/
│   ├── AGENTS.md
│   └── README.md
├── durable-medical-equipment-supplier-repair-continuity/
│   ├── AGENTS.md
│   └── README.md
├── home-oxygen-respiratory-equipment-supply-continuity/
│   ├── AGENTS.md
│   └── README.md
├── diabetes-insulin-glucose-monitoring-supplies-continuity/
│   ├── AGENTS.md
│   └── README.md
├── provider-directory-network-adequacy-continuity/
│   ├── AGENTS.md
│   └── README.md
├── primary-care-panel-appointment-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── specialist-referral-authorization-navigation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── appointment-availability-wait-time-continuity/
│   ├── AGENTS.md
│   └── README.md
├── outpatient-laboratory-specimen-result-routing-continuity/
│   ├── AGENTS.md
│   └── README.md
├── diagnostic-imaging-order-scheduling-report-continuity/
│   ├── AGENTS.md
│   └── README.md
├── ambulatory-procedure-surgery-center-continuity/
│   ├── AGENTS.md
│   └── README.md
├── after-hours-urgent-care-triage-continuity/
│   ├── AGENTS.md
│   └── README.md
├── health-insurance-enrollment-renewal-continuity/
│   ├── AGENTS.md
│   └── README.md
├── insurance-eligibility-benefits-verification-continuity/
│   ├── AGENTS.md
│   └── README.md
├── medical-service-prior-authorization-utilization-management-continuity/
│   ├── AGENTS.md
│   └── README.md
├── claims-adjudication-eob-denial-continuity/
│   ├── AGENTS.md
│   └── README.md
├── patient-billing-payment-plan-continuity/
│   ├── AGENTS.md
│   └── README.md
├── price-transparency-good-faith-estimate-continuity/
│   ├── AGENTS.md
│   └── README.md
├── surprise-billing-balance-bill-protection-continuity/
│   ├── AGENTS.md
│   └── README.md
├── charity-care-financial-assistance-medical-debt-continuity/
│   ├── AGENTS.md
│   └── README.md
├── patient-portal-account-message-continuity/
│   ├── AGENTS.md
│   └── README.md
├── medical-record-access-amendment-release-continuity/
│   ├── AGENTS.md
│   └── README.md
├── clinical-results-notification-followup-continuity/
│   ├── AGENTS.md
│   └── README.md
├── informed-consent-refusal-shared-decision-continuity/
│   ├── AGENTS.md
│   └── README.md
├── healthcare-language-interpreter-effective-communication-continuity/
│   ├── AGENTS.md
│   └── README.md
├── healthcare-disability-accommodation-accessibility-continuity/
│   ├── AGENTS.md
│   └── README.md
├── patient-grievance-complaint-ombuds-continuity/
│   ├── AGENTS.md
│   └── README.md
├── healthcare-civil-rights-nondiscrimination-continuity/
│   ├── AGENTS.md
│   └── README.md
├── emergency-contact-next-of-kin-notification-continuity/
│   ├── AGENTS.md
│   └── README.md
├── personal-health-record-emergency-summary-continuity/
│   ├── AGENTS.md
│   └── README.md
├── medical-id-allergy-critical-alert-continuity/
│   ├── AGENTS.md
│   └── README.md
├── medication-list-implant-device-emergency-continuity/
│   ├── AGENTS.md
│   └── README.md
├── chronic-condition-emergency-action-plan-continuity/
│   ├── AGENTS.md
│   └── README.md
├── immunization-record-proof-continuity/
│   ├── AGENTS.md
│   └── README.md
├── organ-donor-registry-anatomical-gift-continuity/
│   ├── AGENTS.md
│   └── README.md
├── access-functional-needs-emergency-registry-continuity/
│   ├── AGENTS.md
│   └── README.md
├── death-certificate-registration-cause-of-death-record-continuity/
│   ├── AGENTS.md
│   └── README.md
├── funeral-cremation-burial-disposition-continuity/
│   ├── AGENTS.md
│   └── README.md
├── cemetery-memorial-remains-location-continuity/
│   ├── AGENTS.md
│   └── README.md
├── bereavement-leave-grief-support-continuity/
│   ├── AGENTS.md
│   └── README.md
├── survivor-benefits-death-notification-continuity/
│   ├── AGENTS.md
│   └── README.md
├── life-insurance-beneficiary-claim-continuity/
│   ├── AGENTS.md
│   └── README.md
├── estate-inventory-asset-liability-handoff-continuity/
│   ├── AGENTS.md
│   └── README.md
├── post-death-account-closure-service-cancellation-continuity/
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
├── rental-lease-tenancy-rights-continuity/
│   ├── AGENTS.md
│   └── README.md
├── eviction-prevention-court-diversion-continuity/
│   ├── AGENTS.md
│   └── README.md
├── emergency-rental-assistance-arrears-continuity/
│   ├── AGENTS.md
│   └── README.md
├── housing-choice-voucher-public-housing-continuity/
│   ├── AGENTS.md
│   └── README.md
├── fair-housing-discrimination-reasonable-accommodation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── housing-habitability-inspection-code-enforcement-continuity/
│   ├── AGENTS.md
│   └── README.md
├── hud-approved-housing-counseling-navigation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── manufactured-housing-park-tenure-safety-continuity/
│   ├── AGENTS.md
│   └── README.md
├── self-represented-litigant-court-self-help-continuity/
│   ├── AGENTS.md
│   └── README.md
├── court-efiling-document-submission-continuity/
│   ├── AGENTS.md
│   └── README.md
├── remote-hybrid-court-hearing-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── court-language-access-interpreter-continuity/
│   ├── AGENTS.md
│   └── README.md
├── court-disability-accommodation-accessibility-continuity/
│   ├── AGENTS.md
│   └── README.md
├── court-fees-fines-ability-to-pay-continuity/
│   ├── AGENTS.md
│   └── README.md
├── jury-service-summons-hardship-continuity/
│   ├── AGENTS.md
│   └── README.md
├── small-claims-civil-dispute-resolution-continuity/
│   ├── AGENTS.md
│   └── README.md
├── data-broker-registry-opt-out-deletion-continuity/
│   ├── AGENTS.md
│   └── README.md
├── privacy-rights-access-correction-deletion-continuity/
│   ├── AGENTS.md
│   └── README.md
├── opt-out-preference-signal-consent-revocation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── commercial-surveillance-adtech-profile-continuity/
│   ├── AGENTS.md
│   └── README.md
├── sensitive-location-data-exposure-continuity/
│   ├── AGENTS.md
│   └── README.md
├── biometric-identifier-template-governance-continuity/
│   ├── AGENTS.md
│   └── README.md
├── children-teen-data-privacy-consent-continuity/
│   ├── AGENTS.md
│   └── README.md
├── data-breach-notification-identity-recovery-continuity/
│   ├── AGENTS.md
│   └── README.md
├── content-provenance-authenticity-credential-continuity/
│   ├── AGENTS.md
│   └── README.md
├── synthetic-media-watermarking-disclosure-continuity/
│   ├── AGENTS.md
│   └── README.md
├── ai-impersonation-deepfake-fraud-continuity/
│   ├── AGENTS.md
│   └── README.md
├── voice-call-caller-id-authentication-continuity/
│   ├── AGENTS.md
│   └── README.md
├── email-domain-authentication-spoofing-continuity/
│   ├── AGENTS.md
│   └── README.md
├── official-web-domain-brand-impersonation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── digital-evidence-preservation-chain-of-custody-continuity/
│   ├── AGENTS.md
│   └── README.md
├── platform-content-moderation-notice-appeal-continuity/
│   ├── AGENTS.md
│   └── README.md
├── copyright-authorship-registration-licensing-continuity/
│   ├── AGENTS.md
│   └── README.md
├── dmca-notice-counter-notice-platform-removal-continuity/
│   ├── AGENTS.md
│   └── README.md
├── creative-commons-open-content-license-continuity/
│   ├── AGENTS.md
│   └── README.md
├── open-source-software-license-compliance-continuity/
│   ├── AGENTS.md
│   └── README.md
├── trademark-brand-identity-rights-continuity/
│   ├── AGENTS.md
│   └── README.md
├── patent-invention-disclosure-maintenance-continuity/
│   ├── AGENTS.md
│   └── README.md
├── creator-royalty-rights-metadata-continuity/
│   ├── AGENTS.md
│   └── README.md
├── ai-training-data-rights-opt-out-provenance-continuity/
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
├── scholarly-identity-orcid-affiliation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── persistent-identifier-doi-citation-metadata-continuity/
│   ├── AGENTS.md
│   └── README.md
├── research-data-repository-fair-sharing-continuity/
│   ├── AGENTS.md
│   └── README.md
├── research-software-capsule-reproducibility-continuity/
│   ├── AGENTS.md
│   └── README.md
├── preregistration-registered-report-study-plan-continuity/
│   ├── AGENTS.md
│   └── README.md
├── lab-notebook-protocol-versioning-continuity/
│   ├── AGENTS.md
│   └── README.md
├── contributor-role-authorship-attribution-continuity/
│   ├── AGENTS.md
│   └── README.md
├── conflict-of-interest-funding-disclosure-continuity/
│   ├── AGENTS.md
│   └── README.md
├── research-artifact-archive-retention-preservation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── systematic-review-protocol-search-screening-continuity/
│   ├── AGENTS.md
│   └── README.md
├── risk-of-bias-critical-appraisal-continuity/
│   ├── AGENTS.md
│   └── README.md
├── meta-analysis-effect-size-heterogeneity-continuity/
│   ├── AGENTS.md
│   └── README.md
├── publication-reporting-bias-detection-continuity/
│   ├── AGENTS.md
│   └── README.md
├── evidence-certainty-grade-summary-findings-continuity/
│   ├── AGENTS.md
│   └── README.md
├── evidence-to-decision-guideline-panel-continuity/
│   ├── AGENTS.md
│   └── README.md
├── guideline-appraisal-adaptation-localization-continuity/
│   ├── AGENTS.md
│   └── README.md
├── living-evidence-surveillance-update-continuity/
│   ├── AGENTS.md
│   └── README.md
├── rapid-review-emergency-evidence-triage-continuity/
│   ├── AGENTS.md
│   └── README.md
├── research-misconduct-investigation-correction-continuity/
│   ├── AGENTS.md
│   └── README.md
├── retraction-expression-concern-correction-continuity/
│   ├── AGENTS.md
│   └── README.md
├── preprint-versioning-public-review-continuity/
│   ├── AGENTS.md
│   └── README.md
├── journal-editorial-policy-peer-review-integrity-continuity/
│   ├── AGENTS.md
│   └── README.md
├── predatory-publishing-paper-mill-detection-continuity/
│   ├── AGENTS.md
│   └── README.md
├── citation-network-claim-propagation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── research-metrics-incentives-assessment-continuity/
│   ├── AGENTS.md
│   └── README.md
├── replication-reproducibility-many-labs-continuity/
│   ├── AGENTS.md
│   └── README.md
├── science-communication-evidence-translation-continuity/
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
├── semiconductor-manufacturing-metrology-continuity/
│   ├── AGENTS.md
│   └── README.md
├── semiconductor-advanced-packaging-continuity/
│   ├── AGENTS.md
│   └── README.md
├── chip-design-eda-verification-ip-continuity/
│   ├── AGENTS.md
│   └── README.md
├── ai-hardware-accelerator-performance-continuity/
│   ├── AGENTS.md
│   └── README.md
├── data-center-cooling-water-thermal-continuity/
│   ├── AGENTS.md
│   └── README.md
├── large-load-grid-interconnection-transmission-continuity/
│   ├── AGENTS.md
│   └── README.md
├── grid-scale-energy-storage-flexibility-continuity/
│   ├── AGENTS.md
│   └── README.md
├── advanced-nuclear-energy-safety-generation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── undersea-cable-internet-backbone-continuity/
│   ├── AGENTS.md
│   └── README.md
├── satellite-communications-spectrum-orbit-continuity/
│   ├── AGENTS.md
│   └── README.md
├── cardiac-arrest-cpr-defibrillation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── sepsis-shock-early-recognition-resuscitation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── trauma-system-hemorrhage-control-continuity/
│   ├── AGENTS.md
│   └── README.md
├── intensive-care-organ-support-delirium-continuity/
│   ├── AGENTS.md
│   └── README.md
├── mechanical-ventilation-respiratory-failure-continuity/
│   ├── AGENTS.md
│   └── README.md
├── ecmo-extracorporeal-life-support-continuity/
│   ├── AGENTS.md
│   └── README.md
├── acute-kidney-injury-renal-replacement-continuity/
│   ├── AGENTS.md
│   └── README.md
├── transfusion-blood-management-hemorrhage-continuity/
│   ├── AGENTS.md
│   └── README.md
├── overdose-poisoning-reversal-toxicology-continuity/
│   ├── AGENTS.md
│   └── README.md
├── burn-injury-critical-care-rehabilitation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── acute-coronary-syndrome-reperfusion-continuity/
│   ├── AGENTS.md
│   └── README.md
├── acute-heart-failure-decompensation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── cardiac-arrhythmia-syncope-decompensation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── venous-thromboembolism-pulmonary-embolism-continuity/
│   ├── AGENTS.md
│   └── README.md
├── hypertensive-crisis-end-organ-risk-continuity/
│   ├── AGENTS.md
│   └── README.md
├── diabetic-hyperglycemic-hypoglycemic-crisis-continuity/
│   ├── AGENTS.md
│   └── README.md
├── anaphylaxis-allergic-emergency-continuity/
│   ├── AGENTS.md
│   └── README.md
├── asthma-copd-exacerbation-airway-continuity/
│   ├── AGENTS.md
│   └── README.md
├── acute-gastrointestinal-bleeding-endoscopy-continuity/
│   ├── AGENTS.md
│   └── README.md
├── obstetric-emergency-hemorrhage-hypertension-continuity/
│   ├── AGENTS.md
│   └── README.md
├── hypertension-detection-control-continuity/
│   ├── AGENTS.md
│   └── README.md
├── lipid-atherosclerosis-risk-management-continuity/
│   ├── AGENTS.md
│   └── README.md
├── prediabetes-diabetes-prevention-continuity/
│   ├── AGENTS.md
│   └── README.md
├── obesity-adiposity-metabolic-risk-continuity/
│   ├── AGENTS.md
│   └── README.md
├── tobacco-nicotine-cessation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── alcohol-use-risk-reduction-continuity/
│   ├── AGENTS.md
│   └── README.md
├── chronic-kidney-disease-screening-progression-continuity/
│   ├── AGENTS.md
│   └── README.md
├── cancer-screening-early-detection-continuity/
│   ├── AGENTS.md
│   └── README.md
├── osteoporosis-fracture-prevention-bone-health-continuity/
│   ├── AGENTS.md
│   └── README.md
├── fall-risk-prevention-home-safety-continuity/
│   ├── AGENTS.md
│   └── README.md
├── sleep-disordered-breathing-screening-treatment-continuity/
│   ├── AGENTS.md
│   └── README.md
├── chronic-insomnia-cbti-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── sexual-health-sti-prevention-continuity/
│   ├── AGENTS.md
│   └── README.md
├── hiv-testing-prep-prevention-continuity/
│   ├── AGENTS.md
│   └── README.md
├── chronic-viral-hepatitis-screening-liver-protection-continuity/
│   ├── AGENTS.md
│   └── README.md
├── contraception-family-planning-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── menstrual-health-cycle-literacy-continuity/
│   ├── AGENTS.md
│   └── README.md
├── perimenopause-menopause-midlife-health-continuity/
│   ├── AGENTS.md
│   └── README.md
├── pelvic-floor-continence-function-continuity/
│   ├── AGENTS.md
│   └── README.md
├── skin-cancer-uv-protection-early-detection-continuity/
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
├── human-animal-bond-companion-care-continuity/
│   ├── AGENTS.md
│   └── README.md
├── veterinary-care-access-cost-continuity/
│   ├── AGENTS.md
│   └── README.md
├── service-animal-disability-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── pet-identification-microchip-reunification-continuity/
│   ├── AGENTS.md
│   └── README.md
├── pet-food-medication-supply-safety-continuity/
│   ├── AGENTS.md
│   └── README.md
├── pet-disaster-evacuation-sheltering-continuity/
│   ├── AGENTS.md
│   └── README.md
├── animal-shelter-rescue-rehoming-continuity/
│   ├── AGENTS.md
│   └── README.md
├── animal-welfare-cruelty-reporting-continuity/
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
├── domestic-violence-coercive-control-safety-continuity/
│   ├── AGENTS.md
│   └── README.md
├── sexual-assault-forensic-exam-advocacy-continuity/
│   ├── AGENTS.md
│   └── README.md
├── stalking-harassment-protection-order-continuity/
│   ├── AGENTS.md
│   └── README.md
├── victim-witness-rights-notification-continuity/
│   ├── AGENTS.md
│   └── README.md
├── crime-victim-compensation-restitution-continuity/
│   ├── AGENTS.md
│   └── README.md
├── survivor-safe-housing-emergency-transfer-continuity/
│   ├── AGENTS.md
│   └── README.md
├── human-trafficking-victim-identification-services-continuity/
│   ├── AGENTS.md
│   └── README.md
├── missing-persons-unidentified-remains-resolution-continuity/
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
├── depression-mood-disorder-functioning-continuity/
│   ├── AGENTS.md
│   └── README.md
├── anxiety-stress-threat-regulation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── trauma-ptsd-adversity-recovery-continuity/
│   ├── AGENTS.md
│   └── README.md
├── psychosis-reality-testing-community-continuity/
│   ├── AGENTS.md
│   └── README.md
├── bipolar-mood-episode-stability-continuity/
│   ├── AGENTS.md
│   └── README.md
├── adhd-executive-function-neurodevelopment-continuity/
│   ├── AGENTS.md
│   └── README.md
├── autism-neurodiversity-support-continuity/
│   ├── AGENTS.md
│   └── README.md
├── eating-disorders-nutrition-body-continuity/
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
├── loneliness-social-isolation-risk-continuity/
│   ├── AGENTS.md
│   └── README.md
├── social-prescribing-community-referral-continuity/
│   ├── AGENTS.md
│   └── README.md
├── mutual-aid-neighbor-support-network-continuity/
│   ├── AGENTS.md
│   └── README.md
├── volunteering-civic-service-participation-continuity/
│   ├── AGENTS.md
│   └── README.md
├── community-mediation-neighbor-conflict-resolution-continuity/
│   ├── AGENTS.md
│   └── README.md
├── restorative-justice-repair-accountability-continuity/
│   ├── AGENTS.md
│   └── README.md
├── reputation-defamation-public-trust-repair-continuity/
│   ├── AGENTS.md
│   └── README.md
├── references-vouching-recommendation-social-capital-continuity/
│   ├── AGENTS.md
│   └── README.md
├── third-place-belonging-social-participation-continuity/
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
- `semiconductor-manufacturing-metrology-continuity/`、`semiconductor-advanced-packaging-continuity/`、`chip-design-eda-verification-ip-continuity/`、`ai-hardware-accelerator-performance-continuity/`、`data-center-cooling-water-thermal-continuity/`、`large-load-grid-interconnection-transmission-continuity/`、`grid-scale-energy-storage-flexibility-continuity/`、`advanced-nuclear-energy-safety-generation-continuity/`、`undersea-cable-internet-backbone-continuity/` 和 `satellite-communications-spectrum-orbit-continuity/` 负责把先进计算、能源与连接底座拆成芯片制造计量、封装、设计验证、加速器执行、电力与冷却、储能与稳定能源、全球骨干和空间通信这些可独立审查的物理约束。
- `cardiac-arrest-cpr-defibrillation-continuity/`、`sepsis-shock-early-recognition-resuscitation-continuity/`、`trauma-system-hemorrhage-control-continuity/`、`intensive-care-organ-support-delirium-continuity/`、`mechanical-ventilation-respiratory-failure-continuity/`、`ecmo-extracorporeal-life-support-continuity/`、`acute-kidney-injury-renal-replacement-continuity/`、`transfusion-blood-management-hemorrhage-continuity/`、`overdose-poisoning-reversal-toxicology-continuity/` 和 `burn-injury-critical-care-rehabilitation-continuity/` 负责把急性死亡边界拆成心脏骤停、脓毒症休克、创伤出血、ICU、呼吸机、ECMO、AKI/RRT、输血、中毒逆转和烧伤重建这些可独立审查的救援链。
- `acute-coronary-syndrome-reperfusion-continuity/`、`acute-heart-failure-decompensation-continuity/`、`cardiac-arrhythmia-syncope-decompensation-continuity/`、`venous-thromboembolism-pulmonary-embolism-continuity/`、`hypertensive-crisis-end-organ-risk-continuity/`、`diabetic-hyperglycemic-hypoglycemic-crisis-continuity/`、`anaphylaxis-allergic-emergency-continuity/`、`asthma-copd-exacerbation-airway-continuity/`、`acute-gastrointestinal-bleeding-endoscopy-continuity/` 和 `obstetric-emergency-hemorrhage-hypertension-continuity/` 负责把急性内科与时间关键急症拆成急性冠脉再灌注、心衰失代偿、节律/晕厥、VTE/PE、高血压靶器官风险、糖尿病危象、过敏性休克、气道急性加重、GI 出血和产科急症这些进入骤停、ICU 或不可逆损伤之前的可逆窗口。
- `hypertension-detection-control-continuity/`、`lipid-atherosclerosis-risk-management-continuity/`、`prediabetes-diabetes-prevention-continuity/`、`obesity-adiposity-metabolic-risk-continuity/`、`tobacco-nicotine-cessation-continuity/`、`alcohol-use-risk-reduction-continuity/`、`chronic-kidney-disease-screening-progression-continuity/`、`cancer-screening-early-detection-continuity/`、`osteoporosis-fracture-prevention-bone-health-continuity/` 和 `fall-risk-prevention-home-safety-continuity/` 负责把急症和失能之前的上游预防执行层拆成高血压检测控制、血脂/ASCVD、糖尿病前期、肥胖代谢风险、烟草、酒精、CKD、癌筛、骨健康和跌倒预防这些可独立审查的风险因子连续性条件。
- `sleep-disordered-breathing-screening-treatment-continuity/`、`chronic-insomnia-cbti-access-continuity/`、`sexual-health-sti-prevention-continuity/`、`hiv-testing-prep-prevention-continuity/`、`chronic-viral-hepatitis-screening-liver-protection-continuity/`、`contraception-family-planning-access-continuity/`、`menstrual-health-cycle-literacy-continuity/`、`perimenopause-menopause-midlife-health-continuity/`、`pelvic-floor-continence-function-continuity/` 和 `skin-cancer-uv-protection-early-detection-continuity/` 负责把生活史预防与功能连续性拆成睡眠呼吸障碍、慢性失眠、性健康/STI、HIV、病毒性肝炎、避孕家庭计划、月经健康、更年期、盆底控尿控便和 UV/皮肤癌预防这些可独立审查的恢复、身体自主、感染风险和功能参与条件。
- `scholarly-identity-orcid-affiliation-continuity/`、`persistent-identifier-doi-citation-metadata-continuity/`、`research-data-repository-fair-sharing-continuity/`、`research-software-capsule-reproducibility-continuity/`、`preregistration-registered-report-study-plan-continuity/`、`lab-notebook-protocol-versioning-continuity/`、`contributor-role-authorship-attribution-continuity/`、`conflict-of-interest-funding-disclosure-continuity/` 和 `research-artifact-archive-retention-preservation-continuity/` 负责科研身份、持久标识与可复现研究基础设施，覆盖 ORCID/ROR、DOI 元数据、FAIR 数据仓库、研究软件胶囊、预注册、协议版本、贡献者角色、利益冲突披露和研究产物保存。
- `systematic-review-protocol-search-screening-continuity/`、`risk-of-bias-critical-appraisal-continuity/`、`meta-analysis-effect-size-heterogeneity-continuity/`、`publication-reporting-bias-detection-continuity/`、`evidence-certainty-grade-summary-findings-continuity/`、`evidence-to-decision-guideline-panel-continuity/`、`guideline-appraisal-adaptation-localization-continuity/`、`living-evidence-surveillance-update-continuity/` 和 `rapid-review-emergency-evidence-triage-continuity/` 负责证据综合与指南转化连续性，覆盖系统综述协议、风险偏倚、Meta 分析、报告偏倚、GRADE 确定性、证据到决策、指南适配、活证据更新和快速综述。
- `research-misconduct-investigation-correction-continuity/`、`retraction-expression-concern-correction-continuity/`、`preprint-versioning-public-review-continuity/`、`journal-editorial-policy-peer-review-integrity-continuity/`、`predatory-publishing-paper-mill-detection-continuity/`、`citation-network-claim-propagation-continuity/`、`research-metrics-incentives-assessment-continuity/`、`replication-reproducibility-many-labs-continuity/` 和 `science-communication-evidence-translation-continuity/` 负责科研纠错、出版完整性与科学传播连续性，覆盖不端调查、撤稿更正、预印本版本、同行评审制度、paper mill 筛查、引用传播、指标激励、复制复现和公众证据转译。
- `healthcare-access-continuity/`、`medicine-access-treatment-continuity/`、`patient-data-interoperability/`、`telehealth-remote-monitoring-access/`、`health-data-privacy-governance/`、`functioning-quality-of-life-outcomes/`、`health-economics-value-assessment/`、`clinical-trials-regulatory-science-translation/`、`immunization-public-health-surveillance/`、`animal-health-zoonotic-interface-one-health/`、`maternal-newborn-child-development/`、`patient-safety-organizational-learning/`、`health-workforce-capacity/`、`community-health-workers-peer-support/`、`caregiving-long-term-care/`、`housing-built-environment-stability/`、`building-fire-life-safety-codes/`、`transportation-access-mobility/`、`legal-identity-civil-registration/`、`emergency-preparedness-response/`、`weather-climate-observation-forecasting/`、`emergency-alerts-communications/`、`household-emergency-preparedness-resilience/` 和 `disaster-recovery-relief-continuity/` 负责医疗接入、药品治疗连续性、患者数据互操作、远程照护、健康数据治理、结局评估、价值评估、临床监管转化、公共卫生监测、动物健康界面、早期生命发展、患者安全、健康劳动力、社区中介支持、长期照护、居住空间、建筑消防生命安全、交通可达、法律身份、应急响应、天气气候观测、预警通信、家庭准备和灾后恢复这些服务接入与生活连续性条件。
- `rental-lease-tenancy-rights-continuity/`、`eviction-prevention-court-diversion-continuity/`、`emergency-rental-assistance-arrears-continuity/`、`housing-choice-voucher-public-housing-continuity/`、`fair-housing-discrimination-reasonable-accommodation-continuity/`、`housing-habitability-inspection-code-enforcement-continuity/`、`hud-approved-housing-counseling-navigation-continuity/` 和 `manufactured-housing-park-tenure-safety-continuity/` 负责住房 tenure 稳定与可居住性执行连续性，覆盖租赁居住权、驱逐预防、欠租援助、住房补贴、公平住房、可居住性检查、住房咨询和制造房屋园区稳定。
- `self-represented-litigant-court-self-help-continuity/`、`court-efiling-document-submission-continuity/`、`remote-hybrid-court-hearing-access-continuity/`、`court-language-access-interpreter-continuity/`、`court-disability-accommodation-accessibility-continuity/`、`court-fees-fines-ability-to-pay-continuity/`、`jury-service-summons-hardship-continuity/` 和 `small-claims-civil-dispute-resolution-continuity/` 负责法院接入与民事程序执行连续性，覆盖自助中心、电子提交、远程 hearing、语言口译、残障便利、费用罚金、陪审义务和小额纠纷恢复。
- `data-broker-registry-opt-out-deletion-continuity/`、`privacy-rights-access-correction-deletion-continuity/`、`opt-out-preference-signal-consent-revocation-continuity/`、`commercial-surveillance-adtech-profile-continuity/`、`sensitive-location-data-exposure-continuity/`、`biometric-identifier-template-governance-continuity/`、`children-teen-data-privacy-consent-continuity/` 和 `data-breach-notification-identity-recovery-continuity/` 负责个人数据权利、隐私暴露与数据经纪连续性，覆盖数据经纪、访问更正删除、同意撤回、商业监控、位置数据、生物特征、未成年数据和泄露恢复。
- `content-provenance-authenticity-credential-continuity/`、`synthetic-media-watermarking-disclosure-continuity/`、`ai-impersonation-deepfake-fraud-continuity/`、`voice-call-caller-id-authentication-continuity/`、`email-domain-authentication-spoofing-continuity/`、`official-web-domain-brand-impersonation-continuity/`、`digital-evidence-preservation-chain-of-custody-continuity/` 和 `platform-content-moderation-notice-appeal-continuity/` 负责数字内容可信、合成媒体与冒充风险连续性，覆盖内容来源凭据、合成媒体披露、AI 冒充、电话认证、邮件认证、官网品牌冒充、数字证据保存和平台审核通知申诉。
- `copyright-authorship-registration-licensing-continuity/`、`dmca-notice-counter-notice-platform-removal-continuity/`、`creative-commons-open-content-license-continuity/`、`open-source-software-license-compliance-continuity/`、`trademark-brand-identity-rights-continuity/`、`patent-invention-disclosure-maintenance-continuity/`、`creator-royalty-rights-metadata-continuity/` 和 `ai-training-data-rights-opt-out-provenance-continuity/` 负责知识产权、数字作品与 AI 训练数据权利连续性，覆盖版权作者身份登记许可、DMCA 通知反通知、开放内容许可、开源软件许可证、商标品牌身份、专利披露维护、创作者版税元数据和 AI 训练数据权利/provenance。
- `human-animal-bond-companion-care-continuity/`、`veterinary-care-access-cost-continuity/`、`service-animal-disability-access-continuity/`、`pet-identification-microchip-reunification-continuity/`、`pet-food-medication-supply-safety-continuity/`、`pet-disaster-evacuation-sheltering-continuity/`、`animal-shelter-rescue-rehoming-continuity/` 和 `animal-welfare-cruelty-reporting-continuity/` 负责伴侣动物、服务动物与宠物照护连续性，把关系支持、兽医入口、辅助接口、身份重聚、食药供应、灾害撤离、收容转接和福利报告纳入主体持续性模型。
- 上述伴侣/服务动物域不提供动物诊疗、训练、购买、领养、繁育、救助行动、微芯片/寻宠操作、实时灾害撤离、动物举报取证、法律策略、家庭纠纷处理、宠物食品/药品建议、动物虐待或规避检查方法。
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
- `long-distance-travel-booking-itinerary-continuity/`、`air-passenger-rights-disruption-refund-continuity/`、`aviation-security-screening-identity-continuity/`、`baggage-personal-property-travel-continuity/`、`lodging-temporary-accommodation-access-continuity/`、`travel-advisory-consular-assistance-continuity/`、`travel-health-preparedness-continuity/` 和 `customs-border-entry-declaration-continuity/` 负责长距离旅行预订行程、航空中断退款、安检身份核验、行李个人物品、临时住宿、旅行警示领事协助、旅行健康准备和海关边境申报这些离家移动执行连续性条件。
- `online-retail-order-shipping-fulfillment-continuity/`、`consumer-return-refund-dispute-resolution-continuity/`、`consumer-warranty-service-contract-repair-continuity/`、`right-to-repair-parts-manuals-access-continuity/`、`payment-card-dispute-unauthorized-charge-continuity/`、`gift-card-prepaid-stored-value-continuity/`、`price-fee-disclosure-junk-fee-continuity/` 和 `consumer-reviews-endorsements-marketplace-trust-continuity/` 负责在线零售订单履约、退货退款争议、消费品保修维修、维修权零件手册、支付卡争议未授权扣款、礼品卡预付储值、价格费用披露和消费者评价背书市场信任这些消费者交易、履约与市场信任连续性条件。
- `credit-card-revolving-credit-cost-continuity/`、`consumer-loan-origination-apr-disclosure-continuity/`、`mortgage-origination-servicing-foreclosure-continuity/`、`auto-loan-lease-servicing-repossession-continuity/`、`student-loan-servicing-repayment-forgiveness-continuity/`、`payday-small-dollar-title-loan-continuity/`、`buy-now-pay-later-installment-financing-continuity/` 和 `remittance-money-transfer-disclosure-continuity/` 负责信用卡循环信用成本、消费贷款 APR 披露、房贷服务止赎、车贷租赁收车、学生贷款还款减免、发薪日/小额/汽车抵押贷款、BNPL 分期融资和汇款转账费用汇率这些消费者信贷、贷款服务与跨期资源连续性条件。
- `auto-insurance-liability-collision-claims-continuity/`、`homeowners-renters-property-insurance-claims-continuity/`、`flood-insurance-nfip-claims-continuity/`、`catastrophe-wind-wildfire-earthquake-insurance-continuity/`、`disability-income-insurance-claim-continuity/`、`long-term-care-insurance-benefit-activation-continuity/`、`travel-insurance-trip-protection-claims-continuity/` 和 `personal-liability-umbrella-insurance-defense-continuity/` 负责汽车保险理赔、房主租客财产理赔、洪水/NFIP 理赔、风暴野火地震巨灾保险、残障收入保险理赔、长期照护福利启动、旅行保险理赔和个人责任伞形保险防御这些个人保险、财产责任、灾害与理赔执行连续性条件。
- `citizenship-nationality-statelessness-continuity/`、`immigration-status-residency-work-authorization-continuity/`、`asylum-refugee-protection-status-continuity/`、`detention-custody-confinement-status-continuity/`、`civil-commitment-involuntary-treatment-rights-continuity/`、`court-notice-service-process-default-judgment-continuity/` 和 `criminal-record-relief-collateral-consequences-continuity/` 负责公民国籍无国籍、移民居留工作授权、庇护难民保护、拘押羁押监管状态、非自愿治疗权利、法院通知缺席判决和犯罪记录附带后果这些法律状态与强制程序连续性条件。
- `school-enrollment-attendance-continuity/`、`special-education-iep-504-accommodation-continuity/`、`school-meals-nutrition-access-continuity/`、`school-health-services-chronic-condition-continuity/`、`school-transportation-safe-routes-continuity/`、`school-discipline-exclusion-restraint-continuity/`、`school-mental-health-counseling-support-continuity/` 和 `school-climate-bullying-violence-prevention-continuity/` 负责入学出勤、特殊教育 IEP/504、校餐营养、学校健康服务、通学安全、纪律排除约束、学校心理健康和学校气候欺凌暴力预防这些学校服务连续性条件。
- `postsecondary-admissions-transfer-articulation-continuity/`、`student-financial-aid-grant-scholarship-continuity/`、`academic-advising-degree-progress-continuity/`、`campus-basic-needs-student-support-continuity/`、`campus-disability-accommodations-accessibility-continuity/`、`campus-mental-health-crisis-student-support-continuity/`、`campus-safety-title-ix-clery-continuity/` 和 `international-student-sevis-status-continuity/` 负责高等教育入学转学衔接、学生资助奖助学金、学业指导学位进度、校园基本需求、校园残障便利、校园心理危机支持、校园安全 Title IX/Clery 和国际学生 SEVIS 身份这些高等教育学生生命周期连续性条件。
- `email-account-recovery-continuity/`、`phone-number-sim-portability-account-security-continuity/`、`mfa-passkey-credential-recovery-continuity/`、`password-manager-secret-vault-continuity/`、`cloud-backup-file-sync-data-portability-continuity/`、`messaging-contact-graph-portability-continuity/`、`domain-dns-web-presence-continuity/` 和 `platform-account-suspension-appeals-continuity/` 负责邮箱账号恢复、手机号 SIM 携转安全、MFA/passkey 凭证恢复、密码管理器密钥库、云备份文件同步数据可携带、消息联系人图谱可携带、域名 DNS Web 存在和平台账号停权申诉这些数字账户与通信可达连续性条件。
- `personal-computing-device-lifecycle-repair-continuity/`、`home-network-router-iot-security-continuity/`、`software-supply-chain-dependency-provenance-continuity/`、`software-update-vulnerability-patch-continuity/`、`open-source-maintainer-sustainability-continuity/`、`pki-certificate-cryptographic-trust-continuity/`、`cloud-service-exit-interoperability-continuity/` 和 `api-platform-dependency-runtime-continuity/` 负责个人计算设备生命周期维修、家庭网络路由器 IoT 安全、软件供应链来源证明、软件更新漏洞补丁、开源维护者可持续、PKI 证书密码信任、云服务退出互操作和 API 平台运行时依赖这些软件、设备与信任连续性条件。
- `calendar-scheduling-appointment-continuity/`、`notification-alert-routing-attention-continuity/`、`reminder-alarm-routine-task-continuity/`、`meeting-video-conferencing-remote-collaboration-continuity/`、`document-capture-ocr-pdf-record-workflow-continuity/`、`search-index-discovery-retrieval-continuity/`、`personal-automation-integration-workflow-continuity/` 和 `collaborative-document-permission-version-continuity/` 负责日历排程预约、通知警报路由、提醒闹钟例行任务、会议视频远程协作、文件捕获 OCR PDF 记录流、搜索索引发现检索、个人自动化集成工作流和协作文档权限版本这些个人操作与任务协调连续性条件。
- `home-access-lock-key-entry-continuity/`、`household-appliance-maintenance-repair-continuity/`、`home-refrigeration-food-storage-continuity/`、`cooking-meal-preparation-kitchen-safety-continuity/`、`laundry-clothing-footwear-hygiene-continuity/`、`household-cleaning-disinfection-pest-control-continuity/`、`postal-parcel-delivery-pickup-continuity/` 和 `household-maintenance-repair-contractor-continuity/` 负责住所进入、家电维护、家庭冷藏、烹饪备餐、衣物鞋履卫生、家庭清洁消毒害虫控制、邮件包裹接收和家庭维修承包商这些家庭物理运行连续性条件。
- `personal-vehicle-maintenance-recall-repair-continuity/`、`fuel-ev-charging-refueling-access-continuity/`、`parking-curb-access-towing-impound-continuity/`、`walking-bicycling-micromobility-continuity/`、`paratransit-nemt-access-continuity/`、`taxi-rideshare-demand-response-mobility-continuity/`、`transit-fare-payment-toll-account-continuity/` 和 `multimodal-trip-planning-real-time-wayfinding-continuity/` 负责个人车辆维护召回维修、燃料/EV 充电补能、停车路缘拖车扣押、步行骑行微移动、paratransit/NEMT、出租车网约车需求响应交通、交通票卡/过路费账户和多模式实时导向这些个人移动执行连续性条件。
- `public-restroom-sanitation-hygiene-access-continuity/`、`public-drinking-water-hydration-access-continuity/`、`public-seating-shade-rest-cooling-access-continuity/`、`community-resilience-hub-shelter-center-continuity/`、`public-library-community-anchor-access-continuity/`、`parks-recreation-green-space-access-continuity/`、`public-wifi-device-charging-connectivity-continuity/` 和 `public-accommodation-accessibility-service-continuity/` 负责公共厕所卫生、公共饮水补水、公共座椅遮阴休息降温、社区韧性/避难中心、公共图书馆社区锚点、公园娱乐绿地、公共 Wi-Fi/设备充电和公共场所无障碍服务这些公共空间生存接入连续性条件。
- `grocery-retail-food-store-access-continuity/`、`snap-ebt-redemption-retailer-payment-continuity/`、`wic-benefit-redemption-infant-maternal-nutrition-continuity/`、`food-bank-pantry-community-food-distribution-continuity/`、`emergency-food-disaster-feeding-continuity/`、`home-delivered-meals-congregate-nutrition-services-continuity/`、`infant-formula-baby-food-supply-safety-continuity/` 和 `prepared-food-restaurant-cafeteria-safety-access-continuity/` 负责 grocery/食品零售、SNAP EBT 兑换、WIC 母婴营养兑换、食品银行/pantry、灾害供餐、送餐/集体营养服务、婴儿配方/婴幼儿食品供应安全和餐馆/cafeteria 熟食安全可达这些食物获得执行连续性条件。
- `retail-pharmacy-prescription-dispensing-continuity/`、`pharmacy-benefit-formulary-prior-authorization-continuity/`、`medication-reconciliation-regimen-adherence-continuity/`、`patient-medication-labeling-counseling-continuity/`、`unused-medicine-takeback-disposal-continuity/`、`durable-medical-equipment-supplier-repair-continuity/`、`home-oxygen-respiratory-equipment-supply-continuity/` 和 `diabetes-insulin-glucose-monitoring-supplies-continuity/` 负责药房处方配药、药品福利/处方集/事前授权、用药核对与依从执行、患者药品标签/咨询理解、未用药回收处置、DME 供应维修、居家氧疗/呼吸设备供应和糖尿病胰岛素/血糖监测耗材这些治疗获得与医用品执行连续性条件。
- `provider-directory-network-adequacy-continuity/`、`primary-care-panel-appointment-access-continuity/`、`specialist-referral-authorization-navigation-continuity/`、`appointment-availability-wait-time-continuity/`、`outpatient-laboratory-specimen-result-routing-continuity/`、`diagnostic-imaging-order-scheduling-report-continuity/`、`ambulatory-procedure-surgery-center-continuity/` 和 `after-hours-urgent-care-triage-continuity/` 负责 provider 名录/网络充足性、初级照护 panel/预约、专科转诊/授权导航、预约容量/等待时间、门诊检验标本/结果路由、诊断影像医嘱/报告回传、门诊操作/ASC 和非工作时间 urgent care/triage 这些门诊访问与临床服务执行连续性条件。
- `health-insurance-enrollment-renewal-continuity/`、`insurance-eligibility-benefits-verification-continuity/`、`medical-service-prior-authorization-utilization-management-continuity/`、`claims-adjudication-eob-denial-continuity/`、`patient-billing-payment-plan-continuity/`、`price-transparency-good-faith-estimate-continuity/`、`surprise-billing-balance-bill-protection-continuity/` 和 `charity-care-financial-assistance-medical-debt-continuity/` 负责健康保险参保续保、权益核验、医疗服务授权、理赔/EOB/拒付、患者账单/付款计划、价格透明/GFE、意外账单保护和 charity care/医疗债务这些医疗支付执行连续性条件。
- `patient-portal-account-message-continuity/`、`medical-record-access-amendment-release-continuity/`、`clinical-results-notification-followup-continuity/`、`informed-consent-refusal-shared-decision-continuity/`、`healthcare-language-interpreter-effective-communication-continuity/`、`healthcare-disability-accommodation-accessibility-continuity/`、`patient-grievance-complaint-ombuds-continuity/` 和 `healthcare-civil-rights-nondiscrimination-continuity/` 负责患者门户/医疗消息、病历访问修正释放、临床结果通知随访、知情同意/拒绝/共同决策、医疗语言服务、医疗残障便利、患者投诉/ombuds 和医疗民权反歧视这些患者权利与临床沟通连续性条件。
- `emergency-contact-next-of-kin-notification-continuity/`、`personal-health-record-emergency-summary-continuity/`、`medical-id-allergy-critical-alert-continuity/`、`medication-list-implant-device-emergency-continuity/`、`chronic-condition-emergency-action-plan-continuity/`、`immunization-record-proof-continuity/`、`organ-donor-registry-anatomical-gift-continuity/` 和 `access-functional-needs-emergency-registry-continuity/` 负责主体无法表达、急救、灾害和死亡边界中的紧急联系人、急救健康摘要、医疗 ID/关键警报、药物/植入设备、慢病行动计划、免疫记录、器官捐赠登记和功能需求登记连续性条件。
- `death-certificate-registration-cause-of-death-record-continuity/`、`funeral-cremation-burial-disposition-continuity/`、`cemetery-memorial-remains-location-continuity/`、`bereavement-leave-grief-support-continuity/`、`survivor-benefits-death-notification-continuity/`、`life-insurance-beneficiary-claim-continuity/`、`estate-inventory-asset-liability-handoff-continuity/` 和 `post-death-account-closure-service-cancellation-continuity/` 负责死亡边界后的死亡证明/死因记录、遗体处置、墓地纪念、遗属恢复、遗属福利、寿险理赔、遗产清单和账户关闭服务取消连续性条件。
- `loneliness-social-isolation-risk-continuity/`、`social-prescribing-community-referral-continuity/`、`mutual-aid-neighbor-support-network-continuity/`、`volunteering-civic-service-participation-continuity/`、`community-mediation-neighbor-conflict-resolution-continuity/`、`restorative-justice-repair-accountability-continuity/`、`reputation-defamation-public-trust-repair-continuity/`、`references-vouching-recommendation-social-capital-continuity/` 和 `third-place-belonging-social-participation-continuity/` 负责关系执行与社会资本连续性，覆盖孤独隔离风险、社会处方转介、互助邻里、志愿服务、社区调解、修复性司法、声誉信任修复、推荐背书和第三空间归属参与。
- `purpose-meaning-existential-continuity/`、`spiritual-care-religious-practice-continuity/`、`cultural-heritage-identity-continuity/`、`arts-creative-expression-participation-continuity/`、`leisure-recreation-restorative-activity-continuity/`、`narrative-identity-life-review-continuity/`、`ritual-ceremony-life-transition-continuity/` 和 `dignity-personhood-respect-continuity/` 负责意义、文化、身份、创造、休闲、叙事、仪式和尊严连续性，覆盖主体为什么继续、如何表达、如何归属、如何被承认和如何避免被去人格化。
- `human-factors-ergonomics-task-system-continuity/`、`cognitive-load-workload-measurement-continuity/`、`fatigue-risk-alertness-continuity/`、`situational-awareness-decision-environment-continuity/`、`handoff-checklist-procedure-reliability-continuity/`、`incident-reporting-just-culture-learning-continuity/`、`automation-bias-mode-confusion-oversight-continuity/` 和 `alert-fatigue-interruption-signal-management-continuity/` 负责人因与操作可靠性连续性，覆盖人-工具-流程适配、认知负荷、疲劳警觉、情境感知、交接清单、事件学习、自动化监督和告警中断管理。
- `depression-mood-disorder-functioning-continuity/`、`anxiety-stress-threat-regulation-continuity/`、`trauma-ptsd-adversity-recovery-continuity/`、`psychosis-reality-testing-community-continuity/`、`bipolar-mood-episode-stability-continuity/`、`adhd-executive-function-neurodevelopment-continuity/`、`autism-neurodiversity-support-continuity/` 和 `eating-disorders-nutrition-body-continuity/` 负责心理健康、神经发育与功能连续性，覆盖抑郁心境功能、焦虑压力威胁调节、创伤/PTSD 恢复、精神病性现实检验、双相情绪周期稳定、ADHD 执行功能、自闭神经多样性支持和进食障碍营养身体连续性。
- `access-to-justice-legal-aid/`、`civic-participation-election-access/`、`migration-displacement-humanitarian-continuity/` 和 `digital-inclusion-connectivity/` 负责司法可及、公民参与、迁移流离失所人道连续性和数字连接这些制度参与与公共服务接入条件。
- `personal-safety-violence-prevention/` 和 `product-safety-recall-systems/` 负责暴力预防、受害者支持、产品缺陷报告、召回和纠正这些公共安全连续性条件。
- `domestic-violence-coercive-control-safety-continuity/`、`sexual-assault-forensic-exam-advocacy-continuity/`、`stalking-harassment-protection-order-continuity/`、`victim-witness-rights-notification-continuity/`、`crime-victim-compensation-restitution-continuity/`、`survivor-safe-housing-emergency-transfer-continuity/`、`human-trafficking-victim-identification-services-continuity/` 和 `missing-persons-unidentified-remains-resolution-continuity/` 负责把综合人身安全域拆成受害者安全、服务、权利通知、住房转移、补偿恢复、人口贩运识别和失踪身份恢复这些可独立审查的执行连续性条件。
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
- `long-distance-travel-booking-itinerary-continuity/`、`air-passenger-rights-disruption-refund-continuity/`、`aviation-security-screening-identity-continuity/`、`baggage-personal-property-travel-continuity/`、`lodging-temporary-accommodation-access-continuity/`、`travel-advisory-consular-assistance-continuity/`、`travel-health-preparedness-continuity/` 和 `customs-border-entry-declaration-continuity/` 负责旅行、住宿、安检、领事、健康和边境移动连续性的证据边界，不提供路线推荐、票务套利、退款赔偿、安检规避、违禁品携带、住宿选择、旅行安全、医疗、签证、移民、海关申报、保险、法律或个案策略建议。
- `online-retail-order-shipping-fulfillment-continuity/`、`consumer-return-refund-dispute-resolution-continuity/`、`consumer-warranty-service-contract-repair-continuity/`、`right-to-repair-parts-manuals-access-continuity/`、`payment-card-dispute-unauthorized-charge-continuity/`、`gift-card-prepaid-stored-value-continuity/`、`price-fee-disclosure-junk-fee-continuity/` 和 `consumer-reviews-endorsements-marketplace-trust-continuity/` 负责消费者交易、履约、维修、支付、储值、价格披露和市场信任的证据边界，不提供购物推荐、退款脚本、chargeback 策略、维修破解、礼品卡交易、费用规避、刷评营销、金融、法律或个案消费者争议建议。
- `credit-card-revolving-credit-cost-continuity/`、`consumer-loan-origination-apr-disclosure-continuity/`、`mortgage-origination-servicing-foreclosure-continuity/`、`auto-loan-lease-servicing-repossession-continuity/`、`student-loan-servicing-repayment-forgiveness-continuity/`、`payday-small-dollar-title-loan-continuity/`、`buy-now-pay-later-installment-financing-continuity/` 和 `remittance-money-transfer-disclosure-continuity/` 负责消费者信贷、贷款服务与跨期资源连续性的证据边界，不提供贷款申请、还款、再融资、减免、止赎、收车、汇款、避税、制裁规避、KYC/AML 规避、逃债、金融规划、法律或个案争议建议。
- `auto-insurance-liability-collision-claims-continuity/`、`homeowners-renters-property-insurance-claims-continuity/`、`flood-insurance-nfip-claims-continuity/`、`catastrophe-wind-wildfire-earthquake-insurance-continuity/`、`disability-income-insurance-claim-continuity/`、`long-term-care-insurance-benefit-activation-continuity/`、`travel-insurance-trip-protection-claims-continuity/` 和 `personal-liability-umbrella-insurance-defense-continuity/` 负责个人保险、财产责任、灾害与理赔执行连续性的证据边界，不提供投保、保额选择、理赔策略、赔付估值、医疗转运、照护机构选择、诉讼、资产隐藏、重复索赔、保险欺诈、法律或个案争议建议。
- `citizenship-nationality-statelessness-continuity/`、`immigration-status-residency-work-authorization-continuity/`、`asylum-refugee-protection-status-continuity/`、`detention-custody-confinement-status-continuity/`、`civil-commitment-involuntary-treatment-rights-continuity/`、`court-notice-service-process-default-judgment-continuity/` 和 `criminal-record-relief-collateral-consequences-continuity/` 负责法律状态、保护身份、强制程序与记录救济连续性的证据边界，不提供公民身份、国籍、移民、庇护、拘押、非自愿治疗、法院程序、犯罪记录救济、刑事、税务、医疗或法律建议。
- `school-enrollment-attendance-continuity/`、`special-education-iep-504-accommodation-continuity/`、`school-meals-nutrition-access-continuity/`、`school-health-services-chronic-condition-continuity/`、`school-transportation-safe-routes-continuity/`、`school-discipline-exclusion-restraint-continuity/`、`school-mental-health-counseling-support-continuity/` 和 `school-climate-bullying-violence-prevention-continuity/` 负责学校服务连续性的证据边界，不提供个人入学、出勤、IEP/504、校餐、校医、通学路线、纪律申诉、心理危机、欺凌投诉、教育、医疗、法律或个案建议。
- `postsecondary-admissions-transfer-articulation-continuity/`、`student-financial-aid-grant-scholarship-continuity/`、`academic-advising-degree-progress-continuity/`、`campus-basic-needs-student-support-continuity/`、`campus-disability-accommodations-accessibility-continuity/`、`campus-mental-health-crisis-student-support-continuity/`、`campus-safety-title-ix-clery-continuity/` 和 `international-student-sevis-status-continuity/` 负责高等教育学生生命周期连续性的证据边界，不提供个人申请、转学、资助、选课、住宿、残障便利、心理危机、Title IX、校园安全、SEVIS、移民、税务、医疗、法律或个案建议。
- `email-account-recovery-continuity/`、`phone-number-sim-portability-account-security-continuity/`、`mfa-passkey-credential-recovery-continuity/`、`password-manager-secret-vault-continuity/`、`cloud-backup-file-sync-data-portability-continuity/`、`messaging-contact-graph-portability-continuity/`、`domain-dns-web-presence-continuity/` 和 `platform-account-suspension-appeals-continuity/` 负责数字账户与通信可达连续性的证据边界，不提供个人账号恢复、绕过验证、短信拦截、MFA 绕过、密码破解、密钥导出、云盘取证、聊天恢复、联系人抓取、DNS 操作、平台封禁规避、申诉文案、法律或安全事件处置建议。
- `personal-computing-device-lifecycle-repair-continuity/`、`home-network-router-iot-security-continuity/`、`software-supply-chain-dependency-provenance-continuity/`、`software-update-vulnerability-patch-continuity/`、`open-source-maintainer-sustainability-continuity/`、`pki-certificate-cryptographic-trust-continuity/`、`cloud-service-exit-interoperability-continuity/` 和 `api-platform-dependency-runtime-continuity/` 负责软件、设备与信任连续性的证据边界，不提供绕过设备锁、破解加密、网络入侵、IoT 漏洞利用、供应链攻击、恶意包、漏洞利用、证书滥用、云入侵、API 限制规避、计费规避、账号规避或安全事件处置建议。
- `calendar-scheduling-appointment-continuity/`、`notification-alert-routing-attention-continuity/`、`reminder-alarm-routine-task-continuity/`、`meeting-video-conferencing-remote-collaboration-continuity/`、`document-capture-ocr-pdf-record-workflow-continuity/`、`search-index-discovery-retrieval-continuity/`、`personal-automation-integration-workflow-continuity/` 和 `collaborative-document-permission-version-continuity/` 负责个人操作与任务协调连续性的证据边界，不提供抢号刷号、垃圾推送、监控控制、会议入侵、文件伪造、搜索排名操纵、凭证滥用、平台限制规避、未授权导出或隐私窃取方法。
- `home-access-lock-key-entry-continuity/`、`household-appliance-maintenance-repair-continuity/`、`home-refrigeration-food-storage-continuity/`、`cooking-meal-preparation-kitchen-safety-continuity/`、`laundry-clothing-footwear-hygiene-continuity/`、`household-cleaning-disinfection-pest-control-continuity/`、`postal-parcel-delivery-pickup-continuity/` 和 `household-maintenance-repair-contractor-continuity/` 负责家庭物理运行连续性的证据边界，不提供开锁入侵、危险维修、燃气电气施工、食品处置、化学品混合、杀虫剂使用、邮件拦截、冒领、承包商规避、理赔策略、法律意见或个体购买建议。
- `personal-vehicle-maintenance-recall-repair-continuity/`、`fuel-ev-charging-refueling-access-continuity/`、`parking-curb-access-towing-impound-continuity/`、`walking-bicycling-micromobility-continuity/`、`paratransit-nemt-access-continuity/`、`taxi-rideshare-demand-response-mobility-continuity/`、`transit-fare-payment-toll-account-continuity/` 和 `multimodal-trip-planning-real-time-wayfinding-continuity/` 负责个人移动执行连续性的证据边界，不提供车辆维修步骤、危险燃料处理、充电桩破解、停车执法规避、交通违法、共享设备破解、NEMT 资格规避、报销欺诈、平台规避、逃票、票卡破解、过路费规避、路线跟踪或个案申诉/法律策略。
- `public-restroom-sanitation-hygiene-access-continuity/`、`public-drinking-water-hydration-access-continuity/`、`public-seating-shade-rest-cooling-access-continuity/`、`community-resilience-hub-shelter-center-continuity/`、`public-library-community-anchor-access-continuity/`、`parks-recreation-green-space-access-continuity/`、`public-wifi-device-charging-connectivity-continuity/` 和 `public-accommodation-accessibility-service-continuity/` 负责公共空间生存接入连续性的证据边界，不提供厕所定位跟踪、设施破坏、供水篡改、污染制造、露宿/避难资格规避、公共 Wi-Fi 攻击、设备盗充、服务动物欺诈、ADA 诉讼策略、儿童/弱势群体跟踪、实时拥挤跟踪、执法规避或个案法律/医疗/救援建议。
- `grocery-retail-food-store-access-continuity/`、`snap-ebt-redemption-retailer-payment-continuity/`、`wic-benefit-redemption-infant-maternal-nutrition-continuity/`、`food-bank-pantry-community-food-distribution-continuity/`、`emergency-food-disaster-feeding-continuity/`、`home-delivered-meals-congregate-nutrition-services-continuity/`、`infant-formula-baby-food-supply-safety-continuity/` 和 `prepared-food-restaurant-cafeteria-safety-access-continuity/` 负责食物获得执行连续性的证据边界，不提供福利资格规避、EBT/eWIC 破解、PIN 获取、盗刷、福利转售、食品发放重复领取、物资骗领、囤积套利、婴儿喂养医疗建议、配方自制、召回规避、餐馆推荐、饮食处方、外卖平台规避、个案投诉/法律/医疗/福利策略。
- `retail-pharmacy-prescription-dispensing-continuity/`、`pharmacy-benefit-formulary-prior-authorization-continuity/`、`medication-reconciliation-regimen-adherence-continuity/`、`patient-medication-labeling-counseling-continuity/`、`unused-medicine-takeback-disposal-continuity/`、`durable-medical-equipment-supplier-repair-continuity/`、`home-oxygen-respiratory-equipment-supply-continuity/` 和 `diabetes-insulin-glucose-monitoring-supplies-continuity/` 负责治疗获得与医用品执行连续性的证据边界，不提供处方、换药、剂量、停药、替代药、个案相互作用判断、医保申诉代写、PA 材料、诊断证明、保险规避、药房/PBM 规则规避、DME 维修改装、氧流量/设备设置、CPAP 参数、胰岛素剂量、CGM 个案解读、药品处置指令、管制药规避、敏感处方/保险/健康数据收集或急救替代。
- `provider-directory-network-adequacy-continuity/`、`primary-care-panel-appointment-access-continuity/`、`specialist-referral-authorization-navigation-continuity/`、`appointment-availability-wait-time-continuity/`、`outpatient-laboratory-specimen-result-routing-continuity/`、`diagnostic-imaging-order-scheduling-report-continuity/`、`ambulatory-procedure-surgery-center-continuity/` 和 `after-hours-urgent-care-triage-continuity/` 负责门诊访问与临床服务执行连续性的证据边界，不提供 provider/plan/doctor 推荐、诊断、检测/影像/操作选择、检验或影像解释、转诊策略、prior authorization/exception 代写、预约机器人、刷号、排队规避、urgent/ED 分诊、手术/操作准备、麻醉评估、并发症处理、账单争议、法律/保险策略，或收集 PHI、保险、portal、预约、检验、影像、操作、triage 数据。
- `health-insurance-enrollment-renewal-continuity/`、`insurance-eligibility-benefits-verification-continuity/`、`medical-service-prior-authorization-utilization-management-continuity/`、`claims-adjudication-eob-denial-continuity/`、`patient-billing-payment-plan-continuity/`、`price-transparency-good-faith-estimate-continuity/`、`surprise-billing-balance-bill-protection-continuity/` 和 `charity-care-financial-assistance-medical-debt-continuity/` 负责医疗支付、理赔、账单与成本保护连续性的证据边界，不提供保险选择、参保、补贴资格、权益解释、授权/申诉代写、理赔争议、账单谈判、付款计划、价格比较、机构选择、法律/税务/信用修复/债务建议、保险规避、虚假材料、欺诈策略，或收集 SSN、member ID、保险、账单、EOB、claim、收入、资产、信用、银行和 PHI 数据。
- `patient-portal-account-message-continuity/`、`medical-record-access-amendment-release-continuity/`、`clinical-results-notification-followup-continuity/`、`informed-consent-refusal-shared-decision-continuity/`、`healthcare-language-interpreter-effective-communication-continuity/`、`healthcare-disability-accommodation-accessibility-continuity/`、`patient-grievance-complaint-ombuds-continuity/` 和 `healthcare-civil-rights-nondiscrimination-continuity/` 负责患者权利、记录访问、临床沟通与医疗民权连续性的证据边界，不提供门户恢复、病历索取、记录解释、结果解读、医疗建议、同意/拒绝建议、翻译口译、便利申请、投诉代写、法律意见、歧视认定、诉讼策略，或收集 portal 凭证、MRN、授权书、病历、诊断、受保护身份、投诉证据、联系方式和 PHI 数据。
- `emergency-contact-next-of-kin-notification-continuity/`、`personal-health-record-emergency-summary-continuity/`、`medical-id-allergy-critical-alert-continuity/`、`medication-list-implant-device-emergency-continuity/`、`chronic-condition-emergency-action-plan-continuity/`、`immunization-record-proof-continuity/`、`organ-donor-registry-anatomical-gift-continuity/` 和 `access-functional-needs-emergency-registry-continuity/` 负责急救健康信息与紧急交接连续性的证据边界，不提供个人急救、医疗解释、病历摘要生成、联系人通知、亲属查找、用药/设备判断、疫苗建议、器官捐赠登记、灾害报名、撤离计划、法律建议，或收集联系人、PHI、设备序列号、疫苗卡、捐赠登记、地址、定位、残障证明和功能需求资料。
- `death-certificate-registration-cause-of-death-record-continuity/`、`funeral-cremation-burial-disposition-continuity/`、`cemetery-memorial-remains-location-continuity/`、`bereavement-leave-grief-support-continuity/`、`survivor-benefits-death-notification-continuity/`、`life-insurance-beneficiary-claim-continuity/`、`estate-inventory-asset-liability-handoff-continuity/` 和 `post-death-account-closure-service-cancellation-continuity/` 负责死亡后与遗属连续性的证据边界，不提供死亡证明办理、遗体处置安排、墓地查找、心理治疗、福利申请、保险理赔、probate、税务、债务、账户关闭、平台申诉或法律建议，或收集死亡证明、遗体位置、保单、资产负债、账号、密码、亲属关系和身份文件。
- `loneliness-social-isolation-risk-continuity/`、`social-prescribing-community-referral-continuity/`、`mutual-aid-neighbor-support-network-continuity/`、`volunteering-civic-service-participation-continuity/`、`community-mediation-neighbor-conflict-resolution-continuity/`、`restorative-justice-repair-accountability-continuity/`、`reputation-defamation-public-trust-repair-continuity/`、`references-vouching-recommendation-social-capital-continuity/` 和 `third-place-belonging-social-participation-continuity/` 负责关系执行与社会资本连续性的证据边界，不提供心理治疗、危机干预、医疗/福利转介、志愿者调度、调解代理、法律建议、声誉清洗、推荐信代写、社交操控、舆论操作、场所推荐、活动组织或敏感社交数据收集。
- `purpose-meaning-existential-continuity/`、`spiritual-care-religious-practice-continuity/`、`cultural-heritage-identity-continuity/`、`arts-creative-expression-participation-continuity/`、`leisure-recreation-restorative-activity-continuity/`、`narrative-identity-life-review-continuity/`、`ritual-ceremony-life-transition-continuity/` 和 `dignity-personhood-respect-continuity/` 负责意义文化身份连续性的证据边界，不提供心理治疗、宗教指导、文化正统裁判、艺术治疗、活动推荐、生命故事代写、仪式安排、法律/医疗建议、临终决策、个体化价值判断或敏感身份资料收集。
- `human-factors-ergonomics-task-system-continuity/`、`cognitive-load-workload-measurement-continuity/`、`fatigue-risk-alertness-continuity/`、`situational-awareness-decision-environment-continuity/`、`handoff-checklist-procedure-reliability-continuity/`、`incident-reporting-just-culture-learning-continuity/`、`automation-bias-mode-confusion-oversight-continuity/` 和 `alert-fatigue-interruption-signal-management-continuity/` 负责人因与操作可靠性连续性的证据边界，不提供医疗/法律/安全个案建议、现场指挥、操作清单、排班规避、员工监控、事故调查代理、高风险系统部署、告警配置、自动化接管或敏感操作数据收集。
- `depression-mood-disorder-functioning-continuity/`、`anxiety-stress-threat-regulation-continuity/`、`trauma-ptsd-adversity-recovery-continuity/`、`psychosis-reality-testing-community-continuity/`、`bipolar-mood-episode-stability-continuity/`、`adhd-executive-function-neurodevelopment-continuity/`、`autism-neurodiversity-support-continuity/` 和 `eating-disorders-nutrition-body-continuity/` 负责心理健康、神经发育与功能连续性的证据边界，不提供诊断、治疗、药物、危机处置、家庭干预、饮食控制、行为训练、招聘/教育筛选、个体风险评分、危险性判断、社交训练或敏感资料收集。
- `regenerative-medicine/`、`cancer-control/` 和 `immune-maintenance/` 负责身体基底维护相关的机制、风险和证据边界。
- `rehabilitation-functioning/`、`assistive-technology-access/`、`skin-barrier-wound-healing/` 和 `sensory-continuity/` 负责功能恢复、能力补偿、外界屏障和感官反馈连续性。
- `antimicrobial-resilience/` 负责抗微生物耐药、感染控制和现代医学抗感染底座。
- `neuro-continuity/`、`memory-editing/`、`cognitive-augmentation/`、`ai-agency-safety/`、`digital-identity-security/` 和 `disembodied-cns/` 负责神经、身份、认知、AI 代理、数字入口和去具身连续性相关边界。
- `ai-evaluation-benchmark-validity-continuity/`、`ai-red-teaming-adversarial-testing-continuity/`、`ai-incident-reporting-post-deployment-monitoring-continuity/`、`ai-data-provenance-contamination-drift-continuity/`、`synthetic-data-generation-validation-continuity/`、`ai-model-supply-chain-provenance-release-continuity/`、`ai-agent-tool-permission-sandbox-continuity/`、`human-ai-oversight-handoff-accountability-continuity/` 和 `ai-resource-cost-latency-budget-continuity/` 负责 AI 作为主体增强系统时的评测、红队、事故监控、数据谱系、合成数据、模型供应链、工具权限、人机交接和资源预算边界。
- `semiconductor-manufacturing-metrology-continuity/`、`semiconductor-advanced-packaging-continuity/`、`chip-design-eda-verification-ip-continuity/`、`ai-hardware-accelerator-performance-continuity/`、`data-center-cooling-water-thermal-continuity/`、`large-load-grid-interconnection-transmission-continuity/`、`grid-scale-energy-storage-flexibility-continuity/`、`advanced-nuclear-energy-safety-generation-continuity/`、`undersea-cable-internet-backbone-continuity/` 和 `satellite-communications-spectrum-orbit-continuity/` 负责先进计算、能源与连接物理底座的证据边界，不提供芯片制造、EDA 绕权、数据中心建设、电网并网、核设施、光缆、频谱、卫星、采购、投资、出口管制规避、攻击或关键基础设施操作建议。
- `cardiac-arrest-cpr-defibrillation-continuity/`、`sepsis-shock-early-recognition-resuscitation-continuity/`、`trauma-system-hemorrhage-control-continuity/`、`intensive-care-organ-support-delirium-continuity/`、`mechanical-ventilation-respiratory-failure-continuity/`、`ecmo-extracorporeal-life-support-continuity/`、`acute-kidney-injury-renal-replacement-continuity/`、`transfusion-blood-management-hemorrhage-continuity/`、`overdose-poisoning-reversal-toxicology-continuity/` 和 `burn-injury-critical-care-rehabilitation-continuity/` 负责急性救援与临时器官支持的证据边界，不提供 CPR、除颤、抗生素、ICU、呼吸机、ECMO、透析、输血、中毒处理、烧伤处理或个案医疗建议。
- `acute-coronary-syndrome-reperfusion-continuity/`、`acute-heart-failure-decompensation-continuity/`、`cardiac-arrhythmia-syncope-decompensation-continuity/`、`venous-thromboembolism-pulmonary-embolism-continuity/`、`hypertensive-crisis-end-organ-risk-continuity/`、`diabetic-hyperglycemic-hypoglycemic-crisis-continuity/`、`anaphylaxis-allergic-emergency-continuity/`、`asthma-copd-exacerbation-airway-continuity/`、`acute-gastrointestinal-bleeding-endoscopy-continuity/` 和 `obstetric-emergency-hemorrhage-hypertension-continuity/` 负责急性内科与时间关键急症的证据边界，不提供胸痛、心衰、晕厥、肺栓塞、高血压危象、糖尿病危象、过敏性休克、哮喘/COPD、消化道出血、产科急症的诊断、分诊、用药、设备、操作、转运、预后或个案医疗建议。
- `hypertension-detection-control-continuity/`、`lipid-atherosclerosis-risk-management-continuity/`、`prediabetes-diabetes-prevention-continuity/`、`obesity-adiposity-metabolic-risk-continuity/`、`tobacco-nicotine-cessation-continuity/`、`alcohol-use-risk-reduction-continuity/`、`chronic-kidney-disease-screening-progression-continuity/`、`cancer-screening-early-detection-continuity/`、`osteoporosis-fracture-prevention-bone-health-continuity/` 和 `fall-risk-prevention-home-safety-continuity/` 负责预防筛查与风险因子控制的证据边界，不提供血压、血脂、血糖/A1c、BMI/体脂、烟草/酒精、肾功能、癌筛、骨密度或跌倒风险的个体判断、用药、处方、戒断、饮食、运动、检查频率、设备、家庭处理、保险或医疗建议。
- `sleep-disordered-breathing-screening-treatment-continuity/`、`chronic-insomnia-cbti-access-continuity/`、`sexual-health-sti-prevention-continuity/`、`hiv-testing-prep-prevention-continuity/`、`chronic-viral-hepatitis-screening-liver-protection-continuity/`、`contraception-family-planning-access-continuity/`、`menstrual-health-cycle-literacy-continuity/`、`perimenopause-menopause-midlife-health-continuity/`、`pelvic-floor-continence-function-continuity/` 和 `skin-cancer-uv-protection-early-detection-continuity/` 负责生活史预防与功能连续性的证据边界，不提供睡眠报告判读、CBT-I 操作、STI/HIV/肝炎检测解释、PrEP/PEP/ART、避孕选择、周期判读、激素治疗、盆底训练、皮损照片判断、防晒产品、用药、检查频率、保险、法律或个体医疗建议。
- `mental-health-affective-stability/`、`sleep-circadian-recovery/` 和 `pain-suffering-control/` 负责心理稳定、恢复调度和持续存在的可承受性。
- `social-connection-relational-infra/` 负责社会连接、孤独、照护网络、信任和社区关系。
- `loneliness-social-isolation-risk-continuity/`、`social-prescribing-community-referral-continuity/`、`mutual-aid-neighbor-support-network-continuity/`、`volunteering-civic-service-participation-continuity/`、`community-mediation-neighbor-conflict-resolution-continuity/`、`restorative-justice-repair-accountability-continuity/`、`reputation-defamation-public-trust-repair-continuity/`、`references-vouching-recommendation-social-capital-continuity/` 和 `third-place-belonging-social-participation-continuity/` 负责把社会连接拆成可执行、可转介、可互助、可参与、可调解、可修复、可纠错、可背书和可归属的关系基础设施层。
- `purpose-meaning-existential-continuity/`、`spiritual-care-religious-practice-continuity/`、`cultural-heritage-identity-continuity/`、`arts-creative-expression-participation-continuity/`、`leisure-recreation-restorative-activity-continuity/`、`narrative-identity-life-review-continuity/`、`ritual-ceremony-life-transition-continuity/` 和 `dignity-personhood-respect-continuity/` 负责把主体持续性拆成目的、意义、精神照护、文化身份、创造表达、休闲恢复、生命叙事、仪式承认和尊严人格这些价值与身份基础设施层。
- `human-factors-ergonomics-task-system-continuity/`、`cognitive-load-workload-measurement-continuity/`、`fatigue-risk-alertness-continuity/`、`situational-awareness-decision-environment-continuity/`、`handoff-checklist-procedure-reliability-continuity/`、`incident-reporting-just-culture-learning-continuity/`、`automation-bias-mode-confusion-oversight-continuity/` 和 `alert-fatigue-interruption-signal-management-continuity/` 负责把主体持续性拆成人因适配、负荷边界、疲劳恢复、情境感知、交接过程、事件学习、自动化监督和信号环境这些任务可靠性基础设施层。
- `depression-mood-disorder-functioning-continuity/`、`anxiety-stress-threat-regulation-continuity/`、`trauma-ptsd-adversity-recovery-continuity/`、`psychosis-reality-testing-community-continuity/`、`bipolar-mood-episode-stability-continuity/`、`adhd-executive-function-neurodevelopment-continuity/`、`autism-neurodiversity-support-continuity/` 和 `eating-disorders-nutrition-body-continuity/` 负责把主体持续性拆成动机能量、威胁调节、创伤恢复、现实检验、情绪周期、执行功能、神经多样性支持和身体供能这些心理功能基础设施层。
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
