---
title: "Codex"
type: entity
tags: [AI-product, OpenAI, coding-agent, agent]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/26 - OpenAI's head of platform engineering on the next 12-24 months of AI ｜ Sherwin Wu.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/39 - Inside OpenAI： 2026 is the year of agents, AI's biggest bottleneck, and why compute isn't the issue.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/27 - The rise of the professional vibe coder (a new AI-era job).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We've passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-10
---

## Definition

Codex is OpenAI's coding agent — an IDE extension (VS Code), CLI tool, and cloud product that acts as a software engineering teammate. It can answer questions about code, write code, run tests, execute code, and participate across the full software development lifecycle.

## Key Information

- Product lead is Alexander Imbiricos
- Has seen 20x growth since the launch of GPT-5 in August 2025
- Codex models serve many trillions of tokens per week and are the most served coding model in OpenAI's API
- The key product unlock was shifting from a cloud-only async agent (Codex Cloud) to an IDE/CLI-integrated interactive agent that works locally in a sandbox
- The original "Codex" brand at OpenAI was the model powering GitHub Copilot years ago; OpenAI reused the brand for their own coding agent
- Compaction is a critical feature that enables Codex to run for 24+ hours by managing context windows
- GPT-5.1 Codex Max is the latest model, ~30% faster and more intelligent at higher reasoning levels
- Routinely used for multi-hour/overnight tasks — users report it running for 24+ hours on hard problems
- André Karpathy praised Codex for solving his "gnarliest bugs" that no other tool could solve
- Codex is now used by all technical staff at OpenAI, including designers, PMs, product marketers, and researchers
- Codex is being used for its own training runs — babysitting training graphs, catching configuration mistakes, and being on call for training issues
- The Sora Android app was built using Codex in 18 days (employee launch) and 28 days total (public GA) by 2-3 engineers
- Atlas (OpenAI's browser) was accelerated by Codex, with tasks that previously took 2-3 weeks for 2-3 engineers now taking 1 engineer, 1 week
- The team is actively building features for code review (not just code writing), making review more fun and efficient
- The vision is to evolve from a tool you prompt into a proactive teammate that anticipates needs without being asked
- Codex is best used by giving it your hardest tasks, not trivial ones — work with it like onboarding a new teammate
- Tips for success: try tasks in parallel, ask it to understand the codebase first, formulate a plan together, build trust incrementally
- Has a Slack integration for quick questions, and a browser integration (Atlas) for contextual web assistance
- The Codex team is structured as a tightly integrated product and research team iterating on model and harness together
- The agent stack has three layers: the reasoning model, the API, and the harness — all three must be optimized together
- The team monitors Reddit (r/codex) and Twitter/X for user feedback, treating complaints seriously
- GPT-5.1 Codex Max is the first model that natively understands PowerShell for Windows support
- Zevi Arnovitz uses Codex (GPT-5.1 Max) as one of the models in his multi-model peer review workflow
- Zevi describes Codex's personality as "the best coder within the company who comes to the office with a hoodie and sandals and sits in a dark room"
- Codex solves the hardest bugs but is "really not communicative" — it just fixes things without explaining
- Zevi: "You only bother him when you have the worst bugs... he'll just close the door for two hours and come out and say 'I fixed it'"
- Part of Zevi's peer review system: Claude (dev lead), Codex, and Gemini each review code independently, then Claude evaluates all findings
- [[Kiti Bottom]] works on Codex at OpenAI, helping build the code review product which has gained "extreme amount of traction" catching bugs both at OpenAI and with external customers
- When deploying new model changes for code review, the team AB tests to identify whether it finds the right mistakes and monitors user reactions — if users get annoyed, they switch off the product entirely
- Codex's eval approach is balanced: evals for core product safety + heavy customer feedback monitoring + social media listening to quickly fix problems
- [[Caffeinate]] is used by Codex team members to prevent Mac from sleeping during multi-hour local Codex tasks

- 95% of OpenAI engineers use Codex on a daily basis (Sherwin Wu, 2026)
- 100% of PRs at OpenAI are reviewed by Codex daily — any code that goes into production has Codex's eyes on it
- Engineers who use Codex more open 70% more PRs than those who don't, and the gap is widening over time
- An internal team at OpenAI is maintaining a 100% Codex-written codebase as an experiment, with no "escape hatch" to manually write code
- When Codex agents fail, it's usually a context/underspecification problem — the fix is to add documentation and encode tribal knowledge into the codebase
- Codex has made code review go from a 10-15 minute task to 2-3 minutes for many engineers
- For small PRs, engineers often trust Codex alone without a human reviewer
- The CI process and post-push/deployment process have been heavily automated via Codex internally
- Codex models are the most served coding model in OpenAI's API
- Peter (OpenClaw developer) is a power user who trusts Codex enough to "almost certainly commit it to master"
- Sherwin Wu: "It literally feels like we're wizards now... casting all these spells and having software do all these things for you"
- The Sorcerer's Apprentice analogy: Codex is extremely powerful and high-leverage, but you need to supervise it — the brooms can go wild

## Related

- [[Alexander Imbiricos]] — product lead
- [[OpenAI]] — company
- [[ChatGPT]] — related product, vision of super assistant
- [[Atlas]] — OpenAI's browser, integrated with Codex
- [[GPT-5]] — foundation model
- [[summary-39 - Inside OpenAI： 2026 is the year of agents, AI's biggest bottleneck, and why compute isn't the issue]] — source summary
- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Zevi Arnovitz]] — uses Codex for peer review
- [[Multi-Model Peer Review]] — Zevi's code review technique
- [[Model Personality Types]] — Zevi's anthropomorphization of AI models
- [[Kiti Bottom]] — works on Codex at OpenAI
- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — additional source
