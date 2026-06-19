# Operation Log

Append-only chronological record of all wiki operations.

Format: `## [YYYY-MM-DD] <action> | <one-line summary>`

Grep-friendly: `grep "^## \[" log.md | tail -10` to see recent operations.

---

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
