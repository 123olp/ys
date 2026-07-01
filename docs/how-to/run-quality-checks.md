# How To Run Quality Checks

Human Infra keeps local checks intentionally small. The repository is documentation-first, so checks focus on structure, links, and lightweight script validity.

## Full Check

Run:

```bash
make check
```

This performs:

1. cache cleanup;
2. repository structure check;
3. Python compilation for maintenance and data scripts;
4. cache cleanup again;
5. final repository structure check.

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

GitHub Actions runs the same command on pushes and pull requests:

```bash
make check
```

Keep CI as a thin wrapper around local checks so failures can be reproduced locally.
