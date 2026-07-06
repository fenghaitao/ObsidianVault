---
title: "Anthropic"
type: entity
tags: [company, ai, claude, platform]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - Japan/01 - Code with Claude Tokyo 2026： Opening Keynote.md, raw/01-articles/claude/2024-05-01 - Introducing the Claude Team plan and iOS app.md, raw/01-articles/claude/2024-09-10 - Claude for Enterprise.md, raw/01-articles/claude/2024-05-20 - Generate better prompts in the developer console.md, raw/01-articles/claude/2024-05-30 - Claude can now use tools.md, raw/01-articles/claude/2024-10-24 - Introducing the analysis tool in Claude.ai.md, raw/01-articles/claude/2025-03-13 - Token-saving updates on the Anthropic API.md, raw/01-articles/claude/2024-09-10 - Workspaces in the Anthropic API Console.md, raw/01-articles/claude/2025-06-23 - Introducing Citations on the Anthropic API.md, raw/01-articles/claude/2025-07-25 - Build and share AI-powered apps with Claude.md, raw/01-articles/claude/2025-07-24 - How Anthropic teams use Claude Code.md, raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md, raw/01-articles/claude/2025-09-09 - Claude can now create and edit files.md, raw/01-articles/claude/2025-09-24 - Claude is now available in Microsoft 365 Copilot.md, raw/01-articles/claude/2026-05-14 - The founder&#39;s playbook Building an AI-native startup.md]
last_updated: 2026-07-05
---

## Definition

Anthropic is an AI company that builds the Claude family of models and the Claude platform. It positions itself as a platform company, providing developers with the tools to build systems on top of Claude.

## Key Information

- Creator of Claude (Haiku, Sonnet, Opus, Fable, Mythos model families).
- All Claude 3 models support [[ToolUse|tool use]] (generally available as of May 2024), enabling Claude to interact with external APIs and tools.
- Platform includes Claude Code (developer agent), Claude Managed Agents (production agent infrastructure), the Claude API, [[ClaudeTeamPlan]] (team collaboration), , [[ClaudeEnterprise]] (enterprise collaboration with 500K context window and GitHub integration), and mobile apps ([[ClaudeIOSApp]], Android app).
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

Detection Platform Engineering Technical Lead Jackie Bow's team built [[ClaudeCode|Claude Code]]-powered CLUE ("Claude Looks Up Evidence"), a detection-and-response platform connecting Claude via tool use to Slack, internal docs, code repos, and data warehouses. CLUE Triage auto-dispositions alerts (false positive rate dropped ~33% → 7%); CLUE Investigate runs natural-language investigations via parallel sub-agent queries (3-4 minutes vs. hours-to-days manually). Over 30 days: ~12,000 queries, ~27,000 tool calls automated, an estimated 1,870 hours (234 person-days) of manual work saved, 5-10x time savings. See [[summary-2026-05-12 - How Anthropic's cybersecurity team built a threat detection platform with Claude Code]].

### Code with Claude Expansion (March 2026)

Runs [[CodeWithClaude]], its developer conference; expanded from San Francisco-only (2025) to San Francisco, London, and Tokyo for spring 2026, per [[summary-2026-03-18 - Code with Claude comes to San Francisco, London, and Tokyo]].

### Project Glasswing (April 2026)

Announced [[ProjectGlasswing]], putting the cybersecurity capabilities of its newest frontier model at the time, Claude Mythos Preview, to defensive use. Published prioritized security-program recommendations ([[AIAcceleratedOffense]]) for organizations bracing for AI-accelerated vulnerability discovery and exploitation. See [[summary-2026-04-10 - Preparing your security program for AI-accelerated offense]].

### The Founder's Playbook (May 2026)

Published "The Founder's Playbook: Building an AI-native startup," remapping the four startup lifecycle stages (Idea, MVP, Launch, Scale) for 2026-era AI capabilities, with goals, exit criteria, failure modes, and AI-powered exercises for each stage. Central thesis: AI is shifting the founder's role from individual contributor to orchestrator, letting founders with no coding background ship production applications and reach revenue before scaling headcount. See [[AINativeStartup]] and [[summary-2026-05-14 - The founder's playbook Building an AI-native startup]].

### Internal Use: Growth Marketing (January 2026)

Growth marketer Austin Lau (no prior coding experience) built a [[Figma]] plugin generating ad creative variants in one click and a Google Ads copy workflow (`/rsa` slash command) combining campaign data with [[ClaudeCodeSkills|Skills]] for brand tone/voice and RSA best practices — cutting ad creation from 30 minutes to 30 seconds. Broader marketing-org results: Influencer Marketing frees 100+ hours/month; Customer Marketing drafts case studies in 30 minutes instead of 2.5 hours; Digital Marketing lifted web-dev productivity 5x year-over-year; Product Marketing saves 5-10 hours per launch brief using Skills and Projects; Partner Marketing cut trade-show prep time 40%. See [[summary-2026-01-26 - How Anthropic&#39;s Growth Marketing team cut ad creation time from 30 minutes to 30 seconds with Claude Code]].

## Related

- [[Claude.ai]] — web application with conversational AI, code execution, and document analysis
- [[ClaudeCode]] — the developer tool
- [[summary-2026-05-12 - How Anthropic's cybersecurity team built a threat detection platform with Claude Code]] — CLUE detection-platform internal case study
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
- [[summary-2026-05-14 - The founder's playbook Building an AI-native startup]] — Founder's Playbook announcement (May 2026)
