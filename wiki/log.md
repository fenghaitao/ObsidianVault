# Operation Log

Append-only chronological record of all wiki operations.

Format: `## [YYYY-MM-DD] <action> | <one-line summary>`

Grep-friendly: `grep "^## \[" log.md | tail -10` to see recent operations.

---

## [2026-06-23] query | Cross-cutting syntheses: Cole Medin vs Brian Casel on planning and autonomy
- **Changes**: created [[cole-vs-brian-planning-methodologies]], created [[cole-vs-brian-agent-autonomy]], updated [[index]], updated [[SpecDrivenDevelopment]], updated [[PRDFirstDevelopment]], updated [[PIVLoop]], updated [[MilestoneBasedBuilding]], updated [[HarnessEngineering]], updated [[NightShiftModel]], updated [[AgentMultitasking]]
- **Conflicts**: none

## [2026-06-19] ingest | Cole Medin "Archon - The AI Agent Builder" playlist (4 transcripts, batched)
- **Sources processed**:
  - `raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md`
  - `raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md`
  - `raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md`
  - `raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md`
- **Changes**:
  - Created sources: [[summary-introducing-archon-ai-agent-builder]], [[summary-build-an-army-of-ai-agents-archon]], [[summary-10x-your-ai-agents-parallel-architecture]], [[summary-coding-subagents-mcp-evolution]]
  - Created entities: [[Archon]], [[ColeMedin]], [[PydanticAI]], [[LangGraph]], [[LangChain]], [[ModelContextProtocol]], [[Anthropic]], [[OpenAI]], [[Windsurf]], [[Cursor]], [[Supabase]], [[Streamlit]]
  - Created concepts: [[AIAgent]], [[AgenticWorkflow]], [[SubAgent]], [[ParallelAgentArchitecture]], [[MetaAgent]], [[RetrievalAugmentedGeneration]], [[HumanInTheLoop]], [[ToolUse]], [[AICodingAssistant]], [[StructuredOutputs]]
  - Updated [[index.md]] (registered all 26 new pages)
- **Conflicts**:
  - On [[LangChain]]: noted Cole's tension — criticizes LangChain as "abstraction distraction" while praising [[LangGraph]] (same team). Captured as `## Knowledge Conflicts` section with reconciliation.
  - On [[RetrievalAugmentedGeneration]]: noted philosophical conflict between Karpathy LLM-Wiki anti-RAG stance and Cole's pro-RAG-for-doc-grounding usage. Captured as `## Knowledge Conflicts` section; the two are compatible at different layers.
- **Notes**:
  - Batched ingest of all 4 transcripts since they form a single coherent series about one tool ([[Archon]]). Entities/concepts written once with synthesis from all 4 sources rather than incrementally merged.
  - Skipped sponsor segments (Vectorize, Lutra, FishAudio) and tangential vendor names (Pinecone, Qdrant, Brave, GitHub MCP server, Slack, Airtable, etc.) — captured these only inline within the Archon and ModelContextProtocol pages.
  - Auto-generated YouTube subtitles render "Windsurf" as "Windswept" and "Supabase" as "Superbase". Wiki uses canonical names; transcription quirk noted on the relevant entity pages.

## [2026-06-19] ingest | Cole Medin "Channel Only" — batch 1 of 7 (Apr-May 2025, 4 transcripts)
- **Sources processed**:
  - `raw/03-transcripts/Cole Medin/Channel Only/20250414 - The ULTIMATE Guide to Building Your Own MCP Servers (Free Template).md`
  - `raw/03-transcripts/Cole Medin/Channel Only/20250508 - The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide).md`
  - `raw/03-transcripts/Cole Medin/Channel Only/20250515 - The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them).md`
  - `raw/03-transcripts/Cole Medin/Channel Only/20250526 - How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap).md`
- **Changes**:
  - Created sources: [[summary-build-your-own-mcp-servers-template]], [[summary-easiest-strategy-for-accurate-rag]], [[summary-3-must-have-mcp-servers-for-ai-coding]], [[summary-how-to-learn-ai-agents-roadmap]]
  - Created entities: [[N8N]], [[Mem0]], [[Crawl4AIRAG]]
  - Created concepts: [[ContextualRetrieval]], [[CapabilitiesOverTools]], [[AgentEvaluation]], [[AgentObservability]], [[Guardrails]]
  - Updated entities: [[ModelContextProtocol]] (build-your-own + 3-must-have sections), [[ColeMedin]] (Crawl4AIRAG, Mem0, Dynamis course, expanded philosophy), [[Anthropic]] (Contextual Retrieval article + FastMCP), [[Archon]] (planned Crawl4AIRAG integration)
  - Updated concepts: [[RetrievalAugmentedGeneration]] (added ContextualRetrieval section, updated vector DB list)
  - Updated [[index.md]] (12 new pages registered)
- **Conflicts**: none new
- **Notes**:
  - Batch 1 of 7 planned chronological clusters covering 49 Channel Only transcripts.
  - Following Archon-style batch synthesis — read all 4 sources, write/update pages once with cross-source synthesis rather than incremental per-file ingest.
  - Skipped sponsor segments (Neon — though linked when relevant; DataButton, Aqua Voice, Mem note tool, Perplexity — tangential).
  - Skipped tangential mentions: Brave/GitHub/Slack/Airtable/Pinecone/Qdrant/Weaviate as standalone entities; covered inline within parent pages.
  - Tools mentioned in passing but not given dedicated pages (intentional, low signal-to-noise at this point): Cline, Roo Code, Bolt.new, Lovable, Flowise, Voiceflow, Relevance AI, Agno, CrewAI, OpenAI Agents SDK, Docker, Render, Digital Ocean, Hostinger, AWS, GCP, Vast AI, RunPod, Langfuse, Helicone, Langsmith, Logfire, Context7. May get pages later if they reappear in subsequent batches.

## [2026-06-19] ingest | Cole Medin "Channel Only" — selective batch A: Context Engineering trilogy (3 transcripts)
- **Sources processed**:
  - `raw/03-transcripts/Cole Medin/Channel Only/20250703 - Context Engineering is the New Vibe Coding (Learn this Now).md`
  - `raw/03-transcripts/Cole Medin/Channel Only/20250717 - Context Engineering 101 - The Simple Strategy to 100x AI Coding.md`
  - `raw/03-transcripts/Cole Medin/Channel Only/20250724 - Build ANY AI Agent with this Context Engineering Blueprint.md`
- **Changes**:
  - Created sources: [[summary-context-engineering-is-new-vibe-coding]], [[summary-context-engineering-101]], [[summary-context-engineering-blueprint-for-ai-agents]]
  - Created entities: [[ClaudeCode]], [[AndrejKarpathy]], [[Rasmus]]
  - Created concepts: [[ContextEngineering]], [[VibeCoding]], [[PRPFramework]], [[ValidationGates]]
  - Updated entities: [[ColeMedin]] (mid-2025 shift to Claude Code, Context Engineering frame, Rasmus collaboration)
  - Updated concepts: [[AICodingAssistant]] (added agentic-loop camp + Claude Code era)
  - Updated [[index.md]] (10 new pages registered)
- **Conflicts**: none new
- **Notes**:
  - Selective ingest — picking only Tier 1 + Tier 2 from the curated list (Tier 1 = directly-relevant-to-our-wiki, Tier 2 = concept-defining canonicals). Skipping ~28 transcripts of news commentary, livestreams, model-release reactions, and niche workflow content.
  - Batch A is the Context Engineering trilogy — foundational. Batch B and C will build on these concepts.
  - Skipped sponsor segments (Sneak, Lindy, Scribba) and tangential vendor mentions (Cloudflare Workers, Wrangler, Aider, Cline as standalone — covered inline).
  - "Rasmus" recorded with last name unknown — Cole's videos use first name only. May get refined in later batches.

## [2026-06-20] ingest | Cole Medin "Channel Only" — selective batch B (4 transcripts, Nov 2025 - Jan 2026)
- **Sources processed**:
  - `raw/03-transcripts/Cole Medin/Channel Only/20251103 - Every RAG Strategy Explained in 13 Minutes (No Fluff).md`
  - `raw/03-transcripts/Cole Medin/Channel Only/20251218 - Are Agent Harnesses Bringing Back Vibe Coding.md`
  - `raw/03-transcripts/Cole Medin/Channel Only/20260108 - The 5 Techniques Separating Top Agentic Engineers Right Now.md`
  - `raw/03-transcripts/Cole Medin/Channel Only/20260126 - I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How).md`
- **Changes**:
  - Created sources: [[summary-every-rag-strategy-explained]], [[summary-agent-harnesses-and-vibe-coding]], [[summary-5-techniques-top-agentic-engineers]], [[summary-second-brain-with-claude-code-obsidian-skills]]
  - Created entities: [[ClaudeSkills]], [[Obsidian]]
  - Created concepts: [[AgentHarness]], [[ContextRot]], [[SecondBrain]], [[SystemEvolution]], [[AgenticEngineering]], [[PRDFirstDevelopment]], [[ModularRulesArchitecture]], [[Commandification]], [[ContextReset]], [[ProgressiveDisclosure]], [[KarpathyLLMWiki]]
  - Updated concepts: [[RetrievalAugmentedGeneration]] (11-strategy survey), [[VibeCoding]] (harness-era reframe)
  - Updated entities: [[ColeMedin]] (Second Brain era + AgenticEngineering codification), [[ClaudeCode]] (Skills + Second Brain + harness substrate), [[AndrejKarpathy]] (KarpathyLLMWiki cross-link)
  - Updated [[index.md]] (16 new pages registered)
- **Conflicts**: none new
- **Notes**:
  - Big batch — 4 transcripts produced 13 new pages + 5 updates. The "5 Techniques" video alone spawned 6 concept pages (AgenticEngineering umbrella + 5 techniques) since each technique is referenced independently across Cole's other content.
  - [[KarpathyLLMWiki]] created as a stub — directly relevant to THIS vault's design. Will be substantially expanded in batch C when the `20260406` Karpathy-LLM-Wiki video is ingested.
  - [[SecondBrain]] + [[Obsidian]] + [[ClaudeSkills]] form the self-referential core: these pages describe the exact pattern/tools this wiki is built with.
  - Skipped sponsor segments (OutSystems, Lindy, Scribba) and tangential vendor mentions (Manus, LangChain Deep Agents, Graphiti, Docling, Zapier, Excalidraw, Remotion, Gamma, Helicone — covered inline where relevant).

## [2026-06-20] ingest | Cole Medin "Channel Only" — selective batch C (4 transcripts, Mar-May 2026) — FINAL curated batch
- **Sources processed**:
  - `raw/03-transcripts/Cole Medin/Channel Only/20260330 - Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique).md`
  - `raw/03-transcripts/Cole Medin/Channel Only/20260402 - Full Guide - Build Your Own AI Second Brain with Claude Code.md`
  - `raw/03-transcripts/Cole Medin/Channel Only/20260406 - I Built Self-Evolving Claude Code Memory w⧸ Karpathy's LLM Knowledge Bases.md`
  - `raw/03-transcripts/Cole Medin/Channel Only/20260528 - Harness Engineering： What Separates Top Agentic Engineers Right Now.md`
- **Changes**:
  - Created sources: [[summary-adversarial-dev-technique]], [[summary-full-guide-ai-second-brain]], [[summary-self-evolving-memory-karpathy-llm-wiki]], [[summary-harness-engineering]]
  - Created entities: [[Codex]], [[OpenClaw]]
  - Created concepts: [[HarnessEngineering]], [[AILayer]], [[AdversarialDev]], [[Sycophancy]], [[RalphLoop]], [[LethalTrifecta]]
  - **Major expansion**: [[KarpathyLLMWiki]] — promoted from batch-B stub to full page. The `20260406` video is its canonical source and describes THIS vault's exact architecture (raw → compiler → wiki → lint → query). Added the compiler analogy, Cole's self-evolving internal-memory variant, the compounding loop, and a section mapping the pattern to this vault's implementation.
  - Updated concepts: [[SecondBrain]] (memory layer + heartbeat + lethal-trifecta security from the full guide), [[AgentHarness]] (adversarial dev, ralph loop, harness engineering cross-links), [[SystemEvolution]] (the "skill-issue reframe" / mindset-half-of-harness-engineering connection)
  - Updated entities: [[Archon]] (repositioned as harness builder for 2026)
  - Updated [[index.md]] (16 new pages registered)
- **Conflicts**: none new (the RAG-vs-Wiki tension noted in prior batches is reinforced and reconciled in [[KarpathyLLMWiki]])
- **Notes**:
  - This completes the curated Tier 1 + Tier 2 selective ingest (11 of 11 transcripts across batches A/B/C).
  - The `20260406` Karpathy LLM Wiki video is the single most self-relevant source in the entire corpus — it literally documents the pattern this vault is built on. KarpathyLLMWiki page now cross-references the vault's own `CLAUDE.md` schema and `.claude/skills/`.
  - Skipped sponsors (Scrimba, Google Cloud Agency CLI, InspoForge) and inline-only mentions (Jeffrey Huntley — credited in RalphLoop; GANs; Threek/Anthropic ToS clarification; Simon Willison — origin of lethal-trifecta term, noted in that page).
  - 28 of the original 49 Channel Only transcripts remain un-ingested by design (news commentary, livestreams, model-release reactions, niche workflows). They stay in raw/03-transcripts for optional future ingest.

## [2026-06-20] query | Four cross-cutting syntheses (paradigm evolution, RAG playbook, vault self-mapping, context rot)
- **Output**: saved 4 synthesis pages:
  - [[evolution-vibe-coding-to-harness-engineering]]
  - [[cole-medin-rag-playbook]]
  - [[vault-architecture-mapped-to-cole-teachings]]
  - [[fighting-context-rot]]
- **Pages consulted**: VibeCoding, ContextEngineering, HarnessEngineering, AgentHarness, AgenticEngineering, SystemEvolution, ContextRot, AndrejKarpathy, RetrievalAugmentedGeneration, ContextualRetrieval, Reranking, HybridSearch, PromptCaching, Crawl4AIRAG, Neon, Supabase, KarpathyLLMWiki, SecondBrain, Obsidian, ClaudeCode, ClaudeSkills, ProgressiveDisclosure, ModularRulesArchitecture, ContextReset, Commandification, RalphLoop, AdversarialDev, SubAgent, HumanInTheLoop, plus the relevant source summaries.
- **Notes**: First population of wiki/syntheses/ — demonstrates the query→synthesize→file-back compounding loop. All four are analytical/comparative spanning 4+ pages each, so all met the save-worthy threshold. User pre-approved saving all four.

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 2 (2026-H1), file 1/11: AI Exploded in 2025
- **Changes**: created [[summary-ai-exploded-in-2025]]; updated [[Anthropic]] (2025 milestones), [[ClaudeCode]] ($1B revenue, Bun, Claude Code for web), [[ClaudeSkills]] (Oct 2025 release timeline), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 2 (2026-H1), file 2/11: Kiro Hackathon announcement
- **Changes**: created [[summary-kiro-hackathon]], created [[Kiro]]; updated [[AICodingAssistant]] (linked Kiro), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 2 (2026-H1), file 3/11: Ralph Wiggum / final evolution of vibe coding
- **Changes**: created [[summary-ralph-wiggum-vibe-coding]]; updated [[RalphLoop]] (plugin mechanics, use cases, failure modes, PRP+Ralph, Model T), [[VibeCoding]] (Ralph as ceiling), [[AgentHarness]] (Ralph as most basic harness), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 2 (2026-H1), file 4/11: Claude Skills for ANY Agent
- **Changes**: created [[summary-build-skills-for-any-agent]]; updated [[ClaudeSkills]] (universal impl + skill creator), [[ProgressiveDisclosure]] (from-scratch mechanics + sizing), [[PydanticAI]] (skills agent, evals, Logfire), [[AgentEvaluation]] (skill-usage eval example), [[AgentObservability]] (Logfire detail), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 2 (2026-H1), file 5/11: Full Engineering Team with Subagents
- **Changes**: created [[summary-full-engineering-team-subagents]], created [[Arcade]], created [[ClaudeAgentSDK]]; updated [[AgentHarness]] (tool belt / full AI engineer), [[SubAgent]] (context isolation + per-model), [[Archon]] (N8N for AI coding pivot), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 2 (2026-H1), file 6/11: Safer OpenClaw Alternative
- **Changes**: created [[summary-safer-openclaw-alternative]]; updated [[OpenClaw]] (security incidents, 4 components, Peter/185k stars, corrected Nano Claw, ToS), [[SecondBrain]] (clone-and-rebuild method + VPS stack), [[LethalTrifecta]] (concrete OpenClaw vulns), [[ClaudeAgentSDK]] (heartbeat use), updated [[index.md]]
- **Conflicts**: none (corrected a prior factual note: "Nemo Claw" → "Nano Claw", a separate tool not a fork)

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 2 (2026-H1), file 7/11: Claude Code Agent Teams (live build)
- **Changes**: created [[summary-agent-teams-live-build]], created [[AgentTeams]], created [[VercelAgentBrowser]]; updated [[PRPFramework]] (clarifying-questions planning), [[ValidationGates]] (e2e browser validation), [[SubAgent]] (Agent Teams evolution), [[ClaudeSkills]] (SaaS ships skills), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 2 (2026-H1), file 8/11: Why the Best AI Tools Abandoned RAG
- **Changes**: created [[summary-is-rag-dead-for-coding]], created [[AgenticSearch]]; updated [[RetrievalAugmentedGeneration]] (is-RAG-dead nuance), [[ClaudeCode]] (agentic search), [[Archon]] (RAG-for-coding decline), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 2 (2026-H1), file 9/11: COMPLETE Agentic Coding Workflow
- **Changes**: created [[summary-complete-agentic-coding-workflow]], created [[PIVLoop]]; updated [[AILayer]] (greenfield context-asset framing), [[Commandification]] (commands vs skills), [[PRDFirstDevelopment]] (PRD creation flow), [[SystemEvolution]] (parallel evolution + git memory), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 2 (2026-H1), file 10/11: Self-healing e2e validation (/e2e-test)
- **Changes**: created [[summary-self-healing-e2e-validation]]; updated [[ValidationGates]] (self-healing workflow), [[VercelAgentBrowser]] (validation micro-loop), [[PIVLoop]] (e2e-test as validate step), [[SubAgent]] (3 parallel research agents), [[Neon]] (test-data branching), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 2 (2026-H1), file 11/11: Beautiful Diagrams with Claude Code
- **Changes**: created [[summary-beautiful-diagrams-claude-code]], created [[Excalidraw]]; updated [[ClaudeSkills]] (diagram skill), [[Obsidian]] (Excalidraw render target), [[SecondBrain]] (diagram-generator skill), updated [[index.md]]
- **Conflicts**: none
- **Batch note**: Batch 2 (2026-H1) COMPLETE — all 11 files ingested and archived. Batches 1 (2025, 12 files) and 3 (2026-H2, 11 files) remain unprocessed in raw/03-transcripts/.

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 3 (2026-H2), file 1/11: Is Software Engineering Finally Dead
- **Changes**: created [[summary-is-software-engineering-dead]], created [[IntentEngineering]]; updated [[ContextEngineering]] (intent-engineering successor), [[AgenticEngineering]] (evolution chain), [[ClaudeCode]] (Boris Cherny nuance), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 3 (2026-H2), file 2/11: 2,000+ Hours of Claude Code (WISK)
- **Changes**: created [[summary-2000-hours-claude-code-wisk]], created [[WISKFramework]]; updated [[ContextRot]] (Chroma report, distractors, 80% stat), [[SubAgent]] (scout pattern + 90.2% isolation), [[Archon]] (new command-center demo), [[fighting-context-rot]] (WISK), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 3 (2026-H2), file 3/11: The Subagent Era Is Officially Here
- **Changes**: created [[summary-subagent-era]]; updated [[SubAgent]] (sub-agent era, cheap models, sidecar pattern), [[Codex]] (GPT-5.4 Mini sub-agents), [[WISKFramework]] (backlink), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 3 (2026-H2), file 4/11: Everything About Building AI Agents is Wrong
- **Changes**: created [[summary-sdk-vs-framework-agents]], created [[AgentSDKvsFramework]]; updated [[ClaudeAgentSDK]] (limitations, non-coding agents, ToS), [[RetrievalAugmentedGeneration]] (agentic-RAG arc, LlamaIndex), [[PydanticAI]] (framework-vs-SDK), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 3 (2026-H2), file 5/11: Parallel Claude Code + Git Worktrees
- **Changes**: created [[summary-parallel-claude-code-worktrees]], created [[ParallelAgenticDevelopment]]; updated [[ClaudeCode]] (native worktrees/model/Codex plugin), [[Neon]] (branch-per-worktree), [[AgentTeams]] (worktrees-preferred contrast), [[AdversarialDev]] (cross-model PR review), [[SystemEvolution]] (self-healing layer), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 3 (2026-H2), file 6/11: Principled Agentic Engineer (workshop)
- **Changes**: created [[summary-principled-agentic-engineer]] (consolidation, no new pages); updated [[PIVLoop]] (inner/outer loop), [[PRDFirstDevelopment]] (PRD→stories→Jira, PM role), [[SystemEvolution]] (outer loop, version-controlled AI layer), [[AgenticEngineering]] (simple-vs-bloated framing), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 3 (2026-H2), file 7/11: AI YouTube Is Only Claude Hype Now
- **Changes**: created [[summary-ai-youtube-claude-hype]] (thin source); updated [[ColeMedin]] (content philosophy, live streams, Dark Factory), [[BuildInPublic]] (live building), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 3 (2026-H2), file 8/11: Make the PERFECT Videos with Claude Code
- **Changes**: created [[summary-ai-generated-videos-claude-code]], created [[HyperFrames]]; updated [[Archon]] (shipped: arkon.diy, 21k stars, PIV/Fix/Review workflows), [[ClaudeSkills]] (video skill backlink), updated [[index.md]]
- **Conflicts**: none

## [2026-06-20] ingest | Cole Medin "Channel Only" — Batch 3 (2026-H2), file 9/11: Anthropic Masterclass on Large Codebases
- **Changes**: created [[summary-large-codebases-claude-code]], created [[LargeCodebaseStrategies]]; updated [[AILayer]] (7th component LSP, layered rules, self-improving hooks), [[ModularRulesArchitecture]] (subdirectory CLAUDE.md), [[AgenticSearch]] (LSP complement), updated [[index.md]]
- **Conflicts**: none

## [2026-06-21] ingest | Cole Medin "Channel Only" — Batch 3 (2026-H2), file 10/11: Claude Plans, Gemini Designs
- **Changes**: created [[summary-claude-plans-gemini-designs]], created [[CrossProviderWorkflow]], created [[Pi]], created [[Antigravity]]; updated [[AILayer]] (Pi link), [[AICodingAssistant]] (Pi/Antigravity), [[Archon]] (cross-provider one-shot), [[summary-ai-exploded-in-2025]] (Antigravity link), updated [[index.md]]
- **Conflicts**: none

## [2026-06-21] ingest | Cole Medin "Channel Only" — Batch 3 (2026-H2), file 11/11: Loop Engineering (Creators Don't Prompt Anymore)
- **Changes**: created [[summary-loop-engineering]], created [[LoopEngineering]], created [[Retool]]; updated [[ClaudeCode]] (/loop, /goal, /routines), [[RalphLoop]] (/goal), [[HarnessEngineering]] (loop engineering folds in), [[Archon]] (deterministic loops), updated [[index.md]]
- **Conflicts**: none
- **Batch note**: Batch 3 (2026-H2) COMPLETE — all 11 files ingested and archived. Batch 1 (2025, 12 files) remains unprocessed in raw/03-transcripts/.

## [2026-06-22] ingest | Brian Casel "Channel Only" — Batch 1 of 8 (Jun-Apr 2026, 7 transcripts)
- **Sources processed**:
  - `raw/03-transcripts/Brian Casel/Channel Only/20260622 - How to build your own CRM (start to finish).md`
  - `raw/03-transcripts/Brian Casel/Channel Only/20260611 - Claude Fable： Build me an app.md`
  - `raw/03-transcripts/Brian Casel/Channel Only/20260609 - Hermes vs. Claude Cowork Wrong Question.md`
  - `raw/03-transcripts/Brian Casel/Channel Only/20260605 - Why apps built with AI look a little... OFF.md`
  - `raw/03-transcripts/Brian Casel/Channel Only/20260518 - You don't need to learn to code anymore.md`
  - `raw/03-transcripts/Brian Casel/Channel Only/20260512 - How I build agents that work the night shift.md`
  - `raw/03-transcripts/Brian Casel/Channel Only/20260429 - Multitasking With Agents： My 2026 Workflow.md`
- **Changes**:
  - Created sources: [[summary-build-your-own-crm]], [[summary-claude-fable-build-app]], [[summary-hermes-vs-claude-cowork]], [[summary-apps-built-with-ai-look-off]], [[summary-dont-need-to-learn-code]], [[summary-night-shift-agents]], [[summary-multitasking-agents-2026]]
  - Created entities: [[BrianCasel]], [[BuildNew]], [[PRDCreator]], [[DesignSystem]], [[HermesAgent]], [[ClaudeCowork]], [[SparkDrop]], [[BrainDown]], [[ResonanceRadar]], [[SuperSet]], [[Superconductor]], [[Consensus]]
  - Created concepts: [[SpecDrivenDevelopment]], [[MilestoneBasedBuilding]], [[ProductArchitect]], [[NightShiftModel]], [[AgentPlatformPortability]], [[AgentMultitasking]], [[InternalTools]], [[StarterKit]], [[DesignDrift]], [[VerificationCriteria]], [[IntakeProcessing]], [[ContentIdeation]], [[AgentSkills]]
  - Updated [[index.md]] (32 new pages registered)
- **Conflicts**: none
- **Notes**:
  - Batch 1 of 8 planned chronological clusters covering 55 Brian Casel Channel Only transcripts (newest first).
  - Brian Casel is a distinct voice from Cole Medin — focused on spec-driven development, internal tools, and agent orchestration for solo business operators.
  - Key new concepts: [[NightShiftModel]], [[SpecDrivenDevelopment]], [[DesignDrift]], [[AgentPlatformPortability]].
  - Brian's tools ([[PRDCreator]], [[DesignSystem]], [[BuildNew]]) are free and open-source.
  - Skipped sponsor segments and tangential mentions.

## [2026-06-22] ingest | Brian Casel "Channel Only" — Batch 2 of 8 (Apr-Mar 2026, 7 transcripts)
- **Sources processed**:
  - `raw/03-transcripts/Brian Casel/Channel Only/20260424 - Where Claude Design actually fits.md`
  - `raw/03-transcripts/Brian Casel/Channel Only/20260414 - We build fast. But does it work.md`
  - `raw/03-transcripts/Brian Casel/Channel Only/20260406 - 4 Agent Skills I Use for Marketing.md`
  - `raw/03-transcripts/Brian Casel/Channel Only/20260331 - The Skill AI Can't Replace.md`
  - `raw/03-transcripts/Brian Casel/Channel Only/20260326 - Claude Code on Mobile： The Complete Guide.md`
  - `raw/03-transcripts/Brian Casel/Channel Only/20260312 - Claude Code changed recently.md`
  - `raw/03-transcripts/Brian Casel/Channel Only/20260306 - OpenClaw vs. Claude for Running an Agent Team.md`
- **Changes**:
  - Created sources: [[summary-where-claude-design-fits]], [[summary-we-build-fast-but-does-it-work]], [[summary-4-agent-skills-marketing]], [[summary-skill-ai-cant-replace]], [[summary-claude-code-mobile-guide]], [[summary-claude-code-changed-recently]], [[summary-openclaw-vs-claude-agent-team]]
  - Created entities: [[ClaudeDesign]], [[KainAI]], [[NimbleList]]
  - Created concepts: [[Restraint]], [[VisualIdeation]], [[MobileAgentWorkflow]], [[AutoPlan]], [[AutoMemory]], [[VoiceMode]], [[ServerMode]], [[BrandVisuals]], [[EndToEndTesting]]
  - Updated [[index.md]] (19 new pages registered)
- **Conflicts**: none
- **Notes**:
  - Batch 2 of 8. Key new concepts: [[Restraint]] (strategic discipline), [[VisualIdeation]] (shaping phase technique), [[MobileAgentWorkflow]] (four scenarios for mobile coding).
  - Claude Code 2026 features documented: [[AutoPlan]], [[AutoMemory]], [[VoiceMode]].
  - Brian's marketing automation skills ([[BrandVisuals]], newsletter writer/builder) show the [[AgentSkills]] pattern applied beyond development.

## [2026-06-22] ingest | Brian Casel "Channel Only" — Batch 3 of 8 (Feb-Jan 2026, 7 transcripts)
- **Sources processed**: 7 transcripts (20260225 through 20260119)
- **Changes**:
  - Created sources: [[summary-create-jobs-openclaw-agents]], [[summary-multi-agent-team-openclaw]], [[summary-claude-code-slack-teams-ship]], [[summary-build-marketing-tools-claude-code]], [[summary-brennan-dunn-ai-developers]], [[summary-agent-os-v3]], [[summary-arvid-kahl-saas-claude]]
  - Created entities: [[AgentOS]], [[ColleenSchnettler]], [[ArvidKahl]], [[BrennanDunn]], [[Podscan]], [[FernDesk]], [[CompoundEngineering]]
  - Created concepts: [[ComprehensionDebt]], [[AgentJobs]], [[BuilderStories]], [[SlackIntegration]]
  - Updated [[index.md]] (18 new pages registered)
- **Conflicts**: none
- **Notes**: Batch 3 introduces Builder Stories guests (Arvid Kahl, Brennan Dunn, Colleen Schnettler) and Brian's Agent OS v3 release. Key new concept: [[ComprehensionDebt]].

## [2026-06-22] ingest | Brian Casel "Channel Only" — Batch 4 of 8 (Jan-Nov 2025, 7 transcripts)
- **Sources processed**: 7 transcripts (20260114 through 20251120)
- **Changes**: created 7 source summaries, 1 entity ([[DesignOS]]), 1 concept ([[ModelConvergence]]), updated [[index.md]]
- **Conflicts**: none

## [2026-06-22] ingest | Brian Casel "Channel Only" — Batches 5-8 (Nov 2025-Apr 2025, 27 transcripts)
- **Sources processed**: 27 transcripts (20251112 through 20250404)
- **Changes**: created 27 source summaries, updated [[index.md]]
- **Conflicts**: none
- **Notes**: Batches 5-8 completed in rapid succession. These earlier transcripts cover Brian's foundational content: the case for Claude Code, early Agent OS releases, spec-driven development methodology, Rails tutorials, and the transition from vibe coding to professional building. Many concepts introduced here (spec-driven development, milestone building, design systems) were later refined in his 2026 content.
