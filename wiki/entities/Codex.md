---
title: "Codex"
type: entity
tags: [product, tool, openai, coding-agent, desktop-app]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/03 - Why OpenAI is merging Codex and ChatGPT and the future of knowledge work ｜ Andrew Ambrosino.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/27 - The rise of the professional vibe coder (a new AI-era job).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/39 - Inside OpenAI： 2026 is the year of agents, AI’s biggest bottleneck, and why compute isn’t the issue.md"]
last_updated: 2026-07-12
---

## Definition

Codex is [[OpenAI]]'s coding-agent product, led by [[Andrew Ambrosino]]. It began as a CLI tool, grew into a desktop app for developers, and is now being merged with [[ChatGPT]] into a general-purpose knowledge-work application.

## Key Information

- Started as "Codex web": give the agent a task, it goes off and completes it and returns with finished code. Ambrosino says this early form factor was "too early" — not because the concept was wrong, but because the underlying model wasn't good enough yet at the work (contrasted with Cloud Code's more conversational, "ask you questions" approach, which fit the model capability of that moment better).
- The desktop Codex app began development around November; the team wasn't using it full-time at first. By the time of this interview it is used "for everything."
- Deliberately not built as an IDE: it is a right-sized surface, more than a chatbot but not a full code editor — you could see the code but (initially) not edit it directly.
- Internally, adoption reached near-100% of OpenAI employees weekly (not just engineers), driving the decision to widen its scope beyond a developer tool.
- Growth: usage up 6x since January 2026(ish), with 5M+ weekly active users at time of interview, a number the host expects to be quickly outdated.
- A May-ish release ("Codex for almost everyone") added an in-app browser, computer use, and artifact creation — described internally as their first coordinated, "vibe coding"-era release.
- The in-app browser evolved from a narrow developer tool (testing local front-end builds, originally on Electron's limited in-app browser capabilities) to a full multi-tab browser (after switching to the "owl" stack that also powers Atlas) with enterprise security/login support, plus an alternative Chrome-extension integration path — reflecting ongoing uncertainty about whether the in-app browser should be "for the agent only" or a full user-facing browser.
- Can perform computer use to complete tasks without a pre-built connector (e.g., Andrew describes asking it to configure a Google Cloud Pub/Sub API integration, and it just started clicking through the console UI itself).
- Can extend itself into third-party tools: an in-house videographer used Codex to edit Adobe Premiere Pro files, and Codex built its own Premiere Pro extension to accomplish edits it couldn't do purely by editing backing files.
- OpenAI's strategic direction: merge Codex and ChatGPT into one app that serves as a "home base" for all knowledge work — some tasks handled inside the app, others handled by the app driving external tools (e.g., a spreadsheet add-in inside Microsoft Excel) — deliberately avoiding the "everything happens in one rectangle on screen" model.
- The Codex org is intentionally lean: roughly double-digit engineers, about half that in design, fewer dedicated product people, mostly individual contributors with large scope (see [[Zone Defense]]).
- Central to the org's development practice is aggressive [[Dogfooding]] — building the app largely by using the app itself, even when doing so is inefficient for the team's own process.
- Per [[Lazar]] (episode 27, professional vibe coding at [[Lovable]]): uses Codex as his go-to external diagnostic tool in step 3 of his "[[4x4 Debugging Framework]]" — exports a Lovable/Cursor project's code to GitHub, imports it into Codex, and asks Codex to diagnose (but deliberately not fix) a bug he couldn't resolve within Lovable itself, since he trusts its syntax judgment but doesn't want to steer an agent he isn't personally fluent with.
- Per [[Zevi Arnovitz]] (episode 31): uses Codex's built-in code review as one leg of his [[Multi-Model Peer Review]] process, running it against the same branch reviewed by Claude and Cursor's Composer. Personifies it as an uncommunicative but highly effective solo problem-solver — "closes the door for two hours and comes out and says I fixed it" — contrasted with Claude's more collaborative, opinionated style.
- Per [[Kiriti Badam]] (episode 33, who works on Codex at OpenAI): because Codex is built for open-ended developer customizability rather than five or six fixed workflows, the team's eval strategy combines targeted regression evals (ensuring a change doesn't break something core) with heavy direct customer/social-media feedback monitoring and per-engineer "vibes" testing against a shared list of hard problems for every new model — rather than trying to build comprehensive LLM judges for every possible interaction. Illustrated via Codex's recently launched code-review product: changes are AB-tested for catch-rate accuracy and watched for user annoyance/opt-outs, since building predictive eval datasets for a brand-new feature's failure modes ahead of time is impractical. See [[Evals Vs Production Monitoring]].
- Also cited as Badam's tool of choice for long unattended coding runs, paired with a Mac-sleep-prevention utility ("caffeinate") to let a task run for four or five hours unattended — see [[Raycast]].

### Per episode 39 ([[Alexander Imbiricos]], Codex product lead)

- Growth: roughly 20x since GPT-5's August launch (up from an earlier-reported 10x); Codex models now serve many trillions of tokens per week and are the most-served coding model both in OpenAI's own harness and, increasingly, via API adoption by third-party coding tools.
- Origin-story reframing: the first version, "Codex Cloud," was a fully asynchronous, cloud-delegated agent (Imbiricos's still-believed-in eventual end state), but proved too hard to adopt cold, since it required upfront environment configuration and trust that new users didn't yet have. The real growth unlock was building an interactive IDE/CLI extension that met developers in their existing workflow first — closely paralleling how you'd onboard and gradually delegate more to a new human teammate.
- Ships "compaction," a feature spanning the model, API, and harness layers that lets Codex work continuously for very long stretches (users report 24+ hour runs) by having the model recognize it's approaching its context-window limit and prepare a compressed handoff into a fresh context window.
- Deliberately built around the shell/terminal (not semantic search or bespoke tool-calling), reasoning that optimizing deeply for one consistent way of working lets the team move faster, with a sandbox layer added to make raw shell access safe.
- GPT-5.1 Codex Max, shipped the week before this episode, is ~30% faster at a given task and meaningfully smarter at higher reasoning levels — Karpathy's "give it your gnarliest bugs and let it run for an hour" praise is specifically attributed to this model. See [[GPT-5.1 Codex Max]].
- Internal acceleration case studies: the Sora Android app was built to internal-employee readiness in 18 days and public launch (reaching #1 in the App Store) in 28 days total, by only 2-3 engineers, heavily using Codex to port/adapt logic from the existing iOS app; the [[Atlas]] browser team reports work that used to take 2-3 engineers 2-3 weeks now takes one engineer one week.
- Also used for non-engineering, "coding-adjacent" work: throwaway data-analysis tooling (e.g., "give Codex some data and ask it to build an interactive data viewer"), a Codex designer vibe-coding an entire animation editor just to build one UI animation, and a product marketer making live string/doc updates directly from Slack.
- Has a Slack integration letting anyone (not just engineers) @-mention Codex to ask questions like "why did this metric move?" and get an answer back in-channel without touching code directly.
- Emerging capability: "Codex on call for its own training" — an early internal experiment having Codex monitor its own model-training run charts/metrics on a loop and flag or act on anomalies, since Codex already writes much of the code managing OpenAI's training infrastructure and its code review has caught real configuration mistakes.
- Team philosophy for eval/progress-tracking: watches D7 retention and the raw "sign up from scratch, try it as a new user" feeling as a check against over-indexing on power-user features; monitors Reddit (particularly r/Codex) as a source of unvarnished, "real" feedback, contrasted with a "hypier" Twitter/X.
- Recommended way to try Codex: give it your hardest real single-task problem (e.g., a hard, not-yet-diagnosed bug) rather than a deliberately trivial one, since it's built as a professional tool for difficult production codebases, not primarily a casual vibe-coding sandbox.
- Language support is roughly proportional to real-world language popularity — no special exclusions beyond very esoteric or private languages.
- The Codex team was actively hiring (engineers, product, sales) at time of episode.

## Related

- [[summary-03 - Why OpenAI is merging Codex and ChatGPT and the future of knowledge work ｜ Andrew Ambrosino]] — source summary
- [[Andrew Ambrosino]] — product/engineering lead for Codex
- [[OpenAI]] — company that builds Codex
- [[ChatGPT]] — app Codex is merging into
- [[Atlas]] — browser sharing underlying tech ("owl" stack) with Codex's in-app browser
- [[Operator]] — earlier, related agent feature in ChatGPT
- [[Taste]] — the skill Codex's org optimizes for internally
- [[Zone Defense]] — how the Codex product org organizes coverage
- [[Dogfooding]] — core development practice behind Codex
- [[Design Process]] — discussion of prototypes vs. docs in building Codex features
- [[summary-27 - The rise of the professional vibe coder (a new AI-era job)]] — source summary
- [[Lazar]] — uses Codex as an external diagnostic tool
- [[4x4 Debugging Framework]] — debugging methodology where Codex is used
- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Zevi Arnovitz]] — uses Codex in his multi-model review rotation
- [[Multi-Model Peer Review]] — review practice Codex participates in
- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
- [[Kiriti Badam]] — works on Codex; describes its eval/monitoring philosophy in depth
- [[Evals Vs Production Monitoring]] — framework applied to Codex's approach
- [[Raycast]] — productivity tool Badam pairs with Codex for long unattended runs
- [[summary-39 - Inside OpenAI： 2026 is the year of agents, AI’s biggest bottleneck, and why compute isn’t the issue]] — source summary
- [[Alexander Imbiricos]] — Codex product lead, guest of episode 39
- [[GPT-5.1 Codex Max]] — latest model release discussed
- [[Compressing The Talent Stack]] — organizational framework Imbiricos applies to the Codex team
- [[Sora (app)]] — internal case study for Codex-driven acceleration
