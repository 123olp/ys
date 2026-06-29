# Fresh Reviewer Context Packet: CTX9

Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`
Packet hash: `sha256:070e6f9334225a7de3cd2284e170dd09b0641da3a82b9563cabf13f580e082b5`

## Review Boundary

This packet is for an external fresh reviewer. Do not treat local review verdicts as proof. Re-open the listed sources or PDFs, then judge whether the sources support the registered safe use and whether the manuscript violates the forbidden-use boundary.

## Context

| Field | Value |
| --- | --- |
| Priority | 8 |
| Context | CTX9 |
| Risk tier | MEDIUM |
| Risk score | 3 |
| Source group | Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI |
| Claims | CL3, CL6, CL7 |
| Used for | 定义 U_t -> causal claim 的因果门禁和预测模型报告门禁。 |
| Safe use | population、intervention、comparator、time zero、outcome、estimand、试验登记、AI 干预报告、验证、校准和偏倚审查。 |
| Forbidden use | 不能消除所有不可测混杂，也不证明任何注册试验或预测模型有效。 |
| Local verdict | KEEP_WITH_BOUNDARY |
| Required action before submission | Review after high-risk contexts; keep registered boundary language. |

## Reviewer Questions

- 拒绝从任务内 AI 效果直接跳到通用能力增强、健康寿命收益或永生收益。
- 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
- 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。
- 该来源是否真实存在，且题名、作者、年份、场所、DOI 或 URL 与登记信息一致？
- 该来源是否支持 safe use 中登记的最小用途？
- 当前正文、图注或表格是否把该来源扩展成 forbidden use 中禁止的结论？
- 如果只支持部分用途，需要把哪一句改成更弱表述？

## References

| Reference | Title | Audit status | Live status | Registered use |
| --- | --- | --- | --- | --- |
| `clinicaltrialsGov` | ClinicalTrials.gov | official-url-200 | PASS | 提供临床试验登记、人群、比较组、结局和结果回填入口。 |
| `clinicaltrialsGovApi` | ClinicalTrials.gov Data API | official-url-200 | PASS | 提供结构化试验注册与结果数据的机器读取入口，用于后续试验证据采集和协议字段回填。 |
| `consortAi2020` | Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension | doi-verified | PASS | 约束 AI 干预临床试验结果报告中的干预说明、输入输出、人机交互和错误案例分析。 |
| `gradeHandbook` | GRADE Handbook | official-web | PASS | 提供证据确定性、收益风险权衡和从证据到建议的政策语言。 |
| `hernan2022targetTrial` | Target Trial Emulation | crossref-verified | PASS | 定义因果协议门禁和观察数据因果推断边界。 |
| `probastAi2025` | PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods | doi-and-official-site-verified | PASS | 提供 AI 预测模型研究的偏倚风险、适用性、可信度、公平性和质量审查门禁。 |
| `robins2000marginalStructural` | Marginal Structural Models and Causal Inference in Epidemiology | pubmed-verified | PASS | 说明时间变化混杂下的因果估计入口和边界。 |
| `spiritAi2020` | Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension | doi-verified | PASS | 约束 AI 干预临床试验方案中的协议透明度、输入输出、人机交互和错误分析计划。 |
| `tripodAi2024` | TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods | doi-and-official-site-verified | PASS | 提供 AI/机器学习临床预测模型的报告清单、外部验证、校准和透明度门禁。 |
| `tripodProbast` | TRIPOD Statement and PROBAST | official-urls-200 | PASS | 约束预测模型报告质量、偏倚风险、校准和外部验证。 |
| `whoIctrp` | International Clinical Trials Registry Platform (ICTRP) | official-url-200 | PASS | 提供国际临床试验注册网络、WHO 数据集和试验透明度原则的上位入口。 |

## Prompt

```text
你是独立引用语境审稿人。不要使用项目作者的本地结论作为证据，必须重新打开来源并检查正文语境。

Context: CTX9
Source group: Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI
Risk: MEDIUM / score 3
Claims: CL3, CL6, CL7
Used for: 定义 U_t -> causal claim 的因果门禁和预测模型报告门禁。
Safe use: population、intervention、comparator、time zero、outcome、estimand、试验登记、AI 干预报告、验证、校准和偏倚审查。
Forbidden use: 不能消除所有不可测混杂，也不证明任何注册试验或预测模型有效。

References:
- clinicaltrialsGov: ClinicalTrials.gov (official-url-200; PASS)
- clinicaltrialsGovApi: ClinicalTrials.gov Data API (official-url-200; PASS)
- consortAi2020: Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension (doi-verified; PASS)
- gradeHandbook: GRADE Handbook (official-web; PASS)
- hernan2022targetTrial: Target Trial Emulation (crossref-verified; PASS)
- probastAi2025: PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods (doi-and-official-site-verified; PASS)
- robins2000marginalStructural: Marginal Structural Models and Causal Inference in Epidemiology (pubmed-verified; PASS)
- spiritAi2020: Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension (doi-verified; PASS)
- tripodAi2024: TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods (doi-and-official-site-verified; PASS)
- tripodProbast: TRIPOD Statement and PROBAST (official-urls-200; PASS)
- whoIctrp: International Clinical Trials Registry Platform (ICTRP) (official-url-200; PASS)

请逐项输出：
1. reference_existence: PASS / FAIL / UNCERTAIN，并给出核验 URL。
2. safe_use_support: SUPPORTS / WEAK / WRONG，并说明来源文本如何支持或不支持。
3. forbidden_use_violation: NONE / POSSIBLE / PRESENT。
4. required_action: KEEP / SOFTEN / REWRITE / REMOVE / REPLACE_SOURCE。
5. one_sentence_reason: 一句话说明 verdict。
```

## Result Stub

Copy this object into `results/CTX9.json` after review, replacing null values with the external reviewer verdict. Keep that per-context file in the results directory; `npm run assemble:fresh-reviewer-results` is the only supported way to create `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json`.

```json
{
  "context_id": "CTX9",
  "priority": 8,
  "risk_tier": "MEDIUM",
  "source_group": "Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI",
  "claims": [
    "CL3",
    "CL6",
    "CL7"
  ],
  "references": [
    "clinicaltrialsGov",
    "clinicaltrialsGovApi",
    "consortAi2020",
    "gradeHandbook",
    "hernan2022targetTrial",
    "probastAi2025",
    "robins2000marginalStructural",
    "spiritAi2020",
    "tripodAi2024",
    "tripodProbast",
    "whoIctrp"
  ],
  "source_protocol_hash": "sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de",
  "reviewer_identity_class": null,
  "reviewed_at": null,
  "source_urls": [],
  "reference_existence": null,
  "safe_use_support": null,
  "forbidden_use_violation": null,
  "required_action": null,
  "resolution_status": "NOT_REVIEWED",
  "reviewer_reason": null,
  "manuscript_change_required": null,
  "manuscript_change_summary": null,
  "reviewer_trace_path": null
}
```
