# ADR 0108: Add One-Hundred-Third Wave Vector Animal Pest Exposure Execution Domains

## Status

Accepted.

## Context

Human Infra 已经有 `vector-borne-disease-environmental-control/`、`animal-health-zoonotic-interface-one-health/`、`household-cleaning-disinfection-pest-control-continuity/`、`water-sanitation-hygiene-continuity/` 和 `chemical-safety-poison-control-toxicology/`。

这些域覆盖病媒传播环境控制、One Health、家庭卫生和化学安全的上位框架。但主体持续性的执行层还缺少更薄的场景入口：蚊虫叮咬、蜱虫叮咬、狂犬病暴露、犬咬伤、鼠害、床虱、毒咬蜇伤、特定宠物/后院家禽沙门氏菌、虱疥和农药标签/中毒连接。

这些问题通常不是单一疾病，而是把居住、睡眠、学校、旅行、户外劳动、照护、宠物共处和灾后恢复空间重新定价的摩擦系统。

## Decision

新增第 103 波 10 个 vector / animal / pest exposure execution continuity domains：

- `mosquito-bite-arbovirus-prevention-continuity/`
- `tick-bite-lyme-rickettsial-prevention-continuity/`
- `rabies-exposure-bite-pep-continuity/`
- `dog-bite-community-injury-prevention-continuity/`
- `rodent-infestation-hantavirus-plague-continuity/`
- `bed-bug-infestation-sleep-housing-continuity/`
- `venomous-bites-stings-envenomation-continuity/`
- `reptile-amphibian-backyard-poultry-salmonella-continuity/`
- `lice-scabies-school-shelter-infestation-continuity/`
- `pesticide-label-exposure-poison-control-continuity/`

这些域共同覆盖小型生物风险和控制工具如何进入主体的行动、睡眠、住房、学校、旅行、工作和恢复系统。

## Boundaries

- 不提供个体诊断、治疗、用药、暴露后决策、疫苗安排、抗毒素建议、急救步骤、驱虫产品推荐、灭虫操作、农药使用、动物捕捉处置、法律责任判断或旅行许可。
- 不替代 CDC、EPA、NPIC、Poison Help、地方公共卫生、毒物中心、医疗机构、兽医、动物控制、学校、住房机构或职业安全机构。
- 不把地图、病例、病媒监测、宠物资料、产品标签或 AI 输出写成个体感染概率、医疗决策、资产判断或现场操作。
- 不重复 `vector-borne-disease-environmental-control/` 的总论功能；新增域只承载执行薄片和具体暴露链路。

## Source Signals

- CDC Mosquitoes: https://www.cdc.gov/mosquitoes/
- CDC Ticks: https://www.cdc.gov/ticks/
- CDC Lyme Disease: https://www.cdc.gov/lyme/
- CDC Rabies: https://www.cdc.gov/rabies/
- CDC Healthy Pets: https://www.cdc.gov/healthy-pets/
- CDC Hantavirus: https://www.cdc.gov/hantavirus/
- CDC Plague: https://www.cdc.gov/plague/
- CDC Bed Bugs: https://www.cdc.gov/bed-bugs/
- CDC Head Lice: https://www.cdc.gov/lice/about/head-lice.html
- CDC Scabies: https://www.cdc.gov/scabies/
- EPA Bed Bugs: https://www.epa.gov/bedbugs
- EPA Safe Pest Control: https://www.epa.gov/safepestcontrol
- EPA Pesticide Labels: https://www.epa.gov/pesticide-labels
- National Pesticide Information Center: https://npic.orst.edu/
- Poison Help: https://www.poisonhelp.org/
- AVMA Dog Bite Prevention: https://www.avma.org/resources-tools/pet-owners/dog-bite-prevention

## Consequences

- 病媒/动物/虫害/农药风险从上位环境控制补齐到主体执行层。
- `domain-map.md`、`research-domain-atlas.md`、`research-domain-radar.md`、`ethics-and-safety-boundaries.md` 和 `applications-and-literature.md` 需要同步索引。
- `tools/check_repository.py` 必须把新增域 README/AGENTS 和本 ADR 纳入结构检查。
- 后续 source card 应优先整理官方来源、禁止用途、暴露链路和与既有总域的上下游边界。
