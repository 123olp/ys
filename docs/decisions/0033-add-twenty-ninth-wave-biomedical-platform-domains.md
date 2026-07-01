# 0033. Add Twenty-Ninth-Wave Biomedical Platform Domains

Date: 2026-06-30

## Status

Accepted.

## Context

Human Infra 已经有 `cellular-reprogramming/`、`regenerative-medicine/`、`cancer-control/`、`longevity-evidence/` 和多个生理维护域，但还缺少一组能够把“未来医学技术如何改变生命路径概率分布”拆成平台变量的研究域。

山中因子只是其中一个研究域。继续做先验追问时，会遇到更多同级条件：基因治疗能否安全递送，生物年龄是否可验证，多组学是否能形成主体状态底图，工程细胞能否成为活体药物，类器官/组织芯片能否降低转化失败，关键器官能否被替换或工程化。

这些方向不能只归入 `cellular-reprogramming/`、`regenerative-medicine/`、`clinical-trials-regulatory-science-translation/`、`measurement-feedback/` 或 `blood-organ-tissue-biovigilance-transplantation/`。它们各自有独立平台、变量、证据体系、失败模式和安全边界。

## Decision

Add six formal biomedical platform domains:

- `domains/c6-local-unlocking/gene-therapy-genome-editing-delivery-safety/`
- `domains/c2-source-maintenance/biological-age-clocks-biomarker-validation/`
- `domains/c3-generation-engine/multiomics-personal-baseline-systems-biology/`
- `domains/c2-source-maintenance/engineered-cell-therapy-regenerative-platforms/`
- `domains/c2-source-maintenance/organoids-organ-on-chip-disease-models/`
- `domains/c2-source-maintenance/xenotransplantation-bioengineered-organ-replacement/`

Update root navigation, docs navigation, reference maps, radar, ethics boundaries, changelog and repository checks so the new domains are discoverable and validated.

## Consequences

- Human Infra can now separate direct intervention platforms, measurement platforms, modeling platforms and organ replacement platforms.
- Future quantitative modeling can express these domains as distinct variables: editing accuracy, delivery safety, biological age validity, multi-omics baseline quality, engineered cell controllability, preclinical model fidelity and organ replacement availability.
- Safety boundaries must explicitly prohibit lab protocols, clinical advice, DIY biology, genetic enhancement instructions, human experimentation, organ procurement instructions and overclaiming early-stage results.
- Future evidence work can organize Source Cards around FDA, NIH, NIA, NCATS, ISSCR, HRSA/OPTN and peer-reviewed biomedical literature.

## Non-Goals

- No gene editing design, vector construction, cell manufacturing, organoid culture, xenotransplantation procedure, dose, protocol, surgery, animal handling or self-experimentation guidance.
- No claim that any platform currently provides general anti-aging, immortality or broad human enhancement.
- No individual biomarker interpretation, disease diagnosis, therapy choice, trial enrollment, transplant advice or medical decision support.
- No replacement for `clinical-trials-regulatory-science-translation/`; the new domains define platform variables while clinical translation still owns human evidence pathways.
