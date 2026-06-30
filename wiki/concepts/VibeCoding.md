---
---
title: "VibeCoding"
type: concept
tags: [ai-coding, development-methodology]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - No More Slop – swyx.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - The New Application Layer - Malte Ubl, CTO Vercel.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - How Lovable self-improves every hour — Benjamin Verbeek, Lovable.md"]
last_updated: 2026-06-30
---

## Definition
Vibe Coding is an AI-assisted coding approach where developers guide AI to write code based on intent and feel rather than precise specifications. The term was coined by [[Lovable]], who built one of the first platforms where users describe what they want in a chat interface and see the result in a visual sandbox without ever looking at code. The quality of outcomes varies significantly depending on approach and taste.

## Key Information
- **Origin**: The term was coined by [[Lovable]], one of the first platforms where users code without looking at code — using a chat interface and visual sandbox to describe what they want, see it, test it, and ship it
- swyx notes there are "different takes on vibe coding" — some much better than others
- Represents one of the tensions AI engineers must navigate: between rapid AI-assisted development and quality
- Can produce either kino (high-quality) or slop (low-quality) code depending on the developer's taste and approach
- Part of the broader theme of coding that dominated the AI Engineer Summit
- Aman Khan contrasts vibe coding with "thrive coding" — using data-driven evaluation to build confidence in outputs rather than shipping based on "looks good to me"
- Vibe coding has its place for prototyping and hacky/fast builds, but cannot be used in production environments where reliability matters

- Al Harris (Amazon Kiro) describes vibe coding as relying heavily on the operator getting things right and providing guardrails — Kiro's spec-driven development aims to add structure to improve reliability
- Kiro was built in response to the observation that "vibe coding is great, but vibe coding relies a lot on me as the operator getting things right"
- **Malte Ubl's usage**: Malte described his personal projects (chat SDK and just bash) as his "vibe coding stack" — side projects hacked on with AI assistance
- **Priscila Andre de Oliveira (Sentry)**: Referenced vibe coding; her presentation was AI-generated. Advocates for "keynote code" (high quality) over slop. Argues that vibe coding quality depends on the tool.
- **Daniel Szoke (Sentry)**: Argues Rust is the ideal language for vibe coding. Conventional wisdom says Python/TypeScript are best because LLMs write them easily on first try. Szoke inverts this: Rust's strict compiler catches LLM errors deterministically at compile time, and AI agents in compile-fix loops can fix them autonomously. The language hardest for LLMs on first try may be safest overall.

## Related
- [[summary-20251222 - No More Slop – swyx]] — source
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[summary-20260420 - The New Application Layer - Malte Ubl, CTO Vercel]] — source (Malte's vibe coding stack)
- [[summary-20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful]] — source
- [[summary-20260527 - The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry]] — source (Priscila's "vibe coded presentation")
- [[summary-20260527 - Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry]] — source (Rust as ideal vibe coding language)
- [[ThriveCoding]] — the data-driven alternative to vibe coding
- [[CodeSlop]] — the negative outcome of poor vibe coding
- [[Kino]] — the positive outcome of good vibe coding
- [[Slop]] — the broader quality problem
- [[Malte Ubl]] — uses vibe coding for personal projects
- [[Vibe Engineering]] — structured extension with engineering practices
- [[Priscila Andre de Oliveira]] — referenced vibe coding; her presentation was AI-generated
- [[DanielSzoke]] — argues Rust is the ideal language for vibe coding
- [[Rust]] — the language argued to be ideal for vibe coding
- [[CompilerGuardrails]] — the deterministic safety net that makes Rust compelling for vibe coding
- [[Lovable]] — coined the term, built one of the first vibe coding platforms
- [[Benjamin Verbeek]] — Member of Technical Staff at Lovable
- [[summary-20260602 - How Lovable self-improves every hour — Benjamin Verbeek, Lovable]] — source (Lovable coining the term)
