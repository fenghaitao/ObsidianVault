---
title: "MCP"
type: concept
tags: [protocol, agent-integration, context, tools]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gateways are All You Need — Karan Sampath, Anthropic.md"]
last_updated: 2026-06-26
---

## Definition
MCP (Model Context Protocol) is a protocol for providing context to AI agents, enabling standardized integration between agents and external tools or data sources. MCP servers expose callable functions (tools) wrapped with descriptions that guide agent behavior.

## Key Information
- Described as "an amazing new protocol that's gotten everyone and their mom thinking about how to provide context to agents"
- Amp Code made a contrarian decision to limit MCP investment in favor of a custom tool set, for two reasons:
  1. MCP server creators don't know what the agent is trying to do, so tool descriptions aren't tuned to the agent's specific feedback loops
  2. Too many tools in the context window cause "context confusion" — the agent gets confused choosing among irrelevant tools
- This position was described as "less controversial now than it was back in April" (2025)
- **Third-party tool challenges**: MCP server tools are designed for generic use cases and often fail out of the box for specific applications. Tool descriptions are intentionally shallow (e.g., "Press a key on the keyboard") because they must serve many different use cases.
- **Optimization framework**: Five practices can transform generic MCP tools into effective tailored components: curation (filtering), wrapping (enhanced descriptions), deterministic guardrails, tool composition, and deterministic usage outside the agent loop.
- **LangChain integration**: LangChain's `load_mcp_tools` method provides a standard way to import MCP server tools into agent workflows.
- **Agentic product design**: Jeremiah Lowin argues MCP servers should be treated as user interfaces for AI agents, not REST API wrappers. Key design principles: outcomes over operations, flatten arguments, instructions as context, respect the token budget, curate ruthlessly.
- **Token budget constraint**: On handshake, agents download all tool descriptions at once. With 800 tools and a 200K token window, each tool gets only ~250 tokens. The GitHub MCP server reportedly ships ~200K tokens on handshake.
- **50-tool heuristic**: Agent performance degrades beyond ~50 tools per agent. Kelly KFL at Fiverr curated a server from 188 tools down to 5.
- **Claude Desktop limitations**: Hashes tools on first contact into SQLite, ignores subsequent updates, and sends structured arguments as strings -- breaking progressive disclosure and dynamic tool listing.
- **Elicitation**: MCP spec feature allowing tools to request additional input mid-execution. Limited client support.
- **Readonly hint**: MCP annotation marking tools as read-only, helping clients with permission handling.
- **Code mode**: Emerging technique where LLMs write code calling MCP tools in sequence, sidestepping iteration problems.
- **Context overhead concern** (Brendan O'Leary): Every enabled MCP server adds tool descriptions to the system prompt on every interaction. Disable unused MCP servers to avoid wasted tokens and potential agent confusion. Example: a Postgres MCP connected to a database adds unnecessary context when doing front-end work. There are thousands of MCP servers available.
- **Examples**: GitHub MCP (interact with GitHub API, pull requests, issues), Context7 (up-to-date framework documentation), Postgres MCP (database connectivity).

- **Enterprise challenges**: Three core problems for enterprise MCP adoption — observability (who is using which MCP, which tools aren't working), access control (scoping tools to correct users/groups), and security (verifying server safety, preventing data exfiltration, securing remote untrusted clients). Described as a "three-headed hydra."
- **MCP Gateway**: Proposed solution for enterprise MCP deployment — a middleware layer centralizing authentication, access control, routing, observability, credential management, and deployment. Establishes a root of trust enabling decentralized MCP development across teams.
- **Registry gap**: MCP registries are useful but incomplete for enterprises — they lack authentication, access control, observability, and credential management.
- **Decentralized development**: With a gateway, non-technical teams (e.g., legal) can build their own MCP servers focusing only on business logic, not infrastructure concerns.- **Amazon Kiro integration**: Kiro integrates MCP across all spec phases (requirements generation, design, implementation). Users can add MCP servers via UI or by asking the agent; tools can be allow-listed or disabled. Changing MCP config mid-session invalidates prompt cache, dramatically slowing deep sessions. Kiro's internal team uses MCP to blast specs into their wiki for design reviews. Example MCP servers used with Kiro: Asana (task pulling), AWS documentation, fetch (web content), Brave search.

## Related
- [[summary-20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code]] — source (Amp Code's MCP position)
- [[summary-20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz]] — source (MCP optimization framework)
- [[AmpCode]] — product that deliberately limits MCP usage
- [[ThirdPartyToolOptimization]] — framework for optimizing MCP tools
- [[ContextExhaustion]] — related context management challenge
- [[ToolCalling]] — underlying mechanism
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source (MCP best practices)
- [[FastMCP]] — de facto standard Python framework for building MCP servers
- [[AgenticProductDesign]] — design philosophy for MCP servers
- [[TokenBudget]] — critical constraint on MCP server design
- [[FiftyToolRule]] — heuristic for tool count limits
- [[CurateRuthlessly]] — key design principle
- [[OutcomesOverOperations]] — key design principle
- [[FlattenArguments]] — key design principle
- [[ErrorsAsPrompts]] — key design principle
- [[Elicitation]] — MCP protocol feature
- [[ReadonlyHint]] — MCP annotation
- [[CodeMode]] — emerging MCP technique
- [[ProgressiveDisclosure]] — design pattern for MCP servers
- [[ClaudeDesktop]] — MCP client with known limitations
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — source (context overhead concerns)
- [[ContextEngineering]] — the practice of managing context, including MCP overhead
- [[Context7]] — example MCP server for documentation
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source (Kiro's MCP integration)
- [[AmazonKiro]] — IDE that extensively uses MCP across all spec phases
