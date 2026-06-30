---
title: "summary-20260525 - Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind"
type: source
tags: [source, transcript, evals, benchmarks, kaggle, game-arena, agent-exams, hackathons, open-source, democratization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Core Summary
Nicholas Kang (PM, Kaggle Benchmarks) and Michael Aaron (SWE, Kaggle) present Google DeepMind's open-source platform strategy for democratizing AI evaluation. They diagnose three core problems with current AI evals: (1) benchmarks are scattered, decentralized, and stale fast — 10+ drop daily with no centralized tracking; (2) evals lack transparency, accessibility, and verifiability — model publishers optimize configurations for their own models, skewing published results; (3) a tiny fraction of the world (30K AI researchers) creates evals that affect billions, leading to jagged AI capabilities. They then present four platform solutions: hackathons for community-driven benchmark creation, standardized agent exams for consumer agent testing, Game Arena for unsaturable PvP model benchmarking via Elo scores, and a Benchmark platform enabling anyone to build, run, and share evals openly.

## Key Points

### The Three Problems with AI Evals
- **Scattered and stale**: 10+ benchmarks drop daily on arXiv with no central tracking. Leaderboards go stale as authors move on to the next paper. Nick Kang cannot keep up even though it's his full-time job.
- **Non-transparent and unverifiable**: Model publishers optimize benchmark configurations for their own models. Real anecdote: a competing AI lab re-ran a Kaggle benchmark with their model's compaction feature enabled (while Kaggle hadn't used compaction for other models) and published deceptively better results. The results you see don't always reflect actual capability.
- **Built by too few people**: 30K AI researchers serve 30M+ technical professionals and billions of users. If something isn't evaluated, we can't hill-climb on it. This leads to jagged AI — superhuman in some areas, mediocre in others. Not equitable AI.

### The Wastewater Treatment Plant Engineer
- A 20-year wastewater plant engineer from Turkey built a proprietary benchmark from his own experience to evaluate how AI could help prevent safety incidents that had killed people in his country
- This dataset doesn't exist anywhere else — not in AI lab focus areas because it's not economically productive for them
- Exemplifies why open-source community contributions to evals are essential

### Solution 1: Hackathons
- Platform for anyone to host a hackathon to channel energy toward specific eval problems
- Guardrails with creative freedom so participants can flourish
- All results are open source for everyone's benefit
- Current example: hackathon with Google DeepMind AGI team building benchmarks around five cognitive faculties of AGI (from their recent paper)
- Challenges: providing tools (dataset hosting, model API access) for globally distributed participants, especially those without money for API keys; human expert judging required since AI agents can't judge innovation and creativity well

### Solution 2: Standardized Agent Exams
- Paste a one-line prompt for your agent, it takes an exam, and returns a score on a leaderboard
- Experimental MVP launched the week before the talk
- Addresses the gap: research labs use sophisticated eval setups, but consumer agent builders rarely test before sending agents into the real world (e.g., OpenClaw filing 1,100 security advisories)
- Future direction: safety-focused exams for quick baseline checks before deployment
- Spectrum challenge: too difficult and nobody finishes; too easy and no meaningful signal
- Early traction: 500+ agents evaluated in one week with minimal promotion; organic community content like "SAE prep courses" emerging on Mopbook

### Solution 3: Game Arena
- PvP game-based benchmark where models compete directly; Elo score rating
- Unsaturable and evergreen — there must always be a winner and a loser
- Current games: Werewolf (deception), Poker (randomization + deception, reveals model personalities — Grok goes all-in, newer models more risk-averse), Chess (ML analysis staple)
- Engineering pipeline: design/iterate game → prompt engineering for fairness → build harness (mostly OpenSpiel RL framework) → run simulations via LLM model proxy on Kaggle simulation platform → Bradley-Terry pairwise scheduling → publish results with Elo scores, conversation datasets, and game visualizer
- All open source; GitHub link provided in talk
- Challenges: (1) Cost — 400K poker hands for statistical significance, very expensive API bills; (2) Engagement — watching LLMs play each other gets boring, exploring community participation models like prompt-engineering hackathons; (3) Comparison over time — old models disappear, new models arrive, endpoint providers not always honest about which model is running

### Solution 4: Benchmark Platform
- Platform enabling anyone to build, run, and share evals openly and verifiably
- NOT a production evaluation platform — focused on community involvement
- Architecture: write assertions (code-based checks like "does this contain a towel?"), LLM judging, group into tasks, evaluate against model collections, aggregate tasks into benchmarks
- Example: Paige Bailey's XKCD SVG parsing task — model generates SVG, assertions check if it generates SVG at all, has correct text, etc.; side-by-side comparison view
- Challenges: (1) Inspiration and incentivization — harder than production evals since community members need motivation to build benchmarks others find interesting (hackathons and Kaggle points/medals help); (2) Agentic benchmark execution ambiguity — what's actually being tested? SWE-bench Pro shows six frontier models within a few percentage points, but harness choice causes 22% difference. Are you testing the harness or the model?; (3) Fast release/deprecation cycles make comparisons over time difficult

### Key Quote
- "If something's not being evaluated, not being benchmarked, we cannot hill climb on it, we cannot know how good we are at those things." — Nicholas Kang

## Related
- [[NicholasKang]] — speaker, PM at Kaggle Benchmarks
- [[MichaelAaron]] — speaker, SWE at Kaggle
- [[Kaggle]] — platform, world's largest AI/ML community (30M+ users)
- [[GoogleDeepMind]] — parent organization
- [[Game Arena]] — PvP unsaturable benchmark
- [[Agent Exams]] — standardized agent testing
- [[Eval Hackathons]] — community-driven eval creation
- [[AgenticEvaluations]] — the evaluation paradigm
- [[BenchmarkSaturation]] — problem Game Arena addresses
- [[EvalPlatforms]] — broader platform category
- [[Bradley-Terry Pairing]] — statistical scheduling technique
- [[OpenSpiel]] — RL game framework used
- [[LLM-as-Judge]] — judging technique used in benchmarks
- [[PvP Benchmarking]] — competitive model evaluation
- [[Elo Score]] — rating system used in Game Arena
- [[Paige Bailey]] — contributed XKCD SVG task example
- [[SWE-bench Pro]] — benchmark where harness choice dominates model choice
