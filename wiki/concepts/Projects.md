---
title: "Projects"
type: concept
tags: [claude-ai, projects, context, knowledge-base, rag]
sources: ["raw/01-articles/claude/2026-03-05 - Skills explained How Skills compares to prompts, Projects, MCP, and subagents.md", "raw/01-articles/claude/2026-05-22 - How Anthropic's finance team uses Claude to shape the narrative behind the numbers.md"]
last_updated: 2026-07-04
---

## Definition

Projects are self-contained Claude.ai workspaces (available on all paid plans) with their own chat histories and knowledge bases — persistent background knowledge and custom instructions that apply to every conversation within that project.

## Key Information

- Each project includes a 200K context window where users upload documents, add context, and set custom instructions applying project-wide.
- Everything uploaded to a project's knowledge base becomes available across all chats in that project; when project knowledge approaches context limits, Claude automatically enables [[RetrievalAugmentedGeneration|RAG]] mode to expand capacity up to 10x.
- **Use Projects for**: persistent background knowledge that should inform every conversation on an initiative, workspace organization (separate contexts per initiative), team collaboration (shared knowledge/history on Team and Enterprise plans), and project-specific tone/perspective via custom instructions.
- **Audience-specific projects**: In [[ClaudeCowork]], separate projects can be maintained for separate audiences (e.g., monthly review vs. board deck), since tone and conventions differ. Each project's memory preserves context that grows richer each cycle. [[AliceFong]] on Anthropic's corporate finance team uses this pattern to keep board-deck and monthly-review narratives distinct.
- **Projects vs. Skills**: Projects say "here's what you need to know" (static reference material always loaded); [[ClaudeCodeSkills|Skills]] say "here's how to do things" (dynamic, on-demand procedural expertise usable across any project or conversation). If the same instructions get copied across multiple Projects, that's a signal to extract them into a Skill instead.

## Related

- [[ClaudeCodeSkills]] — the on-demand procedural-expertise counterpart to Projects' static context
- [[RetrievalAugmentedGeneration]] — the technique automatically enabled as project knowledge grows
- [[ClaudeCowork]] — product where audience-specific projects are used for financial narrative workflows
- [[FinancialNarrative]] — concept where separate projects separate board deck and monthly review contexts
- [[AliceFong]] — Anthropic finance team member using audience-specific project separation
- [[summary-2026-03-05 - Skills explained How Skills compares to prompts, Projects, MCP, and subagents]] — source article
- [[summary-2026-05-22 - How Anthropic's finance team uses Claude to shape the narrative behind the numbers]] — source article for audience-specific project usage
