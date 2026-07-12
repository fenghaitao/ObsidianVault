---
title: "Vibe Coding"
type: concept
tags: [AI, coding, software-development, hype]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/26 - OpenAI's head of platform engineering on the next 12-24 months of AI ｜ Sherwin Wu.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/39 - Inside OpenAI： 2026 is the year of agents, AI's biggest bottleneck, and why compute isn't the issue.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/38 - The new AI growth playbook for 2026 ｜ How Lovable hit $200M ARR in one year.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/32 - How to show up in any room with a low heart rate： Silicon Valley's missing etiquette playbook.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/27 - The rise of the professional vibe coder (a new AI-era job).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/29 - Marc Andreessen： The real AI boom hasn't even started yet.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We've passed the inflection point & dark factories are coming.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo.md"]
last_updated: 2026-07-11
---

## Definition

Vibe coding is the practice of using AI to generate code by describing what you want in natural language. Edwin Chen considers it overhyped and warns about long-term maintainability issues.

## Key Information

- Edwin: "I definitely think that vibe coding is overhyped"
- The concern: "people don't realize how much it's going to make their systems unmaintainable in the long term if they simply dump this code into their code bases if it seems to work out right now"
- This is distinct from the more positive vision of AI-generated product UIs (like Claude Artifacts) where the AI helps people achieve their ideas in a more interactive way
- The risk is that AI-generated code that "seems to work" may create technical debt that compounds over time
- At OpenAI, designers are "vibe coding" prototypes of the Codex app and landing PRs directly — they build standalone prototypes, then vibe engineer them into actual PRs
- Alexander Imbiricos describes a designer who built a coin animation by vibe coding an animation editor, using the editor to create the animation, then checking it into the repo
- "Vibe coding" is now a common practice at OpenAI, with designers doing substantial product work through throwaway prototypes built with Codex
- Elena Verna considers vibe coding a skill worth adding to resumes, alongside Excel; it takes a few iterations to learn how to translate ideas effectively
- Vibe coding is creating a new full-time job role: "vibe coder" — a non-technical person who uses AI tools to prototype and ship products
- The vibe coding market is in the "Capabilities" stage (John Cuddler's framework): everyone is exploring what's possible, and capabilities change every 1-3 months
- Lovable uses vibe coding internally: specs are accompanied by Lovable prototypes, pricing page changes are prototyped by vibe coding screenshots, and the company runs internal hackathons
- The feedback cycle from idea to functioning product has collapsed to as little as one day with vibe coding
- Elena describes vibe coding as addictive: "you just go... this is possible, I had no idea, I want to keep building"

- Sam Lessin built the first version of Letter Meme (lettermeme.com) end-to-end using vibe coding with Cursor, DigitalOcean, and Cloudflare, though he notes vibe coding doesn't scale and had engineer friends upgrade it later
- Zevi Arnovitz distinguishes between "vibe coding" (just going with the vibes, no planning) and "really building serious apps" (structured exploration, planning, and review)
- Zevi: "The big difference between just vibe coding and going along with the vibes and really building serious apps [is planning]. I spend a lot of time going back and forth and understanding."
- Zevi describes his early approach as "vibe coding" — running at the wall until it worked, without updating documentation or tooling
- Zevi graduated from "vibe coding" to a structured workflow after realizing that planning prevents "gnarly bugs"
- The key insight: AI coding tools (Bolt, Lovable) are "super eager to write code" — their system prompt is "you're a coding agent," so they skip planning
- Lazar started vibe coding in July 2024, seven months before Karpathy coined the term in early 2025
- Lazar's definition: "Vibe coding is just coding in 12 months from now" — it will become the default way of building software
- Professional vibe coding involves 80% planning/chatting and 20% executing, with structured PRDs, rules files, and documentation
- The Genie/Aladdin metaphor: AI has limited token context, and vague prompts produce wrong results
- Key distinction: "vibe your way for fun and while prototyping, but when exploration is done, use referencing documentation"
- Marc Andreessen's 10-year-old son independently discovered Replit and vibe coding without parental influence, and is obsessed with building Star Trek simulators using the LCARS design language
- Marc's son spends hours vibe coding games and simulators — an example of how the technology is accessible even to children
- Marc notes that his son discovered it on his own (or through friends), not through him, highlighting the organic adoption of vibe coding tools

- Sherwin Wu draws the Sorcerer's Apprentice analogy for vibe coding: it's powerful and high-leverage, but you need to supervise the agents
- Sherwin: "It literally feels like we're wizards now... casting all these spells and having software do all these things for you"
- The SICP textbook (1980) described programming as sorcery — AI makes it "literally incantations"
- The risk: "Mickey sets the brooms off on a task and then goes to sleep" — vibe coding without supervision
- Seniority matters: "there is some skill and some seniority... a lot of thought that needs to go into this"

- Simon Wilson's distinction: "vibe coding" should be reserved for the hands-off approach (Andrej Karpathy's original definition: "you don't even look at the code"). When professional engineers use AI to write production code that they review and verify, Simon calls that "agentic engineering" — keeping the terms separate prevents "vibe coding" from being devalued.
- Simon's rule of thumb: "If you're vibe coding something for yourself where the only person who gets hurt if it has bugs is you, go wild. The moment you're vibe coding code for other people to use, where your bugs might actually harm somebody else, that's when you need to take a step back"
- Simon writes ~95% of his code via AI and often writes it from his phone — but he distinguishes this from vibe coding because he reviews the code
- Open Claw is described as "very vibe coded" — over 1,000 contributors, "extraordinary kind of a miracle that it works as well as it does"

## Related

- [[summary-40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen]] — source summary
- [[summary-38 - The new AI growth playbook for 2026 ｜ How Lovable hit $200M ARR in one year]] — source summary
- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Claude]] — Claude's Artifacts are a more positive vision of AI-generated UIs
- [[Lovable]] — leading vibe coding platform
- [[Elena Verna]] — advocates for vibe coding as a skill
- [[Vibe Coder (role)]] — emerging job role
- [[Zevi Arnovitz]] — distinguished between vibe coding and serious building
- [[Slash Commands Workflow]] — the structured alternative to vibe coding
- [[Minimum Lovable Product]] — related product philosophy
- [[summary-29 - Marc Andreessen： The real AI boom hasn't even started yet]] — source summary
- [[Marc Andreessen]] — his son discovered vibe coding independently
- [[Replit]] — platform Marc's son uses for vibe coding
- [[Star Trek]] — what Marc's son builds with vibe coding
