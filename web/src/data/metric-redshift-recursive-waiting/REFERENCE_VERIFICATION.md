# Metric Redshift Reference Verification

**Generated**: 2026-06-29T17:50:38.491Z
**Verdict**: WARN

Metric-redshift source URLs were checked; at least one source returned a warning that requires human review.

This artifact checks source-entry existence and URL accessibility. It does not prove that a source supports a manuscript claim.

## Summary

| Status | Count |
| --- | ---: |
| PASS | 9 |
| WARN | 3 |
| FAIL | 0 |

## Entries

| Source | Status | Method | HTTP | URL | Note |
| --- | --- | --- | ---: | --- | --- |
| `pound1959redshift` | WARN | CURL_HEAD | 403 | https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.3.439 | curl HEAD returned 403; human review may be needed for access-controlled or transient responses. |
| `vessot1980gravityProbeA` | WARN | CURL_HEAD | 403 | https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.45.2081 | curl HEAD returned 403; human review may be needed for access-controlled or transient responses. |
| `ashby2003gps` | PASS | CURL_HEAD | 302 | https://link.springer.com/article/10.12942/lrr-2003-1 | Source URL responded successfully to curl HEAD. |
| `nasaBlackHoleTooClose` | PASS | CURL_HEAD | 200 | https://science.nasa.gov/universe/what-happens-when-something-gets-too-close-to-a-black-hole/ | Source URL responded successfully to curl HEAD. |
| `nasaBlackHoleVisualization` | PASS | CURL_HEAD | 200 | https://science.nasa.gov/universe/black-holes/supermassive-black-holes/new-nasa-black-hole-visualization-takes-viewers-beyond-the-brink/ | Source URL responded successfully to curl HEAD. |
| `grib2009infiniteFuture` | PASS | CURL_HEAD | 200 | https://arxiv.org/abs/0906.1442 | Source URL responded successfully to curl HEAD. |
| `pavlov2012futureObservation` | PASS | CURL_HEAD | 200 | https://arxiv.org/abs/1203.4000 | Source URL responded successfully to curl HEAD. |
| `etesi2002malamentHogarth` | PASS | CURL_HEAD | 200 | https://arxiv.org/abs/gr-qc/0104023 | Source URL responded successfully to curl HEAD. |
| `welch2006malamentHogarth` | PASS | CURL_HEAD | 200 | https://arxiv.org/abs/gr-qc/0609035 | Source URL responded successfully to curl HEAD. |
| `earmanNortonForeverDay` | PASS | CURL_HEAD | 200 | https://philsci-archive.pitt.edu/1307/ | Source URL responded successfully to curl HEAD. |
| `lewis1976timeTravel` | WARN | CURL_HEAD | 403 | https://www.jstor.org/stable/2025310 | curl HEAD returned 403; human review may be needed for access-controlled or transient responses. |
| `humanInfraEffectiveImmortality` | PASS | LOCAL_ROUTE | 200 | /papers/effective-immortality-flywheel/ | Local route source exists at src/pages/papers/effective-immortality-flywheel.astro. |
