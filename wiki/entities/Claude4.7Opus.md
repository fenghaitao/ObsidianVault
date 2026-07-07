---
title: "Claude Opus 4.7"
type: entity
tags: [claude, model, anthropic, llm, foundation-model, opus, agentic-coding]
sources: [raw/01-articles/claude/2026-04-16 - Best practices for using Claude Opus 4.7 with Claude Code.md, raw/01-articles/claude/2026-05-21 - How our partners are putting Opus to work for cybersecurity.md, raw/01-articles/claude/2026-05-27 - Using LLMs to secure source code.md, "raw/01-articles/claude/2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon.md"]
last_updated: 2026-07-07
---

## Definition

Claude Opus 4.7 is Anthropic's strongest generally available model to date (as of April 2026) for coding, enterprise workflows, and long-running agentic tasks — the successor to [[Claude4.6Opus|Opus 4.6]].

## Key Information

- **Improvements over Opus 4.6**: handles ambiguity better, is more capable at finding bugs and reviewing code, carries context across sessions more reliably, and reasons through ambiguous tasks with less direction. Performs better on long-running tasks — complex multi-file changes, ambiguous debugging, code review across a service, and multi-step agentic work — making these previously supervision-bottlenecked tasks a good fit.
- **Tokenizer and token usage**: ships an updated tokenizer, and has a greater proclivity to think more at higher effort levels (especially on later turns in longer sessions) — together these increase token usage relative to Opus 4.6, meaning prompts/harnesses tuned for the older model may need retuning.
- **Interactive vs. autonomous behavior**: in interactive, multi-turn agentic coding settings, it reasons more after each user turn (improving coherence, instruction-following, and code quality over long sessions, at the cost of more tokens); behaves differently in single-turn, autonomous/asynchronous agent deployments.
- **New `xhigh` effort level**: introduces an effort level between `high` and `max`, trading more reasoning for latency on hard problems. `xhigh` is now the default effort level for Opus 4.7 in [[ClaudeCode]] and is recommended for most agentic coding work, especially intelligence-sensitive tasks (API/schema design, legacy-code migration, large-codebase review). Existing Claude Code users without a manually-set effort level are auto-upgraded to `xhigh`.
- **No fixed-budget extended thinking**: unlike prior models, Opus 4.7 does not support [[ExtendedThinking|extended thinking]] with a fixed thinking-token budget. It instead uses [[AdaptiveThinking|adaptive thinking]] exclusively — thinking is optional at each step and the model decides when more thinking is warranted — and this adaptive thinking is less prone to overthinking than in the prior release.
- **Default behavior changes vs. Opus 4.6** (relevant when migrating existing Claude Code setups): less default-verbose (response length calibrated to task complexity rather than uniformly long); calls tools less often while reasoning more per call; spawns fewer [[ClaudeCodeSubagents|subagents]] by default, requiring explicit prompting to fan out across files/independent items when parallelism is desired.
- **[[ComputerUse|Computer use]] (May 2026)**: supports a higher resolution budget than the 4.6 family (2576px max long edge, ~3.75MP max pixel budget, vs. 1568px/~1.15MP) — recommended starting resolution 1080p. Its clicking precision is roughly on par with Sonnet 4.6 (closing a prior gap where Sonnet was mechanically more precise), while its larger resolution budget reduces how much screenshots need to be downscaled. On the OSWorld Verified benchmark, Opus 4.7 outperforms the entire 4.6 family at equivalent token/effort settings — at `low` effort it scores similarly to Sonnet 4.6 at `max` effort while using ~1/10th the tokens, making it the recommended choice for difficult computer-use tasks or high-resolution source images. See [[summary-2026-05-13 - Best practices for computer and browser use with Claude]].
- **Visual schematic understanding**: Opus 4.7's spatial reasoning capabilities extend to understanding visual schematics and boardviews, demonstrated in the Built with Opus 4.7 hackathon where [[WrenchBoard]] used it to trace power paths on motherboard schematics, lighting up boardviews step by step. [[VirtualPuppetTheater]] leveraged its spatial reasoning for real-time webcam-based puppet animation and 3D prop generation.
- **Hackathon adoption**: Opus 4.7 powered all six winning projects in Anthropic's Built with Opus 4.7 hackathon (June 2026), spanning medical training ([[Medkit]]), electronics repair ([[WrenchBoard]]), CS education ([[Maieutic]]), interactive play ([[VirtualPuppetTheater]]), home repair ([[MaestrIA]]), and factory maintenance ([[ARIA]]). See [[summary-2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon]].

## Related

- [[ClaudeSecurity]] — Enterprise vulnerability-scanning product built on this model (public beta, April 2026)
- [[summary-2026-04-16 - Best practices for using Claude Opus 4.7 with Claude Code]] — source summary
- [[Claude4.6Opus]] — predecessor model
- [[ClaudeCode]] — primary product surface discussed; xhigh is now its default effort level for this model
- [[AdaptiveThinking]] — the thinking paradigm this model relies on exclusively
- [[ExtendedThinking]] — the fixed-budget thinking paradigm this model does NOT support
- [[ClaudeCodeSubagents]] — subagent delegation behavior changed in this release
- [[summary-2026-05-13 - Best practices for computer and browser use with Claude]] — computer-use resolution limits and OSWorld Verified benchmarks
- [[ComputerUse]] — capability with model-specific resolution/effort guidance for this model
- [[summary-2026-05-21 - How our partners are putting Opus to work for cybersecurity]] — cybersecurity partner offerings powered by Opus
- [[ClaudeSecurity]] — partner ecosystem built on this model
- [[summary-2026-05-27 - Using LLMs to secure source code]] — security scanning workflow guidance using Opus
- [[ThreatModeling]] — threat modeling with Opus as the first step of security scanning
- [[VulnerabilityDetection]] — vulnerability discovery powered by Opus
- [[VulnerabilityVerification]] — adversarial verification using Opus
- [[AutomatedPatching]] — patch generation using Opus
- [[WrenchBoard]] — hackathon project using visual schematic understanding
- [[VirtualPuppetTheater]] — hackathon project using spatial reasoning for puppet animation
- [[Medkit]] — hackathon project using Opus 4.7 for medical training simulation
- [[Maieutic]] — hackathon project using Opus 4.7 for CS education
- [[MaestrIA]] — hackathon project using Opus 4.7 for home repair diagnostics
- [[ARIA]] — hackathon project using Opus 4.7 for industrial maintenance
- [[summary-2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon]] — hackathon source summary
