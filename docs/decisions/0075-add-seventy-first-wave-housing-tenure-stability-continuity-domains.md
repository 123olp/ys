# ADR 0075: Add Seventy-First-Wave Housing Tenure Stability Continuity Domains

## Status

Accepted.

## Context

`housing-built-environment-stability` covers the broad housing condition, while existing related domains cover tenant screening, homelessness, mortgage foreclosure, survivor safe housing, utility shutoff protection, and property records. The missing layer is the everyday execution chain that keeps a person housed after they have a unit: lease terms, notices, arrears, eviction diversion, subsidy continuity, fair housing, habitability enforcement, counseling navigation, and manufactured-housing tenure.

## Decision

Add eight formal domains:

- `rental-lease-tenancy-rights-continuity`
- `eviction-prevention-court-diversion-continuity`
- `emergency-rental-assistance-arrears-continuity`
- `housing-choice-voucher-public-housing-continuity`
- `fair-housing-discrimination-reasonable-accommodation-continuity`
- `housing-habitability-inspection-code-enforcement-continuity`
- `hud-approved-housing-counseling-navigation-continuity`
- `manufactured-housing-park-tenure-safety-continuity`

## Consequences

- Housing work must route to these domains when the object is tenancy execution, eviction prevention, rent arrears, subsidy housing, fair housing, habitability, housing counseling, or manufactured-housing park tenure.
- These domains do not provide individual rental, eviction, subsidy, fair-housing, repair, counseling, manufactured-housing, legal, tax, financial, mortgage, relocation, or benefits advice.
- Official-source grounding should prioritize HUD, CFPB, Treasury, USA.gov, and related public legal-aid / housing-counseling materials.
