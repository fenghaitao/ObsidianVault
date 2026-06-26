---
title: "Anthropic"
type: entity
tags: [company, ai, frontier-models, claude]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240805 - What's new from Anthropic and what's next： Alex Albert.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - No More Slop – swyx.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Welcome to AIE CODE - Jed Borovik, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gateways are All You Need — Karan Sampath, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240724 - From Software Developer to AI Engineer： Antje Barth.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - The New Application Layer - Malte Ubl, CTO Vercel.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Taste & Craft： A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - The End of Apps — Kitze, Sizzy.co.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer.md"]
last_updated: 2026-06-26
---

## Definition
Anthropic is an AI research company known for its Claude models, which pioneered the computer use capability and advanced context management techniques for long-running autonomous agents.

## Key Information
- **Claude 3.5 Sonnet** (August 2024): First model in the Claude 3.5 family, a middle-tier model that outperforms Claude 3 Opus. 200k context with near-perfect recall, state-of-the-art vision (table transcriptions, OCR, screenshot-to-code), 64% on internal PR evaluations. 5x cheaper than 3 Opus at $3/M input tokens and $15/M output tokens. Available on AWS Bedrock and Vertex AI
- **Artifacts**: Product feature that separates Claude's content from chat dialogue, enabling collaborative work on essays, SVGs, React websites. Combined with 3.5 Sonnet's vision for screenshot-to-code workflows
- **Projects**: Team collaboration feature that grounds Claude's outputs in organizational knowledge (style guides, code bases, transcripts, past work). Shareable across teammates on the Claude Team plan
- **Tool Use API**: Custom client-side functions that Claude can intelligently leverage, with consistent structured JSON output. Developers give Claude hundreds of tools at a time
- **Developer Console**: Prompt generator (Claude writes optimized prompts from task descriptions), variable support (editable prompt templates), Evaluate feature (beta)
- **Interpretability research**: "Scaling Monosemanticity" paper — finding features that activate for different topics within models, then clamping feature values to steer outputs. Demonstrated via Golden Gate Claude. Steering API in beta testing
- Debuted computer use capability around late 2024, enabling AI to autonomously operate complex desktop applications including IDEs
- Computer use has significantly improved since its debut — "getting really really good now"
- Evangelized the technique of dumping memories directly into the file system and having the agent decide when to retrieve them
- Claude Sonnet 4.5 demonstrated running focused tasks for more than 30 hours in a row
- Their Claude model can be prompted to explicitly avoid producing slop, with significant quality improvements
- One of the frontier model providers whose capabilities form the first pillar of autonomy in Replit's framework
- CPO Mike Krieger publicly stated at Lenny's conference that Anthropic's models hallucinate and that writing evals is essential — cited by Aman Khan as evidence that even model creators acknowledge the reliability problem
- Platinum sponsor of the 2025 AI Engineering Code Summit in New York
- Claude 3.7 Sonnet was the frontier model at the time of METR's time horizon paper; Claude 3.6/3.7 Sonnet was used via Cursor Pro in the developer productivity RCT
- Claude 3 Opus had a time horizon of ~4 minutes in METR's measurements
- Built the Claude Agent SDK on top of Claude Code after observing users organically using Claude Code for non-coding tasks
- Published research on reward hacking relevant to agent alignment and the Swiss cheese defense model
- In the 2024 AI Engineer Summit keynote, Sonnet 3.5 was explicitly called out as a competitive alternative to GPT-4, with the advice to "quickly drop models when there's a clearly better competitor." The keynote referenced Sonnet as an example of treating models like interchangeable SaaS products rather than moats.
- Uses Claude Code internally for GitHub and Slack automations (issue triaging, code review)
- Claude.ai is increasingly adopting file-system-built patterns (skills, memory tool, doc creation via code generation)
- Anthropic's philosophy for Claude Code: "give it tools and get out of the way" — simple architecture over complex DAGs
- Their models are described as "very optimized tool calling models" specifically trained for autonomous agent operation
- Claude Code's architecture embodies the "AGI pill" philosophy: don't over-engineer around model flaws today because models will get better
- The Claude Code system prompt can be found on users' machines (not hidden on servers)
- Claude Code releases new features every few days
- Created the MCP (Model Context Protocol) as an open standard, with an official registry containing thousands of servers
- Karan Sampath, Forward Deployed Engineer, advocates for MCP Gateways as the solution to enterprise MCP adoption challenges (observability, access control, security)
- Anthropic's vision: separate the agent harness from the data layer, with the MCP Gateway as the invariant layer
- MCP reached 110 million monthly downloads, growing faster than React did — used by OpenAI's Agent SDK, Google's ADK, LangChain, and thousands of frameworks
- MCP roadmap includes: stateless transport protocol (from Google), improved async tasks for agent-to-agent communication, TypeScript SDK v2 and Python SDK v2, cross-app access, server discovery via well-known URLs, skills over MCP, and MCP applications
- David Soria Parra, MCP engineer, advocates for a connectivity stack approach: skills + MCP + CLI/computer use, used together seamlessly
- Emphasizes progressive discovery and programmatic tool calling as essential client-side patterns for MCP
- Acknowledged FastMCP as better than the official Python SDK, which he originally authored
- **Agent product harness separation**: As of April 2026, Anthropic's new agent product separates where the harness runs from where generated code runs — a key architectural decision that Malte Ubl (CTO Vercel) praised as correcting the "fundamentally wrong architecture" of most current agent harnesses

## Related
- [[summary-20240805 - What's new from Anthropic and what's next： Alex Albert]] — source
- [[Alex Albert]] — Anthropic presenter
- [[Claude 3.5 Sonnet]] — model released August 2024
- [[Artifacts]] — content collaboration feature
- [[ModelSteering]] — interpretability-based output control
- [[TechnologyAdoptionAnalogies]] — electricity analogy used by Anthropic
- [[AmazonBedrock]] — Claude 3.5 Sonnet platform
- [[Vertex AI]] — Claude 3.5 Sonnet platform
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — source
- [[summary-20251222 - No More Slop – swyx]] — source
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
- [[summary-20260105 - Welcome to AIE CODE - Jed Borovik, Google DeepMind]] — source
- [[summary-20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR]] — source
- [[Computer Use]] — capability debuted by Anthropic
- [[Context Management]] — technique Anthropic evangelized
- [[Three Pillars of Autonomy]] — framework
- [[Slop]] — their models can be prompted to avoid producing it
- [[TimeHorizon]] — metric measured on Claude models
- [[RandomizedControlledTrial]] — study using Claude via Cursor
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[ClaudeAgentSDK]] — agent framework built by Anthropic
- [[SwissCheeseDefense]] — security model
- [[BashTool]] — core agent primitive
- [[SimpleDesignPhilosophy]] — philosophy behind Claude Code
- [[MasterWhileLoop]] — core architecture of Claude Code
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[summary-20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint]] — source
- [[ReadOnlyAI]] — design philosophy using Claude for read-only personal AI
- [[Fulan]] — read-only AI system built on Claude
- [[LethalTriquetra]] — security model discussed in context of Claude-based systems
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[Sonnet]] — Anthropic model family used as a backend for Amazon Kiro
- [[AmazonKiro]] — IDE that uses Sonnet as a backend LLM
- [[MCP]] — protocol created by Anthropic
- [[MCPGateway]] — enterprise architecture advocated by Anthropic
- [[KaranSampath]] — Forward Deployed Engineer at Anthropic
- [[summary-20260427 - Gateways are All You Need — Karan Sampath, Anthropic]] — source
- [[WorkOS]] — authentication provider for Anthropic's Claude Code
- [[CrossAppAccess]] — XAA implementation for MCP authentication
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]] — source
- [[summary-20240724 - From Software Developer to AI Engineer： Antje Barth]] — source (Claude 3 Haiku and Claude 3.5 Sonnet on Bedrock)
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source (Sonnet as competitive alternative, model-as-moat discussion)
- [[ModelIsNotTheMoat]] — concept Anthropic's mention supports
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source (MCP roadmap and future)
- [[DavidSoriaParra]] — MCP engineer at Anthropic
- [[MCPApplications]] — experimental MCP feature
- [[ProgressiveDiscovery]] — client-side MCP pattern advocated by Anthropic
- [[ProgrammaticToolCalling]] — client-side MCP pattern advocated by Anthropic
- [[ConnectivityStack]] — skills + MCP + CLI/computer use framework
- [[SkillsOverMCP]] — upcoming MCP extension
- [[StatelessTransportProtocol]] — Google's MCP transport proposal
- [[AgentToAgentCommunication]] — MCP async task primitive
- [[ServerDiscovery]] — upcoming MCP specification
- [[summary-20260420 - The New Application Layer - Malte Ubl, CTO Vercel]] — source (harness separation in new agent product)
- [[AgentHarnessSeparation]] — architectural principle in their new agent product
- **Mario Zechner's perspective**: Mario loved the Claude team ("brilliant people, talented, super high velocity") but criticized Claude Code's context control, system prompt instability, and lack of observability. He built Pi as an alternative. Mario called Amp and FactoryDroid the "Porsche and Lamborghini" of agent harnesses — excellent but not free.
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source
- [[MarioZechner]] — creator of Pi
- [[Pi (coding agent)]] — alternative to Claude Code
- [[ContextOwnership]] — Mario's core critique
- **Tuomas Artman's critique**: Tuomas noted that Anthropic's claim of Claude Code being built by Claude is visible in the product — small bugs appear within seconds, it's slow, and behaves unexpectedly. He attributes this to Anthropic being in a winner-takes-all competition with OpenAI, forcing them to ship features at the expense of quality. "The side effect of that is that the quality just isn't there."
- [[summary-20260421 - Taste & Craft： A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer]] — source (critique)
- [[TuomasArtman]] — critic who noted quality issues
