# Agent guidance for this repository

Do not modify chart data to make a reference image look better. Financial semantics override stylistic preferences. The public GitHub repository contains only curated, whitelisted visual references, not raw browser archives.

Keep the skill client-independent and short. Put rich documentation in `references/` and tests in `tests/`. Preserve relative links and the exact 53 unique indicators. Do not treat fallback screenshots as successful app exports.

Before committing: run `python scripts/validate.py` and `python -m unittest discover -s tests -v`. When updating a pinned PNG, regenerate the hash/size metadata. Never claim browser tests ran unless a browser was actually used.
