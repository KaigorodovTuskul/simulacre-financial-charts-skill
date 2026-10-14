# Contributing

Please open an issue with a reproducer and the specific financial/visual decision before proposing a change. Keep `SKILL.md` concise and move detailed decisions into `references/`.

For every new chart pattern, document: the economic question; units, dates and missing-data semantics; a justified reference; an example prompt; and one counterexample. Keep dataset licensing and user consent in mind.

If updating any reference PNG, update its `sha256`, `width`, `height` and `status` in `reference-manifest.json`, explain its provenance and run `python scripts/validate.py` and `python -m unittest discover -s tests -v`.

Do not submit Playwright trace archives, auth/OAuth URLs, session cookies, access tokens, individual account data, or copyrighted third-party materials without rights. Strip unneeded identifiers from logs and screenshots. A screenshot fallback must stay labeled as such.
