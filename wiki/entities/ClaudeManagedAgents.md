---
title: "ClaudeManagedAgents"
type: entity
tags: [product, claude, anthropic, agents, platform]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - Japan/01 - Code with Claude Tokyo 2026： Opening Keynote.md]
last_updated: 2026-07-04
---

## Definition

Claude Managed Agents is Anthropic's product offering for building and deploying production AI agents at scale. It provides an agentic harness, context management tools, and production-grade infrastructure, purpose-built for Claude models.

## Key Information

- **Harness:** separates "brain" (decision-making) from "hands" (sandbox execution); outcome-based iteration with rubrics defining what good looks like.
- **Context:** 1M token context window, memory (file system for learnings across sessions), skills (self-written knowledge gap filling), dreaming (retrospective self-improvement from past trajectories).
- **Infrastructure:** auto-scaling sandboxes, agentic fleets for parallel work, scheduled deployments (cron-based), vaults for secure secret storage.
- **Customer adoption:** Notion (agent orchestration in-product), Asana (AI teammates alongside humans in projects), Rakuten (custom internal agents across engineering, product, sales, finance).
- **Dreaming:** agents look back over all past sessions, update memory and skills for better future performance.
- **Scheduled deployments:** agents can run on any cadence (nightly, weekly, etc.) without manual triggering.
- **Public beta (April 2026)**: launched into public beta on the Claude Platform. Composable APIs replace months of infra work (sandboxing, checkpointing, credential management, permissioning, tracing) with a built-in orchestration harness.
- **Feature set**: production-grade agents (secure sandboxing/auth/tool execution handled), long-running sessions (hours, persist through disconnections), multi-agent coordination (research preview — agents spin up/direct other agents to parallelize work), trusted governance (scoped permissions, identity management, execution tracing).
- **Benchmark**: internal testing on structured file generation showed up to a 10-point improvement in outcome task success vs. a standard prompting loop, with the largest gains on the hardest problems.
- **Console tooling**: session tracing, integration analytics, and troubleshooting guidance built into the Claude Console.
- **Pricing**: consumption-based — standard Claude Platform token rates plus $0.08/session-hour for active runtime.
- **Getting started**: a new CLI to deploy agents; also buildable via Claude Code plus a built-in "claude-api" Skill.
- **Internal PM dogfooding (April 2026)**: Jess Yan, the product's own PM, builds bespoke Managed Agents in Claude Code to automate her operational workflow (long-tail "jobs to be done" that previously couldn't scale) and to prototype against pre-production API specs before they ship, surfacing API/Console UX problems earlier than doc review or user feedback would. See [[summary-2026-04-29 - Product development in the agentic era]].
- **Customer roster (April 2026)**: Notion, Rakuten, Asana, [[Vibecode]], and [[Sentry]] cited as teams shipping production use cases 10x faster.
- **Memory public beta (April 23, 2026)**: memory feature (a separate dated announcement from the April 8 general production beta) reached public beta — filesystem-mounted, exportable/API-managed memory files with scoped permissions, audit logs, version rollback, and redaction; multiple agents can work concurrently against a shared store without overwriting each other; updates surface in the Console as session events. See [[AgenticMemory]].
- **Additional memory customers (April 2026)**: [[Wisedocs]] (document-verification pipeline) and [[Ando]] (workplace messaging platform) join the customer roster, using memory rather than building custom retrieval/memory infrastructure.
- **Vaults for MCP OAuth (April 2026)**: Vaults register a user's MCP OAuth tokens once; developers reference the vault by ID at session creation and the platform injects the right credentials into each MCP connection and refreshes them automatically — no custom secret store or per-call token passing needed. See [[ModelContextProtocol]].
- **Four new features (announced at Code w/ Claude SF 2026, May 2026)**: a further set of capabilities for building/deploying cloud-hosted agents at scale was announced at the conference and made available to all developers; the recap article only teases the count and links to a separate, not-yet-ingested blog post ("new-in-claude-managed-agents") for specifics. See [[summary-2026-05-12 - Code w Claude SF 2026 recap Building on the AI exponential]].
- **Self-hosted sandboxes and MCP tunnels (May 19, 2026)**: two features keep agent execution and tool access inside the customer's security perimeter. **Self-hosted sandboxes** (public beta) move tool execution to infrastructure the customer controls — their own servers or a managed provider ([[Cloudflare]], [[Daytona]], [[Modal]], [[Vercel]]) — while the agent loop (orchestration, context management, error recovery) stays on Anthropic's infrastructure; the customer's existing network policies, audit logging, and security tooling apply automatically, files/repositories never leave the perimeter, and the customer sets compute sizing and runtime image. **MCP tunnels** (research preview) let agents reach [[ModelContextProtocol|MCP]] servers inside a private network (internal databases, private APIs, knowledge bases, ticketing systems) without exposing them publicly, via a lightweight customer-deployed gateway making one outbound, end-to-end-encrypted connection (no inbound firewall rules, no public endpoints); supported in both Managed Agents and the Messages API, and managed from workspace settings in the Claude Console by organization admins. See [[summary-2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels]], [[Sandboxing]].
- **Dreaming launches as research preview (May 19, 2026)**: a scheduled process that reviews past agent sessions and memory stores, extracts patterns (recurring mistakes, workflows agents converge on, team-shared preferences), and curates memory so agents self-improve over time. Developers choose the autonomy level — dreaming can update memory automatically or route changes through human review first. Complements real-time memory: memory captures learning *as* an agent works, dreaming refines it *between* sessions — especially useful for long-running work and multiagent orchestration. Request access via Anthropic's form. See [[AgenticMemory]].
- **Outcomes reaches public beta (May 19, 2026)**: developers write a rubric describing success; a separate grader (previously introduced as research-preview "outcome-based mode" in the April 8 launch) evaluates the output against the rubric in its own context window, isolated from the agent's own reasoning, pinpoints what needs to change, and the agent retries. Especially useful for tasks needing exhaustive coverage or subjective quality judgment (brand voice, visual/design guidelines). Confirms the April benchmark (up to 10-point task-success improvement over a standard prompting loop, largest gains on the hardest problems) and adds file-type detail: +8.4% task success on `.docx` generation, +10.1% on `.pptx` generation. Outcomes can now be paired with a **webhook** that fires a notification when a run completes, so developers don't need to poll.
- **Multiagent orchestration reaches public beta (May 19, 2026)**: previously research preview (per the April 8 launch); now a lead agent can break work into pieces and delegate each to a specialist with its own model, prompt, and tools. Specialists work in parallel on a **shared filesystem** and contribute to the lead agent's overall context. Because events are persistent, the lead agent can check back in with subagents mid-workflow, and every step is traceable in the Claude Console (which agent did what, in what order, and why). See [[MultiAgentSystem]].
- **Customer evidence for dreaming/outcomes/multiagent orchestration (May 2026)**: [[Harvey]] uses dreaming so agents remember filetype workarounds and tool-specific patterns between long-form legal-drafting sessions, driving a ~6x completion-rate increase. [[Netflix]]'s platform team built a multiagent log-analysis agent that processes builds from hundreds of sources in parallel to surface only recurring, actionable issues. [[Spiral]] (built by [[Every]]) runs a Haiku-led, Opus-subagent writing agent that uses multiagent orchestration for parallel drafting and outcomes (rubric graded against editorial principles + memory-stored user voice) to gate what's returned. [[Wisedocs]] built a document quality-check agent using outcomes to grade reviews against internal guidelines. See [[summary-2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration]].

## Related

- [[summary-01 - Code with Claude Tokyo 2026： Opening Keynote]] — launch keynote
- [[summary-2026-04-08 - Claude Managed Agents get to production 10x faster]] — public-beta launch article
- [[Vibecode]] — customer building production agents on the platform
- [[Sentry]] — customer building production agents on the platform
- [[ClaudeFable5]] — the model optimized for Managed Agents
- [[ClaudeCode]] — the developer-facing agent tool
- [[Anthropic]] — the company behind the platform
- [[analysis-claude-product-landscape]] — comparison with Claude Code and Claude Cowork
- [[analysis-agent-evolution-loop-to-self-learning]] — the evolution from agentic loop to self-learning agents
- [[summary-13 - Introducing Claude Managed Agents]] — product-launch teaser announcing the product
- [[summary-05 - New agents for financial services ｜ Claude Cowork + Claude Managed Agents]] — financial-services agents launch
- [[summary-2026-04-23 - Built-in memory for Claude Managed Agents]] — memory public-beta launch article
- [[Wisedocs]] — memory customer, document-verification pipeline
- [[Ando]] — memory customer, workplace messaging platform
- [[ModelContextProtocol]] — protocol behind the Vaults OAuth credential feature
- [[summary-2026-04-29 - Product development in the agentic era]] — PM dogfooding: prototyping and shipping custom agents via Claude Code + Managed Agents
- [[summary-2026-05-12 - Code w Claude SF 2026 recap Building on the AI exponential]] — Code w/ Claude SF 2026 recap teasing four new features
- [[summary-2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels]] — self-hosted sandboxes and MCP tunnels launch article
- [[Daytona]] — self-hosted sandbox provider
- [[Modal]] — self-hosted sandbox provider
- [[Vercel]] — self-hosted sandbox provider
- [[summary-2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration]] — dreaming, outcomes, multiagent orchestration, and webhooks launch article
- [[Harvey]] — dreaming customer example
- [[Netflix]] — multiagent orchestration customer example
- [[Spiral]] — outcomes and multiagent orchestration customer example
- [[Every]] — company behind Spiral
- [[MultiAgentSystem]] — the coordination pattern productized as multiagent orchestration
