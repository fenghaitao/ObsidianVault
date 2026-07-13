---
title: "Continuous Calibration Continuous Development"
type: concept
tags: [ai, product-development, framework, evals, agentic-systems]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-11
---

## Definition

"Continuous Calibration, Continuous Development" (CCCD) is [[Aishwarya Naresh Reganti]] and [[Kiriti Badam]]'s named life cycle for building AI products, deliberately named after CI/CD (continuous integration/continuous deployment) to signal that AI product development is an iterative loop rather than a linear ship-and-move-on process. It pairs a "continuous development" side (scope capability, curate data, design evaluation metrics, deploy) with a "continuous calibration" side (observe real user behavior, spot emerging error patterns, fix issues, and design new evaluation metrics for patterns you didn't originally anticipate).

## Key Information

- **Why it exists**: the pair built end-to-end autonomous agents for early customers and found debugging nearly impossible once a workflow spanned four or five decision-making steps — they eventually had to shut down a customer-support product due to unmanageable hot-fixing, and cite [[Air Canada]]'s chatbot hallucinating a refund policy the company was legally bound to honor as a public example of the same failure mode.
- **Continuous development loop**: scope capability and curate a dataset of expected inputs/outputs (a forcing function that surfaces team misalignment on desired behavior before any code is written) → set up the application → design evaluation *metrics* (Reganti is deliberate about this phrasing: evaluation is the process, metrics are the specific dimensions being tracked) → deploy.
- **Continuous calibration loop**: observe behavior patterns you didn't expect in the original dataset → analyze traces and spot error patterns → apply direct fixes for one-off/spot errors (e.g., a tool-calling error from a poorly defined tool) → design new evaluation metrics for patterns that are systematic rather than one-off.
- **Staged-agency dimension layered on top**: while iterating through the loop, deliberately start with lower-agency, higher-human-control versions and only reduce control as the system earns trust — see [[Agency Control Trade-off]]. Autonomy can be constrained by number of actions permitted, by topic/domain risk, or by other axes chosen jointly by PMs, engineers, and subject-matter experts.
- **Worked example — customer support agent**, given as three versions:
  - **V1: Routing** — can the agent correctly classify and route a ticket to the right department? High control (humans can undo a bad routing), but often much harder than it looks because enterprise taxonomies are frequently messy/inconsistent (e.g., a "shoes" category with "women's"/"men's" as siblings in one place and children in another, with stale unused nodes from years earlier). Human agents intuit these quirks; an agent needs that undocumented context made explicit.
  - **V2: Co-pilot** — once routing is solid and underlying data issues are fixed, the agent drafts a suggested resolution (based on standard operating procedures) for a human to edit or approve; logging how much of the draft survives human editing yields free error analysis for the flywheel.
  - **V3: End-to-end resolution** — once drafts are barely edited, let the agent resolve tickets autonomously, including actions like issuing refunds.
- **Same staged pattern applied to other domains** in the source material: a coding assistant (inline completions → generate PRs/tests for review → autonomously open PRs) and a marketing assistant (draft copy → build and launch a multi-step campaign → autonomously AB-test and optimize campaigns).
- **Why not "just build evals and be done"**: evaluation metrics only catch failure modes you already know to look for; CCCD's calibration side exists specifically to surface emerging patterns you couldn't have anticipated before deployment, using low-risk, human-in-the-loop staging so you're never exposed to a large blast radius of undiscovered failure modes at once.
- **When to advance to the next stage — "minimizing surprise"**: there's no fixed rule, but if you're calibrating every 1-2 days and no longer seeing new data-distribution patterns (users behaving consistently with the system), that's the signal you're ready to raise agency and lower control.
- **Recalibration can be forced by external events**, not just steady-state drift: a model deprecation (e.g. GPT-4o being retired in favor of GPT-5) changes system behavior and resets calibration; user behavior itself can evolve as users' trust and expectations of the system grow — e.g. an underwriting co-pilot built to answer policy lookups was, after 3-4 months of strong results, suddenly asked much harder precedent-matching questions ("for a case like this, what did previous underwriters do") that the original design never anticipated.

## Related

- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
- [[Aishwarya Naresh Reganti]] — co-creator
- [[Kiriti Badam]] — co-creator
- [[Agency Control Trade-off]] — the staged-autonomy dimension layered onto CCCD
- [[Non-Determinism In AI Products]] — the underlying problem CCCD is designed to manage
- [[Evals Vs Production Monitoring]] — the two complementary signal sources CCCD relies on
- [[Air Canada]] — cautionary incident motivating the framework
- [[Problem First Approach]] — the mindset CCCD's "scope capability" step is meant to enforce
