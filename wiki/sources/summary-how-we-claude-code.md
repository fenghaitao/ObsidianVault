---
title: "How We Claude Code"
type: source
tags: [claude-code, HTML, verification, prompting, agent-workflow]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London Day 2/06 - How we Claude Code.md]
last_updated: 2026-06-23
---

## Core Summary

Arno from Anthropic's Applied AI team presents a workshop based on Tariq's "Unreasonable Effectiveness of HTML Files" concept, demonstrating three levels of Claude Code workflow improvement. Level 1: Let Claude interview you for requirements rather than specifying everything upfront — Claude is better at extracting latent requirements than humans are at articulating them. Level 2: Use HTML files instead of markdown for specs because they are more information-dense and ergonomic for human review. Level 3: Embed verification directly into artifacts using DOM-published state contracts, Storybook fixtures, and Playwright MCP, enabling both human-readable dashboards and agent-driven verification that can be recorded and shared.

## Key Points

- **The bitter lesson for agents:** As models get more capable, resist constraining them. Claude is better at extracting your requirements than you are at defining them. Use the "ask user question" tool to let Claude interview you.
- **HTML over Markdown:** HTML specs are more information-dense, more ergonomic for human review, and enable richer interaction (screenshots via Playwright MCP, interactive exploration). Long markdown files (>200 lines) are unlikely to be read.
- **Verification embedded in artifacts:** Publish component state to the DOM via data attributes so agents can read contracts without scraping. Define schemas, fixtures (known states), and invariants that must always hold.
- **Three verification surfaces:** Human-readable dashboard (click to run individual or all verifications), agent-driven from browser (Playwright MCP reads DOM contracts), headless CLI (bun verify for CI).
- **Recording verification:** Verification runs can be recorded as video clips and stored (S3) or shared with colleagues as evidence bundles.
- **Model recommendations:** Use Opus 4.7 for its superior vision model (critical for HTML/screenshot workflows). Use fast mode for quick spec iteration. Use auto mode and extra high effort as defaults.
- **Token efficiency of HTML:** While individual HTML specs use more tokens to generate, they reduce total iteration cycles, making them more token-efficient overall.

## Related

- [[ClaudeCode]] — the tool being optimized
- [[ClaudeFable5]] — Opus 4.7 recommended for vision capabilities
- [[ModelContextProtocol]] — Playwright MCP used for browser automation
- [[PromptEngineering]] — the interview-based prompting technique
