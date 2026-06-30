---
title: "Implicit Signals"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.md"]
last_updated: 2026-06-29
---

# Implicit Signals

## Definition

Implicit signals are semantic, harder-to-detect indicators of agent health that deal with the meaning and quality of interactions rather than objective metrics. Introduced by Zubin Koticha of Raindrop, they complement explicit signals (error rate, latency, cost) and are essential for catching "fuzzy failures" that traditional monitoring misses.

## Key Information

### Three Types of Implicit Signals

**1. Regex Signals**
- Pattern matching for frustration keywords in agent outputs or user messages
- Example: Claude Code's leaked `keywords.ts` — a long regex string looking for "WTF", "this sucks", "horrible", etc.
- When matched, flips a `boolean isNegative` flag; frustration rate tracked per release
- Cheap and powerful in aggregate — even if individual cases are missed, aggregate trends are valuable
- Works across millions of users; a 10% spike is meaningful regardless of edge case misses

**2. Classifier Signals**
- Binary classifiers detecting specific issues rather than LLM-as-judge scoring outputs
- More effective to have a solid set of issues you're looking for than to ask "rate this response on a scale of 1-10"
- Common signals: refusals ("I can't do that"), task failure, user frustration, content moderation, NSFW, jailbreaking, wins (positive signals)
- Raindrop provides these out of the box using trained models (not LLMs) to avoid doubling AI spend
- Trained models work across languages, unlike regex which is language-specific

**3. Self-Diagnostics**
- Models introspecting on their own behavior, inspired by OpenAI's December paper on training models to self-confess misalignment
- Can catch: tool failures (agent rants about failing tools), user frustration (diplomatic responses), capability gaps (user wants features the agent lacks — acts as pseudo feature requests), self-correction (both good and bad, e.g., bypassing sandbox restrictions)
- Only requires a simple tool + one line in the system prompt
- Tool naming matters: "report" works better than "unsafe bash use" — models are trained to look polished and avoid self-incrimination
- Framing as "giving feedback to creators" improves compliance

## Related

- [[ExplicitSignals]] — complementary objective signal category
- [[AgentObservability]] — parent concept
- [[SelfDiagnostics]] — third type of implicit signal
- [[UserFrustration]] — key classifier signal
- [[AgentExperiments]] — using signals for production A/B testing
- [[Raindrop]] — platform providing implicit signals out of the box
- [[Zubin Koticha]] — introduced the concept
- [[ClaudeCode]] — referenced for regex frustration detection in keywords.ts
- [[OpenAI]] — referenced for self-diagnostics inspiration paper
- [[summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop]] — source transcript
