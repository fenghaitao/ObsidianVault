---
title: "SubAgent"
type: concept
tags: [concept, agents, architecture, specialization]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260202 - Turn Claude Code into Your Full Engineering Team with Subagents.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260216 - How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260226 - This One Command Makes Coding Agents Find All Their Mistakes (Use it Now).md"
last_updated: 2026-06-20
---

## Definition

A sub-agent is a specialized [[AIAgent]] invoked by a primary (orchestrator) agent to handle a narrow part of a larger task. The primary agent decides *which* sub-agent to call (based on each sub-agent's tool description); the sub-agent then handles its own narrow tool surface and returns results to the primary.

## Key Information

### The core problem sub-agents solve

LLMs degrade as you give them more tools or longer system prompts. Cole demonstrates this concretely in the MCP Agent Army:

- **Bad approach**: one agent with 30+ tools across Brave, GitHub, Slack, Airtable, Filesystem, Firecrawl. The LLM gets overwhelmed picking among them.
- **Good approach**: 6 sub-agents, each owning ~5 tools for one MCP server. The primary agent picks among 6 sub-agents, not 30 tools. Each sub-agent picks from its narrow tool set.

### Two structural patterns Cole demonstrates

#### 1. Sub-agents as MCP-server-handlers (MCP Agent Army)

Each sub-agent owns the tools of one [[ModelContextProtocol]] server. The primary agent dispatches based on the request domain.

```
User → Primary agent
       ├─ "search the web"  → Brave sub-agent
       ├─ "list my repos"   → GitHub sub-agent
       └─ "save to Airtable" → Airtable sub-agent
```

#### 2. Sub-agents as parallel specialists (Travel Planner)

Multiple sub-agents run *simultaneously* on different facets of the same problem. See [[ParallelAgentArchitecture]].

```
User → Info gatherer →┬→ Flight sub-agent ─┐
                      ├→ Hotel sub-agent  ─┤→ Synthesizer → User
                      └→ Activity sub-agent ┘
```

### MCP-as-sub-agent (the meta-pattern)

[[Archon]] takes this to another level: Archon itself is wrapped as an MCP server, becoming a sub-agent that AI IDEs ([[Windsurf]], [[Cursor]]) invoke when they need PydanticAI/LangGraph code generation. The IDE plays primary-agent; Archon plays sub-agent.

This is the pattern Cole calls "the next evolution of AI IDEs" — generalists delegating to framework specialists over MCP.

#### 3. Sub-agents as a harness "tool belt" (context isolation)

In an [[AgentHarness]] (see `summary-full-engineering-team-subagents`), dedicated **service sub-agents** — one each for Linear, GitHub, Slack — let the orchestrator delegate non-coding work *without* loading those tools into its own context window. Two benefits beyond routing:

- **Context isolation**: the orchestrator's precious context stays lean; the Linear/GitHub/Slack tool surfaces live inside their sub-agents.
- **Per-agent model selection**: each sub-agent can run a different model via the [[ClaudeAgentSDK]] — e.g. Haiku for fast, cheap Linear updates, Sonnet/Opus for coding — tuning cost and speed per role.

```
Orchestrator → Linear sub-agent  (Haiku)  — tasks
             → GitHub sub-agent  (Haiku)  — commits/PRs
             → Slack sub-agent   (Haiku)  — progress updates
             → coding work       (Sonnet/Opus)
```

### Evolution: [[AgentTeams]] (communicating sub-agents)

Sub-agents' key limitation is that they **don't communicate** — they run in parallel and each reports back only to the main agent, which aggregates. [[ClaudeCode]]'s **[[AgentTeams]]** feature (Opus 4.6, 2026) removes that limit: teammate agents share a task list and message each other (and the lead), coordinating who does what. Agent Teams is "where this is going" — but as of early 2026 it's experimental, non-deterministic, token-heavy, and lacks observability. See [[AgentTeams]].

### Tool description as contract

A sub-agent's docstring (or, more generally, the description registered with the primary agent) is the contract. The primary agent reads it to decide *when* to invoke the sub-agent. Good descriptions matter as much as good prompts at this boundary.

### Trade-offs

- **Pro**: dramatically reduces hallucination on complex multi-domain tasks.
- **Pro**: each sub-agent can be tested and iterated independently.
- **Use research sub-agents for parallel discovery.** Cole's `/e2e-test` skill (`summary-self-healing-e2e-validation`) launches **three sub-agents in parallel** at the start — app-structure/user-journeys, DB schema, and a bug-hunt code review — each loading large context but returning only a compact summary to the primary agent. This is the canonical "research, not implementation" use of sub-agents.
- **Con**: more LLM calls — the orchestrator's call plus each sub-agent's call. Latency and token cost rise.
- **Con**: orchestrator must reliably route — if the description is ambiguous, dispatch is wrong.

## Related

- [[AIAgent]] — what a sub-agent is
- [[ParallelAgentArchitecture]] — pattern using parallel sub-agents
- [[ModelContextProtocol]] — common transport for sub-agents
- [[ToolUse]] — what each sub-agent's surface consists of
- [[Archon]] — example: Archon-as-sub-agent for AI IDEs
- [[Windsurf]], [[Cursor]] — primary-agent role in MCP-as-sub-agent pattern
- [[ColeMedin]] — author of all these demos
- [[AgentHarness]] — sub-agents as a service tool belt with context isolation
- [[AgentTeams]] — communicating sub-agents (the 2026 evolution)
- [[ClaudeAgentSDK]] — defines sub-agents (incl. per-agent model) in code
- [[summary-build-an-army-of-ai-agents-archon]] — MCP Agent Army demo
- [[summary-coding-subagents-mcp-evolution]] — MCP-as-sub-agent thesis
- [[summary-full-engineering-team-subagents]] — sub-agents as a harness tool belt
- [[summary-agent-teams-live-build]] — Agent Teams, the communicating evolution
- [[summary-self-healing-e2e-validation]] — three parallel research sub-agents in practice
