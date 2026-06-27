# Human Infra Core 12 Source Card Pack

Card status: draft pack
Access date: 2026-06-28
Local cache root: `.research/literature/human-infra-genealogy/core-12/`

This pack is the first Human Infra genealogy reading spine. It converts the user's proposed 12-paper list into project-facing source cards.

## A1 - Li et al., 2010, Personal Informatics Stage Model

Metadata: paper; Li, Dey, Forlizzi; 2010; URL: https://www.cs.cmu.edu/~jhm/Readings/2010-ianli-chi-stage-based-model.pdf; local path: `.research/literature/human-infra-genealogy/core-12/a1-li-2010-stage-based-personal-informatics.pdf`.

One-sentence use: Provides the observation-to-action workflow for Human Infra self-data systems.

| Field | Notes |
| --- | --- |
| Human Infra mapping | Personal informatics, observation layer, feedback loop |
| Model position | Observation process `O_t`; action policy `pi`; state update through reflection and behavior |
| Evidence role | Method and HCI workflow support |
| Transfer boundary | Does not prove that tracking improves health or lifespan; it models system stages and user tasks |
| Repository action | Use in source-card workflow and future personal data pipeline design |

Key extracts: personal informatics systems require preparation, collection, integration, reflection, and action; Human Infra should not treat data capture as enough by itself.

## A2 - Epstein et al., Lived Informatics

Metadata: paper; Epstein et al.; URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12435389/; local paths: `.research/literature/human-infra-genealogy/core-12/a2-epstein-2015-lived-informatics-author.pdf`, `.research/literature/human-infra-genealogy/core-12/a2-epstein-2015-lived-informatics.html`.

One-sentence use: Keeps self-tracking grounded in daily routines, interruptions, motivation, and lived context.

| Field | Notes |
| --- | --- |
| Human Infra mapping | Personal informatics as lived practice |
| Model position | Observation process `O_t`; adherence and missingness; action policy feasibility |
| Evidence role | Method, qualitative model, narrative boundary |
| Transfer boundary | Does not provide mortality endpoints or causal effects |
| Repository action | Use to prevent overly mechanical tracking language |

Key extracts: self-tracking happens inside life, not outside it; Human Infra must model burden, breakdown, repair, and context.

## A3 - Lopez-Otin et al., 2013, The Hallmarks of Aging

Metadata: review paper; Lopez-Otin et al.; 2013; URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3836174/; local path: `.research/literature/human-infra-genealogy/core-12/a3-lopez-otin-2013-hallmarks-of-aging.html`.

One-sentence use: Provides a biological variable map for aging-related state degradation.

| Field | Notes |
| --- | --- |
| Human Infra mapping | Biological substrate of subject continuity |
| Model position | State variable `X_t`; state transition `P(X_{t+1} | X_t, A_t)` |
| Evidence role | Mechanism and review support |
| Transfer boundary | Hallmarks are not direct intervention prescriptions or guaranteed longevity levers |
| Repository action | Map hallmarks into candidate biological state variables |

Key extracts: aging should be represented as multiple interacting damage, response, and maintenance processes rather than a single scalar.

## A4 - Horvath, 2013, DNA Methylation Age

Metadata: paper; Horvath; 2013; URL: https://genomebiology.biomedcentral.com/articles/10.1186/gb-2013-14-10-r115; local paths: `.research/literature/human-infra-genealogy/core-12/a4-horvath-2013-dna-methylation-age-springer.pdf`, `.research/literature/human-infra-genealogy/core-12/a4-horvath-2013-dna-methylation-age.html`.

One-sentence use: Introduces biological age as an observation proxy rather than a literal lifespan counter.

| Field | Notes |
| --- | --- |
| Human Infra mapping | Biomarker and biological age observation layer |
| Model position | Observation process `O_t`; latent biological state estimate |
| Evidence role | Biomarker method and association support |
| Transfer boundary | Methylation age is not an individual death-date predictor and not automatically an intervention target |
| Repository action | Use in biomarker section of life-path model contract |

Key extracts: biological age proxies can support model observation, but their meaning depends on tissue, cohort, calibration, and endpoint.

## A5 - Lu et al., 2019, GrimAge

Metadata: paper; Lu et al.; 2019; URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC6366976/; local paths: `.research/literature/human-infra-genealogy/core-12/a5-lu-2019-grimage-unc-repository-copy.pdf`, `.research/literature/human-infra-genealogy/core-12/a5-lu-2019-grimage.html`.

One-sentence use: Connects methylation-derived biomarkers to lifespan, healthspan, and mortality-risk associations.

| Field | Notes |
| --- | --- |
| Human Infra mapping | Mortality-risk biomarker layer |
| Model position | Hazard `lambda(t | X_t, A_t)`; lifespan and healthspan association |
| Evidence role | Association and endpoint prediction support |
| Transfer boundary | Predictive association is not proof that changing the biomarker causally extends life |
| Repository action | Use as example of hazard-linked biomarker with caution language |

Key extracts: Human Infra should separate prognostic value from causal intervention value.

## A6 - Kaplan and Meier, 1958, Survival Curve Estimation

Metadata: paper; Kaplan and Meier; 1958; URL: https://www.tandfonline.com/doi/abs/10.1080/01621459.1958.10501452; local paths: `.research/literature/human-infra-genealogy/core-12/a6-kaplan-meier-1958-public-course-copy.pdf`, `.research/literature/human-infra-genealogy/core-12/a6-kaplan-meier-1958-metadata.url`.

One-sentence use: Provides the survival-curve ancestor for modeling life-path distributions under censoring.

| Field | Notes |
| --- | --- |
| Human Infra mapping | Statistical foundation of lifespan distribution |
| Model position | Survival function `S(t)`; censoring; event-time data |
| Evidence role | Method standard |
| Transfer boundary | Method does not explain causality or define biological mechanisms |
| Repository action | Use in quantitative model glossary and visualization design |

Key extracts: Human Infra should represent survival as a curve and distribution, not a single deterministic date.

## A7 - Cox, 1972, Proportional Hazards

Metadata: paper; Cox; 1972; URL: https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1972.tb00899.x; local paths: `.research/literature/human-infra-genealogy/core-12/a7-cox-1972-public-course-copy.pdf`, `.research/literature/human-infra-genealogy/core-12/a7-cox-1972-metadata.url`.

One-sentence use: Provides the hazard-function ancestor for linking variables to event risk over time.

| Field | Notes |
| --- | --- |
| Human Infra mapping | Hazard modeling layer |
| Model position | Hazard `lambda(t | X_t, A_t)`; covariate-risk relationship |
| Evidence role | Method standard |
| Transfer boundary | Proportional hazards assumptions may fail; method does not establish intervention effects by itself |
| Repository action | Use in model contract and chart vocabulary |

Key extracts: The correct question is not "does X extend life" but "how does X enter the risk function, under what assumptions?"

## A8 - Hernan et al., 2022, Target Trial Emulation

Metadata: paper; Hernan et al.; 2022; URL: https://pubmed.ncbi.nlm.nih.gov/36508210/; local paths: `.research/literature/human-infra-genealogy/core-12/a8-hernan-2022-target-trial-public-mirror.pdf`, `.research/literature/human-infra-genealogy/core-12/a8-hernan-2022-target-trial-metadata.url`. Open reading substitute: Matthews et al., https://pmc.ncbi.nlm.nih.gov/articles/PMC9910387/, local path `.research/literature/human-infra-genealogy/core-12/a8-open-matthews-2022-causal-inference-target-trial-emulation.html`.

One-sentence use: Turns "would this intervention help?" into an explicit causal design problem.

| Field | Notes |
| --- | --- |
| Human Infra mapping | Causal evaluation and intervention governance |
| Model position | Action policy `pi`; state transition; hazard under intervention |
| Evidence role | Method standard for causal inference |
| Transfer boundary | Requires careful eligibility, time zero, assignment, follow-up, outcome, estimand, and analysis choices |
| Repository action | Use as gate before treating observational signals as interventions |

Key extracts: Human Infra should emulate the target trial before interpreting observational data as if it were causal evidence.

## A9 - Mulder et al., 2022, Dynamic Digital Twin

Metadata: paper; Mulder et al.; 2022; URL: https://www.jmir.org/2022/9/e35675/; local path: `.research/literature/human-infra-genealogy/core-12/a9-mulder-2022-dynamic-digital-twin.pdf`.

One-sentence use: Connects diagnosis, prediction, prevention, treatment, and life-course modeling into a dynamic twin frame.

| Field | Notes |
| --- | --- |
| Human Infra mapping | Human digital twin and life-course simulation |
| Model position | State variable; transition; observation; policy simulation |
| Evidence role | Framework and system architecture support |
| Transfer boundary | Digital twin is a modeling aspiration, not proof of clinical validity or personal prediction accuracy |
| Repository action | Use for model architecture and dashboard vocabulary |

Key extracts: A useful twin must stay dynamic, longitudinal, and tied to diagnosis, prevention, treatment, and prediction workflows.

## A10 - Clark and Chalmers, 1998, The Extended Mind

Metadata: philosophy paper; Clark and Chalmers; 1998; URL: https://consc.net/papers/extended.html; local paths: `.research/literature/human-infra-genealogy/core-12/a10-clark-chalmers-1998-extended-mind-public-copy.pdf`, `.research/literature/human-infra-genealogy/core-12/a10-clark-chalmers-1998-extended-mind.html`.

One-sentence use: Provides the philosophical basis for treating tools, notes, memory systems, and AI assistants as parts of the subject's functional cognitive system under conditions.

| Field | Notes |
| --- | --- |
| Human Infra mapping | Cognition, memory externalization, AI/tool augmentation |
| Model position | Effective time; cognitive state; action policy; option value |
| Evidence role | Narrative and conceptual support |
| Transfer boundary | Does not imply every external tool is part of the self; coupling, availability, trust, and integration matter |
| Repository action | Use in genealogy and value-lens documents |

Key extracts: Human Infra should define tool integration conditions, not simply call every AI tool "extension."

## A11 - Burwell et al., 2017, BCI Ethics

Metadata: scoping review; Burwell, Sample, Racine; 2017; URL: https://bmcmedethics.biomedcentral.com/articles/10.1186/s12910-017-0220-y; local paths: `.research/literature/human-infra-genealogy/core-12/a11-burwell-2017-bci-ethics-springer.pdf`, `.research/literature/human-infra-genealogy/core-12/a11-burwell-2017-bci-ethics.html`.

One-sentence use: Supplies neurotechnology boundary conditions for identity, autonomy, consent, privacy, and responsibility.

| Field | Notes |
| --- | --- |
| Human Infra mapping | BCI, neural data, body boundary, governance |
| Model position | Governance; safety boundary; future option value |
| Evidence role | Ethics review and risk taxonomy |
| Transfer boundary | Does not validate any BCI intervention; it frames ethical concerns and oversight needs |
| Repository action | Use in ethics and safety boundary updates |

Key extracts: Neural tools require stronger consent, identity, agency, and privacy boundaries than ordinary productivity tools.

## A12 - Bostock et al., 2011, D3: Data-Driven Documents

Metadata: paper; Bostock, Ogievetsky, Heer; 2011; URL: http://vis.stanford.edu/files/2011-D3-InfoVis.pdf; local path: `.research/literature/human-infra-genealogy/core-12/a12-bostock-2011-d3-data-driven-documents.pdf`.

One-sentence use: Provides the technical lineage for Human Infra's interactive research visualizations.

| Field | Notes |
| --- | --- |
| Human Infra mapping | Web model lab, interactive explanation, evidence visualization |
| Model position | Visualization of `S(t)`, hazard, state transitions, thresholds, and uncertainty-free public demo curves |
| Evidence role | Tooling support |
| Transfer boundary | Visualization does not make a model valid; it only makes assumptions inspectable |
| Repository action | Use in Web implementation and visualization toolkit |

Key extracts: Data-bound documents make models inspectable when the data, marks, interactions, and narrative remain linked.

## Synthesis

The first pack establishes seven connected layers:

```text
personal informatics
  -> lived tracking
  -> biological state variables
  -> biomarkers and hazard associations
  -> survival and causal methods
  -> human digital twin simulation
  -> cognitive/tool extension and governance
  -> interactive research visualization
```

Human Infra should treat this as a genealogy, not a proof chain. The papers support vocabulary, modeling positions, and workflow gates; they do not prove any specific longevity intervention, AI tool, or BCI pathway is safe or effective.
