---
title: "summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary"
type: source
tags: [source, transcript, ai, agentic-engineering, context-engineering, workflow]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary.md"]
last_updated: 2026-06-26
---

## Core Summary
Brendan O'Leary of Kilo Code presents "agentic engineering" — the paradigm shift from merely using AI tools to working with them as collaborators. He argues that the mental model must evolve: AI agents should be treated as energetic, well-read, often confidently wrong junior developers who lack judgment and business context. The key to success is deliberate context engineering (curating what goes into the context window) and a structured research-plan-implement workflow that front-loads human thinking before letting AI generate code.

## Key Points
- 90% of engineers have used AI tools, but most cannot articulate their actual workflow — the gap between using AI and working with AI is the core problem
- AI evolution timeline: line completion (early 2020s) → function suggestion (2022, GitHub Copilot) → autonomous execution (2025-2026, agents that can break down tasks, touch files, run tests, create PRs)
- Armin Ronacher (Flask creator): "We're no longer just using machines. We're now working with them."
- Mental model: AI agent = energetic, enthusiastic, extremely well-read, often confidently wrong junior developer — incredibly fast, no ego, astonishing breadth of knowledge, but no judgment or business context
- Context engineering (Karpathy): the delicate art of filling the context window with just what's needed — context is expensive, more context doesn't always mean better results, and bad context can poison everything
- Context window degrades past ~50% fullness; MCP servers add hidden context overhead
- Four context management habits: persist info outside the window (scratch pads, memory files, agents.md), be selective about what to pull in, summarize/trim/compress as the window grows, isolate context across sessions
- Research-Plan-Implement loop: Phase 1 (Research) — understand the system using ask-only mode, produce a research document; Phase 2 (Plan) — outline explicit steps, scope, verification strategy, produce a plan file; Phase 3 (Implement) — start a fresh session with just the plan, commit frequently, review like a PR
- Dex Horthy: "A bad line of research can potentially be hundreds of lines of bad code" and "AI can't replace thinking. It can only amplify the thinking you've done or the lack of thinking you haven't done."
- Agent configuration in three buckets: modes (role-based: ask, code, architect), agents.md (always-on project rules), skills.md (on-demand reusable playbooks)
- MCP servers add tool descriptions to every interaction — disable unused ones to avoid wasted tokens and confusion
- Internal platform API integration: use OpenAPI/Swagger specs if available, convert to markdown, use reference URLs for frequently changing APIs, or build custom MCP servers for complex multi-step workflows
- Practical tips: one task per session, watch the context meter, start fresh when things go off the rails, use AI to summarize for a new agent session
- Git as a local first-pass PR review with your agents before sharing with human colleagues
- Kilo Code features: ask/code/architect modes, at-mentioning for context, slash commands, VS Code integration, CLI/mobile/cloud/Slack surfaces, OpenClaw and KiloClaw for safe agent usage

## Related
- [[BrendanOLeary]] — speaker, Kilo Code
- [[KiloCode]] — company/product
- [[ArminRonacher]] — Flask creator, quoted
- [[DexHorthy]] — quoted on AI and thinking
- [[AndrejKarpathy]] — coined "context engineering"
- [[GitLab]] — Brendan's former employer
- [[AgenticEngineering]] — the core paradigm
- [[ContextEngineering]] — the art of curating context
- [[ResearchPlanImplement]] — structured workflow
- [[AIasJuniorDeveloper]] — mental model for AI agents
- [[AgentModes]] — ask/code/architect mode paradigm
- [[AgentsDotMd]] — de facto standard for agent project configuration
- [[ThreePhaseApproach]] — related workflow from Jake Nations
- [[MCP]] — Model Context Protocol, with context overhead concerns
- [[Context Management]] — related techniques
- [[Parallel Agents]] — context isolation strategy
- [[Skills]] — reusable agent playbooks
