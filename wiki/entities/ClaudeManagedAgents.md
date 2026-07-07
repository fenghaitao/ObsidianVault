---
title: "ClaudeManagedAgents"
type: entity
tags: [product, claude, anthropic, agents, platform]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - Japan/01 - Code with Claude Tokyo 2026： Opening Keynote.md, "raw/01-articles/claude/2026-05-26 - Code w Claude London 2026 Rethinking how we build.md", "raw/01-articles/claude/2026-06-10 - The evolution of agentic surfaces building with Claude Managed Agents.md", "raw/01-articles/claude/2026-06-09 - New in Claude Managed Agents run agents on a schedule and store environment variables in vaults.md", "raw/01-articles/claude/2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon.md"]
last_updated: 2026-07-07
---

## Definition

Claude Managed Agents is Anthropic's product offering for building and deploying production AI agents at scale. It provides an agentic harness, context management tools, and production-grade infrastructure, purpose-built for Claude models.

## Key Information

- **Harness:** separates "brain" (decision-making) from "hands" (sandbox execution); outcome-based iteration with rubrics defining what good looks like.
- **Context:** 1M token context window, memory (file system for learnings across sessions), skills (self-written knowledge gap filling), dreaming (retrospective self-improvement from past trajectories).
- **Infrastructure:** auto-scaling sandboxes, agentic fleets for parallel work, scheduled deployments (cron-based), vaults for secure secret storage.
- **Customer adoption:** Notion (agent orchestration in-product), Asana (AI teammates alongside humans in projects), Rakuten (custom internal agents across engineering, product, sales, finance).
- **Customer metrics (June 2026)**: [[Notion]] runs its Custom Agents on Managed Agents — teams assign work from a task board, Claude picks up docs, meeting notes, and connected data, and finished code/decks/sites land back for review. Dozens of tasks run in parallel; an early prototype turned roughly twelve hours of work into twenty minutes. [[Rakuten]] shipped specialist agents across product, sales, marketing, and finance, each live within about a week. [[Sentry]] paired its Seer debugging agent with a Claude agent that writes the patch and opens the PR, built in weeks instead of months by a single engineer. [[Asana]] built AI Teammates that pick up tasks inside projects. Atlassian put developer agents into Jira workflows.
- **Dreaming:** agents look back over all past sessions, update memory and skills for better future performance.
- **Scheduled deployments:** agents can run on any cadence (nightly, weekly, etc.) without manual triggering.
- **Public beta (April 2026)**: launched into public beta on the Claude Platform. Composable APIs replace months of infra work (sandboxing, checkpointing, credential management, permissioning, tracing) with a built-in orchestration harness.
- **Feature set**: production-grade agents (secure sandboxing/auth/tool execution handled), long-running sessions (hours, persist through disconnections), multi-agent coordination (research preview — agents spin up/direct other agents to parallelize work), trusted governance (scoped permissions, identity management, execution tracing).
- **Benchmark**: internal testing on structured file generation showed up to a 10-point improvement in outcome task success vs. a standard prompting loop, with the largest gains on the hardest problems.
- **Console tooling**: session tracing, integration analytics, and troubleshooting guidance built into the Claude Console.
- **Pricing**: consumption-based — standard Claude Platform token rates plus $0.08/session-hour for active runtime.
- **Getting started**: a new CLI to deploy agents; also buildable via Claude Code plus a built-in "claude-api" Skill. The Claude Developer Console at platform.claude.com offers a quickstart that generates a production-ready agent from a template or plain-language description in minutes. Claude Code ships with the `/claude-api` skill providing up-to-date reference material; run `/claude-api managed-agents-onboard` for an interview-driven walkthrough.
- **Three primary API resources (June 2026)**: (1) **Agents** — a configuration bundling a model, prompt, tools, and guardrails. (2) **Environments** — the execution context: sandbox container, networking rules, and pre-installed packages, hosted on Anthropic cloud or self-hosted infrastructure. (3) **Sessions** — pairs an agent with an environment in an isolated sandbox instance; persists full event history, sandbox state, and outputs server-side so long-running work can pause, resume cleanly, and be traced step by step.
- **Latency improvement**: decoupling brain from hands allows Claude to begin reasoning while the sandbox spins up in parallel. Sessions that never run a tool skip the container entirely. Time-to-first-token improved ~60% at p50 and >90% at p95 in Anthropic's testing.
- **Vaults with envelope encryption**: credentials for MCPs, CLIs, and GitHub repos live in a separate vault outside the sandbox. A proxy fetches and decrypts them only on demand, protected with envelope encryption before storage; retrieval requires a signed request token for verification. This keeps credentials out of the sandbox entirely, mitigating prompt injection risks.
- **Claude Developer Console observability**: a native visual timeline view of agent sessions with deep debugging — scrub the timeline, open any step, and read its raw payload. Because sessions are append-only event logs, every model call, tool call, and result is reconstructable.
- **Harness evolution principle**: the harness must evolve alongside model intelligence. A fix for [[ContextAnxiety]] on [[Claude4.5Sonnet|Claude Sonnet 4.5]] (context resets) became pure overhead on [[Claude4.7Opus|Claude Opus 4.5]], where the behavior disappeared. Managed Agents absorbs this evolution so teams don't maintain model-specific harness tuning.
- **Internal PM dogfooding (April 2026)**: Jess Yan, the product's own PM, builds bespoke Managed Agents in Claude Code to automate her operational workflow (long-tail "jobs to be done" that previously couldn't scale) and to prototype against pre-production API specs before they ship, surfacing API/Console UX problems earlier than doc review or user feedback would. See [[summary-2026-04-29 - Product development in the agentic era]].
- **Customer roster (April 2026)**: Notion, Rakuten, Asana, [[Vibecode]], and [[Sentry]] cited as teams shipping production use cases 10x faster.
- **Memory public beta (April 23, 2026)**: memory feature (a separate dated announcement from the April 8 general production beta) reached public beta — filesystem-mounted, exportable/API-managed memory files with scoped permissions, audit logs, version rollback, and redaction; multiple agents can work concurrently against a shared store without overwriting each other; updates surface in the Console as session events. See [[AgenticMemory]].
- **Additional memory customers (April 2026)**: [[Wisedocs]] (document-verification pipeline) and [[Ando]] (workplace messaging platform) join the customer roster, using memory rather than building custom retrieval/memory infrastructure.
- **Vaults for MCP OAuth (April 2026)**: Vaults register a user's MCP OAuth tokens once; developers reference the vault by ID at session creation and the platform injects the right credentials into each MCP connection and refreshes them automatically — no custom secret store or per-call token passing needed. See [[ModelContextProtocol]].
- **Four new features (announced at Code w/ Claude SF 2026, May 2026)**: a further set of capabilities for building/deploying cloud-hosted agents at scale was announced at the conference and made available to all developers; the recap article only teases the count and links to a separate, not-yet-ingested blog post ("new-in-claude-managed-agents") for specifics. See [[summary-2026-05-12 - Code w Claude SF 2026 recap Building on the AI exponential]].
- **Self-hosted sandboxes and MCP tunnels (May 19, 2026)**: two features keep agent execution and tool access inside the customer's security perimeter. **Self-hosted sandboxes** (public beta) move tool execution to infrastructure the customer controls — their own servers or a managed provider ([[Cloudflare]], [[Daytona]], [[Modal]], [[Vercel]]) — while the agent loop (orchestration, context management, error recovery) stays on Anthropic's infrastructure; the customer's existing network policies, audit logging, and security tooling apply automatically, files/repositories never leave the perimeter, and the customer sets compute sizing and runtime image. **MCP tunnels** (research preview) let agents reach [[ModelContextProtocol|MCP]] servers inside a private network (internal databases, private APIs, knowledge bases, ticketing systems) without exposing them publicly, via a lightweight customer-deployed gateway making one outbound, end-to-end-encrypted connection (no inbound firewall rules, no public endpoints); supported in both Managed Agents and the Messages API, and managed from workspace settings in the Claude Console by organization admins. These capabilities were also highlighted at [[CodeWithClaude|Code w/ Claude London 2026]] (May 20–21), with [[Amplitude]], [[Clay]], and [[Rogo]] confirmed as building on Managed Agents with self-hosted sandboxes. See [[summary-2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels]], [[summary-2026-05-26 - Code w Claude London 2026 Rethinking how we build]], [[Sandboxing]].
- **Dreaming launches as research preview (May 19, 2026)**: a scheduled process that reviews past agent sessions and memory stores, extracts patterns (recurring mistakes, workflows agents converge on, team-shared preferences), and curates memory so agents self-improve over time. Developers choose the autonomy level — dreaming can update memory automatically or route changes through human review first. Complements real-time memory: memory captures learning *as* an agent works, dreaming refines it *between* sessions — especially useful for long-running work and multiagent orchestration. Request access via Anthropic's form. See [[AgenticMemory]].
- **Outcomes reaches public beta (May 19, 2026)**: developers write a rubric describing success; a separate grader (previously introduced as research-preview "outcome-based mode" in the April 8 launch) evaluates the output against the rubric in its own context window, isolated from the agent's own reasoning, pinpoints what needs to change, and the agent retries. Especially useful for tasks needing exhaustive coverage or subjective quality judgment (brand voice, visual/design guidelines). Confirms the April benchmark (up to 10-point task-success improvement over a standard prompting loop, largest gains on the hardest problems) and adds file-type detail: +8.4% task success on `.docx` generation, +10.1% on `.pptx` generation. Outcomes can now be paired with a **webhook** that fires a notification when a run completes, so developers don't need to poll.
- **Multiagent orchestration reaches public beta (May 19, 2026)**: previously research preview (per the April 8 launch); now a lead agent can break work into pieces and delegate each to a specialist with its own model, prompt, and tools. Specialists work in parallel on a **shared filesystem** and contribute to the lead agent's overall context. Because events are persistent, the lead agent can check back in with subagents mid-workflow, and every step is traceable in the Claude Console (which agent did what, in what order, and why). See [[MultiAgentSystem]].
- **Customer evidence for dreaming/outcomes/multiagent orchestration (May 2026)**: [[Harvey]] uses dreaming so agents remember filetype workarounds and tool-specific patterns between long-form legal-drafting sessions, driving a ~6x completion-rate increase. [[Netflix]]'s platform team built a multiagent log-analysis agent that processes builds from hundreds of sources in parallel to surface only recurring, actionable issues. [[Spiral]] (built by [[Every]]) runs a Haiku-led, Opus-subagent writing agent that uses multiagent orchestration for parallel drafting and outcomes (rubric graded against editorial principles + memory-stored user voice) to gate what's returned. [[Wisedocs]] built a document quality-check agent using outcomes to grade reviews against internal guidelines. See [[summary-2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration]].
- **Scheduled deployments public beta (June 9, 2026)**: agents can now run on a cron schedule with no scheduler for the developer to build or host. Each fire starts a new session. Once live, a deployment can be paused, resumed, archived, or triggered on demand. See [[ScheduledDeployments]].
- **Scheduled deployments customers (June 2026)**: [[Rakuten]] uses scheduled deployments for weekly/monthly spreadsheet analysis and report/deck generation, plus production log and metrics monitoring so PMs see application health without dashboards. [[ActivelyAI]] replaced its own scheduling infrastructure with scheduled deployments to refresh agentic search answers regularly. [[Ando]] uses scheduled deployments so agents autonomously watch channels for proposed next steps, follow up when due, and send meeting reminders.
- **Environment variable vaults public beta (June 9, 2026)**: vaults (previously MCP OAuth only) now support environment variables, enabling CLI tools and other shell-based integrations to make authenticated API calls. The agent never sees the real key — the sandbox holds only a placeholder; the real key is injected at the network boundary and only on requests to approved domains. Key rotation is seamless: update the vault and running sessions pick up the new value on their next call. See [[AgenticVaults]].
- **CLI vault customers (June 2026)**: [[Notion]] uses vaults to roll out its CLI alongside MCP tools, adding file-upload capabilities without tokens ever reaching the model. [[Browserbase]] built its public catalog of browser skills using the browse CLI authenticated through vaults, with a scheduled deployment validating the catalog periodically. [[KERNEL]] uses vaults to connect agents to databases tracking usage and customer conversations, flagging usage surges as they happen. [[Milana]] uses vaults to securely connect its AI product engineer to customer codebases for automated bug finding and fixing.
- **Browser capabilities via CLI vaults**: [[Browserbase]] and [[KERNEL]] CLIs, authenticated through vaults, give Managed Agents browser capabilities for the first time, enabling agents to navigate and interact with the web alongside their other tools.

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
- [[summary-2026-05-26 - Code w Claude London 2026 Rethinking how we build]] — London 2026 recap highlighting Managed Agents adoption
- [[Amplitude]] — London 2026 confirmed Managed Agents customer
- [[Clay]] — London 2026 confirmed Managed Agents customer
- [[Rogo]] — London 2026 confirmed Managed Agents customer
- [[summary-2026-06-10 - The evolution of agentic surfaces building with Claude Managed Agents]] — architectural deep-dive on brain/hands decoupling, three-resource API, latency, and vaults
- [[summary-2026-06-09 - New in Claude Managed Agents run agents on a schedule and store environment variables in vaults]] — scheduled deployments and environment variable vaults announcement
- [[ScheduledDeployments]] — cron-based agent scheduling concept
- [[AgenticVaults]] — secure credential management for agents
- [[Browserbase]] — browser capabilities and CLI vaults customer
- [[KERNEL]] — browser capabilities and CLI vaults customer
- [[Milana]] — AI product engineer using vaults for codebase access
- [[ActivelyAI]] — agentic search customer using scheduled deployments
- [[AgenticSurfaces]] — the evolution of agent-building interfaces culminating in Managed Agents
- [[ContextAnxiety]] — model behavior pattern that illustrates why harnesses must evolve alongside models
- [[ARIA]] — Best Use of Claude Managed Agents prize winner in the Built with Opus 4.7 hackathon
- [[Medkit]] — hackathon winner using Managed Agents for agentic grading of medical simulations
- [[summary-2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon]] — hackathon source summary
- [[summary-01 - Ship your first Managed Agent]] — source summary
- [[summary-11 - Memory and dreaming for self learning agents]] — source summary
