# ADR 0109: Add One-Hundred-Fourth Wave Plant Algae Fungi Outdoor Biological Exposure Domains

## Status

Accepted.

## Context

Human Infra 已经有慢性环境暴露、病媒/动物/虫害、食品安全、水资源、生态系统服务、户外公共空间和职业暴露等上位域。

但主体持续性的先验条件还缺少一组更薄的自然生物暴露执行入口：花粉过敏、漆酚植物、有害藻华、野生蘑菇、有毒植物、入侵物种、霉菌毒素、休闲水病原、贝类毒素和园林园艺户外复合伤害。

这些问题不是单一疾病，也不是单纯生态背景；它们会把空气、水、植物、食物、户外劳动、公共空间和恢复环境重新变成行动摩擦、急性中毒、慢性暴露或季节性损耗。

## Decision

新增第 104 波 10 个 plant / algae / fungi / outdoor biological exposure execution continuity domains：

- `pollen-allergen-asthma-outdoor-activity-continuity/`
- `poison-ivy-oak-sumac-urushiol-exposure-continuity/`
- `harmful-algal-bloom-cyanotoxin-water-recreation-continuity/`
- `toxic-mushroom-foraging-poisoning-continuity/`
- `poisonous-plant-childcare-household-exposure-continuity/`
- `invasive-species-human-health-access-continuity/`
- `mycotoxin-food-crop-storage-safety-continuity/`
- `recreational-water-illness-beach-lake-access-continuity/`
- `shellfish-biotoxin-harmful-algal-bloom-food-continuity/`
- `landscaping-horticulture-worker-equipment-injury-continuity/`

这些域共同覆盖植物、藻类、真菌、水域病原和户外生态维护如何进入主体的呼吸、皮肤、食品、水域活动、儿童照护、职业安全和恢复空间。

## Boundaries

- 不提供诊断、治疗、用药、急救、解毒、免疫治疗、食用许可、植物/蘑菇鉴定、采食建议、水质个案判断、采样解释、藻华识别、农药/除草剂操作、设备作业、PPE 选型、施工流程、旅游许可、食品合规或个体风险判断。
- 不替代 CDC、EPA、FDA、USDA、NOAA、OSHA、NIOSH、Poison Help、地方公共卫生、水务、食品监管、农业推广、职业健康、医疗、兽医、学校、托育或环境监测机构。
- 不把照片、地图、花粉预报、AQI、水色、检测值、AI 识别、民间经验或社交媒体信息写成个人诊疗、食用、作业、游泳、采捕或现场安全许可。
- 不重复 `biodiversity-ecosystem-services-resilience/`、`water-sanitation-hygiene-continuity/`、`food-safety-contamination-control/` 或 `occupational-exposure-industrial-hygiene/` 的总论功能；新增域只承载薄片化暴露链路和禁止用途边界。

## Source Signals

- CDC Asthma: https://www.cdc.gov/asthma/
- EPA Asthma: https://www.epa.gov/asthma
- CDC/NIOSH Poisonous Plants: https://www.cdc.gov/niosh/topics/plants/
- CDC Harmful Algal Blooms: https://www.cdc.gov/harmful-algal-blooms/
- EPA Harmful Algal Blooms: https://www.epa.gov/habs
- NOAA Harmful Algal Blooms: https://oceanservice.noaa.gov/hazards/hab/
- FDA Bad Bug Book: https://www.fda.gov/food/foodborne-pathogens/bad-bug-book-second-edition
- USDA National Invasive Species Information Center: https://www.invasivespeciesinfo.gov/
- CDC Healthy Swimming: https://www.cdc.gov/healthy-swimming/
- FDA National Shellfish Sanitation Program: https://www.fda.gov/food/federalstate-food-programs/national-shellfish-sanitation-program-nssp
- OSHA Landscaping and Horticultural Services: https://www.osha.gov/landscaping
- Poison Help: https://www.poisonhelp.org/

## Consequences

- 自然生物暴露从生态/环境/食品/职业总论补齐到主体执行层。
- `domain-map.md`、`research-domain-atlas.md`、`research-domain-radar.md`、`ethics-and-safety-boundaries.md` 和 `applications-and-literature.md` 需要同步索引。
- `tools/check_repository.py` 必须把新增域 README/AGENTS 和本 ADR 纳入结构检查。
- 后续 source card 应优先整理官方来源、暴露链路、不可操作化边界和与既有总域的上下游关系。
