---
title: "Agents for Everything Else — swyx"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Agents for Everything Else — swyx.md"
date: 2026-05-01
ingested: 2026-06-29
tags: [keynote, agents, tiny-teams, productivity, ai-engineering, devin, figma, automation]
---

## Core Thesis
swyx presents how the AI Engineer conference team (a 9-person tiny team running a $9M+ business) uses AI agents not just for coding but for "everything else" — design-to-code, conference management, ETL, purchasing, and knowledge work. The key insight: agents unlock productivity gains not by replacing humans but by removing blockers and yak shaves, enabling non-technical team members to execute independently, and making work more fun — which drives more output.

## Key Topics
- **Tiny Teams**: AI Engineer is a 9-person team running a $9M+ business. swyx defines tiny teams as teams with more millions in revenue than number of employees. This is the third year of his keynote series on AI productivity.
- **Death of Yak Shaving**: Agents eliminate the dependency tree crawling of "I have to do X before Y before Z" — particularly for installing dependencies or fixing Python environments. The productivity model that doesn't appreciate parallelism and autonomy is not fully capturing agent benefits.
- **Figma to Website**: Hooked Devin up to Figma (via Coworker) and produced a pixel-perfect website in very short order. The designer was happy. This became the live ai.engineer website.
- **Multiplayer Agent Usage**: 207 replies in a Devin session — swyx kicks off work, goes to bed, designer in Indonesia wakes up and continues prompting Devin with red-line annotations (like Steve Ruiz does with TLDraw). No instruction manual needed — just "how would you communicate with another human being?"
- **Fun as Productivity Driver**: The designer started working on throwaway projects because it was fun. The feedback cycle for non-technical team members went from "waiting/blocked on swyx or contractor" to "have idea → do it." swyx is getting work he's never gotten from employees before — animations, polish, Easter eggs.
- **Agents for Everything Else**: The major theme — moving beyond "how many lines of code" to "getting more productivity out of humans." Agents for conference management (CMS replacement), ETL (syncing vendor data), buying (researching and purchasing a lobster for the conference), and knowledge management (Apple Notes → formatted Notion doc with speaker research).
- **Code as Source of Truth**: The unlock for conference management was throwing away the CMS and committing data to code, letting Devin manage it. Speaker changes come in via email — just forward to Devin with "handle it."
- **AI Replacing SaaS**: swyx argues with employees about kicking out SaaS tools and building replacements with agents. Method: identify top 3 concerns and systematically reduce them.
- **Agent Experience (AX)**: The primary user is shifting from humans to agents. Malte Ubl's data: 60% of Vercel's user base is bots/agents. Dashboards don't matter — APIs, CLIs, and MCPs matter. Custom UI is going away; ship UI to someone else's app.
- **AI Psychosis**: The term swyx uses for the extreme belief in AI's capabilities. Leaders with "the most psychosis" need to bring skeptical employees along the journey without dismissing their valid concerns.
- **Personal Automation**: Agents for buying a lobster for the conference — research phone numbers, emails, websites. This kind of on-demand, serverless knowledge work replaces what an executive assistant or junior employee would do.

## Entities
- [[swyx]] — speaker, co-founder of AI Engineer conferences
- [[Devin]] — AI coding agent from Cognition, used extensively
- [[Cognition]] — company behind Devin; swyx joined them
- [[Coworker]] — tool used to hook Devin up to Figma
- [[Steve Ruiz]] — creator of TLDraw, mentioned for red-line annotation workflow
- [[BenLear]] — co-founder of AI Engineer alongside swyx
- [[aiDotEngineer]] — the AI Engineer conference organization
- [[Figma]] — design tool, source for Devin website generation
- [[TLDraw]] — drawing tool, Steve Ruiz's annotation workflow
- [[Vercel]] — company with 60% agent traffic
- [[Malte Ubl]] — CTO of Vercel, cited for agent traffic data
- [[OpenClaw]] — open-source personal agent, referenced as "nano claw" equivalent
- [[Notion]] — knowledge management, formatted doc output from Apple Notes
- [[Slack]] — company communication, where swyx added Devin

## Concepts
- [[TinyTeam]] — teams with more millions in revenue than employees
- [[YakShaving]] — dependency tree crawling that agents eliminate
- [[AgentsForEverythingElse]] — expanding agents beyond coding to all knowledge work
- [[Agent Experience]] — designing for agent users, not human users
- [[AIReplacingSaaS]] — building replacements for SaaS tools with agents
- [[AIPsychosis]] — extreme belief in AI capabilities; managing the gap between believers and skeptics
- [[ServerlessDevelopers]] — non-technical team members enabled to code via agents
- [[CodeAsSourceOfTruth]] — using code (managed by agents) instead of CMS
- [[PersonalAutomation]] — on-demand agent tasks replacing executive assistants
- [[FigmaToCode]] — pixel-perfect design-to-website via agents
- [[AgentOnboarding]] — getting non-technical teams comfortable with agents
- [[FunAsProductivityDriver]] — agents making work more enjoyable, increasing output
- [[MultiplayerAgentUsage]] — multiple humans collaborating with the same agent session
- [[AgentsForBuying]] — using agents for purchasing and vendor research
- [[AgentsForETL]] — using agents for data syncing and ETL tasks
- [[AgentsForCMS]] — using agents to replace content management systems
- [[OnePizzaTeam]] — related team size concept
- [[Feedback Loops as AI Speed Limit]] — related to removing blockers
- [[Agents as Software Users]] — related to AX theme
- [[SaaS Copocalypse]] — related to AI replacing SaaS

## Related
- [[summary-20251222 - No More Slop – swyx]] — earlier swyx keynote
- [[summary-20260420 - The New Application Layer - Malte Ubl, CTO Vercel]] — Malte's agent traffic data
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — OpenClaw reference
- [[summary-20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer]] — one-pizza team discussion
