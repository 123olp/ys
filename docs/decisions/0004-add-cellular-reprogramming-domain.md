# 0004 Add Cellular Reprogramming Domain

## Status

Accepted.

## Context

Human Infra 已有 `longevity-evidence/` 用于健康寿命、干预证据、临床试验和安全边界。但山中因子、部分重编程、化学重编程、AI 因子设计和表观遗传编辑不是普通长寿干预条目。

它们共同指向一个更底层的机制问题：

```text
细胞身份与细胞年龄是否可以在一定条件下被拆开调控。
```

如果把该谱系直接放进 `longevity-evidence/`，会把机制谱系、商业前沿、体外指标、动物实验、人体安全性试验和真实临床疗效混成一个证据桶，增加过度推断风险。

## Decision

Create `domains/c2-source-maintenance/cellular-reprogramming/` for cellular reprogramming and epigenetic rejuvenation.

The domain covers:

- OSKM / OSK / iPS;
- partial reprogramming;
- transient mRNA and chemical reprogramming;
- AI-designed reprogramming factors;
- epigenetic editing;
- rejuvenation versus dedifferentiation;
- identity retention, tumor risk, delivery control and evidence levels.

## Alternatives Considered

- Add it to `longevity-evidence/`: rejected because this is a mechanism genealogy and safety boundary, not a mature intervention evidence ledger.
- Add it to `docs/reference/`: rejected because the domain will need its own source trail, claim-evidence matrix and mechanism-specific review checklist.
- Add it under `future-waiting/`: rejected because cellular reprogramming changes biological state variables directly, while future-waiting changes waiting cost and time exposure.

## Consequences

- Cellular reprogramming receives an independent boundary and source trail.
- Longevity Evidence remains focused on evidence ledgers, clinical trials, public data and intervention safety.
- Human Infra can discuss cell-state rewriting without treating it as validated whole-body rejuvenation.
- Future work must maintain clear links between this domain and the life-path prediction model.

## Safety And Evidence Boundary

This domain must not provide wet-lab protocols, vector construction steps, dosing, delivery instructions, clinical recommendations, or claims that cellular reprogramming currently proves whole-body rejuvenation, lifespan extension in humans, or immortality.
