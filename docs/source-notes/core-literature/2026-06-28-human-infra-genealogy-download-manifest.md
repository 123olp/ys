# Human Infra Genealogy Download Manifest

Access date: 2026-06-28

Local cache root:

```text
.research/literature/human-infra-genealogy/
```

## Download Policy

- Use legal public sources only: arXiv, PMC article pages, publisher open PDFs, author pages, institution pages, public course copies, public repository copies, and official download APIs.
- Do not bypass paywalls, login gates, Cloudflare challenges, PMC browser proof-of-work pages, or institutional subscription restrictions.
- Prefer canonical publisher, arXiv, PMC, author, institution, or official project sources.
- When the canonical PDF is blocked but a public copy exists, cache it and mark the source class.
- When only metadata is accessible, create a `.url` marker and keep the source as metadata-only.

## Prepared Scope

This pack covers the papers explicitly needed for the current Human Infra genealogy spine:

1. Core 12 reading spine.
2. Adjunct genealogy sources named in the first map.
3. Research narrative and reproducible visualization methods.

It does not attempt to download every possible longevity, AI, BCI, or public health paper.

## Core 12 Pack

| ID | Branch | Source | Canonical URL | Local cache | Status | Human Infra mapping |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | Personal informatics | Li, Dey, Forlizzi, 2010, A Stage-Based Model of Personal Informatics Systems | https://www.cs.cmu.edu/~jhm/Readings/2010-ianli-chi-stage-based-model.pdf | `.research/literature/human-infra-genealogy/core-12/a1-li-2010-stage-based-personal-informatics.pdf` | PDF downloaded from CMU course copy | Observation-reflection-action workflow |
| A2 | Lived informatics | Epstein et al., A Lived Informatics Model of Personal Informatics | https://pmc.ncbi.nlm.nih.gov/articles/PMC12435389/ | `.research/literature/human-infra-genealogy/core-12/a2-epstein-2015-lived-informatics-author.pdf`; `.research/literature/human-infra-genealogy/core-12/a2-epstein-2015-lived-informatics.html` | Author PDF downloaded; PMC HTML cached | Self-tracking in lived routines |
| A3 | Aging biology | Lopez-Otin et al., 2013, The Hallmarks of Aging | https://pmc.ncbi.nlm.nih.gov/articles/PMC3836174/ | `.research/literature/human-infra-genealogy/core-12/a3-lopez-otin-2013-hallmarks-of-aging.html` | HTML cached; Cell PDF blocked by challenge; PMC PDF endpoint returns browser check | Biological state variables |
| A4 | Biological age | Horvath, 2013, DNA methylation age of human tissues and cell types | https://genomebiology.biomedcentral.com/articles/10.1186/gb-2013-14-10-r115 | `.research/literature/human-infra-genealogy/core-12/a4-horvath-2013-dna-methylation-age-springer.pdf`; `.research/literature/human-infra-genealogy/core-12/a4-horvath-2013-dna-methylation-age.html` | Springer PDF downloaded; PMC HTML cached | Observation process and biological age proxy |
| A5 | Mortality risk marker | Lu et al., 2019, DNA methylation GrimAge strongly predicts lifespan and healthspan | https://pmc.ncbi.nlm.nih.gov/articles/PMC6366976/ | `.research/literature/human-infra-genealogy/core-12/a5-lu-2019-grimage-unc-repository-copy.pdf`; `.research/literature/human-infra-genealogy/core-12/a5-lu-2019-grimage.html` | UNC repository PDF downloaded; PMC HTML cached | Hazard and lifespan association |
| A6 | Survival analysis | Kaplan, Meier, 1958, Nonparametric Estimation from Incomplete Observations | https://www.tandfonline.com/doi/abs/10.1080/01621459.1958.10501452 | `.research/literature/human-infra-genealogy/core-12/a6-kaplan-meier-1958-public-course-copy.pdf`; `.research/literature/human-infra-genealogy/core-12/a6-kaplan-meier-1958-metadata.url` | Stanford public course PDF downloaded; publisher metadata retained | Survival curve method ancestor |
| A7 | Survival analysis | Cox, 1972, Regression Models and Life-Tables | https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1972.tb00899.x | `.research/literature/human-infra-genealogy/core-12/a7-cox-1972-public-course-copy.pdf`; `.research/literature/human-infra-genealogy/core-12/a7-cox-1972-metadata.url` | McGill public course PDF downloaded; publisher metadata retained | Hazard model method ancestor |
| A8 | Causal inference | Hernan et al., 2022, Target Trial Emulation | https://pubmed.ncbi.nlm.nih.gov/36508210/ | `.research/literature/human-infra-genealogy/core-12/a8-hernan-2022-target-trial-public-mirror.pdf`; `.research/literature/human-infra-genealogy/core-12/a8-hernan-2022-target-trial-metadata.url` | Public mirror PDF downloaded; PubMed/JAMA metadata retained | Intervention question framing |
| A8-open | Causal inference reading copy | Matthews et al., 2022, Causal inference from observational data and target trial emulation | https://pmc.ncbi.nlm.nih.gov/articles/PMC9910387/ | `.research/literature/human-infra-genealogy/core-12/a8-open-matthews-2022-causal-inference-target-trial-emulation.html` | Open PMC HTML cached; Oxford PDF blocked by challenge | Open reading substitute for target trial method |
| A9 | Human digital twin | Mulder et al., 2022, Dynamic Digital Twin | https://www.jmir.org/2022/9/e35675/ | `.research/literature/human-infra-genealogy/core-12/a9-mulder-2022-dynamic-digital-twin.pdf` | JMIR PDF downloaded | Dynamic life-course simulation |
| A10 | Extended mind | Clark, Chalmers, 1998, The Extended Mind | https://consc.net/papers/extended.html | `.research/literature/human-infra-genealogy/core-12/a10-clark-chalmers-1998-extended-mind-public-copy.pdf`; `.research/literature/human-infra-genealogy/core-12/a10-clark-chalmers-1998-extended-mind.html` | Public PDF downloaded; author HTML cached | Cognitive extension and tool boundary |
| A11 | BCI ethics | Burwell, Sample, Racine, 2017, Ethical aspects of brain computer interfaces | https://bmcmedethics.biomedcentral.com/articles/10.1186/s12910-017-0220-y | `.research/literature/human-infra-genealogy/core-12/a11-burwell-2017-bci-ethics-springer.pdf`; `.research/literature/human-infra-genealogy/core-12/a11-burwell-2017-bci-ethics.html` | Springer PDF downloaded; PMC HTML cached | Consent, identity, neuroethics boundary |
| A12 | Visualization | Bostock, Ogievetsky, Heer, 2011, D3: Data-Driven Documents | http://vis.stanford.edu/files/2011-D3-InfoVis.pdf | `.research/literature/human-infra-genealogy/core-12/a12-bostock-2011-d3-data-driven-documents.pdf` | Stanford PDF downloaded | Interactive research visualization |

## Adjunct Genealogy Pack

| Branch | Source | Canonical URL | Local cache | Status |
| --- | --- | --- | --- | --- |
| Personal identity | Persson, 2013, Parfit on Personal Identity | https://onlinelibrary.wiley.com/doi/10.1111/theo.12092 | `.research/literature/human-infra-genealogy/adjunct/persson-2013-parfit-personal-identity-metadata.url` | Metadata-only; Wiley PDF not publicly accessible in this environment |
| Personal identity root | Parfit, 1971, Personal Identity | https://www.jstor.org/stable/2184309 | `.research/literature/human-infra-genealogy/adjunct/parfit-1971-personal-identity-public-course-copy.pdf` | Public course PDF downloaded as genealogy substitute |
| Mind uploading | Wiley, Koene, 2015, The Fallacy of Favoring Gradual Replacement Mind Uploading Over Scan-and-Copy | https://arxiv.org/abs/1504.06320 | `.research/literature/human-infra-genealogy/adjunct/wiley-koene-2015-mind-uploading-gradual-replacement.pdf` | arXiv PDF downloaded |
| Human digital twin | Pascual et al., 2023, A Systematic Review on Human Modeling | https://arxiv.org/abs/2302.03593 | `.research/literature/human-infra-genealogy/adjunct/pascual-2023-human-digital-twin-systematic-review.pdf` | arXiv PDF downloaded |
| Human digital twin | Digital twins as global learning health and disease models, 2025 | https://link.springer.com/article/10.1186/s13073-025-01435-7 | `.research/literature/human-infra-genealogy/adjunct/genome-medicine-2025-digital-twins-global-learning-models.pdf`; `.research/literature/human-infra-genealogy/adjunct/genome-medicine-2025-digital-twins-metadata.url` | Springer PDF downloaded; metadata retained |
| Human-AI collaboration | Human-AI Symbiosis | https://arxiv.org/abs/2103.09990 | `.research/literature/human-infra-genealogy/adjunct/akhatkulov-2021-human-ai-symbiosis.pdf` | arXiv PDF downloaded |
| BCI use studies | Kogel et al., 2019, Using brain-computer interfaces: a scoping review of studies employing social research methods | https://bmcmedethics.biomedcentral.com/articles/10.1186/s12910-019-0354-1 | `.research/literature/human-infra-genealogy/adjunct/kogel-2019-using-brain-computer-interfaces.pdf` | Springer PDF downloaded |
| AI misuse | Brundage et al., 2018, The Malicious Use of Artificial Intelligence | https://arxiv.org/abs/1802.07228 | `.research/literature/human-infra-genealogy/adjunct/brundage-2018-malicious-use-ai.pdf` | arXiv PDF downloaded |
| AI risk taxonomy | AI Risk Repository, 2024 | https://arxiv.org/abs/2408.12622 | `.research/literature/human-infra-genealogy/adjunct/ai-risk-repository-2024.pdf` | arXiv PDF downloaded |
| Catastrophic AI risks | An Overview of Catastrophic AI Risks, 2023 | https://arxiv.org/abs/2306.12001 | `.research/literature/human-infra-genealogy/adjunct/bengio-2023-catastrophic-ai-risks.pdf` | arXiv PDF downloaded |
| Intelligence augmentation | Engelbart, 1962, Augmenting Human Intellect | https://www.dougengelbart.org/pubs/augment-3906.html | `.research/literature/human-infra-genealogy/adjunct/engelbart-1962-augmenting-human-intellect.html` | Author/project HTML cached |

## Methods And Research Narrative Pack

| Branch | Source | Canonical URL | Local cache | Status |
| --- | --- | --- | --- | --- |
| Literate programming | Knuth, 1984, Literate Programming | https://academic.oup.com/comjnl/article/27/2/97/343244 | `.research/literature/human-infra-genealogy/methods/knuth-1984-literate-programming.pdf` | Tufts public course PDF downloaded |
| Computational narrative | Granger, Perez, 2021, Jupyter: Thinking and Storytelling With Code and Data | https://www.computer.org/csdl/magazine/cs/2021/02/09387490/1smCZM9XKSY | `.research/literature/human-infra-genealogy/methods/granger-perez-2021-jupyter-thinking-storytelling.pdf` | IEEE Computer Society API PDF downloaded |

## Counts

- Core 12 targets: 12 sources plus 1 open target-trial substitute.
- Core PDF coverage: 11 of 12 targets have a PDF or public PDF copy; A3 remains HTML-only because the Cell PDF is challenged in this environment.
- Adjunct genealogy sources: 11 sources, including 1 metadata-only source and 1 substitute root text.
- Methods sources: 2 PDFs.
- Local cache after this run: 35 files, about 48 MB.

## Remaining Blockers

| Source | Blocker | Current fallback |
| --- | --- | --- |
| A3, Lopez-Otin et al., The Hallmarks of Aging | Cell PDF is behind Cloudflare challenge; PMC PDF endpoint returns browser check HTML | PMC article HTML cached |
| Persson, Parfit on Personal Identity | Wiley full text not publicly accessible in this environment | Wiley metadata marker plus Parfit 1971 public course copy |
| Matthews et al., target trial emulation substitute | Oxford PDF endpoint is blocked by challenge | PMC article HTML cached |

## Next Actions

1. Split the Source Card pack into single-card files after first close reading.
2. Promote stable claims to `docs/reference/applications-and-literature.md`.
3. Map model-ready sources to `docs/reference/life-path-prediction-model-contract.md`.
4. Use D3, Knuth, and Jupyter papers to refine `/paper/` and future model-lab visualization design.
