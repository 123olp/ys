# 0083: Add Seventy-Ninth Wave AI Evaluation Operations Governance Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra already has broad AI domains such as `ai-agency-safety/`, `model-cards-ai-audit-documentation/`, `compute-data-center-ai-infrastructure/` and automation-bias / human-factors domains. These are necessary, but they do not yet split the operational interfaces required for AI to serve as a durable subject-amplification system.

The project needs a more precise layer for AI evaluation, red teaming, incident monitoring, data provenance, synthetic data validation, model supply chain, agent permissions, human handoff, and resource budgets.

## Decision

Add nine AI evaluation and operations governance domains:

- `ai-evaluation-benchmark-validity-continuity/`
- `ai-red-teaming-adversarial-testing-continuity/`
- `ai-incident-reporting-post-deployment-monitoring-continuity/`
- `ai-data-provenance-contamination-drift-continuity/`
- `synthetic-data-generation-validation-continuity/`
- `ai-model-supply-chain-provenance-release-continuity/`
- `ai-agent-tool-permission-sandbox-continuity/`
- `human-ai-oversight-handoff-accountability-continuity/`
- `ai-resource-cost-latency-budget-continuity/`

Each domain is initialized with `README.md` and `AGENTS.md` only. No model weights, private datasets, attack payloads, credentials, logs, scripts, or production AI automation are added.

## Consequences

- AI is treated as an operating subsystem that must pass evaluation, safety testing, data, supply-chain, permission, monitoring, handoff, and budget gates before it can be framed as subject-continuity infrastructure.
- `ai-agency-safety/` remains the broad agency-safety domain; the new domains own specific interfaces and evidence cards.
- The domain map, atlas, radar, applications/literature index, safety boundaries, root README, AGENTS and structure checker must reference this wave.

## Non-Goals

- Do not provide jailbreaks, prompt injection payloads, exploit steps, model theft methods, supply-chain poisoning, access-control bypasses, cloud cost bypasses, surveillance workflows, or compliance guarantees.
- Do not turn evaluation scores, red-team claims, synthetic data, model cards or incident records into production safety proof.
- Do not output individual medical, legal, financial, employment or mortality predictions through these AI governance domains.

## Verification

- `python3 tools/check_repository.py`
- `git diff --check -- . ':(exclude)web'`
- `make check`
