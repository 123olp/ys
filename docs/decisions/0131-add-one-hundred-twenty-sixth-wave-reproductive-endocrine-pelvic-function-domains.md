# 0131 Add One-Hundred-Twenty-Sixth Wave Reproductive Endocrine Pelvic Function Domains

Date: 2026-07-01

Status: Accepted

## Context

Human Infra 已有 `reproductive-fertility-continuity/`、第 124 波 ART/生育保存/PGT/第三方生殖治理域，以及第 84 波性健康、月经健康、更年期、盆底功能等生活史预防域。

仍然缺少一个中间层：常见生殖内分泌、盆腔疼痛、结构性出血、男性因素不育、性功能和外阴阴道疼痛这些对象，既不是单纯“生殖技术”，也不是泛化“性健康”或“月经健康”。它们通过代谢风险、慢性疼痛、贫血、疲劳、精子健康、血管信号、污名、关系负担和诊断延迟影响主体有效时间、未来选择权和长期健康风险。

如果不拆成独立域，Human Infra 会把 PCOS、内异症、肌瘤、男性因素不育、ED 和外阴阴道疼痛混入泛泛的不孕、月经或性健康叙事，导致模型无法识别不同机制、证据来源、隐私风险、服务入口和禁止用途。

## Decision

新增第一百二十六波 6 个生殖内分泌、盆腔疼痛和性功能连续性域：

- `domains/polycystic-ovary-syndrome-metabolic-reproductive-continuity/`
- `domains/endometriosis-pelvic-pain-fertility-continuity/`
- `domains/uterine-fibroids-bleeding-anemia-fertility-continuity/`
- `domains/male-factor-infertility-sperm-health-continuity/`
- `domains/erectile-dysfunction-vascular-sexual-function-continuity/`
- `domains/vulvovaginal-pain-infection-sexual-function-continuity/`

这些域只整理公开资料、变量接口、机制链、风险信号、隐私边界、功能结果和禁止用途，不提供诊断、化验/影像解释、药物、激素、手术、补剂、生活方式、性行为、生育治疗、伴侣建议、产品推荐、保险、法律或个体医疗建议。

## Consequences

- `reproductive-fertility-continuity/` 保持上位未来选择权域；新增域负责 PCOS、内异症、肌瘤、男性因素不育、ED 和外阴阴道疼痛这些机制层。
- 第 124 波生殖技术治理域继续处理 ART/IVF、质量报告、生育保存、供体追溯、PGT 和第三方生殖执行层，不承担疾病/症状/功能机制归因。
- 第 84 波生活史预防域继续处理性健康/STI、月经、更年期、盆底等宽入口；新增域补足特定疾病、疼痛、出血、男性因素和性功能风险信号。
- 项目边界更严格：任何个体诊疗、生育治疗、性功能治疗、影像/化验解释或伴侣/法律/保险建议都必须留在禁止区。
