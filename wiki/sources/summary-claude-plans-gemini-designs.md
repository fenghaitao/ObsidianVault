---
title: "summary-claude-plans-gemini-designs"
type: source
tags: [source, original-material, cross-provider, frontend, gemini, opus, workflow]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260604 - Claude Plans, Gemini Designs： The Workflow to Build BEAUTIFUL Frontends.md"]
last_updated: 2026-06-21
---

## Core Summary

[[ColeMedin]] builds a **cross-provider workflow** that one-shots beautiful full-stack web apps by mixing models to their strengths: **Gemini 3.5 Flash** (cheap, fast, great at handcrafted-looking UIs) designs the front end, while **Opus 4.8** (superior reasoning) handles planning, page copy, and integrations. Because you can't switch providers mid-conversation, each step is a **separate session** that communicates via **handoff markdown documents** — see [[CrossProviderWorkflow]]. Delivered as skills (run individually) or an [[Archon]] one-shot workflow.

## Key Points

- **Model specialization**: Gemini 3.5 Flash builds UIs that look human-crafted (one-shot results in **Antigravity** that beat Claude Code / Lovable / Bolt for first-pass design) and is cheap (~$1.50/M input); but its *page copy* tends to hallucinate. **Opus 4.8** reasons better — so it owns planning, copy, and integrations. **Sonnet** handles cheap exploration/validation. Mixing = best-of-both + cost savings.
- **Why session-per-step + handoff docs**: (1) there's no way to mix providers within a single context window; (2) one focused task per session avoids [[ContextRot]] — no single model (even Opus) can do explore→plan→UI→integrations→deploy well at once. Each step outputs a markdown doc read by the next.
- **The "don't let Opus design" insight**: the plan deliberately **omits any UI structure** (no grids/columns) — early versions where Opus described the layout "steamrolled" Gemini and produced *worse* UIs. Let each model own its strength. The plan has 3 sections: **A) site content & intent** (voice/mood/copy, no structure), **B) integration scope** (APIs, DB model, auth), **C) deployment plan** (e.g. Vercel/DigitalOcean MCP).
- **The workflow nodes**: explore (Sonnet → `context.md`) → plan (Opus → `plan.md`) → **design UI** (Gemini via [[Pi]] or [[Antigravity]], reading *only section A* → UI summary) → integrations (Opus) → validation (Sonnet: tests/lint) → fix (Opus) → deploy → **smoke test** (agent-browser automation) → deployed app.
- **Tools**: skills are the workflow steps (invoke `front-end-mix-explore`, `...-plan`, `...-design`, etc.); **[[Pi]]** + **OpenRouter** to reach Gemini, or **[[Antigravity]]** (Google's agentic IDE). Skills work the same in Claude Code and Pi; for agents without skill support you can "read the skill and execute it" as a prompt. **[[Archon]]** bundles all steps into a single autonomous run.
- **Easy experimentation**: because steps are isolated sessions, you can swap providers per node in minutes (e.g. exploration on Gemini via Pi, integrations on Kimi K2.6) to find the best mix.
- **Scope caveat**: great for non-trivial **MVPs/POCs**, not guaranteed to one-shot arbitrarily complex apps.

## Related

- [[CrossProviderWorkflow]] — the mix-models-by-strength pattern
- [[Pi]] — coding-agent harness used to run Gemini via OpenRouter
- [[Antigravity]] — Google's agentic IDE (Gemini) for one-shot UIs
- [[Archon]] — one-shot orchestration of the whole workflow
- [[ContextRot]] — why one focused task per session
- [[ClaudeCode]] — runs the Claude/Opus/Sonnet steps
- [[ColeMedin]] — author
