# Research Software, Capsule and Computational Reproducibility Continuity

## Scope

This domain studies research software citation, executable environments, containers, computational capsules, dependency capture, archival snapshots and reproducible analysis packages.

Human Infra treats computational reproducibility as a tool continuity layer: if code, dependencies and execution context vanish, then models cannot be checked, reused or upgraded.

## Human Infra Chain

```text
claim depends on computation
  -> computation depends on code, dependencies, parameters, runtime and data paths
  -> reproducibility packages capture executable context and citation metadata
  -> reviewers and future researchers can rerun, inspect and adapt the analysis
  -> model errors, dependency drift and hidden assumptions become easier to detect
  -> long-horizon research capacity increases
```

## Non-Goals

- No malware packaging, exploit reproduction, credential leakage or unsafe execution instructions.
- No guarantee that rerunnable code proves scientific truth.
- No private data packaging or license laundering inside reproducibility bundles.
- No dependency pinning advice that bypasses security patches.

## Source Signals

- FORCE11 Software Citation Principles: https://force11.org/info/software-citation-principles/
- Software Heritage archive: https://www.softwareheritage.org/
- CITATION.cff format: https://citation-file-format.github.io/
- Zenodo GitHub archiving: https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content
- The Turing Way reproducible research guide: https://the-turing-way.netlify.app/

## Next Notes

- Define minimum reproducibility package fields: code, data pointer, environment, seed, parameters, license and citation.
- Connect to D3/Observable/Web paper outputs without mixing demo code with validated scientific models.
- Track reproducibility failure modes: dependency rot, hidden state, nondeterminism, missing data and hardware assumptions.
