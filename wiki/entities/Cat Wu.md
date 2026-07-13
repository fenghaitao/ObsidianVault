---
title: "Cat Wu"
type: entity
tags: [person, claude-code, anthropic, product-management]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/04 - What happens after coding is solved ｜ Fiona Fung (Claude Code & Cowork).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/13 - How Anthropic’s product team moves faster than anyone else ｜ Cat Wu (Head of Product, Claude Code).md"]
last_updated: 2026-07-11
---

## Definition

Cat Wu (transcribed in this source as "Kat Wu") is Head of Product for [[Claude Code]] and [[Claude Cowork]] at [[Anthropic]], overseen by [[Fiona Fung]] and working closely with [[Boris Cherny]] (tech lead/product visionary). Guest on one of [[Lenny's Podcast]]'s most-listened-to episodes ("How Anthropic's product team moves faster than anyone else"), explaining how her team ships product features on 1-day-to-1-month timelines.

## Key Information

- Splits work with Boris Cherny along an "80% mind-meld" line: he sets the 3-6-month product vision; she owns the cross-functional path to it (marketing, sales, finance, capacity) and removing shipping blockers.
- Diagnoses a common mistake among the hundreds of PM candidates she interviews: over-indexing on 6-12-month roadmap alignment with partner teams, a habit left over from when code was expensive. Her prescription for AI-native PMs: set clear, narrow goals; ship almost everything as clearly-branded "research preview" to lower commitment; and build a tight, repeatable process (e.g., a dedicated "evergreen launch room" where an engineer posts a dogfooded feature and marketing/docs/DevRel turn around materials the next day).
- Still writes PRDs, but only for particularly ambiguous or heavy-infrastructure projects; day-to-day alignment instead comes from weekly metrics readouts and a written list of team principles (who the key users are and why) that lets people make decisions without being blocked on a PM.
- On the Claude Code source-code leak: attributes it to human error in a PR-review process (not malice), says the employee involved is still at Anthropic, and says the team hardened its review process afterward.
- On the OpenClaw/third-party-harness token restriction: says Anthropic had to prioritize first-party products/API under infrastructure demand, offering credits as a transition softener — a hard trade-off, not a punitive move.
- PM team is ~30-40 people across research PM (model feedback, launch shepherding), Claude developer platform (APIs, managed agents), Claude Code/Cowork, enterprise (RBAC, cost controls, security), and growth.
- On the future of the PM role: believes engineering, PM, and design are merging into overlapping skill sets, with [[Taste]] (deciding what's worth building) as the one skill that persists regardless of background; favors hiring engineers with strong product taste over adding more pure PMs, since it lowers coordination overhead. Sees an engineering background as useful mainly for estimating build difficulty, but expects that advantage to keep shrinking every few months as models improve. See [[Role Collapse]].
- Names the recurring "[[AGI Pilled|right amount of AGI-pilled]]" tension: it's easy to design for a hypothetical super-capable future model (a single text box), but hard — and the actually valuable skill — to elicit maximum capability from the current model and steer users onto its "golden path."
- Builds this skill (and trains her team) via three practices: (1) asking the model to introspect on why it made an unexpected decision, to find and fix harness/prompt gaps; (2) identifying and trusting a small group of people (~5) with unusually well-calibrated model/harness taste for fast feedback — e.g. [[Amanda]], who shapes Claude's character; (3) building a small number (as few as 10) of high-quality evals to concretely define and track a feature's goal. See [[Evals As Product Definition]].
- Describes Claude's positive, low-ego, confident-but-earnest "character" (credited largely to Amanda's work) as core to why people enjoy working with it, not a cosmetic feature.
- Explains the "[[Building Blocks Progression]]" roadmap for Claude Code/Cowork: single-task success → multiple simultaneous tasks ("multi-clauding") → eventually running many (50-100+) agents in parallel, remotely, with self-improving feedback loops. Credits [[Sid]] with the original to-do-list feature that solved early models' tendency to abandon large refactors partway through — scaffolding later models needed less and less of.
- Cites an [[Andrej Karpathy]] tweet (via Lenny) about the divide between people who tried early chatbots, found them unimpressive, and stayed cynical, versus people who've seen AI's full power through coding tools — her advice is to actually use current tools for real work rather than judge from an old first impression.
- States a hard automation principle: an automation that works 95% of the time isn't really an automation — the last 5-10% is where the real value is, and it's worth the extra "elbow grease" to get there. See [[100% Automation Threshold]].
- On mission as Anthropic's key structural advantage: the company's central mission (safe AGI for humanity) sits above any individual product line, so teams will sacrifice their own goals for the company's — "if Claude Code failed but Anthropic succeeded, I would be extremely happy." See [[Mission Over Product]].
- Personal tool usage: Claude Code (CLI) for quick one-off/parallel coding tasks; Claude Desktop for front-end/visual work (live preview pane) and non-technical users; Claude mobile/web for kicking off tasks away from a laptop; Claude Cowork for anything with a non-code output (decks, inbox management, docs) — built an entire 20-page conference-talk slide deck overnight in Cowork by connecting Calendar/Slack/Gmail/Drive and her org's design-system template.
- Personal/lightning-round notes: recommends *How Asia Works*, *The Technology Trap*, and *The Paper Menagerie*; loves *Drive to Survive* and *Free Solo* (she's a rock climber); daily Waymo user (worth a 2x price premium to her over Uber/Lyft) — see [[Waymo]]; life motto "just do things" / "jobs are fake"; favorite Claude "thinking word" is "manifesting"; would spend post-AGI time rock climbing (dreams of living in Fontainebleau) and catching up on a large reading backlog.

## Related

- [[summary-04 - What happens after coding is solved ｜ Fiona Fung (Claude Code & Cowork)]] — source summary
- [[summary-13 - How Anthropic’s product team moves faster than anyone else ｜ Cat Wu (Head of Product, Claude Code)]] — source summary (her own episode)
- [[Fiona Fung]] — manager who oversees her
- [[Boris Cherny]] — close working partner (tech lead/product vision)
- [[Claude Code]] / [[Claude Cowork]] — products she leads
- [[Anthropic]] — employer
- [[Taste]] — the skill she says persists regardless of PM/eng/design background
- [[Role Collapse]] — the broader trend she describes across PM/eng/design
- [[AGI Pilled]] — the core tension she names in building AI-native products
- [[Amanda]] — colleague she cites as exceptional at model/character evaluation
- [[Evals As Product Definition]] — her practice for concretely defining feature success
- [[Building Blocks Progression]] — the Claude Code/Cowork roadmap she describes
- [[100% Automation Threshold]] — her automation-quality principle
- [[Mission Over Product]] — Anthropic's structural advantage, in her framing
- [[Waymo]] — personal daily-use product
- [[Open Claw]] — third-party harness affected by the token-access decision she discusses
- [[Sid]] — colleague credited with Claude Code's to-do-list feature
- [[Andrej Karpathy]] — cites his tweet on AI perception divides
