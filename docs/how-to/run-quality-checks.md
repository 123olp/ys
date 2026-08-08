# How To Run Quality Checks

Human Infra keeps local checks reproducible. The repository is documentation-first, so checks focus on privacy, structure, links, research contracts, and lightweight script validity.

## Full Check

Run:

```bash
make check
```

This performs:

1. privacy regression tests and current tracked-tree scan;
2. cache cleanup and repository structure checks;
3. history-timeline and research-contract gates;
4. Python compilation for maintenance and data scripts;
5. final cleanup and structure check.

## Privacy Checks

Run the local gate with relative locations:

```bash
make privacy-audit
```

Run the full reachable-history and commit-identity gate with CI-safe output:

```bash
python3 tools/audit_repository_privacy.py --scope all --revision HEAD --report-mode ci
```

CI-safe failures contain only a rule name, finding count, and irreversible `location_id`; they never echo the matched value, path, commit message, author identity, or environment variable.

## Structure Only

Run:

```bash
make structure
```

This runs `tools/check_repository.py`, which checks:

- required files;
- required directories;
- temporary filename leaks;
- Python cache directories;
- local Markdown links.

## Cleanup

Run:

```bash
make clean
```

This removes Python cache and pytest cache directories.

## Data Script Smoke Check

Run:

```bash
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_mvp_data.py --help
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_core_data.py --help
```

Do not run network data collection unless you intentionally want to refresh generated data.

## Remote Check

GitHub Actions first checks out complete history without persisted credentials and runs the standard-library privacy preflight before installing project dependencies. It then runs the same local command on pushes and pull requests:

```bash
make check
```

Keep CI as a thin wrapper around local checks so failures can be reproduced locally.
