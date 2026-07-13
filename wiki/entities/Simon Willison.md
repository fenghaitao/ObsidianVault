---
title: "Simon Willison"
type: entity
tags: [person, software-engineer, ai, open-source]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-12
---

## Definition

Veteran software engineer (10x engineer for 20+ years), co-creator of [[Django]], creator of [[Datasette]] and 100+ other open-source projects; coined "prompt injection" and "[[Lethal Trifecta]]," popularized "AI slop" and "[[Agentic Engineering]]." Writes extensively in real time about AI-assisted software development at blog.simonwillison.net and is writing a chapter-at-a-time book on agentic engineering patterns.

## Key Information

- Frames November of the prior year as an "inflection point": GPT-5.1 and Claude Opus 4.5 crossed a threshold where coding agents went from "mostly works, needs close supervision" to "almost always does what you told it to," driven by a year of both OpenAI and Anthropic focusing training on code plus the "reasoning models" trend (OpenAI's o1, late 2024) that turned out to work especially well for code.
- Distinguishes "vibe coding" (Andrej Karpathy's original sense: not looking at the code, playing purely on vibes, fine when only you get hurt by bugs) from "[[Agentic Engineering]]" (professional use of coding agents to produce reviewed, production-ready software) — argues collapsing the two terms together devalues both.
- Describes the "[[Dark Factory Pattern]]" (aka "software factory"): a stage beyond agentic engineering where nobody writes code and nobody reads code, but professional quality practices still apply — illustrated via [[StrongDM]]'s simulated-Slack/simulated-Jira agent-swarm QA approach.
- Currently produces ~95% of his code without typing it himself; runs Claude Code primarily via Claude Code for Web (safer than local, since a compromised agent can only affect Anthropic's servers, not his machine) and increasingly from his phone.
- Describes agentic engineering as mentally exhausting despite (or because of) amplifying 25 years of experience — can run 4 parallel agents but is "wiped out" by 11am; sees this intensity/burnout risk as a live open problem, not necessarily permanent.
- Predicts by year-end it "will not be uncommon" for an engineer to report ~95%+ of their code is AI-written, though adoption will vary by culture (notes US/European AI-skepticism gap via Hacker News time-zone patterns).
- Cites a ThoughtWorks VP roundtable finding that AI most benefits senior engineers (skill amplification) and new engineers (onboarding acceleration, citing [[Cloudflare]] and [[Shopify]] each hiring ~1,000 interns in 2025 partly for this reason) — leaving *mid-career* engineers as the group most at risk, since they lack both deep expertise to amplify and beginner-level onboarding gains.
- Advocates "[[Hoarding Things You Know How To Do]]" as career advice: maintain a growing personal backlog (his public GitHub repos `simonw/tools` and `simonw/research`) of small verified experiments/techniques that compound into a unique combinatorial advantage.
- Advocates test-driven development and specifically "[[Red-Green TDD]]" as a compact prompt ("red/green TDD") that reliably improves agent-written code quality; also advocates starting new projects from a "[[Thin Template Pattern]]" (a minimal styled skeleton, not a long CLAUDE.md) so agents pick up house style by example.
- Coined "prompt injection" (2022) and, when that term got redefined by public misuse (people conflating it with jailbreaking), coined the deliberately opaque "[[Lethal Trifecta]]" to force people to look up the actual definition: private data access + exposure to untrusted input + an exfiltration path.
- Predicts an eventual "Challenger disaster" for AI security — drawing on the "normalization of deviance" research into the Space Shuttle Challenger disaster — arguing repeated undetected close calls with prompt injection are making the industry systematically overconfident; has made this same prediction roughly every 6 months for 3 years without it yet occurring. See [[Normalization Of Deviance]].
- Cites Google DeepMind's "[[CAMEL Pattern]]" (splitting a privileged agent from a quarantined, untrusted-input-exposed agent, with human approval only for tainted/high-risk actions) as the most credible partial mitigation he's seen for prompt injection, though not yet well-implemented in practice.
- Created the "[[Pelican Riding A Bicycle Benchmark]]" (asking models to generate an SVG of a pelican on a bicycle) as a joke rebuttal to numeric AI benchmarks — found an unexplained but consistent correlation between drawing quality and general model capability; deliberately keeps secret backup prompts (an ocelot on a moped, etc.) to detect if labs ever train specifically to game the benchmark.
- Extensive commentary on [[Open Claw]]: built its first line of code November 25 and reached a (vaporware) Super Bowl ad within ~3.5 months; argues its success proves enormous latent demand for a personal digital assistant, which Anthropic/OpenAI themselves didn't ship because they didn't know how to do it securely — leaving room for an independent, less risk-averse third party. Runs his own instance in a sandboxed Docker container on a dedicated Mac mini, with only read-only access to his work email.
- Day job: open-source data-journalism tooling (his goal is to get "3% credit" on a future Pulitzer-winning story); also does "zero deliverable consulting" (paid hour-long calls, no reports or code).
- [[Sander Schulhoff]] (episode 37, "[[Guardrails Do Not Work]]") independently arrives at closely related conclusions from an AI red-teaming/adversarial-robustness research angle: guardrail vendor "99% blocked" claims are statistically meaningless against an effectively infinite attack space, and a joint OpenAI/Google DeepMind/Anthropic paper Schulhoff co-authored found adaptive human attackers break every state-of-the-art guardrail in 10-30 attempts — direct empirical support for Willison's "[[Normalization Of Deviance]]"/eventual-"Challenger disaster" prediction.

## Related

- [[summary-17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming]] — source summary (his episode)
- [[Django]] — framework he co-created
- [[Datasette]] — data-analysis tool he created
- [[Andrej Karpathy]] — originated the term "vibe coding" that Willison distinguishes from agentic engineering
- [[Agentic Engineering]] / [[Dark Factory Pattern]] — his central framing of professional AI-assisted software work
- [[StrongDM]] — case study for the dark factory pattern
- [[Prompt Injection]] / [[Lethal Trifecta]] — security concepts he coined
- [[CAMEL Pattern]] — mitigation approach he endorses
- [[Normalization Of Deviance]] — framework for his "Challenger disaster" prediction
- [[Pelican Riding A Bicycle Benchmark]] — benchmark he created
- [[Hoarding Things You Know How To Do]] / [[Red-Green TDD]] / [[Thin Template Pattern]] — his agentic-engineering career/technique advice
- [[Open Claw]] — extensively discussed, runs his own instance
- [[Claude Code]] — primary tool, especially Claude Code for Web
- [[ThoughtWorks]] / [[Cloudflare]] / [[Shopify]] — cited for the "AI helps seniors and juniors, squeezes the middle" observation
- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Sander Schulhoff]] — independently arrives at closely related AI security conclusions
- [[Guardrails Do Not Work]] — Schulhoff's thesis, empirically supporting Willison's concerns
