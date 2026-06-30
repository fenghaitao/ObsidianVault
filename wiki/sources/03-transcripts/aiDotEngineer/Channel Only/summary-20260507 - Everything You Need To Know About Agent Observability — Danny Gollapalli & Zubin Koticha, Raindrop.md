---
title: "summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop"
type: source
tags: [source, transcript, agent-observability, signals, self-diagnostics, experiments, raindrop, monitoring]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.md"]
last_updated: 2026-06-29
---

## Core Summary
Zubin Koticha (CEO) and Danny Gollapalli (back-end engineer) of Raindrop present a comprehensive framework for agent observability, arguing that traditional evals are insufficient for production agents. Agents are non-deterministic, unbounded, and increasingly complex — running for hours with recursive sub-agents and exponentially growing tool sets. The solution is a monitoring paradigm built on explicit and implicit signals, self-diagnostics, and production experiments that create a continuous improvement flywheel.

## Key Points

### Why Agent Failures Are Different
- Agents are non-deterministic with infinite input/output spaces
- They can use tools to affect other systems arbitrarily
- Sessions are getting longer (hours without user input)
- Stakes are increasing: healthcare, finance, military deployments
- Sub-agents can have their own tools, memory sources, and recursive sub-agents — creating combinatorial complexity that evals cannot cover
- "Humanity's last problem": when humans can no longer monitor agents and find issues

### Two Types of Signals

**Explicit Signals** (objective, verifiable true/false):
- Error rate (especially tool error rate)
- Latency
- User regenerations
- Cost
- If any of these spike, something is likely wrong

**Implicit Signals** (semantic, harder to detect):
- **Regex signals**: Pattern matching for frustration keywords (e.g., "WTF", "this sucks", "horrible"). Claude Code's leaked `keywords.ts` used this approach — a long regex string detecting frustration, flipping a `boolean isNegative` flag to track issue rates per release. Cheap and powerful in aggregate.
- **Classifier signals**: Binary classifiers detecting specific issues — refusals ("I can't do that"), task failure, user frustration, content moderation, NSFW, jailbreaking, and positive wins. Raindrop provides these out of the box using trained models (not LLMs on every output, which would double AI spend).
- **Self-diagnostics**: Models introspecting on their own behavior (inspired by OpenAI's December paper on training models to self-confess misalignment). Can catch: tool failures (agent rants about failing tools), user frustration (diplomatic responses), capability gaps (user wants features the agent lacks — acts as pseudo feature requests), and self-correction (both good and bad, e.g., bypassing sandbox restrictions).

### Self-Diagnostics Workshop
- Only requires a simple tool + one line in the system prompt
- Tool naming matters: "report" works better than "unsafe bash use" — models are trained to look polished and avoid self-incrimination
- Framing as "giving feedback to creators" improves compliance
- Models won't self-incriminate if the tool name implies wrongdoing
- Can send reports directly to Slack without any observability platform
- The agent in the demo bypassed a broken write tool by using bash heredoc syntax, then self-reported the workaround

### Production Experiments
- Ship changes (new prompt, model, tool, agent harness) to a percentage of users
- Compare signal rates (refusals, user frustration, etc.) against control group
- Example: prompt 2.4 reduced user frustration from 37% to 9%, increased average tools used
- Statistical relevance starts at a few hundred events — when you can no longer read every input/output
- Multiple experiments can run in parallel; compounding effects observable via query API
- Data can be piped to Statsig, BigQuery, or Snowflake for custom analysis

### Raindrop Platform Features
- **Signals out of the box**: refusals, task failure, user frustration, laziness, jailbreaking, content moderation, NSFW
- **Deep Search**: natural language queries to find specific issues, create new binary classifier signals
- **Trajectories**: visual topology of tool calls — see which tools were called in what order, which had errors, find similar patterns
- **Triage Agent**: autonomous agent that monitors signals daily, detects spikes, investigates root causes, and creates automatic issues (e.g., detected a database provider failing for specific customers)
- **Alerting**: set alerts on any signal with day-by-day rate tracking
- **Experiments**: automatic experiment setup via metadata flags, compare signal rates across versions
- **SDK**: Python support improving, self-diagnostics built into SDK (tool injected automatically)
- **Integrations**: query API for BigQuery/Snowflake export, Statsig integration for experiment analysis
- **Historical backfill**: ingest historical data, backfill signals for past days when new signals are created

### Customer Use Cases
- Production monitoring with custom signal sets per domain (coding agents vs. companions vs. legal apps)
- User intent clustering: discover what people use the agent for (React apps, Python, debugging, vibe coding), measure issue rates per use case
- Daily breakdown of issues with delta from previous day
- Feedback loop: improve prompting → change models → modify agent harness → measure impact on signals
- Raindrop used alongside Sentry and LogRocket — Raindrop focuses on "fuzzy failures" (user frustration) while traditional tools handle explicit exceptions

### Q&A Highlights
- **Minimum data for experiments**: A few hundred events, when you can no longer manually read all inputs/outputs
- **Non-English detection**: Trained classifier models work across languages; regex works in aggregate even with edge cases
- **Single-turn vs. multi-turn**: Most value in multi-turn agents, but tool error rates and refusals work for single-turn too
- **Free trial**: 2 weeks (likely extending), DM for longer access
- **PII and experiments**: Query API allows customers to export signal tags and run experiments in their own systems (BigQuery, Statsig)

## Related
- [[Danny Gollapalli]] — speaker, back-end engineer at Raindrop
- [[Zubin Koticha]] — speaker, CEO and co-founder of Raindrop
- [[Raindrop]] — agent observability platform
- [[AgentObservability]] — the core concept
- [[ImplicitSignals]] — semantic signals (regex, classifiers, self-diagnostics)
- [[ExplicitSignals]] — objective signals (error rate, latency, cost, regenerations)
- [[SelfDiagnostics]] — models introspecting on their own behavior
- [[AgentExperiments]] — production A/B testing with signal comparison
- [[UserFrustration]] — key implicit signal for agent health
- [[Trajectories]] — visual topology of agent tool calls
- [[TriageAgent]] — autonomous agent for issue detection and root cause analysis
- [[ClaudeCode]] — referenced for leaked keywords.ts regex frustration detection
- [[OpenAI]] — referenced for self-diagnostics inspiration paper
- [[Sentry]] — traditional observability tool used alongside Raindrop
- [[LogRocket]] — traditional observability tool used alongside Raindrop
- [[Statsig]] — experiment analysis integration
- [[BigQuery]] — data export integration
- [[Snowflake]] — data export integration
- [[Replit]] — referenced as scale where LLM-on-every-output becomes expensive
- [[aiDotEngineer]] — event host
