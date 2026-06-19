---
title: "LethalTrifecta"
type: concept
tags: [concept, security, prompt-injection, agents, second-brain]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260402 - Full Guide - Build Your Own AI Second Brain with Claude Code.md"
last_updated: 2026-06-20
---

## Definition

The Lethal Trifecta is a security model for AI agents: an agent becomes dangerously exploitable (via prompt injection) when **all three** of these are present simultaneously — (1) private data access, (2) untrusted content intake, and (3) an exfiltration vector. Remove any one and the risk drops sharply. [[ColeMedin]] uses it to argue why you must be careful building a [[SecondBrain]] (which inherently has all three).

> The term originates from security researcher Simon Willison; Cole applies it to the second-brain design decision.

## Key Information

### The three pillars

| Pillar | Meaning | Example |
|---|---|---|
| **1. Private data access** | The agent can read sensitive data | Your email, calendar, documents |
| **2. Untrusted content** | Input the agent processes that isn't from you | Incoming emails, web page content — any of which could carry injected instructions |
| **3. Exfiltration vector** | A way for the agent to send data out | Sending a message, posting to an API |

### The core logic

The danger requires **all three** to coexist:

- Private data + exfiltration, but **no untrusted content** → attacker has no way to inject the malicious instruction. Lower risk.
- Untrusted content + exfiltration, but **no private data** → nothing sensitive to steal. Lower risk.
- Private data + untrusted content, but **no exfiltration** → attacker can manipulate the agent but can't get data out. Lower risk.
- **All three** → an injected instruction in untrusted content can make the agent read private data and send it to the attacker. This is the lethal combination.

### Why a [[SecondBrain]] always has all three

A useful second brain *inherently* satisfies all three:
1. It needs private data access (email, calendar) to be useful.
2. It ingests untrusted content (incoming emails, web research).
3. It can send messages / post to APIs (its whole point is acting on your behalf).

You can't make a useful second brain without exposure to the lethal trifecta. So the design imperative isn't "avoid the trifecta" — it's **"limit each pillar as much as possible."**

### How Cole limits each pillar in his [[SecondBrain]]

- **Limit private data access** — zero-trust default. A Python API layer controls exactly what each integration can do. Read-only Slack. Gmail drafts but no send. Asana writes only in specific projects.
- **Limit exfiltration** — careful per-capability permissions; the agent can't send emails or post to most surfaces by default.
- **Untrusted content** is hardest to limit (you want to process incoming email/web) — so you compensate by tightening the other two pillars and starting zero-trust.

### Why this argues against running [[OpenClaw]] directly

[[OpenClaw]] (and similar out-of-the-box agents) don't limit private-data-access and exfiltration well, and they're huge code bases you don't understand — so you can't reason about how the trifecta affects you. Building your own (taking inspiration, not running the code) lets you define permissions up front and layer capabilities deliberately. The security argument is the core of Cole's "build your own second brain" thesis.

### General applicability

The trifecta applies to *any* agent, not just second brains. Whenever you're designing an agent with tool access, ask: does it have all three pillars? If so, you're in high-risk territory and need to limit each as much as the use case allows.

## Related

- [[SecondBrain]] — the system that inherently has all three pillars
- [[OpenClaw]] — the out-of-the-box agent Cole argues is risky on this model
- [[Guardrails]] — input/output validation that limits the pillars
- [[AIAgent]] — the general subject
- [[ColeMedin]] — applies the model in this corpus
- [[summary-full-guide-ai-second-brain]] — primary source
