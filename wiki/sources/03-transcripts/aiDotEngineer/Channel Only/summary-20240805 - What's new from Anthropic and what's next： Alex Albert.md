---
title: "What's new from Anthropic and what's next： Alex Albert"
type: source
source_type: transcript
source_url: "https://www.youtube.com/watch?v=aiDotEngineer"
author: "Alex Albert"
organization: "Anthropic"
date: 2026-08-05
raw_file: "raw/03-transcripts/aiDotEngineer/Channel Only/20240805 - What's new from Anthropic and what's next： Alex Albert.md"
tags: [anthropic, claude, artifacts, tool-use, steering, interpretability, ai-adoption, product-design]
---

# What's new from Anthropic and what's next： Alex Albert

## Core Thesis
AI adoption today mirrors the dawn of the electrical revolution: companies are simply swapping their "steam engine" for an "electric motor" without redesigning from the ground up. We are in the "magic star icon phase" of AI — tacking AI features onto existing products instead of reimagining products with AI at their core. Anthropic's recent releases (Claude 3.5 Sonnet, Artifacts, Projects, Tool Use API) demonstrate what becomes possible when products are built with LLMs as the foundation, not an afterthought.

## Key Points
- **Electricity-steam analogy**: In 1882, factory owners simply replaced steam engines with electric motors but kept inefficient layouts dictated by transmission lines. The real revolution came only when factories were redesigned from the ground up around electricity's unique capabilities (flexibility, distributed power, specialized tools)
- **The "magic star icon" phase**: Today's AI adoption mirrors mobile-first adoption in the 2010s — companies are adding AI star icons to existing products rather than redesigning around unique LLM capabilities. The Snapchats and Ubers of AI have yet to emerge
- **Why we're stuck**: LLMs are non-deterministic, hard to build on, completely different from what developers are used to. Reliability is still an issue, prompts need rounds of optimization, and we've only scratched the surface of product opportunities
- **Claude 3.5 Sonnet**: The first model in the Claude 3.5 family, only the middle model yet outperforms Claude 3 Opus (Anthropic's previous best). Top of its class on MMLU, HumanEval, GPQA, and tool use benchmarks. 5x cheaper than 3 Opus ($3/M input tokens, $15/M output tokens)
- **Coding performance**: 64% on internal pull request evaluations vs. 38% for Claude 3 Opus. Better at debugging, doesn't get stuck in loops as much. Iteratively writes and tests its way to solutions
- **200k context and recall**: Particularly strong in RAG use cases with 200k context window and near-perfect recall over the entire context
- **Vision capabilities**: State-of-the-art vision abilities showing considerable improvement over 3 Opus. Table transcriptions and OCR are described as "a breeze" — perfectly replicated hand-drawn tables in markdown
- **Availability**: Available on AWS Bedrock and Vertex AI. Anthropic wants Claude available wherever developers are
- **Artifacts**: New product feature that separates Claude's content from the chat dialogue, enabling collaborative work on essays, SVGs, React websites. Combined with 3.5 Sonnet's coding, reasoning, and vision skills, enables screenshot-to-code and Figma-to-component workflows
- **Projects**: Enables teams to ground Claude's outputs in their own knowledge (style guides, code bases, transcripts, past work). On Claude Team plan, projects and chats can be shared across teammates. Engineers at Anthropic upload code repos and documentation into Projects
- **Tool Use API**: Gives Claude custom client-side functions it can intelligently leverage. Enables consistent structured JSON output with 3.5 Sonnet. Developers are giving Claude hundreds of tools at a time
- **Developer Console improvements**: Prompt generator (uses Claude to write optimized prompts from task descriptions), variable support (for editing prompt templates and testing RAG use cases), Evaluate feature (beta, in console)
- **What's next**: 3.5 Haiku and 3.5 Opus coming later this year. Each generation aims to increase intelligence, decrease latency, and decrease cost. Models will become smarter, cheaper, and faster in orders of months, not years
- **Interpretability research**: "Scaling Monosemanticity" paper explains how features within models activate for different topics. By identifying and clamping feature values, they can steer model outputs. Demonstrated via Golden Gate Claude (Golden Gate Bridge feature turned up)
- **Steering API**: In beta testing — allows developers to find and clamp features for specific attributes, controlling Claude's outputs beyond prompting
- **Build philosophy**: Alex Albert advises developers to build with the belief that new models may arrive during their development period. Be ambitious enough in product roadmaps to account for rapidly improving models
- **Build with Claude contest**: Top 3 projects receive $10K in Anthropic API credits

## Entities
- [[AlexAlbert]] — Anthropic, speaker
- [[Anthropic]] — AI research company
- [[Claude 3.5 Sonnet]] — newest model at time of talk
- [[AmazonBedrock]] — platform where Claude 3.5 Sonnet is available
- [[Vertex AI]] — platform where Claude 3.5 Sonnet is available
- [[aiDotEngineer]] — host conference/channel

## Concepts
- [[TechnologyAdoptionAnalogies]] — electricity-steam engine historical parallel
- [[AIAdoptionPatterns]] — the "magic star icon" phase of AI product integration
- [[ToolCalling]] — Anthropic's Tool Use API implementation
- [[Structured Outputs]] — consistent JSON output with Claude 3.5 Sonnet
- [[PromptOptimization]] — Anthropic's prompt generator tool
- [[ModelSteering]] — Anthropic's interpretability-based feature steering
- [[AIReliability]] — LLM non-determinism as a barrier to adoption

## Related
- [[Artefacts]] — Anthropic product feature for separating content from chat
- [[Artifacts]] — Anthropic product feature for separating content from chat
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — Claude tooling
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — Claude Code architecture
- [[summary-20260427 - Gateways are All You Need — Karan Sampath, Anthropic]] — Anthropic MCP strategy
