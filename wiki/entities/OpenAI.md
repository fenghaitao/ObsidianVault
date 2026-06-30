---
title: "OpenAI"
type: entity
tags: [company, ai, frontier-models]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - No More Slop – swyx.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240726 - Copilots Everywhere： Thomas Dohmke and Eugene Yan.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - The New Application Layer - Malte Ubl, CTO Vercel.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - The End of Apps — Kitze, Sizzy.co.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Mastering AI Pricing — Mayank Pant, Stripe.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-29
---

## Definition
OpenAI is a leading AI research company co-founded by Greg Brockman, known for frontier models and the Sora video generation tool. It contributes to the frontier model capabilities pillar of autonomy.

## Key Information
- Co-founded by Greg Brockman, who preaches modularity in AI system design
- **Codex**: A version of GPT-3 released in preview in 2020, which powered the original GitHub Copilot. GitHub had early access and used it to build the first AI auto-completion developer tool, built entirely remotely during the lockdown
- Produces Sora, a video generation tool that can produce both "kino" (creative, high-quality) and "slop" (low-quality) outputs depending on the user
- Demonstrated similar results to Anthropic in running long-horizon coherent tasks
- One of the frontier model providers whose capabilities form the first pillar of autonomy in Replit's framework
- Used as the LLM provider in Arize's prompt learning workshop, with models accessed via API key for the optimization loop
- The workshop used OpenAI's JSON response format and zero temperature for consistent, structured outputs
- swyx noted that the same tool (Sora) can produce vastly different quality outputs — the difference is in taste and execution
- CPO Kevin Weil publicly stated at Lenny's conference that OpenAI's models hallucinate and that writing evals is essential — cited by Aman Khan as evidence that even model creators acknowledge the reliability problem
- o1-preview had a time horizon of ~15 minutes in METR's measurements
- GPT 5.1 CEX max represents the most recent data point on METR's time horizon trend line

- The Manus API supports the OpenAI responses SDK for compatibility with existing AI frameworks
- OpenAI embeddings are used with Chroma vector database in Manus-built applications for semantic search
- **OpenAI Agents SDK**: Launched around May 2025, available in Python and TypeScript. Provides agents with tools, handoffs, guardrails, and tracing. Integrated with Temporal for durability.
- **Temporal integration**: OpenAI made the `Runner` class abstract in the Agents SDK so Temporal could provide a durable implementation. OpenAI Codex and OpenAI image gen both run on Temporal.
- **Responses API**: Used for tool calling; unlike the Completions API, there is currently no public API to generate JSON tool descriptions from function doc strings (an open issue)

- In the 2024 AI Engineer Summit keynote, OpenAI models were discussed as the reference point for LLM cost reduction trends: the DaVinci API (original GPT-3), text-davinci-002 (underlying ChatGPT), and GPT-4 each represented distinct capability tiers with ~15 months between each order-of-magnitude cost reduction. GPT-4 was noted as a model with high benchmark scores (87% on Spider SQL) that do not automatically translate to product success.
- Sam Altman's "steamrolling" phrase was referenced — the idea that model providers will inevitably build features for all customers, so application builders should avoid competing on capabilities the providers will commoditize.
- **OpenClaw relationship**: Peter Steinberger joined OpenAI to work on bringing agents to everyone. "OpenAI bought OpenClaw — that's not the truth. They might have bought my soul.md." OpenAI understands that supporting OpenClaw is strategically useful: users who play with OpenClaw at home will come to work asking "why don't we have AI at work?", creating demand for enterprise AI tools.
- OpenAI is "moving more into the open direction" — Codex is open source, released Symphony orchestration layer. Peter contrasted this with "some other top tier labs that start with an A" that "very much will sue you if you leak any of their source or block you if you are too successful."
- Peter deliberately limits OpenAI involvement in OpenClaw to avoid perception of takeover — "I could get a lot more people from OpenAI to help with the project, but that would just make a picture that they could have taken over the project and I don't want that."
- Part of Peter's role at OpenAI is "to help them not make the same mistakes again" that were learned at OpenClaw
- **Malte Ubl's perspective**: OpenAI is one of the three major model providers (alongside Anthropic and Google) in the model commoditization thesis. Codex is described as "amazing" and part of the competitive dynamic that drives prices down.
- **BullshitBench performance**: GPT models score ~50/50 on BullshitBench — they go along with nonsense questions about half the time. GPT-5.4 traces show the model questioning the premise in one line then spending 20 paragraphs trying to solve it anyway. OpenAI models show no clear upward trend in nonsense detection over time.
- **MCP Apps co-development**: Partnered with Anthropic and the MCPUI team to standardize MCP Apps as the first official MCP extension. ChatGPT supports MCP Apps and recommends it as the way to build ChatGPT apps.
- **Advanced Voice Mode**: Half-duplex speech-to-speech model — either listening or speaking, not both. Runs at a loss as a marketing initiative, using a "gigantic multimodal model." Cannot handle simultaneous speaking or back-channeling.
- **Real-time API**: Uses a single speech-to-speech model behind the scenes — an example of the emerging speech-to-speech architecture. Like Nvidia Voice Chat, still struggles with instruction following and tool calling.
- **Whisper**: Released in 2022 as a batch STT model trained on 30-second audio clips. Now being superseded by streaming-native architectures for voice agent use cases.

## Related
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — source
- [[summary-20251222 - No More Slop – swyx]] — source
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
- [[summary-20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR]] — source
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[summary-20240726 - Copilots Everywhere： Thomas Dohmke and Eugene Yan]] — source (Codex and Copilot origins)
- [[GitHub Copilot]] — powered by OpenAI Codex
- [[GregBrockman]] — co-founder
- [[Three Pillars of Autonomy]] — framework
- [[Anthropic]] — peer company in frontier models
- [[Slop]] — can be produced by their tools
- [[Kino]] — can also be produced by their tools
- [[PromptOptimizationLoop]] — workshop using OpenAI models
- [[TimeHorizon]] — metric measured on OpenAI models
- [[ManusAPI]] — supports OpenAI responses SDK
- [[Chroma]] — used with OpenAI embeddings
- [[OpenAIAgentsSDK]] — agent framework
- [[Temporal]] — integration partner; Codex and image gen run on Temporal
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — source
- [[summary-20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR]] — source
- [[WorkOS]] — authentication provider for OpenAI
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]] — source
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source (cost reduction trends, model-as-moat discussion)
- [[SamAltman]] — referenced for "steamrolling" concept
- [[summary-20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI]] — source
- [[GPT 5.2]] — model release enabling "code is free"
- [[Symphony]] — agent orchestrator treating code as disposable build artifact
- [[RyanLopopolo]] — MTS at OpenAI, coined Harness Engineering
- [[Harness Engineering]] — discipline coined by Ryan Lopopolo
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — source (OpenClaw relationship, open source direction)
- [[PeterSteinberger]] — employee, OpenClaw creator
- [[OpenClaw]] — project OpenAI supports
- [[summary-20260420 - The New Application Layer - Malte Ubl, CTO Vercel]] — source (model commoditization thesis)
- [[Model Commoditization]] — strategic context
- [[Google]] — commoditizing competitor
- [[summary-20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench]] — source (BullshitBench ~50/50 performance)
- [[BullshitBench]] — benchmark where GPT models are mid-tier
- [[Nonsense Detection]] — capability where OpenAI models struggle
- [[Reasoning Limits]] — GPT-5.4 overthinking observed in traces
- [[Peter Gostev]] — BullshitBench creator
- [[summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop]] — source (self-diagnostics inspiration paper)
- [[SelfDiagnostics]] — inspired by OpenAI's December paper on self-confessing misalignment
- [[summary-20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful]] — source (GPT 5.4 used for vibe engineering)
- [[Model Prompting Styles]] — GPT models prefer lowercase prompts
- [[Vibe Engineering]] — methodology using GPT 5.4
- [[summary-20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI]] — source (advanced voice mode)
- [[Half Duplex]] — limitation of advanced voice mode
- [[Voice AI Cost]] — voice mode runs at a loss
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source (real-time API, Whisper)
- [[Whisper]] — batch STT model
- [[Voice Chat (Nvidia)]] — comparable speech-to-speech model