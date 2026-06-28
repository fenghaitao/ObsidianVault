---
title: "Anthropic"
type: entity
tags: [company, ai, claude, platform]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - Japan/01 - Code with Claude Tokyo 2026： Opening Keynote.md, raw/01-articles/claude/2024-05-01 - Introducing the Claude Team plan and iOS app.md, raw/01-articles/claude/2024-09-10 - Claude for Enterprise.md, raw/01-articles/claude/2024-05-20 - Generate better prompts in the developer console.md, raw/01-articles/claude/2024-05-30 - Claude can now use tools.md, raw/01-articles/claude/2024-10-24 - Introducing the analysis tool in Claude.ai.md, raw/01-articles/claude/2025-03-13 - Token-saving updates on the Anthropic API.md, raw/01-articles/claude/2024-09-10 - Workspaces in the Anthropic API Console.md, raw/01-articles/claude/2025-06-23 - Introducing Citations on the Anthropic API.md, raw/01-articles/claude/2025-07-25 - Build and share AI-powered apps with Claude.md, raw/01-articles/claude/2025-07-24 - How Anthropic teams use Claude Code.md, raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md, raw/01-articles/claude/2025-09-09 - Claude can now create and edit files.md, raw/01-articles/claude/2025-09-24 - Claude is now available in Microsoft 365 Copilot.md]
last_updated: 2026-06-28
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

## Related

- [[Claude.ai]] — web application with conversational AI, code execution, and document analysis
- [[ClaudeCode]] — the developer tool
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
- [[summary-2024-09-10-Workspaces]] — Workspaces feature for managing multiple Claude deployments
- [[summary-2024-10-24 - Introducing the analysis tool in Claude.ai]] — Code execution and data analysis capabilities in Claude.ai
- [[summary-2024-05-20 - Generate better prompts in the developer console]] — Prompt generator feature in Anthropic Console
- [[summary-2025-04-02 - Claude on Google Cloud's Vertex AI FedRAMP High and IL2 Authorized]] — Government compliance announcement for federal and defense agencies
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
