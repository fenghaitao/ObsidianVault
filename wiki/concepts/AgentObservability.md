---
title: "Agent Observability"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind.md"]
last_updated: 2026-06-30
---

# Agent Observability

## Definition

Agent observability is the built-in capability to inspect AI agent runs, including every step (LLM call, tool call), its inputs, outputs, events, and timing. Mario Zechner cited the lack of observability as a primary reason for abandoning Claude Code: "There's zero observability because that's how the tool is constructed and I like knowing what my agents are doing."

## Key Information

### Mario Zechner's Perspective
- Claude Code has "zero observability" — a fundamental design limitation
- Mario: "I like knowing what my agents are doing"
- This lack of transparency was one of the key reasons he built Pi

### Workflow DevKit Perspective
- **What is observable**:
  - Every workflow run with its status (running, completed, failed, cancelled)
  - Every step within a run, displayed as spans with inputs and outputs
  - Events associated with each step
  - Timing and retry information
- **Access methods**:
  - **Local**: `npx workflow web` starts a local UI for inspecting runs
  - **Production**: `npx workflow web --backend <deployment-url>` connects to production runs
  - **API**: Programmatic access to run data for export to external monitoring (e.g., DataDog)
  - **CLI**: List, inspect, and cancel runs from the command line
- **Future capabilities**: OpenTelemetry span export for integration with existing observability stacks; end-to-end encryption for sensitive step data
- **Key insight**: Observability is a first-class feature, not an afterthought -- it comes automatically when using the workflow pattern

### Braintrust Perspective

Braintrust treats observability and evals as the same problem from a systems perspective. Observability is what you do after an agent reaches production — monitoring real user interactions to maintain confidence that the agent performs as expected. It forms one half of the "eval flywheel": production traces reveal real user behavior and failure modes, which feed back into offline evals for continuous improvement.

Key challenges of agent observability at scale:
- **Data velocity**: Production traffic generates traces at high speed
- **Data size**: Individual spans can be 10-20MB (vs. traditional spans at a few KB)
- **Structure**: Semi-structured to unstructured, heavy on text
- **Query patterns**: Need both low-latency point queries (viewing a trace) and aggregate analytics plus full-text search
- **Multimodal**: Traces may contain audio, video, and other media stored in object storage

### Raindrop Perspective

Raindrop frames agent observability as a paradigm shift from evals to production monitoring. Agents are non-deterministic, unbounded, and increasingly complex — running for hours with recursive sub-agents and exponentially growing tool sets. Traditional evals with golden datasets cannot cover the combinatorial input space.

Two categories of signals:
- **Explicit signals**: Error rate, latency, user regenerations, cost — objective and verifiable true/false
- **Implicit signals**: Regex patterns (e.g., Claude Code's leaked `keywords.ts`), classifier signals (refusals, user frustration, task failure, jailbreaking), and self-diagnostics (models introspecting on their own behavior)

The end goal is a continuous improvement flywheel: ship changes to a percentage of users → compare signal rates against control group → identify regressions → fix → repeat. Raindrop calls this "humanity's last problem" — when humans can no longer monitor agents and find issues.

### Microsoft Foundry Perspective

Microsoft Foundry (Amy Boyd & Nitya Narasimhan) frames agent observability through the "Mind the Gap" analogy, mapping to three dimensions:
- **Evaluation gap**: Between requirements (platform) and actual agent behavior (train) — agents drift as models, prompts, and environments change
- **Guardrails**: Warning signs that protect users and agents, like tube station "mind the gap" signs
- **Continuous monitoring**: Constant awareness across many agents over time

Foundry builds observability on **OpenTelemetry** with three phases: early build (tracing + evals from day one), debug/optimize in production (scheduled evals, red teaming, Azure Monitor integration), and fleet-wide management (centralized observability across many multi-agent systems).

Key innovations:
- **Trace-linked evaluations**: Traces and eval results visible together, shortening detection-to-diagnosis time
- **Agentic evaluators**: Intent resolution, tool call evaluation, task adherence — evaluating the agent holistically, not just individual LLM calls
- **Workflow agent observability**: Multi-agent traces show which specialist agent is underperforming
- **Observe Skill**: Coding agent automates the eval-optimize loop — generates datasets, runs evals, optimizes prompts, compares versions, rolls back to best
- **Agentic red teaming**: Proactive adversarial testing for agent-specific vulnerabilities like prohibited actions
- **Ask AI & Observability Agent**: Natural language interfaces for querying traces and logs in the portal

### Laurie Voss / Phoenix Perspective

Phoenix (Arize's open-source observability platform) captures every LLM call, tool call, and agent step with inputs and outputs at each point. It provides:
- **Auto-instrumentation**: Two lines of code (`import phoenix.otel` + `register()`) enable full tracing for Claude, OpenAI, Gemini, LangChain, CrewAI, and other frameworks via OpenInference integration packages
- **Trace visualization**: Nested span views showing the full execution tree — research steps, web searches, writing steps
- **Eval storage**: Evals are stored alongside traces, enabling filtering by score, latency, token count, and cost
- **Experiments**: Controlled comparison of prompt versions against datasets
- **Cloud option**: Phoenix Cloud requires no local installation — traces sent to `app.phoenix/s/<username>`

The observability loop: instrumentation → traces → evaluation → annotation → analysis → prompt improvement → repeat. This is the same loop as the eval flywheel — observability and evals are two sides of the same coin.

## Related

- [[WorkflowDevKit]]
- [[DurableAgents]]
- [[WorkflowPattern]]
- [[StepCaching]]
- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source (Braintrust perspective)
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source (Mario's critique)
- [[summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop]] — source (Raindrop perspective)
- [[Braintrust]] — agent quality platform
- [[Raindrop]] — agent observability platform
- [[EvalFlywheel]] — observability-evals loop
- [[TraceDataChallenges]] — data challenges of agent traces
- [[OnlineEvals]] — scoring functions on observability traffic
- [[ClaudeCode]] — criticized for zero observability; referenced for regex frustration detection
- [[MarioZechner]] — critic of Claude Code's lack of observability
- [[ContextOwnership]] — related transparency concern
- [[ImplicitSignals]] — semantic signal detection
- [[ExplicitSignals]] — objective signal detection
- [[SelfDiagnostics]] — model introspection for issue detection
- [[AgentExperiments]] — production A/B testing with signals
- [[UserFrustration]] — key implicit signal
- [[Trajectories]] — visual tool call topology
- [[TriageAgent]] — autonomous issue detection agent
- [[Microsoft Foundry]] — platform with built-in observability
- [[TraceLinkedEvaluations]] — linking evaluations to traces for diagnosis
- [[AgenticEvaluations]] — agent-specific evaluation metrics
- [[ObserveSkill]] — automated observability loop
- [[AgenticRedTeaming]] — adversarial testing for agents
- [[ContinuousEvaluation]] — evaluation throughout lifecycle
- [[OpenTelemetry]] — tracing standard
- [[summary-20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft]] — source (Microsoft Foundry perspective)
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source (Phoenix perspective)
- [[Phoenix]] — open-source observability platform
- [[Arize]] — commercial observability platform
- [[DataFlywheel]] — continuous improvement cycle
- [[TracesAndSpans]] — the data structure captured
- [[OpenTelemetry]] — instrumentation standard
- [[OpenInference]] — LLM-specific OTel extension
- [[Agent Trajectory Store]] — Google's custom trajectory store for coding agents
- [[summary-20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind]] — source (Google's custom observability)
