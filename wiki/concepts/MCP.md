---
title: "MCP"
type: concept
tags: [protocol, agent-integration, context, tools]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gateways are All You Need — Karan Sampath, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md"]
last_updated: 2026-06-29
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

- **Ecosystem growth**: Reached 110 million monthly downloads, growing faster than React did. Used by OpenAI's Agent SDK, Google's ADK, LangChain, and thousands of frameworks as a dependency — establishing one common standard across the industry.
- **MCP roadmap** (from David Soria Parra, Anthropic): (1) Stateless transport protocol (from Google) for easier hyperscaler scaling — June 2026; (2) Improved async task primitive for agent-to-agent communication; (3) TypeScript SDK v2 and Python SDK v2; (4) Cross-app access — login once with company IdP, use all MCP servers; (5) Server discovery via well-known URLs; (6) Skills over MCP — ship domain knowledge with servers; (7) MCP applications — serving UI interfaces over MCP.
- **Connectivity stack**: David Soria Parra advocates using skills, MCP, and CLI/computer use together — no single solution fits all connectivity problems. MCP is best when you need rich semantics, platform independence, authorization, governance, or enterprise features.
- **Design for agents**: MCP servers should be designed for agent interaction, not just wrapped REST APIs. Use rich MCP semantics: applications, skills over MCP, tasks, elicitation.

- **Enterprise challenges**: Three core problems for enterprise MCP adoption — observability (who is using which MCP, which tools aren't working), access control (scoping tools to correct users/groups), and security (verifying server safety, preventing data exfiltration, securing remote untrusted clients). Described as a "three-headed hydra."
- **MCP Gateway**: Proposed solution for enterprise MCP deployment — a middleware layer centralizing authentication, access control, routing, observability, credential management, and deployment. Establishes a root of trust enabling decentralized MCP development across teams.
- **Registry gap**: MCP registries are useful but incomplete for enterprises — they lack authentication, access control, observability, and credential management.
- **Decentralized development**: With a gateway, non-technical teams (e.g., legal) can build their own MCP servers focusing only on business logic, not infrastructure concerns.
- **Amazon Kiro integration**: Kiro integrates MCP across all spec phases (requirements generation, design, implementation). Users can add MCP servers via UI or by asking the agent; tools can be allow-listed or disabled. Changing MCP config mid-session invalidates prompt cache, dramatically slowing deep sessions. Kiro's internal team uses MCP to blast specs into their wiki for design reviews. Example MCP servers used with Kiro: Asana (task pulling), AWS documentation, fetch (web content), Brave search.

- **MCP as Middleware** (Matt Carey): MCP will become a native flag in web frameworks (`MCP=true`), SDK getting super lightweight, natively in every TypeScript full-stack framework by end of year. Express thousands of APIs from one Next.js app with `MCP=true`.
- **Context explosion** (Matt Carey): Cloudflare's OpenAPI spec is 2.3M tokens, ~1.1M tokens as tools — impossible to load all at once. Initial response was 16 product-based MCP servers, but this had incomplete coverage. Progressive discovery and code mode are the solutions.
- **Building MCP clients**: Has been very hard — requires managing stateful connections, resumability. Most clients are stripped-down, offloading to bare-bones SDKs. This will change as the SDK improves.

- **Demand-Driven Context critique**: Raj built 20+ MCP servers before realizing the approach doesn't work against monolithic knowledge bases. MCP outputs are undeterministic, unreliable, and untested — 10-30% accuracy at best. Engineers don't do evals on MCP outputs; they check if output is coming, not if it's valuable. The fundamental problem is the underlying knowledge base quality, not the retrieval mechanism.

## Related
- [[summary-20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code]] — source (Amp Code's MCP position)
- [[summary-20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz]] — source (MCP optimization framework)
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — source (context explosion, MCP as middleware, client challenges)
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source (MCP limitations critique)
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
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source (MCP roadmap, ecosystem growth, connectivity stack)
- [[DavidSoriaParra]] — MCP engineer at Anthropic
- [[MCPApplications]] — experimental feature for serving UI over MCP
- [[ProgressiveDiscovery]] — client-side pattern for on-demand tool loading
- [[ProgrammaticToolCalling]] — composing tool calls in code
- [[ConnectivityStack]] — skills + MCP + CLI/computer use framework
- [[SkillsOverMCP]] — upcoming extension for shipping skills with servers
- [[StatelessTransportProtocol]] — Google's proposal for scalable MCP transport
- [[AgentToAgentCommunication]] — async task primitive for agent-to-agent
- [[ServerDiscovery]] — auto-discovery via well-known URLs
- [[ToolSearch]] — mechanism for progressive discovery
- [[MCP as Middleware]] — vision for MCP as a framework flag
- [[MattCarey]] — presenter on MCP context problems and solutions
- [[DemandDriven Context]] — alternative pull-based approach
- [[Knowledge Base Monolith]] — the deeper problem MCP doesn't solve
- [[EvalEngineering]] — missing practice for MCP outputs
