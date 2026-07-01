---
title: "ClaudeCode"
type: entity
tags: [tool, coding-agent, anthropic, claude]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Taste & Craft： A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - The End of Apps — Kitze, Sizzy.co.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - Agents Don't Do Standups： Building the Post-Engineer Engineering Org — Mike Spitz, PFF.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer.md"]
last_updated: 2026-06-29
---

## Definition
Claude Code is Anthropic's coding agent that uses Claude models to autonomously write, edit, and manage code. It uses a system prompt and a Claude.md file for user-customizable rules.

## Key Information
- In prompt learning experiments, vanilla Claude Code (with no rules added) resolved approximately 40% of SWE-bench GitHub issues.
- After prompt learning with 150 training examples, Claude Code improved to approximately 45% — a 5 percentage point gain purely from system prompt iteration.
- Claude 4.1 achieved performance near Claude 4.5 (considered state-of-the-art for coding) at two-thirds the cost after prompt optimization.
- Uses a Claude.md file where users can append repository-specific rules, analogous to Cline's rules file.
- Its system prompt has been publicly leaked and discussed, revealing its length and complexity compared to other coding agents.
- Mentioned alongside Cursor as a successful example of coding agents with good planning capabilities.
- Foundation of the Claude Agent SDK — users organically started using Claude Code for non-coding tasks, revealing the bash tool and file system as universal agent primitives.
- The bash tool is what makes Claude Code so effective: instead of custom search/lint/execute tools, it uses grep, npm, and the existing software ecosystem.
- Described as "the first true agent" — the first time AI was seen working autonomously for 10, 20, or 30 minutes.
- Includes sub-agents with best-in-class bash support, handling race conditions and process isolation.
- Has a plugin marketplace (accessible via /plugins) for skill discovery.
- Includes a to-do tool, compacting, hooks, and memory features.
- **Semantic Code Search**: Uses agentic (grep-based) search by default, not semantic search. Early versions experimented with a local vector DB but abandoned it in favor of simpler grep-based search. Kuba Rogut benchmarked adding semantic search (via TurboGrep + Turbopuffer) to Claude Code, finding it improved file precision from 65% to 87% on ContextBench. However, Claude Code is built for grepping and does not have a true understanding of when to call semantic search, limiting its gains compared to Cursor's built-in approach (24% improvement).
- Architecture: a simple master while-loop (internally called "N0") — while tool calls exist, run the tool, feed results to model, repeat
- Core tools: Read (with token limits), Grep/Glob (instead of RAG), Edit (using unified diffs), Bash (the most important tool), Web Search/Fetch, Todos, Tasks (sub-agents)
- System prompt nudges: concise outputs, use tools over text explanations, match existing code, run commands in parallel, use todo lists
- Context management: H2A async buffer decouples I/O from reasoning; compaction drops middle and summarizes head/tail at ~92% capacity
- Uses trigger phrases for reasoning budgets: think, think hard, think harder, ultra think
- Features Skills: extendable system prompts loaded on demand for specialized tasks
- Sandboxing: pipeline gates bash commands by prefix; containerization for web fetch to prevent prompt injection
- Jared Zoneraich rebuilt his engineering org around Claude Code with the rule: if it takes under an hour, use Claude Code
- Zoneraich personally uses Claude Code for human-like actions (git, local environment, back-and-forth tasks)
- Peter Steinberger used Claude Code for OpenClaw's WhatsApp relay — noticed its default personality "didn't really fit how people would write to you on WhatsApp," which inspired the soul.md concept and agent personality work
- **Demand-Driven Context Demo**: Raj used Claude Code for the Demand-Driven Context workshop demo, implementing the approach with a combination of skills, rules, agents, hooks, and a file-system knowledge base. Claude Code's 1M token context window easily accommodates per-domain knowledge bases (~96K tokens).
- **Viking Phone Reverse Engineering**: Boris Starkov (Eleven Labs) used Claude Code to reverse engineer a legacy Viking VOIP phone protocol. Claude Code autonomously discovered the phone on the network via nmap, brute-forced 676 two-letter command combinations to find 80 valid commands, set up a TCP proxy for man-in-the-middle analysis between a Windows VM and the phone, reverse engineered a single-byte checksum algorithm, and discovered the persistence command sequence. Starkov describes his role as "the agent for Claude" — Claude orchestrated the entire process while he performed physical actions (rebooting, listening for beeps). The reverse-engineered protocol was open-sourced as a reusable Claude Code skill. Token cost: $10-$100. The task had previously defeated three senior engineers plus ChatGPT a year earlier.

## Related
- [[Cline]] — another coding agent benchmarked alongside Claude Code
- [[Cursor]] — another successful coding agent
- [[SWEBench]] — benchmark used to evaluate Claude Code
- [[PromptLearning]] — technique used to improve Claude Code's performance
- [[RuleBasedPrompting]] — the approach that yielded improvements
- [[summary-20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize]] — source
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[ClaudeAgentSDK]] — agent framework built on Claude Code
- [[BashTool]] — what makes Claude Code effective
- [[SubAgents]] — key feature
- [[Hooks]] — verification mechanism
- [[MasterWhileLoop]] — core architectural pattern
- [[BashAsUniversalAdapter]] — key design principle
- [[UnifiedDiffing]] — editing approach
- [[TodoListPattern]] — steerability mechanism
- [[Skills]] — extendable system prompt mechanism
- [[SandboxingAndPermissions]] — security layer
- [[ReasoningBudgets]] — thinking tiers
- **XAA Demo**: Claude Code was demonstrated with XAA (Cross-App Access) compatibility, automatically connecting to the Figma MCP server via Okta SSO without consent screens
- **WorkOS Integration**: Uses WorkOS for authentication, enabling XAA support for enterprise SSO connections

- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]] — source
- [[WorkOS]] — authentication provider
- [[CrossAppAccess]] — XAA implementation
- [[Paperclip]] — agent orchestrator supporting Claude Code as an employee agent
- [[summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa]] — source
- **Mario Zechner's critique**: Claude Code controls the user's context behind their back — system prompts change every release, tools are removed/modified, system reminders inject irrelevant information confusing the model, zero observability, zero model choice (Anthropic-only), shallow hooks that spawn new processes. Mario built Pi as an alternative.
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source (critique)
- [[MarioZechner]] — critic who built Pi as an alternative
- [[Pi (coding agent)]] — alternative built in response to Claude Code's limitations
- [[ContextOwnership]] — the core problem Mario identified
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source (progressive discovery benefits demonstrated in Claude Code)
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — source (WhatsApp relay, personality inspiration)
- [[ProgressiveDiscovery]] — pattern demonstrated with Claude Code's tool context reduction
- [[ToolSearch]] — mechanism used in Claude Code for progressive discovery
- [[PeterSteinberger]] — used Claude Code for WhatsApp relay
- [[AgentPersonality]] — concept inspired by Claude Code's default personality not fitting WhatsApp
- [[OpenClaw]] — project where Claude Code was used as personality baseline
- **Tuomas Artman's critique**: Anthropic claims all Claude Code functionality was coded by Claude, and Tuomas says "it shows" — small bugs appear within seconds of use, it's slow, and behaves unexpectedly. He attributes this to Anthropic being in a winner-takes-all competition with OpenAI, forcing them to ship features at the expense of quality.
- [[summary-20260421 - Taste & Craft： A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer]] — source (critique)
- [[TuomasArtman]] — critic who noted quality issues
- [[AIAndTaste]] — related concept about AI's inability to produce tasteful software
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — source (YOLO mode as high-trust extreme, planning inefficiency)
- [[AgentHuman Collaboration]] — trust spectrum from low-trust (asks every time) to YOLO mode
- [[JacobLauritzen]] — referenced Claude Code's trust spectrum and planning inefficiency
- [[summary-20260423 - The End of Apps — Kitze, Sizzy.co]] — source (Kitze's usage for personal skills, WhatsApp relay, model personality degradation)
- [[summary-20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub]] — source (referenced as "Claude" in the "one man, two dozen Clods" framing of single-player agent interfaces)
- [[Kitze]] — loaded Claude Code with personal skills, used for WhatsApp relay
- [[AgentPersonality]] — "box of oatmeal" model degradation critique
- [[Wolfer]] — Kitze's alternative (avoids Claude Code: "I might get arrested")
- [[SinglePlayerAgentInterfaces]] — critique that Claude Code and similar tools are solo interfaces ignoring team collaboration
- [[summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop]] — source (leaked keywords.ts regex frustration detection)
- [[Raindrop]] — referenced Claude Code's regex approach as example of cheap implicit signals
- [[ImplicitSignals]] — regex-based frustration detection in keywords.ts
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source (used for workshop demo)
- [[DemandDriven Context]] — methodology demonstrated with Claude Code
- [[Raj]] — used Claude Code for the workshop demo
- [[summary-20260515 - Agents Don't Do Standups： Building the Post-Engineer Engineering Org — Mike Spitz, PFF]] — PFF case study: 2 engineers with Claude Code achieved 25x deploys and 10x output
- [[PFF]] — sports data company that used Claude Code in their post-engineer org case study
- [[MikeSpitz]] — engineering leader who presented the PFF Claude Code case study
- **Intercom 2x Adoption**: Intercom chose Claude Code as their unified AI coding platform for the "2x" project, consolidating from Cursor, Augment, and GitHub Copilot. Connected Claude Code to all internal systems with the vision that it should act as a senior engineer on any technical task. Built hundreds of internal plugins and skills. Result: doubled engineering throughput in under a year with PR throughput from Claude Code exceeding 90%.
- [[summary-20260515 - How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom]] — source (Intercom 2x adoption)
- [[Intercom]] — company that consolidated on Claude Code for 2x
- [[BrianScanlan]] — Senior Principal Engineer leading Claude Code adoption
- [[Doubling Engineering Throughput]] — the 2x project using Claude Code
- [[Platform Consolidation for AI Coding]] — strategy exemplified by Intercom
- [[Skills Flywheel]] — Intercom's approach to Claude Code skills
- [[summary-20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs]] — source (Viking phone reverse engineering)
- [[Boris Starkov]] — used Claude Code to reverse engineer Viking phone
- [[Viking Phone]] — legacy VOIP hardware reverse engineered with Claude Code
- [[ElevenLabs]] — company whose engineer used Claude Code for hardware hacking
- [[AIAssisted Hardware Reverse Engineering]] — methodology demonstrated with Claude Code
- [[Protocol Brute Forcing]] — technique Claude Code used to discover commands
- [[ManInTheMiddle Protocol Analysis]] — technique Claude Code set up
- [[Checksum Reverse Engineering]] — technique Claude Code performed
- [[AI as Orchestrator, Human as Hands]] — Starkov's role while Claude Code directed
- [[summary-20260603 - Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer]] — source (semantic code search benchmarking)
- [[SemanticCodeRetrieval]] — semantic search approach benchmarked against Claude Code's grep-based search
- [[TurboGrep]] — CLI tool that adds semantic search to Claude Code
- [[Turbopuffer]] — vector database used in semantic search experiments
- [[ContextBench]] — benchmark used to evaluate Claude Code's code retrieval
- [[Agentic Search]] — the grep-based search Claude Code uses by default
