---
title: "summary-20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize"
type: source
tags: [source, transcript, observability, evals, experimentation, arize, phoenix, arize-ax, open-telemetry, agents, harness, traces, spans, sessions]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize.md"]
last_updated: 2026-06-30
---

## Core Summary
Dat Ngo, AI Architect at Arize AI, presents a comprehensive overview of Arize's observability, evaluation, and experimentation platform for LLM-powered agents and harnesses. He frames AI engineering as "software reimagined" — the same patterns, just a different flavor — and walks through three pillars: (1) observability via OpenTelemetry traces, spans, and sessions to understand what agents are doing; (2) evals across five signal flavors (LLM-as-judge, human feedback, golden datasets, deterministic evals, business metrics) and four scopes (span, multi-span, trajectory, session-level); and (3) experimentation and improvement through datasets, controlled experiments, and an AI assistant (Alex) that automates the entire flywheel. Arize's ultimate goal is to automate users out of the observability-evals-experimentation loop entirely.

## Key Points

### Observability: What's Happening in Your Agent?
- AI engineering is "software reimagined" — same patterns (observability, testing, deployment), different flavor due to non-determinism
- Arize is OpenTelemetry (OTel)-first: add one line of code via auto-instrumentation, and it creates OTel traces and spans from the framework/SDK
- Traces are the "audit record" of what an agent did — code doesn't audit agents, telemetry does
- Beyond traces and spans: sessions capture back-and-forth conversations and state transitions across runs
- **Agent distributional view**: Instead of looking at one agent invocation, view all instantiations of an agent to see what percentage of traffic goes down each branch, which branches cause latency, and where loops occur
- **Trajectory analysis**: Identify that a particular branch causes evals to drop, then root-cause: e.g., B was called before A but B depends on A — the LLM's call ordering was mismatched
- Custom analytics dashboards for real-time views of agent behavior
- Observability is step one — the same progression that happened in traditional software

### Evals: Deriving Signal from Non-Deterministic Systems
- **Five flavors of signal**: (1) LLM as a judge — can get complex, tune against trusted data; (2) Human feedback — end-user satisfaction is extremely valuable; (3) Golden datasets — domain experts label data, then tune LLM judges to approximate them; (4) Deterministic/logic-based evals — cheap, reliable (JSON validity, schema compliance, non-null fields); (5) Business metrics — make more money, save money, or save time
- **Two personas converge**: Technical AI engineers (good at building/automating) and domain experts/PMs (know what the AI experience should be). Arize allows non-technical users to run evals in a UI while technical users can attach evals programmatically
- **Four eval scopes**: (1) Span eval — single input/output of one LLM call component; (2) Multi-span eval — requires data across multiple components (e.g., how well agents pass data to each other); (3) Trajectory eval — across all spans, did we call things in the right order to finish the business process?; (4) Session-level eval — zoom out to the state machine: was the user ever frustrated? Did we answer all questions?
- Not everything needs to be evaled — find the minimal set of evals that gives signal about whether the application works as intended (cost-aware)

### Experimentation and Improvement
- Starting point: traces identify where signal is bad → collect failing cases into a dataset → run experiments
- Experiments are changes: prompts, models, orchestration, configurations
- Can test changes in a UI or programmatically
- **Everything is automatable**: Arize exposes all primitives via CLI and tools/skills so coding agents (Claude Code, Codex) can call the system
- **Alex (Arize's AI assistant)**: An AI system built into Arize that can be invoked to analyze issues, plan and run tasks — "Hey, do you see any issues with my application?"
- **Ultimate goal**: Automate users out of the process. AI should create evals on the fly, detect changes that need new evals, and continuously monitor — "not magic, but it should feel like magic"

### Arize Product Line
- **Arize Phoenix**: Open-source, single-container deployment, no Kubernetes required — for engineering-first folks
- **Arize AX**: Enterprise product for large companies (Uber, Booking.com, Reddit) — more features, compliance, scale
- Everything shown manually is also available programmatically for coding agents

## Related
- [[DatNgo]] — speaker, AI Architect at Arize
- [[Arize]] — company and platform
- [[ArizeAX]] — enterprise product
- [[Phoenix]] — open-source observability platform
- [[OpenTelemetry]] — instrumentation standard
- [[AlexArizeAgent]] — Arize's AI assistant
- [[Uber]] — Arize AX enterprise customer
- [[BookingCom]] — Arize AX enterprise customer
- [[Reddit]] — Arize AX enterprise customer
- [[AgentObservability]] — core concept
- [[TracesAndSpans]] — observability primitives
- [[LLMAsJudge]] — evaluation technique
- [[DeterministicEval]] — code/logic-based evaluation
- [[Golden Dataset]] — trusted labeled data
- [[AgentExperiments]] — controlled comparison
- [[EvalScopes]] — span, multi-span, trajectory, session-level eval taxonomy
- [[AgentDistributionalView]] — distribution across agent instantiations
- [[AutomatedObservabilityFlywheel]] — automating the observability-evals-experimentation loop
- [[Trajectory Analysis]] — tracing agent paths for root cause
