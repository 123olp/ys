# Living Evidence Surveillance and Update Continuity

## Scope

This domain studies living systematic reviews, surveillance searches, update triggers, evidence monitoring, versioned conclusions and stale-claim retirement.

Human Infra treats evidence as time-sensitive: a claim that was reasonable when written can become unsafe when new trials, harms, retractions or guidelines appear.

## Human Infra Chain

```text
claim is published
  -> new studies, registries, safety reports and retractions continue to appear
  -> surveillance rules decide when evidence must be revisited
  -> versioned conclusions separate old confidence from current confidence
  -> Human Infra pages can retire, downgrade or update claims
  -> long-horizon models avoid becoming fossilized around stale evidence
```

## Non-Goals

- No real-time medical alerting, clinical monitoring, trading signal, emergency recommendation or automated treatment change.
- No scraping restricted databases, redistributing copyrighted content or bypassing publisher access.
- No claim that a living review is always superior to a conventional review.
- No manipulation of update triggers to preserve preferred conclusions.

## Source Signals

- Cochrane living evidence resources: https://www.cochrane.org/
- Cochrane Handbook: https://training.cochrane.org/handbook
- Living systematic review methods literature: https://www.bmj.com/content/362/bmj.k2925
- Retraction Watch database: https://retractiondatabase.org/

## Next Notes

- Define update-card fields: surveillance interval, sources, trigger type, version, change type and claim consequence.
- Connect to `research-artifact-archive-retention-preservation-continuity/` for versioned Web papers.
- Track failure modes: stale search, silent conclusion drift, update fatigue, missed safety signal and retraction ignored.
