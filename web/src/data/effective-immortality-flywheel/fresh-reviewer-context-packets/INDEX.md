# Fresh Reviewer Context Packet Index

Date: 2026-06-29T00:00:00.000Z
Protocol hash: `sha256:2615318e3e11f7b5d9e0cb7db273b7d0dd0dabf9618b34ad685df8357a9222de`

This directory splits the fresh reviewer citation-context queue into one packet per context. It is a consumption artifact for an external reviewer; it does not clear the fresh-reviewer gate by itself.

## Workflow

1. Review packets in priority order.
2. For each packet, re-open the source URLs, DOI pages, official pages, PDFs, or retrieval notes.
3. Fill the packet's result stub with reviewer verdicts.
4. Save each completed stub as `results/CTX*.json`.
5. Run `npm run assemble:fresh-reviewer-results` to create the canonical results ledger with input hashes.
6. Run `npm run audit:fresh-reviewer-results`; only a complete PASS can clear the external citation-context gate.

## Packets

| Priority | Context | Risk | Score | Source group | Files |
| ---: | --- | --- | ---: | --- | --- |
| 1 | CTX2 | HIGH | 6 | Grossman Health Capital; WHO HALE; NICE QALY | [MD](./CTX2.md) / [JSON](./CTX2.json) |
| 2 | CTX3 | MEDIUM | 4 | Hallmarks of Aging; GrimAge; Cognitive Reserve | [MD](./CTX3.md) / [JSON](./CTX3.json) |
| 3 | CTX5 | MEDIUM | 4 | Human Capital; Social Capital; Social Relationships Mortality | [MD](./CTX5.md) / [JSON](./CTX5.json) |
| 4 | CTX7 | MEDIUM | 4 | Generative AI at Work; Noy and Zhang; GitHub Copilot; Jagged Technological Frontier | [MD](./CTX7.md) / [JSON](./CTX7.json) |
| 5 | CTX10 | MEDIUM | 4 | Apple Heart Study; Personal Informatics; Lived Informatics; Dynamic Digital Twin | [MD](./CTX10.md) / [JSON](./CTX10.json) |
| 6 | CTX11 | MEDIUM | 4 | Extended Mind; Engelbart; Cognition in the Wild | [MD](./CTX11.md) / [JSON](./CTX11.json) |
| 7 | CTX12 | MEDIUM | 4 | Capability Approach; WHO SDOH; WHO Primary Health Care | [MD](./CTX12.md) / [JSON](./CTX12.json) |
| 8 | CTX9 | MEDIUM | 3 | Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI | [MD](./CTX9.md) / [JSON](./CTX9.json) |
| 9 | CTX1 | LOW | 2 | Kaplan-Meier 1958; Cox 1972 | [MD](./CTX1.md) / [JSON](./CTX1.json) |
| 10 | CTX4 | LOW | 2 | Deliberate Practice; Law of Practice; Self-Regulated Learning; Feedback Intervention Theory | [MD](./CTX4.md) / [JSON](./CTX4.json) |
| 11 | CTX6 | LOW | 2 | TAM; UTAUT; Diffusion of Innovations | [MD](./CTX6.md) / [JSON](./CTX6.json) |
| 12 | CTX8 | LOW | 2 | NIST AI RMF; Guidelines for Human-AI Interaction; NASA-TLX; Automation taxonomy | [MD](./CTX8.md) / [JSON](./CTX8.json) |
