---
title: "MultiAgentSystem"
type: concept
tags: [multi-agent, orchestration, subagents, context-engineering, architecture]
sources: ["raw/01-articles/claude/2026-01-23 - Building multi-agent systems When and how to use them.md", "raw/01-articles/claude/2026-01-28 - How leading retailers are turning AI pilots into enterprise-wide transformation.md"]
last_updated: 2026-07-04
---

## Definition

A multi-agent system is an architecture where multiple LLM instances run with separate conversation contexts, coordinated through code. Anthropic's guidance focuses on the **orchestrator-subagent pattern** — a hierarchical model where a lead agent spawns and manages specialized subagents for specific subtasks — as a straightforward starting point, distinct from agent-swarm, capability-based, or message-bus coordination patterns. A April 2026 follow-up article names and contrasts five concrete coordination patterns implementing this space — generator-verifier, orchestrator-subagent, agent teams, message bus, and shared state — arranged from centralized/bounded to decentralized/autonomous. See [[summary-2026-04-10 - Multi-agent coordination patterns Five approaches and when to use them]].

## Key Information

- **Default to single-agent**: a well-designed single agent with the right tools handles most enterprise workflows; multi-agent systems introduce coordination overhead — typically 3-10x more tokens than an equivalent single-agent approach, from duplicated context, coordination messages, and result summarization across handoffs.
- **Three scenarios where multi-agent systems consistently win**:
  1. **Context pollution isolation** — a subtask generating high context volume (1000+ tokens) that's mostly irrelevant to the main task (e.g., an order-history lookup during a technical support conversation) is delegated to a subagent that returns only a compact summary, keeping the main agent's context focused.
  2. **Parallelizable tasks** — a lead agent decomposes a query into independent facets and runs subagents concurrently (Anthropic's [[Research]] feature works this way); the benefit is thoroughness/coverage, not necessarily speed, since total token/compute cost rises.
  3. **Specialization** — different tasks need different toolsets, personas, or domain context (e.g., a CRM agent vs. a marketing-automation agent with 8-10 focused tools each, rather than one agent juggling 40+ tools across platforms).
- **Concrete adoption signals**: approaching context limits (though compaction is reducing this constraint), managing 15-20+ tools (try the Tool Search Tool first — up to 85% token reduction via on-demand discovery — before splitting agents), and subtasks that naturally decompose into independent pieces.
- **Context-centric decomposition (not problem-centric)**: split along context boundaries, not work-type boundaries. Splitting by role (one agent plans, one implements, one tests, one reviews) creates a "telephone game" where each handoff loses fidelity — in one experiment, role-specialized subagents spent more tokens coordinating than executing. An agent handling a feature should also handle its own tests, since it already holds the relevant context.
- **Verification subagents**: a dedicated agent whose sole job is testing/validating the main agent's output. Effective because verification needs minimal context transfer — the verifier blackbox-tests an artifact against explicit success criteria without needing to know how it was built. More capable orchestrators (e.g., Claude Opus 4.5) increasingly evaluate subagent work directly without this step, but it remains valuable with weaker orchestrators or specialized verification tooling. Primary failure mode: a verifier declaring success after shallow testing — mitigated by requiring complete test-suite runs and explicit pass/fail criteria.
- **Default advice**: start with the simplest single-agent approach that works, and add multi-agent complexity only when evidence — not intuition — supports it.

## Five Coordination Patterns (April 2026)

A follow-up to the January 2026 post above names five patterns for *how* agents coordinate once multi-agent is chosen, recommending starting with the simplest and evolving as limitations surface:

- **Generator-Verifier**: broader framing of this page's "verification subagent" concept — a generator produces output, a verifier accepts or returns feedback, looping until acceptance or a max-iteration cap. Best for code generation, fact-checking, rubric grading, compliance checks. Fails when the verifier's criteria are underspecified (rubber-stamping) or when generation/evaluation require the same skill.
- **Orchestrator-Subagent**: this page's existing default pattern. Newly identified limitations: the orchestrator becomes an information bottleneck when one subagent's finding is relevant to another's work, and unparallelized sequential dispatch incurs multi-agent token costs without a speed benefit.
- **Agent Teams**: distinguished from orchestrator-subagent by **worker persistence** — a coordinator assigns work to teammates that stay alive across many assignments (vs. a subagent dispatched for one bounded task that then terminates), accumulating domain context over time. Best for independent subtasks needing sustained multi-step work (e.g., migrating each service of a codebase independently). Fails on inter-teammate information sharing, completion-time variance, and shared-resource (same file/DB) conflicts.
- **Message Bus**: agents publish/subscribe to topics via a shared router, letting new agent types join without rewiring connections. Best for event-driven pipelines with a growing agent ecosystem (e.g., security-alert triage). Harder to trace/debug than sequential orchestration; misrouted or dropped events fail silently.
- **Shared State**: agents read/write a persistent shared store directly, with no central coordinator — removes the single point of failure that orchestrators and message-bus routers introduce, at the cost of predictability. Best for accumulating a shared knowledge base (e.g., multi-angle research synthesis). Main failure mode is **reactive loops** (agents ping-ponging on each other's writes without converging), which need first-class termination conditions (time budget, convergence threshold, or a designated "sufficient answer" judge) rather than being treated as an afterthought.

See [[summary-2026-04-10 - Multi-agent coordination patterns Five approaches and when to use them]].

## Production Example: L'Oréal (January 2026)

[[LOreal|L'Oréal]] built a multi-agent system with Claude at the core, orchestrating 15+ specialized agents that transform natural-language user questions into insights and visualizations for 44,000 employees across 150 countries — an enterprise-scale instance of the orchestrator-subagent pattern.

## Production Example: Respiro (May 2026)

At the opposite end of scale from L'Oréal's enterprise deployment, a single non-technical builder ([[Respiro]], built by project manager Kostiantyn Vlasenko with [[ClaudeCode]]) independently arrived at the same 15+ specialized-subagent orchestrator-subagent pattern (TCA architect, Swift developer, Metal specialist, code reviewer, and more running in parallel across modules) — illustrating the pattern's applicability from solo hackathon projects to 44,000-employee rollouts alike.

## Agent Teams (Claude Code, March 2026)

Lets users coordinate multiple Claude Code instances working together; validated internally via a hand-crafted eval suite (built by engineer Conner) to understand when the feature works well, when it doesn't, and what to fix — an example of evals substituting for a written spec during feature development. See [[summary-2026-03-19 - Product management on the AI exponential]].

## Claude Managed Agents Multi-Agent Coordination (April–May 2026)

Claude Managed Agents' multi-agent coordination (research preview, announced 2026-04-08): agents can spin up and direct other agents to parallelize complex work, a productized instance of the orchestrator-subagent pattern at the platform level. See [[ClaudeManagedAgents]] and [[summary-2026-04-08 - Claude Managed Agents get to production 10x faster]].

**Reaches public beta as "multiagent orchestration" (May 19, 2026)**: a lead agent breaks a job into pieces and delegates each to a specialist with its own model, prompt, and tools. Specialists work in parallel on a **shared filesystem** and contribute back to the lead agent's overall context. Because events are persistent, the lead agent can check back in with subagents mid-workflow — every agent remembers what it's done — and every step is traceable in the Claude Console (which agent did what, in what order, and why), addressing the visibility gap that ad-hoc orchestration usually has. Production examples: [[Netflix]]'s platform team runs a log-analysis agent that fans out across batches of build logs from hundreds of sources in parallel to surface only recurring, actionable patterns; [[Spiral]] (built by [[Every]]) runs a lead agent on Claude Haiku that delegates drafting to parallel subagents on Claude Opus, then gates output through an "outcomes" rubric grader (see [[ClaudeManagedAgents]]) — a concrete instance of the Generator-Verifier pattern above, productized. See [[summary-2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration]].

## Knowledge Conflicts

- This page's "Context-centric decomposition" guidance above states that splitting subagents by role/sequential stage causes a "telephone game" of fidelity loss, and should be avoided in favor of context-boundary splits. A April 2026 article ([[summary-2026-04-07 - How and when to use subagents in Claude Code]]) recommends subagents for **sequential multi-stage pipelines** (design → implement → test) as a good use case, provided handoffs go through **files** (e.g. `docs/api-spec.md`) rather than conversational summaries. This may be a reconciling nuance (file-based handoffs avoid the fidelity loss that conversational-summary handoffs suffer) rather than a true contradiction, but the two sources give unqualified opposite verdicts on "sequential pipelines" as a pattern, so it's flagged here rather than silently merged.
- *Note (April 2026):* the companion "five patterns" article ([[summary-2026-04-10 - Multi-agent coordination patterns Five approaches and when to use them]]) separately observes that orchestrator-subagent's **unparallelized sequential execution** limits throughput — but this is a runtime-dispatch-order concern (subagents run one after another), distinct from the role/stage-decomposition fidelity-loss debate above (design→implement→test subagents). Treated as adjacent, not resolving, the existing conflict.

## Related

- [[ClaudeCodeSubagents]] — Claude Code's own subagent implementation, exemplifying context isolation and verification patterns
- [[Respiro]] — solo-builder production example of the orchestrator-subagent pattern at hackathon/indie-app scale
- [[LOreal]] — production customer example at enterprise scale
- [[summary-2026-01-28 - How leading retailers are turning AI pilots into enterprise-wide transformation]] — source article for the L'Oréal example
- [[AgentWorkflowPatterns]] — the sequential/parallel/evaluator-optimizer patterns for *shaping* a multi-agent system once adopted
- [[CodeReview]] — production example of the parallel pattern (multiple review agents dispatched per PR)
- [[ContextEngineering]] — the discipline underlying context-centric decomposition
- [[Research]] — Anthropic's parallel multi-agent research feature
- [[AgenticCoding]] — the broader practice this pattern operates within
- [[summary-2026-01-23 - Building multi-agent systems When and how to use them]] — source article
- [[ClaudeCode]] — product where the agent teams feature ships
- [[summary-2026-03-19 - Product management on the AI exponential]] — agent teams / evals-over-spec source
- [[ClaudeManagedAgents]] — productizes multi-agent coordination as a research-preview feature
- [[summary-2026-04-08 - Claude Managed Agents get to production 10x faster]] — multi-agent coordination source
- [[ClaudeCodeSubagents]] — sequential-pipeline handoff guidance in tension with this page's context-centric decomposition guidance
- [[summary-2026-04-07 - How and when to use subagents in Claude Code]] — source of the sequential-pipeline conflict
- [[summary-2026-04-10 - Multi-agent coordination patterns Five approaches and when to use them]] — five-pattern coordination taxonomy (generator-verifier, orchestrator-subagent, agent teams, message bus, shared state)
- [[summary-2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration]] — multiagent orchestration reaches public beta, with shared-filesystem and Console-tracing detail
- [[Netflix]] — multiagent orchestration customer example (parallel log analysis)
- [[Spiral]] — multiagent orchestration + outcomes customer example (Haiku lead, Opus subagents)
- [[Every]] — company behind Spiral
