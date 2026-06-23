# How To Add A Domain

Use this when a new subject area does not fit an existing domain.

## Before You Add It

Do not create a domain just because a topic is interesting. A domain should exist only when it has a stable object, durable boundary, and recurring documents or work.

Ask:

- What does this domain own that no existing domain owns?
- Which existing domain would become confused if this material stayed there?
- What are the safety and evidence boundaries?
- What files are needed now, not someday?

## Steps

1. Add or update a decision record under `docs/decisions/` if the domain changes project architecture.
2. Update `docs/reference/domain-map.md`.
3. Create `domains/<domain>/README.md` from `docs/templates/domain-readme.md`.
4. Create `domains/<domain>/AGENTS.md`.
5. Add the domain to `domains/README.md` and `domains/AGENTS.md`.
6. Add required files to `tools/check_repository.py` only if the new domain is part of the baseline structure.
7. Run:

```bash
make check
```

## Stop Conditions

Stop and do not create the domain if:

- the material belongs in an existing domain;
- the topic is only a single source note;
- the scope is speculative and has no stable owner;
- the safety boundary cannot be stated clearly.
