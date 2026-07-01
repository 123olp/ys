# ADR 0097: Add Ninety-Third-Wave Swallowing Feeding Execution Domains

## Status

Accepted.

## Context

The existing `swallowing-dysphagia-aspiration-nutrition/` domain captures the broad claim that swallowing is the interface between external food/water/medication resources, airway protection, nutrition, hydration, dignity, and care burden.

That parent domain was too coarse for Human Infra's transcendental domain mapping. Swallowing and feeding continuity fails through different mechanisms: oral-pharyngeal swallow safety, esophageal transport, aspiration pneumonia risk, acute choking, standardized texture/thickened liquid interfaces, enteral feeding, pediatric feeding development, post-stroke screening and recovery, neurodegenerative dysphagia, and mealtime assistance/dignity. These are not interchangeable because they have different time windows, anatomical stages, care-team interfaces, device dependencies, evidence sources, and safety boundaries.

## Decision

Add ten swallowing feeding execution continuity domains:

- `oropharyngeal-dysphagia-swallow-safety-continuity/`
- `esophageal-dysphagia-motility-obstruction-continuity/`
- `aspiration-pneumonia-airway-protection-continuity/`
- `choking-foreign-body-airway-risk-continuity/`
- `texture-modified-diet-thickened-liquid-continuity/`
- `enteral-feeding-tube-nutrition-continuity/`
- `pediatric-feeding-swallowing-development-continuity/`
- `post-stroke-dysphagia-screening-recovery-continuity/`
- `neurodegenerative-dysphagia-nutrition-continuity/`
- `feeding-assistance-mealtime-dignity-continuity/`

Each domain receives a `README.md` and `AGENTS.md`, and the root README, domain indexes, research atlas, radar, domain map, ethics boundaries, applications/literature map, and repository check script are updated.

## Consequences

- Human Infra can now distinguish broad dysphagia from concrete swallow-stage, airway, feeding, nutrition-route, child-development, stroke-recovery, neurodegenerative, and mealtime-care failure modes.
- Swallowing domains can be modeled as task-resource constraints: safe swallow mechanics, esophageal passage, airway protection, acute choking risk, texture communication, non-oral nutrition, child feeding development, post-stroke recovery, progressive disease planning, and assisted mealtime dignity.
- The domains remain research and governance maps, not diagnosis, swallow test interpretation, diet prescription, tube-feeding recommendation, feeding technique generation, emergency instruction, school/service eligibility determination, prognosis, or individual medical guidance.

## Source Signals

- NIDCD dysphagia resources.
- ASHA adult dysphagia and pediatric feeding/swallowing practice materials.
- IDDSI texture and liquid-thickness framework.
- AHA/ASA stroke dysphagia screening signals.
- ASPEN/ESPEN enteral nutrition materials.
- CMS paid feeding assistant and long-term-care materials.
- MedlinePlus public medical materials for swallowing disorders, choking, and feeding tubes.
