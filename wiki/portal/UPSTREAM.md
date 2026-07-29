# Wikimedia Portal Upstream

The language portal is a locally adapted snapshot of the official
`www.wikipedia.org` production portal.

- Source repository: `https://gerrit.wikimedia.org/r/wikimedia/portals`
- Source revision: `d40655d75fa618970e43cd59e608d3180e4a4da1`
- Production snapshot: `https://www.wikipedia.org/`
- Snapshot date: `2026-07-25`
- Upstream license: MIT, preserved in `LICENSE.wikimedia-portals`

`index.html` retains the upstream HTML structure and inline production CSS.
The upstream script owns the language-list interaction. `adapter.js` is limited
to local Wiki routing and local search submission. It must not add or override
visual CSS.

The snapshot also preserves the upstream Simplified and Traditional Chinese
localization payloads under `portal/wikipedia.org/assets/l10n/`. Their
filenames are bound to the `translationsHash` embedded in `index.html`; a
portal refresh must update the HTML and localization payloads atomically.

Refresh with:

```bash
python3 wiki/scripts/refresh-wikipedia-portal.py
```

After refreshing, run:

```bash
cd wiki
./scripts/validate-source.sh
./scripts/smoke-test.sh
```
