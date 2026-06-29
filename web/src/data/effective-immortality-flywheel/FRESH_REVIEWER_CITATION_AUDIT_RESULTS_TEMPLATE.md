# Fresh Reviewer Citation Audit Results Template

Source protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`

Use this JSON template as a field reference only. Do not copy it directly to `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`.

Use `web/src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/INDEX.md` to review one citation context at a time.

Completed reviewer result files belong in `web/src/data/effective-immortality-flywheel/fresh-reviewer-context-packets/results/CTX*.json`. Run `npm run assemble:fresh-reviewer-results` to create the canonical results ledger with per-file hashes.

## Required Verdict Fields

| Field | Allowed values |
| --- | --- |
| reference_existence | PASS, FAIL, UNCERTAIN |
| safe_use_support | SUPPORTS, WEAK, WRONG |
| forbidden_use_violation | NONE, POSSIBLE, PRESENT |
| required_action | KEEP, SOFTEN, REWRITE, REMOVE, REPLACE_SOURCE |
| resolution_status | RESOLVED, ACCEPTED_WITH_BOUNDARY, PENDING_FIX, UNRESOLVED, NOT_REVIEWED |

## Queue

| Priority | Context | Risk | Source group | References |
| ---: | --- | --- | --- | --- |
| 1 | CTX2 | HIGH | Grossman Health Capital; WHO HALE; NICE QALY | grossman1972healthcapital, niceEconomicEvaluation, whohale7752 |
| 2 | CTX3 | MEDIUM | Hallmarks of Aging; GrimAge; Cognitive Reserve | lopezotin2013hallmarks, lu2019grimage, stern2012cognitiveReserve |
| 3 | CTX5 | MEDIUM | Human Capital; Social Capital; Social Relationships Mortality | coleman1988socialCapital, holtlunstad2010social, mincer1974humanCapital |
| 4 | CTX7 | MEDIUM | Generative AI at Work; Noy and Zhang; GitHub Copilot; Jagged Technological Frontier | brynjolfsson2025generative, dellacqua2026jagged, noy2023productivity, peng2023copilot |
| 5 | CTX10 | MEDIUM | Apple Heart Study; Personal Informatics; Lived Informatics; Dynamic Digital Twin | epstein2015lived, li2010personalInformatics, mulder2022dynamicDigitalTwin, perez2019appleHeart |
| 6 | CTX11 | MEDIUM | Extended Mind; Engelbart; Cognition in the Wild | burwell2017bciEthics, clark1998extended, engelbart1962augmenting, hutchins1995cognition |
| 7 | CTX12 | MEDIUM | Capability Approach; WHO SDOH; WHO Primary Health Care | robeyns2021capability, whoSdhPhc |
| 8 | CTX9 | MEDIUM | Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI | clinicaltrialsGov, clinicaltrialsGovApi, consortAi2020, gradeHandbook, hernan2022targetTrial, probastAi2025, robins2000marginalStructural, spiritAi2020, tripodAi2024, tripodProbast, whoIctrp |
| 9 | CTX1 | LOW | Kaplan-Meier 1958; Cox 1972 | cox1972regression, kaplan1958incomplete |
| 10 | CTX4 | LOW | Deliberate Practice; Law of Practice; Self-Regulated Learning; Feedback Intervention Theory | ericsson1993deliberatePractice, kluger1996feedback, newell1981lawPractice, zimmerman2002selfRegulated |
| 11 | CTX6 | LOW | TAM; UTAUT; Diffusion of Innovations | davis1989tam, rogers2003diffusion, venkatesh2003utaut |
| 12 | CTX8 | LOW | NIST AI RMF; Guidelines for Human-AI Interaction; NASA-TLX; Automation taxonomy | amershi2019hai, burwell2017bciEthics, dellacqua2026jagged, nasaTlx, nist2023airmf, parasuraman2000automation |
