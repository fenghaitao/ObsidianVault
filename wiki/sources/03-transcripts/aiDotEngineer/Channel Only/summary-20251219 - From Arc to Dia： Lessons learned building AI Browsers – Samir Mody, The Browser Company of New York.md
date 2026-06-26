---
title: "summary-20251219 - From Arc to Dia： Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York"
type: source
tags: [source, transcript, ai-browsers, browser-company]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251219 - From Arc to Dia： Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York.md"]
last_updated: 2026-06-25
---

## Core Summary

Samir Mody, head of AI engineering at The Browser Company of New York, shares the company's journey from building Arc (2022) to Dia (2025), their AI-native browser. The talk covers four key lessons: optimizing tools and process for faster iteration (building prompt editors, evals, and automation into the product itself), treating model behavior as a craft and discipline (behavior design, data collection, model steering), AI security as an emergent property of product building (with focus on prompt injection prevention through UX confirmation steps), and the importance of embracing technology shifts with company-wide conviction.

## Key Points

- The Browser Company built all their AI tooling (prompt editors, evals, data collection) directly into Dia, enabling everyone from CEO to new hires to ideate and iterate on AI features with full personal context.
- They use a technique called Jeba (based on a 2025 paper) for sample-efficient prompt optimization: seed prompts, execute on tasks, score, select best via PA selection, reflect, and mutate — tuning text rather than weights.
- Model behavior is treated as a discipline with three phases: behavior design (tone, style, response shape), data collection for measurement/training, and model steering (prompting, model selection, context window).
- Prompt injection prevention in browsers is critical due to the "lethal trifecta": access to private data, exposure to untrusted content, and ability to externally communicate.
- Their security approach blends technology with UX: confirmation steps before autofill, scheduling, or email actions give users control and awareness even when injections occur.
- The formation of their model behavior team came from a strategy & ops person who rewrote all prompts over a weekend, unlocking a new level of product quality.

## Related

- [[TheBrowserCompany]] — company behind Arc and Dia browsers
- [[SamirMody]] — head of AI engineering at The Browser Company
- [[DiaBrowser]] — AI-native browser by The Browser Company
- [[ArcBrowser]] — predecessor browser to Dia
- [[ModelBehavior]] — craft and discipline of shaping LLM behavior
- [[PromptInjection]] — security vulnerability in LLM-powered applications
- [[Jeba]] — sample-efficient prompt optimization technique
- [[AIBrowsers]] — category of AI-native web browsers
