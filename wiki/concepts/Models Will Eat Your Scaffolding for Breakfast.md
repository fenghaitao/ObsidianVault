---
title: "Models Will Eat Your Scaffolding for Breakfast"
type: concept
tags: [AI, development, best-practice, scaffolding, frameworks]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/26 - OpenAI's head of platform engineering on the next 12-24 months of AI ｜ Sherwin Wu.md"]
last_updated: 2026-07-10
---

## Definition

"Models will eat your scaffolding for breakfast" is a phrase coined by Nicholas (founder of FinTool) that captures the phenomenon where improving AI models disrupt and obsolete the tooling, frameworks, and abstractions built around them. The scaffolding you build today to steer and control models may be rendered unnecessary as the models themselves get smarter.

## Key Information

- Coined by Nicholas, founder of FinTool, in an article on X about best practices for building AI agents in financial services
- Sherwin Wu references this phrase as a core truth about building with AI APIs
- Historical examples: agent frameworks (less useful now), vector stores (2023-era scaffolding that's being replaced by simpler search + tool approaches), skills files (current scaffolding that may be next to go)
- The pattern: in 2022 when ChatGPT launched, models were raw and needed heavy scaffolding (agent frameworks, vector stores). As models improved, they "ate" much of that scaffolding
- Current scaffolding that may be at risk: skills files, context management files, agent orchestration frameworks
- This is an instance of "The Bitter Lesson" applied to building with AI: general methods (smarter models) outperform specialized human-built scaffolding
- Sherwin's advice: "Build for where the models are going and not where they are today"
- Even OpenAI's API team has been "guilty" of building scaffolding that models later ate
- The moving target nature of building on AI makes it both exciting and challenging

## Related

- [[The Bitter Lesson]] — the broader AI principle this instantiates
- [[Build for Where Models Are Going]] — the strategic response
- [[FinTool]] — where the phrase originated
- [[Sherwin Wu]] — referenced the phrase
- [[summary-26 - OpenAI's head of platform engineering on the next 12-24 months of AI ｜ Sherwin Wu]] — source summary
