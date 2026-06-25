# Life-Path Prediction Model Contract

## Purpose

This contract defines the first quantitative model boundary for Human Infra. It specifies how factors, technologies, resources, institutions, environments, and personal actions may be represented as interventions that alter a subject's future life-path probability distribution.

It is a model contract, not an implementation. Any future script, data model, simulation, report, or prediction product must conform to this contract before making quantitative claims.

## Scope

Included:

- lifespan, healthspan, effective time, subjective time, relative time, and future option value;
- intervention modeling for medical, AI, resource, environmental, institutional, and behavioral factors;
- survival, multi-state, causal, simulation, and uncertainty requirements;
- evidence admission rules for quantitative claims.

Excluded:

- medical diagnosis or individualized treatment recommendation;
- immortality claims;
- insurance, employment, credit, policing, or coercive ranking use;
- deterministic prediction of a person's death date;
- automated life decisions without human review, consent, and appeal.

## Canonical Question

Every quantitative claim must answer this form:

```text
For subject or population P,
under time horizon H,
intervention A,
compared with comparator C,
through mechanism M,
using evidence E,
with uncertainty U,
how does A change the distribution of life paths?
```

Invalid forms:

```text
Technology T extends life.
Factor X is good for longevity.
Metric Y improved, therefore lifespan improved.
AI predicts this person will live until date D.
```

## Core Variables

| Symbol | Meaning | Notes |
| --- | --- | --- |
| `i` | subject or population unit | Individual, cohort, subgroup, or simulated agent |
| `t` | time | Calendar time, biological age, subjective time, or proper time must be specified |
| `X_t` | observed state variables | Measured biological, cognitive, resource, tool, environment, and recovery variables |
| `U_t` | unobserved or latent variables | Frailty, unknown disease state, latent risk, selection factors |
| `A_t` | intervention or action | Technology, medicine, behavior, resource change, policy, tool, or environment change |
| `O_t` | observation process | Screening, wearable, lab, imaging, AI diagnosis, data availability |
| `Q_t` | health quality or capability weight | Used for effective time and health-adjusted time |
| `T` | death time | Random variable, not a fixed known endpoint |
| `D_k` | event time for failure mode `k` | Disease, disability, accident, crisis, institutional exclusion |
| `lambda_k(t)` | cause-specific hazard | Risk of failure mode `k` at time `t` |
| `S(t)` | survival function | `P(T > t)` |
| `pi` | strategy or policy | Rule for choosing `A_t` from observed state history |

## Variable Classes

Every candidate intervention must declare which variable classes it can plausibly affect.

| Class | Examples | Contract requirement |
| --- | --- | --- |
| Biological | inflammation, metabolism, immunity, cell damage, cancer risk, cardiovascular risk | Must separate mechanism, biomarker, disease endpoint, and mortality endpoint |
| Cognitive | judgment, learning, attention, memory, decision quality | Must state whether effect is capability, productivity, safety, or health-mediated |
| Resource | wealth, time, care access, information access, housing, legal access | Must state whether effect operates through care, recovery, risk exposure, or option value |
| Tool | AI, automation, screening, diagnosis, drug discovery | Must separate observation improvement from outcome improvement |
| Environment | pollution, accident risk, workload, violence, social support | Must define exposure, duration, dose, and reversibility |
| Recovery | sleep, repair, rehabilitation, stress recovery, redundancy | Must define whether effect changes state level or transition rate |

## Intervention Operator

Human Infra treats a technology or factor as an operator on a life-path distribution:

```text
A_t: P(omega | history_t) -> P'(omega | history_t)
```

Operationally, an intervention can affect at least one of four model locations:

```text
1. State update:
   P(X_{t+1} | X_t, A_t)

2. Event hazard:
   lambda_k(t | X_t, A_t)

3. Observation process:
   P(O_t | X_t, A_t)

4. Action policy:
   pi(A_t | history_t)
```

If a claim cannot identify at least one location, it remains qualitative speculation.

## Outcome Functions

The model may report only outcomes whose definition is explicit.

```text
Lifespan:
  E[T], median(T), P(T > t)

Healthspan:
  time alive above a defined health or capability threshold

Effective time:
  integral over survival, health quality, and capability weight

Subjective time:
  integral over experienced time weighting psi(t)

Relative time:
  mapping between subject proper time and external reference time

Future option value:
  expected future ability to choose among meaningful strategies
```

Recommended canonical form:

```text
effective_time = integral S(t) * Q_t * C_t dt
```

Where `Q_t` is health quality and `C_t` is capability or agency weight. Any use of `Q_t` or `C_t` must state measurement source and uncertainty.

## Required Causal Contract

Every quantitative intervention claim must define:

| Field | Requirement |
| --- | --- |
| Population | Who the claim applies to |
| Time zero | When follow-up begins |
| Intervention | What changes, at what dose/intensity, for how long |
| Comparator | No intervention, standard care, alternative technology, or baseline exposure |
| Outcome | Mortality, disease onset, disability, health quality, effective time, subjective time, option value |
| Follow-up | Time horizon and censoring rules |
| Causal graph | Main confounders, mediators, colliders, and selection mechanisms |
| Estimand | Average treatment effect, subgroup effect, hazard ratio, survival difference, expected effective time gain, or other |
| Evidence basis | RCT, observational, mechanistic, animal, computational, expert prior, or mixed evidence |
| Uncertainty | Confidence interval, credible interval, sensitivity analysis, or scenario range |

Claims without comparator, time zero, outcome, and uncertainty must not be presented as quantitative estimates.

## Model Families And Allowed Use

| Model family | Use | Required guardrail |
| --- | --- | --- |
| Survival analysis | Event time, mortality, disease onset, disability onset | Check proportionality, censoring, competing risks, and follow-up bias |
| Multi-state model | Health, disease, disability, recovery, death transitions | Define states, transition matrix, absorbing states, and reversibility |
| Dynamic health impact model | Risk-factor changes across population over time | Declare risk-factor distributions, disease links, lag, and competing risks |
| Microsimulation | Individual or cohort life-path simulation | Calibrate baseline risks and validate aggregate outputs |
| Causal model | Intervention effect estimation | Define target trial, confounding, positivity, selection, and sensitivity analysis |
| Dynamic decision model | Sequential strategy evaluation | Avoid claiming optimal policy without strong validation and ethical review |
| Effective-time model | Quality/capability-adjusted time | Declare weights, value assumptions, and non-health capability dimensions |

## Evidence Strength

Evidence must be graded separately for mechanism, intermediate outcome, clinical endpoint, mortality, safety, and transferability.

| Grade | Meaning | Permitted wording |
| --- | --- | --- |
| G0 | Conceptual or mechanistic hypothesis | "May affect a pathway" |
| G1 | Animal, in vitro, or computational support | "Shows preclinical signal" |
| G2 | Human biomarker or short-term outcome | "May improve intermediate marker in studied context" |
| G3 | Disease endpoint or functional endpoint | "Has evidence for clinical or functional outcome in population P" |
| G4 | Mortality, healthspan, or long-term event evidence | "Changes event risk or survival estimate under stated conditions" |
| G5 | Replicated, long-term, externally validated evidence | "Robustly changes modeled life-path distribution within stated scope" |

No grade permits personal treatment advice.

## Output Contract

Any future model card, report, or API output must include:

```yaml
model_claim:
  population:
  time_horizon:
  intervention:
  comparator:
  affected_variables:
  causal_path:
  model_location:
    state_transition:
    hazard:
    observation:
    policy:
  outcomes:
    lifespan:
    healthspan:
    effective_time:
    subjective_time:
    relative_time:
    option_value:
  evidence_grade:
  uncertainty:
  assumptions:
  risks:
  opportunity_cost:
  prohibited_uses:
  review_status:
```

## Non-Negotiable Boundaries

- Do not output a deterministic death date.
- Do not convert a biomarker-only improvement into a lifespan claim.
- Do not hide uncertainty behind a single score.
- Do not merge animal lifespan evidence with human mortality evidence.
- Do not use the model for coercive employment, insurance, credit, policing, or social ranking.
- Do not recommend prescription drugs, invasive procedures, neural interventions, or unsafe experiments.
- Do not treat relative-time or subjective-time paths as biological immortality.

## Source Traceability

- DYNAMO-HIA dynamic health impact modeling. <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0033317>
- Future Elderly Model microsimulation. <https://schaeffer.usc.edu/data/future-elderly-model/>
- Target trial emulation. <https://pubmed.ncbi.nlm.nih.gov/26994063/>
- Marginal structural models and causal inference for time-varying treatments. <https://pubmed.ncbi.nlm.nih.gov/10955408/>
- OHDSI OMOP common data model. <https://www.ohdsi.org/data-standardization/>
- OHDSI patient-level prediction. <https://www.ohdsi.org/web/wiki/doku.php?id=projects:workgroups:patient-level_prediction>
- NICE economic evaluation. <https://www.nice.org.uk/process/pmg36/chapter/economic-evaluation-2>
- WHO HALE metadata. <https://www.who.int/data/gho/indicator-metadata-registry/imr-details/7752>
- TRIPOD statement. <https://www.tripod-statement.org/>
- PROBAST. <https://www.probast.org/>

## Maintenance

- Owner: Human Infra maintainers.
- Review trigger: any quantitative model, simulation output, prediction claim, data standard, or intervention ranking.
- Related files: [Life-Path Prediction Model](../explanations/life-path-prediction-model.md), [Prediction Model Governance](life-path-prediction-model-governance.md), [Evidence Policy](evidence-policy.md), [Review Checklists](review-checklists.md).
