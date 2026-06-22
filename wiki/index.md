# Wiki Index

This is the global directory of all wiki pages. Every new page must be registered here under its category, with a one-sentence description.

Format: `[[Page Name]] — One-sentence description.`

---

## Sources

*(Summaries of `raw/` files — kebab-case filenames)*

- [[summary-introducing-archon-ai-agent-builder]] — Cole Medin's official intro to Archon, an open-source meta-agent that builds other AI agents.
- [[summary-build-an-army-of-ai-agents-archon]] — Demo of an "MCP Agent Army": primary agent + 6 specialized sub-agents each owning one MCP server.
- [[summary-10x-your-ai-agents-parallel-architecture]] — Deep dive on the parallel agent architecture; Travel Planner demo with PydanticAI + LangGraph.
- [[summary-coding-subagents-mcp-evolution]] — Argument that the next evolution of AI IDEs is generalists delegating to specialized sub-agents over MCP.
- [[summary-build-your-own-mcp-servers-template]] — Cole's open-source MCP server template using FastMCP, demonstrated with a Mem0 long-term-memory server.
- [[summary-easiest-strategy-for-accurate-rag]] — Walkthrough of Anthropic's Contextual Retrieval pattern in N8N and Python.
- [[summary-3-must-have-mcp-servers-for-ai-coding]] — Cole's recommended MCP triad: documentation RAG, database management, web search.
- [[summary-how-to-learn-ai-agents-roadmap]] — 10-phase roadmap for learning to build AI agents from scratch.
- [[summary-context-engineering-is-new-vibe-coding]] — Cole introduces Context Engineering as the successor to Vibe Coding; demos Rasmus's PRP framework in Claude Code.
- [[summary-context-engineering-101]] — Deep dive on the PRP framework with Rasmus as guest; ships an MCP-server use-case template.
- [[summary-context-engineering-blueprint-for-ai-agents]] — Cole ships a PydanticAI-specific PRP template; builds a Research + Email-Draft agent end-to-end.
- [[summary-every-rag-strategy-explained]] — 13-minute survey of 11 RAG strategies; recommends reranking + agentic RAG + context-aware chunking.
- [[summary-agent-harnesses-and-vibe-coding]] — Agent harnesses as the next evolution after context engineering; the two unsolved problems (context rot, compounding errors).
- [[summary-5-techniques-top-agentic-engineers]] — PRD-first dev, modular rules, commandification, context reset, system evolution.
- [[summary-second-brain-with-claude-code-obsidian-skills]] — Claude Code + Obsidian + Skills as a personal knowledge/ideation/research engine.
- [[summary-adversarial-dev-technique]] — GAN-inspired generator/evaluator harness that solves agent sycophancy; built a RAG app one-shot with Sonnet + harness.
- [[summary-full-guide-ai-second-brain]] — Comprehensive second-brain build: memory layer, skills, heartbeat; the lethal-trifecta security argument.
- [[summary-self-evolving-memory-karpathy-llm-wiki]] — Karpathy's LLM-Wiki pattern explained (compiler analogy); Cole's self-evolving internal-memory variant. THE source for this vault's architecture.
- [[summary-harness-engineering]] — Harness engineering defined: the AI layer (6 components) + multi-session orchestration (Ralph loop).
- [[summary-building-effective-agents]] — (external article) Anthropic's canonical taxonomy of agent architectures; cited across the corpus.
- [[summary-ai-exploded-in-2025]] — Cole's ~50-item chronological recap of the 2025 AI industry; the timeline behind the corpus.
- [[summary-kiro-hackathon]] — Announcement of the Dynamous × Kiro AI coding hackathon (Jan 2026); introduces Kiro and its workflow primitives.
- [[summary-ralph-wiggum-vibe-coding]] — Ralph Wiggum (the Ralph loop) as the ceiling of vibe coding; why a real agent harness is the next step.
- [[summary-build-skills-for-any-agent]] — Reimplementing Claude Skills / progressive disclosure in any framework (PydanticAI), plus evals and observability.
- [[summary-full-engineering-team-subagents]] — Extending Anthropic's harness into a full AI engineer with Linear/GitHub/Slack sub-agents via Arcade + the Claude Agent SDK.
- [[summary-safer-openclaw-alternative]] — OpenClaw's magic and its security failures; cloning its components into a controlled second brain with Claude Code.
- [[summary-agent-teams-live-build]] — Live brownfield payment build using Claude Code Agent Teams; planning by clarifying questions + autonomous e2e validation.
- [[summary-is-rag-dead-for-coding]] — Why traditional RAG is dead for code (agentic search) but alive for unstructured data; the structured-vs-unstructured distinction.
- [[summary-complete-agentic-coding-workflow]] — Cole's dead-simple greenfield framework: AI layer + PRD phases + PIV loops + four golden rules.
- [[summary-self-healing-e2e-validation]] — The /e2e-test skill: a six-step self-healing validation workflow that drives a browser and DB to test user journeys autonomously.
- [[summary-beautiful-diagrams-claude-code]] — An Excalidraw diagram skill that teaches the agent to "argue visually" and self-validates by rendering and viewing the image.
- [[summary-is-software-engineering-dead]] — Why SWE isn't dying: slow enterprise adoption + the prompt→context→intent-engineering evolution of the role.
- [[summary-2000-hours-claude-code-wisk]] — The WISK framework (Write/Isolate/Select/Compress) for context management, from 2,000+ hours in Claude Code.
- [[summary-subagent-era]] — The "sub-agent era": cheap fast models (GPT-5.4 Mini/Nano) built for sub-agents; research-only delegation at scale.
- [[summary-sdk-vs-framework-agents]] — When to build agents on a coding-agent SDK vs a framework; the RAG-evolved-to-agentic-RAG clarification.
- [[summary-parallel-claude-code-worktrees]] — A five-pillar playbook for parallel agentic development with git worktrees (ports, deps, Neon DB branching).
- [[summary-principled-agentic-engineer]] — One-hour workshop consolidating the full system: ideate → PIV loop → system evolution; PRD→stories→Jira; inner/outer loops.
- [[summary-ai-youtube-claude-hype]] — Channel-update: depth over Claude-hype, a live-stream shift, and the Dark Factory autonomy experiment.
- [[summary-ai-generated-videos-claude-code]] — End-to-end AI video generation with Claude Code + HyperFrames + ElevenLabs, orchestrated by Archon.
- [[summary-large-codebases-claude-code]] — Anthropic's playbook for Claude Code in large codebases: layered rules, self-improving hooks, LSP, scoped skills.
- [[summary-claude-plans-gemini-designs]] — A cross-provider workflow: Gemini designs the UI, Opus plans/integrates; session-per-step with handoff docs.
- [[summary-loop-engineering]] — A skeptical, practical take on "loop engineering" (/loop, /goal, /routines); fold it into harness engineering with durability + HITL.
- [[summary-build-your-own-crm]] — Brian Casel builds a complete CRM from scratch with Claude Code, demonstrating spec-driven development end to end.
- [[summary-claude-fable-build-app]] — Brian Casel stress-tests Anthropic's Claude Fable model on a real business tool expansion; model selection as a new skill.
- [[summary-hermes-vs-claude-cowork]] — Brian Casel argues for platform-agnostic patterns over committing to any single agent platform; runs Hermes + Claude Co-work simultaneously.
- [[summary-apps-built-with-ai-look-off]] — Brian Casel diagnoses "design drift" in AI-built apps and presents his free Design System skill as the fix.
- [[summary-dont-need-to-learn-code]] — Brian Casel argues the real skill is becoming a product architect, not coding; demonstrates full PRD planning process.
- [[summary-night-shift-agents]] — Brian Casel's three-part Night Shift pattern for delegating recurring business tasks to AI agents.
- [[summary-multitasking-agents-2026]] — Brian Casel's evolution to agent orchestration in 2026: multitasking across features, mobile management, content pipeline.
- [[summary-where-claude-design-fits]] — Brian Casel evaluates Claude Design: not for production, but useful for marketing assets and visual ideation.
- [[summary-we-build-fast-but-does-it-work]] — Brian Casel demonstrates Kain AI for end-to-end QA testing by clicking through an app like a real user.
- [[summary-4-agent-skills-marketing]] — Brian Casel's four agent skills for marketing: radar scan, brand visuals, newsletter writer, newsletter builder.
- [[summary-skill-ai-cant-replace]] — Brian Casel argues "restraint" is the skill AI can't replace; provides pre-planning framework.
- [[summary-claude-code-mobile-guide]] — Complete guide to using Claude Code from mobile: remote control, cloud sessions, new projects, power user setup.
- [[summary-claude-code-changed-recently]] — Three under-the-radar Claude Code features: Auto Plan, Auto Memory, and Voice Mode.
- [[summary-openclaw-vs-claude-agent-team]] — Brian Casel compares OpenClaw vs Claude for running autonomous agent teams; bets on portable skills.
- [[summary-create-jobs-openclaw-agents]] — Brian Casel's framework for creating real jobs (not tasks) for OpenClaw agents; three systems needed.
- [[summary-multi-agent-team-openclaw]] — Brian Casel's complete OpenClaw multi-agent setup: Mac mini, 4 agents, Slack bots, OpenRouter, custom dashboard.
- [[summary-claude-code-slack-teams-ship]] — Three ideas from Anthropic for extending Claude Code into Slack: prototypes, Q&A, analytics.
- [[summary-build-marketing-tools-claude-code]] — Colleen Schnettler built her own voice-to-LinkedIn tool in 2 days; Compound Engineering workflow.
- [[summary-brennan-dunn-ai-developers]] — Brennan Dunn's sub-agent team with Linear integration and Fern Desk auto-documentation.
- [[summary-agent-os-v3]] — Brian Casel releases Agent OS v3, stripped 70%, focusing on standards discovery and spec shaping.
- [[summary-arvid-kahl-saas-claude]] — Arvid Kahl's Podscan is 98% Claude-coded; comprehension debt and super delayed TDD.
- [[summary-claude-code-all-you-need-2026]] — Brian Casel argues vanilla Claude Code handles 90% of work in 2026; frameworks are overkill.
- [[summary-replacing-n8n-with-claude-skill]] — Brian scrapped a week-long N8N workflow and rebuilt it as a Claude Code skill in 30 minutes.
- [[summary-design-os]] — Brian Casel releases Design OS: guided design process filling the gap between idea and codebase.
- [[summary-cursor-visual-editor]] — Brian evaluates Cursor's visual editor: a refinement tool, not a creation tool.
- [[summary-google-antigravity-review]] — Brian tries Google Antigravity: good ideas, dysfunctional execution.
- [[summary-opus-vs-gemini-app-build]] — Brian builds the same app with Opus 4.5 and Gemini 3; frontier models are converging.
- [[summary-ai-skeptic-to-unfair-advantage]] — Five skills giving experienced builders an unfair advantage in the AI era.

## Entities

*(People, companies, tools, products — TitleCase filenames)*

- [[Archon]] — Open-source AI agent that builds other AI agents using PydanticAI and LangGraph.
- [[ColeMedin]] — AI engineer and YouTube creator; built Archon, Crawl4AIRAG, the LocalAIPackage; advocate for PydanticAI + LangGraph + N8N-first prototyping.
- [[Crawl4AIRAG]] — Cole's open-source MCP server that crawls websites and serves contextual-retrieval-enhanced RAG to AI IDEs.
- [[Mem0]] — Long-term memory library for AI agents; featured in Cole's MCP server template.
- [[N8N]] — Open-source visual workflow automation platform; Cole's preferred prototyping tool for AI agents and RAG pipelines.
- [[PydanticAI]] — Python framework for building AI agents with type-safe LLM interactions, MCP support, and structured outputs.
- [[LangGraph]] — Python framework for orchestrating multi-step agentic workflows as state-machine graphs.
- [[LangChain]] — Popular high-level LLM framework that Cole considers "abstraction distraction" and avoids in favor of LangGraph + PydanticAI.
- [[ModelContextProtocol]] — Anthropic's protocol for standardizing how LLMs discover and call external tools; powers MCP server ecosystem.
- [[Anthropic]] — AI lab behind Claude, MCP, and the Contextual Retrieval and Building Effective Agents articles Cole frequently cites.
- [[AndrejKarpathy]] — AI researcher who coined "vibe coding" and articulated the canonical definition of "context engineering"; foundational LLM-Wiki pattern is his.
- [[ClaudeCode]] — Anthropic's terminal-based AI coding agent; Cole's primary AI coding driver from mid-2025 and the canonical execution surface for the PRP framework.
- [[ClaudeSkills]] — Anthropic's capability-packaging primitive; folder + SKILL.md + progressive disclosure. The scaling layer of Cole's Second Brain.
- [[Obsidian]] — Local markdown-based knowledge management app; the canvas for Cole's Second Brain and the app this wiki lives in.
- [[Codex]] — OpenAI's terminal-based coding agent; the primary alternative/counterpart to Claude Code in Cole's 2026 content.
- [[Kiro]] — AWS's feature-rich agentic AI coding assistant (CLI + IDE); a Claude Code counterpart with steering-docs/commands/devlog workflow.
- [[Arcade]] — Platform exposing Linear/GitHub/Slack to agents through one MCP gateway with agent authorization (guided OAuth).
- [[ClaudeAgentSDK]] — Anthropic's SDK for building agentic systems/harnesses on Claude in code; powers Claude Code and Cole's harness experiments.
- [[VercelAgentBrowser]] — Vercel's browser-automation CLI; lets a coding agent run end-to-end tests through a real browser like a user.
- [[Excalidraw]] — Free open-source JSON-based diagramming tool (excalidraw.com / Obsidian plugin); target of Cole's diagram-generation skill.
- [[HyperFrames]] — AI video-rendering tool (HTML-based scenes + preview) driven by Claude Code; the engine in Cole's video-generation pipeline.
- [[Pi]] — Provider-flexible coding-agent harness (CLI); runs Gemini and other models via OpenRouter; skills-compatible.
- [[Antigravity]] — Google's Gemini-powered agentic IDE; exceptional at one-shot front-end/UI generation.
- [[Retool]] — Low-code platform to deploy/govern internal dashboards (e.g. loop-control dashboards) with permissions and audit trails.
- [[OpenClaw]] — Out-of-the-box open-source second-brain agent; Cole takes inspiration from it but argues against running it directly (lethal trifecta).
- [[Neon]] — Serverless Postgres with pgvector; Cole's go-to Postgres for RAG, interchangeable with Supabase.
- [[Zapier]] — Workflow-automation platform; Cole connects it to his Second Brain via MCP wrapped as a skill.
- [[Rasmus]] — Creator of the PRP Framework (Product Requirements Prompts); collaborator with Cole on use-case templates.
- [[OpenAI]] — Provider of the GPT model family used as default LLMs (GPT-4o, GPT-4o-mini, o3-mini) in most of Cole's demos.
- [[Windsurf]] — AI-powered IDE (Codeium) used as the primary demo target for Archon's MCP integration.
- [[Cursor]] — AI-powered IDE; functionally equivalent to Windsurf as an MCP-aware host for Archon.
- [[Supabase]] — Open-source Postgres-with-pgvector database used as Archon's RAG knowledge backend.
- [[Streamlit]] — Python UI framework Cole defaults to for building chat interfaces over agentic workflows.
- [[BrianCasel]] — Software developer and YouTube creator teaching spec-driven development and AI agent orchestration for building custom business tools.
- [[BuildNew]] — Brian Casel's free open-source Ruby on Rails + React starter application template with design system built in.
- [[PRDCreator]] — Brian Casel's free agent skill that automates PRD planning and milestone breakdown for spec-driven development.
- [[DesignSystem]] — Brian Casel's free agent skill that installs a living design system into the codebase to prevent design drift.
- [[HermesAgent]] — Personal AI agent platform Brian Casel uses for routine recurring background jobs, running on a dedicated Mac mini via Discord.
- [[ClaudeCowork]] — Anthropic's agent platform with scheduled recurring tasks; Brian Casel uses it for high-stakes creative jobs with Claude Opus.
- [[SparkDrop]] — Brian Casel's custom-built content pipeline app where agents submit ideas via API and he reviews via UI.
- [[BrainDown]] — Brian Casel's custom-built markdown editor/viewer integrated with Dropbox for reviewing agent-generated reports.
- [[ResonanceRadar]] — Brian Casel's custom app for curating content ideas from internal and external sources; expanded with Claude Fable.
- [[SuperSet]] — Agentic development tool with native Claude Code CLI integration; Brian Casel's current daily driver for multitasking.
- [[Superconductor]] — Agentic development tool wrapping Claude Code in a GUI; evaluated by Brian Casel alongside SuperSet.
- [[Consensus]] — MCP server searching 200M+ peer-reviewed academic papers with citable sources for AI agents.

## Concepts

*(Frameworks, methodologies, theories — TitleCase filenames)*

- [[AIAgent]] — A large language model given the ability to interact with the outside world via tool use.
- [[AgenticWorkflow]] — Multi-step orchestration of one or more AI agents with explicit control flow and shared state.
- [[SubAgent]] — A specialized agent invoked by a primary agent to handle a narrow part of a larger task; solves the LLM tool-overload problem.
- [[AgentTeams]] — Claude Code feature (Opus 4.6): parallel agents that share a task list and communicate; the contract-first evolution of sub-agents.
- [[ParallelAgentArchitecture]] — Multi-agent pattern where specialized sub-agents execute simultaneously; outputs combined by a synthesizer.
- [[MetaAgent]] — An AI agent whose purpose is to design or generate other AI agents (Cole calls these "agenteers"); Archon is the canonical example.
- [[RetrievalAugmentedGeneration]] — Pattern of grounding LLM responses in retrieved external documents via vector search.
- [[AgenticSearch]] — Tool-driven retrieval (ripgrep/glob/file navigation) coding agents use instead of vector RAG; still RAG, no vector DB.
- [[AgentSDKvsFramework]] — Decision framework: build on a batteries-included coding-agent SDK vs a from-scratch framework.
- [[ParallelAgenticDevelopment]] — Running many coding-agent sessions at once via git worktrees; the five-pillar system for 10x output.
- [[LargeCodebaseStrategies]] — Anthropic's AI-layer playbook for large codebases: layered CLAUDE.md, self-improving hooks, LSP-via-MCP, scoped skills.
- [[CrossProviderWorkflow]] — Chaining sessions from different model providers (by strength) via handoff docs; e.g. Gemini designs, Opus plans.
- [[LoopEngineering]] — Designing loops (/loop, /goal, /routines) that prompt agents 24/7; Cole folds it into harness engineering.
- [[ContextualRetrieval]] — Anthropic's RAG enhancement: prepend each chunk with LLM-generated context positioning it within its source document.
- [[HumanInTheLoop]] — Workflow pattern where execution pauses for human confirmation, correction, or input before resuming.
- [[ToolUse]] — Mechanism by which an LLM invokes external functionality; the foundation of every AI agent.
- [[AICodingAssistant]] — IDE-integrated AI tools (Cursor, Windsurf, etc.); "generalists" that benefit from delegating to specialist sub-agents.
- [[StructuredOutputs]] — LLM responses constrained to a predefined schema; used for downstream consumption and conditional branching.
- [[CapabilitiesOverTools]] — Cole Medin's heuristic: focus on transferable skills rather than mastering specific frameworks that churn rapidly.
- [[AgentEvaluation]] — Measuring agent behavior correctness (vs. code correctness); Cole's "75% of agent dev time is evaluation" rule.
- [[AgentObservability]] — Production-side capture of every input/output/tool-call/cost/latency for an agent; Cole's "100% necessary for production".
- [[Guardrails]] — Input and output validation layers wrapped around an agent; the reliability primitive that makes agents production-ready.
- [[ContextEngineering]] — The discipline of supplying an AI coding assistant with all the context it needs to plausibly solve a task on the first attempt; mid-2025-onwards successor to Vibe Coding.
- [[IntentEngineering]] — The evolution beyond context engineering: explicit success criteria, self-validation, and alignment on intent (Nate B. Jones).
- [[VibeCoding]] — Letting the AI write code with minimal context and review; coined by Karpathy; great for prototypes, breaks at production.
- [[PRPFramework]] — Rasmus's Product Requirements Prompt methodology; Cole's canonical context-engineering toolkit. Two-pass plan-then-execute with use-case templates.
- [[ValidationGates]] — Explicit lint/test/iterate checks the AI runs before declaring done; the inner correctness loop of the PRP framework.
- [[AgentHarness]] — Infrastructure layer connecting many LLM sessions for long-running tasks; the post-context-engineering evolution.
- [[ContextRot]] — Degradation of LLM reasoning as context fills ("the dumb zone"); the central problem harnesses and context engineering address.
- [[WISKFramework]] — Write/Isolate/Select/Compress: Cole's battle-tested context-management framework for Claude Code.
- [[AgenticEngineering]] — The practitioner discipline of getting production results from AI coding agents; umbrella over the 5 techniques.
- [[PIVLoop]] — Plan-Implement-Validate: the per-phase unit of work in Cole's greenfield coding workflow.
- [[PRDFirstDevelopment]] — Writing a project-scope north-star markdown doc before any feature work. (Technique 1)
- [[ModularRulesArchitecture]] — Short global rules + conditionally-loaded reference docs to protect the context window. (Technique 2)
- [[Commandification]] — Packaging any twice-used workflow as a reusable slash command. (Technique 3)
- [[ContextReset]] — Clearing context between planning and execution to keep the executor's working memory lean. (Technique 4)
- [[SystemEvolution]] — "Fix the system that allowed the bug, not just the bug." The compounding technique. (Technique 5)
- [[SecondBrain]] — Personal knowledge/ideation/research engine: Claude Code + Obsidian + Skills. Directly ancestral to this wiki.
- [[ProgressiveDisclosure]] — Load short capability descriptions upfront, full instructions on demand; what makes Skills scale.
- [[KarpathyLLMWiki]] — Karpathy's compile-don't-retrieve knowledge-base pattern; the foundation this entire vault is built on.
- [[HarnessEngineering]] — Building the wrapper around the model; the 2026 evolution of context engineering. Skill (AI layer) + mindset (system evolution).
- [[AILayer]] — The six-component wrapper you build on top of a coding agent: rules, skills, MCP, code-search, hooks, sub-agents.
- [[AdversarialDev]] — GAN-inspired generator/evaluator harness; a separate critic agent solves self-review sycophancy.
- [[Sycophancy]] — LLMs' bias toward agreeing with the user and their own work; worst when an agent reviews its own code.
- [[RalphLoop]] — Simple automation stringing many coding-agent sessions together for large scopes (Jeffrey Huntley).
- [[LethalTrifecta]] — Security model: private data + untrusted content + exfiltration vector = high prompt-injection risk.
- [[PromptCaching]] — Provider feature that cheapens repeated prompt prefixes; what makes Contextual Retrieval economical.
- [[HybridSearch]] — RAG strategy combining semantic (vector) + keyword (BM25) search for better recall.
- [[Reranking]] — Two-step RAG: retrieve many candidates, then a reranker model returns the most relevant few.
- [[BuildInPublic]] — Cole's philosophy of open-source-from-day-one, iterate-visibly development.
- [[SpecDrivenDevelopment]] — Methodology of shaping clear written plans (PRDs) before coding, then directing AI to build in structured milestones; contrasts with vibe coding.
- [[MilestoneBasedBuilding]] — Breaking software projects into self-contained, sequentially-dependent chunks that AI agents build one at a time.
- [[ProductArchitect]] — The emerging builder role: shaping specs and directing AI agents rather than writing code.
- [[NightShiftModel]] — Three-part pattern (shared interface + human review + agent on schedule) for delegating recurring business tasks to AI agents.
- [[AgentPlatformPortability]] — Strategy of betting on portable patterns (skills, schedules) rather than committing to a single agent platform.
- [[AgentMultitasking]] — 2026 workflow of running multiple AI coding agents on different features simultaneously via git worktrees.
- [[InternalTools]] — Custom-built software for a single business's specific workflow, now accessible to non-developers via AI.
- [[StarterKit]] — Distributable package of prompts, plans, PRDs, and video guides to rebuild Brian Casel's internal tools.
- [[DesignDrift]] — Gradual UI inconsistency in AI-built apps when each session reinvents design from scratch; solved by a living design system.
- [[VerificationCriteria]] — Checklist pattern defining what must be true for a milestone to be complete; AI agents use it to self-check work.
- [[IntakeProcessing]] — Automated system capturing all published content and daily work into a structured file system for AI agents to draw from.
- [[ContentIdeation]] — Agent-driven process of researching, generating, and pitching new content ideas based on captured work and audience data.
- [[AgentSkills]] — Reusable markdown files with step-by-step instructions that AI agents follow; the portable unit of agent automation.
- [[Restraint]] — Product strategy discipline of choosing focus over capability; saying no to features AI makes trivially easy to build.
- [[VisualIdeation]] — Using visual mockups during the shaping phase before locking decisions into a spec or PRD.
- [[MobileAgentWorkflow]] — Starting, monitoring, and continuing AI coding agent sessions from a mobile device.
- [[AutoPlan]] — Claude Code feature that automatically enters plan mode for substantial prompts.
- [[AutoMemory]] — Claude Code feature where Claude maintains its own memory, learning from corrections over time.
- [[VoiceMode]] — Claude Code's built-in voice dictation; speaking prompts produces higher detail than typing.
- [[ServerMode]] — Claude Code remote configuration allowing mobile-initiated sessions with full local file/skill access.
- [[BrandVisuals]] — Brian Casel's agent skill for generating consistent on-brand illustrations via Claude + Google ImageGen.
- [[EndToEndTesting]] — Final QA layer verifying real users can complete critical flows; catches what unit tests miss.
- [[ComprehensionDebt]] — Gap between developer's mental model and actual code when AI writes the vast majority; coined by Arvid Kahl.
- [[AgentJobs]] — Defining recurring roles (not one-off tasks) for AI agents, modeled after human hiring practices.
- [[BuilderStories]] — Brian Casel's video series where builders share screens and demonstrate their AI-first workflows.
- [[SlackIntegration]] — Extending Claude Code intelligence beyond terminals into Slack for the whole organization.
- [[ModelConvergence]] — Frontier AI models becoming similarly capable; builder skill matters more than model choice.

## Syntheses

*(Cross-document analyses and deep dives — kebab-case filenames)*

- [[evolution-vibe-coding-to-harness-engineering]] — The paradigm timeline: vibe coding → context engineering → harness engineering, and how vibe coding returns (qualified).
- [[cole-medin-rag-playbook]] — Consolidated RAG strategies, tooling, cost controls, and Cole's actual recommendations; plus the RAG-vs-Wiki tension.
- [[vault-architecture-mapped-to-cole-teachings]] — How this vault is itself an instance of the Karpathy LLM Wiki / Second Brain pattern it documents.
- [[fighting-context-rot]] — Every technique Cole uses against context rot, organized by layer; the unifying thread of the corpus.

- [[summary-claude-code-vs-cursor-vs-codex]] — Brian Casel compares Claude Code, Cursor, and Codex for cloud-based agent workflows.
- [[summary-cursor-2-changed-work]] — Brian reviews Cursor 2.0: built-in browser, background agents, mobile access, agent sidebar.
- [[summary-claude-code-skills-problem]] — Brian explains what problem Claude Code Skills solve: progressive disclosure and context pollution.
- [[summary-agent-os-v2]] — Brian releases Agent OS v2, expanding spec-driven development to work with any AI tool.
- [[summary-claude-code-2-features]] — Three Claude Code 2.0 features Brian uses daily: plan mode, skills, sub-agents.
- [[summary-codex-cli-worth-switch]] — Brian evaluates whether OpenAI's Codex CLI is worth switching to from Claude Code.
- [[summary-spec-driven-real-world]] — Brian demonstrates spec-driven development applied to a real-world project.
- [[summary-day-one-claude-code]] — Brian's getting-started guide for Claude Code: installation, plan mode, first build.
- [[summary-agent-os-v1]] — Brian introduces Agent OS v1, the original spec-driven development framework.
- [[summary-finding-flow-ai-agents]] — Brian discusses achieving flow state while working with AI coding agents.
- [[summary-claude-code-memory-problem]] — Brian addresses Claude Code's context limitations and presents milestone-based solutions.
- [[summary-missing-system-coding-agents]] — Brian identifies the need for documented coding standards; groundwork for Agent OS.
- [[summary-cursor-keyboard-shortcuts]] — Brian's essential Cursor keyboard shortcuts for staying fast without the mouse.
- [[summary-claude-code-multitasking]] — Brian demonstrates multitasking with Claude Code using git worktrees.
- [[summary-case-for-claude-code]] — Brian makes the case for adopting Claude Code as a primary development tool.
- [[summary-crush-backlog-background-agents]] — Brian uses Cursor's background agents to work through a development backlog.
- [[summary-vibe-coding-goes-pro]] — Brian explains transitioning from vibe coding to professional building with specs.
- [[summary-openai-claude-rails-integrations]] — Brian demonstrates integrating OpenAI and Claude APIs into Rails applications.
- [[summary-adding-search-rails]] — Brian demonstrates adding search functionality to Rails applications.
- [[summary-saas-billing-rails-stripe]] — Brian builds a complete SaaS billing system with Rails and Stripe.
- [[summary-build-rails-apps-fast]] — Brian shares his methodology for rapidly building Rails apps with AI assistance.
- [[summary-ai-isnt-my-replacement]] — Brian argues AI amplifies developers rather than replacing them.
- [[summary-hard-thing-hard-decisions]] — Brian discusses the difficulty of product decisions when everything is buildable.
- [[summary-build-products-scratch-itch]] — Brian's philosophy of building products that solve his own problems first.
- [[summary-linear-manage-saas]] — Brian demonstrates using Linear for project management in SaaS development.
- [[summary-build-rails-components]] — Brian demonstrates faster Rails development using reusable components.
- [[summary-vibe-coding-vs-coding-cursor]] — Brian contrasts vibe coding with professional coding in Cursor.
