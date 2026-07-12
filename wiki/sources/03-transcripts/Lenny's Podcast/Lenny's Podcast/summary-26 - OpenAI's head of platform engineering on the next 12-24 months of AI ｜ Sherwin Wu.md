---
title: "OpenAI's head of platform engineering on the next 12-24 months of AI ｜ Sherwin Wu"
type: summary
source: "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/26 - OpenAI's head of platform engineering on the next 12-24 months of AI ｜ Sherwin Wu.md"
playlist: "Lenny's Podcast"
date: 2026-07-10
tags: [podcast, AI, OpenAI, Codex, software-engineering, API, platform, agents, startups]
---

## Core Thesis

Sherwin Wu, head of engineering for OpenAI's API and developer platform, describes how AI is fundamentally transforming software engineering — 95% of OpenAI engineers use Codex, 100% of PRs are reviewed by Codex, and engineers are becoming "tech leads" managing fleets of AI agents. He predicts that in the next 12-24 months, models will achieve multi-hour coherent task execution, multimodal audio will unlock new enterprise use cases, and the collapsing cost of building software will usher in a golden age of B2B SaaS and startups. His core advice: build for where the models are going, not where they are today.

## Entities

- [[Sherwin Wu]] — head of engineering for OpenAI's API and developer platform
- [[OpenAI]] — AI research organization behind ChatGPT, Codex, and the API platform
- [[Codex]] — OpenAI's coding agent, used by 95% of OpenAI engineers, reviews 100% of PRs
- [[ChatGPT]] — OpenAI's consumer AI product with 800M+ weekly active users
- [[Sam Altman]] — CEO of OpenAI, coined "one-person billion dollar startup"
- [[Greg Brockman]] — OpenAI president, reinforces platform ecosystem philosophy
- [[Kevin Weil]] — VP of Science at OpenAI, coined "this is the worst the models will ever be"
- [[Lenny Rachitsky]] — host of Lenny's Podcast
- [[Peter / OpenClaw]] — developer of OpenClaw, power user of Codex
- [[Cursor]] — AI-powered code editor, competitor in the AI coding space
- [[SICP]] — Structure and Interpretation of Computer Programs (the "wizard book"), inspirations behind the sorcery metaphor for programming
- [[The Mythical Man-Month]] — Fred Brooks's book with the "surgeon" metaphor for software engineering
- [[Ubiquiti]] — home networking and security camera product, praised as "the Apple of home networking"
- [[Eero]] — competing home networking product
- [[Quora]] — Sherwin Wu's first job out of college
- [[OpenDoor]] — Sherwin's previous company where he built home pricing models
- [[Zillow]] — real estate company, referenced for front door ROI research
- [[Sentry]] — error tracking and AI debugging platform (Seir agent), sponsor
- [[Datadog]] — observability and experimentation platform (EPO), sponsor
- [[DX]] — developer intelligence platform, sponsor
- [[Dan Wang]] — author of "Breakneck" (book on US-China dynamics)
- [[Patrick McGee]] — author of book on Apple and China
- [[There Is No Antimemetics Division]] — sci-fi book by qntm, recommended by Sherwin
- [[Jujutsu Kaisen]] — anime series, Season 3 recommended by Sherwin
- [[Apple]] — technology company, Sherwin is a self-described "Apple fanboy"
- [[Mark Zuckerberg]] — referenced as example of same iPhone as regular users
- [[Marc Andreessen]] — quoted: "AI makes good people better and it makes great people exceptional"
- [[FinTool]] — startup by Nicholas, where the "models will eat your scaffolding" quote originated
- [[Fantasia]] — Disney film, source of the Sorcerer's Apprentice analogy

## Concepts

- [[Sorcerer's Apprentice Problem (AI)]] — the risk of AI agents running wild when unsupervised, like Mickey Mouse flooding the sorcerer's workshop
- [[Models Will Eat Your Scaffolding for Breakfast]] — as models improve, they disrupt the tooling and frameworks built around them
- [[Build for Where Models Are Going]] — design products for future model capabilities, not current limitations
- [[The Worst the Models Will Ever Be]] — Kevin Weil's reminder that today's models are the least capable they'll ever be
- [[One-Person Billion Dollar Startup]] — Sam Altman's vision of extreme individual leverage through AI
- [[Golden Age of B2B SaaS]] — the second-order effect: many small startups building bespoke software for each other
- [[Business Process Automation (BPA) in AI]] — underrated opportunity: automating repeatable business operations, not just open-ended engineering work
- [[Top-Down vs Bottom-Up AI Adoption]] — successful AI deployments need both executive buy-in and grassroots employee excitement
- [[AI Tiger Team]] — a dedicated internal team to explore AI capabilities, evangelize, and create bottom-up adoption
- [[Multi-Hour Coherent AI Tasks]] — the next frontier: models that can work coherently for hours, not just minutes
- [[Multimodal Audio AI]] — underrated domain: speech-to-speech models for enterprise use cases
- [[Context as Key to Agent Success]] — when agents fail, it's usually a context/underspecification problem, not a model capability problem
- [[Engineering Manager as Surgeon]] — management philosophy: treat engineers like surgeons and the manager's job is to hand them scalpels before they ask
- [[Ecosystem Platform Company]] — OpenAI's philosophy of enabling an ecosystem via API, not squashing startups
- [[Never Feel Sorry for Yourself]] — Sherwin's life motto: always maintain a sense of agency
- [[The Bitter Lesson]] — applied to building with AI: the models keep eating the scaffolding
- [[AI-Native Codebase]] — 100% Codex-written codebase experiment at OpenAI, no escape hatch
- [[Vibe Coding]] — Sherwin draws the Sorcerer's Apprentice analogy: powerful but requires supervision

## Key Takeaways

1. **95% of OpenAI engineers use Codex daily; 100% of PRs are reviewed by Codex.** Engineers who use Codex more open 70% more PRs, and the gap is widening. Code review has gone from a 10-15 minute task to 2-3 minutes.

2. **Engineers are becoming tech leads managing fleets of agents.** Senior engineers now run 10-20 parallel Codex threads, checking in, steering, and giving feedback. The job has shifted from writing code to managing AI agents.

3. **"This is the worst the models will ever be"** (Kevin Weil). The models will only get better at software engineering, and trust in them will continue to grow.

4. **The Sorcerer's Apprentice is the right metaphor for AI coding.** It's extremely powerful and high-leverage, but you need to know what you're doing — the brooms can go wild. Seniority and skill matter in directing agents.

5. **When agents fail, it's usually a context problem.** The 100% Codex codebase experiment at OpenAI revealed that underspecification and lack of documentation are the main blockers. The fix is to encode tribal knowledge into the codebase via docs, comments, and MD files.

6. **"Models will eat your scaffolding for breakfast."** Agent frameworks, vector stores, and skills files — the tooling built around models gets disrupted as models improve. Build for where models are going, not where they are today.

7. **The one-person billion dollar startup implies a golden age of B2B SaaS.** If one person can build a billion-dollar company, there will be hundreds of smaller startups building bespoke software — a massive explosion of B2B SaaS.

8. **Business process automation is a massively underrated AI opportunity.** Silicon Valley focuses on open-ended engineering work, but most of the economy runs on repeatable business processes — SOPs, operations, support workflows. This is where AI will have huge impact.

9. **Successful AI deployments need both top-down buy-in AND bottom-up adoption.** Companies that fail at AI ROI typically have a top-down mandate without grassroots excitement. Build an AI tiger team of excited technical-adjacent employees to evangelize.

10. **Spend more than 50% of your time with top performers.** AI supercharges the best people. As a manager, unblock them, empower them, and treat them like surgeons — your job is to hand them scalpels before they ask.

11. **Multi-hour coherent tasks and multimodal audio are the next 12-18 month frontiers.** Models will go from minute-long tasks to multi-hour coherent work. Audio (speech-to-speech) is hugely underrated for enterprise use cases.

12. **OpenAI views itself as a platform company, not a startup squasher.** The API was the first product. Every model released in a product also gets released in the API. The mission is to spread AI's benefits to all of humanity — and the API ecosystem is how they do it at scale.

## Related

- [[summary-39 - Inside OpenAI： 2026 is the year of agents, AI's biggest bottleneck, and why compute isn't the issue]]
- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]]
- [[summary-38 - The new AI growth playbook for 2026 ｜ How Lovable hit $200M ARR in one year]]
- [[summary-41 - Why AI is disrupting traditional product management ｜ Tomer Cohen (LinkedIn CPO)]]
