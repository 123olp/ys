# Add One Hundred Twenty Second Wave Child Nutrition Program Execution Domains

Date: 2026-07-01

Status: Accepted

## Context

Human Infra already has a broad `school-meals-nutrition-access-continuity` domain and food acquisition domains such as SNAP, WIC, food banks, disaster feeding, meal delivery, infant formula and prepared food access.

Those domains are not enough to model child nutrition execution. School-calendar gaps, site-based summer meals, CACFP reimbursement, afterschool meals, special dietary accommodations and unpaid meal balance stigma each have different program interfaces, records, failure modes and safety boundaries.

## Decision

Add six child nutrition program execution continuity domains:

- `summer-ebt-sun-bucks-school-break-food-continuity`
- `summer-food-service-program-site-access-continuity`
- `cacfp-child-adult-care-food-program-continuity`
- `afterschool-snack-supper-meal-continuity`
- `special-diet-allergy-school-meal-accommodation-continuity`
- `school-meal-debt-unpaid-balance-stigma-continuity`

Keep `school-meals-nutrition-access-continuity` as the parent school-meal domain. The new domains model execution seams that must be independently indexed, reviewed and bounded.

## Consequences

- Child nutrition is now represented as a program execution layer, not only as a general school meal or food security concept.
- The project can distinguish benefit issuance, site meals, care-setting meals, afterschool meals, accommodation safety and debt/stigma risk.
- Ethics boundaries must explicitly prohibit individual applications, eligibility judgments, menu or allergy advice, student account handling, complaint templates and child-sensitive data collection.
