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
