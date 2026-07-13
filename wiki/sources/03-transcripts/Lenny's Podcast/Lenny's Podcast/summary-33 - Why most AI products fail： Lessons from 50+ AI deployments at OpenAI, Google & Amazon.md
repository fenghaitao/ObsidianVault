---
title: "summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon"
type: source
tags: [source, original-material, ai-product-development, evals, agentic-systems]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-11
---

## Core Summary

[[Lenny Rachitsky]] interviews [[Aishwarya Naresh Reganti]] and [[Kiriti Badam]] — who together have led or supported 50+ AI product deployments at companies including [[Amazon]], [[Databricks]], [[OpenAI]], and [[Google]], and teach a top-rated AI product course on [[Maven]] — about why most AI products fail and how to build them successfully instead. Their core argument: AI products differ fundamentally from traditional software along two axes — [[Non-Determinism In AI Products|non-determinism]] (you can't predict how users will phrase intent or how the LLM will respond) and the [[Agency Control Trade-off|agency/control trade-off]] (every unit of decision-making autonomy handed to an agent is a unit of control relinquished). Because of this, teams should build in deliberately staged versions that start with high human control and low agent agency, earning more autonomy only as the system proves reliable — formalized as their "[[Continuous Calibration Continuous Development|Continuous Calibration, Continuous Development (CCCD)]]" life cycle, a CI/CD-inspired loop of scoping capability, curating data, setting evaluation metrics, deploying, then calibrating against real user behavior to catch emerging error patterns evals alone can't anticipate. They argue evals and production monitoring are complementary, not competing (a "false dichotomy"), that the term "eval" itself has suffered [[Semantic Diffusion]] (Martin Fowler's term) as different practitioners use it to mean different things, and that company success rests on a "[[AI Product Success Triangle|success triangle]]" of hands-on leaders, an empowered (non-FOMO) culture, and workflow-obsessed technical execution. They close on "[[Pain Is The New Moat|pain is the new moat]]": durable advantage doesn't come from being first to ship an agent but from having gone through the iterative pain of learning what actually works.

## Key Points

- **Non-determinism**: traditional software maps a well-defined user intention to a deterministic sequence of clicks/forms (e.g. booking.com); AI products replace that with free-form natural-language input (unpredictable user phrasing) feeding a non-deterministic, prompt-sensitive LLM output — so both the input and the output surfaces are unknown in advance.
- **Agency/control trade-off**: handing an agentic system more decision-making autonomy always means relinquishing human control; the agent has to "earn" that autonomy by building up demonstrated trust/reliability first.
- **Staged autonomy pattern** (illustrated via a customer-support agent): V1 = suggest-only, human decides (high control, low agency); V2 = draft/auto-answer with human review; V3 = full autonomous resolution including actions like issuing refunds. Same pattern given for a coding assistant (inline completions → generate PRs for review → autonomously open PRs) and a marketing assistant (draft copy → build/launch a campaign → fully autonomous AB-testing and optimization).
- **Reliability is the dominant blocker**: cites a UC Berkeley/Databricks-adjacent survey (researchers include people the guests garble as "Mate Zahara" and "Stoker," almost certainly [[Databricks]]'s [[Matei Zaharia]] and [[Ion Stoica]]) finding ~74-75% of enterprises cite reliability as their biggest obstacle to deploying AI to end users — which is why most current AI products skew toward internal productivity rather than customer-facing autonomous agents.
- **"One-click agents" are marketing**: enterprise data/infrastructure is inherently messy (undocumented taxonomies, legacy functions, dead nodes last touched years ago); a system that promises significant ROI in days is not credible — real gains typically take four to six months of iterative flywheel-building even with strong data/infra.
- **Continuous Calibration, Continuous Development (CCCD)**: their named framework (deliberately echoing CI/CD) — see [[Continuous Calibration Continuous Development]] for the full loop and worked customer-support example (routing → co-pilot/draft → end-to-end resolution).
- **Evals vs. production monitoring — a false dichotomy**: evals encode what you already know matters (a curated dataset of must-not-fail cases); production monitoring (explicit signals like thumbs-up/down, implicit signals like regenerate-clicks) surfaces the emerging failure patterns you didn't anticipate. Neither alone is sufficient — see [[Evals Vs Production Monitoring]].
- **"Eval" has suffered semantic diffusion**: a data-labeling company's "experts writing evals" usually means error analysis/annotated notes, not literal LLM judges; "PMs should write evals" doesn't mean PMs build production-grade LLM judges; benchmarks (LM Arena, Artificial Analysis) are not the same as an eval dataset for your own product. See [[Semantic Diffusion]].
- **OpenAI's Codex team's eval philosophy**: because [[Codex]] is built for open-ended developer customization (not five fixed workflows), the team combines targeted regression evals (so a change doesn't break something core) with heavy direct customer-feedback/social-media monitoring and per-engineer "vibes" testing against a shared list of hard problems for every new model — deliberately not claiming evals alone are sufficient.
- **Multi-agent systems are "misunderstood," not overhyped**: naive peer-to-peer "gossip protocol" multi-agent decomposition rarely works reliably; a single supervisor agent orchestrating narrower sub-agents is the pattern that actually succeeds today. See [[Supervisor-Subagent Pattern]].
- **AI Product Success Triangle**: successful AI orgs combine (1) hands-on leaders willing to relearn intuitions built over a career (example: the [[Rackspace]] CEO's 4-6am daily "catching up with AI" block), (2) a culture of empowerment rather than FOMO/job-replacement fear (subject-matter experts must be willing to work with the AI team rather than withhold expertise), and (3) technical teams obsessed with understanding workflows deeply enough to choose the right tool (ML model vs. deterministic code vs. LLM) per sub-task. See [[AI Product Success Triangle]].
- **Recalibration triggers**: teams should recalibrate roughly every 1-2 days early on, graduating to the next autonomy stage once new user-behavior patterns stop appearing ("minimizing surprise"); model deprecations (e.g. GPT-4o retirement) or organic shifts in user behavior (e.g. an underwriting-copilot's users starting to ask open-ended historical-precedent questions after 3-4 months of trust-building) can reset the calibration clock even after a system is stable.
- **Prompt injection / jailbreaking** is flagged as a large, possibly unsolvable open risk that current guardrail systems don't reliably stop, though the guests see the industry as still early enough (low AI penetration) that this hasn't yet become the dominant problem.
- **Cautionary real-world incident cited**: [[Air Canada]]'s chatbot hallucinated a refund policy that the company was legally held to, cited as a reason not to hand agents unconstrained autonomy on high-stakes actions.
- **"Pain is the new moat"**: durable competitive advantage comes not from being first to ship an agent but from having gone through the non-negotiable, undocumented process of learning what trade-offs actually work for your problem — that accumulated organizational pain/knowledge is what's actually hard to copy.
- **Overrated/underrated**: multi-agent "gossip protocol" systems are misunderstood (not overrated); coding agents are underrated (penetration outside the Bay Area is still low); jumping across tools chasing novelty is overrated compared to deeply understanding the business problem, since implementation is becoming cheap while design/judgment/taste becomes the scarce skill.
- **2026 predictions**: Badam expects proactive/background agents (extending the "ChatGPT Pulse" pattern) that surface unprompted work and insights; Reganti expects a leap in multimodal AI (beyond language) to unlock messy real-world data like handwritten documents, citing [[Demis Hassabis]]/[[Google DeepMind]]'s combined image-model/LLM/world-model ("Genie") direction.

## Related

- [[Aishwarya Naresh Reganti]] — co-guest
- [[Kiriti Badam]] — co-guest
- [[Lenny Rachitsky]] — host
- [[Lenny's Podcast]] — show
- [[Continuous Calibration Continuous Development]] — the episode's central named framework
- [[Agency Control Trade-off]] — core conceptual pillar
- [[Non-Determinism In AI Products]] — core conceptual pillar
- [[Evals Vs Production Monitoring]] — the "false dichotomy" discussion
- [[Semantic Diffusion]] — Martin Fowler concept applied to the word "eval"
- [[AI Product Success Triangle]] — leaders/culture/technical framework
- [[Supervisor-Subagent Pattern]] — the multi-agent architecture the guests endorse
- [[Pain Is The New Moat]] — closing thesis
- [[Problem First Approach]] — recurring methodological stance
- [[Databricks]] — cited reliability survey; guests' consulting/deployment work
- [[Rackspace]] — CEO's daily AI-learning habit example
- [[Air Canada]] — cautionary chatbot-hallucination incident
- [[Codex]] — OpenAI's eval/feedback approach discussed in depth
- [[OpenAI]] — employer of Kiriti Badam (Codex team)
- [[Google]] — cited as prior employer and in DeepMind reference
- [[Amazon]] — cited among companies where the guests deployed AI products
- [[Dan Shipper]] — referenced for his "CEO chatting with ChatGPT/Claude" success predictor
- [[ChatGPT]] — referenced (ChatGPT Pulse, ChatGPT vs. Claude usage)
- [[Claude]] — referenced (CEO habit example)
- [[Jason Lemkin]] — referenced anecdote about replacing a sales team with agents
- [[Whisper Flow]] — Reganti's favorite recently discovered product
- [[Raycast]] — Badam's favorite recently discovered product
- [[Maven]] — platform for their AI product course
- [[Kumo]] — Badam's prior employer
