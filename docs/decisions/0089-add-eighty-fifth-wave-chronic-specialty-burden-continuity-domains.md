# 0089 Add Eighty-Fifth Wave Chronic Specialty Burden Continuity Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra 已经覆盖急性救援、时间关键急症、预防筛查和生活史预防，但仍需要把一组高频、长期、反复消耗有效时间和主体行动能力的慢性专科病程拆成独立研究域。

这些对象不能只放进高层 `pain-suffering-control/`、`musculoskeletal-integrity/`、`immune-maintenance/`、`gastrointestinal-barrier-absorption/`、`renal-hepatic-clearance/`、`endocrine-hormonal-regulation/`、`blood-oxygen-hemostasis/`、`respiratory-oxygenation/` 或 `skin-barrier-wound-healing/`，因为每个对象都有独立服务入口、病程变量、证据边界、生活参与结果和禁止用途。

## Decision

新增第八十五波慢性专科负担与功能恢复连续性研究域：

- `chronic-pain-functional-restoration-continuity/`
- `low-back-pain-spine-function-continuity/`
- `osteoarthritis-joint-function-continuity/`
- `autoimmune-rheumatic-disease-inflammatory-burden-continuity/`
- `inflammatory-bowel-disease-digestive-continuity/`
- `chronic-liver-disease-masld-mash-continuity/`
- `thyroid-disease-endocrine-function-continuity/`
- `iron-deficiency-anemia-oxygen-carrying-continuity/`
- `asthma-copd-maintenance-control-continuity/`
- `allergic-atopic-disease-immunologic-burden-continuity/`

## Consequences

- 第八十五波把慢性疼痛、脊柱、关节、自身免疫炎症、消化、肝脏、甲状腺、贫血、慢性气道和过敏/特应性疾病独立出来。
- 每个域必须保持非诊疗边界，不提供个体诊断、检查判读、药物、康复动作、设备、手术、饮食、保险或法律建议。
- 这些域的共同抽象是：慢性病程通过疼痛、疲劳、炎症、氧输送、呼吸、吸收、代谢和环境限制持续降低有效时间密度与行动质量。

## Source Signals

- CDC chronic pain and opioid prescribing signals: https://www.cdc.gov/chronic-pain/ and https://www.cdc.gov/mmwr/volumes/71/rr/rr7103a1.htm
- NIAMS back pain, osteoarthritis, rheumatoid arthritis and lupus signals: https://www.niams.nih.gov/health-topics/back-pain, https://www.niams.nih.gov/health-topics/osteoarthritis, https://www.niams.nih.gov/health-topics/rheumatoid-arthritis and https://www.niams.nih.gov/health-topics/lupus
- NIDDK IBD, MASLD/MASH, cirrhosis and thyroid disease signals: https://www.niddk.nih.gov/health-information/digestive-diseases/crohns-disease, https://www.niddk.nih.gov/health-information/liver-disease/nafld-nash and https://www.niddk.nih.gov/health-information/endocrine-diseases/hypothyroidism
- NHLBI anemia, asthma and COPD signals: https://www.nhlbi.nih.gov/health/anemia, https://www.nhlbi.nih.gov/health/asthma and https://www.nhlbi.nih.gov/health/copd
- NIAID and NIAMS allergic / atopic disease signals: https://www.niaid.nih.gov/diseases-conditions/allergic-diseases and https://www.niams.nih.gov/health-topics/atopic-dermatitis
