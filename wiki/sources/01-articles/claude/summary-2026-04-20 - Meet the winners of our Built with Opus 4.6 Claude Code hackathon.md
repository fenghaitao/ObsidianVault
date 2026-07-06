---
title: "summary-2026-04-20 - Meet the winners of our Built with Opus 4.6 Claude Code hackathon"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-20 - Meet the winners of our Built with Opus 4.6 Claude Code hackathon.md"]
last_updated: 2026-07-04
---

## Core Summary

This Anthropic blog post profiles the five winners of the "Built with Opus 4.6" virtual Claude Code hackathon, Anthropic's first hackathon in a recurring series (a follow-up "Built with Opus 4.7" hackathon was announced separately). Four of the five winners were not professional developers — a personal injury lawyer, a cardiologist, a former Ugandan government infrastructure specialist, and an electronic musician — alongside one professional software engineer, each building a working product with Claude Code in roughly a week or less. Projects spanned housing permitting (CrossBeam), a kid-friendly visual coding IDE (Elisa), post-visit healthcare follow-up (PostVisit), road-infrastructure investment appraisal from dashcam video (TARA), and real-time AI-generated live music accompaniment (Conductr). The piece frames Claude Code as enabling domain experts with no formal coding background to ship substantial, technically sophisticated software by prompting and reviewing rather than writing code directly.

## Key Points

- **CrossBeam** (Mike Brown, personal injury lawyer): uses parallel Claude sub-agents to parse blueprints and correction letters, build a spatial index, and generate a targeted action plan for California housing-permit rejections in ~20 minutes; also lets municipalities batch-process permits. Buena Park, CA is evaluating adoption. Built by prompting Claude Code and having Claude write its own tests; the builder says he "didn't write a single line of code."
- **Elisa** (Jon McBee, software engineer, 2nd place): a block-based visual IDE where users snap together primitives (goals, requirements, agents, skills, rules, portals, deployments) and a meta-planner decomposes the spec into a task graph for agents to execute; includes a teaching engine that surfaces age-appropriate explanations. Built in 30 hours / 76 commits / 39,000+ lines / 1,500+ tests over six days. Named after and built for the builder's 12-year-old daughter, who used it for a science-fair microcontroller project. $30,000 in Claude API credits (2nd-place prize) is funding classroom pilots.
- **PostVisit** (Michał Nedoszytko, cardiologist): explains diagnoses in plain language, analyzes visit notes and AI-scribe transcripts, and surfaces relevant clinical evidence from scientific literature and full health records with physician oversight; built around privacy, security, and clinical best practices. Follow-up to the builder's earlier product, Previsit.AI (an AI patient-intake system deployed in Belgium, Greece, and Poland). Built in about one week while road-tripping from Brussels to San Francisco.
- **TARA** (Kyeyune Kazibwe, former Uganda Ministry of Works and Transport): converts dashcam road footage into a full investment appraisal using Opus 4.6's vision capabilities — identifying surface conditions, distress patterns, and pedestrian/cyclist/market activity; segments roads into condition sections, auto-populates intervention costs, and generates NPV/cash-flow/sensitivity analysis plus an equity score. Demonstrated on real footage from Uganda's Kira–Matugga Road; a report that used to take weeks now takes about five hours, addressing the high cost ($1–4M) and long timeline (9–14 months) of traditional feasibility studies.
- **Conductr** (Asep Bagja Priandana, electronic musician): browser-based MIDI instrument that listens to a live chord performance and generates real-time drums/bass/melody/harmony tracks, adjustable via natural-language prompts (e.g., "make it funky"). A C engine compiled to WebAssembly generates notes every 15ms to keep the arrangement uninterrupted while Claude's decisions reshape it; runs on ~4,800 lines of JavaScript/WebAssembly.
- **Anomaly**: no prompt-injection-style content or scraped widget boilerplate was present in this article; it read as a clean, direct blog post.

## Related

- [[ClaudeCode]] — the tool all five winning projects were built with
- [[Claude4.6Opus]] — the underlying model, including its vision capabilities used by TARA
- [[CrossBeam]] — housing-permit hackathon winner
- [[Elisa]] — visual IDE hackathon winner (2nd place)
- [[PostVisit]] — post-visit healthcare hackathon winner
- [[TARA]] — road-infrastructure appraisal hackathon winner
- [[Conductr]] — live AI music accompaniment hackathon winner
