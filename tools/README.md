# Tools

`tools/` contains repository maintenance scripts. These scripts support the knowledge base itself; they are not product code.

## Current Tools

- `audit_public_product_boundary.py`: rejects Wiki, technology-tree, and immortality-timeline product sources that re-enter this public repository.
- `arxiv_html_paper_tool.py`: installs, verifies, and scaffolds the reusable arXiv HTML papers reader framework for Astro projects.
- `audit_core_claim_evidence_matrix.py`: verifies that the core Human Infra Claim-Evidence Matrix keeps required source anchors, claim IDs, evidence gates, prohibited-use boundaries, method URLs, and index links.
- `audit_human_infra_maturity_gap_register.py`: verifies that the 100% maturity gap register keeps value, research-framework, and quantitative-model gates aligned with the maturity roadmap, local evidence paths, and blocked-state boundaries.
- `audit_human_infra_model_admission_contract.py`: verifies that the model-admission contract keeps L0-L5 admission levels, MAC gates, hard abort gates, standards trace, index links, and calibrated/individual-use blocks intact.
- `audit_human_infra_model_admission_candidate_registry.py`: verifies that the model-admission candidate registry covers all reviewed artifact registers from the contract, preserves L1/L2-only reviewed artifacts, keeps synthetic outputs L3-only, and blocks L4/L5.
- `audit_human_infra_quantitative_capability_ladder.py`: verifies that the Q0-Q5 quantitative capability ladder keeps current capability at Q3/L3 synthetic outputs and blocks Q4 aggregate calibrated modeling, Q5 individual use, individual death-date output, medical advice and intervention ranking.
- `audit_human_infra_domain_to_model_bridge.py`: verifies that representative C1-C6 research domains only enter the model as B2/L2/Q2 candidate-variable and model-location vocabulary, while coefficients, causal effects, calibrated prediction, individual use, medical advice, intervention ranking and death-date output stay blocked.
- `audit_human_infra_brain_body_interface_protocol_register.py`: verifies the C1 `disembodied-cns` brain-body interface protocol register, preserving L2/Q2 candidate-only status, required interface fields, Source Card anchors and blocked operational/clinical/engineering-use boundaries.
- `audit_human_infra_minimal_sufficient_body_claim_evidence_matrix.py`: verifies the C1 `disembodied-cns` minimal-sufficient-body Claim-Evidence Matrix, preserving Source Card/protocol-row anchors, variables, falsifiers, downgrade actions and L2/Q2 no-operational-use boundaries.
- `audit_human_infra_l4_model_readiness_blocker_matrix.py`: verifies that the L4 blocker matrix keeps NHANES local-output, NHATS runway, disclosure, survey-design, calibration and individual-use blockers explicit before any L4 model admission.
- `audit_human_infra_l4_unblock_execution_plan.py`: verifies that the L4 unblock execution plan orders NHANES/NHATS work orders, direct evidence requirements, dependencies, validation commands and AI-only-signoff prohibitions without opening L4.
- `audit_human_infra_l4_evidence_intake_register.py`: verifies that the L4 evidence intake register and evidence packet review playbook keep every direct-evidence slot pending, define a zero-packet evidence packet contract, reject raw/restricted/AI-only evidence classes, require human review and keep L4/public/calibrated/individual uses blocked.
- `audit_human_infra_l4_evidence_packet_validator.py`: verifies synthetic future evidence-packet cases and writes `web/src/data/life-path-l4-evidence-packet-validator-validation.json`, allowing only `rejected`, `cannot-evaluate` or `reviewable-but-still-blocked` verdicts while keeping real packets, slot closure, L4 admission, public weighted output and individual prediction blocked.
- `audit_human_infra_l4_validation_calibration_reporting_contract.py`: verifies that the L4 validation/calibration reporting contract binds L4WO-05 to required report sections, calibration diagnostics, TRIPOD+AI / PROBAST+AI-style reporting and zero-packet blocked-state boundaries.
- `audit_human_infra_research_standards_source_anchor_register.py`: verifies that the external research-standards anchor register covers reporting, bias, certainty, causal-emulation, RWE and model-transparency routes while keeping model admission, individual prediction, medical advice and longevity escape velocity claims blocked.
- `audit_human_infra_l4_validation_calibration_report_execution_register.py`: verifies that the L4 validation/calibration report execution register keeps all 12 report sections and 5 L4WO-05 slots pending real report packets, writes the Web validation summary, and preserves L4/public/calibrated/individual-use blocks.
- `audit_human_infra_audience_claim_map.py`: verifies that value clarity has audience-specific Claim ID entry points and adjacent-project boundary distinctions from `docs/reference/human-infra-audience-claim-map.json`.
- `audit_human_infra_domain_falsifier_coverage.py`: verifies that C1 and the current 20 priority C2 research domains keep falsifier, downgrade-condition, variable-interface and prohibited-use scaffolding from `docs/reference/human-infra-domain-falsifier-coverage.json`.
- `audit_human_infra_domain_claim_evidence_matrix.py`: verifies that the current 30 priority research domains are joined to domain claims, variable-contract sources, falsifier sources and extracted Source Card IDs from `docs/reference/human-infra-domain-claim-evidence-matrix.json`.
- `audit_human_infra_domain_source_card_field_extraction.py`: verifies that each current domain matrix seed row has endpoint candidates, source IDs, population-boundary slots, uncertainty-channel slots, transfer-boundary slots and next field-extraction actions from `docs/reference/human-infra-domain-source-card-field-extraction.json`.
- `audit_human_infra_c2_longtail_coverage_register.py`: verifies that `docs/reference/human-infra-c2-longtail-coverage-register.json` covers every C2 source-maintenance domain from `classification.tsv`, distinguishes 20 reviewed priority domains from 184 long-tail uncovered domains, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_first_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-promotion-queue.json` selects the first high-impact C2 long-tail domains, keeps them tied to the coverage register, requires candidate sources and promotion steps, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_first_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-source-extraction-queue.json` derives the first-batch promotion queue into 48 domain-source extraction tasks with required slots, questions, blocked uses, index links and model-admission boundaries.
- `audit_human_infra_c2_longtail_first_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-source-extraction-register.json` completes all 48/48 C2 long-tail first-batch source-context extraction rows with required fields, downgrade triggers, blocked uses and index links.
- `audit_human_infra_c2_longtail_first_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-local-review-register.json` locally reviews all 48/48 C2-LT-B1 extraction rows, maps them back to queue/register evidence, preserves blocked uses, and routes only to independent fresh review.
- `audit_human_infra_c2_longtail_first_batch_independent_fresh_review_protocol.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-independent-fresh-review-protocol.json` covers all 48 locally reviewed C2-LT-B1 rows in four review batches without embedding verdicts.
- `audit_human_infra_c2_longtail_first_batch_independent_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-independent-fresh-review-verdict-register.json` records 48/48 bounded fresh-review verdicts and keeps reviewed artifact promotion plus model admission controlled.
- `audit_human_infra_c2_longtail_first_batch_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-reviewed-card-artifact-register.json` promotes exactly the 42 eligible C2-LT-B1 verdict rows into 252 reviewed artifacts, preserves 6 blocked rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_first_batch_blocked_source_resolution_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-blocked-source-resolution-register.json` covers exactly the 6 non-eligible C2-LT-B1 rows with source-resolution candidates while keeping artifact promotion and model admission blocked.
- `audit_human_infra_c2_longtail_first_batch_source_resolution_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-source-resolution-fresh-review-verdict-register.json` fresh-reviews the 6 source-resolution rows, allows only corrected source re-extraction, and keeps direct artifact fill plus model admission blocked.
- `audit_human_infra_c2_longtail_first_batch_corrected_source_reextraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-corrected-source-reextraction-queue.json` derives exactly the selected corrected source candidates into re-extraction tasks while keeping route-only candidates, artifact promotion and model admission blocked.
- `audit_human_infra_c2_longtail_first_batch_corrected_source_reextraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-corrected-source-reextraction-register.json` covers all 10 corrected re-extraction tasks with required source identity, endpoint, uncertainty, transfer boundary, downgrade and model-position fields while preserving route/index/fulltext blocking and model-admission boundaries.
- `audit_human_infra_c2_longtail_first_batch_corrected_source_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-corrected-source-fresh-review-verdict-register.json` fresh-reviews all 10 corrected extraction outputs, allows only 5 bounded artifact-prep rows, preserves 5 lineage/route/index/fulltext blocked rows and keeps model admission blocked.
- `audit_human_infra_c2_longtail_first_batch_corrected_source_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-corrected-source-reviewed-card-artifact-register.json` promotes exactly the 5 eligible corrected rows into 30 bounded reviewed artifacts, preserves 5 blocked corrected rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_second_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-second-batch-promotion-queue.json` selects 12 non-B1 C2 long-tail domains, binds 24 web-checked candidate sources, preserves required promotion steps and keeps model admission blocked.
- `audit_human_infra_c2_longtail_second_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-second-batch-source-extraction-queue.json` derives the second-batch promotion queue into 24 domain-source extraction tasks with required slots, questions, blocked uses, index links and model-admission boundaries.
- `audit_human_infra_c2_longtail_second_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-second-batch-source-extraction-register.json` completes all 24/24 C2 long-tail second-batch source-context extraction rows with required fields, downgrade triggers, blocked uses and index links.
- `audit_human_infra_c2_longtail_second_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-second-batch-local-review-register.json` locally reviews all 24/24 C2-LT-B2 extraction rows, maps them back to queue/register evidence, preserves blocked uses, and routes only to independent fresh review.
- `audit_human_infra_c2_longtail_second_batch_independent_fresh_review_protocol.py`: verifies that `docs/reference/human-infra-c2-longtail-second-batch-independent-fresh-review-protocol.json` covers all 24 locally reviewed C2-LT-B2 rows in two review batches without embedding verdicts.
- `audit_human_infra_c2_longtail_second_batch_independent_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-second-batch-independent-fresh-review-verdict-register.json` fresh-reviews all 24 C2-LT-B2 rows, allows only 23 bounded artifact-fill rows, preserves 1 downgrade-before-fill row and keeps model admission blocked.
- `audit_human_infra_c2_longtail_second_batch_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-second-batch-reviewed-card-artifact-register.json` promotes exactly the 23 eligible C2-LT-B2 rows into 138 bounded reviewed artifacts, preserves 1 downgrade-before-fill row, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_third_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-promotion-queue.json` selects 12 non-B1/B2 neuro-sensory-cognitive C2 long-tail domains, binds 24 web-checked candidate sources, preserves required promotion steps and keeps model admission blocked.
- `audit_human_infra_c2_longtail_fourth_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-fourth-batch-promotion-queue.json` selects 12 non-B1/B2/B3 metabolic-endocrine-renal-hepatic homeostasis C2 long-tail domains, binds 24 web-checked candidate sources, preserves required promotion steps and keeps model admission blocked.
- `audit_human_infra_c2_longtail_third_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-source-extraction-queue.json` derives the third-batch promotion queue into 24 domain-source extraction tasks with required slots, questions, blocked uses, index links and model-admission boundaries.
- `audit_human_infra_c2_longtail_fourth_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-fourth-batch-source-extraction-queue.json` derives the fourth-batch promotion queue into 24 domain-source extraction tasks with required slots, questions, blocked uses, index links and model-admission boundaries.
- `audit_human_infra_c2_longtail_fourth_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-fourth-batch-source-extraction-register.json` completes all 24/24 C2-LT-B4 source-context extraction rows with required fields, downgrade triggers, blocked uses, absent-abstract/duplicate-lineage flags and index links.
- `audit_human_infra_c2_longtail_fourth_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-fourth-batch-local-review-register.json` locally reviews all 24/24 C2-LT-B4 extraction rows, preserves one duplicate consensus lineage row and three no-abstract fulltext-needed rows, keeps blocked uses complete, and routes only to independent fresh review or source resolution.
- `audit_human_infra_c2_longtail_fourth_batch_source_resolution_register.py`: verifies that `docs/reference/human-infra-c2-longtail-fourth-batch-source-resolution-register.json` covers the four C2-LT-B4 local-review issue rows, prepares eight duplicate-lineage/fulltext-route candidates, preserves blocked uses and keeps model admission blocked.
- `audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-fourth-batch-manual-fulltext-extraction-register.json` covers all eight C2-LT-B4 source-resolution candidates, separates bounded fresh-review candidates from duplicate/route-only/manual-access blocked rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-fourth-batch-manual-fulltext-fresh-review-verdict-register.json` independently reviews all eight C2-LT-B4 manual/fulltext extraction rows, permits only three bounded artifact-prep rows, preserves five blocked/context-only rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-fourth-batch-manual-fulltext-reviewed-card-artifact-register.json` promotes only the three eligible C2-LT-B4 manual/fulltext fresh-review rows into 18 bounded reviewed artifacts, preserves five blocked rows and keeps model admission blocked.
- `audit_human_infra_c2_longtail_fifth_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-fifth-batch-promotion-queue.json` selects 12 non-B1/B2/B3/B4 cellular-maintenance, organelle-communication, molecular-transport, clearance and barrier C2 long-tail domains, binds 24 web/API-checked candidate sources, preserves required promotion steps and keeps model admission blocked.
- `audit_human_infra_c2_longtail_sixth_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-sixth-batch-promotion-queue.json` selects 12 non-B1/B2/B3/B4/B5 intergenerational, reproductive, maternal-newborn-child and pediatric source-maintenance C2 long-tail domains, binds 24 web-checked candidate sources, preserves required promotion steps and keeps model admission blocked.
- `audit_human_infra_c2_longtail_seventh_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-seventh-batch-promotion-queue.json` selects 12 non-B1/B2/B3/B4/B5/B6 cancer-control, survivorship, transplant-safety, organ-donation and bioengineered organ-replacement C2 long-tail domains, binds 24 web-checked candidate sources, preserves required promotion steps and keeps model admission blocked.
- `audit_human_infra_c2_longtail_seventh_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-seventh-batch-source-extraction-queue.json` derives the seventh-batch promotion queue into 24 domain-source extraction tasks with required slots, questions, blocked uses, index links and model-admission boundaries.
- `audit_human_infra_c2_longtail_seventh_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-seventh-batch-source-extraction-register.json` completes all 24/24 C2-LT-B7 source-context extraction rows with required fields, FDA 404 route, dynamic donor-registration, duplicate CDC lineage, screening-boundary, downgrade-trigger, blocked-use and index-link preservation.
- `audit_human_infra_c2_longtail_seventh_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-seventh-batch-local-review-register.json` locally reviews all 24/24 C2-LT-B7 extraction rows, preserves six FDA route, dynamic registration or duplicate-source issue rows, and keeps artifact/model admission blocked.
- `audit_human_infra_c2_longtail_seventh_batch_source_resolution_register.py`: verifies that `docs/reference/human-infra-c2-longtail-seventh-batch-source-resolution-register.json` resolves the six C2-LT-B7 issue rows into seven official FDA, CDC, Donate Life and RegisterMe route candidates while keeping manual/fulltext extraction, fresh review, artifacts and model admission blocked.
- `audit_human_infra_c2_longtail_seventh_batch_manual_fulltext_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-seventh-batch-manual-fulltext-extraction-register.json` covers all seven C2-LT-B7 source-resolution candidates, permits only three bounded fresh-review candidates, blocks four dynamic-registration/access-restricted/duplicate/index rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_seventh_batch_manual_fulltext_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-seventh-batch-manual-fulltext-fresh-review-verdict-register.json` independently reviews all seven C2-LT-B7 manual/fulltext rows, permits only three bounded artifact-prep rows, blocks four dynamic-registration/access-restricted/duplicate/index rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_seventh_batch_manual_fulltext_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-seventh-batch-manual-fulltext-reviewed-card-artifact-register.json` promotes three eligible C2-LT-B7 manual/fulltext fresh-review rows into 18 bounded reviewed artifacts, preserves four blocked rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_eighth_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-eighth-batch-promotion-queue.json` selects 12 non-B1/B2/B3/B4/B5/B6/B7 pain, trauma recovery, neurodevelopment, sensory-communication, autonomic, BCI and living neural computation C2 long-tail domains, binds 24 web-checked candidate sources, preserves required promotion steps and keeps model admission blocked.
- `audit_human_infra_c2_longtail_eighth_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-eighth-batch-source-extraction-queue.json` derives the eighth-batch promotion queue into 24 domain-source extraction tasks with required slots, questions, blocked uses, index links and model-admission boundaries.
- `audit_human_infra_c2_longtail_eighth_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-eighth-batch-source-extraction-register.json` completes all 24/24 C2-LT-B8 source-context extraction rows with required fields, PubMed/fulltext, practice-portal, policy-instrument, BCI governance and living-neural-computation transfer boundaries, downgrade triggers, blocked uses and index links.
- `audit_human_infra_c2_longtail_eighth_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-eighth-batch-local-review-register.json` completes local structural review for all 24/24 C2-LT-B8 extraction rows, preserves seven PubMed/fulltext or living-neural-computation overclaim-risk issue rows, and keeps artifact/model admission blocked.
- `audit_human_infra_c2_longtail_eighth_batch_source_resolution_register.py`: verifies that `docs/reference/human-infra-c2-longtail-eighth-batch-source-resolution-register.json` prepares 19 PubMed, PMC, DOI or corrected-PMID candidates for seven C2-LT-B8 issue rows, preserves three source-ID mismatch rows and keeps manual/fulltext, artifact and model admission blocked.
- `audit_human_infra_c2_longtail_eighth_batch_manual_fulltext_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-eighth-batch-manual-fulltext-extraction-register.json` covers all 19 C2-LT-B8 source-resolution candidates, separates five PMC open-fulltext bounded fresh-review candidates from fourteen PubMed, corrected-PubMed, DOI or route-only blocked rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_eighth_batch_manual_fulltext_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-eighth-batch-manual-fulltext-fresh-review-verdict-register.json` independently reviews all 19 C2-LT-B8 manual/fulltext rows, allows five PMC-readable rows into bounded reviewed-artifact prep, preserves fourteen route-only or publisher-route blocked rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_eighth_batch_manual_fulltext_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-eighth-batch-manual-fulltext-reviewed-card-artifact-register.json` promotes five eligible C2-LT-B8 manual/fulltext fresh-review rows into 30 bounded reviewed artifacts, preserves fourteen blocked rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_ninth_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-ninth-batch-promotion-queue.json` selects 12 non-B1/B2/B3/B4/B5/B6/B7/B8 musculoskeletal, oral, respiratory, immune-aging and environmental-exposure C2 long-tail domains, binds 24 web-checked candidate sources, preserves required promotion steps and keeps model admission blocked.
- `audit_human_infra_c2_longtail_ninth_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-ninth-batch-source-extraction-queue.json` derives the ninth-batch promotion queue into 24 domain-source extraction tasks with required slots, questions, blocked uses, index links and model-admission boundaries.
- `audit_human_infra_c2_longtail_ninth_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-ninth-batch-source-extraction-register.json` completes all 24/24 C2-LT-B9 source-context extraction rows with required fields, access-route notes, downgrade triggers, blocked uses and index links while keeping local review, fresh review, reviewed artifacts and model admission blocked.
- `audit_human_infra_c2_longtail_ninth_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-ninth-batch-local-review-register.json` completes local structural review for all 24/24 C2-LT-B9 extraction rows, preserves two IDSA/Medicaid manual-route issue rows, and keeps artifact/model admission plus advice uses blocked.
- `audit_human_infra_c2_longtail_ninth_batch_source_resolution_register.py`: verifies that `docs/reference/human-infra-c2-longtail-ninth-batch-source-resolution-register.json` resolves the two IDSA/Medicaid manual-route issue rows into 8 route candidates while keeping manual-route extraction, fresh review, reviewed artifacts, advice uses and model admission blocked.
- `audit_human_infra_c2_longtail_ninth_batch_manual_fulltext_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-ninth-batch-manual-fulltext-extraction-register.json` covers all 8 C2-LT-B9 source-resolution candidates, separates four official-page/PDF/related-policy bounded fresh-review candidates from four PubMed, DOI or redirect-provenance blocked rows, and keeps advice uses plus model admission blocked.
- `audit_human_infra_c2_longtail_ninth_batch_manual_fulltext_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-ninth-batch-manual-fulltext-fresh-review-verdict-register.json` independently reviews all 8 C2-LT-B9 manual/fulltext rows, allows four official-page/PDF/related-policy rows into bounded reviewed-artifact prep, preserves four PubMed, DOI or redirect-provenance blocked rows, and keeps advice uses plus model admission blocked.
- `audit_human_infra_c2_longtail_ninth_batch_manual_fulltext_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-ninth-batch-manual-fulltext-reviewed-card-artifact-register.json` promotes four eligible C2-LT-B9 manual/fulltext fresh-review rows into 24 bounded reviewed artifacts, preserves four PubMed, DOI or redirect-provenance blocked rows, and keeps advice uses plus model admission blocked.
- `audit_human_infra_c2_longtail_tenth_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-tenth-batch-promotion-queue.json` selects 12 non-B1/B2/B3/B4/B5/B6/B7/B8/B9 device-infection, home-dialysis, sensory, wound, thermal, burn, diabetic-retinopathy, caregiver, choking and dysphagia C2 long-tail domains, binds 24 web-checked candidate sources, preserves required promotion steps and keeps model admission blocked.
- `audit_human_infra_c2_longtail_tenth_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-tenth-batch-source-extraction-queue.json` derives the tenth-batch promotion queue into 24 domain-source extraction tasks with required slots, questions, blocked uses, index links and model-admission boundaries.
- `audit_human_infra_c2_longtail_tenth_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-tenth-batch-source-extraction-register.json` completes all 24/24 C2-LT-B10 source-context extraction rows with required fields, access-route notes, downgrade triggers, B10-specific blocked uses and index links while keeping local review, fresh review, reviewed artifacts, advice uses and model admission blocked.
- `audit_human_infra_c2_longtail_tenth_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-tenth-batch-local-review-register.json` completes local structural review for all 24/24 C2-LT-B10 extraction rows, keeps zero source-resolution issues at local-review stage, and preserves fresh-review, reviewed-artifact, advice-use and model-admission blocks.
- `audit_human_infra_c2_longtail_tenth_batch_independent_fresh_review_protocol.py`: verifies that `docs/reference/human-infra-c2-longtail-tenth-batch-independent-fresh-review-protocol.json` defines fresh-review fields, verdict taxonomy, two review batches, B10 advice-use blocks and promotion boundaries without storing verdicts or opening reviewed artifacts/model admission.
- `audit_human_infra_c2_longtail_tenth_batch_independent_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-tenth-batch-independent-fresh-review-verdict-register.json` gives all 24 C2-LT-B10 rows bounded fresh-review verdicts while keeping advice use, intervention ranking and model admission blocked.
- `audit_human_infra_c2_longtail_tenth_batch_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-tenth-batch-reviewed-card-artifact-register.json` promotes 24 eligible C2-LT-B10 verdict rows into 144 bounded reviewed artifacts while keeping individual advice and calibrated model admission blocked.
- `audit_human_infra_c2_longtail_eleventh_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-eleventh-batch-promotion-queue.json` selects 12 non-B1/B2/B3/B4/B5/B6/B7/B8/B9/B10 swallowing, dental, contact-lens, diabetic-foot, eye-injury, hearing, noise, pediatric-vision, chemosensory, temporomandibular and vestibular C2 long-tail domains, binds 24 web-checked candidate sources, preserves required promotion steps and keeps model admission blocked.
- `audit_human_infra_c2_longtail_eleventh_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-eleventh-batch-source-extraction-queue.json` derives the eleventh-batch promotion queue into 24 domain-source extraction tasks with required slots, questions, blocked uses, index links and model-admission boundaries.
- `audit_human_infra_c2_longtail_eleventh_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-eleventh-batch-source-extraction-register.json` completes all 24/24 C2-LT-B11 source-context extraction rows with required fields, downgrade triggers, B11-specific blocked uses and index links while keeping local review, fresh review, reviewed artifacts, advice uses and model admission blocked.
- `audit_human_infra_c2_longtail_eleventh_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-eleventh-batch-local-review-register.json` completes local structural review for all 24/24 C2-LT-B11 extraction rows, keeps zero source-resolution issues at local-review stage, and preserves fresh-review, reviewed-artifact, advice-use and model-admission blocks.
- `audit_human_infra_c2_longtail_eleventh_batch_independent_fresh_review_protocol.py`: verifies that `docs/reference/human-infra-c2-longtail-eleventh-batch-independent-fresh-review-protocol.json` defines the independent fresh-review fields, verdict taxonomy, promotion decisions, review batches and B11-specific blocked advice/model uses without embedding verdicts or opening reviewed artifacts.
- `audit_human_infra_c2_longtail_eleventh_batch_independent_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-eleventh-batch-independent-fresh-review-verdict-register.json` completes 24/24 independent fresh-review verdict rows, allows only 21 rows into bounded reviewed-artifact preparation, keeps 3 PubMed-only rows blocked-cannot-evaluate and preserves all advice-use and model-admission blocks.
- `audit_human_infra_c2_longtail_eleventh_batch_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-eleventh-batch-reviewed-card-artifact-register.json` promotes 21 eligible C2-LT-B11 fresh-review rows into 126 bounded reviewed artifacts, preserves 3 PubMed-only blocked rows, and keeps advice uses, intervention ranking, individual prediction and calibrated model admission blocked.
- `audit_human_infra_c2_longtail_twelfth_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-twelfth-batch-promotion-queue.json` selects 12 non-B1/B2/B3/B4/B5/B6/B7/B8/B9/B10/B11 engineered-cell-therapy, organoids/organ-on-chip, synthetic-biology-biosecurity, radiation/nuclear-safety, sterilization/disinfection, bloodborne-exposure, urogenital, allergic/atopic, dry-eye, auditory-processing, dysarthria and apraxia-of-speech C2 long-tail domains, binds 24 web-checked candidate sources, preserves required promotion steps and keeps model admission blocked.
- `audit_human_infra_c2_longtail_twelfth_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-twelfth-batch-source-extraction-queue.json` derives the twelfth-batch promotion queue into 24 source-specific extraction tasks with required exact-claim, endpoint, population, uncertainty, transfer-boundary, downgrade and model-position slots while keeping local review, fresh review, reviewed artifacts, advice uses and model admission blocked.
- `audit_human_infra_c2_longtail_twelfth_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-twelfth-batch-source-extraction-register.json` completes all 24/24 C2-LT-B12 source-context extraction rows with required fields, downgrade triggers, B12-specific blocked uses and index links while keeping local review, fresh review, reviewed artifacts, advice uses and model admission blocked.
- `audit_human_infra_c2_longtail_twelfth_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-twelfth-batch-local-review-register.json` completes local structural review for all 24/24 C2-LT-B12 extraction rows, keeps zero source-resolution issues at local-review stage, and preserves fresh-review, reviewed-artifact, advice-use and model-admission blocks.
- `audit_human_infra_c2_longtail_twelfth_batch_independent_fresh_review_protocol.py`: verifies that `docs/reference/human-infra-c2-longtail-twelfth-batch-independent-fresh-review-protocol.json` derives the 24 locally reviewed C2-LT-B12 rows into independent fresh-review batches with required verdict fields, verdict taxonomy, promotion decisions and B12-specific advice/model blocks, without storing verdicts or opening artifact promotion.
- `audit_human_infra_c2_longtail_twelfth_batch_independent_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-twelfth-batch-independent-fresh-review-verdict-register.json` completes all 24/24 C2-LT-B12 fresh-review verdict rows, allows only 20 rows into bounded reviewed-artifact prep, keeps 4 PubMed-only rows blocked-cannot-evaluate and preserves all advice/model blocks.
- `audit_human_infra_c2_longtail_twelfth_batch_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-twelfth-batch-reviewed-card-artifact-register.json` promotes 20 eligible C2-LT-B12 fresh-review rows into 120 bounded Source/variable/endpoint/uncertainty/transfer/downgrade artifacts while preserving 4 PubMed-only blocked rows and all advice/model blocks.
- `audit_human_infra_c2_longtail_thirteenth_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-thirteenth-batch-promotion-queue.json` selects 12 non-B1/B2/B3/B4/B5/B6/B7/B8/B9/B10/B11/B12 acromegaly, hypogonadism, erectile-dysfunction, kidney-stone, uterine-fibroids, vulvovaginal-pain/infection, otitis-media, speech-sound-disorder, vestibular-migraine, vestibular-neuritis/labyrinthitis, incontinence-associated-dermatitis and psoriasis C2 long-tail domains, binds 24 web-checked candidate sources, preserves required promotion steps and keeps model admission blocked.
- `audit_human_infra_c2_longtail_thirteenth_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-thirteenth-batch-source-extraction-queue.json` derives the thirteenth-batch promotion queue into 24 source-specific extraction tasks with required exact-claim, endpoint, population, uncertainty, transfer-boundary, downgrade and model-position slots while keeping local review, fresh review, reviewed artifacts, advice uses and model admission blocked.
- `audit_human_infra_c2_longtail_thirteenth_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-thirteenth-batch-source-extraction-register.json` completes all 24/24 C2-LT-B13 source-context extraction rows with required fields, 3 PubMed/manual-review route blocks, downgrade triggers, B13-specific blocked uses and index links while keeping local review, fresh review, reviewed artifacts, advice uses and model admission blocked.
- `audit_human_infra_c2_longtail_thirteenth_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-thirteenth-batch-local-review-register.json` completes local structural review for all 24/24 C2-LT-B13 extraction rows, routes 21 non-issue rows only to independent fresh review, preserves 3 PubMed/manual-review source-resolution rows, and keeps artifact/advice/model admission blocked.
- `audit_human_infra_c2_longtail_thirteenth_batch_source_resolution_register.py`: verifies that `docs/reference/human-infra-c2-longtail-thirteenth-batch-source-resolution-register.json` resolves the 3 C2-LT-B13 PubMed/manual-route issue rows into 2 PubMed identity matches and 1 title/domain mismatch with a corrected IAD PMID candidate while keeping re-extraction, fresh review, artifacts and model admission blocked.
- `audit_human_infra_c2_longtail_fourteenth_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-fourteenth-batch-promotion-queue.json` selects the final 16 currently unqueued non-B1/B2/B3/B4/B5/B6/B7/B8/B9/B10/B11/B12/B13 advanced-nuclear, eyeglasses, geriatric oral-health, scald-burn, Huntington, immunization-proof, mold/dampness, pollen/asthma, pregnancy-parental-work, remote-court, reproductive-tissue, skin-supplies, substance-exposure, synthetic-data, synthetic-media and WIC-redemption C2 long-tail domains, binds 32 web-checked candidate sources, preserves required promotion steps and keeps model admission blocked.
- `audit_human_infra_c2_longtail_fourteenth_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-fourteenth-batch-source-extraction-queue.json` derives the final fourteenth-batch promotion queue into 32 source-specific extraction tasks with required exact-claim, endpoint, population, uncertainty, transfer-boundary, downgrade and model-position slots while keeping local review, fresh review, reviewed artifacts, advice uses and model admission blocked.
- `audit_human_infra_c2_longtail_fourteenth_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-fourteenth-batch-source-extraction-register.json` completes all 32/32 C2-LT-B14 source-context extraction rows with required fields, 7 automated 403/manual-review routes, 1 FDA 404/source-resolution route, downgrade triggers, B14-specific blocked uses and index links while keeping local review, fresh review, reviewed artifacts, advice uses and model admission blocked.
- `audit_human_infra_c2_longtail_fourteenth_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-fourteenth-batch-local-review-register.json` completes local structural review for all 32/32 C2-LT-B14 extraction rows, routes 24 non-issue rows only to independent fresh review, preserves 7 automated 403/manual-review plus 1 FDA 404/source-resolution row, and keeps artifact/advice/model admission blocked.
- `audit_human_infra_c2_longtail_sixth_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-sixth-batch-source-extraction-queue.json` derives the sixth-batch promotion queue into 24 domain-source extraction tasks with required slots, questions, blocked uses, index links and model-admission boundaries.
- `audit_human_infra_c2_longtail_sixth_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-sixth-batch-source-extraction-register.json` completes all 24/24 C2-LT-B6 source-context extraction rows with required fields, guideline-route/manual-review/source-lineage boundaries, downgrade triggers, blocked uses and index links.
- `audit_human_infra_c2_longtail_sixth_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-sixth-batch-local-review-register.json` locally reviews all 24/24 C2-LT-B6 extraction rows, preserves seven source-resolution/manual/fulltext/source-lineage issue rows, and keeps artifact/model admission blocked.
- `audit_human_infra_c2_longtail_sixth_batch_source_resolution_register.py`: verifies that `docs/reference/human-infra-c2-longtail-sixth-batch-source-resolution-register.json` resolves the seven C2-LT-B6 issue rows into 19 official-page, PubMed/PMC, OUP/LWW/AAP or CDC route candidates while keeping manual/fulltext extraction, fresh review, artifacts and model admission blocked.
- `audit_human_infra_c2_longtail_sixth_batch_manual_fulltext_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-sixth-batch-manual-fulltext-extraction-register.json` covers all nineteen C2-LT-B6 source-resolution candidates, permits only seven bounded fresh-review candidates, blocks twelve route-only/bibliographic/summary/companion/policy-resource rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_sixth_batch_independent_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-sixth-batch-independent-fresh-review-verdict-register.json` independently reviews the seventeen non-issue C2-LT-B6 source-extraction rows and nineteen manual/fulltext rows, permits twenty-four bounded artifact-prep rows, preserves twelve manual blocked/context-only rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_sixth_batch_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-sixth-batch-reviewed-card-artifact-register.json` promotes twenty-four eligible C2-LT-B6 fresh-review rows into 144 bounded reviewed artifacts, preserves twelve manual blocked/context rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_fifth_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-fifth-batch-source-extraction-queue.json` derives the fifth-batch promotion queue into 24 domain-source extraction tasks with required slots, questions, blocked uses, index links and model-admission boundaries.
- `audit_human_infra_c2_longtail_fifth_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-fifth-batch-source-extraction-register.json` completes all 24/24 C2-LT-B5 source-context extraction rows with required fields, duplicate/no-open-fulltext boundaries, downgrade triggers, blocked uses and index links.
- `audit_human_infra_c2_longtail_fifth_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-fifth-batch-local-review-register.json` locally reviews all 24/24 C2-LT-B5 extraction rows, preserves eight no-open-fulltext/manual-review or duplicate cross-domain source issue rows, keeps blocked uses complete, and routes only to independent fresh review or source resolution.
- `audit_human_infra_c2_longtail_fifth_batch_source_resolution_register.py`: verifies that `docs/reference/human-infra-c2-longtail-fifth-batch-source-resolution-register.json` covers the eight C2-LT-B5 local-review issue rows, prepares fourteen no-open-fulltext/manual-fulltext or duplicate cross-domain route candidates, preserves blocked uses and keeps model admission blocked.
- `audit_human_infra_c2_longtail_fifth_batch_manual_fulltext_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-fifth-batch-manual-fulltext-extraction-register.json` covers all fourteen C2-LT-B5 source-resolution candidates, permits only two bounded fresh-review candidates, blocks twelve route-only/manual-access/duplicate rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_fifth_batch_independent_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-fifth-batch-independent-fresh-review-verdict-register.json` independently reviews the sixteen non-issue C2-LT-B5 source-extraction rows and fourteen manual/fulltext rows, permits seventeen bounded artifact-prep rows, preserves thirteen manual route-only/manual-access/duplicate/context-only blocked rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_fifth_batch_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-fifth-batch-reviewed-card-artifact-register.json` promotes only the seventeen eligible C2-LT-B5 fresh-review rows into 102 bounded reviewed artifacts, preserves thirteen blocked manual rows and keeps model admission blocked.
- `audit_human_infra_c2_longtail_third_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-source-extraction-register.json` completes all 24/24 C2-LT-B3 source-context extraction rows with required fields, downgrade triggers, blocked uses, source-resolution flags and index links.
- `audit_human_infra_c2_longtail_third_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-local-review-register.json` locally reviews all 24/24 C2-LT-B3 extraction rows, preserves five source-resolution/manual-access issue rows, keeps blocked uses complete, and routes only to independent fresh review or source resolution.
- `audit_human_infra_c2_longtail_third_batch_source_resolution_register.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-source-resolution-register.json` covers the five C2-LT-B3 local-review issue rows, prepares seven corrected/split/route-normalized candidates, preserves blocked uses and keeps model admission blocked.
- `audit_human_infra_c2_longtail_third_batch_independent_fresh_review_protocol.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-independent-fresh-review-protocol.json` splits the 24 locally reviewed C2-LT-B3 rows into two fresh-review batches, includes the five source-resolution issue rows, and keeps verdicts, reviewed artifacts and model admission outside the protocol.
- `audit_human_infra_c2_longtail_third_batch_independent_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-independent-fresh-review-verdict-register.json` completes 24/24 C2-LT-B3 fresh-review verdicts, routes five issue rows to corrected-source re-extraction, keeps one row downgrade-before-fill, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_third_batch_corrected_source_reextraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-corrected-source-reextraction-queue.json` derives seven corrected/split/route-normalized source candidates from the five C2-LT-B3 source-resolution-supported issue rows while keeping artifact promotion and model admission blocked.
- `audit_human_infra_c2_longtail_third_batch_corrected_source_reextraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-corrected-source-reextraction-register.json` completes all seven C2-LT-B3 corrected re-extraction tasks with required source identity, endpoint, uncertainty, transfer-boundary, downgrade and model-position fields while preserving route/split blocking and model-admission boundaries.
- `audit_human_infra_c2_longtail_third_batch_corrected_source_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-corrected-source-fresh-review-verdict-register.json` fresh-reviews all seven C2-LT-B3 corrected extraction outputs, allows only six bounded artifact-prep rows, preserves one duplicate/split route blocked row, records the AAO-HNS publisher-route access update and keeps model admission blocked.
- `audit_human_infra_c2_longtail_third_batch_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-reviewed-card-artifact-register.json` promotes 18 original eligible rows and 6 corrected eligible rows into 144 bounded reviewed artifacts, preserves EXT-022 downgrade-before-fill and C2LTB3-CREXT-004 duplicate/split route blocking, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_thirteenth_batch_corrected_source_reextraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-thirteenth-batch-corrected-source-reextraction-queue.json` derives the single corrected IAD PMID 22193141 candidate while keeping mismatched PMID 26428404, artifacts and model admission blocked.
- `audit_human_infra_c2_longtail_thirteenth_batch_corrected_source_reextraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-thirteenth-batch-corrected-source-reextraction-register.json` completes the bounded IAD corrected-source re-extraction with source identity, endpoint, uncertainty, transfer-boundary, downgrade and model-position fields while preserving clinical/product/model blocking.
- `audit_human_infra_c2_longtail_thirteenth_batch_corrected_source_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-thirteenth-batch-corrected-source-fresh-review-verdict-register.json` fresh-reviews the bounded IAD corrected-source extraction, allows only bounded artifact-prep use, and keeps clinical/product/advice/model admission blocked.
- `audit_human_infra_domain_source_specific_extraction_queue.py`: verifies that the 30 domain field rows derive into 93 domain-source reading tasks over 20 source anchors from `docs/reference/human-infra-domain-source-specific-extraction-queue.json`, while keeping calibrated modeling blocked until exact claim, endpoint, population, uncertainty and transfer-boundary fields are extracted.
- `audit_human_infra_domain_source_specific_extraction_register.py`: verifies the completed original 81/93 domain-source extraction rows from `docs/reference/human-infra-domain-source-specific-extraction-register.json`, including source-role decisions, endpoint binding, blocked uses, 12 queued singularity-domain tasks and index links.
- `audit_human_infra_domain_source_card_promotion_queue.py`: verifies that the 81 completed domain-source field rows derive into fresh-review, Source Card, variable-card, endpoint-card, uncertainty-card, transfer-boundary-card and downgrade-check promotion tasks from `docs/reference/human-infra-domain-source-card-promotion-queue.json`, while keeping model admission blocked.
- `audit_human_infra_source_context_local_review_register.py`: verifies that all 20 locally reviewed source anchors match the promotion queue, source evidence, affected tasks, blocked uses and index links from `docs/reference/human-infra-source-context-local-review-register.json`.
- `audit_human_infra_card_promotion_prep_register.py`: verifies that the 81 locally reviewed promotion tasks have prepared Source/variable/endpoint/uncertainty/transfer/downgrade artifact IDs, reviewer questions, blocked uses and index links from `docs/reference/human-infra-card-promotion-prep-register.json`, while keeping independent fresh review and model admission blocked.
- `audit_human_infra_independent_fresh_review_protocol.py`: verifies that the independent fresh-review protocol in `docs/reference/human-infra-independent-fresh-review-protocol.json` batches the 81 prepared artifact packs, matches prep-register source counts, preserves verdict taxonomy and keeps verdicts outside the protocol artifact.
- `audit_human_infra_independent_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-independent-fresh-review-verdict-register.json` records cumulative independent fresh-review verdict batches over reviewed source anchors and promotion packets, while preserving blocked uses, source-role boundaries and index links.
- `audit_human_infra_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-reviewed-card-artifact-register.json` promotes all 81 fresh-reviewed promotion packets into 486 reviewed Source/variable/endpoint/uncertainty/transfer-boundary/downgrade artifact entities while keeping model admission and individual-use claims blocked.
- `audit_human_infra_future_boundary_route_card_register.py`: verifies that `docs/reference/human-infra-future-boundary-route-card-register.json` covers future waiting, biological stasis, neuro-identity continuity and AI-enabled acceleration route cards with required gate dimensions, abort gates and blocked model admission.
- `audit_human_infra_falsifier_source_card_backfill.py`: verifies that current paper strong claims and C1/C2 priority-domain falsifier rows have Source Card anchor backfill, evidence roles, supported-use boundaries and transfer boundaries from `docs/reference/human-infra-falsifier-source-card-backfill.json`.
- `audit_human_infra_falsifier_source_card_extraction.py`: verifies that all current source anchors from `docs/reference/human-infra-falsifier-source-card-extraction.json` map to exact source identity, Human Infra domains, paper claims, model positions, transfer boundaries and the human-readable source-note pack.
- `check_repository.py`: verifies required files, required directories, temporary filename cleanup, Python cache cleanup, and local Markdown links.
- `audit_repository_privacy.py`: scans Git-tracked files for local user paths, hostnames, sensitive filenames, private-key markers, and high-confidence credential formats without printing matched values.
- `validate_history_timeline.py`: validates the 永生史 history timeline machine contract, including required files, JSON Schema shape, event/source uniqueness, enum values, and governance contract path alignment.
- `update_domain_doc_contracts.py`: regenerates standard README/AGENTS metadata, research-skeleton, maintenance-contract, and agent-workflow blocks for every formal research domain from the possibility-space classification table.

Reusable tool package:

- `arxiv-html-paper/`: templates, consumer contract, governance docs, and usage notes for the arXiv HTML papers reuse kit.

Key arXiv reuse documents:

- [arxiv-html-paper/CONTRACT.md](arxiv-html-paper/CONTRACT.md): stable consumption contract.
- [arxiv-html-paper/CONSUMER_GUIDE.md](arxiv-html-paper/CONSUMER_GUIDE.md): guide for other projects.
- [arxiv-html-paper/GOVERNANCE.md](arxiv-html-paper/GOVERNANCE.md): maintenance and compatibility governance.
- [arxiv-html-paper/MAINTENANCE.md](arxiv-html-paper/MAINTENANCE.md): operational runbook.

## Commands

From the repository root:

```bash
python3 tools/check_repository.py
python3 tools/audit_repository_privacy.py
python3 tools/audit_public_product_boundary.py
python3 tools/audit_core_claim_evidence_matrix.py
python3 tools/audit_human_infra_maturity_gap_register.py
python3 tools/audit_human_infra_model_admission_contract.py
python3 tools/audit_human_infra_model_admission_candidate_registry.py
python3 tools/audit_human_infra_brain_body_interface_protocol_register.py
python3 tools/audit_human_infra_minimal_sufficient_body_claim_evidence_matrix.py
python3 tools/audit_human_infra_audience_claim_map.py
python3 tools/audit_human_infra_domain_falsifier_coverage.py
python3 tools/audit_human_infra_domain_claim_evidence_matrix.py
python3 tools/audit_human_infra_domain_source_card_field_extraction.py
python3 tools/audit_human_infra_c2_longtail_coverage_register.py
python3 tools/audit_human_infra_c2_longtail_first_batch_promotion_queue.py
python3 tools/audit_human_infra_c2_longtail_first_batch_source_extraction_queue.py
python3 tools/audit_human_infra_c2_longtail_first_batch_source_extraction_register.py
python3 tools/audit_human_infra_c2_longtail_first_batch_local_review_register.py
python3 tools/audit_human_infra_c2_longtail_first_batch_independent_fresh_review_protocol.py
python3 tools/audit_human_infra_c2_longtail_first_batch_independent_fresh_review_verdict_register.py
python3 tools/audit_human_infra_c2_longtail_first_batch_reviewed_card_artifact_register.py
python3 tools/audit_human_infra_domain_source_specific_extraction_queue.py
python3 tools/audit_human_infra_domain_source_specific_extraction_register.py
python3 tools/audit_human_infra_domain_source_card_promotion_queue.py
python3 tools/audit_human_infra_source_context_local_review_register.py
python3 tools/audit_human_infra_card_promotion_prep_register.py
python3 tools/audit_human_infra_independent_fresh_review_protocol.py
python3 tools/audit_human_infra_independent_fresh_review_verdict_register.py
python3 tools/audit_human_infra_falsifier_source_card_backfill.py
python3 tools/audit_human_infra_falsifier_source_card_extraction.py
python3 tools/update_domain_doc_contracts.py
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir build/arxiv-html-paper-preview/public
make claim-matrix-audit
make public-product-boundary
make maturity-gap-audit
make model-admission-contract-audit
make model-admission-candidate-registry-audit
make quantitative-capability-ladder-audit
make domain-to-model-bridge-audit
make brain-body-interface-protocol-audit
make minimal-sufficient-body-claim-matrix-audit
make l4-model-readiness-blocker-matrix-audit
make l4-unblock-execution-plan-audit
make l4-evidence-intake-register-audit
make l4-evidence-packet-validator-audit
make l4-validation-calibration-reporting-contract-audit
make research-standards-source-anchor-audit
make l4-validation-calibration-report-execution-register-audit
make audience-claim-map-audit
make domain-falsifier-audit
make domain-claim-matrix-audit
make domain-field-extraction-audit
make c2-longtail-coverage-audit
make c2-longtail-first-batch-promotion-audit
make c2-longtail-first-batch-source-extraction-audit
make c2-longtail-first-batch-source-extraction-register-audit
make c2-longtail-first-batch-local-review-audit
make c2-longtail-first-batch-independent-fresh-review-protocol-audit
make c2-longtail-first-batch-independent-fresh-review-verdict-audit
make c2-longtail-first-batch-reviewed-card-artifact-audit
make c2-longtail-first-batch-blocked-source-resolution-audit
make c2-longtail-first-batch-source-resolution-fresh-review-verdict-audit
make c2-longtail-first-batch-corrected-source-reextraction-queue-audit
make c2-longtail-first-batch-corrected-source-reextraction-register-audit
make c2-longtail-first-batch-corrected-source-fresh-review-verdict-audit
make c2-longtail-first-batch-corrected-source-reviewed-card-artifact-audit
make c2-longtail-second-batch-promotion-audit
make c2-longtail-second-batch-source-extraction-audit
make c2-longtail-second-batch-source-extraction-register-audit
make c2-longtail-second-batch-local-review-audit
make c2-longtail-second-batch-independent-fresh-review-protocol-audit
make c2-longtail-second-batch-independent-fresh-review-verdict-audit
make c2-longtail-second-batch-reviewed-card-artifact-audit
make c2-longtail-third-batch-promotion-audit
make c2-longtail-third-batch-source-extraction-audit
make c2-longtail-third-batch-source-extraction-register-audit
make c2-longtail-third-batch-local-review-audit
make c2-longtail-third-batch-source-resolution-audit
make c2-longtail-third-batch-independent-fresh-review-protocol-audit
make c2-longtail-third-batch-independent-fresh-review-verdict-audit
make c2-longtail-third-batch-corrected-source-reextraction-queue-audit
make c2-longtail-third-batch-corrected-source-reextraction-register-audit
make c2-longtail-third-batch-corrected-source-fresh-review-verdict-audit
make c2-longtail-third-batch-reviewed-card-artifact-audit
make c2-longtail-thirteenth-batch-corrected-source-reextraction-queue-audit
make c2-longtail-thirteenth-batch-corrected-source-reextraction-register-audit
make c2-longtail-thirteenth-batch-corrected-source-fresh-review-verdict-audit
make c2-longtail-fourth-batch-promotion-audit
make c2-longtail-fourth-batch-source-extraction-audit
make c2-longtail-fourth-batch-source-extraction-register-audit
make c2-longtail-fourth-batch-local-review-audit
make c2-longtail-fourth-batch-source-resolution-audit
make c2-longtail-fourth-batch-manual-fulltext-extraction-audit
make c2-longtail-fourth-batch-manual-fulltext-fresh-review-verdict-audit
make c2-longtail-fourth-batch-manual-fulltext-reviewed-card-artifact-audit
make c2-longtail-fifth-batch-promotion-audit
make c2-longtail-sixth-batch-promotion-audit
make c2-longtail-seventh-batch-promotion-audit
make c2-longtail-seventh-batch-source-extraction-audit
make c2-longtail-seventh-batch-source-extraction-register-audit
make c2-longtail-eighth-batch-promotion-audit
make c2-longtail-eighth-batch-source-extraction-audit
make c2-longtail-eighth-batch-source-extraction-register-audit
make c2-longtail-eighth-batch-local-review-audit
make c2-longtail-eighth-batch-source-resolution-audit
make c2-longtail-eighth-batch-manual-fulltext-extraction-audit
make c2-longtail-eighth-batch-manual-fulltext-fresh-review-verdict-audit
make c2-longtail-eighth-batch-manual-fulltext-reviewed-card-artifact-audit
make c2-longtail-ninth-batch-promotion-audit
make c2-longtail-ninth-batch-source-extraction-audit
make c2-longtail-ninth-batch-source-extraction-register-audit
make c2-longtail-ninth-batch-local-review-audit
make c2-longtail-ninth-batch-source-resolution-audit
make c2-longtail-ninth-batch-manual-fulltext-extraction-audit
make c2-longtail-ninth-batch-manual-fulltext-fresh-review-verdict-audit
make c2-longtail-ninth-batch-manual-fulltext-reviewed-card-artifact-audit
make c2-longtail-tenth-batch-promotion-audit
make c2-longtail-tenth-batch-source-extraction-audit
make c2-longtail-tenth-batch-source-extraction-register-audit
make c2-longtail-tenth-batch-local-review-audit
make c2-longtail-tenth-batch-independent-fresh-review-protocol-audit
make c2-longtail-tenth-batch-independent-fresh-review-verdict-audit
make c2-longtail-tenth-batch-reviewed-card-artifact-audit
make c2-longtail-eleventh-batch-promotion-audit
make c2-longtail-eleventh-batch-source-extraction-audit
make c2-longtail-eleventh-batch-source-extraction-register-audit
make c2-longtail-eleventh-batch-local-review-audit
make c2-longtail-eleventh-batch-independent-fresh-review-protocol-audit
make c2-longtail-eleventh-batch-independent-fresh-review-verdict-audit
make c2-longtail-eleventh-batch-reviewed-card-artifact-audit
make c2-longtail-twelfth-batch-promotion-audit
make c2-longtail-twelfth-batch-source-extraction-audit
make c2-longtail-twelfth-batch-source-extraction-register-audit
make c2-longtail-twelfth-batch-local-review-audit
make c2-longtail-twelfth-batch-independent-fresh-review-protocol-audit
make c2-longtail-twelfth-batch-independent-fresh-review-verdict-audit
make c2-longtail-twelfth-batch-reviewed-card-artifact-audit
make c2-longtail-thirteenth-batch-promotion-audit
make c2-longtail-thirteenth-batch-source-extraction-audit
make c2-longtail-thirteenth-batch-local-review-audit
make c2-longtail-thirteenth-batch-source-resolution-audit
make c2-longtail-fourteenth-batch-promotion-audit
make c2-longtail-fourteenth-batch-source-extraction-audit
make c2-longtail-fourteenth-batch-source-extraction-register-audit
make c2-longtail-fourteenth-batch-local-review-audit
make c2-longtail-seventh-batch-local-review-audit
make c2-longtail-seventh-batch-source-resolution-audit
make c2-longtail-seventh-batch-manual-fulltext-extraction-audit
make c2-longtail-seventh-batch-manual-fulltext-fresh-review-verdict-audit
make c2-longtail-seventh-batch-manual-fulltext-reviewed-card-artifact-audit
make c2-longtail-sixth-batch-source-extraction-audit
make c2-longtail-sixth-batch-source-extraction-register-audit
make c2-longtail-sixth-batch-local-review-audit
make c2-longtail-sixth-batch-source-resolution-audit
make c2-longtail-sixth-batch-manual-fulltext-extraction-audit
make c2-longtail-sixth-batch-independent-fresh-review-verdict-audit
make c2-longtail-sixth-batch-reviewed-card-artifact-audit
make c2-longtail-fifth-batch-source-extraction-audit
make c2-longtail-fifth-batch-source-extraction-register-audit
make c2-longtail-fifth-batch-local-review-audit
make c2-longtail-fifth-batch-source-resolution-audit
make c2-longtail-fifth-batch-manual-fulltext-extraction-audit
make c2-longtail-fifth-batch-independent-fresh-review-verdict-audit
make c2-longtail-fifth-batch-reviewed-card-artifact-audit
make domain-source-queue-audit
make domain-source-extraction-audit
make domain-source-promotion-audit
make source-context-local-review-audit
make card-promotion-prep-audit
make independent-fresh-review-protocol-audit
make independent-fresh-review-verdict-audit
make falsifier-source-audit
make falsifier-source-extraction-audit
make check
make clean
```
