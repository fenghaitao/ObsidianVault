---
title: "ContextEngineering"
type: concept
tags: [ai, context, prompt-engineering, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - How we solved Context Management in Agents — Sally-Ann Delucia.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-29
---

## Definition
Context engineering is the deliberate art and science of curating what goes into an AI agent's context window. Coined by Andrej Karpathy, it involves filling the context window with just what the agent needs for the current step — no more, no less — because context is expensive, excess context degrades quality, and bad context can poison outputs.

## Key Information
- Andrej Karpathy: "Context engineering is a delicate art and science of filling the context window with just what needs to happen for the agent to have the right context for the right iteration for the next step."
- Context is expensive: every token added to context is sent as input tokens on every subsequent interaction, accumulating cost rapidly
- More context doesn't always mean better results — quality degrades past ~50% context window fullness (the "dumb zone")
- MCP servers add hidden context overhead: each enabled MCP server loads tool descriptions into the system prompt on every interaction
- Bad context can poison everything: mixing unrelated tasks, outdated comments, or negative patterns from earlier in a session can corrupt outputs
- Four key habits: (1) persist information outside the context window (scratch pads, memory files, agents.md), (2) be selective about what to pull in, (3) summarize/trim/compress as the window grows, (4) isolate context across sessions using parallel agents or fresh sessions
- When things go off the rails: start a new session, have the agent summarize the session for a new agent, verify the summary matches your understanding, then proceed with clean context
- "AI is really great at writing prompts for AI" — use agents to compress and summarize context for new sessions
- **SallyAnn DeLucia's Perspective**: Context management isn't just an engineering problem — it's a product and UX problem. If an agent doesn't have the right context, it gives bad answers, and nobody uses the product. Context engineering is choosing strategically what the model sees, not just fitting under token limits. The best context strategy is one that lets agents remember what they need to and forget what they don't. Agents don't fail because of prompts, they fail because of context.

## Related
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — source transcript
- [[summary-20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic]] — source transcript (context engineering = 80% agentic search)
- [[summary-20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful]] — source transcript
- [[summary-20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust]] — source (context engineering replaces feature engineering as the primary lever for GenAI)
- [[AndrejKarpathy]] — coined the term
- [[AgenticEngineering]] — the parent paradigm
- [[Agentic Search]] — the core mechanism (80% of context engineering)
- [[Context Management]] — related techniques for maintaining coherence
- [[MCP]] — protocol whose servers add context overhead
- [[Parallel Agents]] — context isolation strategy
- [[AgentsDotMd]] — file-based context persistence
- [[ContextRot]] — degradation of context quality over time
- [[Clone the Repo Pattern]] — context strategy for library knowledge
- [[Ralph Loop]] — session restart pattern for context management
- [[SmartTruncation]] — Arize's head+tail truncation with memory approach
- [[LongSessionEvals]] — evaluation technique for measuring context degradation
- [[AlexArizeAgent]] — Arize's agent built with context engineering principles
- [[summary-20260510 - How we solved Context Management in Agents — Sally-Ann Delucia]] — source
- [[ModelAsAPI]] — context engineering is the replacement for feature engineering in the model-as-API paradigm
