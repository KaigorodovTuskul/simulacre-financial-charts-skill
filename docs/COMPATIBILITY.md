# Compatibility

`skills/simulacre-financial-charts/SKILL.md` uses the Agent Skills naming/frontmatter pattern. Markdown references and image assets are relative to its folder. Compatible clients must discover the folder and allow the agent to read references on demand; automatic invocation and interpretation vary by host/model.

Install using `npx skills add KaigorodovTuskul/simulacre-financial-charts-skill --skill simulacre-financial-charts` or copy the skill folder manually. No Python, Node.js chart package, browser or MCP server is required **to read the skill**. Python 3.9+ is needed only for offline repository checks; the optional browser workflow requires the environment's Playwright or equivalent automation tooling, which is not bundled.

This repository does not include a working Chart.js application, a macroeconomic market-data API, or access to the Simulacre original source. Screenshots and code-path notes are reference evidence only.
