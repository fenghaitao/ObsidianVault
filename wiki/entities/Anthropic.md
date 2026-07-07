---
title: "Anthropic"
type: entity
tags: [company, ai, claude, platform]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - Japan/01 - Code with Claude Tokyo 2026： Opening Keynote.md, raw/01-articles/claude/2024-05-01 - Introducing the Claude Team plan and iOS app.md, raw/01-articles/claude/2024-09-10 - Claude for Enterprise.md, raw/01-articles/claude/2024-05-20 - Generate better prompts in the developer console.md, raw/01-articles/claude/2024-05-30 - Claude can now use tools.md, raw/01-articles/claude/2024-10-24 - Introducing the analysis tool in Claude.ai.md, raw/01-articles/claude/2025-03-13 - Token-saving updates on the Anthropic API.md, raw/01-articles/claude/2024-09-10 - Workspaces in the Anthropic API Console.md, raw/01-articles/claude/2025-06-23 - Introducing Citations on the Anthropic API.md, raw/01-articles/claude/2025-07-25 - Build and share AI-powered apps with Claude.md, raw/01-articles/claude/2025-07-24 - How Anthropic teams use Claude Code.md, raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md, raw/01-articles/claude/2025-09-09 - Claude can now create and edit files.md, raw/01-articles/claude/2025-09-24 - Claude is now available in Microsoft 365 Copilot.md, raw/01-articles/claude/2026-05-14 - The founder&#39;s playbook Building an AI-native startup.md, "raw/01-articles/claude/2026-06-03 - Running an AI-native engineering org.md", "raw/01-articles/claude/2026-06-05 - The Claude Cowork product guide.md", "raw/01-articles/claude/2026-06-05 - How one Anthropic seller rebuilt his team's workflows with Claude Code.md", "raw/01-articles/claude/2026-06-03 - How Anthropic enables self-service data analytics with Claude.md", "raw/01-articles/claude/2026-06-08 - Building intelligent apps for Apple platforms with Claude in the Foundation Models framework.md", raw/01-articles/claude/2026-06-08 - Observability for developers building connectors.md, "raw/01-articles/claude/2026-06-24 - Agent identity in Claude Tag a new access model for autonomous, team-wide AI.md", raw/01-articles/claude/2026-06-18 - Centrally manage authorization for MCP connectors.md, "raw/01-articles/claude/2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry.md", "raw/01-articles/claude/2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon.md", "raw/01-articles/claude/2026-06-24 - Building effective human-agent teams.md"]
last_updated: 2026-07-07
---

## Definition

Anthropic is an AI company that builds the Claude family of models and the Claude platform. It positions itself as a platform company, providing developers with the tools to build systems on top of Claude.

## Key Information

- Creator of Claude (Haiku, Sonnet, Opus, Fable, Mythos model families).
- All Claude 3 models support [[ToolUse|tool use]] (generally available as of May 2024), enabling Claude to interact with external APIs and tools.
- Platform includes [[ClaudeCode]] (developer agent), [[ClaudeCowork]] (knowledge work agent), [[ClaudeManagedAgents]] (production agent infrastructure), [[ClaudeTag]] (multiplayer AI in shared Slack channels with [[AgentIdentity|agent identity]] access model), the Claude API, [[ClaudeTeamPlan]] (team collaboration), [[ClaudeEnterprise]] (enterprise collaboration with 500K context window and GitHub integration), and mobile apps ([[ClaudeIOSApp]], Android app).
- Year-over-year API volume up nearly 17x on the platform.
- Engineers at Anthropic ship on average 8x more code than in past years using Claude Code.
- All internal teams use Claude Code's code review product.
- Partners include Rakuten, Canva, Spotify, Mercari, Notion, Asana, Cognition, Genspark, [[Microsoft]] (Claude in Microsoft 365 Copilot, September 2025).
- Enterprise platform partners: [[AmazonBedrock]] (AWS), [[VertexAI]] (Google Cloud), [[Microsoft365Copilot]] — giving enterprise customers model choice across major platforms.
- Claude Sonnet 4 and Claude Opus 4.1 are available in [[Microsoft365Copilot]] via the Researcher agent and [[CopilotStudio]] (September 2025); Anthropic models are hosted outside Microsoft-managed environments.
- Cloud distribution partner: Amazon Web Services (AWS) via [[AmazonBedrock]] — Claude models have been available on Bedrock since its April 2023 launch.
- Enterprise customers via Bedrock include [[LexisNexis]], [[LonelyPlanet]], and [[RicohUSA]].
- All Claude models are trained using [[ConstitutionalAI]], Anthropic's alignment methodology.

### Internal Use: Legal Team (December 2025)

Anthropic's legal team, led by product lawyer Mark Pike (non-coder), built four [[ClaudeCodeSkills|Skills]]- and [[ModelContextProtocol|MCP]]-powered workflows: a Slack-based marketing self-review tool (2-3 days to 24 hours turnaround), a contract redlining assistant working inside Google Docs/Office 365, an outside-business-activity conflict-of-interest checker, and privacy impact assessment generation from an MCP-connected Google Drive folder of precedents. Workflows route to lawyers for final approval rather than around them, since AI can still hallucinate. See [[summary-2025-12-08 - How Anthropic&#39;s legal team cut review times from days to hours with Claude]].

### Internal Use: Cybersecurity / Detection Platform Engineering (May 2026)

Detection Platform Engineering Technical Lead Jackie Bow's team built [[ClaudeCode|Claude Code]]-powered CLUE ("Claude Looks Up Evidence"), a detection-and-response platform connecting Claude via tool use to Slack, internal docs, code repos, and data warehouses. CLUE Triage auto-dispositions alerts (false positive rate dropped ~33% → 7%); CLUE Investigate runs natural-language investigations via parallel sub-agent queries (3-4 minutes vs. hours-to-days manually). Over 30 days: ~12,000 queries, ~27,000 tool calls automated, an estimated 1,870 hours (234 person-days) of manual work saved, 5-10x time savings. See [[summary-2026-05-12 - How Anthropic&#39;s cybersecurity team built a threat detection platform with Claude Code]].

### Code with Claude Expansion (March 2026)

Runs [[CodeWithClaude]], its developer conference; expanded from San Francisco-only (2025) to San Francisco, London, and Tokyo for spring 2026, per [[summary-2026-03-18 - Code with Claude comes to San Francisco, London, and Tokyo]].

### Project Glasswing (April 2026)

Announced [[ProjectGlasswing]], putting the cybersecurity capabilities of its newest frontier model at the time, Claude Mythos Preview, to defensive use. Published prioritized security-program recommendations ([[AIAcceleratedOffense]]) for organizations bracing for AI-accelerated vulnerability discovery and exploitation. See [[summary-2026-04-10 - Preparing your security program for AI-accelerated offense]].

### The Founder's Playbook (May 2026)

Published "The Founder's Playbook: Building an AI-native startup," remapping the four startup lifecycle stages (Idea, MVP, Launch, Scale) for 2026-era AI capabilities, with goals, exit criteria, failure modes, and AI-powered exercises for each stage. Central thesis: AI is shifting the founder's role from individual contributor to orchestrator, letting founders with no coding background ship production applications and reach revenue before scaling headcount. See [[AINativeStartup]] and [[summary-2026-05-14 - The founder&#39;s playbook Building an AI-native startup]].

### Internal Use: Growth Marketing (January 2026)

Growth marketer Austin Lau (no prior coding experience) built a [[Figma]] plugin generating ad creative variants in one click and a Google Ads copy workflow (`/rsa` slash command) combining campaign data with [[ClaudeCodeSkills|Skills]] for brand tone/voice and RSA best practices — cutting ad creation from 30 minutes to 30 seconds. Broader marketing-org results: Influencer Marketing frees 100+ hours/month; Customer Marketing drafts case studies in 30 minutes instead of 2.5 hours; Digital Marketing lifted web-dev productivity 5x year-over-year; Product Marketing saves 5-10 hours per launch brief using Skills and Projects; Partner Marketing cut trade-show prep time 40%. See [[summary-2026-01-26 - How Anthropic&#39;s Growth Marketing team cut ad creation time from 30 minutes to 30 seconds with Claude Code]].

### AI-Native Engineering Org (June 2026)

[[FionaFung]], Director of Engineering for [[ClaudeCode]] and [[ClaudeCowork]], described at Code w/ Claude SF 2026 how the Claude Code team restructured around [[AgenticCoding|agentic coding]] as the default way of working. Key changes: [[JustInTimePlanning|JIT planning]] replaced six-month roadmaps; technical debates are settled by generating competing PRs rather than whiteboarding; [[CodeReview|automated code review]] handles style, linting, bug fixes, and test authoring, with humans reserved for legal review, security-sensitive code, and product taste; hiring indexes on creative builders with product sense and deep systems experts rather than raw throughput; pods operate with agency within a small set of non-negotiable core principles. The team tracks onboarding ramp-up time, PR cycle time, and share of Claude-assisted commits alongside product outcomes. See [[summary-2026-06-03 - Running an AI-native engineering org]].

### Internal Use: GTM / Sales Workflow Automation (June 2026)

Account executive Jared Sires (no prior coding experience) used [[ClaudeCode]] to build **CLAFTS** (Claude Drafts), a ~4,300-line Gmail-integrated application that drafts customer email replies in his voice via the [[ClaudeAPI|Claude API]], saving 10–15 hours per week. The tool uses web search to pull current product documentation on every draft, and CLAFTS Tones pattern-matches writing style across different relationships (customers, peers, family). Shared in Slack and adopted by the sales org within 24 hours. His success led to a role shift into GTM product manager, where he now builds Claude-powered solutions for the entire sales team — including daily brief (morning pre-call research), daily recap (end-of-day follow-up drafts), and a Sales plugin with 20+ [[ClaudeCodeSkills|skills]] adopted by ~80% of the sales organization. See [[AIAcceleratedSalesWorkflows]] and [[summary-2026-06-05 - How one Anthropic seller rebuilt his team's workflows with Claude Code]].

### Internal Use: Self-Service Data Analytics (June 2026)

Anthropic's Data Science and Data Engineering team (Chen Chang, Clement Peng, Justin Leder, Johanne Jiao, Josh Cherry) built an [[AgenticAnalytics|agentic analytics]] stack where Claude handles 95% of business analytics queries with ~95% accuracy. The stack has four layers: data foundations (canonical datasets, enforced standards, colocated artifacts), sources of truth (semantic layer, lineage, query corpus, business context), skills (pairwise knowledge + analysis skills that lifted accuracy from 21% to 95%+), and validation (offline evals, adversarial review, active correction harvesting). Skills are colocated in the same repo as transformation models so model changes and doc updates ship in the same PR; ~90% of data-model PRs include a skill change. Without active skill maintenance, accuracy drifted from ~95% to ~65% over one month. See [[summary-2026-06-03 - How Anthropic enables self-service data analytics with Claude]].

### Apple Foundation Models Integration (June 2026)

Anthropic released a Swift package that connects Apple's [[AppleFoundationModels|Foundation Models framework]] to Claude, enabling Apple platform developers to hand off complex reasoning from on-device models to Claude while preserving typed Swift outputs. The integration works across iOS 27, iPadOS 27, macOS 27, visionOS 27, and watchOS 27. It handles streaming, tool calls, web search, and code execution, returning structured responses into SwiftUI views. This marks Anthropic's first native integration with Apple's on-device AI framework. See [[summary-2026-06-08 - Building intelligent apps for Apple platforms with Claude in the Foundation Models framework]].

### Claude Desktop Cloud Deployment (June 2026)

Anthropic announced the full [[ClaudeDesktop]] experience (chat, Claude Cowork, Claude Code) on AWS, Google Cloud, and Microsoft Foundry, with inference running in the customer's own cloud environment. The deployment includes per-user SSO via IAM Identity Center, Workforce Identity Federation, Microsoft Entra ID, or OIDC providers; MDM policy templates for Intune, GPO, or Jamf; an offline installer for air-gapped environments; and an [[M365Connector|M365 connector]] with local-only mode for strict data residency. Each product surface has its own policy key for phased organizational rollout. See [[summary-2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry]].

### Connector Observability Dashboard (June 2026)

Launched a public beta [[ConnectorObservability|observability dashboard]] for published MCP connectors, enabling developers to monitor connector performance (errors, latency) across all Claude product surfaces. The same launch enabled in-app connector directory submission directly within Claude's Organization Settings. Over 300 third-party connectors are in the directory, used by millions daily. See [[summary-2026-06-08 - Observability for developers building connectors]].

### Claude Tag and Agent Identity (June 2026)

Introduced [[ClaudeTag]], a "multiplayer AI" product where Claude sits in shared Slack channels alongside many people. Claude Tag uses an [[AgentIdentity|agent identity]] access model: Claude has its own service accounts (Slack app, GitHub App, warehouse service accounts) rather than borrowing user credentials. Admins define a baseline identity at the workspace level and override it per-channel. Each private channel gets a distinct identity; revocation terminates access everywhere. Written by Noah Zweben of the Claude Code team. Anthropic's internal experience found that value compounds with tool and context access -- each connected system makes every other one more useful. See [[summary-2026-06-24 - Agent identity in Claude Tag a new access model for autonomous, team-wide AI]].

### Enterprise-Managed Authorization for MCP Connectors (June 2026)

Launched [[EnterpriseManagedAuthorization|Enterprise-Managed Authorization (EMA)]], allowing organization admins to provision [[MCPConnector|MCP connectors]] centrally through their identity provider, starting with [[Okta]]. EMA collapses the two-step connector setup (admin enable + user authorize) into a single admin provisioning step, achieving zero-touch connector setup. Access is scoped by IdP groups/roles and consistent across Claude chat, [[ClaudeCode]], and [[ClaudeCowork]]. MCP providers supporting EMA at launch include [[Asana]], [[Atlassian]], [[Canva]], [[Figma]], [[Granola]], [[Linear]], and [[Supabase]] ([[Slack]] coming soon). Enterprise customers rolling out EMA include [[Hubspot]], [[Ramp]], and [[Webflow]]. Available in beta for Claude Team and Enterprise plans. See [[summary-2026-06-18 - Centrally manage authorization for MCP connectors]].

### Claude Opus 4.8 Build Day Hackathon (June 2026)

Held a 12-hour [[ClaudeOpus4.8]] Build Day hackathon in San Francisco on June 13, 2026, with 310 builders (selected from 1,500+ applicants), each with $500 in credits. Three winning teams were profiled:

- **[[Tekton]]** ([[HollyTang]], [[AustinBurgess]]): reconstructs historical buildings in 3D with 339 incremental construction states, using independent verifier sub-agents in isolated context windows and self-correction loops until all 20 tests passed. Uses [[EvidenceChain|evidence chains]] tracing every component back to documented sources.
- **[[SimFrancisco]]** ([[TanmayiPriyaDasari]], [[TejasPrabhune]]): 10,000 synthetic residents drawn from US Census data forecasting elections and tracking prediction markets. Used an evolutionary clustering algorithm to batch residents into ~300 personas, cutting inference cost 10-100x.
- **[[CustomUniverse]]** ([[JakeStevens]], [[MauricioPereira]]): phone-photo-to-3D object pipeline for robotics labs needing [[SyntheticData|synthetic training data]]. Claude operated a remote [[NVIDIAH100]] throughout the hackathon.

See [[summary-2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon]].

### Internal Use: Human-Agent Teams (June 2026)

Anthropic has been testing [[HumanAgentTeams|human-agent team]] practices internally for several months. Key internal patterns:

- **Working in public**: Teams default to internally public channels and docs within clearly defined security boundaries, so agents can learn from searchable text. Agents read decisions from team meetings, product specs beyond their own team, and enormous volumes of text to surface relevant work humans would have missed. See [[WorkingInPublic]].

- **Defined roles with rosters**: Engineering teams create rosters to codify human and agent roles. Different agents hold different roles (data analysis, design standards, research synthesis). Writing skill files to define agents' roles makes specialization easy, and teams add new agents as projects grow more complex (e.g., adding a release manager agent).

- **North star goals**: Humans set ambitious, wide-reaching goals and share them with agents. An internal tools team with a north star to "make product onboarding more helpful" saw an agent proactively recommend copy revisions that measurably increased onboarding success.

- **Building trust incrementally**: One engineering leader used agents to sort through a backlog — one set read items, determined ownership, and assigned complexity scores; another set created code changes for medium/low complexity items. Humans reviewed every decision initially, then taught agents to surface hard-tradeoff decisions directly to humans. Weekly "lessons & missteps" reports helped agents avoid repeating mistakes. Over time, agents handled increasingly complex changes. Agents were coached to treat human attention as a scarce resource: batch questions, repeat key context, limit what each human sees at once.

- **Guardrails**: Some teams set limits on how much work agents do per day, ensuring humans maintain important skills and the volume of items requiring human review stays sustainable.

See [[summary-2026-06-24 - Building effective human-agent teams]].

## Related

- [[Claude.ai]] — web application with conversational AI, code execution, and document analysis
- [[ClaudeCode]] — the developer tool
- [[summary-2026-05-12 - How Anthropic&#39;s cybersecurity team built a threat detection platform with Claude Code]] — CLUE detection-platform internal case study
- [[MultiAgentSystem]] — orchestrator-subagent pattern CLUE Investigate exemplifies
- [[ClaudeArtifacts]] — interactive artifact feature for building and sharing AI-powered apps
- [[ClaudeFable5]] — the latest frontier model
- [[ClaudeManagedAgents]] — the production agent platform
- [[AnthropicConsole]] — developer console for building with Claude
- [[Workspace]] — resource management and multi-environment deployment feature
- [[ClaudeTeamPlan]] — team collaboration subscription ($30/user/month, 5-seat minimum)
- [[ClaudeEnterprise]] — enterprise collaboration plan with 500K context window and GitHub integration
- [[ClaudeIOSApp]] — mobile application for iOS devices
- [[Claude2]] — earlier frontier model (2023), first Claude model on Amazon Bedrock at GA
- [[Claude3]] — third-generation Claude model family with tool use support
- [[Claude3Opus]] — flagship Claude 3 model with advanced reasoning and thinking tags
- [[Claude3Haiku]] — efficient Claude 3 variant for cost-sensitive workloads
- [[Claude3.5Sonnet]] — flagship Sonnet model with vision, multilingual, and reasoning capabilities
- [[Claude3.7Sonnet]] — most intelligent Claude model supporting government compliance
- [[Claude4]] — frontier model family with agentic capabilities
- [[Claude4Opus]] — flagship Claude 4 model with advanced reasoning
- [[Claude4Sonnet]] — capable Claude 4 variant
- [[ToolUse]] — Claude capability to interact with external tools and APIs
- [[CodeExecutionTool]] — API capability for Python code execution
- [[MCPConnector]] — API capability for automatic MCP server management
- [[FilesAPI]] — API capability for document storage and reuse
- [[Citations]] — API feature for grounding responses in source documents with precise citations
- [[AmazonBedrock]] — AWS managed service hosting Claude models
- [[GoogleCloud]] — cloud partner for government-compliant Claude deployments
- [[VertexAI]] — Google Cloud platform hosting Claude with FedRAMP High and DoD IL2 authorization
- [[ConstitutionalAI]] — Anthropic's training methodology
- [[summary-01 - Code with Claude Tokyo 2026： Opening Keynote]] — Tokyo 2026 keynote
- [[summary-2023-08-23 - Claude 2 on Amazon Bedrock]] — Claude 2 Amazon Bedrock launch announcement
- [[summary-2024-05-01 - Introducing the Claude Team plan and iOS app]] — Team Plan and iOS app announcement (May 2024)
- [[summary-2024-05-30 - Claude can now use tools]] — Tool use general availability announcement with enterprise case studies
- [[summary-2024-07-16 - Claude Android app]] — Claude Android app launch (July 2024)
- [[summary-2024-09-10 - Claude for Enterprise]] — Enterprise collaboration plan announcement (September 2024)
- [[summary-2024-09-10 - Workspaces in the Anthropic API Console]] — Workspaces feature for managing multiple Claude deployments
- [[summary-2024-10-24 - Introducing the analysis tool in Claude.ai]] — Code execution and data analysis capabilities in Claude.ai
- [[summary-2024-05-20 - Generate better prompts in the developer console]] — Prompt generator feature in Anthropic Console
- [[summary-2025-04-02 - Claude on Google Cloud’s Vertex AI FedRAMP High and IL2 Authorized]] — Government compliance announcement for federal and defense agencies
- [[summary-2025-05-22 - New capabilities for building agents on the Anthropic API]] — Announcement of code execution, MCP connector, Files API, and extended prompt caching
- [[summary-2025-07-25 - Build and share AI-powered apps with Claude]] — Interactive artifacts feature for building and sharing AI-powered apps
- [[summary-2025-07-24 - How Anthropic teams use Claude Code]] — real-world usage patterns of Claude Code across Anthropic teams
- [[summary-2025-09-09 - Claude can now create and edit files]] — file creation and editing capability announcement (GA October 2025)
- [[StudyFetch]] — AI tutoring platform using Claude tool use
- [[Intuned]] — browser automation platform using Claude tool use
- [[Hebbia]] — financial and legal services platform using Claude tool use
- [[PromptEngineering]] — discipline for designing effective Claude prompts
- [[ChainOfThoughtReasoning]] — reasoning technique for prompts
- [[ZoomInfo]] — case study of RAG application with Claude
- [[FedRAMP]] — federal compliance standard for civilian agencies
- [[DoD-IL2]] — defense compliance standard for contractors and agencies
- [[GovernmentAI]] — AI adoption in government with compliance requirements
- [[ClaudeCodeSkills]] — mechanism behind the legal team's four internal workflows
- [[ModelContextProtocol]] — connects the legal team's Claude workflows to Google Drive, JIRA, Slack, and Calendar
- [[summary-2025-12-08 - How Anthropic&#39;s legal team cut review times from days to hours with Claude]] — internal legal-team case study
- [[Figma]] — plugin platform used in the Growth Marketing case study
- [[summary-2026-01-26 - How Anthropic&#39;s Growth Marketing team cut ad creation time from 30 minutes to 30 seconds with Claude Code]] — internal Growth Marketing case study
- [[CodeWithClaude]] — Anthropic's developer conference (San Francisco, London, Tokyo)
- [[summary-2026-03-18 - Code with Claude comes to San Francisco, London, and Tokyo]] — 2026 conference expansion announcement
- [[summary-2026-04-02 - Harnessing Claude’s intelligence]] — harness-design patterns article (by Lance Martin, Claude Platform team)
- [[ProjectGlasswing]] — defensive-cybersecurity initiative using Claude Mythos Preview
- [[AIAcceleratedOffense]] — security-program playbook Anthropic published for the AI-accelerated-offense era
- [[summary-2026-04-10 - Preparing your security program for AI-accelerated offense]] — Project Glasswing security-guidance article
- [[AINativeStartup]] — founder-as-orchestrator concept and four-stage lifecycle framework from the Founder's Playbook
- [[summary-2026-05-14 - The founder&#39;s playbook Building an AI-native startup]] — Founder's Playbook announcement (May 2026)
- [[FionaFung]] — Director of Engineering for Claude Code and Claude Cowork
- [[AINativeEngineeringOrg]] — the organizational design principles for AI-native engineering teams
- [[JustInTimePlanning]] — the planning methodology replacing long-range roadmaps on AI-native teams
- [[summary-2026-06-03 - Running an AI-native engineering org]] — the blog article on the Claude Code team's org transformation
- [[summary-2026-06-05 - The Claude Cowork product guide]] — source article for the Claude Cowork product guide and knowledge-work-agent framing
- [[AIAcceleratedSalesWorkflows]] — the broader pattern of non-technical GTM staff building AI tools, exemplified by Jared Sires
- [[summary-2026-06-05 - How one Anthropic seller rebuilt his team's workflows with Claude Code]] — CLAFTS and GTM sales workflow case study
- [[ClaudeAPI]] — the API powering CLAFTS email drafts
- [[ClaudeCowork]] — the platform through which the Sales plugin is distributed to the team
- [[summary-2026-06-03 - How Anthropic enables self-service data analytics with Claude]] — internal data analytics case study
- [[AgenticAnalytics]] — the overarching paradigm of LLM-driven self-service business analytics
- [[AppleFoundationModels]] — Apple's native Swift framework for on-device AI that Claude now integrates with
- [[ModelHandoff]] — the pattern of escalating from on-device to cloud models
- [[summary-2026-06-08 - Building intelligent apps for Apple platforms with Claude in the Foundation Models framework]] — Apple Foundation Models integration announcement (June 2026)
- [[ConnectorObservability]] — public beta observability dashboard for MCP connectors
- [[summary-2026-06-08 - Observability for developers building connectors]] — connector observability and in-app directory submission announcement (June 2026)
- [[ClaudeTag]] — multiplayer AI product with agent identity access model
- [[AgentIdentity]] — the access model where agents have their own workspace-level credentials
- [[MultiplayerAI]] — the paradigm of AI in shared, team-wide channels
- [[summary-2026-06-24 - Agent identity in Claude Tag a new access model for autonomous, team-wide AI]] — Claude Tag agent identity blog post (June 2026)
- [[EnterpriseManagedAuthorization]] — enterprise-managed auth for MCP connectors
- [[summary-2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon]] — hackathon winners announcement (June 2026)
- [[ClaudeOpus4.8]] — the model featured in the Build Day hackathon
- [[Tekton]] — winning hackathon project: 3D historical building reconstruction
- [[SimFrancisco]] — winning hackathon project: synthetic San Francisco population
- [[CustomUniverse]] — winning hackathon project: phone-to-3D robotics data pipeline
- [[EvidenceChain]] — verification methodology used by Tekton
- [[SyntheticPopulation]] — concept underlying Sim Francisco
- [[SyntheticData]] — concept underlying Custom Universe
- [[Okta]] — first identity provider for EMA
- [[summary-2026-06-18 - Centrally manage authorization for MCP connectors]] — EMA launch announcement (June 2026)
- [[ClaudeDesktop]] — the unified desktop application (chat, Cowork, Code) announced for cloud deployment
- [[CloudInference]] — the pattern of running AI inference within the customer's own cloud
- [[summary-2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry]] — cloud Desktop deployment announcement (June 2026)
- [[HumanAgentTeams]] — the human-agent team collaboration model tested internally at Anthropic
- [[WorkingInPublic]] — the transparency practice Anthropic teams use to give agents context
- [[NorthStar]] — the goal-setting practice Anthropic teams use to guide agent proactivity
- [[DoerVerifier]] — the verification pattern Anthropic teams use to build trust in agent output
- [[summary-2026-06-24 - Building effective human-agent teams]] — source article on internal human-agent team practices
- [[summary-01 - How Anthropic uses Claude in GTM Engineering]] — source summary
- [[summary-02 - How Anthropic uses Claude in Cybersecurity]] — source summary
- [[summary-03 - How Anthropic uses Claude in Product Engineering]] — source summary
- [[summary-04 - How Anthropic uses Claude in Product Management]] — source summary
